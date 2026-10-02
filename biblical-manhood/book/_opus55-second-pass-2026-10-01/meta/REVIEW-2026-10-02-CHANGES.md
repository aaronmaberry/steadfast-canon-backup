# Review changes, 2026-10-02 (Aaron approved 7:42 AM CT)

Backup of the manuscript and binder before these changes:
`/workspace/backups/pre-apply-2026-10-02/`

## Applied

1. **Section headings, whole book (binder `book/tools/make_ebook_pdf.py`).**
   - New: Libre Franklin Medium, 11 pt for h2 and 10.5 pt for h3, on 14/13 pt leading.
   - Space above is 7/5 pt and below is 3/2 pt.
   - Color is still NAVY, the accent color.
   - Was: Libre Franklin Bold, 11.5/16 and 10.5/14, with 10/6 and 7/4 pt above and below.
   - Every in-text heading goes through `heading()`, which covers the Introduction, all 35 chapters, About the Author and Condensed Training.
   - Added a keep-with-next rule, so a heading never sits alone at the bottom of a page.
2. **Chapter 2 "You Are Not Crazy": new opening.**
   - It now opens on men in general and three reasons they can't see clearly: crossed instructions, no older man to draw them a picture, and shame that keeps them quiet. Then "You're not crazy."
   - The diner man is now "a man I'll call Garrett", in his own section ("Counting on his fingers").
   - "I learned the costume changes young" became "I know the costume changes", for pen-name safety.
   - Everything from "Six maps" on is unchanged, including the NIV block.
3. **Chapter 1 "A Quiet Tuesday": flare passage replaced with Option A, "Markers aren't miles".**
   - It carries on the mile-marker image from the paragraph above it.
   - "Big days have one more problem…" is unchanged.
4. **Blank pages: no change.** Every opener still starts on a right-hand page (the binder default; `STEADFAST_OPEN_ANY` is unset).

## Pre-apply error check on the Chapter 2 rewrite

Opus 5.5 was not reachable from the session that did this work: the box's CLI offers Grok models only, and the earlier Opus passes ran in cloud agents. The check was done by hand plus these tools:

- **Read-through** for typos, grammar, tense and logic.
- **Scripture:** Genesis 1:27 NIV matches exactly (niv_verify). The "built on sand" echo is consistent with Matt 7:24 in Ch1.
- **Continuity:**
  - Ch1 closes on "You're not imagining it. You Are Not Crazy comes next", and Ch2 now opens there.
  - Ch2 "Next chapter you'll set another line beside it" and "It fits in a sentence" lead into Ch3's one-sentence answer.
  - Ch3 "spread the maps out" still points back to the six maps.
  - The bold cross-reference "The Empty Chair" matches the Ch8 title.
- **Style:** no em or en dashes; no "real man", Lewis, knight, weeknight, "Better Man" or "God's reward"; no creed in Ch2 (sweep: 0 hits); capital He/His for God, consistent with Ch1 to Ch4.
- **Pen name:** the only first person is habit-level self-owns. Garrett's story is third person. "Wes"/"Hart" don't appear in the chapter text.
- **Spelling (pyspellchecker):** the only flags were grandkids, ICU, NIV and whoever's, all correct.

Result: no real errors found, so no fixes were made beyond the approved text.

## Checks after apply

- `checks.py sweep`, whole book: 5 hits, all on the locked copyright acknowledgment (the allowed exception), the same as before.
- niv_verify: 158 blocks (132 EXACT, 17 EXACT-EDGE-DROP, 9 EXCERPT-OK), 0 mismatches.
- `build_local_print.py --strict`: 238 pages, 0 FAIL, 0 WARN; locked front cover sha check passed.
- PDF: `Steadfast Men - Review Print - 2026-10-02.pdf`, sha256 `871fb7d0…eeb7f`.

## Opus 5.5 proofread, ch1 and ch2 (applied 2026-10-02, approved by Aaron)

Source: cloud-agent-artifacts/bc-54962b95.../opus-check-ch1-ch2.md. Backup: /workspace/backups/pre-opus-proof-2026-10-02/.

Chapter 1 (01-a-quiet-tuesday.md)
- E1: "ten thousand Tuesdays" became "every Tuesday until she leaves home".
- S1: "each one under two minutes" became "each choice over in a few seconds".
- S2: "He tells a story about two houses, too." became "Jesus tells a story about two houses, too."
- S3: "whether he made that call, kept that drawer shut, told that small truth" became "whether a man made the call, kept the drawer shut, told the small truth".
- S4: "Pick up when he calls." became "Pick up the call you'd usually let ring out."
- S5: "Never in a meeting, never out loud." became "He never decided it in a meeting, never out loud."

Chapter 2 (02-you-are-not-crazy.md)
- E1: Chapter 3 opener (03-the-four-marks.md) now spreads the maps on the table, with no hood or parking lot.
- S1: the push line now reads "I was told the push inside me to build and lead was a threat ... and then I was told sitting on it was why home felt like a cold room."
- S2: "Once you see which ones were never real maps, you can stop following them."
- S3: "and never admitted it had talked them out of all three."
- S4: "If you don't have a good answer, write the one you've actually been living, even if it's a poor one."
- O2: "a man on a tailgate".
- O3: "the bruises of each".

Introduction (00-introduction.md)
- "twenty-four-week training" became "twenty-four-session training", and "a short map of those weeks" became "a short map of those sessions".

Checks: sweep 5 hits (copyright L28 only), no dashes or banned words, NIV 158 blocks (132 EXACT, 17 EXACT-EDGE-DROP, 9 EXCERPT-OK, 0 mismatches), strict build 238 pages, FAIL 0, WARN 0, cover locked.
PDF: sha256 `9159460217164fe3…60a51cf`, uploaded to Drive as id 1B85xvTqAWncp6abviJUSHy7OLtPYWdAP (private). The old file 1tiarb4FMBpS6d8ddjz84ZdQdkTCxZrvL was trashed.
