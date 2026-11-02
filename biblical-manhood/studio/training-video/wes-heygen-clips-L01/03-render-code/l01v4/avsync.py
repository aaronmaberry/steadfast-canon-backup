import sys,json,subprocess,numpy as np,cv2
sys.path.insert(0,'/workspace/l01v4/build');from tmap import s2o
from insightface.app import FaceAnalysis
fa=FaceAnalysis(name='buffalo_l',allowed_modules=['detection'],providers=['CPUExecutionProvider']);fa.prepare(ctx_id=-1,det_size=(320,320))
V='/workspace/l01v2/L01-P7-ASSEMBLED-v2.mp4';A='/workspace/l01v2/L01-v2-weekcut-minus26-LUFS.mp3'
res={}
for name,(sa,sb) in {'before_cuts_WES_FULL_4':(63.0,70.4),'between_cut2_cut3_SPLIT_60':(1012.0,1019.9),'after_cut3_WES_FULL_68':(1178.6,1192.6)}.items():
    a,b=s2o(sa),s2o(sb);n=int((b-a)*25)
    p=subprocess.run(['ffmpeg','-v','error','-ss',f'{a:.3f}','-i',V,'-frames:v',str(n),'-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True).stdout
    F=np.frombuffer(p,np.uint8).reshape(-1,1080,1920,3);m=[]
    for f in F:
        d=fa.get(f);d=max(d,key=lambda x:x.det_score);k=d.kps;ml,mr=k[3],k[4];w=np.linalg.norm(mr-ml)
        x0,x1=int(ml[0]-0.2*w),int(mr[0]+0.2*w);y0,y1=int(min(ml[1],mr[1])-0.35*w),int(max(ml[1],mr[1])+0.55*w)
        m.append(cv2.resize(cv2.cvtColor(f[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY),(64,48)).astype(np.float32))
    mo=np.array([np.abs(m[i]-m[i-1]).mean() for i in range(1,len(m))])
    au=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-ss',f'{a:.3f}','-t',f'{n/25:.3f}','-i',A,'-f','f32le','-ac','1','-ar','48000','-'],capture_output=True).stdout,np.float32)
    env=np.array([np.sqrt((au[i*1920:(i+1)*1920]**2).mean()) for i in range(n)]);de=np.abs(np.diff(env))
    L=min(len(mo),len(de));mo=mo[:L];de=de[:L]
    cs={lag:float(np.corrcoef(mo[max(0,lag):L+min(0,lag)],de[max(0,-lag):L-max(0,lag)])[0,1]) for lag in range(-5,6)}
    best=max(cs,key=cs.get);res[name]=dict(out=[round(a,2),round(b,2)],best_lag_frames=best,corr_at_best=round(cs[best],3),corr_at_0=round(cs[0],3))
    print(name,res[name],flush=True)
json.dump(res,open('/workspace/l01v2/qc/avsync.json','w'),indent=1)
