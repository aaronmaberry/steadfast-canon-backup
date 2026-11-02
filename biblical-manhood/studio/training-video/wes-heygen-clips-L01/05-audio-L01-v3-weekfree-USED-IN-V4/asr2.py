from faster_whisper import WhisperModel
import json,subprocess,numpy as np
m=WhisperModel('medium.en',device='cpu',compute_type='int8',cpu_threads=2)
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','../L01-P7-ASSEMBLED-v3.mp4','-ar','16000','-ac','1','-f','f32le','-'],capture_output=True).stdout,np.float32)
sr=16000;L=len(x)/sr;out=[];t=0.0;C=28.0;O=2.0
while t<L:
    seg=x[int(t*sr):int(min(L,t+C)*sr)]
    ss,_=m.transcribe(seg,beam_size=5,word_timestamps=True,condition_on_previous_text=False,vad_filter=False,temperature=[0.0,0.2,0.4])
    for s in ss:
        for w in s.words:out.append(dict(w=w.word,s=round(t+w.start,3),e=round(t+w.end,3),chunk=t))
    print(round(t,1),flush=True);t+=C-O
json.dump(out,open('asr2_v3.json','w'))
print('done')
