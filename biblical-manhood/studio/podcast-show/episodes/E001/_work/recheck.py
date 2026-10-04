import os,json,subprocess
os.environ.setdefault('MKL_ENABLE_INSTRUCTIONS','AVX2'); os.environ.setdefault('ONEDNN_MAX_CPU_ISA','AVX2'); os.environ.setdefault('CT2_FORCE_CPU_ISA','AVX2')
from faster_whisper import WhisperModel
import numpy as np
m=WhisperModel(os.environ.get('M','medium.en'),device='cpu',compute_type='int8',cpu_threads=8)
tl={x['n']:x for x in json.load(open('out/timeline.json'))}
L={l['n']:l for l in json.load(open('lines_v3.json'))}
for n in json.loads(os.environ['NS']):
    s=tl[n]['start']-0.15; e=tl[n]['end']+0.15
    a=subprocess.run(['ffmpeg','-v','error','-ss',str(s),'-to',str(e),'-i','../E001-walk-steadfast.wav','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    x=np.frombuffer(a,np.float32)
    segs,_=m.transcribe(x,language='en',beam_size=5,condition_on_previous_text=False)
    print(n,'| SCRIPT:',L[n]['text'][:400]); print('   HEARD:',' '.join(sg.text.strip() for sg in segs)[:400],flush=True)
