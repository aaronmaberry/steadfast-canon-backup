from faster_whisper import WhisperModel
import json,sys
m=WhisperModel('medium.en',device='cpu',compute_type='int8',cpu_threads=3)
seg,_=m.transcribe(sys.argv[1],word_timestamps=True,beam_size=5,condition_on_previous_text=False)
out=[]
for s in seg:
    out.append(dict(start=s.start,end=s.end,text=s.text,words=[dict(w=w.word,s=w.start,e=w.end) for w in s.words]));print(round(s.start,1),s.text,flush=True)
json.dump(out,open(sys.argv[2],'w'),indent=0)
