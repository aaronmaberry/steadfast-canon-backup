# assemble_v5.py (no-date slate, 2026-10-03 evening CT): assemble_v4 with Wes's dated slate line (L10 "Tuesday, January fifth,
#   twenty twenty-seven.") dropped. Aaron's rule: the slate says the number and title only. L9 "Episode one," and L11 "The Man
#   You Keep Saying You'll Be." come from the same continuous Jonathon take (O1J, read with 0.28 s of silence between them), so
#   they now sit together with a short natural pause. The random gap stream is kept identical so every later gap is unchanged.
# assemble_v4.py (polish pass, 5:05 PM CT): v3 + tighter cold open, 3 s sting slot, 0.6 s laugh gaps, closing-music gap.
# assemble.py : build E001 dialogue track from per-line takes.
# Steps per line: pick take -> energy trim -> Wes tempo (atempo WSOLA) -> sentence-gap widening -> loudness match -> place with turn gaps.
import json,glob,os,re,subprocess,random
import numpy as np, wavio
random.seed(1604)
SR=44100
TEMPO={'WES':0.90,'JONATHON':1.0}        # Wes rendered at ~229 wpm vs "lower, slower, drier" spec
SENT_ADD={'WES':0.28,'JONATHON':0.08}   # extra pause at sentence ends inside a line (s)
TARGET={'WES':-20.0,'JONATHON':-20.0}   # active-speech RMS target (dBFS) before master
EQ={'O1W':'highshelf=f=8000:g=-4','P1W':'highshelf=f=8000:g=-4'}
COLD_TEMPO={2:0.95}                     # polish: Wes's cold-open line a touch quicker than his body pace
COLD_PAUSE={1:(28,[0.20]),3:(32,[0.30,0.25])}  # polish: (detect dB below active level, target pause lengths). L1 "615, / on purpose" 0.27 s; L3 "lot. / Then" 0.54 s and "goes, / Since" 0.35 s
STING_GAP=0.25; STING_LEN=3.0; STING_OVERLAP=0.4
SKIP={10}                               # v5: the dated slate line, cut
SLATE_GAP=0.36                          # v5: L9 -> L11 placed gap, about 0.5 s speech to speech (raw take had 0.28 s)
CLOSE_GAP=3.9                           # L295 end -> credits: 0.6 s to the final chord, about 3 s of ring and fade, 0.3 s clean
PICK={113:'R1',239:'S404'}              # v1-numbered body picks: R1 retake; S404 = line 404 with the new "I wrote it." spliced in
# v3 (3:20 PM CT approval): new open + slate, Wes body pickups, credits line, Jonathon retake of "What's the something?"
V3={4:'O1W',6:'O1W',8:'O1W',10:'O1W',5:'O1J',7:'O1J',9:'O1J',11:'O1J',1:'I1J',3:'I1J',
    72:'P1W',240:'P1W',254:'P1W',285:'P1W',296:'P1W',148:'R3J'}
L={l['n']:l for l in json.load(open('lines_v3.json'))}
C={c['id']:c for c in json.load(open('chunks.json'))}
src1={}
for c in C.values():
    if not c.get('retake'):
        for n in c['lines']: src1[n]=c['id']
for n,k in PICK.items(): src1[n]=k
def v1n(n): return {2:5}.get(n, n-4 if 12<=n<=295 else None)
src={}   # v3 n -> (take, n inside that take's split)
for n in L:
    if n in V3: src[n]=(V3[n],n)
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
timeline=[]; pieces=[]; t=0.0; ABRUPT=[]
def add(x):
    global t; pieces.append(x.astype(np.float32)); t+=len(x)/SR
