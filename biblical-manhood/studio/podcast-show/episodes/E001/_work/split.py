# split.py CHUNK_ID : transcribe raw/<K>.mp3 with word timestamps, align to the known line texts, cut per line.
import json,sys,re,subprocess,os,difflib
os.environ.setdefault('MKL_ENABLE_INSTRUCTIONS','AVX2'); os.environ.setdefault('ONEDNN_MAX_CPU_ISA','AVX2'); os.environ.setdefault('CT2_FORCE_CPU_ISA','AVX2')
from faster_whisper import WhisperModel
K=sys.argv[1]
C={c['id']:c for c in json.load(open('chunks.json'))}[K]
L={i['n']:i for i in json.load(open(os.environ.get('LINES','lines.json')))}
src=f'raw/{K}.mp3'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-ac','1','-ar','44100',f'raw/{K}.wav'],check=True)
cache=f'raw/{K}.words.json'
if os.path.exists(cache): words=[tuple(w) for w in json.load(open(cache))]
else:
  m=WhisperModel('medium.en',device='cpu',compute_type='int8',cpu_threads=8)
  segs,_=m.transcribe(f'raw/{K}.wav',word_timestamps=True,language='en',beam_size=5,vad_filter=False,condition_on_previous_text=False)
  words=[]
  for s in segs:
    for w in s.words: words.append((w.word.strip(),w.start,w.end))
  json.dump(words,open(cache,'w'))
from qa import norm
hyp=[norm(w[0]) for w in words]
hyp_flat=[]; hyp_idx=[]
for k,h in enumerate(hyp):
    for x in h: hyp_flat.append(x); hyp_idx.append(k)
ref=[]; ref_line=[]
for n in C['lines']:
    for x in norm(L[n]['tts']): ref.append(x); ref_line.append(n)
sm=difflib.SequenceMatcher(None,ref,hyp_flat,autojunk=False)
r2h={}
for a,b,size in sm.get_matching_blocks():
    for j in range(size): r2h[a+j]=hyp_idx[b+j]
res={}
for n in C['lines']:
    idx=[r for r in range(len(ref)) if ref_line[r]==n]
    hits=[r2h[r] for r in idx if r in r2h]
    res[n]=dict(first=min(hits) if hits else None,last=max(hits) if hits else None,cov=len(hits)/len(idx))
# cut points: midpoint of gap between last word of line i and first word of line i+1 (refined to quietest 10ms)
import numpy as np
import wavio
sr,a=wavio.read(f'raw/{K}.wav')
def quietest(t0,t1):
    i0,i1=int(t0*sr),int(t1*sr)
    if i1-i0<int(0.02*sr): return (t0+t1)/2
    win=int(0.01*sr); seg=a[i0:i1]; e=[np.sqrt(np.mean(seg[k:k+win]**2)) for k in range(0,len(seg)-win,win//2)]
    return t0+ (int(np.argmin(e))*(win//2)+win/2)/sr
ns=C['lines']; bounds=[0.0]
for x,y in zip(ns,ns[1:]):
    le=words[res[x]['last']][2] if res[x]['last'] is not None else None
    fs=words[res[y]['first']][1] if res[y]['first'] is not None else None
    if le is None or fs is None: bounds.append(None); continue
    bounds.append(quietest(le,fs) if fs>le+0.06 else quietest(min(le,fs)-0.12,max(le,fs)+0.08))
bounds.append(len(a)/sr)
os.makedirs('lines',exist_ok=True)
report=[]
for k,n in enumerate(ns):
    t0,t1=bounds[k],bounds[k+1]
    gap=None
    if k+1<len(ns) and res[ns[k]]['last'] is not None and res[ns[k+1]]['first'] is not None:
        gap=round(words[res[ns[k+1]]['first']][1]-words[res[ns[k]]['last']][2],2)
    if t0 is None or t1 is None: report.append(dict(n=n,cov=res[n]['cov'],err='nobound')); continue
    wavio.write(f'lines/L{n:03d}.{K}.wav',sr,a[int(t0*sr):int(t1*sr)])
    report.append(dict(n=n,cov=round(res[n]['cov'],3),t0=round(t0,2),t1=round(t1,2),gap_after=gap))
json.dump(dict(K=K,words=words,report=report),open(f'raw/{K}.split.json','w'))
for r in report: print(r)
