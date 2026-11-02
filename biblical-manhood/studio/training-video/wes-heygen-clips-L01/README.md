# Wes HeyGen clips + Lesson 1 v4 build kit (for Claude)

## The job
Rebuild or improve **Steadfast Men Lesson 1 ("A Quiet Tuesday")**, about 20:25 long, presented by the HeyGen avatar "Wes". The current v4 cut got a **C- grade**. Beat it on these points:
- **No blurred or visible splices.** Lip-patch joins and cuts must not show.
- **Restrained hands.** No hand or fingertip flashes in frame.
- **No chin jut.**
- **Real b-roll variety.**
- **Pace ~150 wpm.** v4 runs ~148 wpm.
- **Loudness -26 LUFS integrated.**
- **Never say or show the word "week"/"weeks".** Use the week-free audio in `05-audio-L01-v3-weekfree-USED-IN-V4/`.
- **walksteadfast.com colors and fonts.** See the SOP.

Read `06-script-docs/LESSON-VIDEO-SOP.md` first. Then read `02-v4-master-kit/V4-QC-REPORT.md`.

## Fetch everything
```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/aaronmaberry/steadfast-canon-backup
cd steadfast-canon-backup
git sparse-checkout set biblical-manhood/studio/training-video/wes-heygen-clips-L01
cd biblical-manhood/studio/training-video/wes-heygen-clips-L01
gh release download wes-heygen-clips-L01 -R aaronmaberry/steadfast-canon-backup -D release-assets   # ~3.1 GB, 85 files
```

## Folder map
| folder | contents |
|---|---|
| 01-wide-segments-v4 | The 17 HeyGen full-frame Wes takes, `hg_w00`-`hg_w16`, 1080p, plus the audio-driver mp3 for each. Their video_ids are in `video_ids.json`. Each clip covers the audio range in its mp3 name, with 0.6 s handles. Together they fill all 21 WES_FULL shots. |
| 02-v4-master-kit | The 720p v4 review copy, the EDL (csv and json), captions (SRT/VTT), the b-roll manifest, the wide-segment json, the QC report, the contact sheet, previews, and QC json/logs. |
| 03-render-code | The v4 render code, `l01v4/build/render_v4.py` with helpers (stab, tmap, windows, kinetic, captions, gate, avsync), plus the shell drivers. `l01v3` holds the previous version. |
| 04-avatar-iv-source-take | A 540p review of the patched take, and `patch-meta`: the windows, accept json, patch wavs, and scripts. **The source take itself is a release asset**: `L01-P5-PATCHED-v2.mp4`, 1.3 GB. It feeds every bubble and split-panel shot. The 81 patch clips (`orig_P*`, `t1-t4_P*`, `v2_P*`) are release assets too. |
| 05-audio-L01-v3-weekfree-USED-IN-V4 | The v4 master audio (mp3, -26 LUFS) plus the cut scripts and json. The WAV is a release asset. |
| 05b-audio-L01-v2-approved-source | The approved audio v2 mp3 that drove the Avatar IV take 4c7713cd, with word timings, line times, and the script. The WAV is a release asset. |
| 06-script-docs | The spoken script v5, the production script and storyboard, the retimed storyboards, SPEND.md (every HeyGen job id and its credits), PROGRESS, and the SOP. |

## How the files map to the timeline
- `L01-P7-v4-EDL.csv` lists `id,kind,t0,t1` on the master timeline. The shot kinds are:
  - TITLE_CARD
  - AGENDA
  - SPLIT (22 shots)
  - WES_FULL (21 shots)
  - TYPE_BOARD_BUBBLE (16)
  - SCRIPTURE_BUBBLE (6)
  - COVER_BOARD (3)
  - BRANDED_STILL_BUBBLE (2)
  - LOGO_END
- **WES_FULL** shots come from `01-wide-segments-v4/hg_wNN.mp4`. `L01-P7-v4-heygen-wide-segments.json` maps each segment to its shot ids and audio range. CLIPS-MANIFEST.md lists the master timestamps.
- **SPLIT and the *_BUBBLE shots** use `release-assets/L01-P5-PATCHED-v2.mp4`, which follows audio-v2 time. `build/tmap.py` maps v3/v4 time (after the week cut) back to v2 time. The cut points are in `audio_cuts*.json`.
- The b-roll is listed in `L01-P7-v4-broll-manifest.csv`. The b-roll media is stock and is **not** in this kit; re-fetch it by the ids in the manifest.

## Known v4 issues to fix
- About 1.5 s of single-frame hand or fingertip flashes remain. Timestamps are in the QC report.
- The wide HeyGen takes are not stabilized and keep HeyGen's native head motion.
- Chin-jut frames went from 23 (v3) to 41 in the wide takes. w12 is the worst, with 44.
- The bubble and split panel use the old Avatar IV take, so face size and lighting differ from the wide takes.
- Splices at the lip-patch windows can look soft or blurred.
- The b-roll variety is weak.
- About **306 HeyGen credits** are left. Do not resubmit any job that SPEND.md marks "Do NOT resubmit".

## NOT in this repo
- **Intentionally not included:** the intro v12 (`INTRO-FINAL-v12.mp4`, its raw HeyGen source and build files) and all HeyGen look/motion/mouth-tone/A-B/wide-soft test sets and test renders. This kit is Lesson 1 HeyGen clips only.
- The 1080p v4 master `L01-P7-ASSEMBLED-v4.mp4` (639 MB). It is going to Google Drive separately.
- The older masters v1, v2, and v3, plus `L01-P5-PATCHED-v1`.
- The stock b-roll source and mezzanine files (`/workspace/l01v3/broll`, about 2 GB).
- Tracking dumps, frame dirs, render chunks, and float audio intermediates.
- The look-generation PNGs.
