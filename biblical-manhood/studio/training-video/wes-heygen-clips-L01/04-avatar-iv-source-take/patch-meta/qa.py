# streaming per-frame QA: qa.py clip.mp4 outtag  (ArcFace every frame vs look A ref, lip gap, mouth frame-diff, face w, cx, red specks)
import sys,os,json,cv2,numpy as np
sys.path.insert(0,'/workspace/artifacts/training/lipsync-tests-2026-10-26/scripts');import evaluate as E
n=lambda v:v/np.linalg.norm(v)
VI=n(np.load('/workspace/steadfast-main/training-locked/INTRO-LOOK-A-MASTER-LOCKED-2026-10-26/intro_ref_embedding.npy').ravel())
fa=E.app();clip,tag=sys.argv[1],sys.argv[2];OUT=os.path.dirname(os.path.abspath(__file__))
c=cv2.VideoCapture(clip);fps=c.get(5);R=[];i=0;prev=None;crops=[]
while True:
    o,x=c.read()
    if not o:break
    f=E.biggest(fa.get(x))
    if f is None: R.append(dict(i=i,miss=1));i+=1;prev=None;continue
    l=f.landmark_2d_106;w=float(f.bbox[2]-f.bbox[0]);inner=l[63:72]
    x0,y0,x1,y1=E.mouth_box(l,x);m=cv2.resize(cv2.cvtColor(x[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY),(96,96)).astype(np.float32)
    md=float(np.abs(m-prev).mean()) if prev is not None else None;prev=m
    # red specks outside lips (vivid red, small blobs)
    h=cv2.cvtColor(x,cv2.COLOR_BGR2HSV);rm=(((h[...,0]<6)|(h[...,0]>172))&(h[...,1]>200)&(h[...,2]>150)).astype(np.uint8)
    lx0,ly0,lx1,ly1=[int(v) for v in (l[52:72,0].min()-15,l[52:72,1].min()-15,l[52:72,0].max()+15,l[52:72,1].max()+15)];rm[max(0,ly0):ly1,max(0,lx0):lx1]=0
    nl,_,st,cen=cv2.connectedComponentsWithStats(rm);red=[(int(cen[k][0]),int(cen[k][1]),int(st[k,4])) for k in range(1,nl) if 3<=st[k,4]<=400]
    r=dict(i=i,t=round(i/fps,3),arc=float(n(f.embedding)@VI),w=w,cx=float((f.bbox[0]+f.bbox[2])/2/x.shape[1]),gap=float((inner[:,1].max()-inner[:,1].min())/w),md=md,red=red)
    if i%12==0: crops.append((i,cv2.resize(x[y0:y1,x0:x1],(120,120))))
    R.append(r);i+=1
    if i%500==0:print(i,flush=True)
json.dump(dict(fps=fps,frames=R),open(f'{OUT}/{tag}-perframe.json','w'))
# mouth sheet (every 12th frame = 0.48 s), 16 per row
T=[]
for j,m in crops: cv2.putText(m,f'{j/fps:.1f}',(2,12),0,0.38,(0,255,255),1);T.append(m)
while len(T)%16:T.append(np.zeros_like(T[0]))
cv2.imwrite(f'{OUT}/{tag}-mouth-sheet.jpg',np.vstack([np.hstack(T[k:k+16]) for k in range(0,len(T),16)]),[cv2.IMWRITE_JPEG_QUALITY,70])
print('done',len(R))
