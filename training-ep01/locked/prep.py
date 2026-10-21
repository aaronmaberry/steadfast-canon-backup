# prep.py SCRIPT OUTDIR -> OUTDIR/secNN.timing.txt + secNN.prompt.txt
import sys,re,os
src,od=sys.argv[1],sys.argv[2]; os.makedirs(od,exist_ok=True)
secs=[];cur=None
for l in open(src).read().split('\n'):
    l=l.strip()
    if not l: continue
    if l.startswith('# SECTION'):
        cur=[l[len('# SECTION:'):].strip(),[]]; secs.append(cur); continue
    if l.startswith('#'): continue  # [CUT SCREEN]/board marker lines (video only, not spoken)
    t,p=l.rsplit('|',1); cur[1].append((t.strip(),p.strip()))
for i,(title,lines) in enumerate(secs,1):
    open(f'{od}/sec{i:02d}.timing.txt','w').write('\n'.join(f'{t}|{p}' for t,p in lines)+'\n')
    paras=[];para=[]
    for t,p in lines:
        para.append(t)
        v=3.0 if p=='ROOM_HANDS' else 1.7 if p=='ROOM_CHUCKLE' else float(p)
        if v>=1.0: paras.append(' '.join(para)); para=[]
    if para: paras.append(' '.join(para))
    pr='\n\n'.join(paras)
    open(f'{od}/sec{i:02d}.prompt.txt','w').write(pr)
    print(f'sec{i:02d} {len(pr):5d} chars {len(lines):3d} lines  {title}')
