# Steadfast Men — Session 12 "A Man With No Brothers" — locked training audio

Recording of the **LOCKED** script (not a review).
- Script (locked 2026-10-20, spoken word for word): `training-ep01/scripts-v7/S12-A-Man-With-No-Brothers.txt`, sha256 `d7da3d877813d705b921e5a47a3cbd3fdd40e3cae1f4f3722c86214eea3a0910`.
  `# SECTION` / `# CUT SCREEN` lines and room cues are not spoken; tone tags (`[warmly]`, `[dry]`, …) are delivery direction only.
- Voice: ElevenLabs **Wes Hart - Option D**, voice ID `krjoGt4x3CttlxSuoDYW` (locked training voice, LOCKED-LECTURE-STYLE.md), model `eleven_v4`, one take per section, generations_count 1.
- Pipeline (unchanged, training-ep01/locked/): prep.py -> eleven_v4 -> post.sh (atempo 0.93, retime.py, capgaps.py) -> mix.sh (hall IR + room tone + loudnorm I=-16 TP=-1.5) -> check.py + faster-whisper medium.en QA (see QA.txt).
- Generation format: ElevenLabs output mp3_44100_128 (44.1 kHz, 128 kbps) for every section. On 2026-10-20 Aaron asked for best quality (pcm_44100, else mp3_44100_192) going forward, but the ElevenLabs creative tool used here does not expose an output_format setting for eleven_v4 (setting it was rejected), so mp3_44100_128 was the highest available. Masters are mixed and exported from these sources as 16-bit 44.1 kHz WAV.
- Section breaks: 1.2 s x23.
- Recorded 2026-10-20 CT. Runtime 24:13 (1453.1 s). 12 sections. 18,961 characters. Cost 18961 credits ($3.13).

| File | Notes |
|---|---|
| `S12-A-Man-With-No-Brothers-full.mp3` | full session, 192 kbps, 44.1 kHz mono |
| `S12-A-Man-With-No-Brothers-master.wav` | full session master, 16-bit 44.1 kHz mono (Git LFS) |
| `sections/S12-secNN-<title>.mp3` | per-section mixes, 192 kbps |
| `gen.log`, `QA.txt` | generation ids/credits, QA result |
| `../web/lesson-12.mp3` | streaming copy (site drop-in: private/lessons/lesson-12.mp3), 96 kbps CBR 44.1 kHz mono (same format as live Lesson 1 audio) |
| `/workspace/artifacts/S12-A-Man-With-No-Brothers-locked.mp3` (repo: `artifacts/`) | 96 kbps share copy |

## Timeframe cleanup re-splice 2026-10-22 CT (Aaron approved)
Paragraphs re-recorded whole (Wes Hart - Option D, eleven_v4, ElevenLabs flow dZjjskDzdN4tAGVzeyMY) and spliced at paragraph-boundary pauses in sections 01, 02, 06, 07, 11, 12; full lesson remixed with locked mix.sh. Each splice checked with faster-whisper medium.en against the new wording. New runtime 24:25.
