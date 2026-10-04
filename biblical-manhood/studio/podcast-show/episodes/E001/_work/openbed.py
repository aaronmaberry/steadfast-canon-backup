# openbed.py (candidate, 5:36 PM CT): theme D sting flowing into a low bed under the open and slate. Main E001 files untouched.
import json,subprocess,re,numpy as np
SR=44100; S=lambda t:int(round(t*SR))
def dec(f,ch):
    return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac',str(ch),'-ar',str(SR),'-'],capture_output=True).stdout,np.float32).reshape(-1,ch).copy()
def lufs(x):
    x.astype('<f4').tofile('/tmp/_ob.f32')
    e=subprocess.run(['ffmpeg','-nostats','-f','f32le','-ar',str(SR),'-ac',str(x.shape[1]),'-i','/tmp/_ob.f32','-af','ebur128=peak=true:framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1])
th=dec('../music/theme-D-full_take1.mp3',2); y=dec('out/master_f32.wav',1)[:,0]
mus=np.load('out/music_stem.npy'); cues=json.load(open('out/music_cues.json')); T={x['n']:x for x in json.load(open('out/timeline.json'))}
st0=cues['sting_start']; A0=0.12                      # sting = theme from its first note (same as the main mix)
JUMP_FROM,JUMP_TO,XF=23.04,9.30,0.30                  # 4-bar repeat in the calm guitar-and-bass section (chroma match 0.98, onset match 0.91)
fade1=T[12]['start']+0.5; fade0=fade1-1.5            # bed fades out over 1.5 s as "Pull up a chair" starts
need=fade1-st0                                        # seconds of music from the sting to the end of the fade
p1=th[S(A0):S(JUMP_FROM+XF/2)].copy(); p2=th[S(JUMP_TO-XF/2):S(JUMP_TO-XF/2)+S(need)].copy()
n=S(XF); c=np.linspace(0,np.pi/2,n)[:,None]
piece=np.concatenate([p1[:-n],p1[-n:]*np.cos(c)+p2[:n]*np.sin(c),p2[n:]])[:S(need)]
t=st0+np.arange(len(piece))/SR
# gains: sting exactly as in the main mix, easing down to the bed level as Wes's open starts
sting=th[S(A0):S(A0)+S(3.0)].copy(); sting[-S(0.8):]*=np.cos(np.linspace(0,np.pi/2,S(0.8)))[:,None]
G_ST=-17.5-lufs(sting); pk=20*np.log10(np.abs(sting).max())+G_ST
if pk>-3: G_ST-=pk+3
bed_src=np.concatenate([th[S(4.4):S(JUMP_FROM)],th[S(JUMP_TO):S(JUMP_TO+need-(JUMP_FROM-A0))]])
G_BED=-35.0-lufs(bed_src)
r0,r1=T[4]['start']-0.6,T[4]['start']
gdb=np.where(t<r0,G_ST,np.where(t>r1,G_BED,G_ST+(G_BED-G_ST)*(t-r0)/(r1-r0)))
amp=10**(gdb/20); m=t>=fade0; amp[m]*=np.cos(np.clip((t[m]-fade0)/(fade1-fade0),0,1)*np.pi/2)
piece*=amp[:,None]
mus2=mus.copy(); mus2[S(st0):S(st0+3.0)]=0; mus2[S(st0):S(st0)+len(piece)]+=piece
out=y[:,None]*np.float32(np.sqrt(0.5))+mus2
out.astype('<f4').tofile('out/candidate_openbed/final_f32.raw')
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','f32le','-ar',str(SR),'-ac','2','-i','out/candidate_openbed/final_f32.raw','-c:a','pcm_f32le','out/candidate_openbed/final_f32.wav'],check=True)
import os; os.remove('out/candidate_openbed/final_f32.raw')
dlg=lambda a,b:lufs(out[S(a):S(b)]-mus2[S(a):S(b)])
info=dict(bed_gain_db=round(G_BED,1),sting_gain_db=round(G_ST,1),
  bed_alone_lufs_open_and_slate=round(lufs(mus2[S(T[4]['start']):S(T[11]['end'])]),1),
  voices_lufs_open_and_slate=round(dlg(T[4]['start'],T[11]['end']),1),
  voices_plus_bed_lufs=round(lufs(out[S(T[4]['start']):S(T[11]['end'])]),1),
  bed_alone_lufs_slate=round(lufs(mus2[S(T[9]['start']):S(T[11]['end'])]),1),
  theme_map=f"theme {A0}-{JUMP_FROM}s, then {JUMP_TO}-{round(JUMP_TO+need-(JUMP_FROM-A0),2)}s (0.3 s crossfade at the 4-bar repeat)",
  fade_out_file_s=[round(fade0,2),round(fade1,2)],music_peak_dbfs=round(20*np.log10(np.abs(mus2).max()),1))
json.dump(info,open('out/candidate_openbed/openbed.json','w'),indent=1,default=float); print(json.dumps(info,indent=1,default=float))
