# qa.py : per-line transcript check against the script, from raw/<K>.split.json (+ retakes/<L>.rN.json)
import json,re,glob,difflib,sys,os
from num2words import num2words
L={i['n']:i for i in json.load(open(os.environ.get('LINES','lines.json')))}
C={c['id']:c for c in json.load(open('chunks.json'))}
EXP={'gonna':'going to','wanna':'want to','gotta':'got to','kinda':'kind of','ok':'okay','alright':'all right','em':'them'}
HOMO={'hours':'ours','shouldve':'should have','wouldve':'would have','o clock':'oclock','tick tock':'tiktok','walksteadfast':'walk steadfast dot','cruise':'crews','jonathan':'jonathon','danny':'dani','everyone':'every one','a cross':'across','hvac':'h vac','them':'him'}
FILL={'uh','um','uhm','er','ah','hmm','mm'}
def _nw(i): return num2words(int(i)).replace('-',' ').replace(',','')
def num(t):
    m=re.fullmatch(r'(\d+)(st|nd|rd|th|s)?',t)
    if not m: return t
    d,suf=m.group(1),m.group(2)
    if suf in ('st','nd','rd','th'): return num2words(int(d),to='ordinal').replace('-',' ')
    if d=='1604': w='sixteen oh four'
    elif len(d)==3: w=_nw(d[0])+' '+_nw(d[1:])
    elif len(d)==4 and d[:2] in ('19','20'): w=_nw(d[:2])+' '+_nw(d[2:])
    else: w=_nw(d)
    if suf=='s': w=w[:-1]+'ies' if w.endswith('y') else w+'s'
    return w
def norm(t):
    t=t.lower().replace('sixteen-oh-four','sixteen oh four').replace('%',' percent')
    t=re.sub(r"(\d),(\d)",r"\1\2",t); t=re.sub(r"(\d+) ?[\.:] ?(\d\d)\b",r"\1\2",t); t=re.sub(r"(\d)'s\b",r"\1s",t)
    for a,b in HOMO.items(): t=re.sub(r"\b"+a+r"\b",b,t)
    t=t.replace('-',' ').replace('’',"'"); t=re.sub(r"(\w)'(\w)",r"\1\2",t)
    t=re.sub(r"[^a-z0-9' ]",' ',t)
    out=[]
    for w in t.split():
        w=w.strip("'")
        if not w: continue
        w=EXP.get(w,w); w=num(w)
        out+=w.split()
    return out
def compare(n,hyp_words):
    ref=norm(L[n]['tts']); hyp=norm(' '.join(hyp_words))
    sm=difflib.SequenceMatcher(None,ref,hyp,autojunk=False)
    ops=[(tag,' '.join(ref[i1:i2]),' '.join(hyp[j1:j2])) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag!='equal']
    errs=sum(max(i2-i1,j2-j1) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag!='equal')
    fill=[w for w in hyp if w in FILL]
    return dict(n=n,ref_n=len(ref),errs=errs,wer=round(errs/max(1,len(ref)),3),ops=ops,fill=fill)
def line_words(split,r):
    return [w for w in split['words'] if r['t0']<=(w[1]+w[2])/2<r['t1']]
if __name__=='__main__':
    out={}
    for f in sorted(glob.glob('raw/K*.split.json')):
        s=json.load(open(f))
        for r in s['report']:
            if 't0' not in r: out[r['n']]=dict(n=r['n'],errs=99,ops=[('nobound','','')],fill=[],src=s['K']); continue
            ws=line_words(s,r)
            c=compare(r['n'],[w[0] for w in ws]); c['src']=s['K']; c['dur']=round(r['t1']-r['t0'],2)
            gaps=[round(b[1]-a[2],2) for a,b in zip(ws,ws[1:])]
            c['maxgap']=max(gaps) if gaps else 0
            out[r['n']]=c
    json.dump(out,open('qa_first.json','w'),indent=0)
    flag=[c for c in out.values() if c['errs']>0 or c['fill'] or c.get('maxgap',0)>1.5]
    print(len(out),'lines checked;',len(flag),'with any diff')
    for c in sorted(flag,key=lambda c:c['n']):
        print(c['n'],c['src'],L[c['n']]['spk'],'errs',c['errs'],'maxgap',c.get('maxgap'),c['fill'],c['ops'])
