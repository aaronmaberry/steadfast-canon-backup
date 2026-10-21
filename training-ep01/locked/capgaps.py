# shrink uncontrolled (mid-line) silences longer than CAP; shift events accordingly
import numpy as np, json, sys, wave, subprocess
SR=44100; inp,out=sys.argv[1],sys.argv[2]; CAP=0.75; NEW=0.6
def load(p):
    raw=subprocess.run(["ffmpeg","-loglevel","error","-i",p,"-f","f32le","-ac","1","-ar",str(SR),"-"],capture_output=True).stdout
    return np.frombuffer(raw,np.float32).copy()
x=load(inp); ctrl=json.load(open(inp+'.ctrl.json')); ev=json.load(open(inp+'.events.json'))
hop=441; n=len(x)//hop
db=20*np.log10(np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2))+1e-9 for i in range(n)]))
thr=np.percentile(db,90)-45; q=db<thr
cuts=[];i=0
while i<n:
    if q[i]:
        j=i
        while j<n and q[j]: j+=1
        L=(j-i)/100; t0=i/100
        near=any(t0-0.3<=c<=t0+0.3+L for c in ctrl)
        if L>CAP and not near and i>10 and j<n-10:
            # remove middle, keep 0.06 head and 0.35 tail (breath)
            a=i*hop+int(SR*0.15); b=j*hop-int(SR*0.30); rem=(b-a)-int(SR*(NEW-0.45))
            if rem>0: cuts.append((a,a+rem)); print("cap %.2fs at %.1f -> %.2f"%(L,t0,NEW))
        i=j
    else: i+=1
parts=[];pos=0;removed=[]
f=int(SR*0.012)
for a,b in cuts:
    p=x[pos:a].copy(); p[-f:]*=np.linspace(1,0,f); parts.append(p); pos=b; removed.append((a/SR,(b-a)/SR))
    x[b:b+f]*=np.linspace(0,1,f)
parts.append(x[pos:]); y=np.concatenate(parts)
def shift(t): return t-sum(d for a,d in removed if a<t)
json.dump([(k,shift(t)) for k,t in ev],open(out+'.events.json','w'))
w=wave.open(out,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes());w.close()
print("dur %.1f"%(len(y)/SR))
