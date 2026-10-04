#!/usr/bin/env python3
"""usage: status_add.py EP NEXT "line text"  -> sets row-9 'Next:' and appends '- EP done: ...' after the last '- E0xx done' line."""
import sys,re,pathlib
ep,nxt,text=sys.argv[1],sys.argv[2],sys.argv[3]
p=pathlib.Path(__file__).resolve().parent.parent/'STATUS.md'
L=p.read_text().split('\n')
row=[i for i,l in enumerate(L) if l.startswith('| 9. Remaining scripts')][0]
import os
b=os.environ.get('SBATCH','Batch 8 (E057-E064)')
bre=re.escape(b)
if re.search(bre+r' IN PROGRESS\. Next: [^|.]*\.',L[row]):
    L[row]=re.sub(bre+r' IN PROGRESS\. Next: [^|.]*\.', f'{b} IN PROGRESS. Next: {nxt}.', L[row])
else:
    L[row]=re.sub(r'\s*\|\s*scripts/ ;', f' {b} IN PROGRESS. Next: {nxt}. | scripts/ ;', L[row],count=1)
idx=[i for i,l in enumerate(L) if re.match(r'- E\d{3} done:',l)]
L=[l for l in L if not l.startswith(f'- {ep} done:')]
idx=[i for i,l in enumerate(L) if re.match(r'- E\d{3} done:',l)]
L.insert(idx[-1]+1, f'- {ep} done: {text}')
p.write_text('\n'.join(L)); print(L[row][-160:])
