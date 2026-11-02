import json
LP='/workspace/artifacts/training/lesson-plan-2026-10-26/L01-build-2026-10-29/'
E=json.load(open('/workspace/l01p6/edl.json'));SH=E['shots']
W=json.load(open('/workspace/artifacts/training/lesson-plan-2026-10-26/L01-audio-2026-10-29/v2/L01-A-Quiet-Tuesday-v2_words.json'))
def shot(t):
    for s in SH:
        if s['t0x']<=t<s['t1x']:return s
ev=[]
for p,io,t,a,b,r,_ in json.load(open(LP+'fixplan-v2/join_sharp.json')):
    if r<0.8 or r>1.25:ev.append((t-0.16,t+0.16,f'join {p} {io} r{r:.2f}'))
for t,io in((286.80,'P04 in'),(377.48,'P06 in'),(864.68,'P14 in')):ev.append((t-0.16,t+0.16,'join-borderline '+io))
for a,b,r in json.load(open(LP+'fixplan-v2/blur_events.json')):
    if r<0.5:ev.append((a,b,f'smear r{r:.2f}'))
for a,b,n in((1022.70,1022.98,'Aaron 17:02.7 warp'),(734.2,734.5,'Aaron 12:14.3 soft'),(753.7,754.0,'Aaron 12:33.8 soft'),(832.2,832.7,'Aaron 13:52.3 soft'),(602.98,603.30,'Aaron 10:03 smear')):ev.append((a,b,n))
ac=json.load(open('/workspace/l01v2/audio_cuts.json'))['cuts']
for c in ac:ev.append((c['a'],c['b'],'AUDIO CUT '+c['text']))
ev.sort()
out=[]
for a,b,n in ev:
    s=shot(a);out.append(dict(a=round(a,3),b=round(b,3),why=n,shot=s['id'],kind=s['kind']))
json.dump(out,open('events.json','w'),indent=0)
for o in out:print(o['a'],o['b'],o['shot'],o['kind'],o['why'])
print(len(out))
