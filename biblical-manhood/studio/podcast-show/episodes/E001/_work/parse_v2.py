import re, json
src='/workspace/biblical-manhood/studio/podcast-show/scripts/E001-the-man-you-keep-saying-youll-be.md'
txt=open(src).read()
body=txt.split('## Script',1)[1].split('## Shorts',1)[0]
items=[]; pend=0.0; chapter=None; pend_reason=[]
TTS_SUBS=[(r'\b1604\b','sixteen-oh-four'),(r'walksteadfast\.com','walk steadfast dot com'),(r'@steadfastwalk','at steadfast walk')]
for raw in body.splitlines():
    l=raw.strip()
    if not l: continue
    m=re.match(r'^\[CHAPTER: (.*)\]$',l)
    if m: chapter=m.group(1); pend=max(pend,1.0); pend_reason.append('chapter'); continue
    m=re.match(r'^(WES|JONATHON): (.*)$',l)
    if m:
        spk,t=m.groups()
        lead=0.0
        # leading (beat...) direction
        mm=re.match(r'^\((beat[^)]*)\)\s*',t)
        if mm: lead=0.6; t=t[mm.end():]
        # mid-line beats -> marker
        t=re.sub(r'\s*\(beat[^)]*\)\s*',' <BEAT> ',t)
        t=re.sub(r'\s*\([^)]*\)\s*',' ',t).strip()
        t=re.sub(r'\s+',' ',t)
        t=t.replace(' .', '.').replace(' ,', ',')
        disp=t.replace(' <BEAT> ',' ').replace('<BEAT>','')
        tts=disp
        for a,b in TTS_SUBS: tts=re.sub(a,b,tts)
        beats=t.count('<BEAT>')
        items.append(dict(n=len(items)+1,spk=spk,text=disp,tts=tts,chapter=chapter,pre=round(pend,2),lead=lead,midbeats=beats,pre_reason=pend_reason))
        pend=0.0; pend_reason=[]; chapter=None
        continue
    if l.startswith('[beat]'): pend=max(pend,0.6); pend_reason.append('beat'); continue
    m=re.match(r'^\[pause (\d+)s\]',l)
    if m: pend=max(pend,float(m.group(1))); pend_reason.append('pause'); continue
    if l.startswith('[BREATHER'): pend=min(pend+0.8,1.9); pend_reason.append('breather'); continue
    if l.startswith('[STING'): pend=max(pend,1.2); pend_reason.append('sting'); continue
    if l.startswith('(both laugh'): pend=max(pend,0.9); pend_reason.append('laugh'); continue
    if l.startswith('('): pend=max(pend,0.8); pend_reason.append('action'); continue
for it in items:
    if it['chapter'] is None: it.pop('chapter')
json.dump(items,open('lines_v2.json','w'),indent=1)
tot=sum(len(i['tts']) for i in items)
print(len(items),'lines; tts chars',tot,'; budget 1.3x =',int(tot*1.3))
for s in ('WES','JONATHON'):
    w=sum(len(i['text'].split()) for i in items if i['spk']==s); print(s,w,'words')
print('midbeats',[ (i['n'],i['text']) for i in items if i['midbeats']])
print('max len',max(len(i['tts']) for i in items))
