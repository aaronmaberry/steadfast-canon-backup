import json,numpy as np,soundfile as sf
W='/workspace/artifacts/training/lesson-plan-2026-10-26/L01-audio-2026-10-29/v2/delivery/L01-A-Quiet-Tuesday-v2-minus26-LUFS.wav'
x,sr=sf.read(W);x=x.mean(1) if x.ndim>1 else x
hop=int(sr*0.01);n=len(x)//hop
db=20*np.log10(np.sqrt((x[:n*hop].reshape(n,hop)**2).mean(1))+1e-9)
q=db<-55
# silence runs >=0.25s
runs=[];i=0
while i<n:
  if q[i]:
    j=i
    while j<n and q[j]:j+=1
    if j-i>=25: runs.append((i/100,j/100))
    i=j
  else:i+=1
S=json.load(open('../../L01-build-2026-10-29/storyboard-retimed-L01-v2.json'))
def kind(t):
  for s in S:
    if s['t_in']<=t<s['t_out']: return s['kind']
targets=[(161.6,162.0),(208.6,209.0),(288.4,289.0),(605.0,605.8),(668.4,673.0),(720.4,720.8),(907.4,908.2),(917.2,917.6),(950.6,956.0),(1024.8,1026.4),(1047.8,1048.6),(1077.6,1079.2),(1097.2,1097.6),(1123.2,1126.6),(1203.6,1204.8),(1214.4,1220.8),
 (52.2,52.6),(121.0,121.4),(127.0,127.4),(300.0,300.4),(379.4,379.8),(403.6,404.0),(478.6,479.2),(501.0,501.6),(536.0,536.6),(865.6,870.6),(886.0,886.6),(1186.6,1193.0)]
def pick(t,side):
  # silence whose relevant edge is 1.5..3 s from t, else nearest beyond 1.5 up to 8
  best=None
  for a,b in runs:
    m=(a+b)/2
    d=(t-m) if side<0 else (m-t)
    if d>=1.5 and d<=8:
      sc=0 if d<=3 else d
      if best is None or sc<best[0] or (sc==best[0] and (b-a)>best[2]): best=(sc,m,b-a)
  return best
P=[]
for a,b in targets:
  L=pick(a,-1);R=pick(b,1)
  P.append([round(round(L[1]/0.04)*0.04,2),round(round(R[1]/0.04)*0.04,2),a,b,kind(a),round(L[2],2),round(R[2],2)])
P.sort()
M=[]
for p in P:
  if M and p[0]<=M[-1][1]: M[-1][1]=max(M[-1][1],p[1]);M[-1][3]=p[3];M[-1].append(p[2])
  else:M.append(p)
tot=0
for m in M: print(m, round(m[1]-m[0],2)); tot+=m[1]-m[0]
print('total s',tot,len(M))
json.dump([dict(s=m[0],e=m[1],dip=[m[2],m[3]],kind=m[4]) for m in M],open('windows.json','w'),indent=0)
