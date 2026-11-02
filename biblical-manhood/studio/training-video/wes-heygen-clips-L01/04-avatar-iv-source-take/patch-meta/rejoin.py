# rejoin.py PID..: per-frame landmark-centre + full-frame diff in edge zones (first/last 40 frames of the clip); pick join minimizing centre shift with mouths closed
import sys,json,cv2,numpy as np
sys.path.insert(0,'/workspace/artifacts/training/lipsync-tests-2026-10-26/scripts');import evaluate as E
fa=E.app();A={a['id']:a for a in json.load(open('accepted.json'))}
def lm(f,idx):
  c=cv2.VideoCapture(f);R={};i=0;S=set(idx)
  while True:
    ok,x=c.read()
    if not ok or i>max(idx):break
    if i in S:
      d=E.biggest(fa.get(x));R[i]=None if d is None else d.landmark_2d_106
    i+=1
  return R
out={}
for pid in sys.argv[1:]:
  a=A[pid];n=a['n'];o=json.load(open(f'orig-{pid}-perframe.json'))['frames'];q=json.load(open(f't1-{pid}-perframe.json'))['frames']
  zin=list(range(0,min(40,n//3)));zout=list(range(n-min(40,n//3),n));idx=zin+zout
  LO,LP=lm(f'orig_{pid}.mp4',idx),lm(f't1_{pid}.mp4',idx)
  def c(k):
    if LO[k] is None or LP[k] is None:return 1e9
    sh=float(np.abs(LO[k].mean(0)-LP[k].mean(0)).max())
    return sh+100*max(0,(o[k].get('gap') or 1)-0.08)+100*max(0,(q[k].get('gap') or 1)-0.08)
  bi=min(zin,key=c);bo=min(zout,key=c)
  out[pid]=dict(i_in=bi,i_out=bo,c_in=round(c(bi),1),c_out=round(c(bo),1),old=[a['i_in'],a['i_out']])
  print(pid,out[pid],flush=True)
json.dump(out,open('rejoin_'+sys.argv[1]+'.json','w'))
