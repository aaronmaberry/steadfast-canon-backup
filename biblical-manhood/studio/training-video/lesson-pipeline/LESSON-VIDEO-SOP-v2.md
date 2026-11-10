# STEADFAST MEN — LESSON VIDEO SOP v2 (HeyGen master pipeline)

**Status:** live as of Nov 5, 2026, 10:14 AM CT, when Aaron locked L03 and L04. This is the process that made the locked L02, L03 and L04 masters. It replaces the production steps in the Oct 28–29 SOP (`wes-heygen-clips-L01/06-script-docs/LESSON-VIDEO-SOP.md`: ElevenLabs source, Voice Changer, −26 LUFS, look plans). That file is still the history and decision log for L00–L01.

**For L05–L24:** run `new_lesson.sh NN "LNN-Title-Words"`, then work through §2 top to bottom. Every gate must pass before the next step. Every correction Aaron has given so far is a rule in §1. When he gives a new one, add it to §1 and §4 in the same turn (R30, correction loop).

---
## 1. RULES — every lesson, no exceptions
Each rule shows where it came from. ✅ = checked by a script; 👁 = checked by eye at QC.

### Approval and handling
| # | Rule | From |
|---|---|---|
| A1 | Nothing is published, uploaded, locked or put on Drive without Aaron's OK. Locking = repo `training-locked/` on his words "lock". | standing |
| A2 | HeyGen credit spend needs Aaron's explicit OK. Rendering, editing and QC are free. | standing |
| A3 | Use only the FINAL HeyGen renders named in Aaron's message or in `FINAL-HEYGEN-RENDERS-REFERENCE.md/.csv`. Never use a "do not use" clip. | L03 |
| A4 | Never permanently delete Aaron's data (Drive trash only, and only when asked). Never ask for or enter passwords. | standing |
| A5 | Each file sent for review must be under 400 MiB (the send limit). CRF 18 lands at ~360–370 MiB for a ~21 min lesson. | L03 |
| A6 | Tell Aaron to review the downloaded file, not in the Claude app player. The app's player stutters the sound, but the file is clean (L02 "skip/stutter/click" was the player). | L02 |

### Script and words
| # | Rule | From |
|---|---|---|
| W1 | ✅ The word "week" is never said or shown. `srt2cues.py` and `captions.py` fail if it appears. | L01 |
| W2 | 👁 Every word on screen is Wes's own words from the script (boards, bands, labels). Plain labels such as names or verse references are the only exception. | standing |
| W3 | 👁 Board/band names in `boards_lNN.py` must not reuse a base name (BLACK, CARD, FIELD, LOGO, LT, OPEN). L03 "CARD" overwrote the Wes card frame; it was renamed WRITECARD. | L03 |

### Audio
| # | Rule | From |
|---|---|---|
| S1 | ✅ The narration is the master's own audio, used as one continuous track. Never stitch, patch or splice audio. The audio may only break at a pause. | L02 |
| S2 | ✅ Program loudness −20.0 LUFS (±0.1), true peak below −1 dBFS. `prog_audio.py` finds the gain by measuring; it varies (+6 dB L03, +9.1 dB L04). | L02–L04 |
| S3 | ✅ Open with 4.0 s of silence and end on the logo card. Captions shift by +4.0 s. | L01 |

### Wes on camera
| # | Rule | From |
|---|---|---|
| C1 | Talking head is the priority. Mix waist-up wides and half-screen (split card) shots. Cuts go in pauses (`k()` = cut in the pause before the cue). | L02 |
| C2 | ✅ Every Wes piece (W/P/WW) is 3 s or longer. Full-frame name stings (one word, e.g. "Peace.") may be 2.4–3 s. | L02, L04 |
| C3 | No zoom or "settle" on shot entries. It wobbles the face (L02 v5). Wide takes are cut to the nearest frame (`trim=start_frame`). | L02 |
| C4 | ✅ Never show a hand rising into the frame, a chin jut/lean (face width > 1.14 × rolling median) or a soft face. `quality.py` masks these, and `layout.check_all` refuses shots on them. Wide takes are used only 0.5 s inside their ends. | L01–L03 |
| C5 | 👁 Drop any wide take that looks warped. Cut a wide shot before the hands come back up at its end. L02 1:50 was removed ("deleting is the easy fix"), and L02 13:16 was ended 1–2 s earlier. | L02 |
| C6 | ✅ Every master and wide clip is byte-identical to HeyGen's file. `plan/verify_heygen.py` checks the S3 ETag over 8 MiB parts of the *joined* file (a small clip has a single-part ETag = plain MD5; the script handles both). | L02–L06 |
| C7 | ✅ Wardrobe must not read as skin. After `scan.py`, the line `N with a hand-sized blob` must be a small fraction of frames. If it is near 100%, the shirt/coat is inside the skin colour range: sample coat vs face (YCrCb Cr, HSV hue) and set `SKIN_CR_MIN` / `SKIN_HUE_MAX` in `scan.py` **and** `widescan.py` (L06 tan chore coat: Cr 146, hue ≤ 12). Re-run scan → widescan → quality. | L06 |

