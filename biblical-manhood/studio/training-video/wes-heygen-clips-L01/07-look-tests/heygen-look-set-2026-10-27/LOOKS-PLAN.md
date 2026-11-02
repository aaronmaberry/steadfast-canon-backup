# HeyGen look set for Wes, 2026-10-27 (CDT)
Request (Aaron, 7:46 AM CDT): give HeyGen different starting images with different angles, plus torso shots.
Identity = ArcFace cosine vs INTRO-LOOK-A intro_ref_embedding.npy (insightface buffalo_l, /workspace/cvenv). Still gate is 0.88. Max zoom is the v5 width (~335 px face at 1080p).
Training-locked files were read only. Every output here is a new file.

## Bottom line
I scored 133 stills (the 115-image Wes bank, plates P01-P08 + facefix, walk plates, stage-batch swap, studio proof). **Only 2 stills reach 0.88: 70-wes-cam-medium (0.881) and 71-wes-cam-close (0.888).** Both are front-facing. Every 3/4, profile, low-angle and hands still scores 0.65-0.72. The plates score about 0.62 and 77-wes-medium-wide (wide, hands low) scores 0.81, so all of them are rejected.
This means **no approved still gives a different camera angle or a torso-with-hands framing at look A identity.** The set below only adds framing variety: a medium-wide, two off-centre mediums, and an MCU.

## Starting images (1920x1080, crop/resize/edge-pad only, nothing generative)
| file | angle | width | face px @1080 | identity | gate | chairs | hands | source |
|---|---|---|---|---|---|---|---|---|
| L1-front-medwide-torso-centre.png | front | medium-wide (chest-up torso, no hands) | 235 | 0.88 | PASS | none seen (faint dark stage shapes lower-left, not seats) | no hands in frame | training-locked/70-wes-cam-medium.jpg |
| L2-front-medium-right-third.png | front, framed right third | medium (upper torso) | 267 | 0.8723 | FAIL <0.88 (rejected) | none seen (faint dark stage shapes lower-left, not seats) | no hands in frame | training-locked/70-wes-cam-medium.jpg |
| L3-front-medium-left-third.png | front, framed left third | medium (upper torso) | 270 | 0.8781 | FAIL <0.88 (rejected) | none seen (faint dark stage shapes lower-left, not seats) | no hands in frame | training-locked/70-wes-cam-medium.jpg |
| L4-front-slight-left-turn-MCU.png | front / slight turn, off-centre right | MCU (v5 width) | 321 | 0.8981 | PASS | none seen (faint dark stage shapes lower-left, not seats) | no hands in frame | training-locked/71-wes-cam-close.jpg |

L4: 71 is resized to 1080p and scaled to 0.965 so the face is 321 px (under v5). The 3.5% border is edge-replicate plus blur, with the face pixels resampled only. L2/L3 are crops of 70 upscaled about 1.6x, and the softness drops their identity below 0.88. They are kept only so you can see them and are **not proposed as looks.**

## How each is meant to be used in the edit
- **L1 front medium-wide (torso, chest-up):** the wide establishing or "reset" shot between look A MCU lines. It is the widest framing that passes, but its face is only 235 px. The earlier FRONT mid-torso look at about 270 px dropped to mean 0.858 in motion (heygen-wide-soft RESULTS), so L1 is **high risk** in motion.
- **L4 MCU, framed right of centre:** the alternate punch-in or 3/4-ish reaction shot to cut against look A (which is centred). It is the same width class as v5, never tighter, and it is the most likely to pass.
- L2/L3 (rejected): would have been left-third and right-third mediums for over-shoulder graphics space.
- Look A's own render plus its punch-out crops in the edit remains the safest variety.

## Background note
Images 70/71 are on the dark stage with the blue screen, the same set as the stage plates. Look A is the IST-logo background. Cutting between them reads as a set change, so use them as a separate "stage" segment.

## HeyGen look creation cost: NOT free, so no looks were created
- HeyGen docs: Photo Avatar creation is **$1.00 per call** (self-serve API) or **1 credit per call** (credit plans) (developers.heygen.com/docs/pricing, /docs/enterprise-pricing). HeyGen's blog says a *new* photo-avatar training costs 60 credits on paid web plans and a generated look costs 1 credit.
- Account history: the 2026-10-26 run made 3 looks plus 3 short renders for about 14 credits combined, which fits roughly 1 credit per look added to the existing group.
- **Expected cost: about 1 credit per look, so 2 credits for L1 and L4 (worst case if billed as new training: 60 each).** Waiting for Aaron's yes.
- Names if approved: Wes-LookA-angle-front-medwide (L1) and Wes-LookA-angle-front-right-MCU (L4), with avatarGroupId c48fd478beb311f1ea481869c933d692.
- Look ids created: **none**.

