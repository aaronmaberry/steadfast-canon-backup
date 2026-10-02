# Questions for Aaron

**Status: every question is answered (2026-10-01).** A later correction from Aaron the same day supersedes question 9: W01-W24 are live training sessions, not YouTube episodes, and S01-S04 are shelved in `_shelved/lectures-S01-S04/`. Below each question are Aaron's answer and what was done about it. The re-check results are in `ACCURACY-PASS.md` under "Aaron's answers (2026-10-01), applied and re-checked". The per-script changes are in `CHANGE-REPORT.md` under "Aaron's answers (2026-10-01), applied".

## Decided (recorded here as asked)

1. **W01 uses Luke 6:47-48, not Matthew 7:24.** The book cites Matthew 7:24 for the house on the rock. Spoken, that's "Matthew seven, verse twenty-four", which the brief bans. Luke's parallel teaches the same thing (hearing plus doing, a foundation tested by the flood), and its "dug down deep" is what the section teaches from. You said keep Luke.
2. **The S02 wallet man is Hank.** Not Ray (chapter 27's Ray) and not Dale (chapter 13's Dale). `meta/tools/lint.py` fails any script that says Ray or Dale, fails any script other than S02 that says Hank, and fails S02 if it loses the Hank wallet story.
3. **Strict first-person rule.** Wes's own life is only his wife, kids, wedding and baptism. Every other story belongs to a man Wes knows.
4. **W and S stay two separate sets.** They share no story, man, image, joke, opener, closer or 6-word string.
5. **The creed** appears in W03 twice, S03 twice and W07 once, and nowhere else. The one optional extra use wasn't taken.

## Answered questions

### 1. Hank's two lines: do they fit the S02 workbook? (ANSWERED)
**Aaron:** The two lines are supposed to contradict each other. Frame them clearly as two orders that fight, not as a mistake, using "never going to shake hands" or close to it. Workbook question 5 reads: "Hank's scrap: Two lines that were never going to shake hands. If you wrote your two lines on a scrap of paper, what would they say?"

**Done:**
- The S02 "Hank's Scrap" section now calls them "Two orders" and says: "Those two lines were never going to shake hands."
- It also says plainly that "Neither line was a mistake. Both were real orders, pulling opposite ways," and that the fight "got handed to him".
- The table question follows the workbook's wording: "If you wrote two lines on a scrap of paper, two orders about being a man that won't shake hands, what would they say?"
- Lint now fails S02 if it loses "never going to shake hands".

### 2. Book examples the drafts reused, and W01 (ANSWERED)
**Aaron:** Rewrite all the remaining book material in W01, the same way as the other 27. Section 1, "Come On In", is locked and approved as recorded, so leave every word of it alone, ellipses included. Make sure W02's recap still matches.

**Done:**
- W01 sections 2-11 were rewritten with new pictures and wording, and they keep the same teaching, verses and order. A was/now table is in `ACCURACY-PASS.md` under W01.
- Section 1 is byte-identical to the approved version, including its pause values.
- The 7-word book-overlap scan for W01 now finds a single 8-word span, which is the end of Luke 16:10 running into the section title "Very Little". Nothing is in section 1.
- W02's recap example was changed to match the new W01 small moves (hauling the trash cans up the driveway).

### 3. Light first-person lines that the strict rule allows (ANSWERED)
**Aaron:** Keep the wife, kids, wedding and baptism lines in first person, but give them a tone check and fix anything bragging, preachy or self-pitying. Remove or rework W01's Monday-intentions line and its "in a minute" (meaning an hour) line.

**Done:**
- **S01:** checked, and no change was needed. The S01 script is unchanged since b7e8361 and ready to record (commit ff350ea).
- **W06:** checked, and no change was needed.
- **W19:** the kitchen line no longer reads as self-congratulating. It is now "Some nights it takes me a good deal longer than two seconds."
- **W20:** the bedtime line no longer reads as self-pity. It is now "There are evenings I just don't feel it."
- **W01:** both habit-level lines are gone.
  - The Monday line is now about men in general: "A man can plan to start over on a Monday for twenty years running."
  - The "in a minute" line was cut.

### 4. Should W01-W04 and S01-S04 become one set? (ANSWERED)
**Aaron:** Keep them separate. Nothing was changed.

### 5. Chapters 25-35 have no training sessions (ANSWERED)
**Aaron:** No W25+ set. Nothing was changed.

### 6. Verse choices to confirm (ANSWERED)
**Aaron:** All substitutions are confirmed. Nothing was changed.

| Script | Verse used | Why |
|---|---|---|
| W07 | Ephesians 2:8-9 | Not 2:8-10, because W20 uses 2:10. |
| W08 | Ephesians 6:4 | Taken from the chapter 26 audit rows. |
| W12 | Ephesians 5:31 | Taken from the chapter 25 audit rows. Chapter 12's Genesis 2:24 would be spoken "verse twenty-four". |
| W11 | 1 Kings 2:2-3 | The quote stops at "wherever you go"; every word is exact. |
| W02 | Psalm 103:14 | Taken from the chapter 31 audit rows. |
| W23 | Philippians 2:6-7 | Not 2:5-7, because W03 uses 2:5. |
| W01 | Luke 6:47-48 | See decided item 1. |
| W14 | Proverbs 13:20 | Not in the audit; checked on Bible Gateway's NIV 2011. |

### 7. Pause technique and ellipses (ANSWERED)
**Aaron:** Keep the ellipses.

**Done:** The ellipses are kept, and the lint limits are unchanged: at most 1 mid-line per section, at most 2 of any kind per section, and at most 4 per script. The fallback in `PAUSE-TECHNIQUES.md` (change "..." to a comma) stays documented but unused.

### 8. A Bible name on a present-day man (ANSWERED)
**Aaron:** Rename Philip to Ike everywhere, and add the name to lint.

**Done:**
- S02's breakfast man is now Ike throughout.
- Lint now fails any script other than W10 that says "Philip" (in W10 he is the apostle of John 14:9).
- Lint also fails any script other than S02 that says "Ike".

### 9. Recaps that mention the room's response (ANSWERED)
**Aaron:** Cut them from the YouTube W episodes and rephrase toward the viewer. The S lectures keep theirs.

**Done:**
- The recaps in W02-W15 and W19-W24 now speak to the viewer, for example "Maybe you…" and "If you tried it…". They no longer report how the room or the group did.
- W16-W18 already spoke to the viewer.
- A few section-1 openers got a short viewer-facing line, so they stay at or above 1,500 characters.
- S01-S04 keep their room recaps.

**Superseded by Aaron's correction (2026-10-01):** that instruction was wrong. W01-W24 are the 24 weekly training sessions, taught live to a room of men in an auditorium. The W02-W24 recaps speak to the men in the room again: W02-W15 and W19-W24 are restored from before the viewer change, and W16-W18 each gained a room line. W14's "subscribe to the wise" is now "nod along with the wise", and lint fails "viewer", "subscribe" and "YouTube" in W scripts. S01-S04 are shelved, unedited. See `CHANGE-REPORT.md`, "Correction from Aaron".
