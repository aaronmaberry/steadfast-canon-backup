import subprocess,glob,os,numpy as np,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
fs=sorted(glob.glob('raw/*.mp3'))
fig,ax=plt.subplots(len(fs),2,figsize=(18,3.2*len(fs)))
for r,f in enumerate(fs):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar','22050','-'],capture_output=True).stdout
    m=np.frombuffer(b,np.float32);sr=22050;t=np.arange(len(m))/sr
    w=int(.05*sr);env=[20*np.log10(np.sqrt((m[i:i+w]**2).mean())+1e-9) for i in range(0,len(m)-w,w)]
    a=ax[r,0];a.plot(t,m,lw=.3);a2=a.twinx();a2.plot(np.arange(len(env))*.05,env,'r',lw=.8);a2.set_ylim(-90,0)
    a.set_title(os.path.basename(f)+'  waveform + RMS dB (red)');a.set_xlim(0,30)
    a=ax[r,1];a.specgram(m,NFFT=2048,Fs=sr,noverlap=1536,cmap='magma',vmin=-120);a.set_ylim(0,8000);a.set_title('spectrogram 0-8 kHz')
    # report end time
    e=np.array(env);last=np.where(e>-50)[0][-1]*.05;print(os.path.basename(f),'last audio above -50 dB at',round(last,2),'s')
plt.tight_layout();plt.savefig('qa/overview.png',dpi=60)
