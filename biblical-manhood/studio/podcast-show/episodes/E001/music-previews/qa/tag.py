import sys
sys.modules["torchvision"]=None
import transformers.utils as _u, transformers.utils.import_utils as _iu
_iu.is_torchvision_available=lambda *a,**k: False
_u.is_torchvision_available=_iu.is_torchvision_available
import glob,os,numpy as np,subprocess,torch
from transformers import ASTFeatureExtractor, ASTForAudioClassification
name="MIT/ast-finetuned-audioset-10-10-0.4593"
fe=ASTFeatureExtractor.from_pretrained(name);m=ASTForAudioClassification.from_pretrained(name).eval()
lab=m.config.id2label
watch=['Singing','Speech','Choir','Vocal music','Male singing','Female singing','Humming','Whistling','Clapping','Hands','Synthesizer','Organ','Ukulele','Piano',
 'Accordion','Cello','Double bass','Violin, fiddle','Bowed string instrument','Acoustic guitar','Electric guitar','Steel guitar, slide guitar','Bass guitar','Guitar','Plucked string instrument','Strum','Drum','Drum kit','Snare drum','Bass drum','Country','Waltz','Hip hop music','Ambient music']
idx={v:k for k,v in lab.items()}
for f in sorted(glob.glob('raw/*.mp3')):
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.float32)
    P=[]
    for s in range(0,len(a)-16000*5,16000*5):
        x=fe(a[s:s+16000*10],sampling_rate=16000,return_tensors='pt')
        with torch.no_grad(): P.append(torch.sigmoid(m(**x).logits)[0].numpy())
    P=np.array(P);mx=P.max(0);mean=P.mean(0)
    top=np.argsort(-mean)[:10]
    print('==',os.path.basename(f));print('  top (mean):',', '.join(f"{lab[i]} {mean[i]:.2f}" for i in top))
    print('  watch (max over 10 s windows):',', '.join(f"{w} {mx[idx[w]]:.2f}" for w in watch if w in idx and mx[idx[w]]>=0.05))
