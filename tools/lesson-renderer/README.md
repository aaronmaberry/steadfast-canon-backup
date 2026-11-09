# Lesson video P7/P8 renderer (L07-class)

Recovered/rebuilt 2026-11-09 after `/workspace/lNN/build/` was wiped by a box restore.

## Files
- `p7_run.sh` — orchestrates make_inputs → build_l07 → track_face → still_runs → run_chunks → check_chunks → finalize
- `build_l07.py` — EDL builder (L5 mix gate, scripture fix, kinetic covers from cover_master)
- `render_l07.py` — 1080p frame renderer (Wes wide/panel/bubble, boards, scripture, kinetic covers, B-roll, transitions)
- `make_inputs.py`, `track_face.py`, `still_runs.py`, `check_chunks.py`, `captions.py`
- `run_chunks.sh`, `finalize.sh`, `text_gates.sh`
- `p8_run.sh`, `share.sh` — P8 QC + review hardlink templates

## Usage
```
export LESSON_WORK=/workspace/l08 LESSON_JSON=/workspace/l08/lesson.json
bash build/p7_run.sh <master.mp4> <wide_rendered.json> v1
```

Copy this directory to `/workspace/lNN/build/` for each lesson. Keep media out of git.
