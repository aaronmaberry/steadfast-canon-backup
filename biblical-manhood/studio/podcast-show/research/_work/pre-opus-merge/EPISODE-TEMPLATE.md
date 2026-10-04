# Walk Steadfast episode template

Copy this file into `launch-kit/E###/` and fill in every field. The settings and limits come from `SPEC.md`. Write the copy to the unslop rules (no em dashes, straight quotes, plain sentences).

## Metadata

| Field | Value | Rule |
|---|---|---|
| Show | Walk Steadfast | Same on every episode |
| Episode title | | No episode number, season number or show name in it. Under about 60 characters. |
| Episode number | | Non-zero integer |
| Season | 1 | Non-zero integer. Apple hides it while only one season exists. |
| Episode type | full | full, trailer or bonus |
| Explicit | false (Clean) | Every episode is clean |
| Publish date | Tue/Fri, DD Mon YYYY 05:00:00 -0600 | RFC 2822, 5:00 AM CT. Use -0500 during daylight time. |
| Duration | seconds | From the final MP3 |
| Audio file | E###-walk-steadfast.mp3 | ASCII file name, 192 kbps MP3, -16 LUFS, -1 dBTP or lower |
| GUID | walksteadfast-e### | Set once and never change it |
| Episode link | https://walksteadfast.com/episodes/e### | Confirm the site path before launch |
| Episode art | none, or E###-art-3000.jpg | Optional. 3000 x 3000 JPG, RGB, no alpha. |
| Transcript | E###-transcript.vtt (plus .srt) | Built from the final audio. Speaker names in the VTT. |
| Chapters | chapters.json | Titles of 45 characters or fewer |

## Description

The first two lines show in the app before "more." Put the search words a man would use in those two lines.

```
[Line 1: the question or claim of the episode, in plain words.]
[Line 2: who is talking and what happens. Name Wes Hart and Jonathon.]

[Short summary, 2 to 4 sentences. What they talk about, the story each man tells, and where they disagree.]

Scripture
[Reference, (NIV)]

This week's challenge
[One line. Versions for the married man and the single man when the episode has them.]

Mentioned
[Book chapter or training session, only when the episode plugs it. "Coming" until launch.]

New episodes every Tuesday, plus Field Notes every Friday.

walksteadfast.com
Instagram, X, Facebook and TikTok: @steadfastwalk

Scripture quotations taken from The Holy Bible, New International Version®, NIV®. Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.™ Used by permission. All rights reserved worldwide.

Produced with AI voice and video tools.
```

Rules from the show bible.
- The last line of the description and of the show notes is always "Produced with AI voice and video tools." on its own line, word for word (show bible section 13). It appears nowhere else in the copy: not in the title, the summary, chapters or the pinned comment.
- Add the 988 line only when the episode touches suicide or self-harm.
- No prices. The book and training stay "coming" until they launch.

## Show notes (website and longer feed notes)

```
[Title]
Walk Steadfast, Episode [#] · [Month D, YYYY]

[About 150 words from the episode's reading narrative.]

Chapters
00:00 [Title]
MM:SS [Title]
...

Scripture
[Reference (NIV), with the verse text quoted word for word]

This week's challenge
[Full text]

Mentioned
[Items]

walksteadfast.com · @steadfastwalk

[Biblica notice]

Produced with AI voice and video tools.
```

## Chapters

Take the times from the final audio, not from the script estimate. Start at 00:00. Use at least three chapters, each 10 s or longer.

| Start | Title |
|---|---|
| 00:00 | |
| | |

`chapters.json` format (podcast namespace):

```json
{
  "version": "1.2.0",
  "chapters": [
    {"startTime": 0, "title": "Cold open"},
    {"startTime": 32.5, "title": "Pull up a chair"}
  ]
}
```

## Standard links

| Where | Link |
|---|---|
| Website | https://walksteadfast.com |
| Instagram | https://instagram.com/steadfastwalk |
| X | https://x.com/steadfastwalk |
| Facebook | https://facebook.com/steadfastwalk |
| TikTok | https://tiktok.com/@steadfastwalk |
| Reddit | https://reddit.com/user/steadfastwalk |
| LinkedIn | https://linkedin.com/company/steadfastwalk |

Handle on air and in copy is @steadfastwalk. The website is walksteadfast.com.

## Pre-upload checklist

- [ ] MP3 measures -16.0 LUFS (plus or minus 1) and true peak at or below -1.0 dBTP
- [ ] No gap over 2 s, no clipping
- [ ] Every script line present, names spelled right in the transcript
- [ ] Title has no episode number and no show name
- [ ] Explicit set to false
- [ ] Chapters checked against the audio by ear at each start time
- [ ] Biblica notice present when NIV is quoted
- [ ] GUID set and recorded here
- [ ] Credits: Wes's spoken line "Produced with AI voice and video tools." is in the audio right after the closing music, at normal credits volume
- [ ] Description and show notes end with "Produced with AI voice and video tools."
