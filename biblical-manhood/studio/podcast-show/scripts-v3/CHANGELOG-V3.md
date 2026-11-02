# Podcast v3 changelog

Overrides and deliberate departures from SHOW-BIBLE.md and the v1 drafts in scripts/, logged per Aaron's v3 brief. The v1 files, SHOW-BIBLE.md and _build/intros_data.py are not edited. Each batch adds its own section.

## Batch E049-E056 (branch podcast-v3-e049-e056)

### Length overrides

SHOW-BIBLE section 4a sets mains at 25-35 minutes (about 3,600-5,000 spoken words), and section 4b sets Field Notes at about 14 minutes. The v3 brief replaces both windows. Every episode in this batch runs past the old limit on purpose. The bible's chapter clock is scaled to the longer run, and the order of the beats is unchanged.

| Episode | Old window | v1 length (timing.py) | v3 length (timing.py) | Spoken words |
|---|---|---|---|---|
| E049 Give Your Son a Hill | 25-35 min | 25:35 | 53:43 | 8,100 |
| E050 Field Notes: The Hill Report | about 14 min | 13:52 | 22:59 | 3,441 |
| E051 A Day He Will Not Forget | 25-35 min | 25:28 | 46:39 | 6,980 |
| E052 Field Notes: Independence Day | about 14 min | 14:03 | 22:41 | 3,416 |
| E053 Before Anything Went Wrong | 25-35 min | 25:58 | 47:37 | 7,165 |
| E054 Field Notes: Work It and Keep It | about 14 min | 14:18 | 21:18 | 3,197 |
| E055 Some Saturdays | 25-35 min | 25:50 | 46:27 | 7,013 |
| E056 Field Notes: The Feeling Isn't the Fire | about 14 min | 14:16 | 20:51 | 3,118 |

E051 sits 20 words under the brief's "about 7,000" guide. Its time (46:39) is inside the 45-60 minute window, so it was not padded.

### Open lines reworded in the script only

Two opens in _build/intros_data.py carry calendar wording the brief keeps out of the scripts. The v3 script reads a reworded line. intros_data.py is not edited.

- **E052.** Jonathon's first line "This is Walk Steadfast on the holiday weekend." reads "This is Walk Steadfast, holiday edition." (The brief avoids "weekend.")
- **E053.** Wes's offer line "Through Labor Day, following Jesus as a man starts where you live." reads "All season, following Jesus as a man starts where you live." (The brief keeps dates out of the open.)

If Aaron wants intros_data.py to match, those are the two lines to change there.

### Chapter and wording changes across the batch

- **"This week's challenge" is now "The challenge"** (chapter title, description chapter list and spoken line) in E049, E051, E053 and E055, because of the "this week" ban.
- **Calendar words removed.** Every v1 "this week," "last week," "week one," "weekend" and "two weeks ago" in spoken lines, cards, pinned comments and descriptions is reworded (for example "last time," "Tuesday" or "before Friday"). The per-episode list is in each script's production notes. Training sessions are named by number or title only.
- **Mr. Abernathy's question (E053).** v1 had "What did you keep this week?" on mic, on the card and as a chapter title. v3 says "What did you keep?" everywhere. The question first aired in this episode's v1 draft, so no earlier canon changes.
- **Plug tense.** The v1 plugs in E051 (book, chapter 29), E053 (training, session eighteen) and E055 (training, session twenty) used "it's coming." All three are present tense ("It's at walksteadfast.com"), with no dates or prices.
- **Plug and sub-mid spacing.** SHOW-BIBLE section 4a lists E051, E053 and E055 among the mains whose plug sits within 30 seconds of the subscribe line. All three are separated in v3: the sub-mid sits before the Word and the plug after it, about two and a half minutes apart in E051, about five in E053 and about four and a half in E055.
- **E051 description verse.** The v1 YouTube description still named Joshua 4:6-7 after the 2026-10-03 swap. v3 names Psalm 78:4, matching the card.
- **E055 training plug** says "session twenty" without its title, because the title contains "vibe" (the episode was retitled "Some Saturdays" on 2026-10-03).
- **Standing outros** keep the rotation (E049 D, E051 E, E053 A, E055 B; E050 F1, E052 F2, E054 F3, E056 F4), each lightly reworded.

### Continuity fixes

- **Jonathon's start in sales.** v1 E053 said twenty-two. v3 says twenty-three, matching the Lorraine story in E049 v3 (first sales manager, Pasadena refinery accounts).
- **Jonathon's nephew** is twenty-two everywhere in the batch (one v3 working line said nineteen; fixed before commit).
- **Wes's flat stretches in E055** sit at "the Thursday table I sit at now," after Mr. Abernathy died, not at Mr. Abernathy's table during the fire decade.
- **"Where are we going?" in E055.** E043 gave Wes's answer as "I can do Saturday." E055 v1 gave "Home." v3 keeps both, in order: "Home," her correction, then "I can do Saturday."
