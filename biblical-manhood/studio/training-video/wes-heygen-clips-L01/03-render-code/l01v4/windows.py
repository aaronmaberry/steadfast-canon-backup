import json
W=json.load(open('/workspace/artifacts/training/lesson-plan-2026-10-26/L01-audio-2026-10-29/v2/L01-A-Quiet-Tuesday-v2_words.json'))
ev=json.load(open('events.json'))
ev.append(dict(a=1044.36,b=1044.68,why='join-borderline P20 in r0.81',shot='61',kind='SPLIT'))
ac=json.load(open('/workspace/l01v2/audio_cuts.json'))['cuts']
def snap(t,dirn):
    # nearest inter-word gap midpoint within 0.8 s, preferring direction
    best=None
    for w1,w2 in zip(W,W[1:]):
        if w2['start']-w1['end']<0.06:continue
        m=(w1['end']+w2['start'])/2
        if abs(m-t)<0.9 and (dirn<0 and m<=t+0.1 or dirn>0 and m>=t-0.1):
            if best is None or abs(m-t)<abs(best-t):best=m
    return best if best is not None else t
cov=[];hide=[]
for e in sorted(ev,key=lambda x:x['a']):
    vis=e['kind'] in('WES_FULL','SPLIT') or 'AUDIO' in e['why']
    if vis:
        a,b=e['a']-1.0,e['b']+1.0
        if b-a<2.6:m=(a+b)/2;a,b=m-1.3,m+1.3
        L=cov
    else:a,b=e['a']-0.5,e['b']+0.5;L=hide
    if L and a-L[-1]['b']<1.6 and b-L[-1]['a']<(6.5 if vis else 99):L[-1]['b']=max(L[-1]['b'],b);L[-1]['why'].append(e['why'])
    else:L.append(dict(a=a,b=b,why=[e['why']],shot=e['shot'],kind=e['kind']))
for c in cov:c['a']=round(snap(c['a'],-1),3);c['b']=round(snap(c['b'],1),3)
# audio-cut covers must contain cut +-0.3
for c in cov:
    for x in ac:
        if c['a']<x['b'] and c['b']>x['a']:c['a']=min(c['a'],x['a']-0.3);c['b']=max(c['b'],x['b']+0.3)
for h in hide:h['a']=round(h['a'],3);h['b']=round(h['b'],3)
json.dump(dict(cover=cov,hide=hide),open('windows.json','w'),indent=0)
for c in cov:print('COV',c['a'],c['b'],round(c['b']-c['a'],2),c['shot'],c['kind'],c['why'],'|',' '.join(w['word'] for w in W if c['a']-3<w['start']<c['b']+2))
for h in hide:print('HIDE',h['a'],h['b'],h['shot'],h['why'])
print(len(cov),len(hide))
