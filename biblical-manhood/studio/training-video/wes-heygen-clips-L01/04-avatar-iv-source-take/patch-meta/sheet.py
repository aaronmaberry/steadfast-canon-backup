# sheet.py PID take : lower-face crops, orig row vs patch row, 14 cols spanning the dip +-0.6s, ArcFace labels
import cv2,json,sys,numpy as np
pid,tk=sys.argv[1],sys.argv[2]
W={w['id']:w for w in json.load(open('windows.json'))}[pid]
o=json.load(open(f'orig-{pid}-perframe.json'))['frames'];q=json.load(open(f'{tk}-{pid}-perframe.json'))['frames']
a=max(0,int((W['dip'][0]-W['s']-0.6)*25));b=min(len(q)-1,int((W['dip'][1]-W['s']+0.6)*25))
idx=np.linspace(a,b,14).astype(int)
def row(f,F):
  c=cv2.VideoCapture(f);out=[];k=0;S=set(idx)
  while True:
    ok,x=c.read()
    if not ok:break
    if k in S:
      cx=int((F[k].get('cx') or .5)*1920);y0=330
      im=cv2.resize(x[y0:y0+300,cx-170:cx+170],(204,180))
      cv2.putText(im,f"{W['s']+k/25:.2f} {F[k].get('arc',0):.2f}",(3,14),0,0.42,(0,255,255),1);out.append(im)
    k+=1
  return np.hstack(out)
img=np.vstack([row(f'orig_{pid}.mp4',o),row(f'{tk}_{pid}.mp4',q)])
cv2.putText(img,f'{pid} top=original  bottom={tk} patch',(3,175),0,0.45,(255,255,255),1)
cv2.imwrite(f'sheet_{pid}_{tk}.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,72])
