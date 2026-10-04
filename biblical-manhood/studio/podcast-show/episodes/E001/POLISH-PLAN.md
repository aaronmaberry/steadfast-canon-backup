# E001 polish plan

**Status, 5:35 PM CT.** Done, with Aaron's calls: theme D, no bed under the open, pauses-only cold open (now 15.5 s), comments line unchanged. Results are in `QA.md` under "Polish pass." The plan below is kept as written.

Written 2026-10-03, 4:50 PM CT, against the 3:20 PM CT build (31:57, 296 lines). Nothing here has been done yet, and none of it has been spent. Times are positions in the current file.

## Summary

| Change | Where | Effect on runtime | Credits |
|---|---|---|---|
| Closing bed under the outro ending, then credits | 31:34.7 to 31:53.6 | about -1.4 s | Part of the music |
| Title sting | After the cold open, 0:17.3 | about +2.0 s | Part of the music |
| Optional quiet bed under the open | 0:19-0:47 | None | Part of the music |
| Laugh placeholders shortened, no canned laughs | 11 spots | about -8.5 s | 0 |
| Cold open tightened to 15 s or under | 0:00-0:17.3 | about -1.5 to -2.1 s | 0, or about 90 for option C |
| The 4.7 s silence before the credits | 31:48.9-31:53.6 | Filled by the music swell | 0 |
| Apple "comments" line | Line 289, 31:23.9 | about +0.5 s | About 120 |
| Final loudness and QA pass | Whole file | None | 0 |

The new runtime will be about 31:48. The music costs are in `MUSIC-OPTIONS.md`.

## 1. Closing bed and credits

Right now, "That's ours now." ends at 31:48.9, followed by 1.7 s of room tone, a 3 s silent music slot, and the credits line at 31:53.6.

The plan:

1. **Bed in at 31:34.7,** on Jonathon's "And if somebody sent you this episode, go tell him thanks." That's where the 20 s end screen starts in the video, so the picture and music arrive together. Fade in over 2.0 s with an equal-power curve.
2. **Under the sign-off** (lines 290-295, 31:34.7-31:48.9), the bed sits low and steady under the voices. Use the quiet, guitar-only section of the chosen theme.
3. **Swell after "That's ours now."** About 0.2 s after the line ends, the music rises over 1.0 s and plays on its own for about 2.5-3 s. This is the bible's "3 seconds of closing music." It replaces the hold, so there's no dead air.
4. **The music ends on its own last chord** about 0.3 s before the credits line. If the generated ending isn't clean, a 1.2 s fade timed to finish at that point does the job.
5. **Credits line dry.** Wes reads "Produced with AI voice and video tools." with no music under it, at his normal level (-16 LUFS, like every other Wes line). Per the bible, nothing is ducked or faded under the line. The file ends 0.6 s after the line, in room tone.

The credits will start about 31:52.3, and the end screen will still end on the credits line.

## 2. Title sting

- The slot is the 1.6 s gap between the cold open (ends 0:17.3) and "This is Walk Steadfast" (0:19.0). It becomes the sting, 3 s per the bible.
- Gap after the cold open's last word "1604?" is 0.25 s. Then the sting plays at full level, with no fade-in, so the two notes land clean.
- The open's first line starts as the sting's ring-out falls about 25 dB, about 0.3-0.5 s of overlap. Wes doesn't wait for full silence.
- In the video, this lines up with the navy title card.

## 3. Optional quiet bed under the open

- Under lines 4-8 (0:19.0-0:46.7), the theme's quiet section plays very low and fades out over 1.5 s before "Episode one." The slate is read dry.
- Build both versions and let Aaron choose. My lean for E001 is no bed. The open is two men at a table, and the sting already marks the start.

## 4. Laugh slots

The bible leaves laugh audio to the edit. The choices are a short real laugh take or room tone. I recommend room tone, shortened, with no canned or generated laughs. A fake laugh is the fastest way for a listener to hear "produced." A clean pause after a funny line reads as two men smiling.

- Each of the 11 "(both laugh)" gaps runs 1.28-1.44 s today. Cut each to a 0.6 s beat, which is close to a normal turn gap. That saves about 8.5 s in all.
- The video cut keeps the laugh on screen with room tone under it. Nothing to add.

| Line | Time now | Before the gap |
|---|---|---|
| 16 | 1:06.9 | "I think it's a negotiation." |
| 36 | 3:11.5 | "I found the reason." |
| 76 | 7:26.0 | "Everyone's been told." |
| 89 | 8:26.5 | "It's beeped in church." |
| 122 | 12:06.4 | "It was a happy accident." |
| 156 | 17:30.0 | "I have a lot of trip pictures." |
| 180 | 19:32.1 | "...I can't argue with it." |
| 197 | 21:33.3 | "It's usually the one that gets eaten." |
| 217 | 23:29.6 | "Very proud." |
| 274 | 29:48.8 | "See, we just did it." |
| 289 | 31:22.5 | "Somebody had the other one." |

In `assemble_v3.py`, this is one change, the laugh pause going from 0.9 s to a 0.6 s beat.

## 5. Cold open, 16.7 s against the 15 s rule

Lines 1-3 run from 0:00.6 to 0:17.3. The spoken part runs 0.6 s to 17.0 s. There are 38 words, so it's under the bible's 40-word guide, and the extra time is pauses.

