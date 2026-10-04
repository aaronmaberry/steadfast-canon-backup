# Visual and production spec, with the Descript edit plan

Internal. Draft 2026-10-02. This is a spec for later production. It authorizes no spending and no renders, and nothing gets uploaded. The tools that generate the video have not been chosen. The realism bar is still unsolved, per Aaron's Sept 29 bar. This file covers what the finished picture must do, whatever tool makes it.

## 1. The set

- **Room.** A Hill Country study, not a church and not a "podcast cave."
  - Limestone wall behind Wes and a dark-stained shiplap wall behind Jonathon.
  - One window, camera left, with late-morning light and a live oak blurred outside.
  - A shelf with a few real books, a mason jar of pencils, and a framed black-and-white photo of a fence line. No neon. No logo wall.
- **Table.** A thick walnut slab, about 6 feet. The two men sit at the corner, about 100 degrees apart rather than straight across, so the two-shot reads as friends rather than a debate.
- **Mics.** Two broadcast dynamic mics on low-profile arms, coming in from below chin height so faces stay clear. No headphones on camera.
- **Props.** Wes has Mr. Abernathy's white diner mug and a worn brown Bible. Jonathon has a navy travel tumbler and his phone, face-down. Each has a water glass, and there's a small notepad between them.
- **Brand.** One small gold plumb-line mark on the shelf, out of focus. The palette is navy #0B1F38, gold #E3C572 and bone #E6DDCC, with warm wood and stone.
- **Grade.** Warm, a little film grain, soft highlight roll-off. Wes reads a touch warmer than Jonathon, since the window is on his side.

## 2. How the men move (natural behavior rules)

The test: muted on a TV, would a viewer believe these men are actually talking?

- **Gestures.**
  - Gestures come with the thought: an open palm on "here's the thing," a hand flat on the table for a firm point, a small chopping hand on a list.
  - Wes gestures less and lower, mostly from the elbow. Jonathon gestures more and higher, and points when he's joking.
  - No gesture loops. The same motion should never repeat within 20 seconds.
- **Drinks.**
  - Each man drinks two or three times in a main episode and once or twice on Fridays.
  - They drink while the other man is talking, never mid-line. The script marks it.
  - Wes turns his mug a quarter turn before something serious. That's his tell.
- **Listening.** The listener is never frozen.
  - He gives small nods, a half smile, and looks down at the table on a heavy line.
  - Jonathon leans back with his arms crossed when he's not buying it, then leans in when he is.
  - About 40% of every cut should be the listener reacting, as in the DOAC reaction-cut practice.
- **Eyes.** They look at each other about 80% of the time. One look to camera per episode at most, usually on the Carry This line or the challenge. Never on the slate.
- **Posture changes.** Lean in for a story, sit back for banter, hands around the mug on a confession.
- **Laughter.**
  - Real laughter is short, and the face carries it: eyes, shoulders.
  - No open-mouth cackle, and Wes doesn't laugh at his own jokes.
  - Laughter goes on a two-shot or the listener's single, never a tight close-up on the man laughing.

## 3. Camera plan

### Shot list (the "virtual 5-camera" setup)

| Code | Shot | Use |
|---|---|---|
| WIDE | The whole table and both men, room visible | Open of each chapter, transitions, laughs, breathers |
| 2S | Two-shot, waist up, both men | Banter, quick exchanges, the slate |
| WES MS / JON MS | Single, chest up, eye line slightly off-camera to the other man | Default talking shot |
| WES CU / JON CU | Close-up, shoulders up | The line that matters, confessions, the verse read |
| OTS | Over the listener's shoulder onto the speaker | Long stories, adds depth |
| INSERT | Hands, mug, Bible open, phone face-down, notepad | Cutaways, covering any edit |
| PUSH-IN | A slow 10-15% digital push on a single | One emphasis line per chapter at most |

### Cutting rules

- **Default.** Cut on speaker change, about 0.2-0.4 s after the new speaker starts (a J-cut feel).
- **Reaction cut.** On a long turn (over about 12 s), cut to the listener's single or the OTS once for 2-3 s, then back.
- **Rhythm.**
  - In conversation, hold each angle 6-12 s.
  - In stories, hold 10-20 s and use OTS and inserts.
  - On the verse read, hold the CU or go full to the verse card.
  - In Shorts, cut every 2-4 s.