### B-roll
| # | Rule | From |
|---|---|---|
| B1 | Real footage only (Mixkit stock). No AI-generated imagery. | L02 |
| B2 | 👁 It must match the spoken line literally. Residential over commercial: a home, not a shop, laundromat or workshop. No props the line doesn't mention: no gloves or nicked-up hands for a man doing a small job, no cash, no SUV when he says truck. If nothing fits, use Wes on camera. | L02 (Ray section), L04 (drill → couple at home) |
| B3 | ✅ Horizontal clips only (L03 rejected m33181 and m41173 as vertical). | L03 |
| B4 | 👁 Check a 6-frame strip of the *whole* clip. Then set `src_in` so the used window has no unrelated action (L04 m48654 ends before the high-five). | L04 |
| B5 | No clip is used twice. | standing |

### Captions (the lower text bands) — Aaron, Nov 5: "nice, crisp, and clean"
| # | Rule | From |
|---|---|---|
| T1 | ✅ Two caption lines are never on screen at once. Band → band changes are sequential: the old line fades out over 0.14 s, then the new one fades in over 0.20 s (`overlays(..., seq=True)` in render.py). Boards may still cross-build, because a full board covers the one under it. | L03 6:24 |
| T2 | ✅ No flash of the last line after a cut. If a carried-over line would be replaced within 0.5 s, the cut takes it and the new line simply fades in. | L03 |
| T3 | ✅ Text is never over a busy picture. A soft dark bottom scrim sits behind bands on b-roll (`RSCRIM.png`, up to 62%) and on wide gesture takes (`WWSCRIM.png`, up to 74%), so bright footage and Wes's hands never cross the words. W shots already fade into the field. | L04, L03 |
| T4 | ✅ Every band and board stays up long enough to read: `layout.py` PROBLEM lines = 0. Fix a short band by dropping it, extending the shot to the next cue, or letting Wes say it bare. Never by squeezing it in. | L02–L04 |

### Encode
| # | Rule | From |
|---|---|---|
| E1 | ✅ libx264 `-preset slow -tune film`, High@4.1, `ref=4:vbv-maxrate=12000:vbv-bufsize=24000`, b-roll `qpmin=20`, **one CRF for every segment: 18 up to ~22:30 of picture, 19 above that** (L05 22:47 = 398 MiB at 18; L06 23:21 needed 19 to stay under A5) (segments are stream-copied together, and the PPS depends on CRF). `postcheck.py` must show 1 SPS/PPS set and 0 decode errors. | L02, L03 |

---
## 2. STEPS (one lesson, ~3–4 h of machine time)
Paths are relative to `/home/claude/lNN/`. Package = this folder (`lesson-pipeline/`).

1. **Inputs from Aaron**
   - Review-release SRT (`LNN-v1.srt`) and lesson title.
   - HeyGen video ids: one FULL talking take, plus all the wide gesture takes he lists (w00…wNN, or a batch id).
   - Wes's shirt source (for the notes).
   - Put the SRT in `in/` and write `in/etags.txt` (id → expected ETag).
2. **Download from HeyGen**
   - In Chrome, open a light page on app.heygen.com (`/robots.txt?x=2`; the app page itself freezes).
   - POST the video.download API per id and fetch `https://resource2.heygen.ai/video/transcode/<id>/1920x1080_nocap.mp4`.
   - Save wides directly. Save the master in 47,185,920-byte parts.
   - Chrome often saves blobs as random `.tmp` names. Map wides by their unique size, and master parts by mtime order (the last part is the short one).
   - Stage one file per call (big parallel stages time out).
   - Join the master parts in mtime order into `master/lNN_master.mp4`.
   - Record every id's size + ETag first (HEAD request) into `in/etags.txt` (`key id size etag`).
   - **Gate C6:** `python3 plan/verify_heygen.py` (moves matching wides into `wide/`) and `python3 plan/verify_heygen.py master master/lNN_master.mp4`.
3. **Set up the lesson**
   - `bash <package>/new_lesson.sh NN "LNN-Title-Words"`.
   - Set `AUDIO_END` (edit/cues.py) and `TOTAL` (plan/quality.py) to the master duration from ffprobe.
