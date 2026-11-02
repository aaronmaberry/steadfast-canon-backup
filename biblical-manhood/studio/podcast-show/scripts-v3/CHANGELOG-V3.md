# Podcast v3 changelog

Changes from the v1 scripts in scripts/ to the v3 scripts in scripts-v3/, logged per batch. The v1 files are untouched.

## Batch E089-E096 (branch podcast-v3-e089-e096)

E089-E096 had no v1 drafts. All eight are new scripts written to the v3 brief, from CALENDAR-104 rows, SHOW-BIBLE section 15 (seasons, threads, the payoff map) and the E073-E080 drafts and continuity rows for the threads running in.

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides SHOW-BIBLE section 4a (main, 25-35 minutes), section 4b (Field Notes, 12-16 minutes) and the minute marks in the section 4d clock. The rule that no chapter runs six minutes without a turn still applies. Each header's Format row says "v3 length" and points here.

| Episode | Old window (bible) | v3 length (timing.py) | Override |
|---|---|---|---|
| E089 Men Who Served | 25-35 min (4a) | 48:24 | 4a, the 4d main clock |
| E090 Field Notes: Veterans Day | 12-16 min (4b) | 24:47 | 4b, the 4d Field Notes clock |
| E091 Gratitude Out Loud | 25-35 min (4a) | 47:27 | 4a, the 4d main clock |
| E092 Field Notes: Thank-You Report | 12-16 min (4b) | 22:28 | 4b, the 4d Field Notes clock |
| E093 Lead the Thanksgiving Table | 25-35 min (4a) | 51:23 | 4a, the 4d main clock |
| E094 Field Notes: Black Friday | 12-16 min (4b), and section 15 asks for a light episode with a three-minute review | 23:01 | 4b, the 4d Field Notes clock. The review itself is held to about three minutes (10:05 to 12:53), as section 15 asks. |
| E095 Joseph Said Nothing | 25-35 min (4a) | 46:49 | 4a, the 4d main clock |
| E096 Field Notes: Advent Report | 12-16 min (4b) | 21:56 | 4b, the 4d Field Notes clock |

No other length cap in the bible applies to these eight.

### Conventions applied in every script

- **Open stage note.** The DRAFT open in `_build/intros_data.py` produces a stage note that says "pending Aaron," which lint reads as an AI mention and fails. The v3 note reads "(Walk Steadfast open written for E0NN from its DRAFT entry in _build/intros_data.py, awaiting Aaron's sign-off. Facts re-checked against this script. Same beats each episode, new words. SHOW-BIBLE section 5.)" It uses "each episode" rather than "every week," to match batch E073-E080.
- **Reading-narrative subtitle has no date.** "### Walk Steadfast, Episode NN" (or "Field Notes, Episode NN"), matching batch E073-E080. Release dates stay in the header table, which isn't read on air.
- **The open lines are verbatim** from `_build/intros_data.py`. E089's open says "Veterans Day week," which is the one spoken "week" in the batch. It is the intros_data text, a calendar phrase, and not a training reference. Lint passes it.
- **Book plugs on fresh topics** (SHOW-BIBLE section 14, item 17). E093 carries chapter 6, Go first, and E095 carries chapter 4, Stop waiting. Each sits after the Word, runs under 20 seconds, is in present tense ("It's in Steadfast Men, at walksteadfast.com.") and has no dates or prices. E089 and E091 have no plug (calendar slot "-"). Field Notes never carry one.
- **Credits disclosure** appears once per script, in the credits slot only, and not in the description or the reading narrative.
- **YouTube chapter timestamps** are taken from `_build/timing.py`'s per-chapter output.

### Change to a script earlier in this batch

- **Cross-batch phrase pass.** After the six-word repeat scan, the later use of thirteen incidental phrases was reworded in E091-E096 (for example "looked at me like I'd," "in front of two hundred people," "in the driveway the whole time"). Chapter timestamps were regenerated from timing.py.
- **E091 pie line.** The first draft had Wes say he'd "never told anybody I left before the pie." The v1 continuity rows (E007, E016) already have him owning that he left early, and his brother saying "Mom made a pecan pie for you. I ate it." E091 now has Jonathon recall the pie from the winter and Wes say he apologized to his brother "in a parking lot" but never thanked him.