- **Generated-video limits.** Following Grok's cut-list note, keep any single generated talking shot under about 8 s. Because the angles are varied, that reads as editing rather than a limit.
- **Open.**
  - The slate plays on the 2S.
  - The cold open is singles (best line first, the DOAC practice).
  - The title sting is the navy card.
  - The first chapter opens on the WIDE.
- **Heavy line.** Use a CU and push in slightly, then `[pause 2s]` on the listener's single or a BREATHER on the window.
- **B-roll.**
  - B-roll only inside a story, never as the first shot of an episode.
  - No other men's faces in B-roll, no crowds, and no shot that puts Wes or Jonathon somewhere with another generated person.
  - Use places, hands, objects and weather.
- **Never.** Spinning transitions, zoom whooshes, emoji, stock "subscribe" animations, red arrows, or a shake effect.

### Where Wes and Jonathon sit

Wes is camera left with the window light, and Jonathon is camera right. This doesn't change, so the 180-degree line holds. The singles are framed with the head centered, so a 9:16 crop works without reframing (the dossier's three-camera note).

## 4. Graphics

| Element | Spec |
|---|---|
| Title sting | 3 s. Navy card, gold wordmark (Playfair), two-note acoustic figure. |
| Lower third | First time each host speaks in an episode. Bone bar, navy text, "Wes Hart" or "Jonathon." 4 s. |
| Verse card | Full screen or right two-thirds over a blurred WIDE. Navy ground, bone Playfair text, reference and "NIV" in gold. On screen while the verse is read, plus 1.5 s. No music under it. |
| Text line | 3-8 words, bone, lower center, 3-4 s. |
| Chapter card | 2 s over the WIDE. Chapter title in Playfair. |
| Subscribe lower third | Bone and navy, a small plumb mark, the word "Subscribe." 5 s. Never over a face. |
| Challenge card | Full screen, 6 s. "This week:" plus the challenge in one sentence, with single and married lines. Also posted as a downloadable image on walksteadfast.com when the site goes live. |
| End screen | Navy background with a slow WIDE behind at 30% opacity. Two elements: next episode and Subscribe. 20 s. |

## 5. Audio

- Dialogue at -16 LUFS integrated for the podcast feed and about -14 for YouTube, with true peak at -1 dB.
- Room tone recorded or generated per set and laid under every gap, so silences sound like a room rather than dead air.
- Music only on the title sting, the end screen and breathers. Never under scripture or dialogue.
- Laughter: test real laughter takes before lock. If the generated audio can't laugh cleanly, the picture carries the laugh, with a soft room reaction underneath.

## 6. Descript edit plan

Aaron will have me edit in Descript. This plan uses Descript's Scenes, Layouts, Captions, Underlord and Sequences (Descript docs and changelog, cited in the dossier). Since our footage is generated, "multicam" here means one clip per shot code, laid into one composition.

### Project setup (once)

1. **Template project** "Walk Steadfast Main." It holds saved layouts for WIDE, 2S, WES MS, JON MS, WES CU, JON CU, OTS-WES, OTS-JON and INSERT. It also holds title sting, lower third, verse card, text line, chapter card, subscribe lower third, challenge card and end screen. Save each as a Layout so every episode uses the same frames.
2. **Template project** "Walk Steadfast Field Notes," the same layouts at a lighter density.
3. **Brand kit.** Navy, gold and bone colors, Playfair for titles, a clean sans for captions.
4. **Speakers.** Set them as "Wes Hart" and "Jonathon" so the transcript labels and captions stay correct.

### Per-episode steps

1. **Import.**
   - Audio takes per chapter (or the joined conversation file) and generated video clips named by script cue, for example `E007_ch3_WES_MS_014.mp4`.
   - Use a Sequence to align the clips to the dialogue audio. The transcript becomes the timeline.
