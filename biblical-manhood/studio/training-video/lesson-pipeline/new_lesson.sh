#!/usr/bin/env bash
# Start a new lesson workspace from the locked L04 pipeline.
#   usage: new_lesson.sh 05 "L05-Pick-Up-the-Weight"
# Makes /home/claude/l05/{audio,broll,deliver,edit,gfx,in,look,master,plan,wide}, copies the template code with every
# l04 path and file name switched to the new lesson, and points the board renderer at this package's graphics folder.
set -euo pipefail
NN="$1"; SLUG="$2"                      # SLUG = file-name stem, e.g. L05-Pick-Up-the-Weight
L="l${NN}"; HERE="$(cd "$(dirname "$0")" && pwd)"; DST="/home/claude/${L}"
[ -e "$DST" ] && { echo "$DST already exists"; exit 1; }
mkdir -p "$DST"/{audio,broll,deliver,edit,gfx/out,in,look,master,plan,wide}
cp "$HERE"/template/edit/*.py "$DST/edit/"
cp "$HERE"/template/plan/*.py "$DST/plan/"
cp "$HERE"/template/gfx/boards_base.py "$HERE"/template/gfx/boards_main.py "$DST/gfx/"
cp "$HERE"/graphics/img/RSCRIM.png "$HERE"/graphics/img/WWSCRIM.png "$DST/gfx/out/"   # caption scrims (SOP T3)
cp "$HERE"/template/gfx/boards_l04.py "$DST/gfx/boards_l04_EXAMPLE.py"   # reference only; write gfx/boards_${L}.py fresh
for f in "$DST"/edit/*.py "$DST"/plan/*.py "$DST"/gfx/boards_base.py "$DST"/gfx/boards_main.py; do
  sed -i -e "s#/home/claude/l04#${DST}#g" -e "s#l04_master#${L}_master#g" -e "s#l04_prog_m20#${L}_prog_m20#g" \
         -e "s#L04W-#L${NN}W-#g" -e "s#L04-Stop-Waiting-v3#${SLUG}-v1#g" -e "s#L04-Stop-Waiting#${SLUG}#g" \
         -e "s#/home/claude/work/graphics#${HERE}/graphics#g" -e "s#\"l04-{name}#\"${L}-{name}#g" "$f"
done
# edit/spec.py is lesson-specific: start it empty (keep the header and helpers, drop L04's shots)
python3 - "$DST/edit/spec.py" <<'EOF'
import sys
p = sys.argv[1]; s = open(p).read()
head = s[:s.index("# ---- open, agenda")]
open(p, "w").write(head + "# ---- write this lesson's shots here (see the SOP, step 8) ----\n")
EOF
echo "made $DST. Still per lesson: AUDIO_END in edit/cues.py and TOTAL in plan/quality.py = master duration;"
echo "gfx/boards_${L}.py; edit/spec.py; NO_WIDE / BAD_TAKES in edit/angles.py. Then follow the SOP from step 3."
grep -rn "l04\|L04" "$DST"/edit "$DST"/plan "$DST"/gfx/boards_base.py "$DST"/gfx/boards_main.py | grep -v "^\S*:[0-9]*:\s*#" || true
