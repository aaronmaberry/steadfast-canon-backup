# warp.py PID: non-rigid optical-flow residual in face box (upper face excl. mouth), orig vs t1, per frame; plus head-center pops
import cv2,json,sys,numpy as np
def run(f,cx):
  c=cv2.VideoCapture(f);prev=None;R=[];P=[]
  while True:
    ok,x=c.read()
    if not ok:break
    g=cv2.cvtColor(x[150:600,cx-230:cx+230],cv2.COLOR_BGR2GRAY);g=cv2.resize(g,(230,225))
    if prev is not None:
      fl=cv2.calcOpticalFlowFarneback(prev,g,None,0.5,3,15,3,5,1.2,0)
      H,W=g.shape;ys,xs=np.mgrid[0:H:4,0:W:4];m=(ys<150)  # eyes/forehead/nose/cheeks (top 2/3), excludes mouth
      X=np.stack([xs[m],ys[m],np.ones(m.sum())],1);F=fl[0:H:4,0:W:4][m]
      A,_,_,_=np.linalg.lstsq(X,F,rcond=None);res=np.linalg.norm(F-X@A,axis=1)
      R.append(float(np.percentile(res,95)));P.append(float(np.abs(F).mean()))
    prev=g
  return np.array(R),np.array(P)
out={}
for pid in sys.argv[1:]:
  w={x['id']:x for x in json.load(open('windows.json'))}[pid]
  o=json.load(open(f'orig-{pid}-perframe.json'))['frames'];cx=int(np.nanmedian([f.get('cx',.5) for f in o])*1920)
  ro,po=run(f'orig_{pid}.mp4',cx);rp,pp=run(f't1_{pid}.mp4',cx)
  out[pid]=dict(o_res_p95=round(np.percentile(ro,95),2),p_res_p95=round(np.percentile(rp,95),2),o_res_max=round(ro.max(),2),p_res_max=round(rp.max(),2),
    p_res_max_t=round(w['s']+(int(rp.argmax())+1)/25,2),o_mot=round(po.mean(),2),p_mot=round(pp.mean(),2))
  print(pid,out[pid],flush=True)
json.dump(out,open('warp_'+'_'.join(sys.argv[1:3])+'.json','w'))
