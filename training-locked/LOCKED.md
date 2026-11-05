# LOCKED — Steadfast Men training videos (finals)

Nothing in this folder changes without Aaron's OK. A new version gets a new file name and a new entry here; the old one is only removed when Aaron asks.

| Lesson | File | Length | Spec | Locked |
|---|---|---|---|---|
| Intro (L00) | `L00-intro/SM-L00-introduction-v13e-FINAL-1080p-ordinary-days.mp4` (29,103,727 bytes) | 3:44.08 | 1920x1080, 25 fps, H.264 + AAC, -20 LUFS | Final placed in Drive Nov 2, 2026 (Drive file id 129W80lA0AB0QRnbpGdv2iTgcrgZ59IrU) |
| Lesson 1 — A Quiet Tuesday | `L01-a-quiet-tuesday/L01-A-Quiet-Tuesday-v6-FINAL-1080p.mp4` (260,772,587 bytes — stored as 3 pieces; DOWNLOAD.md has the one-line join) | 20:14.32 | 1920x1080, 25 fps, H.264 + AAC 192k, -20 LUFS | Nov 3, 2026, 1:59 PM CT — Aaron: "beautiful, lock it down" |
| Lesson 2 — You Are Not Crazy | `L02-you-are-not-crazy/L02-You-Are-Not-Crazy-v7-FINAL-1080p.mp4` (393,868,754 bytes — stored as 5 pieces; DOWNLOAD.md has the one-line join) | 20:51.24 | 1920x1080, 25 fps, H.264 High@4.1 + AAC 160k, -20 LUFS | Nov 4, 2026, 2:05 PM CT — Aaron: "good, lock that in complete" |
| Lesson 3 — The Four Marks | `L03-the-four-marks/L03-The-Four-Marks-v3-FINAL-1080p.mp4` (381,089,824 bytes — stored as 5 pieces; DOWNLOAD.md has the one-line join) | 21:01.68 | 1920x1080, 25 fps, H.264 High@4.1 + AAC 160k, -20 LUFS | Nov 5, 2026, 10:14 AM CT — Aaron: "great lock in these 2" |
| Lesson 4 — Stop Waiting | `L04-stop-waiting/L04-Stop-Waiting-v3-FINAL-1080p.mp4` (378,551,672 bytes — stored as 5 pieces; DOWNLOAD.md has the one-line join) | 21:35.64 | 1920x1080, 25 fps, H.264 High@4.1 + AAC 160k, -20 LUFS | Nov 5, 2026, 10:14 AM CT — Aaron: "great lock in these 2" |

Checksums: `SHA256SUMS` in each lesson folder. Captions (`-en.vtt`, `-en.srt`) sit beside each video.

## Lesson 1 v6 — what it is
- Narration: v5 (the week-free read, cut only at sentence pauses; approved "audio is good"). 4.0 s silent open, logo end card.
- Wes: only the burgundy henley master — HeyGen video 90d853361e62719736c781537b50fdc5 "L01 FULL master u4 upright weekfree v3" (rendered on the v3 narration), re-timed frame-exact onto the v5 clock (`burg/remap_v3_to_v5.py`). Lip sync checked against v5: 0 ms offset in every 10 s window; 41 Wes shots within 5 ms.
- Framing: wide shots = full frame, faded into the field from y 660–840; card shots = crop 1120x800 at (400,0) in the 840x600 card. Hands kept out of view; two cuts moved to pauses for hand gestures (6:12 "You come home tired" → full-frame board; 10:27 "I got to feel like I'd shown up" → b-roll starts a sentence earlier).
- Not used: the 17 "L01 burg wide" clips (crew-neck tee — shirt would not match).
- Boards, b-roll (real stock, no AI imagery), layout and pacing unchanged from the approved v5 review. "Week" is never said or shown.

## Lesson 2 v7 — what it is
- Narration: the v2 20:42 read, HeyGen's own audio track from the master (highpass 70 Hz + level only). 4.0 s silent open, logo end card.
- Wes: HeyGen video 315207b517f3d3cb4ea01383561b18d2 "L02 v2 FULL master olive level no prompt 1243.2s" (byte-identical to HeyGen's 1080p download, ETag checked) plus the 20 "L02 v2 wide" clips (all ETag-checked; w01/w06/w10 re-pulled). Waist-up / half-screen pieces cut at pauses; none at 1:50 (Aaron).
- Encode: every Wes shot at CRF 16 slow/film, b-roll capped (qpmin 20), peaks under 12 Mb/s, level 4.1. No entry zoom (it wobbled the face in v5).
- B-roll real stock (Mixkit), matched to the line; Ray section: home laundry room, Wes tells the wallet and truck lines. "Week" is never said or shown.

## Lesson 3 v3 — what it is
- Narration: HeyGen's own audio from the master (highpass 70 Hz + level only, -20 LUFS). 4.0 s silent open, logo end card.
- Wes: HeyGen video 948c2751165551363eb887d6d48df62c "L03 FULL master" 1253.68 s (ETag 38c42373835ada9c35e14f0a3f7f4658-129, byte-identical) plus the 20 L03 wide gesture takes (all ETag-checked; placed by audio correlation 0.999). Waist-up / half-screen pieces cut at pauses, 3 s or longer.
- B-roll: real stock (Mixkit), horizontal only, matched to the line.
- v3 caption fix (Aaron, Nov 5, "around 6:24 they muddle together"): caption lines never overlap — the old line fades out (0.14 s), then the new one fades in (0.20 s); a carried-over line no longer flashes after a cut; a soft dark scrim sits behind captions on the wide gesture takes so hands never cross the text. "Week" is never said or shown.

## Lesson 4 v3 — what it is
- Narration: HeyGen's own audio from the master (highpass 70 Hz + 9.1 dB + limiter, -20 LUFS). 4.0 s silent open, logo end card.
- Wes: flannel tartan (HeyGen image 71569f3c). Full talking take 343c6afbc1f9578e316d475ea1561168, 1287.88 s (ETag ea462af8c17d63f5ce172e3bee3a7bc2-201, byte-identical) plus all 21 wide gesture takes of batch 66023ffee24d480582e0d8eb144a7679 (all ETag-checked; placed by audio correlation 0.995 or better).
- B-roll: real stock (Mixkit) — kayak (m7899), couple building furniture at home (m48654, replaces a workshop drill clip: residential over commercial), youth baseball (m23462), bat on the fence (m17371); soft bottom scrim so captions read over bright footage.
- Same caption rules as Lesson 3 v3. "Week" is never said or shown.