2. **Paste the script cues.** Paste the script into a doc beside the transcript. Each `[CAM: ...]` cue becomes a scene break with that layout applied. Each `[CHAPTER: ...]` becomes a Descript chapter marker and gets a chapter card.
3. **Pauses.**
   - Confirm every `[beat]`, `[pause 1s]` and `[pause 2s]` landed at its length.
   - In Descript, "Shorten word gaps" is set to keep gaps between 0.3 and 0.8 s. Exclude the marked pauses (select them and lock them) so they aren't shortened.
   - Don't run filler removal on these scripts, because they have no fillers by design. Run it only as a check.
4. **Overlays.**
   - Each `[CARD: ...]` becomes the verse card layout, with text pasted from the script's exact NIV. It's on screen while the verse is spoken.
   - Each `[TEXT: ...]` becomes a text line.
   - `[LOWER THIRD]` goes at each host's first line.
   - `[SUB-MID]` becomes the subscribe lower third.
   - `[PLUG: ...]` gets no graphic, except a small "walksteadfast.com" text line on a site plug.
5. **Transitions.**
   - Hard cuts between angles.
   - A 6-frame cross-dissolve only into and out of chapter cards and breathers.
   - A 12-frame dip to navy into the title sting and the end screen. Nothing else.
6. **Captions.**
   - Burned in for Shorts only. For long-form, use the YouTube caption file exported from the Descript transcript (SRT).
   - Check NIV wording and names (Jonathon is spelled with an "o").
7. **Chapters.**
   - Export the chapter markers. Check that 00:00 is first, there are at least three, and each is at least 10 s.
   - Paste them into the description template.
8. **End screen.** Leave the last 20 s on the end-screen layout. The sign-off line lands as it appears.
9. **Audio.**
   - Studio Sound off, since generated voices are already clean. Test it at 20% only if the room sounds thin.
   - Loudness targets from section 5. Use the exported WAV for the podcast feed.
10. **Exports.**
    - YouTube master: 16:9, 1080p or 4K, H.264 high bitrate.
    - Podcast audio: MP3 128 kbps mono or 192 stereo, -16 LUFS.
    - Video for Spotify (if used), the YouTube SRT, and a chapters text file.

### Shorts and social cutdowns

1. In the script, `[SHORT n IN]` and `[SHORT n OUT]` mark each cut. In Descript, make each one a Composition named `E007_S3_hook-text`.
2. Reframe to 9:16 with the vertical layouts: centered single, or a stacked two-shot (Wes on top, Jonathon below) for exchanges.
3. Have a hook line on screen by frame 1 (the `On-screen hook` in the script's Shorts list). Burn in large captions in the lower-middle safe zone, clear of the platform buttons.
4. Cut every 2-4 s. Use a push-in on the payoff line.
5. **Endings.** On YouTube, end with "Full episode linked" as a caption and add the Related Video link. On TikTok and Reels, end with the caption "Full episode: Walk Steadfast on YouTube."
6. **Lengths.**
   - 20-60 s preferred. Up to 3 min for YouTube Shorts and Reels.
   - A TikTok can run longer, but keep it under 90 s.
7. Export 1080x1920, H.264, and keep a 9:16 thumbnail frame.
8. **Posting plan** (when Aaron approves posting):
   - Shorts go out one a day on the days after each main episode.
   - The same clip goes to TikTok and Reels the same day.
   - Don't post a Short before its full episode is live.

Underlord can propose clips (Descript says it can make 3-5 social clips). Use it as a second opinion only. The script's marked Shorts come first, because they were written to stand alone.

### QC checklist before export

- [ ] Slate correct: number and title only, no date anywhere in the open or slate (Aaron, 2026-10-03)
- [ ] Every verse card matches the NIV word for word, with no em dash
- [ ] No reused book or session names on screen or in captions
- [ ] Every chapter starts at a real topic turn
- [ ] Listener reactions present, with no frozen listener longer than 4 s
- [ ] Each host drinks 2-3 times (main episodes)
- [ ] No generated talking shot longer than 8 s
- [ ] Subscribe lower third doesn't cover a face
- [ ] Spoken outro matches the end-screen elements
- [ ] Loudness targets met
- [ ] YouTube upload settings checked against current platform policy (Aaron's call at first upload; SHOW-BIBLE section 13)
