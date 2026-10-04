# qa2.py FILE... : independent whisper pass on single-line wavs (second opinion). prints compare vs script.
import os,sys,json,re
os.environ.setdefault('MKL_ENABLE_INSTRUCTIONS','AVX2'); os.environ.setdefault('ONEDNN_MAX_CPU_ISA','AVX2'); os.environ.setdefault('CT2_FORCE_CPU_ISA','AVX2')
from faster_whisper import WhisperModel
from qa import compare,L
m=WhisperModel('medium.en',device='cpu',compute_type='int8',cpu_threads=8)
out={}
for f in sys.argv[1:]:
    n=int(re.search(r'L(\d+)',f).group(1))
    segs,_=m.transcribe(f,word_timestamps=True,language='en',beam_size=5,vad_filter=False,condition_on_previous_text=False,initial_prompt='Wes Hart, Jonathon, Dani, Ruby, Theo, Abernathy, sixteen-oh-four.')
    ws=[(w.word.strip(),w.start,w.end) for s in segs for w in s.words]
    c=compare(n,[w[0] for w in ws]); c['file']=f; c['text']=' '.join(w[0] for w in ws)
    out[f]=c
    print(n,c['errs'],c['ops'],'|',c['text'][:300],flush=True)
json.dump(out,open('qa2_last.json','w'),indent=0)
