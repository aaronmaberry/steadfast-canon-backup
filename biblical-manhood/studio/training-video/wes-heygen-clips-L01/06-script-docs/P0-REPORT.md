# L01 — P0 Kickoff report (2026-10-29, ~6:20 AM CT). $0 spent. Nothing posted, uploaded or sent.

## Gate: PASS (with 3 flags for Aaron below)
| Item | Result |
|---|---|
| R25 SOP + rules re-check | logged 06:07 AM CT in PROGRESS.md |
| Look plan | L01.json re-run; signature 199f31b72a63 unique (24/24 unique). Summary: L01-LOOK-PLAN-SUMMARY.md. Wes source set to burg_a (script default pointed at rejected chambray) |
| HeyGen (read live via connector) | Pro, **931 premium credits**, resets Nov 28 (5:48 PM CT). L01 estimate 363 / 471 buffered → OK, leaves ~460–568 |
| ElevenLabs | No balance tool in the installed connector. Last known ~1,265,484 left of 1,809,761 (Oct 28 10:49 AM CT; not re-read live). Renews Nov 26. L01 need ~21–27.5k (+~1k sample) → ample |
| Task cards | 11 L01 cards P0–P10 already in /workspace/pm/lessons-tracker.csv (gen_lesson_cards.py reported "L01 exists"); P0 set to **pass** (backup lessons-tracker.csv.bak-p0-1029) |

## burg_a as HeyGen Avatar IV source
- ArcFace vs look A (intro_ref_embedding.npy, both copies identical): **0.9286** (≥0.90 PASS). One face. Face width **433 px** (≥220 PASS). 2560×1440.
- Mouth open ratio **0.069** (insightface 68-pt inner-lip gap / mouth width) — **just over the R3 0.06 limit**. Likely a slight lip part; Avatar IV usually handles it, but it's a rule miss. Options: (a) Aaron waives, (b) free local fix: close lips via inswapper/proc.py pass and re-measure, (c) test 5 s render first in P5.
- It is **not look A**: a new outfit (burgundy tee), so it needs a new HeyGen photo look; R1 ArcFace must be re-measured per frame on the renders. Hands are cut at frame edge (Aaron accepted).
- **P5 creation plan (not done):** 1) upload burg_a PNG as an asset (create_asset_upload_batch → PUT → complete_asset_batch); 2) `create_photo_avatar(name="Wes v4 burg_a", file={asset_id}, avatar_group_id=<Wes group of look A>)` so it's a new look under the same Wes character (Mode 2); 3) poll get_avatar_creation_status until trained; consent is not expected for an AI-generated face but if create_avatar_consent is demanded, stop and ask Aaron; 4) one 10–15 s Avatar IV test with the v23 sample audio, ArcFace + mouth check, before the full render. Photo-look creation is normally included in the Pro plan (no premium credits); the spend is the Avatar IV render (estimate 363). Confirm the actual charge with get_current_user before/after and log it.

## L01 script state
- production-scripts/L01/production-script.md (5,434 words incl. markup; older teacher-to-class draft).
- rewrite-2026-10-27/L01/L01-SPOKEN-SCRIPT-v4-camera.md = current one-man-to-camera script; **2,925 spoken words** (v4-body.txt 3,850 incl. markers) → **~19.5 min at 150 wpm** (~21 min with pauses; cost CSV says 21.1).
- L01-audio-full-2026-10-28: TTS build STOPPED (TTS source now banned). Spent **19,582.75 EL credits**, no usable final audio.
- **R23 grep (Steadfast Men excluded):** v4-camera: **men 4** (L106 "good men hide", L168 "a lot of men", L171 "younger men", L208 "good men keep waiting") + 1 in header note (not spoken), **everyone 1** (header note only), **we 12** (needs a manual read; mostly "we look at" lesson-framing, which addresses a group of us). you guys/guys/brothers/gentlemen/y'all/folks/fellas/fellows/all of us = 0. production-script.md: everyone 2, men 1, we 13. → **R23 gate FAILS now; fix in P1.** Note: "men" as a 3rd-person noun ("good men hide") isn't addressing an audience; strict grep counts it. Recommend rewording anyway so the grep is 0 ("a lot of guys" won't work — use "a lot of good fathers", "a man", etc.).

## P2 recommendation (natural human read)
**Recommended: Aaron records it himself on his phone, one take (Option A). $0, ~35–45 min of his time.** Matches how the intro source worked; Voice Changer replaces timbre with Wes, keeping timing and pitch movement, so his voice only needs to be relaxed and conversational. Fallback: Casting Call Club/Fiverr male narrator, one continuous unedited take; typical long-form rates ~$60–$200 for ~20 finished minutes (Voices.com higher, ~$250–$500), 1–3 days turnaround; must deliver dry 48 kHz WAV, no edits, no noise reduction.

Instructions to send Aaron (draft):
1. Quiet small room with soft stuff (bedroom/closet or parked car). Phone on Do Not Disturb, AC/fans off.
2. Use Voice Memos (iPhone: Settings → Voice Memos → Audio Quality: **Lossless**) or any app recording WAV.
3. Phone ~8–12 in from your mouth, slightly off to the side, on a stand or table. Don't hold it.
4. Read the script I send (big-font PDF, one thought per line) like you're talking to one friend across a table. Normal volume, no whisper, no "announcer". Your natural speed is fine (I slow it to 150 wpm later; aim ~180–190 wpm, a normal conversational pace).
5. ONE take start to finish (~16–20 min). If you flub, pause 2 s and re-say the sentence, keep going. Don't stop the recording.
6. Leave 5 s silence at the start (room tone). Send me the file, no edits.
Then I align it, cut flubbed repeats only if Aaron approves (strict R5 says no edits — **decision for Aaron: allow removing restarted lines at pauses before the single VC pass?**), and make a 30–60 s Voice Changer sample (~1k credits) for his ear.

## Blockers needing Aaron
1. **P2 source:** OK to record it yourself (Option A), or hire a reader (B)? Decide whether flub-restarts may be trimmed before the one VC pass.
2. **burg_a mouth open 0.069 > 0.06 (R3):** waive, or let me close the lips locally ($0) before P5.
3. **P1 script approval** needed after R23 rewrite (4 "men" lines + review of 12 "we").
