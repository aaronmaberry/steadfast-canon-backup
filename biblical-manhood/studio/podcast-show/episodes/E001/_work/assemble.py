# assemble.py : build E001 dialogue track from per-line takes.
# Steps per line: pick take -> energy trim -> Wes tempo (atempo WSOLA) -> sentence-gap widening -> loudness match -> place with turn gaps.
import json,glob,os,re,subprocess,random
import numpy as np, wavio
random.seed(1604)
SR=44100
TEMPO={'WES':0.90,'JONATHON':1.0}        # Wes rendered at ~229 wpm vs "lower, slower, drier" spec
SENT_ADD={'WES':0.28,'JONATHON':0.08}   # extra pause at sentence ends inside a line (s)
TARGET={'WES':-20.0,'JONATHON':-20.0}   # active-speech RMS target (dBFS) before master
PICK={113:'R1'}                          # v1-numbered retakes chosen; everything else = first-pass take
INTRO={1:'I1J',3:'I1J',5:'I1J',7:'I1J',4:'I1W',6:'I1W',8:'I1W'}   # v2 opening re-record (10:40 AM script)
import os
INTRO.update(json.load(open('intro_pick.json')) if os.path.exists('intro_pick.json') else {})
INTRO={int(k):v for k,v in INTRO.items()}
L={l['n']:l for l in json.load(open('lines_v2.json'))}
C={c['id']:c for c in json.load(open('chunks.json'))}
src1={}
for c in C.values():
    if not c.get('retake'):
        for n in c['lines']: src1[n]=c['id']
for n,k in PICK.items(): src1[n]=k
def v1n(n): return {2:5,9:2,10:3}.get(n, n-3 if n>=11 else None)
src={}   # v2 n -> (take, n inside that take's split)
for n in L:
    if n in INTRO: src[n]=(INTRO[n],n)
    else: m=v1n(n); src[n]=(src1[m],m)
SPL={k:json.load(open(f'raw/{k}.split.json')) for k in set(v[0] for v in src.values())}
def rep(k,n): return [r for r in SPL[k]['report'] if r['n']==n][0]
def words_in(k,r): return [w for w in SPL[k]['words'] if r['t0']<=(w[1]+w[2])/2<r['t1']]
def frames_db(a,win=441):
    n=len(a)//win; x=a[:n*win].reshape(n,win); return 20*np.log10(np.sqrt((x**2).mean(1))+1e-9)
def trim(a):
    db=frames_db(a); act=np.where(db>-48)[0]
    if len(act)==0: return a,0
    s=max(0,act[0]*441-int(0.04*SR)); e=min(len(a),(act[-1]+1)*441+int(0.10*SR))
    return a[s:e],s
def atempo(a,t):
    if abs(t-1)<1e-3: return a
    wavio.write('/tmp/_in.wav',SR,a)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i','/tmp/_in.wav','-af',f'atempo={t}','/tmp/_out.wav'],check=True)
    return wavio.read('/tmp/_out.wav')[1]
def quiet_point(a,t0,t1):
    i0,i1=int(t0*SR),int(t1*SR)
    if i1-i0<int(0.03*SR): return int((i0+i1)/2)
    db=frames_db(a[i0:i1],220); return i0+int(np.argmin(db))*220+110
def active_rms(a):
    db=frames_db(a); g=db[db>-45]
    return 10*np.log10(np.mean(10**(g/10))) if len(g) else -60
timeline=[]; pieces=[]; t=0.0
def add(x):
    global t; pieces.append(x.astype(np.float32)); t+=len(x)/SR
def sil(d): add(np.zeros(int(round(d*SR)),np.float32))
order=sorted(L)
prev_spk=None
log=[]
for i,n in enumerate(order):
    l=L[n]; spk=l['spk']; k,sn=src[n]; r=rep(k,sn)
    sr,ch=wavio.read(f'lines/L{sn:03d}.{k}.wav')
    ws=[(w[0],w[1]-r['t0'],w[2]-r['t0']) for w in words_in(k,r)]
    a,off=trim(ch); ws=[(w,s-off/SR,e-off/SR) for w,s,e in ws]
    tp=TEMPO[spk]; a=atempo(a,tp); ws=[(w,s/tp,e/tp) for w,s,e in ws]
    # inserts: sentence ends (+SENT_ADD) and scripted mid-line beats (+0.6)
    ins=[]
    for j in range(len(ws)-1):
        w,s,e=ws[j]; nxt=ws[j+1]
        extra=0
        if re.search(r'[.?!]["”]?$',w): extra=SENT_ADD[spk]
        if 'not that bad' in l['text'] and re.sub(r'\W','',w).lower()=='bad' and j+1<len(ws): extra=max(extra,0.6)
        if l['text'].startswith('Yeah. That one') and j==0 and re.sub(r'\W','',w).lower()=='yeah': extra=max(extra,0.6)
        if extra>0 and nxt[1]>e-0.05:
            ins.append((quiet_point(a,max(0,e-0.02),max(e+0.01,nxt[1]+0.02)),extra))
    segs=[]; last=0
    for p,d in sorted(ins):
        segs.append(a[last:p]); segs.append(np.zeros(int(d*SR),np.float32)); last=p
    segs.append(a[last:]); a=np.concatenate(segs)
    # loudness: full speaker offset, half per-line correction (keep some natural dynamics), clamp
    lv=active_rms(a); g=TARGET[spk]-lv; g=float(np.clip(g,-8,10)); a=a*10**(g/20)
    # gap before line
    if i==0: gap=0.6
    else:
        base=random.uniform(0.32,0.55) if spk!=prev_spk else random.uniform(0.45,0.6)
        gap=min(1.7,base+l["pre"])+l["lead"]
        gap=min(gap,1.7)
    sil(gap)
    t0=t; add(a); t1=t
    timeline.append(dict(n=n,spk=spk,take=k,start=round(t0,3),end=round(t1,3),chapter=l.get('chapter'),ch=l.get('ch'),gain=round(g,2),
                         words=[(w,round(t0+s,3),round(t0+e,3)) for w,s,e in ws]))
    prev_spk=spk
sil(1.5)
y=np.concatenate(pieces)
# room tone bed: very low filtered noise so gaps never drop to digital zero
rng=np.random.default_rng(7); nz=rng.normal(0,1,len(y)).astype(np.float32)
from numpy.fft import rfft,irfft
# cheap pink-ish: integrate + highpass via moving average difference
nz=np.cumsum(nz); nz-=np.convolve(nz,np.ones(2205)/2205,mode='same'); nz/=np.sqrt((nz**2).mean())+1e-9
y=y+nz*10**(-72/20)
os.makedirs('out',exist_ok=True)
y.astype('<f4').tofile('out/dialogue.f32'); subprocess.run(['ffmpeg','-y','-loglevel','error','-f','f32le','-ar',str(SR),'-ac','1','-i','out/dialogue.f32','-c:a','pcm_f32le','out/dialogue.wav'],check=True)
json.dump(timeline,open('out/timeline.json','w'))
print('runtime',round(len(y)/SR,1),'s =',round(len(y)/SR/60,2),'min; lines',len(timeline))
