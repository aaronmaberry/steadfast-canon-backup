import cv2,numpy as np,subprocess,sys
V,OUT=sys.argv[1],sys.argv[2]
T0,DUR=44.76,20.0; A,B=44.84,57.44; FPS=25
d2s=lambda p:(1080+p[0]/1.97,110+p[1]/1.97)
L=[(62,622),(170,600),(286,572),(290,550),(410,546),(408,694),(102,795),(82,730)]
R=[(384,316),(640,280),(722,418),(726,574),(468,640),(424,505)]
mask=np.zeros((1080,1920),np.float32)
for P in (L,R): cv2.fillPoly(mask,[np.array([d2s(p) for p in P],np.int32)],1.0)
mask=cv2.GaussianBlur(mask,(0,0),3)[...,None]
W,H=1920,1080
dec=subprocess.Popen(['ffmpeg','-v','error','-ss',str(T0),'-t',str(DUR),'-i',V,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','25','-i','-','-c:v','libx264','-preset','slow','-crf','12','-profile:v','high','-level','5.0','-pix_fmt','yuv420p','-g','250','-keyint_min','250','-sc_threshold','0','-bf','3','-video_track_timescale','12800',OUT],stdin=subprocess.PIPE)
i=0;n=0
while True:
  b=dec.stdout.read(W*H*3)
  if len(b)<W*H*3: break
  t=T0+i/FPS
  if A-1e-3<=t<B:
    f=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.float32)
    bl=cv2.GaussianBlur(f,(0,0),7); bl=cv2.GaussianBlur(bl,(0,0),7)
    f=f*(1-mask)+bl*mask; b=np.clip(f+0.5,0,255).astype(np.uint8).tobytes(); n+=1
  enc.stdin.write(b); i+=1
enc.stdin.close(); enc.wait(); print('frames',i,'patched',n)
