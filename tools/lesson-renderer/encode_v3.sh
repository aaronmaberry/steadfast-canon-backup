#!/bin/bash
set -e
export LESSON_WORK=/workspace/l08
cd /workspace/l08
echo "START $(date) free=$(df -h / | awk 'NR==2{print $4}')"
# 3 workers for this encode only
/workspace/cvenv/bin/python -c "import json;p='lesson.json';d=json.load(open(p));d['procs']=3;json.dump(d,open(p,'w'),indent=1)"
rm -f p7/chunks/c*.mp4 p7/chunks/c*.part.mp4
bash build/run_chunks.sh
echo "CHUNKS_DONE $(date)"
# restore procs
/workspace/cvenv/bin/python -c "import json;p='lesson.json';d=json.load(open(p));d['procs']=2;json.dump(d,open(p,'w'),indent=1)"
bash build/finalize.sh v3
echo "FINALIZED $(date)"
/workspace/cvenv/bin/python build/contact_sheet.py
echo "CONTACT_DONE $(date)"
echo V3_ENCODE_DONE