4. **Cues and words**
   - `python3 plan/srt2cues.py in/LNN-v1.srt` (gate W1).
   - `ffmpeg -i master/lNN_master.mp4 -vn -ac 1 -ar 48000 -c:a pcm_s16le audio/narr_raw.wav`.
   - `python3 plan/words.py`.
   - **Gate:** 0 cues off by more than 0.4 s between `lines.json` and the SRT (the voice matches the captions).
5. **Picture maps**
   - `python3 plan/scan.py` (~10 min, background). **Gate C7:** hand-sized blobs must not be in nearly every frame.
   - `echo [] > master/warp_runs.json`.
   - `python3 plan/align_wides.py`. **Gate:** every wide correlation ≥ 0.99.
   - Write `wide/verified.json` ({master:{id,etag,match}, wide:{id:true}}).
   - `python3 plan/widescan.py`, then `python3 plan/quality.py`.
6. **Boards**
   - Write `gfx/boards_lNN.py` from the script, using `boards_l04_EXAMPLE.py` as the model:
     - TITLE with `progress(NN)`
     - AG agenda
     - LAST recap
     - name stings
     - scripture cards with the reference
     - stacked lists that build one row at a time
     - NEXT with `progress(NN+1)` and the next lesson's title
   - `cat gfx/boards_base.py gfx/boards_lNN.py gfx/boards_main.py > gfx/boards.py && python3 gfx/boards.py`.
   - 👁 Contact-sheet the boards for overflow and wording (W2, W3).
7. **B-roll**
   - Pick clips on mixkit.co for the lines that are pictures (a story moment, an object Wes names).
   - Download them in Chrome from a mixkit.co page: fetch `https://assets.mixkit.co/videos/<id>/<id>-720.mp4` (1080 is usually 403) and save it as a blob. The container shell is blocked from mixkit.
   - Stage them, then copy to `broll/m<id>.mp4`.
   - **Gate B1–B4:** ffprobe the size (horizontal) and look at a 6-frame strip of the whole clip. Replace any that fail, or switch that shot to Wes.
8. **The cut (`edit/spec.py`)**
   - Shot types: `W` (Wes full frame + bands), `P` (split: board left, Wes card right), `F` (full board), `R` (b-roll + label bands, optional `src_in`).
   - Cut points use `k(cue)` / `k("word", cue)`; band times use `c(cue)`.
   - Keep W/P/WW ≥ 3 s (C2).
   - `python3 edit/layout.py`. **Gate T4:** no PROBLEM lines.
   - Then list any W/P/WW shorter than 3 s and fix them. Example: L04 "They won't. I checked." became a 5.8 s Wes shot instead of a 2 s cut-in, by letting the lead-in line play on camera, because the house list builds up.
9. **Audio and captions**
   - `python3 plan/prog_audio.py` (gate S2).
   - `python3 plan/captions.py in/LNN-v1.srt deliver/LNN-Title-Words-v1`.
10. **Render**
    - `cd edit && python3 render.py --crf 18` (~20–25 min; cached segments are reused).
    - Then `python3 finish.py && python3 postcheck.py`. **Gates E1, A5, S2:** 1 SPS/PPS, 0 decode errors, under 400 MiB, −20.0 LUFS.
11. **QC — all of it, every time**
    - `python3 qc_v6.py`: every Wes shot's face PSNR ≥ 36 dB vs. the source (W/P median ~39). A WW "low" at a shot start is usually the checker's seek landing one frame off. Confirm with a full-frame compare before acting.
    - `python3 bandcheck.py ../deliver/<file>.mp4 <scratch dir>`, then 👁 every sheet. Gate T1/T2: never two lines at once, never a 1-frame flash.
    - 👁 A contact sheet of ~10 frames across the lesson, plus a full-size frame of every R and captioned WW shot (gate T3: text clear of bright footage and hands).
    - 👁 Look at every b-roll window you used (B2/B4).
12. **Send for review**
    - Send the mp4 + .srt + .vtt (`-vN` names; never overwrite a version Aaron has seen).
    - Report briefly what changed from the plan and why, and remind him to watch the downloaded file.
