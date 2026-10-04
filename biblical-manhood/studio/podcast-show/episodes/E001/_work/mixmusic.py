# mixmusic.py (polish pass): lay the theme D sting and closing bed over the mastered dialogue, stereo out.
import json,subprocess,re,numpy as np
SR=44100
THEME='../music/theme-D-full_take1.mp3'
def dec(f,ch):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac',str(ch),'-ar',str(SR),'-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32).reshape(-1,ch).copy()
def lufs(x):
    x.astype('<f4').tofile('/tmp/_m.f32')
    e=subprocess.run(['ffmpeg','-nostats','-f','f32le','-ar',str(SR),'-ac',str(x.shape[1]),'-i','/tmp/_m.f32','-af','ebur128=peak=true:framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1]),float(re.findall(r'Peak:\s+(-?[\d.]+|-inf) dBFS',e)[-1])
y=dec('out/master_f32.wav',1)[:,0]
th=dec(THEME,2)
cues=json.load(open('out/music_cues.json')); tl=json.load(open('out/timeline.json')); T={x['n']:x for x in tl}
N=len(y); mus=np.zeros((N,2),np.float32)
S=lambda t:int(round(t*SR))
def ramp(n,up=True):  # equal-power (sine) curve
    c=np.sin(np.linspace(0,np.pi/2,n)) if up else np.cos(np.linspace(0,np.pi/2,n)); return c.astype(np.float32)
# ---- sting: the theme's opening figure, 3.0 s, starting at its first note
env=np.sqrt((th.mean(1)[:S(1)].reshape(-1,441)**2).mean(1)); a0=int(np.argmax(env>0.01))*441-S(0.01)
st=th[a0:a0+S(cues['sting_len'])].copy()
st[:S(0.005)]*=ramp(S(0.005))[:,None]; st[-S(0.8):]*=ramp(S(0.8),False)[:,None]
I,P=lufs(st); g=10**((-17.5-I)/20); pk=20*np.log10(np.abs(st).max()*g)
if pk>-3: g*=10**((-3-pk)/20)
st*=g; s0=S(cues['sting_start']); mus[s0:s0+len(st)]+=st
sting=dict(theme_start_s=round(a0/SR,3),file_start_s=cues['sting_start'],lufs=round(lufs(st)[0],1),peak_dbfs=round(20*np.log10(np.abs(st).max()),1))
# ---- closing bed: theme excerpt whose final chord lands 0.6 s after "That's ours now."
on=np.sqrt((th.mean(1)[S(82):S(85)].reshape(-1,441)**2).mean(1)); d=np.diff(20*np.log10(on+1e-9))
chord_t=82+(int(np.argmax(d))+1)*0.01
t_chord=cues['l295_end']+0.6; bed0=cues['end']-20.0; bed1=cues['credits_start']-0.3
src0=chord_t-(t_chord-bed0)
ex=th[S(src0):S(src0)+S(bed1-bed0)].copy()
Ibed,_=lufs(th[S(src0):S(chord_t)]); Isw,_=lufs(th[S(chord_t):S(chord_t+2.0)])
G_BED=-35.0-Ibed; G_SW=-20.0-Isw; G_GAP=G_BED+6
t=bed0+np.arange(len(ex))/SR; gdb=np.full(len(ex),G_BED,np.float32)
# speech mask: bed level while anyone talks (300 ms down-ramp before, 600 ms up-ramp after), +6 dB only in gaps over 1.2 s
lines=[x for x in tl if x['end']>bed0 and x['n']<=295]
for a,b in zip(lines,lines[1:]):
    gs,ge=a['end'],b['start']
    if ge-gs>1.2:
        m=(t>gs)&(t<ge); up=np.clip((t-gs)/0.6,0,1); dn=np.clip((ge-t)/0.3,0,1); gdb[m]=G_BED+6*np.minimum(up,dn)[m]
sw0=cues['l295_end']+0.15; m=t>=sw0; gdb[m]=G_BED+(G_SW-G_BED)*np.clip((t[m]-sw0)/0.8,0,1)
amp=10**(gdb/20)
amp[:S(2.0)]*=ramp(S(2.0))                           # 2 s fade-in at the end screen
amp[-S(1.0):]*=ramp(S(1.0),False)                    # chord rings, then a 1 s fade, done 0.3 s before the credits
ex*=amp[:,None]; b0=S(bed0); mus[b0:b0+len(ex)]+=ex
out=y[:,None]*np.float32(np.sqrt(0.5))+mus   # same -3 dB pan law ffmpeg used for the mono-to-stereo deliverables, so dialogue stays at -16 LUFS
np.save('out/music_stem.npy',mus)
out.astype('<f4').tofile('out/final_f32.raw')
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','f32le','-ar',str(SR),'-ac','2','-i','out/final_f32.raw','-c:a','pcm_f32le','out/final_f32.wav'],check=True)
info=dict(sting=sting,chord_theme_s=round(chord_t,2),bed_theme_from_s=round(src0,2),bed_file_s=[round(bed0,3),round(bed1,3)],chord_file_s=round(t_chord,3),
          bed_gain_db=round(G_BED,1),swell_gain_db=round(G_SW,1),bed_lufs_under_speech=round(lufs(ex[S(2.5):S(sw0-bed0)])[0],1),
          swell_lufs=round(lufs(ex[S(t_chord-bed0):S(t_chord-bed0+2.0)])[0],1),music_peak_dbfs=round(20*np.log10(np.abs(mus).max()),1),
          long_gaps_in_bed=[(a['n'],b['n'],round(b['start']-a['end'],2)) for a,b in zip(lines,lines[1:]) if b['start']-a['end']>1.2])
json.dump(info,open('out/music_mix.json','w'),indent=1,default=float); print(json.dumps(info,indent=1,default=float))
print('final',lufs(out))
