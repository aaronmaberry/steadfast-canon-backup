import json,subprocess,sys,os
sys.path.insert(0,'/workspace/l01v3/build');from tmap import s2o
B=json.load(open('broll_plan_v3.json'));V2={b['id']:b for b in json.load(open('/workspace/l01v2/build/broll_plan.json'))}
os.makedirs('/workspace/l01v3/broll/mezz',exist_ok=True)
for k,b in enumerate(B):
    i=b['id'];need=s2o(b['b'])-s2o(b['a'])+0.4;o=f'/workspace/l01v3/broll/mezz/b{k:02d}_{i}.mp4'
    if i in('99888','99890'):
        v=V2[i];print('v2',v['a'],v['b'],'v3',b['a'],b['b'],'need',need,'v2len',v['out_len']+0.4);assert need<=v['out_len']+0.4+1e-3;b.update(mezz=v['mezz'],src_dur=v['src_dur'],clip_in=v['clip_in'],out_len=round(need-0.4,3));print(k,i,'reuse v2 mezz');continue
    f=b['file'] if b['src']!='mixkit' else f'/workspace/l01v3/broll/mx/{i}.mp4'
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    off=max(0.0,min(b['clip_in'],d-need-0.1))
    if need>d-0.05:print('TOO SHORT',i,need,d)
    b.update(mezz=o,file=f,src_dur=round(d,2),clip_in=round(off,2),out_len=round(need-0.4,3))
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{off:.2f}','-i',f,'-t',f'{need:.2f}','-vf','scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,fps=25,eq=saturation=0.86:brightness=-0.02:contrast=1.03,vignette=angle=0.45','-an','-c:v','libx264','-crf','15','-preset','fast','-pix_fmt','yuv420p',o],check=True)
    print(k,i,round(d,1),off,round(need,2),flush=True)
json.dump(B,open('broll_plan_v3.json','w'),indent=0)
