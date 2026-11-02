# L01 · P1 report (script + production script/storyboard) + P2 source research · 2026-10-29 ~7:00 AM CT
Nothing published, uploaded to Drive or sent. ElevenLabs research spend 4,746.20 of the 12,000 authorized (SPEND.md). HeyGen 0. No full-lesson Voice Changer pass.

## 1. Script v5 (one man, face to face)
- File: `L01-SPOKEN-SCRIPT-v5-one-man.md` (+ plain text `L01-v5-script.txt` for fa19/TTS; generator `mk_v5.py`).
- **2,942 spoken words, 210 lines. At the intro pace (150 wpm whole file, pauses included) that is about 19:37.** The pacing check warns that this is just under its 20-30 min window. I did not pad the script to reach 20 min.
- R23: lines L013, L018, L024, L076, L100, L106, L107, L140, L168, L171 and L208 were rewritten. The four plural "men" lines are gone. Every remaining "we", "us" or "let's" means only Wes and the viewer, or Wes's own family in a story. **The R23 grep on spoken lines finds 0 hits** ("Steadfast Men" is excluded as the brand). No em dashes.
- I kept the teaching points, the three NIV scriptures word for word, every story beat, both exercises, the final write-down, the one move and the four locked lines.
- Validators:
  - `validate_scripts.py` exits 1. For L01 the only failure is Z1 (punch-in), and it comes from the **old** shotplan `production-script.json`, which the new storyboard replaces. The same Z1 failure shows on all 24 lessons.
  - `pacing_plan_check.py`: its target was moved from 110-120 to 145-155 (R7/R26; backup `rules/pacing_plan_check.pre-150-2026-10-29.py`). `production-scripts/L01/pacing-plan.json` now says 150 wpm and 2,942 words (backup `.pre-v5-2026-10-29`). Result: OK, one warning (19.6 min is under 20).
  - `checkpoint.py log L01 0` and `gate L01 0`: OK.
- The Reed prose pass and Reader Panel review have not been run. They are SOP consults and need Jarvis to dispatch them.

## 2. Production script with storyboard (R31, R32)
- File: `L01-PRODUCTION-SCRIPT-STORYBOARD.md` (+ `storyboard.json`; generator `mk_storyboard.py`, reusable for L02).
- **70 shots over 19:37, 3.6 layout changes per minute.** Each row gives In–Out, hold, layout, line range, the spoken passage in full verbatim prose, picture/graphics and the transition in.
- Layout counts: WES_FULL 21, SPLIT 22, TYPE_BOARD_BUBBLE 18, SCRIPTURE_BUBBLE 6, BRANDED_STILL_BUBBLE 3.
- Screen time: Wes full 32%, split 32%, type board 24%, scripture 9%, branded still 3%.
- No shot is longer than about 26 s.
- Bubble is top-right, oval, held at least 9 s, and carries across short shots without re-fading. Transitions are dip-to-bg 0.4 s or a hard cut in a pause. Palette and fonts come from TOKENS, with no music.
- B-roll: the workbook twice (different files or crops) and the Steadfast lockup. The live podcast image and the YouTube banner are **not** used because L01's words never mention the podcast or the channel.
- Honest limits:
  - Times are projected from word counts, not measured. They get re-timed to real word times at P3/P6.
  - Shots that were split automatically carry a generic picture note plus a quoted row. They need a design pass at P6.
  - The intro ran 9.2 changes per minute over 3 minutes. L01 is 3.6 per minute and relies on in-shot builds, which is below the intro density.

## 3. How the old v3c intro audio was made
- **It was ElevenLabs TTS, not a human read.** The voice was Wes Hart Option D `krjoGt4x3CttlxSuoDYW` on `eleven_v4`, at default-range (low) stability.
- Evidence:
  - Aaron's 2026-10-27 4:58 PM rule (in memory) and `audio-podcast-voice-2026-10-26/studio-reference/README.md` both say "Option D, eleven_v4, default settings".
  - The retired v5 REPORT says "the same recipe as the old approved v3c intro".
  - The Oct 1 Option D lecture generator (`/workspace/archive-old-wes-voice-2026-10-26/workspace/print-build/lecture-audio/`, `gen.log`) shows the method: creative-flow TTS, a `[warmly]` opener, plain conversational prose, sections of about 1.5-1.65k characters, gens=1, post-processed with atempo 0.93, a retime to planned pauses and capgaps.
