import numpy as np, subprocess, json, re
sr=44100; y=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','out/master_f32.wav','-f','f32le','-ac','1','-'],capture_output=True).stdout,np.float32)
tl=json.load(open('out/timeline.json')); T={x['n']:x for x in tl}
NEWB={72,148,240,243,254,285,296}
def lufs(ns):
    a=np.concatenate([y[int(T[n]['start']*sr):int(T[n]['end']*sr)] for n in ns])
    a.astype('<f4').tofile('/tmp/_seg.f32')
    o=subprocess.run(['ffmpeg','-nostats','-f','f32le','-ar','44100','-ac','1','-i','/tmp/_seg.f32','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    I=float(re.findall(r'I:\s+(-?[\d.]+) LUFS',o)[-1]); P=float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS',o)[-1]); return [I,P]
m={'clipped_samples':int((np.abs(y)>=0.999).sum()),'sample_peak_dbfs':round(float(20*np.log10(np.abs(y).max())),2)}
for spk in ('WES','JONATHON'):
    alln=[x['n'] for x in tl if x['spk']==spk]
    m[spk]=lufs(alln); m[spk+'_open']=lufs([n for n in alln if n<=11]); m[spk+'_pickups']=lufs([n for n in alln if n in NEWB]) ; m[spk+'_rest']=lufs([n for n in alln if n>11 and n not in NEWB])
def gaprms(pairs):
    v=[]
    for a,b in pairs:
        s,e=T[a]['end']+0.15,T[b]['start']-0.05
        if e-s>0.1: v.append(np.mean(y[int(s*sr):int(e*sr)]**2))
    return round(float(10*np.log10(np.mean(v))),1)
ns=sorted(T)
m['gap_rms_open_db']=gaprms([(a,b) for a,b in zip(ns,ns[1:]) if b<=12])
m['gap_rms_rest_db']=gaprms([(a,b) for a,b in zip(ns,ns[1:]) if a>=12])
g=[T[b]['start']-T[a]['end'] for a,b in zip(ns,ns[1:])]
g_body=[x for x,(a,b) in zip(g,zip(ns,ns[1:])) if b!=296]
m['turn_gap_min']=round(min(g),2); m['turn_gap_max_excl_credits']=round(max(g_body),2); m['turn_gap_median']=round(float(np.median(g)),2)
m['credits_gap_s']=round(T[296]['start']-T[295]['end'],2); m['tail_after_credits_s']=round(len(y)/sr-T[296]['end'],2)
for spk in ('WES','JONATHON'):
    L={l['n']:l for l in json.load(open('lines_v3.json'))}
    w=sum(len(L[x['n']]['text'].split()) for x in tl if x['spk']==spk); d=sum(x['end']-x['start'] for x in tl if x['spk']==spk); m[spk+'_wpm']=round(w/d*60)
m['cold_open_s']=round(T[3]['end']-T[1]['start'],1); m['open_s']=round(T[8]['end']-T[4]['start'],1); m['slate_s']=round(T[11]['end']-T[9]['start'],1)
m['runtime_s']=round(len(y)/sr,2)
json.dump(m,open('out/metrics_v3.json','w'),indent=1); print(json.dumps(m))
