# join.py PID take -> per-frame full-frame diff orig vs patch in edge zones; best in/out
import cv2,json,sys,numpy as np
pid,tk=sys.argv[1],sys.argv[2]
def frames(f):
  c=cv2.VideoCapture(f);R=[]
  while True:
    o,x=c.read()
    if not o:break
    R.append(cv2.resize(x,(480,270),interpolation=cv2.INTER_AREA).astype(np.float32))
  return R
O,P=frames(f'orig_{pid}.mp4'),frames(f'{tk}_{pid}.mp4');n=min(len(O),len(P))
d=np.array([np.abs(O[i]-P[i]).mean() for i in range(n)])
o=json.load(open(f'orig-{pid}-perframe.json'))['frames'];p=json.load(open(f'{tk}-{pid}-perframe.json'))['frames']
g=lambda F,i:F[i].get('gap',1) or 1
cost=np.array([d[i]+150*max(0,g(o,i)-0.07)+150*max(0,g(p,i)-0.07) for i in range(n)])
m=min(40,n//3)
i_in=int(np.argmin(cost[:m]));i_out=n-m+int(np.argmin(cost[n-m:]))
print(json.dumps(dict(id=pid,take=tk,n=n,i_in=i_in,i_out=i_out,d_in=round(float(d[i_in]),2),d_out=round(float(d[i_out]),2),dmed=round(float(np.median(d)),2),dmin=round(float(d.min()),2),gaps_in=[g(o,i_in),g(p,i_in)],gaps_out=[g(o,i_out),g(p,i_out)])))
for tag,i in (('in',i_in),('out',i_out)):
  a=cv2.resize(O[i].astype(np.uint8),(960,540));b=cv2.resize(P[i].astype(np.uint8),(960,540))
  cv2.imwrite(f'join_{pid}_{tk}_{tag}.jpg',np.hstack([a,b]),[cv2.IMWRITE_JPEG_QUALITY,80])
json.dump(dict(i_in=i_in,i_out=i_out,d=d.tolist()),open(f'join_{pid}_{tk}.json','w'))