13. **Lock (only on Aaron's word)**
    - Make `training-locked/LNN-slug/` with `<name>-FINAL-1080p.mp4` split into 90,000,000-byte pieces (`split -b 90000000 -d -a 1`).
    - Add `DOWNLOAD.md` (Windows `copy /b` + Mac/Linux `cat` join), the captions, and `SHA256SUMS` (whole file, captions, pieces). **Gate:** the joined pieces' sha256 = the reviewed file's sha256.
    - Add a row to `LOCKED.md` (bytes, length, spec, date/time CT, Aaron's words) and a "what it is" section.
    - Commit and push one piece per commit (GitHub's 50 MB warnings are expected; the hard limit is 100 MB).
    - Delete superseded review cuts in the workspace (never Aaron's files).

---
## 3. RUNNING NOTES (tooling)
- `words.py` once crashed when a voiced run had no punctuation boundary (`groups[-1]` was None). It is fixed in the template; keep the fix.
- Disk is a fixed allowance (~250 GB volume, low free space). Before a lesson, delete the previous lesson's staged `.tmp` downloads and superseded deliverables. A lesson needs ~3 GB of free space (master 1.7 GB, wides ~0.4 GB, segments ~0.7 GB, file 0.37 GB).
- The board renderer and the HTML templates, fonts and logo live in `lesson-pipeline/graphics/`. `new_lesson.sh` points the lesson there.
- Chrome tab for HeyGen API calls: keep one light page open. Classifier or tool hiccups are transient; retry once and don't loop.
- L07 (Nov 10): staging from Aaron's PC slowed to ~200 KB/s and every 47 MB part hit the stage wall-clock timeout, while the Chrome tab froze mid-download. Fix: close the frozen tab, open a fresh light page, and re-fetch the remaining byte range in 15 MiB (15,728,640-byte) Range pieces (`L07N-NNN.bin`); 15 MiB stages fit the timeout. Chrome silently drops some blob downloads (3 of 98): list the folder, re-fetch the gaps under a new name, then join and run the ETag check (C6) — it caught nothing wrong, but it is the only proof the order is right.
- L07: panel boards need their `_F` twins rendered too (render.py falls back to them). After adding boards, re-run the full `boards.py`, not a name list.
- L07: watch for a one-word orphan on big full boards (CROSSSTAYED wrapped "it."). Drop the size until the line fits.
- L08 (Nov 10): the review release had no .srt (not attached, not inside the mp4). Build one from the spoken script: `plan/align_script.py audio/narr_raw.wav in/LNN-lines.txt in/LNN-v1.srt` (lines = the numbered `Lnnn` rows of the SPOKEN-SCRIPT md on the `lesson-NN-script-v1` branch, `in/LNN-pauses.txt` = each row's [pause N]; [beat] stays inline). Gate: every line end lands on a voice stop, and OCR of the release's own boards at ~30 points (tesseract is installed) must show our cue starting at or a few seconds before the board. Ask Aaron for the .srt in parallel. The plain `.txt` script on that branch is the same words; use the md for its line breaks and pauses.
- L08: download every HeyGen file (wides too) as 10 MiB Range pieces named `LNN-<key>-NNN.bin`, 4 s apart, from one light tab; stage 3 per call. Whole-file blobs over ~20 MB timed out or were dropped by Chrome. Chrome also showed a multiple-downloads prompt; Aaron allowed it.

## 4. CORRECTION LOG (newest first; each one is already a rule above)
- **Nov 9, 2026 — L05/L06 builds (my QC):** L06 chore coat read as skin → every frame flagged as a hand; fixed with per-lesson skin thresholds (C7). L06 at 23:21 would exceed 400 MiB at CRF 18 → CRF 19 (E1). HeyGen single-part ETag on a 3 MB wide → verify script handles it (C6). B-roll rejected for B2: holiday-feast dinner sets (twice), gloved/female hands for Wade's plate; L05 and L06 kept to Wes where no true clip existed.
- **Nov 5, 2026, 8:00 AM CT — L03 v2, Aaron:** "text captions … around 6:24 … they muddle together … garbled … make sure they're nice, crisp, and clean." Cause: a new band faded in on top of the fully visible old one (0.3 s overlap), at 32 changes in L03 and 31 in L04. Fix: T1, T2, T3 (wide-take scrim added as well). L03/L04 v3 re-rendered; every change checked frame by frame. Locked 10:14 AM ("great lock in these 2 … make sure SOP … is updated on those corrections moving forward").
- **Nov 4, 2026 — L04 build (my QC before Aaron saw it):** the workshop drill clip was replaced with a home clip (B2). The bright-footage scrim was added (T3). Seven unreadable bands were fixed and one 2 s Wes piece lengthened (T4, C2).
- **Nov 4, 2026 — L03 build:** the CARD name clash (W3). Jut threshold 1.08 flagged normal laughs, so it was raised to 1.14 (C4). CRF 16 went over the send limit, so CRF 18 (A5). Vertical clips rejected (B3).
- **Nov 4, 2026 — L02 v6, Aaron:** removed the warped 1:50 wide (C5). "One seamless track": audio verified identical; the stutter was the app player (S1, A6). Ray b-roll: residential, no gloves or nicked hands (B2). 12:15: no cash, no SUV for "truck" (B2). 13:16: end the wide before the hands come up (C5). Locked v7, 2:05 PM.
- **Oct 29, 2026 — L01 v1, Aaron (C−):** never show a blurred join; edit around it. Hands and chin jut. Too little b-roll. The word "weeks" is banned (W1, C4).
