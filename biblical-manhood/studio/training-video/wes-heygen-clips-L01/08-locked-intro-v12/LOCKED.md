# LOCKED — Steadfast Men Course Intro (v12)

- Locked: Oct 29, 2026, 12:48 PM CT — approved by Aaron Maberry: "Yup, replace it" (replace v11 with v12)
- Replaces v11.
- File: INTRO-FINAL-v12.mp4 — 136703632 bytes
- sha256: 855e5ffba5970bb6af01ae89c55137751eb907736304e760bbed8fae35e02548
- Spec: 1920x1080, 25 fps, H.264 + AAC, 208.68 s (5217 frames), -26 LUFS
- Drive: folder "LOCKED Training Videos/INTRO v12 (LOCKED 2026-10-29)" id 1crztZv3p8fvcYPPLhhkbZoePa1xDKXVg; mp4 file id 1g13C_m4qFnWpMn-vGkPe8EXRkwIHyONS (size 136703632 verified via Drive metadata 2026-10-29 12:58 PM CT)

## What changed vs v11
- Workbook page 0:44.84–0:57.44: AI pseudo body text blurred on both pages; headings kept sharp
- Subtitles (SRT/VTT): "pick up the wait" -> "pick up the weight"
- Everything else identical: audio bit-identical (same packets, md5 0eda933e6e0fd49fae47e3c86b18d633), same timing, transitions, podcast image, length. Frames outside 0:44.76–1:04.76 pixel-identical to v11; that 20 s GOP span was re-encoded (x264 crf12).

## Files
INTRO-FINAL-v12.mp4, .srt, .vtt, podcast-v12.jpg (same as podcast-v11.jpg), SHA256SUMS; source/ = rebuild assets (raw HeyGen c25a93f0, v23 audio, build scripts, v11 assets, patch_workbook.py). Rebuild v12 = run source/patch_workbook.py on v11 GOPs 1119–1618 and splice (see source/README-v12.md).
