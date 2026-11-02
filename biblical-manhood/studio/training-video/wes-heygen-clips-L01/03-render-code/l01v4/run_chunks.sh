#!/bin/bash
cd /workspace/l01v4
N=$(/workspace/cvenv/bin/python -c "import sys;sys.path.insert(0,'build');from tmap import OUT_END;print(int(round(OUT_END*25)))")
K=8;S=$(( (N+K-1)/K ))
run(){ i=$1; a=$((i*S)); b=$(( (i+1)*S )); [ $b -gt $N ] && b=$N; o=chunks/c$(printf %02d $i).mp4; [ -f $o ] && return; rm -f $o.part.mp4; /workspace/cvenv/bin/python build/render_v4.py $a $b $o > chunks/c$i.log 2>&1; }
for p in 0 2 4 6; do run $p & run $((p+1)) & wait; done; echo ALLDONE
