#!/bin/bash
cd /workspace/l01v4
P=/workspace/cvenv/bin/python
$P build/render_v4.py 1875 2375 test/bub.mp4 > test/bub.log 2>&1 &
$P build/render_v4.py 3200 3700 test/med.mp4 > test/med.log 2>&1 &
wait; echo TESTDONE > test/done
