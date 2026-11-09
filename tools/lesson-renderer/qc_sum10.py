"""qc_sum.py cfg mp_glob arc.json asr.json master.mp4 out.json : summarise P8 metrics."""
import sys,json,glob,numpy as np,subprocess,re
from collections import Counter,defaultdict
cfg,MPG,ARC,ASR,MASTER,OUT=sys.argv[1:7]
C=json.load(open(cfg));E=json.load(open(C['edl']))
R=[];[R.extend(json.load(open(f))) for f in sorted(glob.glob(MPG))]
S={}
lay=defaultdict(list)
for r in R:lay[r['lay']].append(r)
for k,v in lay.items():
    hands=[r for r in v if r.get('hands')];jut=[r for r in v if r.get('dz',0)<-150]
    S[k]=dict(samples=len(v),wes_on_s=round(len(v)*10/25,1),hand_s=round(len(hands)*10/25,2),hand_times=sorted({round(r['n']/25,1) for r in hands})[:60],jut_frames=len(jut)*10,jut_times=sorted({round(r['n']/25) for r in jut})[:60])
# smears / jumps
sh=[r for r in R if r.get('sharp')];flags=[]
for k,v in lay.items():
    v=[r for r in v if r.get('sharp')];med=np.median([r['sharp'] for r in v]) if v else 0
    for a,b in zip(v,v[1:]):
        if b["n"]-a["n"]==10 and 'cx' in a and 'cx' in b:
            j=((a['cx']-b['cx'])**2+(a['cy']-b['cy'])**2)**0.5
            if j>12*(b['fw']/330 if k!='BUBBLE' else 1):flags.append(dict(t=round(b['n']/25,2),lay=k,type='jump',px=round(j,1)))
    for r in v:
        if r['sharp']<0.5*med:flags.append(dict(t=round(r['n']/25,2),lay=k,type='smear',ratio=round(r['sharp']/med,2)))
S['flags']=flags
A=[a for a in json.load(open(ARC)) if a['arc'] is not None] if ARC!='-' else []
for k in ('WIDE','PANEL','BUBBLE'):
    x=np.array([a['arc'] for a in A if a['lay']==k])
    if len(x):S.setdefault(k,{})['arc']=dict(n=len(x),mean=round(float(x.mean()),4),p10=round(float(np.percentile(x,10)),4),min=round(float(x.min()),4),below090=int((x<0.9).sum()))
if ASR!='-':a=json.load(open(ASR));S['asr']=dict(week_hits=a['week_hits'],words=a['words'],dur=a['dur'])
ld=subprocess.run(['ffmpeg','-nostdin','-hide_banner','-i',MASTER,'-map','0:a','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
m=re.findall(r'I:\s+(-?[\d.]+) LUFS',ld);lra=re.findall(r'LRA:\s+([\d.]+) LU',ld);tp=re.findall(r'Peak:\s+(-?[\d.]+) dBFS',ld)
S['loudness']=dict(I=float(m[-1]) if m else None,LRA=float(lra[-1]) if lra else None,TP=float(tp[-1]) if tp else None)
W=json.load(open(C['out'].replace('.json','_words.json')));sp=W[-1]['end']-W[0]['start'];S['pace']=dict(words=len(W),speech_s=round(sp,1),wpm=round(len(W)/sp*60,1))
mix=Counter(c['type'] for c in E['cuts'])+Counter(r['tin'] for r in E['broll'])+Counter(r['tout'] for r in E['broll'])
for k in E['kinetic']:mix[k.get('in','xfade')]+=1;mix[k.get('out','xfade')]+=1  # match build_l07 edge_counts
tot=sum(mix.values());S['transitions']=dict(total=tot,mix={k:[v,round(100*v/tot,1)] for k,v in mix.most_common()})
S['broll']=dict(count=len(E['broll']),unique_clips=len({r['clip'] for r in E['broll']}),secs=round(sum(r['t1']-r['t0'] for r in E['broll']),1),kinetic=len(E['kinetic']))
# B-roll edges inside words
Wd=W;inw=[]
for r in E['broll']:
    for t in (r['t0'],r['t1']):
        if any(w['start']+0.02<t<w['end']-0.02 for w in Wd):inw.append(round(t,2))
S['broll']['edges_inside_word']=inw
# shot transitions inside words
S['cuts_inside_word']=[round(c['cut'],2) for c in E['cuts'] if any(w['start']+0.02<c['cut']<w['end']-0.02 for w in Wd)]
json.dump(S,open(OUT,'w'),indent=1);print(json.dumps({k:v for k,v in S.items() if k!='flags'},indent=0)[:3000]);print('flags',len(flags))