- **Not found:** the exact v3c TTS node. I read 8 flows. The Oct 21-22 flows hold only S01/S02 lesson nodes, and the v3c HeyGen video is offloaded. Its stability value is inferred, not confirmed.
- Why v19/v20 failed: v19 used the same voice at **stability 0.7** (174.7 Hz, spread 4.56 st). v20 used `eleven_multilingual_v2` at speed 0.90 (188.6 Hz, 3.78 st). The steady settings made the flat, raised pitch, not TTS as such.

## 4. Candidates tested (same 137-word excerpt, L040-L048; raw read before any processing)
| source | f0 median | f0 spread (st) | talking wpm | span wpm | clicks (raw) | verdict |
|---|---|---|---|---|---|---|
| old v3c natural delivery (whole intro, reference) | 146.1 Hz | 5.24 | 238.6 | 193.1 | - | target |
| C1 v4 Wes D default settings | 154.6 | 5.40 | 224.0 | 168.4 | 0 | close, a little high |
| **C2 v4 Wes D, stability 0.3, `[warmly]`** | **146.6** | **5.64** | **232.6** | 172.0 | 0 | **best match** |
| C3 v3 Wes D Natural, `[warmly]` | 173.4 | 4.82 | 219.0 | 172.8 | 4 | announcer-high, clicks: rejected |
| C4 v4 "Roger" (stock voice, for VC) | 118.5 | 5.17 | 228.0 | 163.5 | 0 | too low, not tried further |
| rejected v19 source (v4 stab 0.7) | 174.7 | 4.56 | - | 160.6 | - | reference |
| rejected v20 source (multilingual_v2 0.90) | 188.6 | 3.78 | - | 143.8 | - | reference |
| C2b repeat, story passage L077-L088 | 144.5 | 5.38 | **274.0** | 201.6 | 3 | pitch repeats; pace and clicks vary |

- Some tools could not be used as named:
  - The ElevenLabs connector has no history or balance tool, and voice settings beyond stability and similarity cannot be set.
  - `previous_text`/`next_text` continuity is not exposed in the connector.
  - Voice Design was not tried. Wes D already matches.

## 5. The sample (C2 through the locked chain)
- C2 was prepped with `prep_source.py --atempo 0.88`. That is 150.0 wpm, against 134.6 at 0.79, because this read is slower than the 193 wpm v3c read. Then ONE Voice Changer pass (`eleven_multilingual_sts_v2`, Wes D, gens=1, 913 credits), then `build_wes_audio.sh finish` (chain23, gates, -26 LUFS).
- **File: `L01-build-2026-10-29/L01-P2-SAMPLE-selfmade-source-minus26-LUFS.mp3` (.wav beside it), 55.9 s.**

| gate | sample | locked intro v23 (56 s excerpts at 20/80/140 s) | result |
|---|---|---|---|
| clicks WAV/MP3 | 0 / 0 (declick23 fixed 12 pre-EQ spots) | 0 | PASS |
| true peak / LUFS master | -2.48 dBTP / -19.5 | -3.12 / -19.5 | PASS |
| cuts into speech, room tone, digital zeros, decode | 0, -92.2 dB min, 0, 0 | - | PASS |
| HNR | 5.73 | 6.03-6.29 | PASS (≥4.5), a bit below intro |
| similarity / worst 30 s | 0.9695 / 0.9585 | 0.959-0.968 / 0.951-0.960 | PASS |
| pitch median (studio-check) | 163.9 Hz | 158-178 (whole file 164.8) | matches intro |
| f0 spread | 5.42 st | 5.21 st (whole) | matches |
| pace | 147.1 wpm | 149.6 (whole) | in range |
| DRR | **4.69** | 5.04-5.42 | **soft miss** (band 4.9-5.1) |
| late tail | **-55.3 dB** | -61.1 / -60.4 / -51.6 | **flag** (≤-58). The same flag fires on one v23 excerpt |
| -26 LUFS delivery MP3 | -26.0, TP -8.98, 0 clicks | -26, TP -9.62 | PASS |

