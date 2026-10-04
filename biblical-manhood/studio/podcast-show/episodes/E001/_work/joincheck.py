import json, numpy as np, wavio, subprocess
sr=44100; y=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','out/master_f32.wav','-f','f32le','-ac','1','-'],capture_output=True).stdout,np.float32)
tl={x['n']:x for x in json.load(open('out/timeline.json'))}
def feats(n):
    t=tl[n]; a=y[int(t['start']*sr):int(t['end']*sr)]
    w=441; k=len(a)//w; d=20*np.log10(np.sqrt((a[:k*w].reshape(k,w)**2).mean(1))+1e-9); g=d[d>-45]
    lv=10*np.log10(np.mean(10**(g/10)))
    N=2048; H=1024; cs=[]; fs=[]
    fr=np.fft.rfftfreq(N,1/sr); win=np.hanning(N)
    for i in range(0,len(a)-N,H):
        x=a[i:i+N]
        if np.sqrt(np.mean(x**2))<0.02: continue
        S=np.abs(np.fft.rfft(x*win)); cs.append((fr*S).sum()/S.sum())
        r=np.correlate(x,x,'full')[N-1:]; lo,hi=int(sr/300),int(sr/60)
        k=lo+np.argmax(r[lo:hi])
        if r[k]>0.5*r[0]: fs.append(sr/k)
    cen=np.median(cs); f0=np.median(fs) if fs else np.nan
    words=len([w for w in t['words']]); wpm=words/((t['end']-t['start'])/60)
    return lv,cen,f0,wpm
NEW={4,5,6,7,8,9,10,11,72,148,240,243,254,285,296}
rows=[]
for n in sorted(tl):
    if n in NEW or any(abs(n-m)<=6 for m in NEW):
        lv,cen,f0,wpm=feats(n); rows.append((n,tl[n]['spk'],n in NEW,float(lv),float(cen),float(f0),float(wpm)))
json.dump(rows,open('out/joincheck.json','w'))
for spk in ('WES','JONATHON'):
    for grp in (True,False):
        r=[x for x in rows if x[1]==spk and x[2]==grp]
        print(spk,'NEW' if grp else 'neighbors',len(r),'level %.1f dB  centroid %.0f Hz  F0 %.0f Hz  wpm %.0f'%tuple(np.nanmedian([x[i] for x in r]) for i in (3,4,5,6)))
for x in rows:
    if x[2]: print(x[0],x[1][0],'level %.1f cen %.0f f0 %.0f wpm %.0f'%x[3:])
