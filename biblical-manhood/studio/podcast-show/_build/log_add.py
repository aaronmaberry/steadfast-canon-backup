#!/usr/bin/env python3
"""usage: log_add.py TARGET "bullet text"
TARGET: changelog | wes | jon. Appends '- bullet' to the current batch section (creates it if missing).
Batch label comes from env BATCH (default 'batch 6 (E041-E048)')."""
import sys,os,pathlib
root=pathlib.Path(__file__).resolve().parent.parent
batch=os.environ.get('BATCH','batch 6 (E041-E048)')
tgt,text=sys.argv[1],sys.argv[2]
if tgt=='changelog':
    p=root/'CHANGELOG.md'; period=os.environ.get('PERIOD','2026-10-03 (morning CT)')
    head=f'## {period}: {batch}, polish, panel round'
    L=p.read_text().split('\n')
    if head not in L:
        import re
        i=[k for k,l in enumerate(L) if re.match(r'^## 2026-10-0\d .*batch \d',l)][0]
        L[i:i]=[head,'','']
    i=L.index(head)+1
    j=i+1
    while j<len(L) and not L[j].startswith('## '): j+=1
    # insert before trailing blank lines of section
    k=j
    while L[k-1]=='' : k-=1
    L.insert(k,'- '+text)
    if L[k+1]!='' : L.insert(k+1,'')
else:
    p=root/'hosts'/('WES-HART-HOST.md' if tgt=='wes' else 'JONATHON-CHARACTER.md')
    head=f'### Continuity added in {batch}'
    s=p.read_text().rstrip('\n')
    if head not in s: s+=f'\n\n{head}\n'
    s+='\n- '+text
    L=(s+'\n').split('\n')
p.write_text('\n'.join(L)); print('ok',p.name)
