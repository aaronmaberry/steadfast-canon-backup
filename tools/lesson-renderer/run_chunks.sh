#!/bin/bash
set -e
WORK=${LESSON_WORK:-/workspace/l08}
cd "$WORK"
N=$(/workspace/cvenv/bin/python -c "import json;print(int(round(json.load(open('p7/edl.json'))['end']*25)))")
K=${CHUNKS:-16}
S=$(( (N+K-1)/K ))
PROCS=$(/workspace/cvenv/bin/python -c "import json;print(json.load(open('lesson.json')).get('procs',2))")
mkdir -p p7/chunks
run(){ i=$1; a=$((i*S)); b=$(( (i+1)*S )); [ $b -gt $N ] && b=$N; o=p7/chunks/c$(printf %02d $i).mp4
  [ -f $o ] && return
  rm -f $o.part.mp4
  /workspace/cvenv/bin/python build/render_l07.py $a $b $o > p7/chunks/c$i.log 2>&1
}
i=0
while [ $i -lt $K ]; do
  for ((j=0;j<PROCS && i+j<K;j++)); do run $((i+j)) & done
  wait
  i=$((i+PROCS))
done
echo ALLDONE
