import json,re,sys,copy
sys.path.insert(0,'/workspace/l01p6');sys.path.insert(0,'/workspace/l01v3/build')
from spec import S,COVERS
from tmap import s2o,o2s,CUTS
LP='/workspace/artifacts/training/lesson-plan-2026-10-26/'
W=json.load(open(LP+'L01-audio-2026-10-29/v2/L01-A-Quiet-Tuesday-v2_words.json'))
V1=json.load(open('/workspace/l01p6/edl.json'))
nz=lambda s:re.sub(r"[^a-z0-9']","",s.lower().replace('’',"'"))
WN=[nz(w['word']) for w in W]
def cue(ph,a,b):
    p=[nz(x) for x in ph.split()];p=[x for x in p if x]
    for i,w in enumerate(W):
        if w['start']<a-0.3 or w['start']>b:continue
        if WN[i:i+len(p)]==p:return round(w['start']-0.04,3)
    print(f'CUE MISS: {ph!r} in {a}-{b}');return a
def gap(c):
    pe=max([w['end'] for w in W if w['end']<=c+0.05]+[0]);ns=min([w['start'] for w in W if w['start']>=c-0.05]+[1e9])
    return pe,ns
# ---- spec changes (week fixes A + list fix + covers)
S=copy.deepcopy(S)
S[9]=dict(rows=[('You and I','You and I'),('24 lessons. One at a time.','Twenty-four of them.')],big_idx=1)
S[64]=dict(kicker='THE MOVE',big_idx=1,rows=[('Your one move:',"here's your one move."),('One meal. Phone in another room.','eat one meal'),('Not in your pocket. In another room.','Not in your')])
S[10]=dict(kicker='HOW EACH LESSON WORKS',rows=[('I teach','First, I teach.'),('You stop and write','Second, you stop'),('One move. Not a list.','you walk away')],chips=True,inset=('workbook',167.72,175.97),maxw=760)
S['60c']=dict(rows=[('The job might be over.','The job might'),("Being a man didn't clock out with it.","Being a man")],big_idx=1,full=True)
S['9c']=dict(kicker='HOW THIS WORKS',counter=(24,'Twenty-four of them.'),rows=[('lessons',None),('One. Then the next one.','One.')],full=True)
for k,v in S.items():
    for r in v.get('rows',[]):assert 'week' not in r[0].lower(),(k,r)
shots=[]
for x in V1['shots']:
    if x['id'] in('11','12','13'):continue
    sid=x['id'];k=x['kind'];key=int(sid) if sid.isdigit() else sid
    sp=dict(S.get(key,{}))
    t0,t1=x['t0'],x['t1']
    if sid=='10':t1=[y for y in V1['shots'] if y['id']=='13'][0]['t1']
    shots.append(dict(id=sid,kind=k,t0=t0,t1=t1,spec=sp))
# 60c starts at the pause before 'The boy didn't' (Aaron 17:02.7 warp)
ix={s['id']:s for s in shots};ix['60']['t1']=1022.25;ix['60c']['t0']=1022.25
END_SRC=V1['end']
for s in shots:
    a,b=s['t0'],s['t1'];sp=s['spec']
    for key in('rows','callouts','side','verse'):
        if key in sp:sp[key]=[(t,cue(ph,a,b) if ph else a) for t,ph in sp[key]]
    for key in('ref','lt','title','kat','lat','counter'):
        if key in sp:t,ph=sp[key];sp[key]=(t,cue(ph,a,b) if ph else a)
    if 'hi_at' in sp:sp['hi_at']=cue(sp['hi_at'],a,b)
