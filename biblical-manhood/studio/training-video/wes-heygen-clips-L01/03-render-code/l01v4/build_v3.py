import json,re,sys,copy
from collections import Counter
sys.path.insert(0,'/workspace/l01p6');sys.path.insert(0,'/workspace/l01v4/build')
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
# v3: callouts carry word times (word-by-word build); closing (intro J style) on the last Wes shot
WW=[w for w in W]
def words_from(at,txt):
    n=len([x for x in txt.split() if nz(x)]);i=min(range(len(W)),key=lambda k:abs(W[k]['start']-0.04-at));return [round(W[i+j]['start']-0.04,3) for j in range(n)]
for s_ in shots:
    if s_['kind']=='WES_FULL' and 'callouts' in s_['spec'] and s_['id']!='71':
        s_['spec']['callouts']=[(t,at,words_from(at,t)) for t,at in s_['spec']['callouts']]
ix71=[x for x in shots if x['id']=='71'][0];ix71['spec']={'close':[("That was your first yes.",cue('That was your first',ix71['t0'],ix71['t1'])),("Don't waste it.",cue("Don't waste it.",ix71['t0'],ix71['t1']))]}
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
BR=json.load(open('/workspace/l01v4/build/broll_plan_v3.json'))
HIDE=json.load(open('/workspace/l01v2/build/windows.json'))['hide']
# v3: hide the bubble over the three week cuts that land in bubble shots (A agenda, B shot 10, C shot 17)
HIDE+= [dict(a=36.88,b=38.40,why=['AUDIO CUT A this week.'],shot='2',kind='AGENDA'),dict(a=197.68,b=198.62,why=['AUDIO CUT B this week,'],shot='10',kind='TYPE_BOARD_BUBBLE'),dict(a=263.62,b=268.00,why=['AUDIO CUT C weekend retreat sentence'],shot='17',kind='BRANDED_STILL_BUBBLE')]
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
H5={int(k):v for k,v in json.load(open('/workspace/l01v3/qc/hp0.json')).items()}
def hands_in(a,b,box):
    x0,y0,w,h=box;n=int(a*25)//5*5
    while n<=b*25:
        for hb in H5.get(n,{'h':[]})['h']:
            if hb[1]<y0+h-15 and hb[2]>x0+15 and hb[0]<x0+w-15:return True
        n+=5
    return False
FR=[('FULL',1.0,0),('CARD',1.0,0)]
framing=[];fi=0
for s in shots:
    if s['kind']!='WES_FULL':continue
    for a,b in visible_runs(s['t0x'],s['t1x']):
        t=a
        while b-t>8.0:
            # split at a gap between 4 and 8 s in
            cands=[g for g in gaps if t+4.0<=g<=t+7.8 and g<b-2.0]
            if not cands:break
            g=max(cands);framing.append(dict(shot=s['id'],a=t,b=g));t=g
        framing.append(dict(shot=s['id'],a=t,b=b))
for f in framing:
    ts0,ts1=o2s(s2o(f['a'])),f['b']
    f['f']=FR[1] if hands_in(f['a']-0.2,f['b']+0.2,(0,0,1920,1080)) else FR[0]
# light-leak (brand-colour glow sweep in the empty beat) on dips at section changes with a pause >= 0.6 s, at most 5, spaced >= 120 s
last=-1e9;nl=0
for c in cuts:
    if c['type']=='dip' and c['gap'][1]-c['gap'][0]>=0.6 and c['s']-last>=120 and nl<5 and c['b']!='72':
        D=min(0.9,c['gap'][1]-c['gap'][0]-0.04);m=(c['gap'][0]+c['gap'][1])/2;s0=m-D/2;e=m+D/2
        c.update(s=s0,e=e,cut=m,out=[s0,s0+0.35*D],empty=[s0+0.35*D,s0+0.65*D],inn=[s0+0.65*D,e],leak=True);last=c['s'];nl+=1
        IXS={x['id']:x for x in shots};IXS[c['a']]['t1x']=m;IXS[c['b']]['t0x']=m
KIN=json.load(open('/workspace/l01v4/build/kinetic.json'))
json.dump(dict(fps=25,end_src=END_SRC,shots=shots,cuts=cuts,bubble_runs=runs,overlay_boards=[ob]+KIN,broll=BR,hide=HIDE,framing=framing),open('/workspace/l01v4/build/edl_v4.json','w'),indent=1)
C=Counter(c['type'] for c in cuts);print('framing modes',Counter(f['f'][0] for f in framing),'full s',round(sum(f['b']-f['a'] for f in framing if f['f'][0]=='FULL'),1),'card s',round(sum(f['b']-f['a'] for f in framing if f['f'][0]=='CARD'),1));print(len(shots),'shots',C,'dip share %.1f%%'%(100*C['dip']/len(cuts)))
lr=[f['b']-f['a'] for f in framing];print('framing segs',len(framing),'max',round(max(lr),2))
