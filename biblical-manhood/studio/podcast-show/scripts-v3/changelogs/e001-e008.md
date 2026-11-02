# CHANGELOG-V3: final scripts, E001-E008

Internal. The v3 folder holds the final scripts for E001-E008. They are rewrites of the first drafts in `scripts/`, which stay untouched. Aaron's direction for v3: drill deeper into the canon topics, and give the two hosts more banter, chemistry, real disagreement, stories, callbacks and running threads.

## Length windows overridden

v3 scripts run longer than the show bible allows, on purpose. These lines in `SHOW-BIBLE.md` do not apply to `scripts-v3/`:

| Where | What it says | v3 target |
|---|---|---|
| Section 2, line 37 | "Every episode is tight, 25-35 minutes" | Mains 45-60 min, Field Notes 20-25 min |
| 4a, line 56 | Main episode 25-35 minutes, about 3,600-5,000 spoken words | 45-60 min, about 7,000-9,000 words |
| 4b, line 75 | Field Notes 12-16 minutes, about 1,900-2,500 words | 20-25 min, about 3,000-3,800 words |
| 4c, line 90 | E001 launch episode about 40-45 minutes | Same as any main: 45-60 min |
| Line 260 | "Plan mains for 3,700+ spoken words" | Plan mains for 7,000+ |
| Line 333 | "Field Notes run 13:50-14:30" | Field Notes run 20:00-25:00 |

Timing is still estimated by `_build/timing.py` at 145 wpm for Wes and 170 for Jonathon, and chapter stamps come from `_build/apply_chapters.py`. Nothing in `_build/` was changed. `lint.sh` has no length check, so the overrides needed no tooling change. The bible itself is unedited. If v3 becomes the house length, update those six lines.

## Rules added for v3

- Jonathon carries 35-50% of the spoken words. Under 20% of his lines are under 12 words. No Wes turn runs past about 120 words without a handoff.
- In every main, Jonathon pushes back for real at least once and brings two stories of his own.
- Jonathon sounds like a sales manager from the Houston suburbs, never country.
- At most one on-mic reference to the show per episode.
- No phrase reused across the batch, except deliberate callbacks named on air and the fixed lines (the open, the slate, the standing outros, the credits).

## Deliberate continuity changes from v1

These are the places where v3 departs from a first-draft fact. Everything else in v1 holds, and each script's header lists what it adds.

- **The gutter is not fixed (E004 v3 onward).** v1 E004 has it fixed on Saturday. In v3 the two men find the fascia board behind it rotten ("That's a carpentry job, not a gutter job"). The carpenter's name goes on a sticky note on the fridge (E005). Wes's wife writes "CALL" on it in red (E006). Jonathon connects it to Wes's knees, and Wes defers ("That's a different Friday," E008). This keeps canon with E014 (the gutter at 15 months) and E018. Wes's real reason (the knees, the ladder, not wanting to pay a man for something he could do at forty) is held for E014.
- **Mom's Tuesdays (E005 v3 onward).** Wes's wife has driven his mother to PT most Tuesdays since August, and Wes has done two. E002's first trip stands. This gives the older brother's "You've always let me handle Mom" something to land on in E007.
- **Mr. Abernathy's question (E001 and E007 v3).** His every-visit question stays "What'd you do since last time?" "What are you waiting on?" is the question he asked once, after Wes's dad died, and the one Wes borrowed for his first breakfast with Jonathon.
- **Jonathon's age.** He is thirty-six throughout. The v1 E003 line said 37. His birthday is in February.
- **The brothers.** The Christmas-money text in E005 goes to the little brother, so E007 can introduce both brothers fresh.
- **The tired man.** The question "How do I stop waiting when I'm genuinely tired?" comes up in E007's pushback and is handed to E008's From the table.
- **The visor card** reads "Win the room" (E003 and E005), so the late-order call in E005 lands.

## Mark ownership left for later episodes

The v3 scripts touch each mark without taking a later episode's job. E009 owns the boulder and the pack (Galatians 6:2 and 6:5). E011 owns going first and its misuse. E012 owns the first apology. E013 owns inheritance in depth. E014 owns the gutter. The steadfast sentence is said in full once per episode where it appears. Pay always means inheritance, never earning.

## Housekeeping

- Cross-batch phrase pass. Repeated tics were varied in later episodes: "on the record", "here's my problem with all of this", "I sat with a man a few years ago", "I can see it on your face", "I want to be careful, because", "Here's where I tell on myself", and "I want to push on it". On-air callbacks stay ("nine thousand notes", the cold plunge, the eggs in front of a waitress, "It's not done / not fixed. It's started.").
- The W01 training owns the driveway image, so E008's call happens "out by the barn". The W04 training owns the voicemail image, so E007 says "half a call".
