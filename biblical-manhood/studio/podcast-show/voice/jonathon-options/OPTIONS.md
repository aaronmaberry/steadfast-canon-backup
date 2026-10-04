# Jonathon voice options (Walk Steadfast)

**LOCKED: option 6, "Jonathon - Podcast" (DUD6Dsyq6xCL5Xqppm7R), saved 2026-10-03 9:40 AM CT.**

Made 2026-10-03, about 8:25 AM CT. Two ElevenLabs Voice Design v3 calls, three previews each, six candidates. Nothing saved to the voice library. Aaron picks first; the pick gets saved as "Jonathon - Podcast".

## How to listen

- `option-1.mp3` ... `option-6.mp3`: Jonathon alone, about 29-39 seconds, the raw preview.
- `with-wes/option-N-with-wes.mp3`: Wes (locked "Wes Hart - Podcast" voice) says his E007 close, then Jonathon answers. Both are leveled to the same loudness. This is the "same table" test.
  - WES: "Carry this. Waiting feels like peace. Most of the time it's a cease-fire, and somebody else is paying for it. Stop waiting."
  - JONATHON: "Okay, so here's my problem with that. You say stop waiting, and I'm sitting here thinking about the dishwasher I said I'd fix in March. March, Wes. My daughter has been loading it around a broken rack for seven months, and she's seven. That's her whole life. But here's the thing, and I mean this. The first time I sat at a table with men like this, I almost didn't go in. I sat in the parking lot for ten minutes with the engine running. So when I say I get it, I really do get it. Let's talk about what you actually do on Monday."

## The six

The descriptions below come from measurements (pitch, pace, tone brightness, roughness) compared with the Wes podcast voice, plus the prompt each option came from. Nobody has listened to them yet. Wes measures about 102 Hz median pitch with a narrow pitch range.

| # | Prompt | Generated voice ID | One-line description |
|---|--------|--------------------|----------------------|
| 1 | Primary (light Gulf Coast) | hgmsQoRxDO0t3LHBiG52 | Late 30s feel, light Gulf Coast Texas, a little higher than Wes (108 Hz), the brightest tone of the six, quick natural pace, lots of lift in the voice. |
| 2 | Primary | pKLNBedlNIynV0FwF6A4 | Late 30s, light Texas, the lowest of the six (101 Hz, about Wes's pitch), slightly grainy, quick pace. Could be too close to Wes. |
| 3 | Primary | veDjH8pYt5yp62vc5l3Y | Warm and darker in tone (106 Hz), the slowest read by far, with long pauses and big pitch swings. Most deliberate, so it may drift toward Wes's tempo. |
| 4 | Alternate (light Southern, some grit) | oLePXAmUvAodwSy9Vdu6 | The highest (119 Hz) and fastest of the six, lively and upbeat. The strongest contrast with Wes; check it doesn't sound younger than 35. |
| 5 | Alternate | 9FxLWAYmJtuKD1ylLCJt | The grittiest texture, mid pitch (103 Hz), a flat melody close to Wes's, quick pace. Drops "it" in "loading it around." |
| 6 | Alternate | DUD6Dsyq6xCL5Xqppm7R | Warm and darker (106 Hz), a moderate, easy pace, everyday guy. "I said I'd" comes out a bit slurred. |

Pace for the same 106 words: 1 = 32.5 s, 2 = 32.4 s, 3 = 39.5 s, 4 = 28.6 s, 5 = 30.5 s, 6 = 33.4 s.

A local transcription check (free, on the box) found no "uh," no invented words and no skipped sentences in any of the six.

The previews have different pitches, but most sit close to Wes's range. Options 1 and 4 are the likeliest to pass the spec's two-second test.

## Credits used (ElevenLabs credits only, no cash, no plan change)

- Voice design: 2 generations x 531 preview characters = about 1,062 credits. ElevenLabs charges Voice Design v3 for the preview-text characters per generation, not per preview. The connector doesn't report this figure; it comes from their published rule.
- Wes line for the side-by-side clips: 123 credits, as reported by the connector (eleven_v3, one take).
- Total: about 1,185 credits.

## To lock (after Aaron picks)

Run `creative_save_designed_voice` with the chosen generated voice ID, named "Jonathon - Podcast". Then add it to `locks/WES-VOICE-LOCKED.txt` as item 3. Preview IDs can be read back with `creative_get_voice_design_previews` (free), but unsaved previews may expire on ElevenLabs' side, so save soon after he picks.

ElevenLabs views: viewstate_01m40z1z4hea4awnrtt1q935sy (options 1-3), viewstate_01m40z21amefts2chmfy6wyhys (options 4-6). Wes line flow: AdaWCoxBe1b4cHAnr2IS.
