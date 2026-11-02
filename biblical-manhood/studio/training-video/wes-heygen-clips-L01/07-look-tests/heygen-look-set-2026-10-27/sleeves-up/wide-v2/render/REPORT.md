# Sleeves-up wide w4: paid test (Aaron approved 10:08 AM CDT, cap 4). Run 10:08–10:30 AM CDT
**Credits: 2412 → 2411 (look) → 2408 (clip) = 4 spent, exactly at cap 4.** Nothing retried.
- New look: **Wes-LookA-sleeves-up-wide (w4)**, id `04d47a1349b5a95f4fc093d5eb26ef16`, group c48fd478beb311f1ea481869c933d692 (look A untouched). Source: ../w4.jpg (1280x720), asset b06219df1e1343f1bc6ac9d500f1525a.
- Clip: video `1cbbb65837094d8374b0d1503d7f1025`, Avatar IV, 1080p 16:9, expressiveness low, no motionPrompt. Audio: existing asset 057cfc41b60f4ce8ad0f2109a6808979 (L01 17.26–23.77, already-rendered locked Wes podcast voice, 6.5 s). No ElevenLabs use.

## Identity (ArcFace per frame vs look A source_still_arcface_embedding, 163 frames)
| mean | min | p10 | frames <0.85 | frames <0.75 | longest dip <0.85 | face px |
|---|---|---|---|---|---|---|
| **0.838** | **0.692** | 0.740 | 98/163 | 19 | 43 frames (1.7 s) | 202–212 |
**Gate (mean ≥0.90, none <0.75, no long dips): FAIL on all three.** The still scored 0.961, but in motion it falls the same way as every other ~140–270 px face (G3 0.831, L1 0.849). Worst stretches are around 3.1–4.2 s and 5.7 s, which is where the mouth opens and the head turns.

## By-eye checks (CONTACT-SHEET.jpg, HANDS-SLEEVES-strip.jpg)
- Hands: five natural fingers per hand in the steady frames. **No ring or speckle seen.** The gestures at about 3.6 s and 6.4 s are motion-blurred and slightly soft/rubbery, as G3 was.
- Sleeves: stay pushed to mid-forearm on both arms for the whole clip.
- Screen/stage: STEADFAST MEN screen is stable, and no warping was seen in the sampled frames. No chairs, audience or podium.
- The face reads as Wes at a glance in the side-by-side, but ArcFace says it drifts.

## Verdict
**FAIL identity.** Use it only as a silent wide cutaway or B-roll, or run a free local inswapper pass, which brought G3/L4/G2 to 0.92 before (soft face at this size). Do not use it as a speaking shot as rendered. The look is kept and nothing was deleted.

Files: TEST-w4-sleeves-wide-L01-1726-1cbbb658.mp4, SIDE-BY-SIDE-lookA-vs-w4.mp4 (left: look A raw v6 intro first 6.5 s, a different line), CONTACT-SHEET.jpg, HANDS-SLEEVES-strip.jpg, perframe.json, qa.py.
