import json,subprocess,re,numpy as np
SR=44100
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','../E001-walk-steadfast.wav','-f','f32le','-'],capture_output=True).stdout,np.float32).reshape(-1,2)
mus=np.load('out/music_stem.npy'); cues=json.load(open('out/music_cues.json')); T={t['n']:t for t in json.load(open('out/timeline.json'))}
m=x.mean(1); S=lambda t:int(round(t*SR))
def env(t0,t1,step=0.1,sig=m):
    return [int(round(20*np.log10(np.sqrt((sig[S(t):S(t+step)]**2).mean())+1e-9))) for t in np.arange(t0,t1,step)]
def lufs(a):
    a.astype('<f4').tofile('/tmp/_q.f32')
    e=subprocess.run(['ffmpeg','-nostats','-f','f32le','-ar','44100','-ac','2','-i','/tmp/_q.f32','-af','ebur128=peak=true:framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1])
r={}
r['clipped']=int((np.abs(x)>=0.999).sum()); r['sample_peak']=round(float(20*np.log10(np.abs(x).max())),2)
# silences: longest run under -50 dBFS (50 ms frames)
w=S(0.05); k=len(m)//w; db=20*np.log10(np.sqrt((m[:k*w].reshape(k,w)**2).mean(1))+1e-9); q=db<-50; runs=[];i=0
while i<k:
    if q[i]:
        j=i
        while j<k and q[j]: j+=1
        runs.append(((j-i)*0.05,i*0.05)); i=j
    else: i+=1
runs.sort(reverse=True); r['longest_silences_s']=[(round(d,2),round(t,1)) for d,t in runs[:5]]
r['cold_open_env_14_20s']=env(14.5,20.5)
r['sting_file_s']=[cues['sting_start'],cues['sting_start']+3]; r['L4_start']=T[4]['start']
r['music_at_L4_start_db']=env(T[4]['start'],T[4]['start']+0.4,0.1,mus.mean(1))
r['outro_env_from_L295_end']=env(cues['l295_end']-0.5,cues['end'],0.25)
r['music_after_resolve_max']=float(np.abs(mus[S(cues['credits_start']-0.3):]).max())
r['credits_lufs']=lufs(x[S(T[296]['start']):S(T[296]['end'])]); r['wes_body_lufs']=lufs(np.concatenate([x[S(t['start']):S(t['end'])] for t in T.values() if t['spk']=='WES' and 30<t['n']<280]))
r['outro_speech_with_bed_lufs']=lufs(x[S(T[291]['start']):S(T[295]['end'])]); r['bed_alone_under_outro_lufs']=lufs(mus[S(T[291]['start']):S(T[295]['end'])])
r['swell_lufs']=lufs(mus[S(cues['l295_end']+0.6):S(cues['l295_end']+2.6)]); r['sting_lufs']=lufs(mus[S(cues['sting_start']):S(cues['sting_start']+3)])
r['end_screen_start']=round(cues['end']-20,2); r['bed_start']=round(cues['end']-20,2)
r['laugh_gaps']=[(n,round(T[n]['start']-T[n-1]['end'],2)) for n in (16,36,76,89,122,156,180,197,217,274,289)]
print(json.dumps(r,indent=0))
json.dump(r,open('out/polish_qa.json','w'),indent=1)
