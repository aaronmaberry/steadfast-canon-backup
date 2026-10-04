import json
L=json.load(open('lines.json'))
# assign chapter index
ch=0; chapters=[]
for i in L:
    if 'chapter' in i: ch+=1; chapters.append(i['chapter'])
    i['ch']=ch
SEP=' [pause] '
chunks=[]
for c in range(1,ch+1):
    for spk in ('WES','JONATHON'):
        cur=[]; n=0
        for i in L:
            if i['ch']!=c or i['spk']!=spk: continue
            if cur and n+len(i['tts'])+len(SEP)>1800:
                chunks.append(dict(spk=spk,ch=c,lines=cur)); cur=[]; n=0
            cur.append(i['n']); n+=len(i['tts'])+len(SEP)
        if cur: chunks.append(dict(spk=spk,ch=c,lines=cur))
byn={i['n']:i for i in L}
for k,c in enumerate(chunks):
    c['id']=f"C{k+1:02d}"
    c['prompt']=SEP.join(byn[n]['tts'] for n in c['lines'])
    c['chars']=len(c['prompt'])
json.dump(chunks,open('chunks.json','w'),indent=1)
json.dump(L,open('lines.json','w'),indent=1)
print(len(chunks),'chunks', sum(c['chars'] for c in chunks),'chars')
for c in chunks: print(c['id'],c['spk'][0],c['ch'],len(c['lines']),c['chars'])
