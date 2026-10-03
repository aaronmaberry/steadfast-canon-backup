# Jonathon voice design spec (ElevenLabs Voice Design v3)

Internal. SPEC ONLY. Nothing generated, no credits spent. **Aaron has to approve the voice-design spend before anyone runs this.**

## Lock target

- **Name to save.** Jonathon - Podcast
- **Account.** The same ElevenLabs account as the Wes voices (see `locks/WES-VOICE-LOCKED.txt`). Unique Voice Design voice: never stock, never Kepler or Castor, never a clone of any real person.
- **Pairing.** It has to sit next to Wes Hart - Podcast (`LxMQekBDeYENHe7wI9hA`) and be told apart from it in two seconds with eyes closed. Wes is lower, slower, drier, Hill Country. Jonathon is a little higher and brighter, quicker, and more Gulf Coast suburban Texas, with a lighter accent.
- **Reference to match room and mic.** `/workspace/training-ep01/voice-options/wes-podcast-1.mp3`. Same close-mic dry studio, same table.

## Parameters (from ElevenLabs docs)

- **Description.** 20-1,000 characters. Prompts over 250 characters are recommended (ElevenLabs Voice Design docs).
- **Preview text.** 100-1,000 characters, matching the intended emotion and style. Longer text gives steadier results.
- **Loudness.** 0, which is about -24 LUFS, to match Wes.
- **Guidance scale.** Start at 5 (default, natural). If the accent drifts, try 8 once. Very high values can sound artificial.
- **Model.** Voice Design v3. Use the same model family as the Wes podcast voice, so their delivery tags behave the same.

Sources: https://elevenlabs.io/docs/api-reference/text-to-voice/design.mdx ; https://elevenlabs.io/docs/eleven-creative/voices/voice-design.mdx ; https://elevenlabs.io/blog/voice-design-v3

## Description prompt (primary)

```
American male, 37, from the suburbs east of Houston, Texas. Light Gulf Coast Texas accent, much lighter than a Hill Country drawl: relaxed vowels, a little twang on certain words, clear consonants. Warm, quick, bright baritone with a slightly higher placement than a deep radio voice. Natural conversational pace, a bit fast when excited, then slows down when something gets serious. Friendly, curious, self-deprecating, quick to smile in the voice. Sounds like a sales manager and young dad talking with a close friend at a kitchen table. Not a preacher, not a radio announcer, not a movie trailer. Close-mic podcast studio, dry room, no reverb, no music, clean and intimate.
```

(About 640 characters. Within the 250-1,000 range.)

## Description prompt (alternate, if the first comes out too polished)

```
37-year-old Texan man, grew up near Houston, light Southern accent. Mid-range baritone with some grit, upbeat and quick, the friend who asks the real question and laughs easily at himself. Talks with energy, then gets plain and honest when it matters. Everyday working guy, not polished, not a host voice. Recorded close on a podcast mic in a quiet, dry room.
```

## Preview text for design (about 600 characters)

```
Okay, so here's my problem with that. You say stop waiting, and I'm sitting here thinking about the dishwasher I said I'd fix in March. March, Wes. My daughter has been loading it around a broken rack for seven months, and she's seven. That's her whole life. But here's the thing, and I mean this. The first time I sat at a table with men like this, I almost didn't go in. I sat in the parking lot for ten minutes with the engine running. So when I say I get it, I really do get it. Let's talk about what you actually do on Monday.
```

## Test lines after design (to judge the candidates)

1. **Quick banter.** "You've told that story four times. It gets better every time. The fish gets bigger."
2. **Sincere.** "My dad left on a Saturday in October. I was nine. I still remember the dent in his tailgate."
3. **Pushback.** "Wait. That sounds great on a podcast. What does it look like at six-forty in the morning with a four-year-old screaming about socks?"
4. **Scripture read, plain.** "James four, seventeen. If anyone, then, knows the good they ought to do and doesn't do it, it is sin for them."
5. **Outro.** "That's the table this week. Everything we talked about is linked in the description. Go do the thing."
6. **Two-shot check (with Wes podcast voice).** Wes: "Well." Jonathon: "Here we go. He said 'well.' Buckle up."

## Pass bar

- Clearly a different man from Wes within two seconds, in mono, on a phone speaker.
- Reads as 35-40, not 25 and not 50.
- The Texas sound is present but lighter than Wes's.
- No announcer sheen, no breathy whisper, no vocal fry on line endings.
- Line 2 lands sincere without going soft or whispery.
- The scripture line sounds like a man reading to a friend, not a pulpit read.
- The same room and mic as `wes-podcast-1.mp3`.

## Spend estimate (for Aaron's approval, not run)

- Voice Design returns three previews per generation. Plan for 2-4 generations (6-12 previews), then save one.
- Credits depend on the current ElevenLabs plan and preview length. The account is on Pro this month, dropping to Creator (from the parent's notes). Ask Aaron for a ceiling before running, for example "one session, stop at four generations."
- Then a 60-second two-host test (Wes and Jonathon) on lines 1-6 before locking.

## Lock procedure (after approval)

1. Generate with the primary prompt and preview text. Save the 3 previews to `studio/podcast-show/hosts/voice-tests/` (no upload).
2. If none pass, use the alternate prompt once.
3. Aaron picks by ear. Save as "Jonathon - Podcast." Record the voice ID in `locks/WES-VOICE-LOCKED.txt` as a new item 3, with the date and his approval.
