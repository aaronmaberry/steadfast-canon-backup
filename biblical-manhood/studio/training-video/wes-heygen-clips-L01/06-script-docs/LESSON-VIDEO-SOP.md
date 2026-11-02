# STEADFAST MEN — LESSON VIDEO SOP (master, v1, 2026-10-28 ~10:05 PM CT)
**BEFORE EVERY STEP (R25): re-read this SOP and the HARD RULES (section 0), then log "SOP + rules re-checked: time, phase" in PROGRESS.md. No exceptions.**
One repeatable process for L01–L24. The locked intro (`intro-final-2026-10-27/LOCKED-INTRO-v12/`, sha256 855e5ffb…2548, Drive id 1g13C_m4qFnWpMn-vGkPe8EXRkwIHyONS) is the design reference. **Do not change it.**
Status: LIVE, updated 2026-10-29 ~7:00 AM CT with R31-R32 (self-made source, storyboard in P1, prose production scripts); earlier 2026-10-28 10:12 PM CT with R23-R26. DRAFT for Aaron review. Nothing in this doc spends credits.

---
## 0. HARD RULES (Aaron, verbatim intent — every lesson, every phase)
| # | Rule |
|---|---|
| R1 | Wes is identical in every shot: **ArcFace ≥ 0.90 vs look A** (`intro_ref_embedding.npy`), mean over on-screen Wes frames; no on-screen frame < 0.75. |
| R2 | Wes is always **casual**. No suit jackets or blazers. |
| R3 | Source images must be **lip-sync capable**: face **≥ 220 px**, sharp, one face, mouth closed (open ratio < 0.06). |
| R4 | **Clear, normal conversational audio.** No whisper or hushed delivery. |
| R5 | **ONE continuous generation / Voice Changer pass per video audio.** No stitching, no patching, no hand edits. |
| R6 | **Locked v23 recipe only:** ElevenLabs Voice Changer `eleven_multilingual_sts_v2`, voice **`krjoGt4x3CttlxSuoDYW`**, ~1,000 credits/min, delivered at **−26 LUFS**. (`WES-VOICE-LOCKED-RECIPE.md`) |
| R7 | **Pace: RESOLVED Oct 28 10:03 PM: match the locked intro (~150 wpm). No other target.** (was open: Aaron said 160–165 wpm (1:40 PM Oct 28). The locked v23 recipe measures ~150 wpm (intro 150.4). Older P1 rule said 110–120. resolved, see Decision Log). |
| R8 | Script keeps **natural spoken prose**, like the intro. |
| R9 | **walksteadfast.com colors and fonts only** (TOKENS.json: #07070a… accent #8b9cff/#5b6ef5; Geist / Geist Mono). |
| R10 | **No music bed.** |
| R11 | **No audience chairs** in any frame (Wes shots or stock). |
| R12 | **No clip used twice** (within a lesson; registry enforces across lessons). |
| R13 | B-roll about the book/podcast shows **OUR branded assets** and the **live podcast image from walksteadfast.com** (hero-table.jpg as in intro v12). |
| R14 | Bubbles: **bigger, oval, polished, held 8–10 s+**, snug, **never cover text**. |
| R15 | Transitions **fully clean**: outgoing leaves fully before the next comes in, no ghosting, placed in pauses. |
| R16 | **Less movement overall.** One animated element at a time; nothing animates on Wes's panel. |
| R17 | **No hallucinated signs/logos** (look A "IST" sign is masked by `clean_look_a_bg.py`/`bg_patch_v4.py`). |
| R18 | **No per-frame matte / head-hair warping.** |
| R19 | **Nothing published, posted or spent without Aaron seeing it first.** |
| R20 | **Aaron reviews before lock.** Lock + Google Drive upload **only on his OK**. |
| R21 | Once Aaron locks: **keep only the locked version**, delete all other cuts (log it like `DELETED-INTRO-CUTS-2026-10-28.md`). |
| R22 | Width rule Z1: never above native look A width (no punch-in); variety from zoom-out, crops, bubbles. |
| R23 | **ONE MAN, FACE TO FACE (10:06 PM):** every script and all dialogue is delivered to one man, never a group. Singular "you" only; no "you guys", "men", "guys", "brothers", "gentlemen", "everyone". Grep-checked at P1 gate and P8 QC. L01–L24 scripts must be rescanned and rewritten. |
| R24 | **100% CONSISTENT (10:04 PM):** same voice ID, v23 recipe, pace (~150 wpm = intro), -26 LUFS, room tone and Wes identity every lesson; measured and logged at P3, P5 and P8; out of tolerance = redo before Aaron sees it. |
| R25 | **RE-CHECK BEFORE EVERY NEXT STEP (10:00 PM):** before starting any phase, re-read this SOP and the rules above, and log the check (`PROGRESS.md`: time, phase, "SOP + rules re-checked"). |
| R26 | **Pace = the locked intro, one number (10:03 PM):** ~150 wpm, delivery matched to the intro. No other target. |
| R27 | **WES OUTFIT LIKE THE INTRO (10:11 PM, corrected from "exact"):** new Wes images use a casual outfit in the same style as the locked intro (look A), not necessarily the identical shirt, but just as real-looking. Chambray set REJECTED ("doesn't look natural, AI slop"). |
| R28 | **REAL-LOOKING CLOTHING, NO AI SLOP (10:10 PM):** fabric, collars, seams, folds and hands must look photographic at 100% zoom. Reject any image with melted/waxy fabric, wrong collars, odd folds or warped hands. Judge close crops of the clothing, not just the face, before showing Aaron. Use real intro/look A pixels as the realism and style reference; compare clothing crops side by side with an intro frame and reject anything that looks synthetic. |

| R29 | **THE LOCKED INTRO (INTRO-FINAL-v12, sha256 855e5ffba5970bb6af01ae89c55137751eb907736304e760bbed8fae35e02548, Drive 1g13C_m4qFnWpMn-vGkPe8EXRkwIHyONS; replaced v11 Oct 29 12:48 PM) IS THE MINIMUM BAR (Aaron 2026-10-29 6:06 AM):** every video must be at least as good as the locked intro in look, audio, pace, polish and realism. Anything below it is redone, not shipped. |
| R30 | **CORRECTION LOOP (10/29):** every correction Aaron gives during a lesson is logged in the Decision Log and folded into this SOP the same turn, so the next lesson needs no hand-holding. |
| R31 | **WE MAKE IT OURSELVES, PLAN FIRST (Aaron 2026-10-29 6:25 AM):** "You rewrite the scripts like you did the intro and record yourself. You should have a production script with storyboard outline in your planning before doing anything... We aren't hiring people for each lesson. We didn't hire anyone for the intro. Do the job right and don't cut corners." No hired reader and Aaron records nothing. The natural-delivery source is made by us with our own tools, the way the intro source was made (P2 recipe below). The production script with storyboard is written in P1 before any audio or video work and Aaron approves it with the script. Videos may look the same or different from lesson to lesson. |
| R33 | **OPEN WITH TITLE + AGENDA, CLOSE WITH THE LOGO (Aaron 2026-10-29 7:29 AM):** every lesson starts with a lesson title card, then the lesson agenda, and ends with the approved Steadfast logo fading in and fading out over a silent hold (no music). The title and agenda are spoken by Wes, so they are written into the spoken script (agenda drawn from the lesson's real teaching points, R23 one-man). Approved logo = the live walksteadfast.com lockup `img/logo-lockup.jpg` (purple STEADFAST / rule / MEN on near-black; sha256 f9471087e25f…, 1142x412; same file as `/workspace/steadfast-main/img/logo-lockup.jpg`). Never invent or redraw a logo. End shot: 0.4 s bg, 0.8 s fade in, 1.6 s hold, 0.8 s fade out, 0.2 s bg; audio carries the -90 dBFS room-tone bed under it (no digital silence). |
| R32 | **PRODUCTION SCRIPTS IN NATURAL PROSE WITH TIME PAIRS (Aaron 2026-10-29 6:28 AM):** every production script pairs each spoken passage, written out in full as natural prose, with its In–Out time range, in the intro PRODUCTION-SCRIPT.md format (In–Out, spoken text verbatim, picture/graphics). No fragments or bullet shorthand for the spoken text. |

**Credits:** ElevenLabs — pace spend around the **Nov 26** renewal (L01 attempt already used 19,582.75 credits; see `lesson-plan-2026-10-26/L01-audio-full-2026-10-28/SPEND.md`). HeyGen Pro — **~931 credits, resets Nov 28.** Per-lesson HeyGen estimate from `lesson-plan-2026-10-26/cost-per-lesson-24-v3-pro.csv`: **~345–454 credits (+30% buffer 449–590), ~$22–29/lesson**; L01 = 363 est / 471 buffered / $23.10, 30 B-roll images. ElevenLabs per lesson ≈ **21–27.5 min × 1,000 ≈ 21,000–27,500 credits** (one pass) + ~500–1,000 for the 30–60 s sample. ⇒ **~931 HeyGen credits covers ~2 lessons per cycle.** Usage Monitor Bot tracks both.

---
## 1. PIPELINE (numbered phases; each ends in a gate. No phase starts until the previous gate is PASS.)
Paths are relative to `/workspace/artifacts/training/` unless absolute. LP = `lesson-plan-2026-10-26/`. NN = 2-digit lesson.

| Ph | Name | Inputs | Tools / commands | Outputs | Gate (PASS = all true) | $ |
|---|---|---|---|---|---|---|
| P0 | Kickoff + look plan | "go on lesson N" from Aaron | `python3 LP/look_plan.py --lesson N --out LP/registry/looks/LNN.json`; open task cards (§4) | `registry/looks/LNN.json`, `LP/production-scripts/LNN/` tracker | plan signature unique vs registry; credit check by Usage Monitor | 0 |
| P1 | Script rewrite + **production script with storyboard** (R31, R32) | `LP/rewrite-2026-10-27/LNN/` latest spoken script, `LP/production-scripts/LNN/`, `LP/registry/looks/LNN.json` | (1) Rewrite like the intro: plain spoken prose for the ear, one man face to face (R23), short sentences, one idea each, meaning pauses marked `[beat]` (~0.45 s) and `[pause N]`, numbers as spoken; apply steadfast-unslop. (2) Validate: `python3 LP/rules/validate_scripts.py`, `LP/rules/pacing_plan_check.py` (target 150 wpm whole file incl. pauses), `LP/rules/checkpoint.py log LNN 0 "..."` then `gate LNN 0`; R23 grep on spoken lines. (3) R33: the spoken script opens with the lesson title line and a spoken agenda (one sentence per main point) and the storyboard opens with TITLE_CARD then AGENDA shots and ends with the silent LOGO_END shot. (4) **Before any audio or video work**, write `LNN-PRODUCTION-SCRIPT-STORYBOARD.md`: a shot-by-shot table in the intro PRODUCTION-SCRIPT.md style, columns # · In–Out · Hold · Layout · Lines · Spoken (full natural prose, verbatim, R32) · Picture/graphics · Transition, timed to the projected 150 wpm audio (re-timed to real word times at P3/P6), using the look plan layouts, bubble rule (oval, ≥9 s), clean transitions in pauses, branded assets only, no music, no reused clips. Template generator: `LP/L01-build-2026-10-29/mk_storyboard.py`. | `LNN-SPOKEN-SCRIPT-vX.md` + `LNN-vX-script.txt` (paragraphs blank-line separated), `pacing-plan.json`, `LNN-PRODUCTION-SCRIPT-STORYBOARD.md` (+ storyboard.json) | validator 0 errors for the lesson (stale Z1 hits on the old shotplan JSON are superseded by the storyboard); pace = intro (~150, R7/R26); **R23 grep = 0 hits**; storyboard covers every line with In–Out times and full prose (R32); **Aaron approves script AND storyboard together** | 0 |
| P2 | **Self-made natural-delivery source (R31)** | approved script | **The intro method** (see "P2 recipe" below): ElevenLabs TTS `eleven_v4`, Wes D `krjoGt4x3CttlxSuoDYW`, stability 0.3, prompt starts `[warmly] `, plain script text (no [beat]/[pause] tags), `generations_count=1`; measure the raw read; then free prep (`build_wes_audio.sh prep` with `--atempo` set so the whole file lands at 150 wpm) | `LP/LNN-audio/source/*.mp3`, `natural.wav`, `src_16.wav` | raw read: f0 median 140-155 Hz, f0 spread ≥ 5.0 st, section pace within 10% of the lesson median; after prep: 150 wpm ±3, 0 cuts into speech; clicks 0 after the P3 chain | ~1 credit/char (~16-17k for a 20-min lesson) |
| P3 | Audio generation + clean chain | natural.wav, script.txt | `wes-audio-pipeline/build_wes_audio.sh prep JOB natural.wav script.txt` → **sample first** (30–60 s, one VC pass ~500–1,000 cr, Aaron OK by ear) → full: ONE VC pass (`eleven_multilingual_sts_v2`, `krjoGt4x3CttlxSuoDYW`, default, `generations_count=1`, input `JOB/src_16.wav`) save `JOB/sts.mp3` → `build_wes_audio.sh finish JOB NAME` → `variants.py … -26` | `NAME.wav` −19.5 master, `*-minus26-LUFS.wav/.mp3`, `JOB/REPORT.md`, `JOB/SPEND.md`, words json (fa19) | all recipe Step 6 gates on WAV+MP3 (HNR ≥4.5, sim ≥0.93, 0 clicks, TP ≤−1, cut-into-speech 0, room tone, decode, word timing p95 ≤20 ms); **Aaron OK on sample before full spend; Aaron OK on credits** | ~21–27.5k EL |
| P4 | Wes images (outfit like the intro, R27/R28) | approved bank | `wes-new-images-2026-10-28/v2-lipsync/` method: GenerateImage ($0) → `scripts/esrgan.py` → 2560x1440 → `scripts/proc.py` (inswapper + LAB + HF detail) | keepers PNG + MANIFEST row | R1–R3, eye QC (no lav mic/cables/hands artifacts), casual outfit LIKE the intro (R27); clothing crop QC at 100% (R28); **Aaron approves bank** | 0 |
| P5 | HeyGen render | −26 LUFS audio, look A `c48fd478beb311f1ea481869c933d692` (or approved new look) | Avatar IV, 1080p, 16:9, no motion prompt, **one continuous render**; clip list from `LP/shotplan.py --lesson N --seed S` (`plans/LNN-*/clips-to-render.csv`) | raw mp4(s), render IDs logged | per-frame ArcFace (R1), mouth sheet (closes in pauses), no chairs/signs; credits ≤ cost-csv row +30%; **Aaron OK on spend** | ~363–590 HG |
| P6 | Boards / B-roll / animations / transitions | look plan JSON, words json, TOKENS.json | Boards: `LP/make_boards.py` (5 layouts, §2); animations: `motion-graphics-toolkit-2026-10-27/` (HyperFrames templates T1–T7, `render.py`); B-roll: `LP/production-scripts/broll/` picker (`cands.py`, `pick.py`) restricted to branded assets; live podcast image as `LOCKED-INTRO-v12/source/hero-table-LIVE-v11.jpg` (re-capture live site if changed) | `boards/`, `boards/anim/*.mp4`, `broll-manifest.csv`, EDL (`plans/LNN-*/edl.json`) | R9–R18; registry: no clip/asset reused; text never under bubble | 0 |
| P7 | Assembly + mux | raw HeyGen, boards, anim, EDL, audio | intro build scripts as template: `LOCKED-INTRO-v12/source/build-scripts/` (`clean_look_a_bg.py`, `bg_patch_v4.py`, `render_v3.py`, `plan_calm.py`, `assemble_v4.sh`, `mux_v4.sh`); 1920x1080, 25 fps, H.264 CRF 12 + AAC | `LNN-vX.mp4`, `.srt/.vtt` (captions separate) | builds clean, duration = audio | 0 |
| P8 | QC | cut | (a) frame sweep 2 fps contact sheet + per-frame overlap check (bubble vs text boxes, no two scenes visible at once at any transition); (b) loudness `ffmpeg ebur128` = −26 LUFS, TP ≤ −1; (c) A/V offset: forced-align words vs mouth sheet, offset ≤ 1 frame; (d) ArcFace per-frame JSON; (e) videoReview two independent passes logged in `REVIEW-LOG.md`; (f) R24 consistency table: wpm, LUFS, tone, room vs intro; (g) R23 group-address grep on transcript | `qa/LNN/*`, REVIEW-LOG entries | all PASS; any FAIL loops back to the owning phase | 0 |
| P9 | Aaron review | 1080p 6–8 Mbps preview + contact sheet + QC summary | Jarvis sends link (no publish) | Aaron's notes / OK | **Aaron says lock** | 0 |
| P10 | Lock + Drive + cleanup | locked cut | write `LOCKED-LNN/LOCKED.md` (sha256, spec, date, Aaron quote); upload to Drive **only after OK**; delete all other cuts and log `DELETED-LNN-CUTS.md`; update registry `LNN.json` as LOCKED | locked folder, Drive link | sha256 matches Drive copy; one cut remains | 0 |

### P2 recipe: how we make the natural-delivery source ourselves (R31, found 2026-10-29)
**What the intro source really was.** The "old natural delivery" (`wes-audio-pipeline/reference/old-intro-natural-delivery_old_full.wav`, the old approved v3c intro audio) was not a human read. It was ElevenLabs TTS: voice Wes Hart Option D `krjoGt4x3CttlxSuoDYW`, model `eleven_v4`, at the low default-range stability (Aaron's 2026-10-27 4:58 PM rule and the studio-reference README both record "Option D, eleven_v4, default settings"; the Oct 1 Option D lecture generator in `/workspace/archive-old-wes-voice-2026-10-26/workspace/print-build/lecture-audio/` shows the same method: creative-flow TTS nodes, `[warmly]` opening tag, plain conversational prose, sections of about 1,500-1,650 characters, `gens=1`). The exact v3c intro TTS node was not found in the ElevenLabs flows the connector can read. The rejected v19/v20 sources were the same voice but run differently: v19 at **stability 0.7** (174.7 Hz, 4.56 st spread) and v20 on `eleven_multilingual_v2` speed 0.90 (188.6 Hz, 3.78 st). The steadier settings are what raised and flattened the pitch.

**Recipe (tested 2026-10-29 on L01 excerpts, see `LP/L01-build-2026-10-29/P1-REPORT.md`):**
1. Text: the approved spoken script, plain prose, paragraphs blank-line separated, markers stripped (`LNN-vX-script.txt`). Prefix `[warmly] ` once per request. No other tags.
2. TTS: creative flow tts node, `eleven_v4`, voice `krjoGt4x3CttlxSuoDYW`, `voice_settings.stability = 0.3`, similarity default, `generations_count=1`. Estimate first, log in SPEND.md. Requests are whole sections that start and end at a paragraph break (≤ about 1,600 characters, as the Oct 1 generator did, unless a single long request is proven); never split inside a paragraph.
3. Measure each raw section free (`LP/L01-build-2026-10-29/p2-research/measure.py`, `fa19.py` via `/workspace/fa-venv/bin/python`, `gates.py --renorm`): f0 median 140-155 Hz, f0 spread ≥ 5.0 st, 0 clicks; talking rate logged per section (old intro 238.6 wpm; L01 tests 233 for teaching, 274 for story). Sections more than 10% off the lesson median are flagged before any Voice Changer spend (open risk, see P1-REPORT). Stop-release clicks in the raw read (seen 1-3 per minute) are left to the chain's declick23 and must be 0 at the P3 gates. A section that fails is regenerated once with the same settings (log it); the words never change.
4. Join sections only at their paragraph silences (both 40 ms sides below -55 dBFS, the recipe's quiet-gate rule), fill with the read's own room tone, then check the join with the cut detector. Then `build_wes_audio.sh prep` with `--atempo` chosen so the whole file lands at 150 wpm (0.88 on the L01 test excerpts; 0.79 was right only for the 193 wpm v3c read).
5. Then P3 as written: ONE Voice Changer pass over the whole prepared source, chain, gates, -26 LUFS.
Aaron does not record and no reader is hired. A human read is not part of the pipeline.


**Chunked source + pace rule (Aaron YES 7:29 AM Oct 29; first used on L01, 8:30 AM):**
1. Chunk at chapter/paragraph breaks, ~800-1,300 chars each, one TTS generation per chunk (same C2 settings). QC each raw chunk: f0 median within ~1.5 st of the lesson median (L01: 147-166 Hz accepted, a 171.7 Hz take was re-rolled once), spread ≥5 st, no cuts. Raw stop-release clicks are expected but MUST be fixed in the source (step 5).
2. Pace rule (same rule for every chunk): talk rate = words / (duration x speech fraction). Per-chunk atempo = lesson-median talk rate / chunk talk rate, clamped 0.88-1.12, pitch kept. (L01 factors 0.92-1.07.)
3. Join: trim each chunk to speech (silence only), 10 ms fades, 1.0 s room tone between chunks. Room tone MUST be at the chunks' own pause level (about -72 dB), not lower: on L01 a -85 dB fill made the Voice Changer output dead air (<-75 dB) at 4 joins, flagged as cuts. Fill any digital-zero run (ffmpeg atempo makes them in TTS pauses) with the same room tone.
4. Honour the script's long pauses: write overrides.json from the [pause X] tags (every tag ≥1.2 s) and pass it to prep. L01 v1 forgot this: 1.5-2.5 s pauses (incl. the three "pause and write" exercise pauses) came out 0.56-0.9 s.
5. Before Voice Changer: run gates.py on src.wav; clicks must be fixed in the SOURCE (chain declick cannot remove TTS stop-release clicks that the Voice Changer re-voices: L01 v1 had 46 source clicks -> 63 after the chain).
6. fa19.py runs out of memory on files over ~10 min: align chunk by chunk with job/align_chunks.py and a join map.
7. Then prep_source with ONE global atempo for 150 wpm (L01: 0.86), ONE Voice Changer pass on the whole file (a 20:08 file went through the connector in one pass, no split).
**v2 fixes proven on L01 (Oct 29, 8:30-9:05 AM; each checked on a 62 s Voice Changer test before the full pass):**
8. Pause floor = the LOCKED INTRO source's own room tone (from `wes-audio-pipeline/reference/src21b_079.wav`, about -89 dB), not the TTS hiss (about -71 dB). Replace every pause run (frames under -60 dB lasting 60 ms or more, 10 ms inside each edge, 10 ms crossfades) with it (`L01-audio-2026-10-29/v2/roomtone_intro.py`). Test 1, with the TTS floor, gave 16 clicks per minute; the Voice Changer turns hiss into ticks.
9. Source declick in two steps. First `v2/declick_src.py`: the gates.py clickloc rule at +15 dB, checked on both raw and -19.5 LUFS copies, with a <3 kHz-preserving HF pull-down. Then `v2/declick_src_rel10.py` plus a broadband dip of 12 dB or less on the spots clickloc flags at +10 dB (word-final stop releases sitting in pauses). The TTS source does not count these as clicks, but the Voice Changer sharpens them into clicks. Test 2 left 4; test 3 had 0 clicks and a -58.5 dB tail. Gate: gates.py on the source = 0 clicks before paying.
10. Pause marks: overrides.json from every [pause X] of 1.2 s or more (36 on L01), all honoured. Atempo stays at the speech-rate value (0.86), so the longer pauses lower the whole-file wpm (L01: 147.4). Speaking pace is unchanged.
11. Always run a ~60 s Voice Changer test (~1,045 credits) on a window that holds a chunk join and a long pause, and check clicks 0 and dry tail -58 dB or lower, before the full pass.
---
## 2. RANDOMIZATION SPEC (different every lesson, always on-brand)
Tool: `LP/look_plan.py --lesson N [--seed S] --out LP/registry/looks/LNN.json` (deterministic per lesson+seed; checks earlier plans in `registry/looks/`). Test: `--check-all`.

| Dimension | Pool (all inside locked rules) | Fixed (never randomized) |
|---|---|---|
| Wes image/outfit | approved bank `wes-new-images-2026-10-28/v2-lipsync/keepers/` (fallback look A) | ArcFace ≥0.90, casual |
| Shot sizes | weights over full / presenter 0.62 / crop 1:1 / split panel | never above native width (Z1) |
| Layout order + variant | 5 layouts × 3 variants (WES_FULL always first) | the 5 layouts themselves |
| Bubble | home corner (bottom-right/left, top-right), hold 9/10/12/15 s | 540x405 oval, 0.7 s in / 0.45 s out, snug, never over text |
| Transitions | 2 of: dip-to-bg 0.4 s, sequential fade 0.4 s, blur-out-then-fade-in 0.5 s, hard cut in pause | outgoing fully gone first; in pauses |
| Animation techniques | 4 from TECHNIQUE-CATALOG (#2,3,4,6,7,8,9,12,15,16,18,20) | no bounce, one element at a time |
| Text-card style | 5 styles | Geist/Geist Mono, palette |
| Accent / glow corner | #8b9cff or #5b6ef5; tl/tr/bl/br | |
| Cut pacing | 3.0–5.5 layout changes/min | Wes full 10–20 s; boards 8–24 s |
| B-roll | 3 primary from branded set (book, workbook, audiobook, live podcast image, site captures, banner, lockup, app) | no stock for owned products; each file once |

**Registry format** (`LP/registry/`):
- `looks/LNN.json` — look plan (fields above + `signature` sha1 of layout order/variants/transitions/techniques). Rule: signature unique across lessons.
- `LNN.json` (existing, from shotplan) — `seq`, `boards`, `audio_keys`, `clip_ids`. Rule: no `clip_id` or B-roll file in two lessons.
- `rules/uniqueness-matrix.csv` — pairwise framing/layout similarity; keep < 0.6, shared_images = 0.

---
## 3. TEAM / ROLES (live roster from `/home/box/agent-data/agents/*/profile.json`, 2026-10-28)
Active: **Jarvis** (coordinator, only bot that talks to Aaron; dispatches executors + computerUse workers), **Project Manager** `ab86a722…` (tracker/checklist/reminders/gates — note: its profile describes a *marketing PM* job; video tracking is an added duty, confirm), **Reed** `0729fda2…` (edit gate, published-facing prose), **Source** `190a17de…` (research/source extraction), **Reader Panel** `00d08357…`, **Director** `6021cd19…` (video planning), **Usage Monitor Bot** `a275d253…`, **Not My Tempo** `3b1c4c6e…` / **Script This Routine** `6943c7a2…` (scripts for repeated routines).
**Not active — do not assign:** Steadfast Training, Steadfast Studio, Dean, Booth, Holt, Reach, Grok Build (on-call only), Frame/Clip/Thread/Tie, Counsel.

| Ph | Responsible | Accountable (Aaron gate) | Consulted | Informed |
|---|---|---|---|---|
| P0 | Jarvis (runs look_plan) | Aaron "go" | Usage Monitor (credits) | PM opens cards |
| P1 | Jarvis → executor (rewrite + production script with storyboard, R31/R32) | Aaron approves script and storyboard together | Reed (prose), Reader Panel (does it sound natural), Source (scripture/facts) | PM |
| P2 | Jarvis → executor (self-made TTS source per P2 recipe; credits logged) | Aaron OK on credits (and hears the P3 sample) | Usage Monitor | PM |
| P3 | Jarvis → executor (prep/finish free; VC pass only with OK) | Aaron: sample by ear + credits | Usage Monitor | PM |
| P4 | Jarvis → executor (image pipeline) | Aaron approves bank | Director (look) | PM |
| P5 | Jarvis → executor (HeyGen) | Aaron OK on spend | Usage Monitor | PM |
| P6 | Jarvis → executor (+computerUse for site captures) | — | Director (plan/EDL), Source (asset provenance) | PM |
| P7 | Jarvis → executor | — | Director | PM |
| P8 | Jarvis → executor QC + 2nd independent review executor | — | Director | PM logs pass/fail |
| P9 | Jarvis (sends preview) | **Aaron** | — | PM |
| P10 | Jarvis → executor (lock, Drive, cleanup) | Aaron's lock OK | — | PM closes cards; Usage Monitor logs spend |
| ops | Not My Tempo / Script This Routine: turn repeated QC/registry checks into scripts | — | — | — |

**Handoffs:** Aaron ↔ Jarvis only. Jarvis → executor (task card in, REPORT.md + paths back). Jarvis → PM (card status, one-way). Jarvis → Reed/Reader Panel/Source/Director (one-way, 1:1; they return notes/files, never message Aaron). No bot group chats.

### Task card template (P1 card carries the storyboard path; R32 prose + times) (PM tracks one per phase)
```
lesson: NN | phase: P# name | owner: <bot/executor/human> | inputs: <paths> | outputs: <paths>
gate: <pass criteria from §1> | aaron_gate: yes/no | credits_est: <n> (EL/HG) | due: <CT date/time>
status: todo/doing/blocked/pass/fail | evidence: <REPORT.md path> | next: P#+1 owner
```

### Trigger: Aaron says "go on lesson 1"
0. Before each step below: re-check this SOP + rules and log it (R25).
1. P2 source method is decided (R31: self-made source, P2 recipe) and pace is decided (match the intro). Nothing to ask.
2. Jarvis runs P0 (`look_plan.py --lesson 1`), asks Usage Monitor for EL/HG balances.
3. Jarvis sends PM the 11 task cards (P0–P10) for L01 with owners/dues; PM starts tracking.
4. Jarvis dispatches P1 executor. Each later phase starts only when PM shows the previous card PASS.

---
## 4. PROJECT MANAGER CHECKLIST (ab86a722-65ef-46c1-a41e-caa6c4eb8502)
Can do: keep the 11 cards per lesson; remind Jarvis of open Aaron gates (script, sample, spend, review, lock); keep a credit ledger (HG reset Nov 28, EL renewal Nov 26) with Usage Monitor; check gate evidence paths exist; flag a phase stuck > 24 h; keep the registry list of locked lessons.
Cannot do: talk to Aaron, approve spend, run HeyGen/ElevenLabs, edit video, publish.
Handoff: receives cards from Jarvis → updates status → returns a daily one-line status per lesson to Jarvis.
- [ ] Cards P0–P10 created  - [ ] R25 re-check logged before each phase  - [ ] R23 group-address grep 0 hits  - [ ] R24 consistency table filled  - [ ] P1 storyboard written (R31/R32, prose + In–Out times) and approved with the script  - [ ] P2 self-made source made + measured  - [ ] script OK (Aaron)  - [ ] audio sample OK (Aaron)  - [ ] EL spend OK  - [ ] HG spend OK  - [ ] QC PASS ×2  - [ ] Aaron review  - [ ] lock + Drive + cleanup  - [ ] registry updated

---
## 5. READINESS AUDIT (honest, 2026-10-28 10 PM CT)
| Item | Status | Evidence | What remains |
|---|---|---|---|
| Images for Wes | PARTIAL | look A locked; `wes-new-images-2026-10-28/v2-lipsync/` (in progress; plan now 1 outfit, chambray over white tee) | finish run, Aaron approves bank; earlier wide shots fail R3 |
| Voice | READY | `WES-VOICE-LOCKED-RECIPE.md` v23, `wes-audio-pipeline/` (bit-exact rebuild) | — |
| Speed | READY (decided: match intro) | 160–165 vs 150 vs 110–120 | decided 10:03 PM |
| Natural prose | PARTIAL | intro script; L01 rewrites in `LP/rewrite-2026-10-27/` | rewrite to locked pace once R7 decided |
| Same voice always | READY | one voice ID, retired list in `_RETIRED-WES-VOICES-2026-10-28/` | — |
| Script rewriting | PARTIAL | validators in `LP/rules/` | validator pace target to update after R7 |
| Audio generation + editing | PARTIAL | chain ready; P2 self-made source recipe tested on a 55 s L01 sample (`L01-build-2026-10-29/P1-REPORT.md`) | full-lesson source + VC pass; Aaron hears the sample |
| Post editing | PARTIAL | intro v12 build scripts (LOCKED-INTRO-v12/source/) | generalize scripts from intro to lesson length; not yet run on a full lesson |
| Boards | READY | `LP/make_boards.py`, `boards/`, `boards/anim/` | per-lesson content |
| B-roll | PARTIAL | `production-scripts/broll/`, intro podcast image | branded asset bank list not finalized; stock pickers must be restricted |
| Animations | READY | `motion-graphics-toolkit-2026-10-27/` (catalog, TOKENS, templates) | — |
| Randomization | READY (new) | `LP/look_plan.py`, `LP/registry/looks/L01–L24.json` | wire look plan into shotplan/assembly |
| Repeatable doc | READY | this file | Aaron review |
| PM ownership | PARTIAL | PM profile is marketing | confirm PM takes video tracking |

---
## 6. OPEN DECISIONS FOR AARON
1. ~~Pace~~ RESOLVED 10:03 PM: match the locked intro (~150 wpm).
2. ~~Natural human source per lesson~~ RESOLVED 6:25 AM Oct 29 (R31): we make it ourselves (P2 recipe). Open sub-question: OK to make the TTS source in paragraph-bounded sections joined at silences before the ONE Voice Changer pass (as the Oct 1 generator did)?
3. ~~Wes image bank~~ chambray REJECTED 10:10 PM; new bank must be an outfit LIKE the intro, just as real-looking (R27/R28). v3 in progress.
4. **Credits:** ~21–27.5k ElevenLabs per lesson; HeyGen ~931 ≈ 2 lessons per cycle. Order/pace of lessons vs Nov 26 / Nov 28 resets; upgrade or not.
5. **PM role:** confirm Project Manager tracks video cards (its profile is marketing).
6. Look A carries the masked "IST" sign: accept the mask or move to a clean new look.

---
## DECISION LOG
- 2026-10-28 10:03 PM CT, Aaron: "match the training video" = pace and delivery MATCH THE LOCKED INTRO (v23 recipe, ~150 wpm). This RESOLVES the pace conflict and supersedes every earlier number (110-120, 137/145, 150-155, 160-165). Script checkers must target the intro's measured pace; no other target.

## CONSISTENCY GATE (Aaron 2026-10-28 10:04 PM: "needs to be 100% consistent")
Every lesson audio and video must match the locked intro: same voice ID krjoGt4x3CttlxSuoDYW, same v23 recipe and chain, same pace (~150 wpm, measured), same loudness (-26 LUFS), same room/tone (dry, close). At P3-P5 (audio) and P9 (QC) measure wpm, LUFS, pitch/tone and room against the intro; any lesson outside tolerance is regenerated or reprocessed BEFORE Aaron sees it. Log the measurements in the lesson's PROGRESS.md. Only the visual look varies by lesson (look_plan.py); the audio never varies.

## HARD RULE: ONE MAN, FACE TO FACE (Aaron 2026-10-28 10:06 PM)
All scripts and dialogue are written for delivery to ONE man, face to face, never a group. Singular "you" only; no "you guys", "men", "guys", "brothers", "gentlemen", "everyone", "all of us" addressed to an audience. Applies at P1 (script rewrite) and is checked at the P1 gate and P9 QC with a grep for group-address words; any hit is rewritten before audio is generated. Existing lesson scripts L01-L24 must be re-scanned and rewritten to comply.

- 2026-10-28 10:10 PM CT, Aaron: chambray shirt images "don't look natural at all... real looking shirt, no AI slop, like the intro video." Set rejected (R28).
- 2026-10-28 10:11 PM CT, Aaron: "not the exact intro outfit, like it... need to look real like it does." Outfit must be LIKE the intro's (same style, same realism), not identical (R27 corrected).
- 2026-10-28 10:18 PM CT, Aaron: v3 set REJECTED, "literally the same shirt from the intro." R27 means a DIFFERENT shirt of the same simple, real-looking kind (not identical, not obviously AI), with varied poses. v4 in progress.
- 2026-10-29 6:06 AM CT, Aaron: LESSON 1 GO with burg_a (v4 burgundy tee, cleaned) as master. Step-by-step with a progress report to him after each phase; lesson 2 runs with no check-ins once lesson 1 proves the SOP. Full spend authorization. R29 locked intro = minimum bar.
- 2026-10-29 6:25 AM CT, Aaron (R31): "You rewrite the scripts like you did the intro and record yourself. You should have a production script with storyboard outline in your planning before doing anything. This should all be in the SOP. The videos can look the same or different, either way. We aren't hiring people for each lesson. We didn't hire anyone for the intro. Do the job right and don't cut corners." Human-read options A/B/D removed; P2 = self-made source (P2 recipe); P1 now includes the production script with storyboard, approved with the script.
- 2026-10-29 6:28 AM CT, Aaron (R32): production scripts are natural speaking prose with time pairs (each spoken passage in full, with its In–Out range, like intro PRODUCTION-SCRIPT.md). No fragments or bullet shorthand for spoken text. Applied to P1, the L01 storyboard, the task cards and the PM checklist.
- 2026-10-29 7:29 AM CT, Aaron: approved L01 v5 script, the storyboard and the P2 sample. YES to (a) making the TTS source in paragraph-sized chunks joined at quiet-gate silences before the ONE Voice Changer pass (R5 exception for the self-made-source recipe) and (b) evening out story vs teaching pace inside the source by rule. Full L01 audio spend authorized (~36-38k EL, stop above 45k).
- 2026-10-29 7:29 AM CT, Aaron (R33): "add an approved steadfast logo fade in and fade out at the end of each lesson. Maybe start with a lesson title too and go to your agenda for the lesson to start as well." Logo confirmed as the live site lockup img/logo-lockup.jpg (the locked intro has no logo end card; its notes name logo-lockup-navy.jpg as optional, which is a different file, not used).
- 2026-10-29 7:31 AM CT, Reed edit gate on L01 v5: PASS with edits (L066, L176, L189, L213, L185; soft L042, L129, L164), applied before any TTS.
- 2026-10-29 9:41 AM CT, Aaron: "perfect! nice work, go to the next step" after hearing L01 audio v2. v2 -26 LUFS delivery (incl. the 6 hard-consonant word-end spots) APPROVED AS IS. Next: P5 test stage only.
- 2026-10-29 10:32 AM CT, Aaron: ONE-TIME R1 identity exception for L01 full render: burg_a look b9d1bd88 on Avatar IV, expressiveness low + steady-head motion prompt (test 3, video 81783c8d), measured ~0.87 mean ArcFace instead of ≥0.90. Applies to Lesson 1 only; R1 stays ≥0.90 for future lessons unless Aaron says otherwise. Full render as ONE continuous job on v2 −26 LUFS audio (20:34.08), hard cap 600 credits.
- 2026-10-29 10:33 AM CT (R25): SOP + rules re-checked before P5 full render; resumed check 11:23 AM CT after interruption, job 4c7713cd still processing, not resubmitted.
- 2026-10-29 12:48 PM CT, Aaron: "Yup, replace it". INTRO-FINAL-v12 is THE locked intro, replacing v11 (v12 = v11 with workbook body-text blur 0:44.84–0:57.44 and subtitle wait→weight; audio bit-identical). `intro-final-2026-10-27/LOCKED-INTRO-v12/`, sha256 855e5ffba5970bb6af01ae89c55137751eb907736304e760bbed8fae35e02548, Drive LOCKED Training Videos/INTRO v12 (LOCKED 2026-10-29) folder 1crztZv3p8fvcYPPLhhkbZoePa1xDKXVg, mp4 id 1g13C_m4qFnWpMn-vGkPe8EXRkwIHyONS. v11 deleted from box and trashed on Drive (DELETION-LOG-2026-10-29.md). R29 bar = v12.
- 2026-10-29 4:52 PM CT, Aaron: "okay, run and do your editing magic - go to the next step and make the full video". L01 P6-P8 GO (boards, B-roll, animation, assembly, tech QC) on L01-P5-PATCHED-v2; cover the P19 'over' dip at 1024.40-1027.60 s with a full-frame board. Nothing uploaded before Aaron reviews (R19/R20).

[2026-10-29 17:37 CDT] Aaron 5:36 PM: 'ii approve' on L01-P7-ASSEMBLED-v1 (P7/P8 phase approval). P9 full review next; P10 lock/Drive upload NOT done, waits for his explicit lock OK. Independent videoReview of 540p copy logged: 13 'ghost' flags checked frame by frame = fade-through-bare-background, false alarm at 12 fps; title 'Lesson 1' not duplicate (build-up).

### Decision Log: Aaron correction 2026-10-29 20:41 CDT (L01-P7-ASSEMBLED-v1 graded C-, below the intro v12 bar)
- Visible facial blur at patch joins (~17:04, 10:03, 13:52, 12:33, 12:14, etc.): if clips cannot be spliced seamlessly, EDIT AROUND them (boards, B-roll, cutaways). Never show a blurred join.
- Too much hand movement (~15:30-16:02); hands look fake/rubbery throughout. Neck/head/lower chin jut toward camera while talking, throughout. Avatar V only if no cheaper fix works (he does not want the spend if fixable).
- Almost no B-roll; must match the intro's variety. Post-editing tricks showed as minimal effort.
- ~17:28: bullet list refreshed back to point 3 (odd); workbook blurred (he asked why).
- SCRIPT: the word "weeks" is HARD-banned (lessons are one at a time). Scan every script, caption and storyboard for "week" before audio; no exceptions.
- Learn from the shared X video-editing posts; consider a DaVinci Resolve MCP vs Descript; add the learned techniques to the SOP and rotate them randomly lesson to lesson.
- Intro v12 is the minimum bar; L01 v1 does NOT meet it. Not locked, not final.
