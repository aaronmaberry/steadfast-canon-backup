# cmp.py PID take -> stats, best in/out splice frames
import json,sys,numpy as np
pid,tk=sys.argv[1],sys.argv[2]
W={w['id']:w for w in json.load(open('windows.json'))}[pid]
o=json.load(open(f'orig-{pid}-perframe.json'))['frames'];p=json.load(open(f'{tk}-{pid}-perframe.json'))['frames']
n=min(len(o),len(p));o,p=o[:n],p[:n]
A=lambda F,k:np.array([f.get(k,np.nan) if f.get(k) is not None else np.nan for f in F],float)
ao,ap=A(o,'arc'),A(p,'arc')
def st(a):
  a=a[~np.isnan(a)];return dict(mean=round(a.mean(),4),p5=round(np.percentile(a,5),4),min=round(a.min(),4),lt80=int((a<0.8).sum()))
# sustained dips <0.80 (>=10 frames=0.4s)
def sus(a):
  c=0;k=0
  for v in a:
    if v<0.8:k+=1
    else:
      if k>=10:c+=1
      k=0
  return c+(k>=10)
fps=25;t0=W['s'];di=int((W['dip'][0]-t0)*fps);de=int((W['dip'][1]-t0)*fps)+1
r=dict(id=pid,take=tk,win=[W['s'],W['e']],orig=st(ao),patch=st(ap),orig_dip=st(ao[di:de]),patch_dip=st(ap[di:de]),sus_orig=sus(ao),sus_patch=sus(ap))
# splice cost per frame: pose diff (cx, w) + both mouths closed
cx=lambda F:A(F,'cx');w=A(o,'w');wp=A(p,'w');go=A(o,'gap');gp=A(p,'gap')
dpos=np.abs(cx(o)-cx(p))*1920+np.abs(w-wp)
cost=dpos+200*np.clip(go-0.07,0,None)+200*np.clip(gp-0.07,0,None)
m=int(1.6*fps)
i_in=int(np.nanargmin(cost[:min(m,n//3)]));i_out=n-min(m,n//3)+int(np.nanargmin(cost[n-min(m,n//3):]))
r.update(in_frame=i_in,out_frame=i_out,in_cost=round(float(cost[i_in]),2),out_cost=round(float(cost[i_out]),2),
 in_dpx=round(float(dpos[i_in]),2),out_dpx=round(float(dpos[i_out]),2),gap_in=[round(go[i_in],3),round(gp[i_in],3)],gap_out=[round(go[i_out],3),round(gp[i_out],3)],
 between=st(ap[i_in:i_out]),between_orig=st(ao[i_in:i_out]))
# lag check via gap correlation
g1=np.nan_to_num(go-np.nanmean(go));g2=np.nan_to_num(gp-np.nanmean(gp))
lags=range(-5,6);cc=[np.corrcoef(np.roll(g2,l)[10:-10],g1[10:-10])[0,1] for l in lags];r['lag_frames']=list(lags)[int(np.argmax(cc))];r['gap_corr']=round(max(cc),3)
print(json.dumps(r))