| Option | What changes | Ends at | Credits |
|---|---|---|---|
| A. Tighten the pauses | Lead-in 0.6 to 0.15 s. Wes's "(beat)" gap 0.93 to 0.6 s. Turn gap into line 3 from 0.50 to 0.35 s. Pauses inside line 3 ("parking lot. / Then", "goes, / Since") from 0.56 and 0.48 to 0.35 and 0.30 s. Wes's line at 0.95x speed instead of 0.90x, in the cold open only. | About 15.5 s | 0 |
| B. A plus a word trim | A, plus cutting "Then one night" from the existing take: "I picked the parking lot. My wife goes, 'Since when do you like 1604?'" | About 14.9 s | 0, needs a script change Aaron approves |
| C. A plus a tighter read of line 3 | A, plus re-recording line 3 as one quicker read, with the same words | About 14.8-15.0 s | About 90 |

**Recommendation: B,** if the cut sounds natural. The joke lands the same and nothing new gets recorded. If "my" carries too much of "night," fall back to C. A alone leaves it half a second over, which nobody will hear, but it still breaks the rule as written.

Line 3 also still has the known "picked" blend, which every model hears as "pick the." Option C would fix that too.

## 6. The 4.7 s silence

It goes away with step 1. After the polish, the longest quiet spots are the 1.0-1.7 s chapter breaks, all under the 2 s limit. Re-run the silence check at -50 dB with a 2.0 s minimum, and expect no hits.

## 7. Levels, fades and ducking

Dialogue stays where it is, -16 LUFS integrated with each voice matched. Music levels below are measured on the music alone, before the master.

| Spot | Music level | Notes |
|---|---|---|
| Sting | -18 to -17 LUFS short-term, peaks no higher than -3 dBFS | Full level, alone, no voice over it |
| Bed under speech (outro, optional open) | -34 to -36 LUFS short-term, 18-20 LU under the dialogue | Low enough that every word stays clear on phone speakers |
| Swell after "That's ours now." | Up to -20 LUFS short-term | Stays 4 LU under the dialogue, so the music never feels louder than the hosts |
| Credits line | None | Dry |

- **Ducking.** Use drawn volume automation from the line timeline rather than a live sidechain, so there's no pumping. Ramp down over 300 ms before a line starts. Ramp back up over 600 ms only in gaps longer than 1.2 s. Shorter gaps stay down.
- **Fades.** Use equal-power fades. Bed fade-in 2.0 s. The open bed's fade-out 1.5 s. The music's final chord decays naturally, or gets a 1.2 s fade timed to end 0.3 s before the credits.
- **EQ.** Cut 2-4 dB around 1-3 kHz on the bed under speech, so the guitar or strings don't mask consonants. Keep everything below 70 Hz out, matching the dialogue high-pass.

## 8. Apple comments line (line 289)

The audio-feed outro ends with "We want to know what your Tuesday looks like. Tell us in the comments." Apple Podcasts has no comments, and other podcast apps vary. The YouTube cut keeps its own pinned-comment wording, so this fix is for the audio feed only.

- **Fix.** Change the last sentence to "Send us a message at @steadfastwalk."
- The full audio line becomes "Every link we mentioned is in the show notes. This week's challenge is written out in the show notes, plus a question for you. We want to know what your Tuesday looks like. Send us a message at @steadfastwalk."
- **How.** Record a Jonathon pickup of the last two sentences for context, then splice in only the new sentence, the same way the line 404 "I wrote it." fix was done. That's about 120 credits on eleven_v3, with Jonathon's locked voice.
- **Free fallback.** Drop "Tell us in the comments." and end on "We want to know what your Tuesday looks like." The show notes already carry the question. It's weaker because it doesn't say where to answer.
- Update the script's audio-feed variant to match, and use the same wording in future audio outros.

## 9. Final loudness and QA pass

1. Rebuild the dialogue with the new gaps (laughs, cold open).
2. Lay in the sting, beds and swell with the automation above.
3. Master the full mix with the same chain, a high-pass at 70 Hz, 2.5:1 compression, limiter at -1.9 dBFS with 4x oversampling.
4. Targets:
   - -16 LUFS integrated, plus or minus 0.5.
   - True peak -1 dBTP or lower on the MP3 after encoding.
   - Loudness range 6 LU or less.
   - The sting shouldn't push the limiter past 2 dB of gain reduction.
5. Checks:
   - No clipping.
   - No silence of 2 s or more.
   - Each voice within 0.5 LU of -16.
   - Music-only spots below the dialogue's short-term loudness.
   - Credits line dry and at Wes's level.
6. Re-export the MP3, WAV and review MP4. The MP4 length is set to the master with `-t`.
7. Re-run whisper on the final file, then `transcript.py` and `package.py`. The chapter times move by the cold-open and sting changes (net about 0 to +0.5 s) and later by the laugh cuts. Run the per-line check on line 289 and the credits line.
8. Update QA.md, SPEND.md and the music rights note in the launch kit (`SPEC.md`).

## What Aaron needs to decide

1. Which music direction, or which ones to preview (see `MUSIC-OPTIONS.md`).
2. Whether the open gets a quiet bed (my lean is no).
3. Cold open option B, C or A.
4. The Apple line wording, and approval of about 120 credits for the pickup.
5. Who the publisher is (individual or company), which decides whether the Pro plan's music terms fit or Scale is needed.
