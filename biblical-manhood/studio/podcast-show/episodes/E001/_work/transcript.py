# transcript.py : SRT + VTT + chapters from the final audio (final_words.json from whisper on the MP3) and the line timeline.
import json,re,difflib
from qa import norm,compare
import os
L={l['n']:l for l in json.load(open(os.environ.get('LINES','lines.json')))}
tl=json.load(open('out/timeline.json'))
FW=json.load(open('out/final_words.json'))   # (word,start,end,prob)
NAME={'WES':'Wes Hart','JONATHON':'Jonathon'}
KIT='/workspace/biblical-manhood/studio/podcast-show/launch-kit/E001/'
def ts(t,sep): h=int(t//3600); m=int(t%3600//60); s=t%60; return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.',sep)
def sentences(text):
    parts=re.split(r'(?<=[.?!])["”]?\s+(?=["“]?[A-Za-z0-9@])',text)
    # re.split drops closing quotes stuck to the boundary; rebuild by scanning instead
    out=[]; cur=''
    toks=re.findall(r'\S+\s*',text)
    for t in toks:
        cur+=t
        if re.search(r'[.?!]["”]?\s*$',t): out.append(cur.strip()); cur=''
    if cur.strip(): out.append(cur.strip())
    return out
def chunks(text,maxc=84):
    res=[]
    for s in sentences(text):
        if res and len(res[-1])+1+len(s)<=maxc and len(s)<40: res[-1]+=' '+s
        elif len(s)<=maxc: res.append(s)
        else:
            # split long sentence at commas / words near the middle(s)
            words=s.split(); cur=''
            for w in words:
                if len(cur)+1+len(w)>maxc and cur: res.append(cur); cur=w
                else: cur=(cur+' '+w).strip()
            if cur: res.append(cur)
    return res
cues=[]; qa_final=[]
# global alignment: all script tokens (per chunk, per line) vs all ASR tokens of the final file
hyp=[];hidx=[]
for k,w in enumerate(FW):
    for t in norm(w[0]): hyp.append(t); hidx.append(k)
ref=[];rid=[]   # rid = (line index, chunk index)
CH={}
for li,x in enumerate(tl):
    CH[li]=chunks(L[x['n']]['text'])
    for ci,ch in enumerate(CH[li]):
        for t in norm(ch): ref.append(t); rid.append((li,ci))
sm=difflib.SequenceMatcher(None,ref,hyp,autojunk=False); r2h={}
for a,b,sz in sm.get_matching_blocks():
    for j in range(sz): r2h[a+j]=hidx[b+j]
# per-line error count from opcodes
lerr={li:[] for li in range(len(tl))}
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag=='equal': continue
    if i2>i1:
        for li in sorted(set(rid[r][0] for r in range(i1,i2))): lerr[li].append((tag,' '.join(ref[i1:i2]),' '.join(hyp[j1:j2])))
    else:
        li=rid[min(i1,len(rid)-1)][0]; lerr[li].append((tag,'',' '.join(hyp[j1:j2])))
for li,x in enumerate(tl):
    n=x['n']; chs=CH[li]
    nref=sum(1 for r in rid if r[0]==li)
    errs=sum(max(len(a.split()),len(b.split())) for _,a,b in lerr[li])
    qa_final.append(dict(n=n,errs=errs,ops=lerr[li],ref_n=nref,start=x['start']))
    tot=sum(len(c_) for c_ in chs); acc=0; bounds=[]
    for ci,ch in enumerate(chs):
        hs=[r2h[r] for r in range(len(ref)) if rid[r]==(li,ci) and r in r2h]
        hs=[h for h in hs if x['start']-1.0<=FW[h][1]<=x['end']+1.0]
        p0=x['start']+(x['end']-x['start'])*acc/tot; acc+=len(ch); p1=x['start']+(x['end']-x['start'])*acc/tot
        t0=FW[min(hs)][1] if hs else p0; t1=FW[max(hs)][2] if hs else p1
        bounds.append([max(t0,x['start']-0.1),min(t1,x['end']+0.1)])
    for ci in range(len(bounds)):
        if ci==0: bounds[ci][0]=min(bounds[ci][0],x['start']+0.05)
        if ci==len(bounds)-1: bounds[ci][1]=max(bounds[ci][1],x['end']-0.1)
        if ci>0 and bounds[ci][0]<bounds[ci-1][1]: bounds[ci][0]=bounds[ci-1][1]
        if bounds[ci][1]<=bounds[ci][0]+0.3: bounds[ci][1]=bounds[ci][0]+0.3
    for ci,(ch,(t0,t1)) in enumerate(zip(chs,bounds)):
        cues.append(dict(spk=x['spk'],first=ci==0,t0=max(0,t0-0.05),t1=t1+0.15,text=ch))
for a,b in zip(cues,cues[1:]):
    if a['t1']>b['t0']: a['t1']=b['t0']-0.01
def wrap(t,w=42):
    if len(t)<=w: return t
    mid=len(t)//2; sp=[i for i,c in enumerate(t) if c==' ']; i=min(sp,key=lambda k:abs(k-mid)); return t[:i]+'\n'+t[i+1:]
with open(KIT+'E001-transcript.vtt','w') as f:
    f.write('WEBVTT\n\n')
    for i,c in enumerate(cues,1):
        f.write(f"{i}\n{ts(c['t0'],'.')} --> {ts(c['t1'],'.')}\n<v {NAME[c['spk']]}>{wrap(c['text'])}\n\n")
with open(KIT+'E001-transcript.srt','w') as f:
    for i,c in enumerate(cues,1):
        t=(NAME[c['spk']]+': ' if c['first'] else '')+c['text']
        f.write(f"{i}\n{ts(c['t0'],',')} --> {ts(c['t1'],',')}\n{wrap(t,46)}\n\n")
# chapters: first line of each scripted chapter; Slate folds into Cold open at 00:00
chap=[]
for x in tl:
    nm=L[x['n']].get('chapter')
    if nm:
        if nm=='Slate': continue
        t=0.0 if nm=='Cold open' else round(x['start']-0.4,1)
        chap.append(dict(startTime=t,title=nm))
json.dump(dict(version='1.2.0',chapters=chap),open(KIT+'chapters.json','w'),indent=2)
def mmss(t): return f'{int(t//60):02d}:{int(t%60):02d}'
open(KIT+'chapters.txt','w').write('\n'.join(f"{mmss(c['startTime'])} {c['title']}" for c in chap)+'\n')
json.dump(qa_final,open('out/qa_final.json','w'))
bad=[c for c in qa_final if c['errs']>0]
print('cues',len(cues),'chapters',len(chap)); print(open(KIT+'chapters.txt').read())
print('final-pass lines with diffs:',len(bad))
for c in bad: print(c['n'],c['errs'],c['ops'])