- Verdict: it **passes every hard gate**. Two soft room measures (DRR, late tail) sit slightly outside the intro's numbers. Aaron's ears decide.
- The word-timing p95 gate was not computed against the source. All 137 words were placed.

## 6. Still unknown or risky
1. The exact v3c node and settings are inferred, not found.
2. **Pace varies by passage.** The story ran 274 talking wpm against 233 for the teaching passage. One global atempo will leave story sections faster than teaching sections. This needs measuring per section on the full lesson before the VC spend. If the spread is over 10%, the options are (a) accept it, as natural delivery speeds up in stories, or (b) Aaron's OK on per-section atempo, which the recipe currently bans.
3. **R5 and chunking.** The full script is 15,189 characters. The Oct 1 method generated sections of about 1.6k characters. Joining TTS sections at paragraph silences before the ONE Voice Changer pass needs Aaron's OK (SOP §6 item 2), unless a single long request works.
4. Raw TTS has 1-3 stop-release clicks per minute. The chain removed all of them in the sample, but a 20-minute file has more chances to fail the 0-click gate.
5. DRR and tail are slightly drier or wetter than the intro.
6. ElevenLabs balance is not readable through the connector.

## 7. SOP and file changes made
- `LESSON-VIDEO-SOP.md`: R31 and R32 added. P1 row now includes the storyboard step, approved with the script. The P2 row and "P2 recipe" section replace the human-read options. RACI, trigger, PM checklist, readiness audit and open decisions are updated. Decision Log has 6:25 and 6:28 AM entries. Backup: `LESSON-VIDEO-SOP.pre-R31-2026-10-29.md`.
- `WES-VOICE-LOCKED-RECIPE.md`: an R31 amendment note at Step 2 (backup `.pre-R31-2026-10-29.md`). The chain is unchanged.
- `/workspace/pm/lessons-tracker.csv`: P1 and P2 cards for all lessons are updated (backup `.bak-p1-1029`). L01 P1 is `doing`. `/workspace/pm/checklist.md` has the storyboard (R31/R32) and self-made source gates.
- `look_plan.py`: the bank is now the cleaned v4 keepers in order burg_a, olive_a, olive_b, grey_a, burg_b, and chambray is removed (backup `.pre-v4bank-2026-10-29.py`). L02-L24 plans were re-emitted with the same seeds; only the Wes image changed (backups in `registry/looks/bak-pre-v4bank-2026-10-29/`). `--check-all`: 24 unique signatures, 24 unique plans, deterministic=True. L01 keeps burg_a; other lessons' images are proposals.
- Tooling:
  - New venv `/workspace/fa-venv` (torch and torchaudio 2.11 CPU) so `fa19.py` runs.
  - `build_wes_audio.sh` now honors `FA_PY=/workspace/fa-venv/bin/python` for fa19 calls (default unchanged).
  - New `p2-research/measure.py` (pitch, spread, HNR, wpm).

## 8. Next step and credit estimate
1. Aaron listens to the sample and approves the v5 script and storyboard (P1 gate).
2. With his OK, run the full L01 source as about 10 paragraph-bounded sections. That is about 15,200 TTS credits, plus about 1,600 for a re-roll allowance.
3. Measure the sections free, then join and prep free.
4. Then ONE Voice Changer pass on about 20-21 min of prepared source. That is about 20,000-21,000 credits.
5. **Total for the full L01 audio: about 36,000-38,000 ElevenLabs credits.** Decisions needed first: chunk-join OK (risk 3) and the pace-spread rule (risk 2).
