#!/bin/bash
set -e
export LESSON_WORK=/workspace/l08
cd /workspace/l08
echo "START $(date) free=$(df -h / | awk 'NR==2{print $4}')"
# 3 workers
/workspace/cvenv/bin/python -c "import json;p='lesson.json';d=json.load(open(p));d['procs']=3;json.dump(d,open(p,'w'),indent=1)"
rm -f p7/chunks/c*.mp4 p7/chunks/c*.part.mp4
mkdir -p p7/chunks
bash build/run_chunks.sh
echo "CHUNKS_DONE $(date) free=$(df -h / | awk 'NR==2{print $4}')"
/workspace/cvenv/bin/python -c "import json;p='lesson.json';d=json.load(open(p));d['procs']=2;json.dump(d,open(p,'w'),indent=1)"
bash build/finalize.sh v4
echo "FINALIZED $(date)"
# contact sheet for the assembled cut (every 20s + broll/boards) — may already be in contact_sheet.py
if [ -f build/contact_sheet.py ]; then
  /workspace/cvenv/bin/python build/contact_sheet.py || true
fi
echo V4_ENCODE_DONE $(date)
df -h / | tail -1
