# PREFLIGHT — HeyGen mouth-tone test, look A (2026-10-26, ~6:35 PM CDT)
Look: c48fd478beb311f1ea481869c933d692 'Wes Intro Into Lens' (unchanged). Engine Avatar IV, 16:9, 720p for variants, best -> 1080p.
Audio: audio/L01-lesson-155.40-166.70-11.3s.wav (same as baseline). Credit cap 30 premium; start balance 2724 -> stop if < 2694.
## Already failed with this tool
- HeyGen precision lipsync on existing clips: did nothing.
- expressiveness medium drifted the face on other stills; low added a hallucinated headset mic on other stills.
- low vs medium identical when a motion prompt is set.
## Locked rules
- identity vs eval/intro_ref_embedding.npy, >=0.85 per sampled frame
- mouth visibly moves and closes in pauses; teeth_rel <=1.35, off-white
- no open palms/hands in frame, no chairs, no watch; centered 0.5+-0.03; face width 300+ px at 1080p
- no texture painted afterward; no hallucinations (red dots, flashes, background change)
## Pass/fail gate
PASS if lip-gap amplitude (median/p90/max) and mouth peaks are measurably smaller than baseline (720p vs A-low-lesson.mp4; 1080p vs A-low-lesson-1080p.mp4), mouth still moves and closes in pauses, identity holds, no hands/grin/hallucinations.
## Variants
V1 motion: "subtle understated lip movement, relaxed jaw, small mouth opening, minimal mouth exaggeration, calm low-energy delivery, hands below frame, never raise hands"
V2 motion: "subtle understated lip movement, relaxed jaw, small mouth opening, minimal mouth exaggeration, calm low-energy delivery"
V3 no motion prompt, expressiveness low
V4 motion: "speaks quietly and conversationally, lips barely move, mouth stays nearly closed, soft relaxed jaw, still head, hands out of frame"
- UPDATE 6:33 PM: hands in frame and lav mic acceptable if consistent; hands reported factually, not a fail.