## Near-miss stills (rejected, <0.88)
| still | identity | face px @1080 |
|---|---|---|
| 81-wes-close-smile.jpg | 0.8175 | 337 |
| 77-wes-medium-wide.jpg | 0.8115 | 142 |
| 76-wes-point-room.jpg | 0.752 | 183 |
| 87-wes-wu-three-quarter-right-gesture.jpg | 0.7178 | 203 |
| 73-wes-side-close.jpg | 0.7158 | 323 |
| 88-wes-wu-high-angle-both-hands.jpg | 0.7144 | 231 |
| 106-wes-wu-low-angle-palm-out.jpg | 0.7062 | 217 |
| 95-wes-wu-three-quarter-right-open-palms.jpg | 0.7047 | 213 |
| 79-wes-both-hands.jpg | 0.701 | 187 |
| 110-wes-wu-smile-three-quarter-right.jpg | 0.6958 | 210 |
| 96-wes-wu-profile-right-still.jpg | 0.6919 | 204 |
| 85-wes-wu-close-profile-right-hand-chest.jpg | 0.686 | 233 |
| 75-wes-walk.jpg | 0.6843 | 138 |
| 105-wes-wu-walk-profile-right.jpg | 0.6764 | 177 |

## Proposed test (NOT run; needs Aaron's yes)
- Create 2 looks (L1, L4), about 1 credit each, so about 2.
- Make one ~6 s clip per look: Avatar IV (engine omitted), 1080p, 16:9, expressiveness low, no motionPrompt, from a 6 s cut of the existing L01 audio asset. About 2.1 credits each at 21.2 credits/min, so about 4.2.
- **Total: about 6.2 credits** (balance 2,539 before the pending intro v6 render). Proposed cap 10.

## PREFLIGHT (pre-generation-preflight)
1. **History:** the 3/4 waist look failed in motion (still 0.873, video mean 0.797, deleted). The FRONT mid-torso look at 182-270 px failed (mean 0.854-0.858). The TIGHT crop was marginal and is now too tight under the v5 rule. Look A 1080p scores 0.911 mean / 0.766 min. What is new: real-photo sources (70/71) instead of generated ones. No 3/4 route is proposed because none passes as a still.
2. **Locked rules:** look A identity, average ≥0.90 with no frame <0.75. Max zoom is v5 (L4 at 321 px is OK). No seats (none seen). walksteadfast palette (dark navy/charcoal stage, no new colours). Hands natural (none in frame). Nothing is reused. No paid image generation. Training-locked files are untouched.
3. **Framing:** L4 is 321 px, OK. L1 is 235 px, below the 300 px guidance and known to cause drift, so it is flagged as likely to fail. It is still worth 2 credits only because it is the only passing torso framing.
4. **Budget:** about 6.2 credits, cap 10, needs Aaron's explicit yes.
5. **Gates:** ArcFace on every frame vs intro_ref (mean ≥0.90, min ≥0.75), measured mouth motion per frame plus a mouth contact sheet viewed directly, face width ≤335, centering as framed, a check for chairs and hands by eye, then an independent review.
6. **Failures dropped:** a failing clip is labeled and the look is left in place for Aaron to decide. Nothing is deleted without approval.
7. **Handoff:** paste this checklist into any worker brief.

## Honest gaps and what it would take
- No approved still has a 3/4, profile, low angle, or torso-with-hands framing at ≥0.88. Real angle variety needs one of these:
  (a) heygen-image-1 identity_remix with look A as identity and an approved bank still (e.g. 87 3/4-right gesture, 83 3/4-left hands low, 77 wide hands low) as the composition reference. That is about 4 credits per image, plus about 1 per look and about 2.1 per test. The 2026-10-26 3/4 attempt failed in motion, so expect several tries (roughly 20-30 credits for 3 angles).
  (b) A local free face swap (inswapper) onto bank stills. The model is not installed here, and it is an identity edit, so it needs Aaron's OK.
  (c) Use real stage/walk footage as non-lip-sync B-roll for the wide and angle shots, with look A carrying the speaking lines. This is the cheapest option and has already been proven.
- Outpainting L4 or 70 for hands is not possible with free tools without making things up. Any generative outpaint is a paid edit and needs approval (heygen-image about 4 credits/image).

