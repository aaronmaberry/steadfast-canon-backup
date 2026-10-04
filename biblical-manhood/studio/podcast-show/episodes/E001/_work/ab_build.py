# ab_build.py (2026-10-03 evening CT): rebuilds music/E001-open-AB.mp4 from the current masters.
# A = first 60 s of the main mix (dry open), 1.5 s silence, B = first 60 s of the open-bed candidate.
# Each half gain-normalized to -16 LUFS, 0.3 s fade at 1:00. Video is capA.png then capB.png.
import subprocess,re,numpy as np
SR=44100
def dec(f): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-t','60','-i',f,'-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True).stdout,np.float32).reshape(-1,2).copy()
def lufs(x):
    x.astype('<f4').tofile('/tmp/_ab.f32')
    e=subprocess.run(['ffmpeg','-nostats','-f','f32le','-ar',str(SR),'-ac','2','-i','/tmp/_ab.f32','-af','ebur128=peak=true:framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1])
D='out/candidate_openbed/'
halves=[]
for f in ('out/final_f32.wav',D+'final_f32.wav'):
    x=dec(f); g=-16.0-lufs(x); x*=np.float32(10**(g/20)); n=int(0.3*SR); x[-n:]*=np.cos(np.linspace(0,np.pi/2,n))[:,None].astype(np.float32)
    print(f,'gain',round(g,2)); halves.append(x)
y=np.concatenate([halves[0],np.zeros((int(1.5*SR),2),np.float32),halves[1]])
y.astype('<f4').tofile('/tmp/_ab.f32')
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','f32le','-ar',str(SR),'-ac','2','-i','/tmp/_ab.f32','-c:a','pcm_s16le',D+'ab_audio.wav'],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-t','60.75','-i',D+'capA.png','-loop','1','-framerate','30','-t','60.75','-i',D+'capB.png','-i',D+'ab_audio.wav',
  '-filter_complex','[0:v]scale=1080:1080,setsar=1[a];[1:v]scale=1080:1080,setsar=1[b];[a][b]concat=n=2:v=1:a=0,format=yuv420p[v]','-map','[v]','-map','2:a',
  '-c:v','libx264','-tune','stillimage','-c:a','aac','-b:a','192k','-ar','44100','-shortest','-movflags','+faststart','../music/E001-open-AB.mp4'],check=True)
print('done')
