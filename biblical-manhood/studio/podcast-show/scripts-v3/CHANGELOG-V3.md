# Podcast v3 changelog

Changes from the v1 scripts in scripts/ to the v3 rewrites in scripts-v3/, logged per batch. The v1 files are untouched.

## Batch E025-E032 (branch podcast-v3-e025-e032)

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides SHOW-BIBLE section 4a (mains 25 to 35 minutes, about 3,600 to 5,000 words), section 4b (Field Notes 12 to 16 minutes, about 1,900 to 2,500 words), and the section 5 clock tables (main about 26 minutes, Field Notes about 14 minutes, with their minute marks for the report, From the Table and the tool). Those minute marks no longer apply to the v3 scripts, but the rule that no chapter runs six minutes without a turn still does.

| Episode | v1 length (header) | v3 length (timing.py) | Override |
|---|---|---|---|
| E025 The Father Who Stays | about 27 min | 53:32 | 4a and the section 5 main clock |
| E026 Field Notes: Easter Week Report | about 15 min | 22:45 | 4b and the section 5 Field Notes clock |
| E027 The Empty Chair at Your Table | about 27 min | 49:24 | 4a and the section 5 main clock |
| E028 Field Notes: The Chair Report | about 15 min | 22:45 | 4b and the section 5 Field Notes clock |
| E029 When Your Dad Is Still Alive | about 28 min | 50:11 | 4a and the section 5 main clock |
| E030 Field Notes: Calling Him Back | about 14 min | 22:04 | 4b and the section 5 Field Notes clock |
| E031 When Home Never Handed You Off | about 26 min | 47:37 | 4a and the section 5 main clock |
| E032 Field Notes: Cutting the String | about 13 min | 22:10 | 4b and the section 5 Field Notes clock |

The extra time comes from added chapters, deeper work on each passage, stories from both hosts, real push-back from Jonathon, hard cases, and banter. No chapter is padding. Each episode's production notes list what was added under "v3 length."

### Rule fixes applied in every script

- **Plugs are present tense.** The v1 plug lines said a book chapter or training session was "coming" or "comes out this week." v3 says it's at walksteadfast.com, with no "coming," "out now," dates or prices. The YouTube descriptions match. Plugs appear only in E025 (book), E027 (book) and E031 (training session 11). E029 has none, and Field Notes never carry one.
- **"This week's challenge" is now "The challenge."** The chapter marker, the on-screen text and the spoken line are retitled. "This week" is gone from every spoken line except one locked open (see below). Descriptions and reading narratives say "The challenge" too.
- **The open stage note says "each episode."** v1 read "Same beats every week, new words." v3 reads "Same beats each episode, new words." That clears lint's legacy-intro check without the word "week."
- **Training is never called a "week."** Sessions are named by number and title (session 8, session 11).
- **"Weekend" is out of the scripts.** In E031 the canon line "And don't come home every weekend" is now "And don't come home every Friday." Flagged in the batch report.
- **No date in the open or the reading-narrative subtitle.** The v1 reading narratives carried a date under the episode title, and v3 drops it. Release dates stay in the header table, which isn't read on air.
- **The credits line appears only in the credits slot,** exactly "Produced with AI voice and video tools." There's no other AI mention anywhere.
- **YouTube chapter timestamps** come from _build/timing.py on the v3 text.

### Locked text left as is

- **E032's open** (from _build/intros_data.py) says "Friday we report, two parts this week." Opens are locked, so it stays verbatim. Aaron decides whether to change it in intros_data.py.
- **E029's open** says "Twice a week, following Jesus as a man." That's the show's schedule, not a training reference, and lint passes it.
