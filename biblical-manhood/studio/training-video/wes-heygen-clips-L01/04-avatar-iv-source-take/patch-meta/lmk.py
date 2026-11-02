# lmk.py PID...: similarity-aligned landmark residual (non-mouth 106-pt, normalized by face w) per frame, orig vs t1, every 2nd frame
import sys,json,cv2,numpy as np
sys.path.insert(0,'/workspace/artifacts/training/lipsync-tests-2026-10-26/scripts');import evaluate as E
fa=E.app()
MOUTH=set(range(52,72))
def L(f):
  c=cv2.VideoCapture(f);R=[];i=0
  while True:
    ok,x=c.read()
    if not ok:break
    if i%2==0:
      d=E.biggest(fa.get(x));R.append(None if d is None else d.landmark_2d_106.astype(np.float64))
    else:R.append(None)
    i+=1
  return R
def proc(A,B):
  A=A-A.mean(0);B=B-B.mean(0);s=np.linalg.norm(A);A/=s;B/=np.linalg.norm(B)
  U,_,Vt=np.linalg.svd(B.T@A);Rm=U@Vt;return float(np.linalg.norm(B@Rm-A,axis=1).mean()*1000)
keep=[k for k in range(106) if k not in MOUTH]
for pid in sys.argv[1:]:
  a=json.load(open('accepted.json'));a={x['id']:x for x in a}[pid]
  O,P=L(f'orig_{pid}.mp4'),L(f't1_{pid}.mp4')
  # reference: median landmark shape of original over window
  ok=[o for o in O if o is not None];ref=np.median(np.stack(ok),0)[keep]
  ro=[];rp=[];jump=[]
  for k in range(a['i_in']+a['i_in']%2,a['i_out']+1,2):
    if O[k] is not None and P[k] is not None:
      ro.append(proc(ref,O[k][keep]));rp.append(proc(ref,P[k][keep]))
  for k in (a['i_in'],a['i_out']):
    kk=k-k%2
    if O[kk] is not None and P[kk] is not None: jump.append(float(np.abs(O[kk][keep].mean(0)-P[kk][keep].mean(0)).max()))
  ro,rp=np.array(ro),np.array(rp)
  r=dict(id=pid,o_p95=round(np.percentile(ro,95),2),p_p95=round(np.percentile(rp,95),2),o_max=round(ro.max(),2),p_max=round(rp.max(),2),p_frac_over_omax=round(float((rp>ro.max()).mean()),3),join_center_px=[round(j,1) for j in jump])
  print(json.dumps(r),flush=True)
