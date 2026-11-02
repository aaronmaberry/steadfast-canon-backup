import json,subprocess,numpy as np,random
def fr(f,t0,n):
  r=subprocess.run(['ffmpeg','-v','error','-ss',f'{t0:.3f}','-i',f,'-frames:v',str(n),'-vf','scale=480:270','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True).stdout
  return np.frombuffer(r,np.uint8).reshape(-1,270,480).astype(np.float32)
def maxd(F):return float(np.abs(np.diff(F,axis=0)).mean((1,2)).max())
O='../L01-P5-FULL-burg_a-4c7713cd.mp4';P='../L01-P5-PATCHED-v1.mp4';out=[]
for a in json.load(open('accepted.json')):
  s0=round(a['s']*25)
  for k,g in (('in',s0+a['i_in']),('out',s0+a['i_out'])):
    t=(g-8)/25;out.append(dict(id=a['id'],edge=k,t=round(g/25,2),patched=round(maxd(fr(P,t,16)),2),orig=round(maxd(fr(O,t,16)),2)))
random.seed(1);W=json.load(open('windows.json'));pz=[]
import soundfile as sf
while len(pz)<5:
  t=random.uniform(30,1220)
  if any(w['s']-1<t<w['e']+1 for w in W):continue
  pz.append(t);out.append(dict(id='rand',edge='pause',t=round(t,2),patched=round(maxd(fr(P,t,16)),2),orig=round(maxd(fr(O,t,16)),2)))
for o in out:print(o)
json.dump(out,open('pops.json','w'),indent=1)
