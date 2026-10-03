import sys,re; sys.path.insert(0,'/workspace/biblical-manhood/studio/podcast-show/_build')
from timing import times,fmt
p=sys.argv[1]; s=open(p).read()
body=s.split('## Script',1)[1].split('\n## Shorts',1)[0]
open('/tmp/_body.md','w').write(body)
out,t=times('/tmp/_body.md')
rows=[(a,b) for a,b in out if b!='Slate']; rows[0]=(0,rows[0][1])
block='Chapters\n'+'\n'.join(f"{fmt(a)} {b}" for a,b in rows)+'\n'
s2=re.sub(r'Chapters\n(?:\d\d:\d\d.*\n)+',block,s,count=1)
s2=s2.replace("(Chapter times are placeholders until the edit. Run `_build/chapters.py` on the final script, then confirm against the cut.)","(Chapter times are estimated from the script by `_build/apply_chapters.py`, at 145 wpm for Wes and 170 for Jonathon. Confirm them against the cut.)")
open(p,'w').write(s2); print(block, 'TOTAL',fmt(t))
