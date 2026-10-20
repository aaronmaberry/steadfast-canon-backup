# Steadfast Men — Session 2 "You Are Not Crazy" — locked training audio

Recording of the **LOCKED** script (not a review).
- Script (locked 2026-10-20, spoken word for word): `training-ep01/scripts-v7/S02-You-Are-Not-Crazy.txt`, sha256 `93f03f8e13f7727505a47e663f0a0f82acbe23ebd8295f43668795ad438b4549`.
  `# SECTION` / `# CUT SCREEN` lines and room cues are not spoken; tone tags (`[warmly]`, `[dry]`, …) are delivery direction only.
- Voice: ElevenLabs **Wes Hart - Option D**, voice ID `krjoGt4x3CttlxSuoDYW` (locked training voice, LOCKED-LECTURE-STYLE.md), model `eleven_v4`, one take per section, generations_count 1.
- Pipeline (unchanged, training-ep01/locked/): prep.py -> eleven_v4 -> post.sh (atempo 0.93, retime.py, capgaps.py) -> mix.sh (hall IR + room tone + loudnorm I=-16 TP=-1.5) -> check.py + faster-whisper medium.en QA (see QA.txt).
- Generation format: ElevenLabs output mp3_44100_128 (44.1 kHz, 128 kbps) for every section. On 2026-10-20 Aaron asked for best quality (pcm_44100, else mp3_44100_192) going forward, but the ElevenLabs creative tool used here does not expose an output_format setting for eleven_v4 (setting it was rejected), so mp3_44100_128 was the highest available. Masters are mixed and exported from these sources as 16-bit 44.1 kHz WAV.
- Section breaks: 1.2 s x25.
- Recorded 2026-10-20 CT. Runtime 24:40 (1480.4 s). 13 sections. 19,272 characters. Cost 19272 credits ($3.18).

| File | Notes |
|---|---|
| `S02-You-Are-Not-Crazy-full.mp3` | full session, 192 kbps, 44.1 kHz mono |
| `S02-You-Are-Not-Crazy-master.wav` | full session master, 16-bit 44.1 kHz mono (Git LFS) |
| `sections/S02-secNN-<title>.mp3` | per-section mixes, 192 kbps |
| `gen.log`, `QA.txt` | generation ids/credits, QA result |
| `../web/lesson-02.mp3` | streaming copy (site drop-in: private/lessons/lesson-02.mp3), 96 kbps CBR 44.1 kHz mono (same format as live Lesson 1 audio) |
| `/workspace/artifacts/S02-You-Are-Not-Crazy-locked.mp3` (repo: `artifacts/`) | 96 kbps share copy |
