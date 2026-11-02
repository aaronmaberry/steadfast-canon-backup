# L01 "A Quiet Tuesday": audio v2 REPORT (2026-10-29, 9:20 AM CT)
Status: **built. One hard gate is still red: clicks = 6** (v1 had 63). All 6 are word-final consonant releases, not ticks (table below). Per instructions I STOPPED: there was no third full pass and no repair of the master. v1 is untouched in ../job/. Nothing has been published or uploaded, and there was no HeyGen work.

## Deliverable
`v2/delivery/L01-A-Quiet-Tuesday-AUDIO-v2-minus26-LUFS.mp3` (+ .wav). It measures -26.0 LUFS, -8.91 dBTP and 20:34.08. The master is `v2/L01-A-Quiet-Tuesday-v2.wav` (-19.5 LUFS).

## Free fixes (all verified on the source before the paid pass)
1. Pauses: 36 [pause ≥1.2] marks were written to overrides.json and **all were honoured**. The three exercise gaps measure 2.48 / 2.52 / 2.51 s; no long pause is more than 0.25 s short. Atempo stays at 0.86, so speaking pace is unchanged and the file is 25 s longer.
2. Room tone: test 1 showed that the TTS hiss (-71 dB) caused the Voice Changer ticks (16 clicks/min). Every pause run was replaced with the locked intro source's own room tone (-89 dB, from src21b_079.wav). Result: 0 digital zeros, min frame -93.4 dB, noise floor -90.3 dB, and no dead air.
3. Source declick: clickloc +15 dB pass, then a +10 dB pass with broadband dips of 12 dB or less on word-final releases (scripts in v2/). gates.py on the final source (src_v2d) = **0 clicks**. 17 sub-threshold +10 dB spots remain, all in pauses.
4. Dry tail: test 2 measured -59.8 and test 3 -58.5. The full master is **-58.5 (pass)**.
5. Three ~62.7 s Voice Changer tests on the same window (join k07 + 2.5 s exercise pause), gated and chained:

| Test | Clicks | Dry tail |
|---|---|---|
| Test 1 (TTS floor) | 16 | -56.9 |
| Test 2 (intro floor) | 4 | -59.8 |
| Test 3 (+ release softening) | 0 | -58.5 |

The full pass ran only after test 3 passed.

## Gate table vs locked intro (v23)
| Gate | Target | Intro | v1 | **v2** | Result |
|---|---|---|---|---|---|
| Clicks (gates.py) | 0 | 0 | 63 | **6** | **FAIL (hard)**, all at word ends (see below) |
| Cuts into speech | 0 | 0 | 4 dead-air joins | 28 flagged, all in pauses (the -89 dB floor trips the ≤-75 dB rule); 4 overlap aligner word-ends by 20-50 ms, checked: no cuts | pass (detector artefact, documented) |
| Room tone continuous | yes | yes | dips | -93.4 dB min, 0 digital zeros, floor -90.3 | pass |
| Dry tail | ≤-58 | -58.6 | -53.5 | **-58.5** | pass |
| HNR | ≥4.5 | 6.25 | 6.07 | 6.08 | pass |
| Similarity mean / min 30 s | ≥0.93 | 0.9675 / 0.9535 | 0.9686 / 0.9514 | 0.9680 / 0.9389 | pass (min a little lower) |
| DRR | ~4.9-5.1 | 4.86 | 5.02 | 5.00 | pass |
| True peak | ≤-1 | -3.12 | -2.22 | -2.41 master / -8.91 delivery | pass |
| LUFS master / delivery | -19.5 / -26 | same | ok | -19.5 / -26.0 | pass |
| Pace, whole file | ~150 | 150.4 (149.6 by measure.py) | 150.3 | **147.2** | soft miss, from the longer scripted pauses (speech rate unchanged, atempo 0.86) |
| f0 median | ~164.8 | 164.8 | 163.3 | 168.7 (studio-check) | pass (+0.4 st) |
| Script vs audio | exact | – | ok | 3,028/3,028 words in order; title, agenda and Reed's lines present | pass |
| Scripted pauses | as written | – | FAIL | all 36 within 0.25 s | pass |
| Word timing p95 | ≤20 ms | – | 25 ms | not re-measured (source alignment skipped); storyboard re-timed from the v2 master itself | n/a |
studio-check's own list (lufs, projected_pitch, projected_effort) also fails on the approved sample and was never a gate.

## The 6 remaining clicks (all within 70 ms after a word-final stop consonant)
| Time | Word | Gap after word | Level (full / >3 kHz) |
|---|---|---|---|
| 2:33.06 | weekend. | 0.02 s | -54 / -63 dB |
| 6:35.03 | tired. | 0.07 s | -47 / -61 |
| 13:35.23 | start. | 0.01 s | -73 / -87 |
| 15:38.16 | need. | 0.04 s | -45 / -54 |
| 17:07.30 | it. | 0.03 s | -42 / -65 |
| 18:49.50 | back. | 0.02 s | -71 / -80 |

## Pace by section (wpm incl. pauses; speech-only rate in brackets)
Chapters: CH1 148.7, CH2 148.1, CH3 143.4, CH4 147.7, CH5 145.7, CH6 144.9, CH7 153.3. Stories 154.8 vs teaching 145.5. Story 3 (apology) 168.4 [199.7] and Story 5 (twenties) 162.7 are still the quickest. Close 157.9.

## Decision for Aaron
- (a) Accept v2 if the 6 word-end spots sound like natural "d/t/k" endings by ear (list above and in the checklist).
- (b) Free, no new pass: a targeted ≤6 dB dip on just those 6 releases in the master. This departs from the locked chain, and I'll do it only if you approve.
- (c) Another full pass (~20.5k). Not recommended: the remaining spots are consonants, and the instruction was no third pass.

Storyboard v2: `../L01-build-2026-10-29/L01-STORYBOARD-RETIMED-v2.md` (+ json). Total with logo is 20:37.27; shots moved by up to 26.7 s from the plan; the shortest shot is 3.8 s.
