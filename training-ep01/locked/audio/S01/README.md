# Steadfast Men — Session 1 "A Quiet Tuesday" — locked training audio

- Script (approved/locked 2026-10-20; kickoff re-locked 2026-10-21, spoken word for word): `training-ep01/scripts-v7/S01-A-Quiet-Tuesday.txt`
  (byte-identical to `training-ep01/rec/S01-v2/S01-A-Quiet-Tuesday-v2-script.txt`; master `training-ep01/rec/S01-v2/W01-script-v-24lessons-LOCKED-2026-10-21.md`).
  `# SECTION` / `# CUT SCREEN` lines and room cues are not spoken; `[warmly]` used as delivery direction only.
- Voice: ElevenLabs **Wes Hart - Option D**, voice ID `krjoGt4x3CttlxSuoDYW` (locked training voice, LOCKED-LECTURE-STYLE.md), model `eleven_v4`, one take per section, generations_count 1.
- Pipeline (unchanged, training-ep01/locked/): prep.py -> eleven_v4 -> post.sh (atempo 0.93, retime.py, capgaps.py) -> mix.sh (hall IR + room tone + loudnorm I=-16 TP=-1.5) -> check.py + faster-whisper medium.en QA.
- Section breaks: 1.2 s (01→02, 02→03), 2.5 s at every section-title cut screen (03→04 … 13→14).
- Recorded 2026-10-20 CT; sec02 Kickoff re-recorded 2026-10-21 CT (4 approved line changes, same voice/model/pipeline; other 13 sections unchanged takes, re-mixed together). Runtime 25:31 (1531.3 s). 14 sections. 19,547 characters.

| File | Notes |
|---|---|
| `S01-A-Quiet-Tuesday-full.mp3` | full session, 192 kbps, 44.1 kHz mono |
| `S01-A-Quiet-Tuesday-master.wav` | full session master, 16-bit 44.1 kHz mono (Git LFS) |
| `sections/S01-secNN-<title>.mp3` | per-section mixes, 192 kbps |
| `gen.log`, `QA.txt` | generation ids/credits, QA result |

## Timeframe cleanup re-splice 2026-10-22 CT (Aaron approved)
Paragraphs re-recorded whole (Wes Hart - Option D, eleven_v4, ElevenLabs flow dZjjskDzdN4tAGVzeyMY) and spliced at paragraph-boundary pauses in sections 02, 08, 09, 14; full lesson remixed with locked mix.sh. Each splice checked with faster-whisper medium.en against the new wording. New runtime 27:48.
