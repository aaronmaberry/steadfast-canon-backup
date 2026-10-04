# E001 QA

Episode: "The Man You Keep Saying You'll Be." Script as of 3:20 PM CT on 2026-10-03, with the open system v3 open and slate, the five approved Wes body pickups and the credits line. 296 spoken lines.

**Status.** Polished at 5:05-5:35 PM CT on 2026-10-03 (see "Polish pass" below). Before that, re-recorded and rebuilt on 2026-10-03 after Aaron's 3:20 PM CT approval. In this pass, the open (lines 4-8), the slate (lines 9-11, now led by Jonathon), Wes's body pickups (script lines 148, 398, 404, 422 and 471), the line 147 retake and the credits line were recorded and dropped in. The cold open (lines 1-3) and every other body line are the earlier recordings. Line numbers below are spoken-line numbers in the 296-line list unless they say "script line." 

## Polish pass (5:05 PM CT)

Aaron picked music direction D and made the calls below. The dialogue takes are unchanged. Only gaps, the cold-open pauses and the music changed. Build scripts are `_work/assemble_v4.py` and `_work/mixmusic.py`.

| Change | Result |
|---|---|
| Theme | `music/theme-D-full_take1.mp3`, 90 s, Eleven Music v2.5, one take (1,350 credits). Nylon guitar leads, with pedal steel swells and upright bass. No vocals, no dead stops. |
| Title sting | The theme's first 3 s (its opening harmonic figure ringing into an E chord, with a 0.8 s fade at the end). It starts 0.25 s after "1604?" (0:15.9). Wes's open starts at 0:18.5 on the ring-out. -17.9 LUFS, peak -3.0 dBFS. |
| Bed under the open | None, per Aaron |
| Closing bed | Theme 70.3-86.7 s. 2 s fade-in at 31:27.3, the start of the 20 s end screen. It sits at -35.0 LUFS under the sign-off (speech plus bed reads -15.8 against -16.0 for speech alone). After "That's ours now." (ends 31:40.1), it rises over 0.8 s. The theme's final chord lands at 31:40.7 at -20.5 LUFS, rings and fades out over 1 s, and is silent from 31:43.7. |
| Credits line | Starts 31:44.0, 0.3 s after the music ends, with no music under it (music stem reads digital zero there). Same level as before. The file ends 0.6 s after it. |
| Laughs | No canned laughs. All 11 laugh gaps are 0.6 s of room tone (were 1.28-1.44 s). |
| Cold open | Pauses only, no script change. Lead-in 0.6 to 0.15 s, Wes's beat 0.93 to 0.5 s, turn into line 3 0.50 to 0.3 s, Wes's line at 0.95x instead of 0.90x, "615, / on purpose" 0.27 to 0.20 s, "lot. / Then" 0.54 to 0.30 s, "goes, / Since" 0.35 to 0.25 s. Lines 1-3 now run 15.5 s (0:00.15 to 0:15.7), down from 16.7 s. That's still about 0.5 s over the 15 s rule. Getting under it needs a word cut or a faster line 3 read. |
| The 4.7 s silence | Gone. The music swell fills it. |
| Comments line | Unchanged ("Tell us in the comments."), still Aaron's call |

Music levels are measured on the music alone, in the stereo file. The dialogue goes into the stereo mix at -3 dB per channel, the same pan law as the mono-to-stereo exports before, so it still reads -16.0 LUFS.

Joins and checks for this pass:

- **Sting and open.** The spectrogram shows a clean start on the sting's first note and no click. The open's first word comes in with the sting about 23 dB down from its start. Whisper on 0:00-0:24 hears every word of the cold open and the open's first lines.
- **Outro.** The bed shows as faint guitar under lines 290-295. Whisper on lines 290-295 with the bed under them hears every word.
- **Credits.** Cut out alone, the credits line transcribes word for word. In the long whole-file pass, whisper drops it after the music swell, a whisper habit at file ends after music. The SRT and VTT cue (31:43.96-31:46.81) comes from the line timeline.
- **Final-file transcript.** 272 of 296 lines match, the same count as before the polish, with the same sound-alike differences plus the credits line above.
- **Silences.** None at 2 s or more. The five longest are 1.6-1.85 s, all chapter breaks.
- **By ear.** I can't play audio in the box. Listen first at 0:14-0:22 (sting) and 31:25-31:47 (bed, swell, credits).

## Files

