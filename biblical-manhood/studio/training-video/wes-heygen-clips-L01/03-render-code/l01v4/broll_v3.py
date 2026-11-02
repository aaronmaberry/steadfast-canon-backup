"""v3 B-roll plan: v2 plan + replacements for loose matches + cover for week cut D; every edge snapped OUTWARD to an inter-word gap."""
import json,sys
sys.path.insert(0,'/workspace/l01v4/build');from tmap import s2o,CUTS
W=json.load(open('/workspace/artifacts/training/lesson-plan-2026-10-26/L01-audio-2026-10-29/v2/L01-A-Quiet-Tuesday-v2_words.json'))
# drop words removed by cuts
W=[w for w in W if not any(a-0.02<=w['start']<b for a,b,_ in CUTS)]
B=json.load(open('/workspace/l01v2/build/broll_plan.json'))
REP={5:('px7841657','pexels','Men talking to each other','https://www.pexels.com/video/men-talking-to-each-other-7841657/','a friend doing this with you (two men talking)',1.0),
     6:('px28339282','pexels','The church is white with a tall steeple','https://www.pexels.com/video/the-church-is-white-with-a-tall-steeple-28339282/','walked out of church (white steeple church)',2.0),
     14:('px4297124','pexels','A young girl writing at home','https://www.pexels.com/video/girl-child-teenager-kid-4297124/','went back to her homework (girl writing)',1.0),
     15:('px3051693','pexels','Lights from an isolated house at night','https://www.pexels.com/video/lights-from-an-isolated-house-makes-it-visible-from-the-darkness-of-the-night-3051693/','late that night, porch light on (lit house at night)',3.0),
     18:('px5534367','pexels','A man with white hair looking at the camera','https://www.pexels.com/video/a-man-with-white-hair-looking-at-the-camera-5534367/','an older man I trusted (white-haired man)',1.5),
     23:('px4052821','pexels','Man resting on sofa','https://www.pexels.com/video/man-resting-on-sofa-and-heavily-breading-4052821/','a nap is allowed (man resting on sofa; replaces bed clip with headboard line art)',0.5),
     28:('px5029481','pexels','Person tying his shoelace','https://www.pexels.com/video/person-tying-his-shoelace-5029481/','show up for it (man tying his shoe)',1.0)}
out=[]
for k,b in enumerate(B):
    d=dict(a=b['a'],b=b['b'],id=b['id'],why=b['why'],src='mixkit',title=None,page=None,clip_in=b['clip_in'],file='/workspace/l01v2/broll/src/%s.mp4'%b['id'])
    if k in REP:
        i,src,title,page,why,ci=REP[k];d.update(id=i,src=src,title=title,page=page,why=b['why'].split(' / ')[0]+' / '+why,clip_in=ci,file='/workspace/l01v3/broll/src/%s.mp4'%i,replaced=B[k]['id'])
    out.append(d)
# new: cover week cut D (SPLIT 38), 'I'd been short with her, and then I acted like it had worn off on its own.'
out.append(dict(a=625.6,b=629.9,id='px8060562',src='pexels',title='A couple having a misunderstanding',page='https://www.pexels.com/video/a-couple-having-a-misunderstanding-8060562/',why='cover AUDIO CUT D "for a week," (SPLIT 38) / short with her',clip_in=11.0,file='/workspace/l01v3/broll/src/px8060562.mp4'))
out.sort(key=lambda d:d['a'])
gaps=[(W[i]['end'],W[i+1]['start']) for i in range(len(W)-1) if W[i+1]['start']-W[i]['end']>=0.06]
def inword(t):return any(w['start']-0.03<t<w['end']+0.03 for w in W)
def snap(t,dirn,lim=1.2):
    c=[(e+s)/2 for e,s in gaps if (dirn<0 and (e+s)/2<=t+0.08 and t-(e+s)/2<lim) or (dirn>0 and (e+s)/2>=t-0.08 and (e+s)/2-t<lim)]
    if not c:return t
    big=[g for g in c if any(abs((e+s_)/2-g)<1e-6 and s_-e>=0.15 for e,s_ in gaps)]
    if big:c=big
    return max(c) if dirn<0 else min(c)
for i,d in enumerate(out):
    a0,b0=d['a'],d['b']
    # shared boundary with previous clip: snap to the nearest gap either way, keep both sides equal
    if i and abs(out[i-1]['b']-d['a'])<0.05:
        near=[((e+s)/2,s-e) for e,s in gaps if abs((e+s)/2-d['a'])<0.9];m=max(near,key=lambda g:(g[1]>=0.15,-abs(g[0]-d['a'])))[0];out[i-1]['b']=d['a']=round(m,3)
    else:d['a']=round(snap(a0,-1),3) if inword(a0) else a0
    d['b']=round(snap(b0,+1),3) if inword(b0) else b0
# no overlaps
for x,y in zip(out,out[1:]):
    if x['b']>y['a']:
        print('OVERLAP',x['a'],x['b'],y['a'],y['b']);m=y['a'];x['b']=m
bad=[(d['a'],d['b']) for d in out if inword(d['a']) or inword(d['b'])]
ids=[d['id'] for d in out];assert len(ids)==len(set(ids)),'clip reused'
print(len(out),'clips; mid-word edges:',len(bad),bad)
for d in out:print(d['id'],d['a'],d['b'],round(s2o(d['b'])-s2o(d['a']),2),'|',' '.join(w['word'] for w in W if d['a']<=w['start']<d['b']))
json.dump(out,open('broll_plan_v3.json','w'),indent=0)
