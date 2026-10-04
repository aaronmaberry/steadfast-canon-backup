# Build v1 line 239 (script line 404) with the new "I wrote it." from P1W in place of "I wrote it, and it's coming."
import json, numpy as np, wavio
sr,K=wavio.read('raw/K24.wav'); _,P=wavio.read('raw/P1W.wav')
K=K.astype(np.float32).reshape(-1); P=P.astype(np.float32).reshape(-1)
S=lambda t:int(round(t*sr))
def arms(x):
    w=441; n=len(x)//w; d=20*np.log10(np.sqrt((x[:n*w].reshape(n,w)**2).mean(1))+1e-9); g=d[d>-45]; return 10*np.log10(np.mean(10**(g/10)))
# match by the phrase before the cut ("The Way of Godly Men."), so the new soft read keeps its own shape
old_iw=K[S(17.16):S(18.16)]; new_iw=P[S(23.04):S(24.16)]
g=arms(old_iw)-arms(new_iw); print('level old',round(arms(old_iw),2),'new',round(arms(new_iw),2),'gain',round(g,2))
new=P[S(24.35):S(25.02)]*10**(g/20)
def fade(x,ms=5):
    n=int(sr*ms/1000); r=np.linspace(0,1,n,dtype=np.float32); x=x.copy(); x[:n]*=r; x[-n:]*=r[::-1]; return x
a=K[S(15.52):S(18.30)]; b=K[S(19.64):S(37.71)]
pad=np.zeros(S(0.08),np.float32)
out=np.concatenate([a,fade(new),pad,b])
wavio.write('lines/L239.S404.wav',sr,out)
# words: shift
S24=json.load(open('raw/K24.split.json')); Pw=json.load(open('raw/P1W.split.json'))['words']
t0=15.52; ws=[]
for w in S24['words']:
    m=(w[1]+w[2])/2
    if 15.52<=m<18.30: ws.append([w[0],w[1]-t0,w[2]-t0])
off1=18.30-t0
for w in Pw:
    m=(w[1]+w[2])/2
    if 24.35<=m<25.02: ws.append([w[0],w[1]-24.35+off1,w[2]-24.35+off1])
off2=off1+(25.02-24.35)+0.08
for w in S24['words']:
    m=(w[1]+w[2])/2
    if 19.64<=m<37.71: ws.append([w[0],w[1]-19.64+off2,w[2]-19.64+off2])
dur=len(out)/sr
json.dump(dict(K='S404',words=ws,report=[dict(n=239,cov=1.0,t0=0.0,t1=round(dur,3))]),open('raw/S404.split.json','w'))
print('dur',round(dur,2),'old',round(37.71-15.52,2)); print(' '.join(w[0] for w in ws[:16]))