| File | Detail |
|---|---|
| `E001-walk-steadfast.mp3` | 192 kbps CBR, 44.1 kHz, joint stereo, ID3v2.3 tags |
| `E001-walk-steadfast.wav` | 24-bit PCM, 44.1 kHz, stereo |
| `E001-review.mp4` | 1080 x 1080 H.264 still of show art A, AAC 160 kbps. For review only. |
| `music/theme-D-full.mp4` | The whole 90 s theme on the art A still, -16 LUFS, for listening |
| `music/theme-D-sting-3s.wav`, `music/theme-D-outro-bed_E001-levels.wav` | The sting and closing bed as mixed in E001, 24-bit stereo, for reuse |
| Runtime | 31:47 (1,907.3 s). It was 31:57 before the polish. |

## Master metrics

Measured with ffmpeg ebur128 (BS.1770) and silencedetect.

| Check | Target | MP3 | WAV |
|---|---|---|---|
| Integrated loudness | -16 LUFS, plus or minus 1 | -16.0 LUFS | -16.0 LUFS |
| True peak | -1.0 dBTP or lower | -3.0 dBTP | -3.0 dBTP |
| Loudness range | | 3.1 LU | 3.1 LU |
| Clipped samples | 0 | 0 | 0 |
| Longest silence (under -50 dB) | under 2 s | 1.85 s, a chapter break at 14:39 | same |

After the polish, the stereo files are the dialogue (two identical channels) plus the stereo music. The true peak of -3.0 dBTP is set by the sting and the music peaks. The dialogue-only mono master reads -16.0 LUFS and -1.8 dBTP (sample peak -1.93 dBFS). The stereo dialogue is two identical channels, and BS.1770 sums both, so each channel sits about 3 dB lower and the stereo true peak reads about -4.8 dBTP at the same loudness. The MP3 got +0.3 dB before encoding so it reads -16.0 after the encoder.

| Voice match | Wes | Jonathon |
|---|---|---|
| Loudness, all lines | -16.0 LUFS | -16.0 LUFS |
| Loudness, opening (lines 1-11) | -16.0 LUFS | -16.0 LUFS |
| Loudness, 3:23 PM pickups and retake | -16.1 LUFS | -16.2 LUFS |
| Loudness, all other lines | -16.0 LUFS | -16.0 LUFS |
| Pace, words per minute of speech | 184 | 199 |

The room tone between lines reads -70.1 dB in the opening and -70.2 dB in the rest, so the spliced opening matches the body.

Before the polish, turn gaps ran 0.32-1.70 s (median 0.48 s). After it, they run 0.30-1.70 s (median 0.47 s), apart from the 2.85 s sting gap and the 3.9 s music gap before the credits, both filled with music. Normal turns are 0.32-0.55 s, same-speaker runs 0.45-0.60 s. Scripted pauses get extra time. Chapter breaks get 1.0 s, [beat] 0.6 s, laughs 0.9 s, actions 0.8 s, the sting slot 1.2 s, [pause 1s] 1.0 s. Every gap is capped at 1.7 s so no silence reaches 2 s. The one planned exception is the credits. The 1.7 s hold after "That's ours now." plus the 3 s closing-music slot come to 4.7 s. No closing music exists yet (see below), so the slot is room tone for now.

## How it was recorded

- Model eleven_v3. Locked voices only. Wes Hart - Podcast (`LxMQekBDeYENHe7wI9hA`), Jonathon - Podcast (`DUD6Dsyq6xCL5Xqppm7R`).
- **Takes, not single lines.** The brief asked for line-by-line renders. Each first-pass take was instead one speaker's lines from one chapter, separated by blank lines, under about 1,800 characters (29 takes). Three reasons. v3 is unstable on very short one-line prompts. The show bible (section 7) sets takes at about 2,000 characters per speaker run. Polling 290 separate renders would have been slow. Each take was cut into single lines at the quietest point between lines, using faster-whisper word timestamps, and every retake was done one line at a time.
- Stage directions, sips and laughs were never sent to the voice. Pauses come from silence in the edit. No "uh" or "um" appears in the script or in the transcripts.
- Spoken forms sent to the voice were 1604 as "sixteen-oh-four," walksteadfast.com as "walk steadfast dot com," @steadfastwalk as "at steadfast walk" and HVAC as "H-VAC." The words match the script.
- **Outro, line 289.** Uses the audio-feed variant from the script ("in the show notes" instead of "in the description" and the pinned-comment line).
- **Mix per line.** Energy trim, then loudness matched per line toward one target, then a low noise bed under the whole episode so gaps never drop to digital zero.
- **Pace.** v3 read Wes at about 229 words per minute, faster than Jonathon and far from the bible's "lower, slower, drier." Wes's lines were slowed to 0.90x with ffmpeg atempo (pitch unchanged), and 0.28 s was added at sentence ends inside his lines. Jonathon got 0.08 s at sentence ends and no tempo change. A whisper confidence check on a stretched test line scored the same as the original (0.980 vs 0.980).
- **3:20 PM CT re-record.** Four renders, each on the first take, at 1 credit per character (1,283 credits):
  - Wes, open lines 4, 6 and 8 and slate line 10, in one take.
  - Jonathon, open lines 5 and 7 and slate lines 9 and 11, in one take.
  - Wes, the five body pickups and the credits line, in one take so his voice matches across them. Script line 404 was rendered with its full sentence for context ("It's called Steadfast Men, The Way of Godly Men. I wrote it. It's thirty-five short chapters in five parts."). Only "I wrote it." was cut out and placed after "The Way of Godly Men." in the original take, replacing "I wrote it, and it's coming." The rest of the recorded line is unchanged.
  - Jonathon, "What's the something?" with his next line for context. Only the first line is used.
