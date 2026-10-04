# E001 QA

Episode: "The Man You Keep Saying You'll Be." Script as of 10:40 AM CT on 2026-10-03, which has the new cold open and the standard intro (variant A, launch wording). 294 spoken lines, 5,549 words.

**Status.** Aaron put the intro on hold at 10:47 AM CT and wants it reworked. The opening (cold open, intro and slate, lines 1-10, the first 55 s) will be recorded again in a separate run. Everything from "Pull up a chair" (line 11) to the end is final unless Aaron asks for changes.

## Files

| File | Detail |
|---|---|
| `E001-walk-steadfast.mp3` | 192 kbps CBR, 44.1 kHz, joint stereo, ID3v2.3 tags |
| `E001-walk-steadfast.wav` | 24-bit PCM, 44.1 kHz, stereo |
| `E001-review.mp4` | 1080 x 1080 H.264 still of show art A, AAC 160 kbps. For review only. |
| Runtime | 31:48 (1,908.5 s) |

## Master metrics

Measured with ffmpeg ebur128 (BS.1770) and silencedetect.

| Check | Target | MP3 | WAV |
|---|---|---|---|
| Integrated loudness | -16 LUFS, plus or minus 1 | -16.0 LUFS | -16.0 LUFS |
| True peak | -1.0 dBTP or lower | -4.7 dBTP | -4.9 dBTP |
| Loudness range | | 3.1 LU | 3.1 LU |
| Clipped samples | 0 | 0 | 0 |
| Longest silence (under -50 dB) | under 2 s | 1.81 s | |

The mono float master reads -16.0 LUFS and -1.9 dBTP. The stereo files are two identical channels, and BS.1770 sums both, so each channel sits about 3 dB lower and the stereo true peak reads about -4.8 dBTP at the same loudness. The MP3 got +0.3 dB before encoding so it reads -16.0 after the encoder.

| Voice match | Wes | Jonathon |
|---|---|---|
| Loudness, all lines | -16.0 LUFS | -16.0 LUFS |
| Loudness, opening (lines 1-10) | -16.0 LUFS | -16.0 LUFS |
| Loudness, lines 11-294 | -16.0 LUFS | -16.0 LUFS |
| Pace, words per minute of speech | 186 | 199 |

The room tone between lines reads -70.1 dB in the opening and -70.1 dB in the rest, so the spliced opening matches the body.

Turn gaps run 0.32-1.70 s (median 0.47 s). Normal turns are 0.32-0.55 s, same-speaker runs 0.45-0.60 s. Scripted pauses get extra time: chapter breaks 1.0 s, [beat] 0.6 s, laughs 0.9 s, actions 0.8 s, the sting slot 1.2 s, [pause 1s] 1.0 s. Every gap is capped at 1.7 s so no silence reaches 2 s.

## How it was recorded

- Model eleven_v3. Locked voices only. Wes Hart - Podcast (`LxMQekBDeYENHe7wI9hA`), Jonathon - Podcast (`DUD6Dsyq6xCL5Xqppm7R`).
- **Takes, not single lines.** The brief asked for line-by-line renders. Each first-pass take was instead one speaker's lines from one chapter, separated by blank lines, under about 1,800 characters (29 takes). Three reasons. v3 is unstable on very short one-line prompts. The show bible (section 7) sets takes at about 2,000 characters per speaker run. Polling 290 separate renders would have been slow. Each take was cut into single lines at the quietest point between lines, using faster-whisper word timestamps, and every retake was done one line at a time.
- Stage directions, sips and laughs were never sent to the voice. Pauses come from silence in the edit. No "uh" or "um" appears in the script or in the transcripts.
- Spoken forms sent to the voice: 1604 as "sixteen-oh-four," walksteadfast.com as "walk steadfast dot com," @steadfastwalk as "at steadfast walk," HVAC as "H-VAC." Intro line 7 was sent with ellipses after "book" and "men" for clearer pauses. The words match the script.
- **Outro, line 288.** Uses the audio-feed variant from the script ("in the show notes" instead of "in the description" and the pinned-comment line).
- **Mix per line.** Energy trim, then loudness matched per line toward one target, then a low noise bed under the whole episode so gaps never drop to digital zero.
- **Pace.** v3 read Wes at about 229 words per minute, faster than Jonathon and far from the bible's "lower, slower, drier." Wes's lines were slowed to 0.90x with ffmpeg atempo (pitch unchanged), and 0.28 s was added at sentence ends inside his lines. Jonathon got 0.08 s at sentence ends and no tempo change. A whisper confidence check on a stretched test line scored the same as the original (0.980 vs 0.980).
- **Master.** High-pass 70 Hz, 2.5:1 compression at -24 dB, gain, limiter at -1.9 dBFS run at 4x oversampling, then MP3 and WAV exports. Settings are in `launch-kit/SPEC.md`.

