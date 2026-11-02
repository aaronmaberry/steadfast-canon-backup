#!/bin/bash
cd /workspace/l01v4;P=/workspace/cvenv/bin/python
$P build/render_v4.py 1875 2375 test/bub3.mp4 > test/bub3.log 2>&1
cd test; $P pulse2.py bub3.mp4 75 95 0 pv4c.json > pt3.log 2>&1; echo T2 > t3.done
