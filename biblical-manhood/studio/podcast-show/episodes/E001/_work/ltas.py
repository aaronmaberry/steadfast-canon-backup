import numpy as np, wavio, glob, sys
B=[(60,250),(250,500),(500,1000),(1000,2000),(2000,4000),(4000,8000),(8000,16000)]
def ltas(f):
    sr,a=wavio.read(f); a=a.astype(np.float32).reshape(-1)
    N=4096;H=2048;fr=np.fft.rfftfreq(N,1/sr);w=np.hanning(N);P=np.zeros(len(fr));c=0
    for i in range(0,len(a)-N,H):
        x=a[i:i+N]
        if np.sqrt(np.mean(x**2))<0.01: continue
        P+=np.abs(np.fft.rfft(x*w))**2; c+=1
    P/=c; tot=P[(fr>60)&(fr<16000)].sum()
    return [10*np.log10(P[(fr>=lo)&(fr<hi)].sum()/tot) for lo,hi in B]
pairs=[('lines/L068.K08.wav','lines/L072.P1W.wav'),('lines/L236.K24.wav','lines/L240.P1W.wav'),('lines/L250.K24.wav','lines/L254.P1W.wav'),('lines/L281.K28.wav','lines/L285.P1W.wav'),('lines/L004.I1W.wav','lines/L004.O1W.wav'),('lines/L005.I1J.wav','lines/L005.O1J.wav'),('lines/L144.K15.wav','lines/L148.R3J.wav')]
print('bands',B)
for o,n in pairs:
    a=np.array(ltas(o)); b=np.array(ltas(n)); print(n.split('/')[1][:9], 'new-old dB:',' '.join('%+5.1f'%x for x in b-a))
