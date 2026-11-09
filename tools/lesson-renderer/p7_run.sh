#!/bin/bash
set -e
WORK=${LESSON_WORK:-/workspace/l08}
export LESSON_WORK=$WORK
MASTER=$1
WIDE=$2
VER=${3:-v1}
cd "$WORK"
mkdir -p p7/chunks p7/stills
/workspace/cvenv/bin/python build/make_inputs.py "$MASTER" "$WIDE" p7
/workspace/cvenv/bin/python build/build_l07.py p7/inputs.json
/workspace/cvenv/bin/python build/track_face.py
/workspace/cvenv/bin/python build/still_runs.py
bash build/run_chunks.sh
/workspace/cvenv/bin/python build/check_chunks.py
bash build/finalize.sh "$VER"
echo P7_ALLDONE