def sil(d): add(np.zeros(int(round(d*SR)),np.float32))
order=sorted(L)
prev_spk=None
log=[]
for i,n in enumerate(order):
    if n in SKIP:
        random.uniform(0.32,0.55)   # the draw L10 used in v4, so every later gap stays the same
        continue
    l=L[n]; spk=l['spk']; k,sn=src[n]; r=rep(k,sn)
    sr,ch=wavio.read(f'lines/L{sn:03d}.{k}.wav')
    if k in EQ:   # tone match: the 3:23 PM takes carry ~2-3 dB more 8-16 kHz air on vowels than the body takes
        wavio.write('/tmp/_eqin.wav',SR,ch)
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i','/tmp/_eqin.wav','-af',EQ[k],'/tmp/_eqout.wav'],check=True)
        ch=wavio.read('/tmp/_eqout.wav')[1]
    ws=[(w[0],w[1]-r['t0'],w[2]-r['t0']) for w in words_in(k,r)]
    a,off=trim(ch); ws=[(w,s-off/SR,e-off/SR) for w,s,e in ws]
    # take-end guard: v3 files can stop while the last word is still decaying (-30 to -45 dB). A 50 ms fade stops a step or click.
    if frames_db(a[-441:])[-1]>-50:
        nf=int(0.05*SR); a=a.copy(); a[-nf:]*=np.cos(np.linspace(0,np.pi/2,nf)).astype(np.float32); ABRUPT.append((n,k))
    tp=COLD_TEMPO.get(n,TEMPO[spk]); a=atempo(a,tp); ws=[(w,s/tp,e/tp) for w,s,e in ws]
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
    if n in COLD_PAUSE:
        db=frames_db(a,441); thr=active_rms(a)-COLD_PAUSE[n][0]; low=db<thr; runs=[]; j=0
        while j<len(low):
            if low[j]:
                k2=j
                while k2<len(low) and low[k2]: k2+=1
                if (k2-j)*0.01>=0.25 and j>5 and k2<len(low)-5: runs.append((j*441,k2*441))
                j=k2
            else: j+=1
        print('L%d internal pauses found:'%n,[(round(p/SR,2),round((q-p)/SR,2)) for p,q in runs])
        assert len(runs)==len(COLD_PAUSE[n][1]), runs
        segs=[]; last=0; cut=[]
        for (p,q),tgt in zip(runs,COLD_PAUSE[n][1]):
            keep=int(tgt*SR); mid0=p+keep//2; mid1=q-(keep-keep//2)
            nf=int(0.01*SR); x=a[last:mid0].copy(); segs.append(x); last=mid1; cut.append((mid0/SR,(mid1-mid0)/SR))
        segs.append(a[last:]); a=np.concatenate(segs)
        for p,d in sorted(cut,reverse=True): ws=[(w,s_-(d if s_>p else 0),e_-(d if e_>p else 0)) for w,s_,e_ in ws]
        print('L%d pauses cut by'%n,[round(d,2) for p,d in cut])
    # loudness: full speaker offset, half per-line correction (keep some natural dynamics), clamp
    lv=active_rms(a); g=TARGET[spk]-lv; g=float(np.clip(g,-8,10)); a=a*10**(g/20)
    # gap before line
    if i==0: gap=0.15
    else:
        base=random.uniform(0.32,0.55) if spk!=prev_spk else random.uniform(0.45,0.6)
        gap=min(1.7,base+l["pre"])+l["lead"]
        gap=min(gap,1.7)
        if n==2: gap=0.5                                   # Wes's scripted beat (was 0.93)
        if n==3: gap=0.3                                   # (was 0.50)
        if n==4: gap=STING_GAP+STING_LEN-STING_OVERLAP     # sting after "1604?", the open starts on its ring-out
        if 'laugh' in l.get('pre_reason',[]): gap=0.6      # no canned laughs: 0.6 s of room tone
        if n==296: gap=CLOSE_GAP
        if n==11: gap=SLATE_GAP
    sil(gap)
    t0=t; add(a); t1=t
    timeline.append(dict(n=n,spk=spk,take=k,start=round(t0,3),end=round(t1,3),chapter=l.get('chapter'),ch=l.get('ch'),gain=round(g,2),
                         words=[(w,round(t0+s,3),round(t0+e,3)) for w,s,e in ws]))
    prev_spk=spk
sil(0.6)   # short natural tail after the credits line
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
T={x['n']:x for x in timeline}
cues=dict(sting_start=round(T[3]['end']+STING_GAP,3),sting_len=STING_LEN,l295_end=T[295]['end'],credits_start=T[296]['start'],end=round(len(y)/SR,3),
          cold_open_s=round(T[3]['end'],3),laughs=[(x['n'],round(x['start']-T[x['n']-1]['end'],3)) for x in timeline if 'laugh' in L[x['n']].get('pre_reason',[])])
json.dump(cues,open('out/music_cues.json','w'),indent=1); print('cues',cues)
print('faded line ends',ABRUPT)
print('runtime',round(len(y)/SR,1),'s =',round(len(y)/SR/60,2),'min; lines',len(timeline))
