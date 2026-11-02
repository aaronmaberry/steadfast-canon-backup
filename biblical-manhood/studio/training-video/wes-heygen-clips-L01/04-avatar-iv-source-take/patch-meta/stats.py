import json,sys,numpy as np
S=json.load(open('../L01-build-2026-10-29/storyboard-retimed-L01-v2.json'))
def kind(t):
  for s in S:
    if s['t_in']<=t<s['t_out']: return s['kind']
def load(fs):
  F=[];[F.extend(json.load(open(f))['frames']) for f in fs];return [f for f in F if 'arc' in f]
def rep(F,name):
  a=np.array([f['arc'] for f in F]);t=np.array([f['t'] for f in F])
  D=[];cur=None
  for f in F:
    if f['arc']<0.8:
      cur=[f['t'],f['t']] if cur is None else [cur[0],f['t']]
    else:
      if cur and cur[1]-cur[0]>=0.4-1e-6:D.append(cur)
      cur=None
  full=[d for d in D if kind(d[0]) in('WES_FULL',)];fs=[d for d in D if kind(d[0]) in('WES_FULL','SPLIT')]
  i=a.argmin()
  print(f"{name}: mean {a.mean():.4f} median {np.median(a):.4f} p5 {np.percentile(a,5):.4f} p1 {np.percentile(a,1):.4f} min {a.min():.4f}@{t[i]:.2f}s <0.80 {100*(a<0.8).mean():.1f}% | sustained<0.80: all {len(D)}, WES_FULL {len(full)}, WES_FULL+SPLIT {len(fs)}")
  print('  WES_FULL dips:',[f'{x:.1f}-{y:.1f}' for x,y in full])
rep(load([f'FULL-seg{i}-perframe.json' for i in range(4)]),'ORIGINAL')
rep(load([f'PATCHED-seg{i}-perframe.json' for i in range(4)]),'PATCHED')
