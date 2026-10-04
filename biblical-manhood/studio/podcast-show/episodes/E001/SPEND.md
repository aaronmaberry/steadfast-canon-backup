# E001 spend

Aaron approved this spend on 2026-10-03 at 9:42 AM CT, approved re-recording the opening at 10:37 AM CT, and approved the new open, the body pickups, the credits line and the line 147 retake at 3:20 PM CT. It came out of ElevenLabs credits on the Pro plan. No cash was spent and the plan was not changed.

| Item | Credits |
|---|---|
| Budget cap (1.3 x 28,915 spoken characters in the 10:40 AM script) | 37,589 |
| Pilot lines 1 and 4 (single-line test, not used) | 170 |
| First pass, 29 takes (K01-K29), 29,108 characters | 29,108 |
| Retake 1, lines 113 and 123 (old numbering) | 390 |
| Retake 2, line 123 (old numbering) | 24 |
| New opening, Jonathon (cold open lines 1 and 3, intro lines 5 and 7) | 359 |
| New opening, Wes (intro lines 4 and 6, slate line 8) | 250 |
| Retake, intro line 7 (Jonathon) | 104 |
| Open system v3, Wes (open lines 4, 6 and 8, slate line 10) | 274 |
| Open system v3, Jonathon (open lines 5 and 7, slate lines 9 and 11) | 226 |
| Wes body pickups (script lines 148, 398, 404 "I wrote it." with its sentence for context, 422, 471) and the credits line | 726 |
| Retake, "What's the something?" (Jonathon, line 147 old numbering, now 148), with the next line for context | 57 |
| **Total used** | **31,688** |
| Left under the cap | 5,901 |

The total is 84% of the cap, or 1.10 credits per spoken character.

- The three 10:41-10:43 AM CT opening renders (713 credits) were replaced by the open system v3 recording. Their cold-open lines 1 and 3 are still in the episode. The rest of those takes is unused.
- The 3:20 PM CT run made 4 renders at 3:23 PM CT, 1,283 credits, each on the first take. No retakes were needed.
- Model is eleven_v3, at 1 credit per character.
- Voices are Wes Hart - Podcast (`LxMQekBDeYENHe7wI9hA`) and Jonathon - Podcast (`DUD6Dsyq6xCL5Xqppm7R`). No stock voices were used.
- Renders ran in the ElevenLabs flow "Walk Steadfast E001 - line renders" (`VaCI0MntRH6rA8guQVSA`). The 3:23 PM CT renders ran in flow `EwRd8CtumnwfR3Dp0ytM`.
- ElevenLabs listed each generation's cost in credits. The per-take log, with session and generation IDs, is in `_work/ledger.tsv`.
- Transcription checks, mixing, mastering, art and video used free local tools (faster-whisper, ffmpeg, Pillow) and cost nothing.

## Music previews (separate from the voice budget)

Aaron approved one 30 s preview of each of the 5 music directions in `MUSIC-OPTIONS.md` at 4:44 PM CT on 2026-10-03, with a 5,000-credit cap. These credits are not part of the E001 voice budget above.

| Item | Credits |
|---|---|
| Cap | 5,000 |
| A. Two chairs, 30 s | 450 |
| B. Limestone, 30 s | 450 |
| C. Dancehall waltz, 30 s | 450 |
| D. Pedal steel evening, 30 s | 450 |
| E. 1604 at night, 30 s | 450 |
| **Total used** | **2,250** |
| Left under the cap | 2,750 |

- The flow estimate said 4,545 credits ($0.75). The actual charge was 450 credits per preview ($0.074 each), which matches ElevenLabs' published rate of 900 credits per minute. The estimate tool overstates music by about 2x.
- Model eleven_music_v2_5, instrumental on, lyrics type "instrumental," one take each, no retakes. Generated at 4:45 PM CT.
- Flow "t3gwySRinyavcLOZYecj." The previews are saved in `music-previews/`.

## Theme D full take

Aaron picked D. Pedal steel evening and approved one full 90 s theme plus one retake at 5:05 PM CT on 2026-10-03, with a 3,000-credit cap.

| Item | Credits |
|---|---|
| Cap | 3,000 |
| Theme D, 90 s, take 1 (used) | 1,350 |
| Retake | 0, not needed |
| **Total used** | **1,350** |
| Left under the cap | 1,650 |

- Model eleven_music_v2_5, instrumental on, generated at 5:06 PM CT. The prompt keeps the preview's character, with nylon guitar leading, soft pedal steel swells underneath and upright bass.
- Flow "t3gwySRinyavcLOZYecj", node `Zr0v9b3ojDql7KcDOzAn`. The raw file is `music/theme-D-full_take1.mp3`.
- Music total so far is 3,600 credits (2,250 for previews plus 1,350 for the theme).

## No-date slate edit (2026-10-03 evening CT)

- 0 credits. Wes's dated slate line was cut from the existing recording with a local edit. No voice or music generation. Music total stays 3,600 credits.
