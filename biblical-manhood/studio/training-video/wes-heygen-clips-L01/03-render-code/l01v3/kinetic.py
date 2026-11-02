"""Pick kinetic word-board cutaways over the remaining chin-jut / hand moments in CARD and PANEL shots (wesqc output)."""
import json,sys
sys.path.insert(0,'/workspace/l01v3/build');from tmap import s2o,o2s,CUTS
W=json.load(open('/workspace/artifacts/training/lesson-plan-2026-10-26/L01-audio-2026-10-29/v2/L01-A-Quiet-Tuesday-v2_words.json'))
W=[w for w in W if not any(a-0.02<=w['start']<b for a,b,_ in CUTS)]
d=json.load(open(sys.argv[1]));BR=json.load(open('broll_plan_v3.json'))
fr=[r for r in d['frames'] if r[1] in('CARD','PANEL')]
cl=[]
for t,_,h,j,ns in fr:
    if cl and t-cl[-1][1]<0.6:cl[-1][1]=t;cl[-1][3]|=h
    else:cl.append([t,t,1,h])
cl=[c for c in cl if c[1]-c[0]>=0.35 or c[3]]
# to src, pad, merge within 3 s
iv=[[o2s(a)-0.4,o2s(b)+0.6] for a,b,_,_ in cl];iv.sort();M=[]
for a,b in iv:
    if M and a-M[-1][1]<3.0:M[-1][1]=max(M[-1][1],b)
    else:M.append([a,b])
gaps=[(W[i]['end'],W[i+1]['start']) for i in range(len(W)-1) if W[i+1]['start']-W[i]['end']>=0.2]
gaps2=[(W[i]['end'],W[i+1]['start']) for i in range(len(W)-1) if W[i+1]['start']-W[i]['end']>=0.1]
out=[]
for a,b in M:
    if b-a<2.4:m=(a+b)/2;a,b=m-1.2,m+1.2
    ga=[g for g in gaps if g[1]<=a+0.05 and a-g[1]<2.5];gb=[g for g in gaps if g[0]>=b-0.05 and g[0]-b<2.5]
    if not ga:ga=[g for g in gaps2 if g[1]<=a+0.05 and a-g[1]<2.5]
    if not gb:gb=[g for g in gaps2 if g[0]>=b-0.05 and g[0]-b<2.5]
    if not ga or not gb:print('no gap',a,b);continue
    A=max(ga,key=lambda g:g[1]);Bg=min(gb,key=lambda g:g[0])
    a2=A[1]-0.03;b2=Bg[0]+min(0.25,(Bg[1]-Bg[0])/2)
    # skip if fully inside existing b-roll
    if any(x['a']<=a2 and b2<=x['b'] for x in BR):continue
    ws=[(w['word'],round(w['start']-0.04,3)) for w in W if a2-0.01<=w['start']<b2]
    out.append(dict(id='K%02d'%len(out),kind='KINETIC',t0=round(a2,3),t1=round(b2,3),spec=dict(words=ws)))
# merge boards closer than 1.5 s; skip the closing shot (intro J closing stays on Wes)
mm=[]
for o in out:
    if mm and o['t0']-mm[-1]['t1']<1.5:mm[-1]['t1']=o['t1'];mm[-1]['spec']['words']+=[w for w in o['spec']['words'] if w[1]>mm[-1]['spec']['words'][-1][1]]
    else:mm.append(o)
for o in mm:
    if o['t1']>1223.95:o['t1']=1223.9;o['spec']['words']=[w for w in o['spec']['words'] if w[1]<1223.9]
out=[o for o in mm if o['t0']<1223.0]
for i,o in enumerate(out):o['id']='K%02d'%i
# pages: sentence by sentence, <=14 words a page
for o in out:
    pg=[];cur=[]
    for w,t in o['spec']['words']:
        cur.append((w,t))
        if w[-1] in '.?!' or (w[-1]=='"' and len(w)>1 and w[-2] in '.?!') or len(cur)>=14:pg.append(cur);cur=[]
    if cur:pg.append(cur)
    o['spec']['pages']=pg
# drop overlaps with broll by trimming none; report
for o in out:
    ov=[x['id'] for x in BR if x['a']<o['t1'] and o['t0']<x['b']]
    o['overlaps_broll']=ov
    print(o['id'],round(s2o(o['t0']),2),round(s2o(o['t1']),2),round(o['t1']-o['t0'],2),ov,' '.join(w for w,_ in o['spec']['words']))
json.dump(out,open('kinetic.json','w'),indent=0);print(len(out),'kinetic boards',round(sum(o['t1']-o['t0'] for o in out),1),'s')
