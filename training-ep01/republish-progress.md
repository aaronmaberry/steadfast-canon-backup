# Republish progress — timeframe cleanup 2026-10-22 (Aaron approved)
## Done
- Script edits: S01(+W01 md, S01-v2 mirror), S07, S12 (2 lines), S15, S20; LOCKED-SESSIONS.md updated (rev 2026-10-22).
- PDFs: 24 transcripts rebuilt; steadfast-main commit 468c878 pushed; Vercel status success 7:50 AM CT.
- Backup repo steadfast-canon-backup: commit 4df4ab4 pushed (scripts + registry).
- ElevenLabs: all 108 paragraph takes generated (flow dZjjskDzdN4tAGVzeyMY), 62,611 chars (~$10.33). raws in /workspace/tf-splice/raw. DO NOT regenerate.
## In progress
- Splicing (/workspace/tf-splice, runall.py 2; done = work/NNN/splice.json exists).
## Per-lesson remix/publish
(none yet)
- 09:28 CT: all 108 paragraphs spliced into work/SNN-secXX.voice.wav; running secqa.py (whole-section STT vs new text, results secqa.json)
- 10:24 CT: secqa pass1 done (77 sections); 25 flagged, rerun with VAD (secqa2.json)
- 10:51 CT: secqa2 (VAD) abandoned: whole-section whisper drops text inconsistently between runs. Switched to bqa.py (boundary-window STT at each cut, small.en, low mem); results bqa.json
- 11:03 CT: bqa pass done on 108; flagged sections to be rebuilt with resplice.py (one-pass word-aligned cut from original voice)
- 11:18 CT: resplice running (nohup, log tf-splice/resplice.log) for 12 sections: S01-sec02 S02-sec12 S03-sec08 S04-sec01 S05-sec11 S07-sec02 S07-sec10 S08-sec01 S08-sec02 S09-sec01 S13-sec13 S14-sec01; then bqa on their ids. Next: remix.py NN per lesson.
- 11:42 CT: 11/12 resplices done + bqa OK; S08-sec01 resplice rerun (fix for adjacent paragraphs), log resplice2.log
- 11:54 CT: QA complete, all 108 splices pass boundary STT. Starting remix chain (remix.log); each lesson logs a line below when done.
- S01: 7 paragraphs spliced (secs 02,08,09,14), remixed 27:48, published to locked/audio + web — 11:55 CT
- S02: 6 paragraphs spliced (secs 01,03,11,12), remixed 24:42, published to locked/audio + web — 11:56 CT
- S03: 6 paragraphs spliced (secs 01,03,08,13), remixed 24:16, published to locked/audio + web — 11:58 CT
- S04: 3 paragraphs spliced (secs 01,11), remixed 23:59, stage only (not published) — 11:58 CT
- S05: 7 paragraphs spliced (secs 01,11), remixed 24:09, stage only (not published) — 11:59 CT
- 12:00 CT: BUG found: splices whose paragraph starts at 0 s kept the whole old section (S01-sec14, S10-sec01, S24-sec13 doubled). Resplicing these 3 (resplice3.log); S01, S10, S24 must be re-remixed after.
- S06: 3 paragraphs spliced (secs 01,02), remixed 24:58, stage only (not published) — 12:00 CT
- S07: 4 paragraphs spliced (secs 01,02,10,12), remixed 24:33, published to locked/audio + web — 12:02 CT
- S08: 4 paragraphs spliced (secs 01,02,08), remixed 23:59, published to locked/audio + web — 12:03 CT
- S09: 3 paragraphs spliced (secs 01,02), remixed 24:27, stage only (not published) — 12:04 CT
- S10: 7 paragraphs spliced (secs 01,02,04,11), remixed 24:28, stage only (not published) — 12:05 CT
- S11: 1 paragraphs spliced (secs 01), remixed 24:05, stage only (not published) — 12:06 CT
- S12: 7 paragraphs spliced (secs 01,02,06,07,11,12), remixed 24:25, published to locked/audio + web — 12:07 CT
- S13: 4 paragraphs spliced (secs 01,02,13), remixed 21:50, stage only (not published) — 12:08 CT
- S14: 2 paragraphs spliced (secs 01), remixed 24:51, stage only (not published) — 12:09 CT
- S15: 5 paragraphs spliced (secs 01,02,09,12), remixed 25:01, stage only (not published) — 12:10 CT
- S16: 5 paragraphs spliced (secs 01,02,11,12), remixed 24:30, stage only (not published) — 12:11 CT
- S17: 3 paragraphs spliced (secs 01,02,09), remixed 25:37, stage only (not published) — 12:12 CT
- 12:13 CT: 3 resplices done, bqa OK (S01-sec14 132.8s, S10-sec01 133.0s, S24-sec13 104.3s)
- S18: 2 paragraphs spliced (secs 01,02), remixed 24:58, stage only (not published) — 12:13 CT
- S19: 5 paragraphs spliced (secs 01,02,12), remixed 24:33, stage only (not published) — 12:14 CT
- S20: 3 paragraphs spliced (secs 01,02,04), remixed 25:33, stage only (not published) — 12:15 CT
- S21: 2 paragraphs spliced (secs 01,02), remixed 24:07, stage only (not published) — 12:16 CT
- S22: 7 paragraphs spliced (secs 01,02,07,09,11), remixed 24:38, stage only (not published) — 12:17 CT
- S23: 4 paragraphs spliced (secs 01,02,11), remixed 24:09, stage only (not published) — 12:18 CT
- S24: 8 paragraphs spliced (secs 01,02,07,11,12,13), remixed 26:23, published to locked/audio + web — 12:19 CT
- S10: 7 paragraphs spliced (secs 01,02,04,11), remixed 24:28, stage only (not published) — 12:33 CT
- S01: 7 paragraphs spliced (secs 02,08,09,14), remixed 25:41, published to locked/audio + web — 12:33 CT
- 12:36 CT: lesson-01.mp3 (25:41) committed+pushed to steadfast-main
- 12:38 CT: Vercel deploy success for f9d374a (12:37 CT); live mp3 is auth-gated
