# INTRO v12 CANDIDATE (not approved; v11 remains the lock)
Built 2026-10-29 from LOCKED-INTRO-v11 (read-only, sha256 verified unchanged).
Fixes: (1) blurred AI pseudo body text on workbook pages 44.84-57.44 s (headings kept); (2) SRT/VTT "pick up the wait" -> "weight".
Method: frames 1119-1618 (GOPs 44.76-64.76 s) decoded from v11, blur mask applied (work/patch_workbook.py), re-encoded x264 crf12; all other video packets and the full audio stream copied bit-exact from v11.
out/INTRO-FINAL-v12.mp4 sha256 855e5ffba5970bb6af01ae89c55137751eb907736304e760bbed8fae35e02548
NOTE 2026-10-29: v11 mp4 was deleted after the v12 lock, so patch_workbook.py cannot be re-run as-is. Future edits start from INTRO-FINAL-v12.mp4 (same GOP splice method) or a full rebuild from build-scripts + raw HeyGen + v23 audio.
