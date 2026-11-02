# L01 P7 v4 QC report (Nov 2, 2026, 11:45 AM CT)

Master: L01-P7-ASSEMBLED-v4.mp4. 1920x1080, 25 fps, 30,629 frames. Video 1225.16 s, audio 1225.15 s (20:25). h264 + MP3, 639 MB.
Audio: stream copy of L01-v3-weekfree-minus26-LUFS.mp3. The extracted audio stream hash is identical to the v3 master's (53dbef41…). The approved source (80c7a27b…) was not touched.
Review copy: L01-P7-v4-REVIEW-720p.mp4, 77 MB.

## Loudness and pace vs the intro (INTRO v12, locked)
| | Integrated | LRA | Pace |
|---|---|---|---|
| INTRO v12 | -26.0 LUFS | 3.7 LU | 148.9 wpm |
| L01 v4 | -26.0 LUFS | 4.7 LU | ~148 wpm (3,028 words / 1225 s) |

The audio is the same as v3, so the week scan carries over from v3: 0 "week"/"weeks" words in the small.en ASR. Captions are reused from v3 (same audio).

## What changed in v4
1. **Bubble face-lock.** Translation-only stabilization, k 0.8, sigma 20 frames (~0.8 s). Test at out 75-95 s:
   - Vertical movement went from 35.2 px to 17.6 px (-50%). As a share of face width: 18.3% to 10.4%.
   - Size swing 3.5% to 3.3%. Hand frames 0. Chin-jut frames 9 to 2.
   - PASS: the target was a 40% or larger drop.
2. **Bubble crop.** 12 of 14 runs widened to 680x800 because the hand check allowed it. Runs 10 and 44-47 stay at 600x706.
3. **HeyGen wide re-render.** All 21 full-frame Wes shots were re-rendered as 17 segments, 365.4 s total, with 0.6 s handles.
   - Recipe: look 58ea634e… (raised hand replaced by a mirrored shoulder), Avatar IV, 1080p, low expressiveness, SOP motion prompt plus "hands stay below frame".
   - Shown at native 1:1 (R22), with a bottom fade into the backdrop from y=880.
   - Face width is ~333 px, compared with 192 px in the v3 card.
4. **MED 1280x720 cards.** Built (5 segments, 28.9 s), but the wide takes replace them everywhere. They are kept only as a fallback in the code.
5. **Fade-out fix at 4:17.9.** The bubble now cuts out in the pause after "job." Checked in qc/fix4179.jpg: no ghost.
6. **Transitions.** All 18 morphs became dips inside the word gaps. The mix is now dip 33, xfade 15, push 15, hard 9 (none over 40%).

## Credits
- 433 before.
- 427 after the test (6 credits).
- 306 after the batch (121 credits).
- Total v4 spend: 127, under the 250 cap.

## Hands (whole master, every 2nd frame, mediapipe on visible Wes regions; the wide card is checked over the full frame)
| layout | Wes on screen | hand frames (sec) |
|---|---|---|
| Full-frame wide take | 225.2 s | 0.8 s |
| Split panel | 266.7 s | 0.4 s |
| Bubble | 446.5 s | 0.3 s |
| **Total** | | **1.5 s** (v3: 1.8 s; v2: ~201 s) |

PASS: the target was under ~20 s. Each hit is a single-frame flash:
- Wide: 0:57, 3:41, 3:42, 8:10, 10:00, 10:30, 10:46, 13:26, 14:21
- Panel: 3:35, 10:16, 17:19, 19:54
- Bubble: 3:05, 4:15, 9:51, 13:04

## Chin jut (dz < -150 frames)
- Wide: 41 (v3 card: 23)
- Panel: 36 (unchanged)
- Bubble: 0

The HeyGen wide takes jut slightly more. Each clip has 0-44 frames at jut150; w12 is the worst with 44.

## Joins and gate
- Gate: 0 of 54 audio-cut events show Wes on screen (all covered).
- Joins: 58 join sheets in qc/joins. The largest frame differences are all intended b-roll covers (max d=20.9 at 15:07).
- 4:17.9: clean.

## Not fixed
- About 1.5 s of single-frame hand or fingertip flashes remain. Some fingertips in the wide takes are only softened by the bottom fade.
- The wide takes are not stabilized and keep HeyGen's native head motion.
- The split panel and bubble still use the old take, so face size and lighting differ slightly from the wide takes.
- Wide-take chin jut is up from 23 to 41 frames.
- No videoReview has been run yet. The parent agent runs it on the 720p review copy.

## Frames to check in videoReview
- 0:57
- 3:35-3:42
- 8:10
- 10:00-10:46
- 13:04-13:26
- 14:21
- 4:15-4:18 (fade fix)
- Any wide-to-bubble dip, for example around 1:00 and 4:35
