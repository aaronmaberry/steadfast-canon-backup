#!/bin/bash
cd /workspace/l01v4
while [ ! -f chunks/c07.mp4 ] || [ ! -f chunks/c06.mp4 ]; do sleep 20; done
./finalize.sh > qc/finalize.log 2>&1
echo "- $(date +%H:%M) CT: master finalized" >> /workspace/l01v3/v4-PROGRESS.md
ffmpeg -nostats -i L01-P7-ASSEMBLED-v4.mp4 -af ebur128 -f null - 2>&1 | tail -n 12 > qc/loud.txt
N=$(ffprobe -v error -count_packets -select_streams v -show_entries stream=nb_read_packets -of csv=p=0 L01-P7-ASSEMBLED-v4.mp4); H=$((N/2))
/workspace/cvenv/bin/python qc/qc_v4.py L01-P7-ASSEMBLED-v4.mp4 qc/qm0.json 0 $H > qc/qm0.log 2>&1 &
/workspace/cvenv/bin/python qc/qc_v4.py L01-P7-ASSEMBLED-v4.mp4 qc/qm1.json $H $N > qc/qm1.log 2>&1 &
wait
echo "- $(date +%H:%M) CT: qc_v4 done" >> /workspace/l01v3/v4-PROGRESS.md
./review.sh > qc/review.log 2>&1
echo "- $(date +%H:%M) CT: review copies done" >> /workspace/l01v3/v4-PROGRESS.md
echo POSTDONE > qc/post.done