# overlay board 9c (covers both L031 audio cuts)
_pe,_ns=gap(158.6);ob=dict(id='9c',kind='COVER_BOARD',t0=149.433,t1=round((_pe+_ns)/2,3),spec=S['9c'])
sp=ob['spec'];sp['rows']=[(t,cue(ph,ob['t0'],ob['t1']) if ph else None) for t,ph in sp['rows']];sp['counter']=(24,cue(sp['counter'][1],ob['t0'],ob['t1']))
sp['rows'][0]=(sp['rows'][0][0],sp['counter'][1]+0.6)
# ---- transitions: rotate types; dip <=40%
WESK=('WES_FULL','SPLIT')
cuts=[];i_rot=0;ROT=['xfade','push','dip','xfade','dip','push']
for A,B in zip(shots,shots[1:]):
    c=B['t0'];pe,ns=gap(c)
    if B['kind']=='LOGO_END':pe,ns=END_SRC-3.8-0.6,END_SRC-3.8+0.4
    lo,hi=pe+0.02,ns-0.02;L=hi-lo
    if A['kind'] in WESK and B['kind'] in WESK and A['kind']!=B['kind']:typ='morph'
    elif A['kind']==B['kind']=='WES_FULL' or (A['kind']==B['kind']=='SPLIT'):typ='hard'
    elif B['kind']=='LOGO_END':typ='dip'
    else:typ=ROT[i_rot%len(ROT)];i_rot+=1
    if typ=='hard':
        m=round((lo+hi)/2*25)/25;cuts.append(dict(a=A['id'],b=B['id'],type='hard',cut=m,s=m,e=m,gap=[pe,ns]))
    else:
        D={'dip':min(0.5,max(L,0.2)),'xfade':min(0.5,max(L,0.24)),'push':0.5,'morph':0.7}[typ]
        if typ in('push','morph'):m=(lo+hi)/2;s0=m-D/2;e=m+D/2
        else:e=hi if L<D else (lo+hi)/2+D/2;s0=e-D
        cuts.append(dict(a=A['id'],b=B['id'],type=typ,s=s0,e=e,cut=s0+0.5*D,gap=[pe,ns],in_speech=(typ in('dip',) and L<0.2)))
        if typ=='dip':cuts[-1].update(out=[s0,s0+0.4*D],empty=[s0+0.4*D,s0+0.6*D],inn=[s0+0.6*D,e])
    A['t1x']=cuts[-1]['cut'];B['t0x']=cuts[-1]['cut']
shots[0]['t0x']=0;shots[-1]['t1x']=END_SRC+10
BUBK=('BUBBLE','AGENDA')
runs=[];cur=None
for s in shots:
    if any(k in s['kind'] for k in BUBK):
        if cur is None:cur=[s['id'],s['id']];runs.append(cur)
        else:cur[1]=s['id']
    else:cur=None
# ---- B-roll + hide windows
BR=json.load(open('/workspace/l01v3/build/broll_plan.json'))
HIDE=json.load(open('/workspace/l01v3/build/windows.json'))['hide']
# ---- WES_FULL framing segments: alternate punch-in framings at word gaps so no single framing runs > 8 s on screen
def visible_runs(a,b):
    # sub-intervals of [a,b) not under b-roll/board covers
    cov=sorted([(x['a'],x['b']) for x in BR]+[(ob['t0'],ob['t1'])])
    segs=[];t=a
    for c0,c1 in cov:
        if c1<=t or c0>=b:continue
        if c0>t:segs.append((t,c0))
        t=max(t,c1)
    if t<b:segs.append((t,b))
    return segs
gaps=[(W[i]['end']+W[i+1]['start'])/2 for i in range(len(W)-1) if W[i+1]['start']-W[i]['end']>=0.12]
FR=[('A',1.12,0),('B',1.22,-90),('A',1.12,0),('C',1.20,90)]
framing=[];fi=0
for s in shots:
    if s['kind']!='WES_FULL':continue
    for a,b in visible_runs(s['t0x'],s['t1x']):
        t=a
        while b-t>8.0:
            # split at a gap between 4 and 8 s in
            cands=[g for g in gaps if t+4.0<=g<=t+7.8 and g<b-2.0]
            if not cands:break
            g=max(cands);framing.append(dict(shot=s['id'],a=t,b=g,f=FR[fi%4]));fi+=1;t=g
        framing.append(dict(shot=s['id'],a=t,b=b,f=FR[fi%4]));fi+=1
json.dump(dict(fps=25,end_src=END_SRC,shots=shots,cuts=cuts,bubble_runs=runs,overlay_boards=[ob],broll=BR,hide=HIDE,framing=framing),open('/workspace/l01v3/build/edl_v2.json','w'),indent=1)
from collections import Counter
C=Counter(c['type'] for c in cuts);print(len(shots),'shots',C,'dip share %.1f%%'%(100*C['dip']/len(cuts)))
lr=[f['b']-f['a'] for f in framing];print('framing segs',len(framing),'max',round(max(lr),2))
