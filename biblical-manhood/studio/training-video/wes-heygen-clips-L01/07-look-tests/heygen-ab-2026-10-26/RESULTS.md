# HeyGen A/B photo-avatar test — intro look (A) vs new v15 look (B). 2026-10-26, 6:00–6:25 PM CDT
**OVERALL: no clip passes every locked gate. All kept because Aaron asked to see both. True failures first:**
- **A (intro look), all clips: FAIL identity vs v15** (mean 0.60, min 0.41; every sampled frame is below 0.85). vs the intro-look reference it scores mean 0.88–0.90 but min 0.76–0.80 (10–17 frames below 0.85), so even against its own reference it drifts on some frames. **FAIL hands**: hands/fingers come up into frame bottom in several frames (eval/A-*-dense.jpg, frames around 1.4–1.6 s and 3.2 s in line4, ~2 s and ~8 s in the lesson clip) even though the prompt said "hands not visible". **FAIL mic**: a lav mic clipped on the shirt; it is in the source still, not hallucinated, but it breaks the no-mic rule. **FAIL face width at 720p** (~223 px); 1080p gives 322–335 px (PASS). **Wide open grin** at ~1.4 s in line4 (eval/A-low-line4-hand-1.4s.jpg). Background shows the "IST" sign (from the source still). It does not change.
- **B (v15 look), all clips: identity PASSES on the mean but FAILS the per-frame min**: v15 mean 0.905–0.914, min 0.76–0.81, 2–5 of 42–95 sampled frames below 0.85 (the dips are on wide-open vowels). **FAIL face width at 720p** (~277 px); 1080p gives 404–414 px (PASS). **Input artifact (mine, not HeyGen's)**: the square master was padded to 16:9 with edge-replicate plus blur, which leaves a grey/brown horizontal band in the lower-left and lower-right corners. It stays static and is visible in every B frame. A cleaner pad, or a native 16:9 master, would fix it. No hands, mic, props, flashes or background change seen.
- **Both, teeth: FAIL per frame**. Medians are 1.27–1.41 (A line4 median 1.41 fails, the others are borderline-pass), max 1.55–1.67, and 30–45 % of frames are over 1.35. Teeth read bright off-white, not chalk white.
- **Expressiveness low vs medium made no visible difference.** A line4 low and med came back byte-identical (same md5). A lesson and both B pairs differ only by encode noise; contact sheets and metrics match. HeyGen seems to ignore the setting when a motionPrompt is given (or caches it), so low/med is redundant here.
- Mouth: visibly opens and closes with speech in both looks and closes in the pauses (B 1080p mouth sheet: closed at 0–0.5 s, 7.9–8.4 s and 9.1–9.6 s, which match the pauses before "Go on" and "nobody's"). Gap-to-audio-RMS correlation is 0.71–0.76 at best lag in both. Best lag is −3 frames in every clip, so the mouth may lead the audio by ~0.12 s, or it is a measurement offset. It is the same for A and B either way, so check by ear. Peak count: A 15, B 12–13 mouth peaks vs 38 audio onsets (lesson); 6 vs 24 (line4). That is word-level motion, not syllable-level.
- None of the Oct-22 hallucinations appeared (no headset mic, no background change, no grin-drift on B).

## Inputs (identical for A and B)
- Audio 1: audio/L01-line4-tightpad-4.98s.wav ("A whole room full of guys just checking it out with a name tag on").
- Audio 2: audio/L01-lesson-155.40-166.70-11.3s.wav, cut from private/lessons/lesson-01.mp3 at 155.40–166.70 s with a 0.15 s fade-out: "Before we get into it, let me see a show of hands. How many of you told somebody you were just coming to check it out? Go on, nobody's writing it down." Voice only.
- Engine Avatar IV, aspect 16:9, motionPrompt "calm man speaking directly to camera, small natural head movement, hands not visible, no props, no microphone, background unchanged", no captions, no background override.
- A look: c48fd478beb311f1ea481869c933d692 (existing, 1392x752).
- **B look: c1b50ca0d128fca7bcbef67d5796a8c1 "Wes v15 Master Into Lens 16x9"** (new photo avatar; training completed in <1 min). Input inputs/B-input-v15-1920x1080.png. **Exact crop:** none. The whole 2048x2048 v15 master was resized (INTER_AREA) to 1080x1080 and placed at x=420..1499 of a 1920x1080 canvas. The left/right 420 px pads are BORDER_REPLICATE plus Gaussian sigma 25 (pad pixels only). The face pixels are unchanged (max diff 0 vs the resized master), and Wes's center x is 0.500. A true 16:9 crop of the square master would cut either the chin or the hairline, which is why it is padded. Upload asset a9963991079c4dad996a6dc619c1a92e.

## Table (ArcFace on every 3rd frame; intro ref = mean embedding of 161 intro-video frames; intro ref vs v15 = 0.643)
| file | look | res | expr | audio | v15 mean/min (<.85) | intro-ref mean/min (<.85) | face w px | cx | mouth peaks / onsets, corr | teeth p50/max (>1.35) | hallucinations / by eye |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-low-line4.mp4 | A | 720p | low | line4 | .598/.498 (42/42) | .880/.802 (7) | 217–223 FAIL | .495–.505 | 6/24, .76 | 1.41/1.59 (59/87) FAIL | hands enter frame, wide grin 1.4 s, lav mic |
| A-med-line4.mp4 | A | 720p | med | line4 | identical file to A-low-line4 (same md5) | | | | | | |
| A-low-lesson.mp4 | A | 720p | low | lesson | .602/.414 (95/95) | .885/.761 (17) | 215–223 FAIL | .493–.503 | 15/38, .74 | 1.34/1.58 (88/187) | hands at bottom ~2 s, ~8 s; lav mic |
| A-med-lesson.mp4 | A | 720p | med | lesson | .602/.419 (95/95) | .886/.764 (17) | 215–223 FAIL | .493–.503 | 15/38, .75 | 1.34/1.59 (89/187) | same as low |
| A-low-lesson-1080p.mp4 | A | 1080p | low | lesson | .602/.433 (95/95) | .903/.778 (10) | 322–334 PASS | .493–.503 | 15/38, .74 | 1.33/1.60 (112/243) | same as 720p |
| B-low-line4.mp4 | B | 720p | low | line4 | .905/.814 (5/42) | .623/.556 | 272–278 FAIL | .493–.506 | 6/24, .71 | 1.33/1.66 (41/94) | pad band (input); otherwise clean |
| B-med-line4.mp4 | B | 720p | med | line4 | .905/.815 (5/42) | .621/.558 | 272–278 FAIL | .494–.506 | 6/24, .71 | 1.33/1.67 (44/94) | same as low |
| B-low-lesson.mp4 | B | 720p | low | lesson | .910/.757 (3/95) | .624/.572 | 270–277 FAIL | .490–.515 | 12/38, .72 | 1.31/1.59 (90/198) | clean, no hands |
| B-med-lesson.mp4 | B | 720p | med | lesson | .909/.759 (4/95) | .623/.571 | 269–277 FAIL | .490–.515 | 13/38, .72 | 1.30/1.57 (91/200) | same as low |
| B-low-lesson-1080p.mp4 | B | 1080p | low | lesson | .914/.769 (2/95) | .631/.584 | 404–414 PASS | .490–.515 | 12/38, .73 | 1.27/1.55 (75/236) | clean, no hands |
Centering passes everywhere (0.5±0.03; B lesson cx_max .515 still within). Neither look has missing faces, flashes, red dots or lighting jumps in the contact sheets I viewed (eval/*-dense.jpg, *-8frames.jpg, *-mouth.jpg).

## Credits
Start 2761 premium, after 2724 → **37 credits used total** (photo-avatar creation + 8 × 720p + 2 × 1080p). The API gives no per-video cost; 2761→2754 after the first 4 launches, →2732 after all 8 at 720p, →2724 after the 2 at 1080p (1080p ≈ 8 credits for 22.6 s). Cap 80 was not hit. No payment prompts, no other vendor, no fal, no xAI, no fal_key_steadfast.

## Deliverables
- SIDE-BY-SIDE-A-vs-B.mp4 (lesson line, A-low left | B-low right, 720p native each, labels in an 80 px top strip only, audio from A) and SIDE-BY-SIDE-A-vs-B-line4.mp4.
- CONTACT-A-vs-B-8frames-plus-v15-and-real-refs.jpg (8 face crops each from the 1080p clips, plus the v15 master, the intro look and the locked real-refs contact).
- STILL-STACK-v15-intro-A-B.jpg (v15 master | intro-look face | A frame | B frame, same scale).
- eval/: per-clip gates JSON (per frame), 8frames, dense, mouth sheets, mouth-sync.json, intro_ref_embedding.npy. scripts/abgates.py.
- HeyGen video ids: A-low-line4 7108895a61fb99ed036e4885bb45b513, A-med-line4 fbac96dad888efd44374237f52cb68a0, A-low-lesson c52acb2b2f54db0f74f3d2fd784af88d, A-med-lesson 396734945099017e85033a9c2f71e386, B-low-line4 a9872c80b0cb8d304bf4bc44607ec284, B-med-line4 a80ac315da60a0490ed77b041d39f7f1, B-low-lesson d97a3082e65bf07d28a3f9df50e0552d, B-med-lesson 559639edae5bd35794c6f87f63996085, A-1080p 30f86f55f76c47d3649ee19e7c886aab, B-1080p c7adc02c0edaeeab475aca786f1962b0.

## Read
B is the v15 Wes (0.91 mean) with HeyGen's motion quality, and it has no hands or mic. Its weaknesses are a few frames dipping to 0.76–0.81 on big vowels, and my padding band. A is the "best ever" Wes, but it is a different man from v15 (0.60), it brings hands into frame, and it carries the lav mic. If B is chosen: re-make the B input with a clean dark pad (or a native 16:9 v15 frame), render at 1080p, and drop the expressiveness setting.
