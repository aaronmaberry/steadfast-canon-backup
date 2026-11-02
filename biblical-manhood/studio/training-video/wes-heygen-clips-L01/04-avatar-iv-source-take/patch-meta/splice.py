# splice.py accepted.json out.mp4 : replace frames in windows with patch frames, XF-frame linear crossfade at each edge, original audio stream-copied
import json,subprocess,sys,numpy as np
A=json.load(open(sys.argv[1]));OUT=sys.argv[2];XF=6
W,H=1920,1080;FS=W*H*3//2;SRC='../L01-P5-FULL-burg_a-4c7713cd.mp4'
rd=lambda f:subprocess.Popen(['ffmpeg','-v','error','-i',f,'-f','rawvideo','-pix_fmt','yuv420p','-'],stdout=subprocess.PIPE,bufsize=FS*4)
src=rd(SRC)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','yuv420p','-s',f'{W}x{H}','-r','25','-i','-','-i',SRC,'-map','0:v','-map','1:a','-c:a','copy',
  '-c:v','libx264','-preset','fast','-crf','14','-profile:v','high','-pix_fmt','yuv420p','-g','50','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
# per accepted patch: global frame range [a,b) = s*25+i_in-XF/2 .. s*25+i_out+XF/2
P=[]
for p in A:
  s0=round(p['s']*25);a=s0+p['i_in']-XF//2;b=s0+p['i_out']+XF//2;P.append(dict(p,s0=s0,a=a,b=b))
P.sort(key=lambda p:p['a']);k=0;i=0;cur=None;pr=None
while True:
  buf=src.stdout.read(FS)
  if len(buf)<FS:break
  if cur is None and k<len(P) and i==P[k]['s0']:
    cur=P[k];pr=rd(cur['file']);k+=1
  if cur is not None:
    pb=pr.stdout.read(FS);j=i-cur['s0']
    if len(pb)==FS and cur['a']<=i<cur['b']:
      o=np.frombuffer(buf,np.uint8).astype(np.float32);q=np.frombuffer(pb,np.uint8).astype(np.float32)
      if i<cur['a']+XF: al=(i-cur['a']+1)/(XF+1)
      elif i>=cur['b']-XF: al=(cur['b']-i)/(XF+1)
      else: al=1.0
      buf=(o*(1-al)+q*al+0.5).astype(np.uint8).tobytes()
    if j==cur['n']-1 or len(pb)<FS:
      pr.stdout.close();pr.wait();cur=None
  enc.stdin.write(buf);i+=1
  if i%2500==0:print(i,flush=True)
enc.stdin.close();enc.wait();print('frames',i)
