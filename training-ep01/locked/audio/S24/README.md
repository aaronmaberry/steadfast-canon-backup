# Steadfast Men — Session 24 "Give Your Son A Day" — locked training audio

Recording of the **LOCKED** script (not a review).
- Script (locked 2026-10-20, spoken word for word): `training-ep01/scripts-v7/S24-Give-Your-Son-A-Day.txt`, sha256 `fd7af7e8ee062f0e00ad7519785930830b0e78dbe2b8a42c1334fb58e799d922`.
  `# SECTION` / `# CUT SCREEN` lines and room cues are not spoken; tone tags (`[warmly]`, `[dry]`, …) are delivery direction only.
- Voice: ElevenLabs **Wes Hart - Option D**, voice ID `krjoGt4x3CttlxSuoDYW` (locked training voice, LOCKED-LECTURE-STYLE.md), model `eleven_v4`, one take per section, generations_count 1.
- Pipeline (unchanged, training-ep01/locked/): prep.py -> eleven_v4 -> post.sh (atempo 0.93, retime.py, capgaps.py) -> mix.sh (hall IR + room tone + loudnorm I=-16 TP=-1.5) -> check.py + faster-whisper medium.en QA (see QA.txt).
- Generation format: ElevenLabs output mp3_44100_128 (44.1 kHz, 128 kbps) for every section. On 2026-10-20 Aaron asked for best quality (pcm_44100, else mp3_44100_192) going forward, but the ElevenLabs creative tool used here does not expose an output_format setting for eleven_v4 (setting it was rejected), so mp3_44100_128 was the highest available. Masters are mixed and exported from these sources as 16-bit 44.1 kHz WAV.
- Section breaks: 1.2 s x23, 2.5 s at every section-title cut screen x2.
- Recorded 2026-10-20 CT. Runtime 26:16 (1577.0 s). 13 sections. 20,755 characters. Cost 20755 credits ($3.42).

| File | Notes |
|---|---|
| `S24-Give-Your-Son-A-Day-full.mp3` | full session, 192 kbps, 44.1 kHz mono |
| `S24-Give-Your-Son-A-Day-master.wav` | full session master, 16-bit 44.1 kHz mono (Git LFS) |
| `sections/S24-secNN-<title>.mp3` | per-section mixes, 192 kbps |
| `gen.log`, `QA.txt` | generation ids/credits, QA result |
| `../web/lesson-24.mp3` | streaming copy (site drop-in: private/lessons/lesson-24.mp3), 96 kbps CBR 44.1 kHz mono (same format as live Lesson 1 audio) |
| `/workspace/artifacts/S24-Give-Your-Son-A-Day-locked.mp3` (repo: `artifacts/`) | 96 kbps share copy |
