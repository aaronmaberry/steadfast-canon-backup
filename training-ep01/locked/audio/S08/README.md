# Steadfast Men — Session 8 "The Empty Chair" — locked training audio

Recording of the **LOCKED** script (not a review).
- Script (locked 2026-10-20, spoken word for word): `training-ep01/scripts-v7/S08-The-Empty-Chair.txt`, sha256 `98eecf8e9c331f22a0d665f5b9bf9758d404792ec4e951aff6557a8ef3f0f9b6`.
  `# SECTION` / `# CUT SCREEN` lines and room cues are not spoken; tone tags (`[warmly]`, `[dry]`, …) are delivery direction only.
- Voice: ElevenLabs **Wes Hart - Option D**, voice ID `krjoGt4x3CttlxSuoDYW` (locked training voice, LOCKED-LECTURE-STYLE.md), model `eleven_v4`, one take per section, generations_count 1.
- Pipeline (unchanged, training-ep01/locked/): prep.py -> eleven_v4 -> post.sh (atempo 0.93, retime.py, capgaps.py) -> mix.sh (hall IR + room tone + loudnorm I=-16 TP=-1.5) -> check.py + faster-whisper medium.en QA (see QA.txt).
- Generation format: ElevenLabs output mp3_44100_128 (44.1 kHz, 128 kbps) for every section. On 2026-10-20 Aaron asked for best quality (pcm_44100, else mp3_44100_192) going forward, but the ElevenLabs creative tool used here does not expose an output_format setting for eleven_v4 (setting it was rejected), so mp3_44100_128 was the highest available. Masters are mixed and exported from these sources as 16-bit 44.1 kHz WAV.
- Section breaks: 1.2 s x21.
- Recorded 2026-10-20 CT. Runtime 23:55 (1435.1 s). 11 sections. 18,523 characters. Cost 18523 credits ($3.06).

| File | Notes |
|---|---|
| `S08-The-Empty-Chair-full.mp3` | full session, 192 kbps, 44.1 kHz mono |
| `S08-The-Empty-Chair-master.wav` | full session master, 16-bit 44.1 kHz mono (Git LFS) |
| `sections/S08-secNN-<title>.mp3` | per-section mixes, 192 kbps |
| `gen.log`, `QA.txt` | generation ids/credits, QA result |
| `../web/lesson-08.mp3` | streaming copy (site drop-in: private/lessons/lesson-08.mp3), 96 kbps CBR 44.1 kHz mono (same format as live Lesson 1 audio) |
| `/workspace/artifacts/S08-The-Empty-Chair-locked.mp3` (repo: `artifacts/`) | 96 kbps share copy |

## Timeframe cleanup re-splice 2026-10-22 CT (Aaron approved)
Paragraphs re-recorded whole (Wes Hart - Option D, eleven_v4, ElevenLabs flow dZjjskDzdN4tAGVzeyMY) and spliced at paragraph-boundary pauses in sections 01, 02, 08; full lesson remixed with locked mix.sh. Each splice checked with faster-whisper medium.en against the new wording. New runtime 23:59.
