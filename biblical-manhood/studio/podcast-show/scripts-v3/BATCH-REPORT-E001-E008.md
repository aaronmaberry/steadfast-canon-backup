# Batch report: v3 final scripts, E001-E008

Internal. All eight scripts are written, linted and timed. Every `lint.sh` run is clean, with 0 FAIL and 0 WARN on all eight files and the open system. Length windows follow the v3 override (`CHANGELOG-V3.md`).

## Numbers

Spoken words and beats come from `_build/lint.sh`. Minutes come from `_build/timing.py` (Wes 145 wpm, Jonathon 170). The Wes/Jonathon split counts dialogue lines outside the locked Intro chapter, so the two columns sum a little below the lint total. "Short" is the share of Jonathon's lines under 12 words.

| Ep | Type | v1 words / min | v3 words | v3 min | Wes | Jonathon | J share | J short | Beats | Lint |
|---|---|---|---|---|---|---|---|---|---|---|
| E001 | Launch main | 5,544 / 38:25 | 8,295 | 56:26 | 4,371 | 3,843 | 46.8% | 17.3% | 7 / 10 | Clean |
| E002 | Field Notes | 2,118 / 14:59 | 3,511 | 23:55 | 1,812 | 1,640 | 47.5% | 17.1% | 3 / 9 | Clean |
| E003 | Main | 3,956 / 27:35 | 7,286 | 49:11 | 3,767 | 3,454 | 47.8% | 13.2% | 8 / 10 | Clean |
| E004 | Field Notes | 1,938 / 13:45 | 3,219 | 21:57 | 1,638 | 1,524 | 48.2% | 17.4% | 5 / 9 | Clean |
| E005 | Main | 3,534 / 24:39 | 8,583 | 58:03 | 4,448 | 4,069 | 47.8% | 17.0% | 9 / 10 | Clean |
| E006 | Field Notes | 1,981 / 13:49 | 3,474 | 23:37 | 1,741 | 1,673 | 49.0% | 18.9% | 4 / 9 | Clean |
| E007 | Main | 3,611 / 25:24 | 7,226 | 49:00 | 3,847 | 3,312 | 46.3% | 14.2% | 8 / 10 | Clean |
| E008 | Field Notes | 1,941 / 13:50 | 3,555 | 24:13 | 1,752 | 1,748 | 49.9% | 15.3% | 3 / 9 | Clean |

Batch total: 45,149 spoken words, about 5 hours 6 minutes. No Wes turn runs over 120 words without a handoff in any episode. Ellipses and long pauses are under their limits everywhere.

## Warnings and judgment calls

- **Lint INFO "eleven/twelve spoken"** (the round-7 number check) shows on every episode except E006. The counts are E001 5, E002 2, E003 3, E004 1, E005 2, E007 2 and E008 2. Each is a deliberate spoken number (Jonathon at eleven checking locks, "11 minutes in the lot", the 11-word prayer, Dani's twelve-hour shift and so on). None is a stray. This is INFO, not WARN.
- **E008 Jonathon share is 49.9%**, right at the 50% ceiling. The Field Notes check-in is mostly his week (the rep, Dani, the bins, Theo, the nephew). Don't add Jonathon lines in the edit without adding Wes lines too.
- **E006 short lines are 18.9%**, under the 20% ceiling with little room. Trimming Jonathon's longer lines in the edit pushes it over.
- **E001 and E005 run long** (56:26 and 58:03), inside the 45-60 window. E005 is the four-marks episode. If the cut needs air, the fake-versions chapter is the easiest to trim, and the sentence and the four marks are not.
- **Scripture.** Every NIV quote was checked word for word on BibleGateway on 2026-11-02. Philippians 2:6-8 and Ephesians 2:8-9 are paraphrased only in E005, because the NIV text uses em dashes.
- **Plugs** follow the calendar slot. E001 is FULL, E003 is B (book, chapter 2), E007 is T (training, session 4), and the rest have none. Every plug is present tense, with no dates, prices or results.
- **Outros** follow the rotation: E001 launch, E002 F1, E003 A, E004 F2, E005 B, E006 F3, E007 C, E008 F4. The credits line is last in every script and is the only AI mention.
- **On-mic show references** are one or fewer per episode. E001's is the plug intro ("This is the one episode where we lay out everything that exists").
- **988 line.** None of these eight is a mental-health episode, so it doesn't appear.
- **Chapter stamps** in each YouTube description come from `apply_chapters.py`. Confirm them against the cut.

## Continuity assumptions

These are assumptions the batch leans on. Each script's header has the full list.

- The gutter stays loose from E004 to E014. Wes never calls the carpenter in this batch.
- Wes's wife has driven Mom to PT most Tuesdays since August, and Wes has done two.
- Mr. Abernathy's regular question is "What'd you do since last time?" "What are you waiting on?" was a one-time question.
- Jonathon is 36, with a February birthday. Dani is a night-shift nurse. Ruby gets a dog (Pancake) after Theo turns five, in August.
- Wes's brothers are never named. The older is 58 and runs their late dad's place. The younger is 47 and lives in Fort Worth.
- Wes and his wife don't pray together out loud yet (seeded in E002, named in E006, unresolved).
- Jonathon's dad's friend request from Christmas Day is still pending. Jonathon hasn't set a date to decide.
- Wes's job is never named on air (a running gag).

## Continuity by episode

| Ep | Pays off | Sets up or leaves open |
|---|---|---|
| E001 | (launch) | Mr. Abernathy and his questions. Dad's "I'm proud of you" at 43. The first-breakfast "What are you waiting on?" Jonathon's upside column. The big-days disagreement, logged for E047 or E051. |
| E002 | E001's challenge. Wes takes Mom to PT. | The 11-word prayer. Truck prayers. "A piece of this I still haven't gotten right" (pays off E006). The basket rule. |
| E003 | E002's check | "Win the room" on the receipt and the visor. "Pay the bills and don't make trouble." The bread basket by the garage door. Jonathon's "be a man about it." Theo's "What's a man?" |
| E004 | E003's sentence test | The gutter isn't fixed, the fascia is rotten (runs to E014). The call to the brother since Thanksgiving (pays off E007 and E008). "It's not done. It's started." |
| E005 | E004's gutter (still hanging) | The sentence said once, the four marks, the fake versions. The carpenter's sticky note. Mom's Tuesdays (feeds E007). The Christmas money to the little brother. The Converse AC call. |
| E006 | E005's challenge. The praying piece named. | "CALL" in red on the sticky note. The son-in-law's grant. Dani's "on your dad." The friend request. The driveway prayer before Dani's shifts. |
| E007 | E006's "on your dad." The brothers. | The older-brother call, Wednesday at 7. The rep review Thursday at 10. Pancake on the calendar. The October fight. The rehearsal. The tired man, handed to E008. |
| E008 | E007's call, review, rehearsal and Theo | Feb 3 knee appointment (E010 check). Feb 7 talk with Dani (E012). Feb 9 Mom's doctor (E011 or E012). Jonathon's date to decide (Wes asks "in a couple of weeks"). The knees and the gutter, deferred to E014. Tuesday's tease is Pick up the weight (E009). |

## Unfinished

Nothing in the brief is left undone. Two items fall outside it. The show bible's length lines are not updated (see `CHANGELOG-V3.md`), and `STATUS.md` doesn't mention `scripts-v3/` yet. Both were left alone because the brief said not to edit existing files.