- **Matching the pickups.** Each new line went through the same chain as the body. That's energy trim, Wes at 0.90x, sentence pauses and per-line loudness match. Two extra steps:
  - On vowels, the new Wes takes carried 2-3 dB more 8-16 kHz air than the body takes. Body takes vary by up to 1.6 dB in any band. A -4 dB high shelf at 8 kHz on the new Wes takes closes the gap.
  - The line 404 splice was level-matched on the phrase before it, "The Way of Godly Men." The new read is softer than the old one. "I wrote it." comes out as a quiet aside rather than a stressed line, and it keeps that shape.
- **Line-end fades.** v3 files and tight take cuts sometimes stop while a word is still decaying (-30 to -45 dB). A 50 ms fade now goes on any line whose last 10 ms sits above -50 dB. That's 45 lines in all, including slate lines 10 and 11 and the credits line, which end their takes. The fade removes steps and clicks at those ends and doesn't change any words.
- **Master.** High-pass 70 Hz, 2.5:1 compression at -24 dB, gain, limiter at -1.9 dBFS run at 4x oversampling, then MP3 and WAV exports. Settings are in `launch-kit/SPEC.md`.

## Transcript checks

Every line was checked three ways with free local faster-whisper models (medium.en, plus small.en and base.en as tie-breakers). Number forms, contractions and known sound-alikes (Jonathan for Jonathon, Danny for Dani, "hours" for "ours") were treated as matches.

1. **Per take.** Whisper on each raw take, aligned to the script, checked line by line. 291 first-pass lines, then each retake, opening take and pickup.
2. **Per line, from the master.** Every new line in this pass (4-11, 72, 148, 240, 243, 254, 285, 296) was cut out of the finished WAV and transcribed on its own. All 15 match the script word for word, apart from number and spelling forms ("20-some," "29," "5th, 2027," "WalkSteadfast.com"). Line 148 now reads "What's the something?" clearly, where the old take came out as "What's the sum?"
3. **Final file.** Whisper on the finished MP3, aligned to the whole 296-line script, which also builds the SRT and VTT. 272 of 296 lines match. None of the 24 lines with a difference is a new line. I cut out and re-transcribed the ones that hadn't shown up in earlier passes (lines 32, 51, 140, 176 and 250). Each comes back word for word, so they are long-pass whisper slips. The rest are sound-alikes and spelling forms ("West" for "Wes," "Fogg," "o'clock," "would have," "a cross," "@steadfastwalk" spelled out) or the two "-ed" items below (lines 3 and 127).

Names were checked in every pass: Wes Hart, Jonathon, Dani, Ruby, Theo, Mr. Abernathy, Pasadena, Lake Charles, Port Aransas and 1604. Both Scripture readings (1 Corinthians 13:11 and Luke 16:10, NIV) transcribe word for word.

### Joins

- **By waveform and spectrogram.** I looked at every join around a new line. That covers the open and slate, lines 72, 148, 240, 254 and 285, the line 404 splice and the credits. No clicks, no broadband ticks at the cuts, and no change in the noise floor at any boundary.
- **By level.** The new lines sit within 0.2 dB of their speaker's level. Wes's pickups read -16.1 LUFS and Jonathon's -16.2, against -16.0 for each across the episode.
- **By tone.** Pitch matches: Wes's new lines have a median of 113 Hz against 116 Hz for the lines around them, and Jonathon's 114 Hz against 114 Hz. After the high shelf, the vowel spectrum of each new take is within 1.5 dB of the body takes in every band.
- **Line 404 (spoken line 243).** "...The Way of Godly Men. I wrote it. It's thirty-five short chapters..." The cut points fall in silence on both sides. The pauses around "I wrote it." run 0.42 s before and 0.38 s after, about the same as the other sentence breaks in that line. Listen at 26:18.
- **Listening.** I can't play audio in the box. The by-ear check here means the per-line transcripts, the level and pitch numbers and the pictures above. These are the spots to listen to first:

