# Steadfast Men — Session 7 "Live For A Reward That Lasts" — locked training audio

Recording of the **LOCKED** script (not a review).
- Script (locked 2026-10-20, spoken word for word): `training-ep01/scripts-v7/S07-Live-For-A-Reward-That-Lasts.txt`, sha256 `3ccd6fef195027580318bf95c9086d992fb178b9ec6b6b7ee6d732f19fbd1d2d`.
  `# SECTION` / `# CUT SCREEN` lines and room cues are not spoken; tone tags (`[warmly]`, `[dry]`, …) are delivery direction only.
- Voice: ElevenLabs **Wes Hart - Option D**, voice ID `krjoGt4x3CttlxSuoDYW` (locked training voice, LOCKED-LECTURE-STYLE.md), model `eleven_v4`, one take per section, generations_count 1.
- Pipeline (unchanged, training-ep01/locked/): prep.py -> eleven_v4 -> post.sh (atempo 0.93, retime.py, capgaps.py) -> mix.sh (hall IR + room tone + loudnorm I=-16 TP=-1.5) -> check.py + faster-whisper medium.en QA (see QA.txt).
- Generation format: ElevenLabs output mp3_44100_128 (44.1 kHz, 128 kbps) for every section. On 2026-10-20 Aaron asked for best quality (pcm_44100, else mp3_44100_192) going forward, but the ElevenLabs creative tool used here does not expose an output_format setting for eleven_v4 (setting it was rejected), so mp3_44100_128 was the highest available. Masters are mixed and exported from these sources as 16-bit 44.1 kHz WAV.
- Section breaks: 1.2 s x23.
- Recorded 2026-10-20 CT. Runtime 24:32 (1472.8 s). 12 sections. 19,167 characters. Cost 19167 credits ($3.16).

| File | Notes |
|---|---|
| `S07-Live-For-A-Reward-That-Lasts-full.mp3` | full session, 192 kbps, 44.1 kHz mono |
| `S07-Live-For-A-Reward-That-Lasts-master.wav` | full session master, 16-bit 44.1 kHz mono (Git LFS) |
| `sections/S07-secNN-<title>.mp3` | per-section mixes, 192 kbps |
| `gen.log`, `QA.txt` | generation ids/credits, QA result |
| `../web/lesson-07.mp3` | streaming copy (site drop-in: private/lessons/lesson-07.mp3), 96 kbps CBR 44.1 kHz mono (same format as live Lesson 1 audio) |
| `/workspace/artifacts/S07-Live-For-A-Reward-That-Lasts-locked.mp3` (repo: `artifacts/`) | 96 kbps share copy |

## Timeframe cleanup re-splice 2026-10-22 CT (Aaron approved)
Paragraphs re-recorded whole (Wes Hart - Option D, eleven_v4, ElevenLabs flow dZjjskDzdN4tAGVzeyMY) and spliced at paragraph-boundary pauses in sections 01, 02, 10, 12; full lesson remixed with locked mix.sh. Each splice checked with faster-whisper medium.en against the new wording. New runtime 24:33.
