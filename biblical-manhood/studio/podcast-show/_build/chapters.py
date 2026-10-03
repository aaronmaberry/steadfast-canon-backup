import sys; sys.path.insert(0,'/workspace/biblical-manhood/studio/podcast-show/_build')
from timing import times,fmt
out,t=times(sys.argv[1])
rows=[(a,b) for a,b in out if b!='Slate']
rows[0]=(0,rows[0][1])
for a,b in rows: print(fmt(a),b)