---
# RESULTS: approved test run (Aaron 7:56 AM CDT, cap 35). Run 8:00 to 8:40 AM CDT
**Credits: balance 2494 → 2460 = 34 spent (cap 35).** The intro v6 render had already been debited before 2494. Each look costs 1 credit (measured 2468→2467). Three 4K identity_remix images cost about 6.5 each, about 19.5 in total. Four test clips of about 6.4–6.9 s at 1080p cost about 2.2 each. Every spend is booked in spend-ledger.csv. Nothing was retried, because the cap ruled out retries.

## Looks created (group c48fd478beb311f1ea481869c933d692; look A untouched; nothing deleted)
| look | id | source image |
|---|---|---|
| Wes-LookA-angle-front-medwide (L1) | 455a3a260420291e8bbf921d9a402bc1 | L1-front-medwide-torso-centre.png |
| Wes-LookA-angle-front-right-MCU (L4) | 436759651d0ee18a330c60304971d984 | L4-front-slight-left-turn-MCU.png |
| Wes-LookA-angle-front-wide-hands (G3) | adc9cb8ca51c5dfc3a862248f3571ef9 | gen/G3-wide-hands-raw.png |
| Wes-LookA-angle-34right-medium (G2) | d7ae986f7eba3684cd7d98508907488d | gen/G2-34R-gesture-raw.png |

## Generated stills (heygen-image-1 identity_remix; identity = look A source plus V3 still; pose ref = bank still)
| still | pose ref | identity | face px | result |
|---|---|---|---|---|
| G1-34L-hands-low | 83 (3/4 L, hands low) | 0.940 | 214 | The model turned it **frontal** and the hands are cut at the frame edge, so it is not a new angle. No look was made (saved credits) |
| G2-34R-gesture | 87 (3/4 R gesture) | 0.892 | 282 | A slight 3/4 R head turn with no hands in the still. Look made |
| G3-wide-hands | 77 (wide, hands low) | 0.925 | 140 | Wide waist-up, torso and hands, hands look natural and relaxed. **A ring is visible on one hand (new prop, check)**. Look made |
Backgrounds are the dark stage with blue screen, as in the approved stage plates, not look A's IST logo. No chairs or seats in any still.