| Time | What |
|---|---|
| 0:18-0:55 | New open and slate |
| 7:03 | Line 72, "thirty-six, thirty-seven in February" |
| 16:16 | Line 148, "What's the something?" |
| 25:50 | Line 240, "named once near the top" |
| 26:18 | Line 243, the "I wrote it." splice |
| 27:45 | Line 254, "That's the one place to check." |
| 31:01 | Line 285, outro walksteadfast.com line |
| 0:14-0:22 | Cold open end, sting, open start |
| 31:25-31:47 | Closing bed, swell, credits line |

### Retakes

| Line | Problem | Result |
|---|---|---|
| 117, Wes, "A man gets made on Tuesday" | All three whisper models dropped "A." | Retake 1 fixed it. The retake is in the episode. |
| 127, Wes, "And skipped the Tuesday." | Whisper hears "skip the" | Retakes 1 and 2 also read as "skip the" in all three models, so this is most likely the "-ed" running into "the," which is normal speech. The retake limit was reached, and the original take is in the episode. Listen at 13:22. |
| 148, Jonathon, "What's the something?" | Two models heard "What's the sum?" in the old take (0.4 s word). | Retaken at 3:23 PM CT. The new take passes cleanly in every pass and is in the episode. |

### Flags that turned out to be whisper errors (no retake)

- Line 3 (cold open), Jonathon, "I picked the parking lot." Every model hears "pick the," the same "-ed" into "the" blend as line 127. The cold open wasn't part of this re-record, so the 10:41 AM take stays. Listen at 0:11.
- Line 63, "the man who sat with me is gone." The per-take pass missed "gone." The per-line pass and the final-file pass both hear it.
- Line 91, Jonathon's "We're going to talk about dads..." The per-take pass skipped half the sentence. The per-line pass hears all of it.
- Line 128, "since when I liked 1604." medium.en heard "like," and small.en heard "liked."
- Line 266, "or a message to @steadfastwalk." Passes hear "or message." It's a reduced "a." Listen at 28:52 if you want to be sure.
- Tail words such as "Thanks for watching" or a stray "you" on silent line ends are a known whisper habit. They are not in the audio.

## Known gaps and notes for Aaron

- **Closing music and sting are in** (polish pass). The note below is from before the polish. No music file existed then. The 3 s closing-music slot before the credits is room tone, so the credits line follows 4.7 s of quiet (the 1.7 s hold plus 3 s). Once the two-note figure exists, it drops into that slot with no other edit. The 3 s title sting after the cold open is still a 1.2 s silent slot, and the eleven "(both laugh)" beats and Wes's silent laugh have no audio.
- **Credits line.** "Produced with AI voice and video tools." Wes reads it right after the music slot, at the same level as the rest of his lines (-16 LUFS). There's no ducking or fade under it. The file ends 0.6 s after the line. It is the only AI mention in the audio. The 20 s end screen covers 31:37 to the end, so it now ends on the credits line, not on music.
- **Cold open.** It runs 15.5 s after the polish, against the bible's 15 s limit. That was pauses only. A word cut or a quicker line 3 read would get it under.
- **Runtime.** 31:47 after the polish (was 31:57). The body pickups net about 6 s shorter as planned, while the new open and slate and the credits add time.
- **Outro asks for comments.** The audio-feed outro (line 289) still says "Tell us in the comments." Apple Podcasts has no comments.
- **Still Aaron's call, no audio planned.** Script line 131 ("every other Thursday for six years") and the pinned comment "We read these."
- **Script body.** Script lines 148, 398, 404, 422 and 471 in `scripts/E001-the-man-you-keep-saying-youll-be.md` now carry the approved wording, so the script, the audio and the transcripts match. A copy of the script from before the edit is in `_work/script_before_pickups.md`.

## Rebuild

From `_work/`:

1. `python3 parse_v3.py`. It writes `lines_v3.json` from the script. Then copy the audio-feed variants from v2 if the script changes again (see the shell history in this pass).
2. `python3 splice404.py` builds the line 404 splice.
3. `python3 assemble_v4.py`, then `cd out && ./master.sh 11.5`, then `cd .. && python3 mixmusic.py` (writes `out/final_f32.wav`, stereo, with the music).
4. Run the export commands in `launch-kit/SPEC.md`, using `out/final_f32.wav` as the input (no `-ac 2`, it's already stereo). The MP4 uses `-t` set to the master length, not `-shortest`.
5. `python3 final_asr.py`, then `LINES=lines_v3.json python3 transcript.py` and `python3 package.py`.

Take picks are in `assemble_v3.py` (V3, PICK and EQ). The joins and tone checks are `joincheck.py`, `ltas.py` and `metrics_v3.py`, and they write to `out/`.
