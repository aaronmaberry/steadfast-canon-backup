import json,subprocess,os,sys
tk=sys.argv[1] if len(sys.argv)>1 else 't1'
W=json.load(open('windows.json'));R=[]
for w in W:
  p=w['id']
  if not (os.path.exists(f'orig-{p}-perframe.json') and os.path.exists(f'{tk}-{p}-perframe.json')):continue
  if not os.path.exists(f'join_{p}_{tk}.json'): subprocess.run(['python3','join.py',p,tk],capture_output=True)
  c=json.loads(subprocess.run(['python3','cmp.py',p,tk],capture_output=True,text=True).stdout)
  j=json.load(open(f'join_{p}_{tk}.json'));i0,i1=j['i_in'],j['i_out']
  import numpy as np
  o=json.load(open(f'orig-{p}-perframe.json'))['frames'];q=json.load(open(f'{tk}-{p}-perframe.json'))['frames']
  ao=np.array([f.get('arc',np.nan) for f in o][i0:i1+1]);aq=np.array([f.get('arc',np.nan) for f in q][i0:i1+1])
  def sus(a):
    c=k=0
    for v in a:
      if v<0.8:k+=1
      else:c+=k>=10;k=0
    return c+(k>=10)
  d=dict(id=p,kind=w['kind'],win=[w['s'],w['e']],i_in=i0,i_out=i1,n=len(q),d_in=round(j['d'][i0],2),d_out=round(j['d'][i1],2),
    o_mean=round(np.nanmean(ao),4),q_mean=round(np.nanmean(aq),4),o_min=round(np.nanmin(ao),4),q_min=round(np.nanmin(aq),4),
    o_lt80=int((ao<0.8).sum()),q_lt80=int((aq<0.8).sum()),o_sus=sus(ao),q_sus=sus(aq),o_dipmean=c['orig_dip']['mean'],q_dipmean=c['patch_dip']['mean'],lag=c['lag_frames'],corr=c['gap_corr'])
  d['accept']=bool(d['q_mean']>=d['o_mean'] and d['q_min']>d['o_min'] and d['q_sus']<=d['o_sus'] and (d['q_lt80']<=0.5*d['o_lt80'] or d['q_mean']>=d['o_mean']+0.01) and d['q_lt80']<d['o_lt80'] and max(d['d_in'],d['d_out'])<6 and abs(d['lag'])<=1)
  R.append(d);print(json.dumps(d))
json.dump(R,open(f'accept_{tk}.json','w'),indent=1)
