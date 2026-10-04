import subprocess,sys,re,glob,os,numpy as np
def dec(f):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','2','-ar','48000','-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32).reshape(-1,2)
def r128(f):
    e=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',f,'-af','ebur128=peak=true:framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
    I=re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1];LRA=re.findall(r'LRA:\s+([\d.]+) LU',e)[-1];TP=re.findall(r'Peak:\s+(-?[\d.]+|-inf) dBFS',e)[-1]
    return float(I),float(LRA),TP
for f in sorted(glob.glob(sys.argv[1])):
    x=dec(f);m=x.mean(1);sr=48000
    pk=20*np.log10(np.abs(x).max()+1e-12);clip=int((np.abs(x)>=0.999).sum())
    w=int(0.1*sr);rms=[20*np.log10(np.sqrt((m[i:i+w]**2).mean())+1e-9) for i in range(0,len(m)-w,w)]
    first=[round(v) for v in rms[:5]];last=[round(v) for v in rms[-10:]]
    # first sound onset
    on=next(i for i,v in enumerate(rms) if v>-45)*0.1
    I,LRA,TP=r128(f)
    print(f"{os.path.basename(f)} dur={len(m)/sr:.2f} I={I} LRA={LRA} TP={TP} samplepk={pk:.1f} clipped={clip} onset={on:.1f}s")
    print('   last 1 s RMS per 100 ms:',last)