## Test clips (Avatar IV, 1080p, 16:9, expressiveness low, no motionPrompt; audio L01-C001 6.4 s / L01-C013 6.9 s). ArcFace on every frame vs intro_ref
| clip | video id | mean | min | frames <.85 | face px | hands/eye check | verdict |
|---|---|---|---|---|---|---|---|
| clips/TEST-L1-front-medwide-8ad32a2f.mp4 | 8ad32a2f0adf45442006c04567e4d35c | 0.849 | 0.749 | 59/161 | 232-244 | no hands; mouth moves | **FAIL** (mean, min) |
| clips/TEST-L4-front-right-MCU-5022449f.mp4 | 5022449f717ef68af2f4427f792eae55 | **0.880** | 0.813 | 22/174 | 316-333 | eyes closed at 0.0 s, big "oh" at 5.9 s | **FAIL mean** (min passes; closest) |
| clips/TEST-G2-34right-medium-982011f2.mp4 | 982011f25e2fcbc4b80ebaa50f067911 | 0.865 | 0.802 | 46/174 | 274-289 | small hand gesture rises into frame at 0 s, natural | **FAIL mean** |
| clips/TEST-G3-front-wide-hands-d283cd8e.mp4 | d283cd8e93de50b6e262873669206459 | 0.857 | 0.735 | 56/161 | 138-146 | natural two-hand gesture at ~4.6 s, hands at sides otherwise | **FAIL** (mean, min) |
Reference: look A at 1080p scores 0.911 / 0.766. No red specks and no missing faces. No chairs seen in the frame sheets. Sheets: qa/*-8frames.jpg, qa/*-mouth-sheet.jpg, CONTACT-SHEET-TESTS.jpg, CONTACT-SHEET-GENERATED.jpg. Per-frame data: qa/*-perframe.json, qa/SUMMARY.txt.

## Read
- **No new look reaches the 0.90 average.** Identity drops in motion as the face gets smaller: 321 px gives 0.880, 282 px 0.865, 235 px 0.849, 140 px 0.857 (at 140 px ArcFace itself is less reliable). This is the same pattern as 2026-10-26.
- L4 is closest. It could be used as a short reaction or punch-in only if Aaron accepts about 0.88. G3 is the only clip that really gives torso and natural hands, but it fails the min (0.735).
- identity_remix holds identity on stills (0.89–0.94) but pulls poses toward frontal. A true 3/4 or profile did not come out.
- Next options (not spent): (1) cut wide/angle shots as non-lip-sync B-roll from G3/G2 clips or real stage footage, with look A carrying the speaking lines; (2) composite look A's talking face region over the G3 wide plate (free, local, seam risk); (3) accept the 0.88 gate for L4/G2 cutaways under 3 s.

---
# LOCAL FIX + paid G3 test (Aaron 8:35 and 9:16 AM CDT), run 8:36–9:40 AM CDT
Only free local tools, except the one approved G3 clip. **Paid: 3 credits (2460 → 2457), cap 3.** Run total 37 credits (34 + 3). Booked in spend-ledger.csv.
Tools: insightface inswapper_128 (downloaded free from HuggingFace), source identity = look A intro_ref mean embedding. GFPGAN was not installed (venv pip is broken), so there is no face enhancer and no painted texture.

| clip | method | len | mean | min | <.85 | longest dip | face px | eye check | use |
|---|---|---|---|---|---|---|---|---|---|
| local-fix/L4-swap.mp4 | inswapper on L4 HeyGen clip (line C013) | 6.9 s | **0.922** | 0.904 | 0 | 0 | 310–328 | face slightly softer and smoother than the raw clip, no visible seam or flicker (arc jitter p95 .007); mouth motion about 17% lower than raw | **speaking shot OK** (MCU, right-framed) |
| local-fix/G2-swap.mp4 | inswapper on G2 clip (C013) | 6.9 s | **0.927** | 0.906 | 0 | 0 | 268–285 | the 128 px swap scaled to about 280 px looks **noticeably soft** on close view; small natural hand gesture at 0 s | **speaking shot, usable short** (3/4-ish medium); soft face is the honest caveat |
| local-fix/G3-swap-noring.mp4 | inswapper on G3 (C001) plus a 1.04x bottom crop to drop the ring | 6.4 s | **0.922** | 0.887 | 0 | 0 | ~150 | no ring in frame; **purple/white speckle on both hands during the 4.6 s gesture** | speaking wide only if 4.4–4.9 s is cut out; otherwise silent cutaway |
| paid-g3/TEST-G3-wide-L01-1726-182d6e6f.mp4 | HeyGen raw (video 182d6e6fe61ee11d451f5ad60244a23c), L01 17.26–23.77 "Glad you're back…grabbed a chair near the back" | 6.5 s | 0.831 | 0.669 | 94 | 48 frames | 137–145 | **ring visible at 2.1–2.6 s** (hand mid-frame, can't be cropped); hand looks rubbery/blurred at 3.6 s and 6.2 s | **FAIL**; avoid (ring) |
| paid-g3/G3-L01-1726-swap.mp4 | inswapper on the paid clip | 6.5 s | **0.925** | 0.909 | 0 | 0 | 139–145 | identity fixed, **ring still visible 2.1–2.6 s** | identity passes, but avoid per the ring rule |
| local-fix/COMP-G3wide-G003.mp4 | look A G003 face composited onto the G3 body (affine plus LAB match, feathered mask) | 10.1 s | 0.824 | 0.605 | 152 | 44 frames | 139–157 | looks plausible by eye, but identity collapses once look A is shrunk to 140 px | FAIL |
| local-fix/COMP-G2-34R-G002.mp4 | composite onto the G2 body | 9.4 s | 0.800 | 0.611 | 155 | — | 271–289 | frontal face on a 3/4 head, misfit | FAIL |

Caveat on the swap scores: inswapper pushes the face toward the same ArcFace identity space the gate measures, so the 0.92s partly reflect the metric itself. A by-eye check against look A is required: SIDE-BY-SIDE-lookA-vs-*.mp4. By eye, the swapped faces read as the same Wes as look A, but softer.
Sheets: CONTACT-SHEET-LOCALFIX.jpg, paid-g3/RING-CHECK-strip.jpg, paid-g3/TEST-G3-wide-L01-1726-182d6e6f-8frames.jpg, qa/*-mouth-sheet.jpg, qa/SUMMARY-localfix.txt. Preflight: paid-g3/PREFLIGHT.md.

## Gaps
- **Rolled-up sleeves: not achieved.** Every look (A, L1, L4, G2, G3) wears long sleeves to the wrist. Rolling them up means regenerating the body (a paid image generation plus a new look and test), or a pose reference that already has rolled sleeves.
- **No clip is 8–10 s.** The swap can only rework existing HeyGen clips (6.4–6.9 s). Longer speaking shots need new paid renders, which the swap would then fix for free.
- No true profile or strong 3/4. G2 is a slight turn only.
