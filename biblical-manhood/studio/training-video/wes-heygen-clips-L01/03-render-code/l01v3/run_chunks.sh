#!/bin/bash
cd /workspace/l01v3
N=$(/workspace/cvenv/bin/python -c "import sys;sys.path.insert(0,'build');from tmap import OUT_END;print(int(round(OUT_END*25)))")
K=8;S=$(( (N+K-1)/K ))
for i in $(seq 0 $((K-1))); do a=$((i*S)); b=$(( (i+1)*S )); [ $b -gt $N ] && b=$N
  o=chunks/c$(printf %02d $i).mp4; [ -f $o ] && continue; rm -f $o.part.mp4
  nohup /workspace/cvenv/bin/python build/render_v3.py $a $b $o > chunks/c$i.log 2>&1 &
done; wait; echo ALLDONE
