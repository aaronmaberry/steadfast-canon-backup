import json,sys,numpy as np
S=json.load(open('../../L01-build-2026-10-29/storyboard-retimed-L01-v2.json'))
def kind(t):
  for s in S:
    if s['t_in']<=t<s['t_out']: return s['kind']
F=[];[F.extend(json.load(open(f'../FULL-seg{i}-perframe.json'))['frames']) for i in range(4)];F=[f for f in F if 'arc' in f];F.sort(key=lambda f:f['i'])
acc=sys.argv[1];V={}
if acc!='none':
  for a in json.load(open(acc)):
    s0=round(a['s']*25);q=json.load(open(f"t1-{a['id']}-perframe.json"))['frames']
    for k in range(a['i_in'],a['i_out']+1):
      if 'arc' in q[k]:V[s0+k]=q[k]['arc']
# optional measured override from direct scoring of the spliced file
if len(sys.argv)>2:
  for f in json.load(open(sys.argv[2]))['frames']:
    if 'arc' in f:V[f['i']]=f['arc']
a=np.array([V.get(f['i'],f['arc']) for f in F]);t=np.array([f['t'] for f in F])
D=[];cur=None
for v,tt in zip(a,t):
  if v<0.8: cur=[tt,tt] if cur is None else [cur[0],tt]
  else:
    if cur and cur[1]-cur[0]>=0.4-1e-6:D.append(cur)
    cur=None
K=lambda ks:[d for d in D if kind(d[0]) in ks]
i=a.argmin()
print(f"mean {a.mean():.4f} p5 {np.percentile(a,5):.4f} min {a.min():.4f}@{t[i]:.2f}s ({kind(t[i])}) <0.80 {100*(a<0.8).mean():.1f}% | sustained<0.80 all {len(D)} WES_FULL {len(K(['WES_FULL']))} SPLIT {len(K(['SPLIT']))}")
print(' WES_FULL:',[f'{x:.1f}-{y:.1f}' for x,y in K(['WES_FULL'])])
