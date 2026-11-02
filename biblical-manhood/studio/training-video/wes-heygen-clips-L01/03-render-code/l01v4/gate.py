import json,sys
sys.path.insert(0,'/workspace/l01v4/build')
import render_v4 as V
from tmap import s2o,o2s,CUTS
ev=json.load(open('events.json'));ev.append(dict(a=1044.36,b=1044.68,why='join-borderline P20 in r0.81',shot='61',kind='SPLIT'))
FPS=25;res=[];fail=0
def state(to):
    ts=V.o2s(to);sh=V.shot_at(ts)
    for b in V.BR:
        if b['oa']<=to<b['ob']:
            ain=1.0 if b['k']%2==0 else V.pr(to,b['oa'],0.2);aout=1-V.pr(to,b['ob']-0.16,0.16) if b['k']%2==0 else 1.0
            if ain*aout>=0.999:return 'broll'
    for o in V.OB:
        if o['oa']<=to<o['ob']:return 'board'
    # in a transition? which shots visible
    vis=set()
    for c in V.CUTS:
        if c['type']!='hard' and c['s']<=ts<c['e']:vis={c['a'],c['b']};break
    if not vis:vis={sh['id']}
    wes_vis=any(V.IX[i]['kind'] in('WES_FULL','SPLIT') for i in vis)
    st=V.bubble_state(ts);bub=st is not None and st[0]*(1-V.hide_alpha(ts))>0.001
    if wes_vis:return 'WES:'+'/'.join(sorted(vis))
    if bub:return 'BUBBLE:'+'/'.join(sorted(vis))
    return 'board-only'
for e in ev:
    o0,o1=s2o(e['a']),s2o(e['b']);bad=[]
    n=int(o0*FPS)
    while n/FPS<=o1+1e-6:
        s=state(n/FPS)
        if s.startswith('WES') or s.startswith('BUBBLE'):bad.append((round(n/FPS,2),s))
        n+=1
    ok=not bad;fail+=not ok
    res.append(dict(e,out_a=round(o0,2),out_b=round(o1,2),covered=ok,uncovered_frames=bad[:5],cover=state((o0+o1)/2)))
    print('OK ' if ok else 'BAD',e['a'],e['why'],'->',res[-1]['cover'],bad[:3])
json.dump(dict(events=res,failed=fail),open('/workspace/l01v4/qc/gate_result.json','w'),indent=0);print('FAILED',fail,'of',len(ev))
