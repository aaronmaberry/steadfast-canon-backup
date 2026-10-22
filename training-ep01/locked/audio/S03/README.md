# Steadfast Men — Session 3 "The Four Marks" — locked training audio

Recording of the **LOCKED** script (not a review).
- Script (locked 2026-10-20, spoken word for word): `training-ep01/scripts-v7/S03-The-Four-Marks.txt`, sha256 `4b6e0b5dab2b01c23b89ba2c6167857626be1fa84e9191c0a460b66f0a2bea6c`.
  `# SECTION` / `# CUT SCREEN` lines and room cues are not spoken; tone tags (`[warmly]`, `[dry]`, …) are delivery direction only.
- Voice: ElevenLabs **Wes Hart - Option D**, voice ID `krjoGt4x3CttlxSuoDYW` (locked training voice, LOCKED-LECTURE-STYLE.md), model `eleven_v4`, one take per section, generations_count 1.
- Pipeline (unchanged, training-ep01/locked/): prep.py -> eleven_v4 -> post.sh (atempo 0.93, retime.py, capgaps.py) -> mix.sh (hall IR + room tone + loudnorm I=-16 TP=-1.5) -> check.py + faster-whisper medium.en QA (see QA.txt).
- Generation format: ElevenLabs output mp3_44100_128 (44.1 kHz, 128 kbps) for every section (generated before the 2026-10-20 best-quality request; the ElevenLabs creative tool does not expose output_format for eleven_v4 in any case). Master exported as 16-bit 44.1 kHz WAV.
- Section breaks: 1.2 s x25.
- Recorded 2026-10-20 CT. Runtime 24:16 (1456.2 s). 13 sections. 19,218 characters. Cost 19218 credits ($3.17).

| File | Notes |
|---|---|
| `S03-The-Four-Marks-full.mp3` | full session, 192 kbps, 44.1 kHz mono |
| `S03-The-Four-Marks-master.wav` | full session master, 16-bit 44.1 kHz mono (Git LFS) |
| `sections/S03-secNN-<title>.mp3` | per-section mixes, 192 kbps |
| `gen.log`, `QA.txt` | generation ids/credits, QA result |
| `../web/lesson-03.mp3` | streaming copy (site drop-in: private/lessons/lesson-03.mp3), 96 kbps CBR 44.1 kHz mono (same format as live Lesson 1 audio) |
| `/workspace/artifacts/S03-The-Four-Marks-locked.mp3` (repo: `artifacts/`) | 96 kbps share copy |

## Timeframe cleanup re-splice 2026-10-22 CT (Aaron approved)
Paragraphs re-recorded whole (Wes Hart - Option D, eleven_v4, ElevenLabs flow dZjjskDzdN4tAGVzeyMY) and spliced at paragraph-boundary pauses in sections 01, 03, 08, 13; full lesson remixed with locked mix.sh. Each splice checked with faster-whisper medium.en against the new wording. New runtime 24:16.
