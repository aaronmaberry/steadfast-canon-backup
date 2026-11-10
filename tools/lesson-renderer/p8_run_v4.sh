#!/bin/bash
set -e
cd /workspace/l08/p8
P=/workspace/cvenv/bin/python
M=/workspace/artifacts/training/lesson-plan-2026-10-26/L08-build-2026-11-09/L08-P7-ASSEMBLED-v4.mp4
C=/workspace/l08/p7/inputs.json
N=36782
echo START $(date)
for i in 0 1 2 3; do
  a=$((i*N/4)); b=$(((i+1)*N/4))
  $P ../qc/qc_mp10.py $C $M $a $b mp_$i.json > mp_$i.log 2>&1 &
done
wait
$P -c "import json,glob;r=[];[r.extend(json.load(open(f))) for f in sorted(glob.glob('mp_?.json'))];json.dump(r,open('mp_all.json','w'))"
$P ../qc/qc_arc.py $M mp_all.json arc.json > arc.log 2>&1
# reuse asr if present (same delivery audio)
[ -s asr.json ] || $P ../qc/asr_week.py $M asr.json > asr.log 2>&1
$P ../qc/qc_sum10.py $C 'mp_?.json' arc.json asr.json $M sum.json > sum.log 2>&1
echo P8DONE $(date)
cat sum.json | /workspace/cvenv/bin/python -m json.tool | head -80
