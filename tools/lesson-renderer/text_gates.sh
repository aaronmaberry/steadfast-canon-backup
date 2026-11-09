#!/bin/bash
# week / R23 / R44 gates (SOP). Args: files to scan.
set -e
fail=0
for f in "$@"; do
  [ -f "$f" ] || { echo "MISSING $f"; fail=1; continue; }
  week=$(rg -ci -i '\bweeks?\b' "$f" || true)
  r23=$(rg -ci -i 'you guys|gentlemen|brotherhood of|men in this room|men in the room' "$f" || true)
  r44=$(rg -ci -i 'tell on myself' "$f" || true)
  echo "$f: week=${week:-0} R23=${r23:-0} R44=${r44:-0}"
  [ "${week:-0}" = "0" ] || { echo "FAIL week"; fail=1; }
  [ "${r44:-0}" = "0" ] || { echo "FAIL R44"; fail=1; }
done
[ "$fail" = "0" ] && echo text_gates_PASS || { echo text_gates_FAIL; exit 1; }
