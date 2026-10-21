# words.py in.audio out.json : word timestamps via faster-whisper medium.en,
# transcribed in ~20s chunks cut at quiet points (full-file runs silently skip audio on v4 takes).
import sys,json,re,subprocess,tempfile,os
import numpy as np
from faster_whisper import WhisperModel
norm=lambda w: re.sub(r"[^a-z0-9']","",w.lower().replace("\u2019","'"))
sr=16000
pcm=subprocess.run(["ffmpeg","-loglevel","error","-i",sys.argv[1],"-ar",str(sr),"-ac","1","-f","s16le","-"],capture_output=True).stdout
a=np.frombuffer(pcm,np.int16).astype(np.float32)/32768
hop=sr//100; e=np.array([np.sqrt(np.mean(a[i:i+hop]**2)+1e-12) for i in range(0,len(a),hop)])
cuts=[0]; T=len(a)/sr
while cuts[-1]+24<T:
    lo,hi=int((cuts[-1]+16)*100),int((cuts[-1]+24)*100)
    w=np.convolve(e[lo:hi],np.ones(15)/15,'same'); cuts.append((lo+int(np.argmin(w)))/100)
cuts.append(T)
m=WhisperModel("medium.en",device="cpu",compute_type="int8")
out=[]
for s0,s1 in zip(cuts,cuts[1:]):
    seg=a[int(s0*sr):int(s1*sr)]
    def run(**k):
        segs,_=m.transcribe(seg,word_timestamps=True,beam_size=5,condition_on_previous_text=False,**k)
        return [(norm(w.word),w.start+s0,w.end+s0) for s in segs for w in s.words if norm(w.word)]
    def bad(ws):
        t=[x[0] for x in ws]
        from collections import Counter
        g=Counter(tuple(t[i:i+4]) for i in range(max(0,len(t)-3)))
        return len(t)<(s1-s0)*1.0 or any(len(set(t[i:i+5]))==1 for i in range(max(0,len(t)-4))) or (g and max(g.values())>=3)
    ws=run(temperature=0)
    if bad(ws):
        alt=run()
        if not bad(alt) or len(set(x[0] for x in alt))>len(set(x[0] for x in ws)): ws=alt
    out+=ws
json.dump(out,open(sys.argv[2],'w'))