## Transcript checks

Every line was checked three ways with free local faster-whisper models (medium.en, plus small.en and base.en as tie-breakers). Number forms, contractions and known sound-alikes (Jonathan for Jonathon, Danny for Dani, "hours" for "ours") were treated as matches.

1. **Per take.** Whisper on each raw take, aligned to the script, checked line by line. 291 first-pass lines, then each retake and opening take.
2. **Per line, second opinion.** Every line flagged in step 1 was cut out and transcribed again on its own.
3. **Final file.** Whisper on the finished MP3, aligned to the whole script, which also builds the SRT and VTT. Result: 268 of 294 lines match the script. 26 lines show a difference. I cut each of those lines out of the master and transcribed it again on its own. 24 are sound-alikes, number or spelling forms ("1 Corinthians," "o'clock"), or words whisper skipped during the long pass that the re-check hears clearly (lines 17, 19, 49, 122, 124 and 140). The other two are the "-ed" items below (lines 3 and 126) and line 147.

Names were checked in every pass: Wes Hart, Jonathon, Dani, Ruby, Theo, Mr. Abernathy, Pasadena, Lake Charles, Port Aransas and 1604. Both Scripture readings (1 Corinthians 13:11 and Luke 16:10, NIV) transcribe word for word.

### Retakes

| Line (old numbering, new numbering) | Problem | Result |
|---|---|---|
| 113 (now 116), Wes, "A man gets made on Tuesday" | All three whisper models dropped "A." | Retake 1 fixed it. The retake is in the episode. |
| 123 (now 126), Wes, "And skipped the Tuesday." | Whisper heard "skip the" | Retakes 1 and 2 also read as "skip the" in all three models, so this is most likely the "-ed" running into "the," which is normal speech. The retake limit was reached, and the original take is in the episode. Listen at 13:20. |
| 7 (new opening), Jonathon, "Steadfast is the book, a video training for men, and this table." | Two models heard "the book of video training for men in this table." | Retake 1 with clearer pauses passes cleanly. The retake is in the episode. |

### Flags that turned out to be whisper errors (no retake)

- Line 59 (now 62), "the man who sat with me is gone." The per-take pass missed "gone." The per-line pass and the final-file pass both hear it.
- Line 87 (now 90), Jonathon's "We're going to talk about dads..." The per-take pass skipped half the sentence. The per-line pass hears all of it, and the line has no internal silence over 0.9 s.
- Line 124 (now 127), "since when I liked 1604." medium.en heard "like," and small.en heard "liked."
- Tail words such as "Thanks for watching" or a stray "you" on silent line ends are a known whisper habit. They are not in the audio.
- Remaining single-word differences are sound-alikes: "would've" and "would have," "across" and "a cross," "well" and "will," "too" and "to," "TikTok" spelled two ways.
- Line 3 (new opening), Jonathon, "I picked the parking lot." Every model hears "pick the," the same "-ed" into "the" blend as line 126. This line will be re-recorded with the new intro, so no retake was made.
- Line 144 (now 147), Jonathon, "What's the something?" medium.en and small.en both hear "What's the sum?" The word is there but very fast (0.4 s). No credits were spent on it because this pass had to finish on the current audio. Listen at 16:15. If it sounds clipped, it's a one-line retake of about 20 characters.
- Line 262 (now 265), "or a message to @steadfastwalk." Two passes heard "or message." It's a reduced "a." Listen at 28:50 if you want to be sure.

## Known gaps and notes for Aaron

