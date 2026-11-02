import json,sys
sys.path.insert(0,'/workspace/l01v3/build');from tmap import s2o,CUTS
W=json.load(open('/workspace/artifacts/training/lesson-plan-2026-10-26/L01-audio-2026-10-29/v2/L01-A-Quiet-Tuesday-v2_words.json'))
W=[dict(w,start=s2o(w['start']),end=s2o(w['end'])) for w in W if not any(a<=w['start']<b for a,b,_ in CUTS)]
cues=[];cur=[]
def flush():
    if cur:cues.append((cur[0]['start'],cur[-1]['end'],' '.join(w['word'] for w in cur)))
for i,w in enumerate(W):
    if cur:
        txt=' '.join(x['word'] for x in cur+[w]);gap=w['start']-cur[-1]['end']
        if len(txt)>84 or gap>0.7 or w['end']-cur[0]['start']>6.0 or (cur[-1]['word'][-1] in '.?!"' and len(' '.join(x['word'] for x in cur))>30):flush();cur=[]
    cur.append(w)
flush()
def split2(s):
    if len(s)<=42:return s
    ws=s.split();best=None
    for k in range(1,len(ws)):
        a,b=' '.join(ws[:k]),' '.join(ws[k:]);m=max(len(a),len(b))
        if best is None or m<best[0]:best=(m,a,b)
    return best[1]+'\n'+best[2]
f=lambda t,sep:'%02d:%02d:%02d%s%03d'%(t//3600,t%3600//60,int(t%60),sep,round(t%1*1000)%1000)
out=[];vt=['WEBVTT','']
for i,(a,b,s) in enumerate(cues):
    nb=cues[i+1][0] if i+1<len(cues) else b+1;b=min(b+0.4,nb-0.04)
    out+= [str(i+1),f'{f(a,",")} --> {f(b,",")}',split2(s),''];vt+=[f'{f(a,".")} --> {f(b,".")}',split2(s),'']
open('/workspace/l01v2/L01-P7-ASSEMBLED-v2.srt','w').write('\n'.join(out));open('/workspace/l01v2/L01-P7-ASSEMBLED-v2.vtt','w').write('\n'.join(vt));print(len(cues),'cues',len(W),'words')
