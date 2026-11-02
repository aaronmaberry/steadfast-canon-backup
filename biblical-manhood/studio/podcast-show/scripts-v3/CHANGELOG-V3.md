# Podcast v3 changelog

Changes and rule overrides for the v3 scripts in scripts-v3/, logged per batch. No existing file was edited or deleted.

## Batch E081-E088 (branch podcast-v3-e081-e088)

E081-E088 had no v1 script in scripts/. All eight were written new from CALENDAR-104.md, SHOW-BIBLE section 15 (the payoff map), the opens in _build/intros_data.py, the host files, production/WARDROBE.md, and the v1 drafts of E049-E080 for the threads running into the batch.

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides four older rules:

- SHOW-BIBLE section 1 says every episode is 25-35 minutes.
- Section 4a says mains are 25-35 minutes, about 3,600-5,000 words.
- Section 4b says Field Notes are 12-16 minutes, about 1,900-2,500 words, and the section 5 clock says about 14 minutes.
- The round 12 forward rules say Field Notes run 13:50 to 14:30 and mains run 25:00 or longer.

| Episode | Older target | v3 length (timing.py) | Override |
|---|---|---|---|
| E081 The Dark Stretch | 25-35 min (sections 1 and 4a, round 12) | 52:21 | sections 1 and 4a, round 12 main length |
| E082 Field Notes: Noticing a Brother | 12-16 min (4b), about 14 (section 5), 13:50-14:30 (round 12) | 22:35 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |
| E083 Money Tells the Truth | 25-35 min | 47:21 | sections 1 and 4a, round 12 main length |
| E084 Field Notes: The Budget Talk | 12-16 min | 21:08 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |
| E085 Paid in Full | 25-35 min | 46:53 | sections 1 and 4a, round 12 main length |
| E086 Field Notes: Season Review: The Long Road | 12-16 min | 21:18 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |
| E087 Small Ways to Serve at Home | 25-35 min | 47:06 | sections 1 and 4a, round 12 main length |
| E088 Field Notes: Serving Report | 12-16 min | 21:29 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |

The Field Notes checkpoints in section 5 (report by 1:15, a miss by 3:30, the single man's text by about 6:00, a re-orienting clause at about 6:30) are kept as written. The later checkpoints (From the Table to 10:20, the tool to 12:20) stretch in proportion to the longer runtime.

### Rule fixes applied in every script

- **"The challenge," not "This week's challenge."** The chapter marker, the on-screen text, the spoken line, the description and the reading narrative all use "The challenge." No host line in the batch says "week," "weeks" or "weekend." The one exception is the approved E085 open text (see the batch report).
- **Training named by title only.** E087's training premiere plug names the session Lay It Down, in the present tense, with no number, no "coming," no date, no price and no claim of results. E081's book plug (chapter thirty-one, Feelings Are the Dash, Not the Wheel) is also present tense.
- **The open's DRAFT note** is written by hand in each script as "(DRAFT Walk Steadfast open for E0NN, awaiting Aaron's approval. Re-check its facts against this script. SHOW-BIBLE section 5.)", and _build/intro.py was not run. Lint still WARNs on it ("open is a DRAFT pending Aaron"). Only Aaron's approval clears that WARN, and the brief doesn't allow editing intros_data.py.
- **No date in the reading-narrative subtitle.** "### Walk Steadfast, Episode NN" and "### Walk Steadfast, Field Notes, Episode NN." This matches the E073-E080 batch. Release dates stay in the header table, which isn't read on air.
- **Dollar amounts are spelled out** in spoken lines, because lint WARNs on a dollar sign followed by a digit.
- **"Napkin" and "testament"** fail lint, so they were replaced ("the back of a diner receipt," "the whole Bible").
- **YouTube chapter timestamps** come from _build/timing.py on the v3 text.
- **The credits line** appears only in the credits slot, exactly "Produced with AI voice and video tools." There's no other AI mention anywhere.
- **Wardrobe** matches production/WARDROBE.md for every episode.

### Batch-level checks

- **Phrase repeats.** I checked all host lines in E081-E088 for any six-word run that appears in two episodes, and reworded about fifty. The ones left on purpose are:
  - the mug ritual before "Carry this";
  - the 988 line (E081, E082);
  - the safe-messaging question (E081, E082);
  - a Field Notes quoting Tuesday's challenge;
  - the E051 barn promise quoted in E086 and E088;
  - the Colossians 3:24 quote (E083, E085);
  - canon labels ("the young man on my floor," "the room with nobody in it").
- **Cross-batch repeat.** E086's line from the retired rep in Corpus Christi was first written as "Took you long enough." The E073-E080 batch uses that line for Wes in E079, so E086 now reads "Four years, son."
- **Jonathon's marriage** is "ten years" throughout, per hosts/JONATHON-CHARACTER.md ("Married 10 years") and E083's spreadsheet, which started that first year.

### Note for whoever merges

This file is created on this branch. The E025-E032 and E073-E080 branches each create their own scripts-v3/CHANGELOG-V3.md, so merging will conflict on this file. The fix is to keep every batch section under the one title.