- **Opening is on hold.** The cold open, intro and slate (lines 1-10) follow the 10:40 AM script and will be replaced with the open system v3 text, see the re-record notes below. The cold open runs 17 s against the bible's 15 s limit.
- **No sting or laugh audio.** The 3 s title sting, the eleven "(both laugh)" beats and Wes's silent laugh have no audio yet. The sting slot and laughs are silence (1.2 s and 0.9 s). The show bible says the laugh method is still to be tested.
- **Runtime.** The script estimate was about 40 minutes. The render runs 31:48 because v3 reads fast even after Wes was slowed.
- **Outro asks for comments.** The audio-feed outro still says "Tell us in the comments." Apple Podcasts has no comments. For later episodes, the audio line could point to a message at @steadfastwalk instead.
- **Apple AI rule.** Resolved 2026-10-03. Aaron locked the disclosure line "Produced with AI voice and video tools." It is spoken once in the credits and is the last line of the description and show notes (SHOW-BIBLE section 13). `launch-kit/E001/description.txt`, `show-notes.md` and `_work/package.py` already carry it. The audio needs the credits line added, see the re-record notes below.

## E001 re-record notes (open system v3, 2026-10-03)

Two pieces get recorded and dropped into the existing master. Everything else stays.

**1. The new opening.** Script `scripts/E001-the-man-you-keep-saying-youll-be.md`, chapter Intro. Text comes from `_build/intros_data.py` through `_build/intro.py`, so re-run that script rather than editing lines by hand. The cold open text has not changed since the 10:40 AM script, so the recorded cold open can stay. It runs 17 s against the 15 s limit, which is Aaron's call (keep it, or trim it in a later pass).

| # | Speaker | Line |
|---|---|---|
| 1 | WES | This is Walk Steadfast. I'm Wes Hart. I've sat at tables with men for twenty-some years. |
| 2 | JONATHON | I'm Jonathon. I came to faith at twenty-nine, and I'm still learning. |
| 3 | WES | Starting today, twice a week, we talk straight about following Jesus as a man. |
| 4 | JONATHON | Wes wrote a book called Steadfast Men, and there's a video training for men. Both are at walksteadfast.com. |
| 5 | WES | Today we start where most men start. With good intentions. |
| 6 | JONATHON | Episode one. |
| 7 | WES | Tuesday, January fifth, twenty twenty-seven. |
| 8 | JONATHON | The Man You Keep Saying You'll Be. |

- The intro and slate run about 36 s on the script clock (0:20 to 0:56). Lower thirds go on lines 1 and 2.
- Read it warm and conversational, two men at a table, not an announcer read. Line 5 has a short stop before "With good intentions." No long pause.
- "walksteadfast.com" is said as "walk steadfast dot com".
- Then "Pull up a chair" (line 11 of the old opening) follows as recorded.

**2. The credits line (new, locked by Aaron).**

- After the last hold on the WIDE shot ("That's ours now.", room tone, cut), play 3 s of closing music.
- Right after the music, Wes reads: "Produced with AI voice and video tools."
- Normal credits volume, the same level as the rest of Wes's dialogue. Read it like a producer credit, plain and even.
- No gap of silence before or after it, and no ducking or fading under it. The file ends right after the line with a short natural tail.
- It is the only AI mention in the audio. It is spoken once.
- The end screen still covers the last 20 s. Check that it now ends on the credits line, not on music.
- Expect the runtime to grow by about 6 s. Re-measure loudness and true peak after the drop-in, as in the master metrics above.

**3. After the drop-in.** Re-run the transcript and chapters (`final_asr.py`, then `transcript.py`) so the new intro and the credits line are in the transcript, then `package.py`. The chapter list should still start "00:00 Cold open". Shift every later chapter time by the change in the opening length.

## Rebuild

From `_work/`: `python3 assemble.py`, then `cd out && ./master.sh 11.5`, then the export commands in `launch-kit/SPEC.md`. Then `python3 final_asr.py` and `LINES=lines_v2.json python3 transcript.py` for the transcripts and chapters, and `python3 package.py` for the package. Take picks are in `assemble.py` (PICK) and `intro_pick.json`.
