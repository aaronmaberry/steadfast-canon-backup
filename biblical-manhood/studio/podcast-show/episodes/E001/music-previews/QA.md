# Music previews QA

Generated 2026-10-03 at 4:45 PM CT. One 30 s take each on Eleven Music v2.5, with instrumental on. No retakes. Total cost was 2,250 credits (450 each), logged in `../SPEND.md`.

## Files

| File | What it is |
|---|---|
| `walk-steadfast-music-previews-A-E.mp4` | All 5 in order, 2:36, with a 1.5 s gap before B to E and a caption for each |
| `A_two-chairs.mp4` to `E_1604-at-night.mp4` | One 30 s video each |
| `raw/*.mp3` | The untouched ElevenLabs downloads (48 kHz, 192 kbps) |
| `qa/` | Waveform and spectrum images and the audio tags for each 3 s window |
| `build.py`, `analyze.py` | The build and check scripts |

The videos are 1080x1080, with the locked art A still and a small caption at the bottom. The audio is normalized to -16 LUFS (measured -15.8 to -16.0), with a true peak of -1.5 dBTP or lower. Each has a 1 s fade-out at the end.

## Checks

- **Clipping.** None in the raw files or the final videos. The loudest raw file (A) peaked at -0.3 dBFS, and the finals peak at -1.5 dBFS or lower.
- **Vocals.** None found. Whisper heard no words in any of them, only its usual "You" on music. The AudioSet tagger never scored singing at 0.05 or more. B has a short fret or slide noise at about 19 s, which the tagger scored 0.23 for "speech." It isn't a voice.
- **Endings.** All 5 come to a natural stop or decay before 30 s, except C. C is still playing in its last second, so the 1 s fade does the work there.
- **Instruments.** These were checked with an audio tagger (AST on AudioSet) and spectrograms, not by ear. Treat the notes below as flags for Aaron to listen for.

| Preview | What came out | Against the prompt |
|---|---|---|
| A. Two chairs | Cello and bowed upright bass, clear all the way through. The music settles by about 24 s, and the rest is the ring-out. | Close. The baritone guitar is faint or missing, so it plays as a string duet. |
| B. Limestone | Solo acoustic guitar, four ringing chords at about 0, 6, 12 and 19 s, each left to decay. The last 6 s is the decay. | Partial. It came out sparser than asked. There's no steady fingerpicked pattern, and the upright bass never comes in. |
| C. Dancehall waltz | Held reed chords with an accordion-style tremolo. It starts after 0.4 s of silence and stops dead twice (5.2-5.8 s and 21.8-22.1 s). | The biggest miss. No bass, brushes, bajo sexto or waltz pulse could be detected. The tagger calls it "TV theme" music. |
| D. Pedal steel evening | Acoustic or nylon guitar the whole way, with a strummed feel (strum score 0.2-0.36). | Missing its lead. The tagger never picks up pedal steel or the brushed snare. |
| E. 1604 at night | Baritone electric guitar with spring-style reverb and echo, a little gritty at the start. It winds down at about 21 s, and the last 8 s is a quiet tail. | Mostly there. The heartbeat kick and brushes aren't detectable. |

## What this means for the pick

- Each preview is one take. The final 90 s theme will be a new generation, so a miss here can be fixed with a tighter prompt. For example, C needs "steady oom-pah-pah waltz rhythm from upright bass and brushes, no pauses," and D needs "pedal steel carries the melody throughout."
- The actual charge was 450 credits per 30 s, or 15 credits per second. A 90 s full theme should cost about 1,350 credits, not the 2,727 the estimate tool showed.
