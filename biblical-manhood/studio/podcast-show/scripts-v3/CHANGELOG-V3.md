# Podcast v3 changelog

Overrides and deliberate departures from SHOW-BIBLE.md and the v1 drafts in scripts/, logged per Aaron's v3 brief. The v1 files, SHOW-BIBLE.md and _build/intros_data.py are not edited. Each batch adds its own section. Other batch branches create this same file, so when the branches merge, keep every batch section.

## Batch E065-E072 (branch podcast-v3-e065-e072)

### Length overrides

SHOW-BIBLE section 4a sets mains at 25-35 minutes (about 3,600-5,000 spoken words), and section 4b sets Field Notes at about 14 minutes. The v3 brief replaces both windows: mains run 45-60 minutes (7,000-9,000 words) and Field Notes run 20-25 minutes (3,000-3,800 words). Every episode in this batch runs past the old limit on purpose. The bible's chapter clock is scaled to the longer run, and the order of the beats is unchanged.

| Episode | Old window | v3 length (timing.py) | Spoken words |
|---|---|---|---|
| E065 The Bed Is a Covenant | 25-35 min | 48:48 | 7,407 |
| E066 Field Notes: Covenant Check | about 14 min | 24:57 | 3,761 |
| E067 When Marriage Feels Like Roommates | 25-35 min | 48:08 | 7,266 |
| E068 Field Notes: Roommates No More | about 14 min | 22:05 | 3,331 |
| E069 You Were Made for a Work | 25-35 min | 47:55 | 7,254 |
| E070 Field Notes: Labor Day | about 14 min | 23:59 | 3,630 |
| E071 What You Build When Nobody Claps | 25-35 min | 46:45 | 7,089 |
| E072 Field Notes: The Unseen Shift | about 14 min | 22:19 | 3,361 |

### Open line reworded in the script only

- **E072.** Jonathon's fact line in _build/intros_data.py is "I learned the school custodian's name this week." The brief bans "this week," so the v3 script reads "I learned the school custodian's name on Wednesday." intros_data.py is not edited. **Recommendation:** make the same change in intros_data.py so the rendered open matches the script.

The other seven opens are read verbatim from intros_data.py.

### Wording changes across the batch

- **"This week" and "weekend"** are gone from every spoken line, chapter title and on-screen text. Challenges say "before Friday," "between now and Tuesday" or name the day. "Labor Day week" (E069) is a holiday name, not the banned phrase, and lint passes it.
- **Plugs are present tense.** E069 (book chapter 30) and E071 (book chapter 33) said the book was "coming" in v1. Both now say it's at walksteadfast.com, and E071's description line drops "coming." E065 and E067 already used present tense.
- **Mid-sentence colons and dashes** are removed from spoken lines. The one colon lint sees in E066 is a clock time inside a text message read aloud ("Thursday, 7:20").
- **Handoffs.** Long Wes runs were broken with Jonathon questions and reactions so no Wes run passes about 120 words. The one exception is in E070 (134 words), where Wes reads his oldest son's text aloud; splitting a read-aloud text would break it.
- **Cross-episode repeats.** A scan of six-word phrases across the eight scripts turned up stacked repeats. The later uses were reworded in E067, E068, E069, E070, E071 and E072. The repeats left are intentional: the locked opens, the slate, the credits line, the standing chapter phrases and canon quotes used as callbacks.
- **Standing outros** keep the rotation: E065 B, E067 C, E069 D, E071 E; E066 F1, E068 F2, E070 F3, E072 F4.

### Single checks

SHOW-BIBLE "the single check" gives each Field Notes one text from a younger man. v1 did not have them in this stretch. Added in v3:

- **E066.** Wes's oldest son (the phone on the dresser, a man from the apprentice class).
- **E068.** Jonathon's nephew (the high-school friend he only texts about the Astros).
- **E070.** Wes's oldest son (a crew member's truck repossessed, the forty-minute drive the wrong way). The nephew rests.
- **E072.** Jonathon's nephew (staples behind the drywall, "the extra syrup boy").

### Continuity fixes

- **E065, welcome line** (SHOW-BIBLE section 14, item 18). The v1 welcome repeated the hook's words. The v3 first line after the slate shares no content word with the hook.
- **E071, Jonathon's age.** v1 had "I'm thirty-seven." He is 36 until his February birthday (SHOW-BIBLE, the facts), so the line is now "thirty-six."
- **Fact tics.** One recurring "twenty-seven years" count was cut, and a line that put Wes's father in his "seventies" now says "late" in life, so it can't contradict his age in the host file.
- **Wes's index card.** Any mention of the card respects canon: the back already holds his prayer names and his heading. E072's new secret list is a separate small notebook kept beside the card.

### Narrow fixes after the batch

- **E066, length.** About 105 spoken words of filler cut to bring it from 25.1 to 24.4 minutes at 150 wpm (24:15 by `_build/timing.py`). Cuts are repeats and throwaway lines only: the second recap of Tuesday's challenge (the "no Friday deadline" line stays), "Same garage feeling," "Which is fair," Jonathon echoing "Grown kids," Wes's "That's a good word for him," "For Austin's daughter in particular," and similar. Chapter times regenerated.
- **E070, Wes runs.** Two Jonathon lines added, "Read it how he wrote it. I'm ready." before the oldest son's text, and "Your dad had the fence. He's got the mailbox. What do you tell him?" after the fence story. No new facts. One Jonathon filler sentence cut ("I've been waiting since Tuesday to hear about it.") to keep his share under 50%. Longest Wes run 134 to 106. Chapter times regenerated.
