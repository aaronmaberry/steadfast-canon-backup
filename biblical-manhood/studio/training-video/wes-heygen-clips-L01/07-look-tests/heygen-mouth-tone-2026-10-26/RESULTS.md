# HeyGen mouth-tone test, look A (c48fd478beb311f1ea481869c933d692), 2026-10-26, 6:35–7:10 PM CDT
## Failures / limits first
- **The reduction is small, not dramatic.** Best = V3 (no motion prompt, expressiveness low). At 1080p, lip-gap p90 is −13%, max −12.5%, median −5%, frame-to-frame gap spread (std) −19%, and wide-open frames (gap>0.12) drop from 11% to 7%. In the mouth contact sheets (eval/cmp-mouth-BASE-vs-V3-1080p.jpg) the visemes and their timing are the same; V3's big opens are only somewhat smaller. The biggest "O" (~7.3 s) and the teeth-baring frame (~6.6 s) are still there. Watching it side by side, it is milder but still the same style of articulation.
- **Mouth-peak count was not reduced in any meaningful way.** With a fixed prominence of 0.015 it goes 20→17 at 1080p (19→18 at 720p). Only peak height drops (0.123→0.117).
- **Teeth gate still FAILS per frame on every clip.** V3 1080p median 1.28 (better than base 1.33) but max 1.63, with 100/249 frames >1.35. V1/V2/V4 medians 1.36–1.38 (worse than base).
- **Identity per-frame min <0.85 on every clip**, the same as baseline. V3 1080p mean 0.911 / min 0.766, 5 of 95 sampled frames <0.85 (baseline 1080p 0.903 / 0.778, 10 frames). So identity is equal or slightly better, not worse.
- **Face width at 720p fails (~223 px), as expected.** V3 1080p is 325–335 px (PASS).
- **By eye, V3's skin reads a touch brighter/warmer than baseline** in the side-by-side (eval/sbs-3.2s.jpg). This is slight. Check it against other shots for consistency.
- **Prompt wording (V1, V2, V4) barely mattered**: −5…−7% on p90, and V4 "lips barely move" was no better than V1/V2. Any motion prompt seems to override the subtlety wording.
- A 1080p launch with an explicit engine={avatar_iv} returned HTTP 500 twice. Both times no video was created and no credits were taken (checked with lookup_videos). It worked with the engine field omitted (default is Avatar IV anyway).

## Table (ArcFace on every 3rd frame vs eval/intro_ref_embedding.npy; gap = inner-lip gap / face width)
| clip | res | lip-gap p50 / p90 / max | std | frames gap>.12 | peaks (prom .015) / mean peak h | teeth p50 / max (>1.35) | intro-ref mean / min (<.85) | face w | cx | hands (skin-in-bottom-centre heuristic + sheet) | hallucinations | credits |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BASE A-low-lesson | 720p | .0881 / .1246 / .1745 | .0273 | 15% | 19 / .129 | 1.34 / 1.58 (88/187) | .885 / .761 (17) | 215–223 | .493–.503 | 15 frames: ~0.8, 2.0–2.4, 5.8, 7.2 s (hand clearly up at ~7 s) | none | (prior) |
| V1 subtle + hands below | 720p | .0807 / .1192 / .1646 | .0261 | 9% | 19 / .123 | 1.36 / 1.63 (78/143) | .899 / .768 (11) | 217–223 | .489–.504 | 4 frames at 7.2–7.3 s | none | 4 |
| V2 subtle, no hands text | 720p | .0798 / .1163 / .1612 | .0259 | 8% | 17 / .125 | 1.37 / 1.62 (85/151) | .900 / .730 (10) | 215–223 | .489–.503 | 0 | none | 4 |
| **V3 no prompt, expr low** | 720p | .0809 / **.1088** / **.1559** | **.0212** | **4%** | 18 / **.114** | 1.36 / 1.60 (86/164) | .892 / .703 (10) | 216–223 | .493–.505 | 0 | none | 4 |
| V4 "lips barely move" | 720p | .0812 / .1175 / .1611 | .0257 | 8% | 18 / .125 | 1.38 / 1.61 (91/148) | .895 / .749 (15) | 215–223 | .490–.504 | 0 | none | 4 |
| BASE A-low-lesson-1080p | 1080p | .0851 / .1236 / .1710 | .0259 | 11% | 20 / .123 | 1.33 / 1.60 (112/243) | .903 / .778 (10) | 322–334 | .493–.503 | as 720p base | none | (prior) |
| **V3-noprompt-low-1080p** | 1080p | .0805 / **.1073** / **.1496** | **.0211** | **7%** | 17 / **.117** | **1.28** / 1.63 (100/249) | **.911** / .766 (5) | 325–335 | .491–.505 | 0 (eval/V3-1080p-bottom-2fps.jpg) | none (no mic change, no flashes, background same) | 4 |
Credits: start 2724 → 2708 after 4×720p → 2704 after 1080p = **20 used** (cap 30). The 720p batch cost 16 for 4, so about 4 each, and the 1080p cost 4.
Mouth still closes in the pauses in V3 (silent-frame mean gap .075 vs voiced .088). Contact sheet rows at ~9–10 s show closed lips.
Hands: hands in frame are no longer a fail per Aaron. The heuristic is crude. Baseline shows a hand rising at ~7 s. V3 showed none across all 283 frames at both resolutions.

## Best settings
Avatar IV (default engine, omit the engine field), look c48fd478beb311f1ea481869c933d692, aspect 16:9, **no motionPrompt**, **expressiveness "low"**, audio asset dc58acc3eb8348f79f81373cd2a03f1b. HeyGen ids: V1 f68f0a2bf698787484a76c68fbfadb6e, V2 2c421efebf442c9cd9093fbab0deda14, V3 2874ecb6827b0ce12a48cf9fa099e14d, V4 130514a2d36400983de86eab2f86d437, V3-1080p 41d283bcb40fde6bc2b317fd0c44e904.

## Other free levers (not tried)
- Audio: a slightly softer/lower-level take, or gentle de-essing / compressing plosives (p, b, t) and a −2 to −3 dB transient soften, since the engine scales the mouth with energy. Slowing the delivery 5–8% with no pitch change gives fewer, smaller opens.
- Post: none allowed on the face (no texture painted afterward). A very slight mouth-region temporal smoothing would count as editing, so it is not proposed.
- HeyGen: Avatar V engine (needs a reference look in the group; unknown); test the same audio with expressiveness low on line4 to confirm the effect is consistent.

## Files
V1–V4 720p mp4s, V3-noprompt-low-1080p.mp4, SIDE-BY-SIDE-baseline-vs-best.mp4 (1080p baseline left, V3 1080p right, baseline audio, labels in the top strip only), baseline/ (copies of the prior clips), eval/ (gates JSON, 8frames, 6 fps mouth sheets, bottom-strip hand sheets, cmp-mouth-*), scripts/abgates.py (adapted: new out dir, gap p50/p90, 6 fps), scripts/compare.py.
