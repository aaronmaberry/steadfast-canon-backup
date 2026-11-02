#!/bin/bash
cd /workspace/l01v4
G=$(cat track_bub_groups.json)
A=$(python3 -c "import json;print(json.dumps(json.load(open('track_bub_groups.json'))[0]))")
B=$(python3 -c "import json;print(json.dumps(json.load(open('track_bub_groups.json'))[1]))")
/workspace/cvenv/bin/python /workspace/l01v2/track.py "$A" trkA.json > trkA.log 2>&1 &
/workspace/cvenv/bin/python /workspace/l01v2/track.py "$B" trkB.json > trkB.log 2>&1 &
wait; echo TRK > trk.done
