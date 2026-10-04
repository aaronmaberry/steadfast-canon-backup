import os,json
os.environ.setdefault('MKL_ENABLE_INSTRUCTIONS','AVX2'); os.environ.setdefault('ONEDNN_MAX_CPU_ISA','AVX2'); os.environ.setdefault('CT2_FORCE_CPU_ISA','AVX2')
from faster_whisper import WhisperModel
m=WhisperModel('medium.en',device='cpu',compute_type='int8',cpu_threads=8)
segs,_=m.transcribe('../E001-walk-steadfast.mp3',word_timestamps=True,language='en',beam_size=5,vad_filter=False,condition_on_previous_text=False,
    initial_prompt='Walk Steadfast. Wes Hart and Jonathon. Dani, Ruby, Theo, Mr. Abernathy.')
words=[]
for s in segs:
    for w in s.words: words.append((w.word.strip(),round(w.start,3),round(w.end,3),round(w.probability,3)))
    print(round(s.end,1),flush=True)
json.dump(words,open('out/final_words.json','w'))
print('DONE',len(words))
