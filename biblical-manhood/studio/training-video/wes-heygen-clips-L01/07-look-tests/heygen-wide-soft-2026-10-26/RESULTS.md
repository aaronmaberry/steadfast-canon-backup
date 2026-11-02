# HeyGen wide/soft tests, look A (c48fd478beb311f1ea481869c933d692), 2026-10-26, 7:03–7:35 PM CDT
Credits: 2704 at start, 2669 at end, so **35 used** (cap 40). Breakdown: S1+S2 720p renders = 9. Image generation = 4 per image (3 images = 12). The 3 new photo-avatar looks plus 3 line4 720p renders = about 14 combined; HeyGen debits these with a lag, so I can't split them exactly.

## Failures first
- **Test 1 gate FAILED. Softening the audio does not reduce lips by the required ≥5%.** S1 (de-ess plus transient soften, same speed) made the mouth bigger: p90 .1170 vs V3 .1088 (+7.5%), and 20 frames fell below .85 identity. S2 (S1 plus 6% slower) gave p90 .1070 (−1.7%), max −1.7%, p50 −4.7%. Teeth p50 got worse (1.42 vs 1.36). Its identity was the best of the three (mean .906, 5 frames <.85), but that is within run-to-run noise. **No 1080p render** (it would not measurably help). HeyGen's mouth size is not driven much by consonant energy.
- **3/4-angle waist-up FAILED identity in motion.** The still s12 scored .873, but the video scored mean .797 / min .683, with 38/42 frames <.85. At 720p the face is ~170 px. It also has **no lav mic** (look A has one) and a lighter background strip. **The look was deleted** (4e269671889cd8df45ded8f8c13d8ba8, after the approval card) and its mp4 is kept only as a labeled reject. Seed 11 (still .816) was rejected before it ever became a look.
- **Front mid-torso look: mean passes, min fails.** Video mean .854 / min .775 (gate is min .80), 20/42 frames <.85. Face 182 px at 720p. The background IST logo was re-drawn larger/whiter than in look A, and the framing is mid-torso, not quite waist. **Kept, but flagged** (not deleted: the still itself scores .914–.920, and the dip comes in motion at a small face size). It needs a 1080p check before use.
- **Tight close-up: min marginally fails.** Mean .889 / min .7945, 6/42 frames <.85. Teeth p50 1.48 (worse than any lesson clip). Face 297 px at 720p (just under 300; it would be ~445 px at 1080p). It is a pixel crop of look A, so this is engine drift, not look drift. Look A itself dips to .70 on the lesson clip.
- **By eye:** every new clip shows the same wide grin with teeth at ~3.9 s, which comes from the line4 audio (eval/FACECROPS-all-clips.jpg). The 3/4 clip has eyes-closed frames at 0.2–1.1 s. **Hands come up at the same moments (~2.0 s and ~3.7–3.8 s) in both wide looks.** The gestures look natural (open palms, low, brief; eval/*-bottom-2fps.jpg), but they are audio-driven, not varied: the same audio gives the same gesture timing. The tight look shows no hands.

## Table (ArcFace every 3rd frame vs intro_ref_embedding.npy; gap = inner-lip gap / face width)
| clip | audio | gap p50/p90/max | teeth p50/max | intro mean/min (<.85) | face w | cx | hands | verdict |
|---|---|---|---|---|---|---|---|---|
| V3 ref 720p (prior) | orig 11.3 s | .0809/.1088/.1559 | 1.36/1.60 | .892/.703 (10) | 223 | .49–.51 | none | reference |
| S1 soft 720p d0fe253e… | S1 11.3 s | .0854/.1170/.1668 | 1.36/1.61 | .885/.725 (20) | 223 | .49–.51 | none | FAIL (worse) |
| S2 soft+slow 720p 30d80198… | S2 12.0 s | .0771/.1070/.1533 | 1.42/1.62 | .906/.756 (5) | 223 | .49–.51 | none | FAIL gate (−1.7%) |
| TIGHT line4 87acb3c6… | line4 4.98 s | .0881/.1200/.1660 | 1.48/1.68 | .889/.795 (6) | 297 | .49–.51 | none | marginal |
| FRONT mid-torso line4 24dc7e64… | line4 | .0834/.1276/.1727 | 1.40/1.65 | .854/.775 (20) | 182 | .50–.51 | 2 gestures | marginal |
| 3/4 waist line4 22b991a0… | line4 | .0807/.1291/.1561 | 1.33/1.50 | .797/.683 (38) | 170 | .62 | 2 gestures | REJECT (look deleted) |
Line4 on the old A-low (with motion prompt) for reference: intro .880/.802, gap max .178, teeth p50 1.41.

## Audio
S1 = `deesser=i=0.5:m=0.5:f=0.5, equalizer f=5000 q-width 1 −2.5 dB, acompressor thr −18 dB ratio 3 att 2 ms rel 60 ms, +5.4 dB, alimiter 0.89`. S2 = S1 + `atempo=0.94` (no pitch change).
Original −16.9 LUFS, peak −1.8 dBFS. S1/S2 −17.6 LUFS (within 1.5 dB), peak −4.5. The 3–8 kHz band share dropped −13.2 → −15.4/−15.6 dB. RMS crest (p99/p50) dropped 4.6 → 2.4. Whisper transcripts of S1/S2 = same words. Spectra: eval/SPECTRA-orig-S1-S2.png. HeyGen audio assets: S1 ae73d3f768b44f839e9a5d754eefb327, S2 6ffe46d6a3b54df4936e6546373ba99d, line4 40f4f3cb1edc4fd98e54fcd8e6155679.
As a voice, S2 is a softer, slightly slower delivery and could still be used for listening comfort. It just doesn't calm the lips.

## How the new looks were made (Test 2)
- HeyGen has no outpaint, angle or pose tool for an existing look. Look templates/packs restyle the clothes and background (rejected unused). The route that works is **create_image_generation (heygen-image-1, identity_remix)**: identity = look A still, plus one composition reference I built locally:
  - REF-34-waist.png: Wes cut from the stage clip 013 (3/4, hand out) pasted on look A's background with the subject removed.
  - REF-front-waist.png: look A shrunk 0.62 with the shirt extended.
  - Then create_photo_avatar into group c48fd478….
- Tight = local crop of look A (1002×564 → 1392×783 Lanczos). No regeneration, face pixels unchanged except for resampling. Still identity .946.
- Render settings for all: Avatar IV (engine omitted), 720p, 16:9, expressiveness "low", no motionPrompt.
- **Surviving new look ids:** TIGHT 7e9b0596ff733f57b37ac453abfdbb00, FRONT mid-torso 0ba38971461eb514ff52f441cba17a59. Deleted: 4e269671889cd8df45ded8f8c13d8ba8. Look A is untouched.

## Answer on waist-up
HeyGen can make a wider shot of the same Wes. Front mid-torso holds identity on average. The real waist-up 3/4 drifted. It cannot make a different camera angle that holds identity at this face size. Alternatives (not spent on):
1. Re-check the FRONT look at 1080p (~4 credits). The face would be ~270 px, which may lift the min above .80.
2. More identity_remix seeds with several identity images (look A plus the tight crop) and a front-only reference (4 credits/image).
3. Use real stage footage of Wes (like clip 013) for wide/3/4 B-roll, where the face doesn't need lip-sync.
4. Composite: keep the talking face from look A's video and place it over a wider plate. Face pixels stay untouched, but it risks seams.
5. Get variety without regeneration: cut between the look A 1080p render and its own punch-in/out crops in the edit.

## Files
- mp4s: S1-soft-V3-720p, S2-soft-slow94-V3-720p, TIGHT/FRONTWAIST/34WAIST(REJECT)-line4-720p, ref-V3 copy.
- SIDE-BY-SIDE-V3-left-vs-S2-right.mp4 and …-vs-S1-right.mp4: each side uses its own audio; S's audio is the one heard; labeled.
- STILL-STACK-original-vs-new-looks.jpg.
- eval/: *-mouth.jpg (6 fps), *-8frames.jpg, *-gates.json, *-bottom-2fps.jpg (hands), FACECROPS-all-clips.jpg, FACECROPS-34.jpg, spectra.
- audio/, looks/ (refs, generated stills), scripts/ (abgates.py: the v15 embedding was moved by the other worker, so the v15_* fields now equal intro).

## Follow-up 7:25 PM CDT: FRONT mid-torso 0ba38971… at 1080p, original lesson audio (video c2526a2c9f4919b8e6fca4580d1e579d)
Settings: engine omitted (Avatar IV), 1080p, 16:9, expressiveness low, no motionPrompt, audio asset dc58acc3eb8348f79f81373cd2a03f1b (original 11.3 s). Credits 2669 → 2665 = **4** (run total 39).
- **Identity FAILS:** mean .858, min .731, **46 of 95** sampled frames <.85, spread across the clip (0–0.8, 1.9–2.4, 3.7–5.6, 7.1–7.4, 8.6–10.3 s). Look A 1080p on the same audio scored .911 / .766 with 5 frames below. 1080p did not rescue it.
- Face width 265–275 px (FAIL, under 300). cx .497–.508 (PASS).
- Lip gap p50/p90/max .0847/.1182/.1585 (larger than V3 1080p's .1073 p90). Teeth p50 1.21 / max 1.52, 66 of 268 frames >1.35, the best teeth of any clip. No big grin in the sampled frames. Eyes look heavy or half-closed at ~1.6 s and ~9.6 s (8frames).
- **Hands:** 3 gesture windows: a small rise at ~0.6–1.0 s, open palms at ~2.0–2.4 s, and a clear two-hand gesture at ~7.1–7.4 s, plus small twitches at 4.5 and 8.9 s (eval/FRONTWAIST-lesson-1080p-bottom-2fps.jpg). They look natural and low. The ~7.2 s gesture matches where baseline A raised a hand on this same audio, so timing follows the audio. In line4 it was 2 gestures (~2.0 and ~3.8 s).
- **Background vs look A (eval/BG-lookA-vs-FRONT1080.jpg):** the IST logo circle is much bigger and white/bright, where look A's is small and dim. The background is brighter and bluer overall. **Rows of seat/bleacher shapes are visible** behind him at lower left (horizontal light bands, also in the bottom strips). Look A's lower background is near-black. Henley and lav mic are consistent.
- **Verdict: FAIL for the lesson cut** (identity and background consistency). Not deleted, per Aaron's 'don't delete the others'.
