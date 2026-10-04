"""Read-only structural audit (open system v3 work, 2026-10-03). Prints one row per script.
Uses the same clock as timing.py. Changes nothing."""
import re,sys,glob,os
sys.path.insert(0,os.path.dirname(__file__))
from timing import fmt
def walk(path):
    t=0.0;ch=[];marks=[];spoken=[]
    for line in open(path):
        line=line.rstrip('\n')
        m=re.match(r'\[CHAPTER: (.*)\]',line)
        if m: ch.append((t,m.group(1))); continue
        for k in ('SUB-MID','PLUG','CREDITS','CLOSING MUSIC'):
            if line.startswith('['+k): marks.append((t,k))
        if line.startswith('[BREATHER'): t+=3
        if line.startswith('[STING'): t+=3
        m=re.match(r'\[CLOSING MUSIC (\d+)s\]',line)
        if m: t+=int(m.group(1))
        m=re.match(r'(WES|JONATHON): (.*)',line)
        if m:
            txt=re.sub(r'\([^)]*\)|\[[^]]*\]','',m.group(2))
            spoken.append((t,ch[-1][1] if ch else '',m.group(1),txt.strip()))
            w=len(txt.split()); rate=145 if m.group(1)=='WES' else 170
            t+=w/rate*60+0.45+0.6*m.group(2).count('[beat]')
        elif line.startswith('(') and 'laugh' in line: t+=1.2
        if line.strip()=='[beat]': t+=0.6
        if line.strip()=='[pause 1s]': t+=1
        if line.strip()=='[pause 2s]': t+=2
    return ch,marks,spoken,t
rows=[]
for f in sorted(glob.glob('scripts/E0[0-9][0-9]-*.md')):
    n=int(os.path.basename(f)[1:4]); fn='field-notes' in f
    ch,marks,sp,T=walk(f)
    st={name:t for t,name in ch}
    names=[name for _,name in ch]
    def start(rx):
        for t,name in ch:
            if re.search(rx,name,re.I): return t
    ends=[ch[i+1][0] if i+1<len(ch) else T for i in range(len(ch))]
    lens=[(e-s,name) for (s,name),e in zip(ch,ends)]
    cold=start('^Intro'); first=ch[2][0] if len(ch)>2 else None
    body=[(l,nm) for l,nm in lens if not re.search('Cold open|Intro|Outro|Carry',nm)]
    longest=max(body) if body else (0,'')
    cold_lines=[x for x in sp if x[1]=='Cold open']
    first3=[x for x in sp if ch and len(ch)>2 and x[1]==ch[2][1]][:2]
    sub=[t for t,k in marks if k=='SUB-MID']; plug=[t for t,k in marks if k=='PLUG']
    rows.append(dict(n=n,fn=fn,T=T,cold=cold,first=first,ch3=ch[2][1] if len(ch)>2 else '',
      third=ch[3][0] if len(ch)>3 else None,word=start('Word'),chal=start('challenge|Tool'),
      longest=longest,over6=[nm for l,nm in body if l>360],sub=sub,plug=plug,
      coldwords=sum(len(x[3].split()) for x in cold_lines),first3=' / '.join(f"{x[2][0]}: {x[3][:90]}" for x in first3)))
if __name__=='__main__':
    print("| Ep | Type | Total | Cold | 3rd ch at | Next ch at | Word at | Challenge/Tool at | Longest body chapter | SUB-MID | PLUG | First lines after the slate |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    f=lambda x: fmt(x) if x is not None else '-'
    for r in rows:
        print(f"| E{r['n']:03d} | {'FN' if r['fn'] else 'Main'} | {fmt(r['T'])} | {round(r['cold'] or 0)}s/{r['coldwords']}w | {f(r['first'])} {r['ch3']} | {f(r['third'])} | {f(r['word'])} | {f(r['chal'])} | {fmt(r['longest'][0])} {r['longest'][1]} | {','.join(fmt(x) for x in r['sub']) or '-'} | {','.join(fmt(x) for x in r['plug']) or '-'} | {r['first3'].replace('|','/')} |")
