# Podcast v3 changelog

Changes from the v1 scripts in scripts/ to the v3 rewrites in scripts-v3/, logged per batch. The v1 files are untouched.

## Batch E073-E080 (branch podcast-v3-e073-e080)

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides SHOW-BIBLE section 4a (main length), section 4b (Field Notes length), and the section 5 clock tables with their minute marks for the report, From the Table and the tool. Those minute marks no longer apply to the v3 scripts, but the rule that no chapter runs six minutes without a turn still does. Each v1 header also carried its own length ("About 25-26 min" or "About 13-14 min"), and the v3 header now says "v3 length (45-60 min)" or "v3 length (20-25 min)."

| Episode | v1 length (header) | v3 length (timing.py) | Override |
|---|---|---|---|
| E073 Feelings Are the Dash, Not the Wheel | about 25-26 min | 53:02 | 4a, the section 5 main clock, the v1 header |
| E074 Field Notes: Dash and Wheel | about 13-14 min | 23:56 | 4b, the section 5 Field Notes clock, the v1 header |
| E075 Every Season Still Counts | about 25-26 min | 46:55 | 4a, the section 5 main clock, the v1 header |
| E076 Field Notes: Season Swap | about 13-14 min | 21:14 | 4b, the section 5 Field Notes clock, the v1 header |
| E077 When the Job Goes Away | about 25-26 min | 46:48 | 4a, the section 5 main clock, the v1 header |
| E078 Field Notes: Between Jobs | about 13-14 min | 24:28 | 4b, the section 5 Field Notes clock, the v1 header |
| E079 Grief at the Table | about 25-26 min | 46:41 | 4a, the section 5 main clock, the v1 header |
| E080 Field Notes: Grief Report | about 13-14 min | 22:30 | 4b, the section 5 Field Notes clock, the v1 header |

The extra time comes from added chapters, deeper work on each passage, stories from both hosts, real push-back from Jonathon, hard cases and banter. Each episode's "New continuity (v3 additions to v1)" header row lists what was added.

### Rule fixes applied in every script

- **Plugs are present tense.** E075's book plug (chapter 32) and E079's training plug (session 13, A Man With No Brothers) said "it's coming" in v1. v3 says each is at walksteadfast.com, with no "coming," dates or prices. The YouTube descriptions match. No other episode in the batch carries a plug, and Field Notes never do.
- **"This week's challenge" is now "The challenge."** The chapter marker, the on-screen text, the spoken line, the description and the reading narrative are all retitled. "This week" is gone from every script, and so is "week 1."
- **The open stage note says "each episode."** v1 read "Same beats every week, new words." v3 reads "Same beats each episode, new words."
- **Training is never called a "week."** Sessions are named by number and title.
- **No date in the reading-narrative subtitle.** v1 read "### Walk Steadfast, [date], Episode NN." v3 reads "### Walk Steadfast, Episode NN." Release dates stay in the header table, which isn't read on air.
- **The credits line appears only in the credits slot,** exactly "Produced with AI voice and video tools." There's no other AI mention anywhere.
- **Wardrobe matches production/WARDROBE.md.** The v1 headers for E074 through E080 listed shirts that differ from WARDROBE.md. v3 uses the WARDROBE.md entries, and each header names the source.
- **YouTube chapter timestamps** come from _build/timing.py on the v3 text, applied with _build/apply_chapters.py.

### Content changes beyond length

- **E073's divorced caller** was a dad at a custody drop-off in v1. That repeated E074's Austin, so v3 makes him a dad whose kids talk about their stepdad at supper.
- **E076 Mr. Abernathy order.** v3 has him go first, then leave the asking to Wes (the gas receipt and the nineteen days, canon E039). His saying is paraphrased, not quoted.
- **E077 scholarship.** Wes's father's A&M scholarship was already told on air in E029 and E053. v3 treats it as known and never calls it a first telling.
- **E079 barn line.** A line saying Wes had never said a barn memory out loud was cut, because E053 already put it on air.
- **E080 installer call.** v1 implied the answer came "today." v3 says the north-side outfit will call by Friday, which puts it after the episode records.
- **Jonathon's canon** was checked against hosts/JONATHON-CHARACTER.md wherever v3 adds his stories: married ten years to Dani, the men's breakfast at twenty-nine, most Thursdays with Wes for seven years.
- **"Sir"** appears once in the batch, from E077's caller.
- **Rotations.** Dani is quoted in alternate episodes only (E076 and E079 quote her; E077 doesn't quote her; E078 and E080 report what she did without quoting her). Wes's deadpan "K" beat appears once (E073). The motive audit runs in E075 and E077 only. Wes's knee and age beat appears in E073 (the rain it keeps predicting), E075 and E079 (his mother counting his PT reps).

### Note for whoever merges

This file was created on this branch. The E025-E032 batch created its own scripts-v3/CHANGELOG-V3.md on podcast-v3-e025-e032, so the two branches will conflict on this file at merge. The fix is to keep both batch sections under the one title.
