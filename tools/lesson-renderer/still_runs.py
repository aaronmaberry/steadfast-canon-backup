#!/usr/bin/env python3
"""Gate: no uncovered WES_FULL still run > 8 s."""
import os,sys,json
WORK=os.environ.get('LESSON_WORK', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
E=json.load(open(f'{WORK}/p7/edl.json'))
kin=E.get('kinetic') or []
def covered(t0,t1):
    for k in kin:
        if k.get('cover') and not (k['t1']<=t0 or k['t0']>=t1):
            return True
    return False
runs=[];cur=None
for s in E['shots']:
    if s['kind']=='WES_FULL':
        a,b=s['t0x'],s['t1x']
        # subtract kinetic covers inside
        segs=[(a,b)]
        for k in sorted([k for k in kin if k.get('cover')], key=lambda x:x['t0']):
            n=[]
            for u,v in segs:
                if k['t1']<=u or k['t0']>=v: n.append((u,v)); continue
                if k['t0']>u: n.append((u,k['t0']))
                if k['t1']<v: n.append((k['t1'],v))
            segs=n
        for u,v in segs:
            if v-u>8.0: runs.append((round(u,2),round(v,2),round(v-u,2)))
print('runs>8s', len(runs), runs)
print('max', max((r[2] for r in runs), default=0))
sys.exit(1 if runs else 0)
