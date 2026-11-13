"""Frame-level hand map (L12): every master frame, skin blobs below the face in the W frame / P card / tight card.
Writes plan/dense_w.npy, dense_p.npy, dense_t.npy; quality.py ORs them into q_wide / q_panel / q_tight. ~20 min, background.
Skin bounds here are the L12 values (Cr > 146 skips sweater highlights; hue <= 11 skips tan/camel knit). Check them per wardrobe (C7)."""
import subprocess, numpy as np, cv2
M='/home/claude/l04/master/l04_master.mp4'; W,H=640,360; k5=np.ones((5,5),np.uint8)
p=subprocess.Popen(["ffmpeg","-v","error","-i",M,"-vf",f"scale={W}:{H}","-f","rawvideo","-pix_fmt","bgr24","-"],stdout=subprocess.PIPE)
dw=[]; dp=[]; dt=[]
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    img=np.frombuffer(b,np.uint8).reshape(H,W,3)
    sub=img[180:280]
    ycc=cv2.cvtColor(sub,cv2.COLOR_BGR2YCrCb); hh=cv2.cvtColor(sub,cv2.COLOR_BGR2HSV)[...,0]
    sk=((ycc[...,1]>146)&(ycc[...,1]<175)&(ycc[...,2]>85)&(ycc[...,2]<125)&(ycc[...,0]>45)&((hh<=11)|(hh>=170))).astype(np.uint8)
    sk=cv2.morphologyEx(sk,cv2.MORPH_OPEN,k5)
    n,lab,st,c=cv2.connectedComponentsWithStats(sk,8)
    bw=bp=bt=0
    for j in range(1,n):
        x,y,w,h,a=st[j]; y+=180
        if a<250 or y<=180: continue
        if 255<x<330 and x+w<420 and y<240 and h<80 and y+h<285: continue   # neck/collar (L12 crewneck sits at y 193-240)
        if (y<268 and a>1500) or y<262: bw=1
        if y<267 and x+w>400/3 and x<1520/3: bp=1
        if y<234 and x+w>470/3 and x<1450/3: bt=1
    dw.append(bw); dp.append(bp); dt.append(bt)
np.save('/home/claude/l04/plan/dense_w.npy',np.array(dw,np.uint8)); np.save('/home/claude/l04/plan/dense_p.npy',np.array(dp,np.uint8))
np.save('/home/claude/l04/plan/dense_t.npy',np.array(dt,np.uint8)); print(sum(dt),'T hits');print(len(dw),'frames; W hits',sum(dw),'P hits',sum(dp))
