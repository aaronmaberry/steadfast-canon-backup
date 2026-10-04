# Reed gate: Grok 4.7 panel revision (Levi), 2026-09-25

**VERDICT: DIG** (one must-fix, a one-phrase fix in two new Your Turn lines. Everything else passes. Re-hand should be quick.)

Scope: `_grok47-panel-rev-2026-09-25/book/` diffed against canon `_grok47-ms/book/` (Grok 4.7 PRE-UNSLOP). Panel source: `reader-panel/grok47-bounce/PANEL-BOUNCE-GROK47-PRE-UNSLOP-2026-09-21.md`. Levi's report was read first. None of its claims were accepted without checking. I made no edits to the revision or to canon. No Unslop pass. No uploads, posts, or messages.

Coordinator steering applied:
- Aaron approved the intro edits (Name it line and time-short path) and the ch24 opener. Those were checked for mechanics only.
- Levi's two late changes (About the Author swap, ch35 second four-marks cut) have landed and were re-verified below.
- The hold is lifted. This is the final verdict.

---

## Check 1: Byte-identical claim (re-run against the current files after the late changes)

`cmp` against canon:
- **Identical:** ch01, ch02, ch03, ch04, ch06, ch08, ch10, ch11, ch32, ch33, ch34, ch37, 00-contents, 00-copyright, 00-dedication, 00-half-title, 00-title-page, wrap-back-copy. PASS.
- **Differ:** 00-introduction, 05, 07, 09, 12 to 31 (all 20 files), 35, 36. Levi's report accounts for every one of them, including the late-change log. The brief's shorter list left out ch12, 14 to 21, 23, 26, 28, 30 and 31, but those are the four-marks cut sites, and they appear in Levi's per-chapter table. No file changed without being listed.
- meta/ and style/ are identical to canon.

## Check 2: Every changed file diffed (word-diff); changes stay inside what Levi listed

| File | Change found | Matches report |
|---|---|---|
| 00-introduction | L13: time-short path extended (Quiet Tuesday and the closer each week, then Every Season Still Counts, one house chapter, one kids chapter). L35: "The first line, **Name it**, asks you..." | Yes (Aaron-approved) |
| 05 | New Tomás broke-Tuesday paragraph, L86 | Yes |
| 07 | L35 couch sentence added to the list. L87 and L124: "Wife or roommate" / "Your wife or your roommate" | Yes |
| 09 | New paragraph L90 (her anger, most of a week) | Yes |
| 12 to 31 (minus 27) | Four-marks sentence cut or bridged. Verified each bridge: 12 "All four marks are standing at this door." 17 "Hang the four marks on that string..." 19 "Come back to the four marks." 21 "passive, and a real man rejects passivity." 22 "Rejecting passivity in a marriage looks like study." 26 "The four marks, as she sees you live them..." 28 "The first mark cuts the other way here." 29 "The four marks followed, every word, in his father's voice." 30 names the fourth mark. Plain deletions in 13, 14, 15, 16, 18, 20, 23, 24, 25, 31. | Yes |
| 13 | Also a new Kenny paragraph, L86 | Yes |
| 22, 23, 24, 26, 27, 28, 29 | Your Turn branch sentences appended. Nothing deleted. | Yes |
| 24 | L9 opener: "I will give you the whole chapter in two sentences first." | Yes (Aaron-approved) |
| 25 | New Eli paragraph, L70 | Yes |
| 35 | Kenny named at L13 and L53, "It is Tuesday". Late change: the full sentence cut from the head of Carry this (L130), which now reads "Tuesday is when it will show. Get up." | Yes |
| 36 | Late change: swapped to the 9/21 shipped bio (see Check 8) | Yes |

Word counts, re-run with Levi's regex: book 67,469 to 67,899 (+430). The per-file numbers match Levi's table. Only 36 changed after his table was written (the late change). Every numbered chapter is still under 2,000 words (max: ch05 at 1,998).

## Check 3: Four-marks sentence (re-run after the late changes)

The full sentence now appears in: 00-copyright (1), 00-introduction (1), ch03 (2), ch07 (1, bolded), ch27 (1), ch32 (1), ch34 (1), **ch35 (1)**, wrap-back-copy (2). It appears in no other chapter. PASS.
- Canon had it in 19 chapter files that are now clean: ch12 to 26 except 27, plus 28 to 31. Levi's report says "18 chapter sites" but lists 19 (soft note 1).
- Orphan and lead-in check: every cut site reads cleanly. I checked for missing spaces (`[a-z][.?!][A-Z]` compared against canon), double spaces, and stray blank lines, and found none. ch20: the standalone stamp line was removed without leaving a double blank. The "Look for a man living the four marks, mostly." (ch13) and "Put the marks on that afternoon and watch them invert." (ch16) lead-ins still have a referent without the sentence.
- Lewis credit is unchanged: `grep "Robert Lewis|Modern-Day Knight"` gives the same output for canon and revision (copyright, intro L17, ch03 L13).

## Check 4: Protected seats

- **Eli:** ch01 is byte-identical ("His real life is the ten o'clock"). The ch25 callback matches ch01 (19, roommates) and ch33 (phone in the kitchen). PASS.
- **If There Is No Wife Yet (ch21):** the only change is the stamp at L80. "No wife yet still leaves you a man" is present. The three seats, the divorced seat, and the closer are untouched. PASS.
- **Empty Chair (ch08):** byte-identical. PASS.
- **Season nobody plans (ch32):** byte-identical. PASS.
- **Ch6 closer:** byte-identical. PASS.
- **Alone, single, divorced, no-child Your Turn options:** the word-diff shows only additions in closers. No existing branch was deleted or reworded. PASS.
- **NIV:** every `:::margin` block is identical to canon, and the NIV count is 153 in both sets. No new Scripture. PASS.

## Check 5: Intro (mechanics only; substance approved by Aaron)

- The binder bug is real. I ran the pack binder's own `parse_md` (`/tmp/steadfast-g47-pack/tools/make_ebook_pdf.py`, read-only import). Canon intro: 17 blocks, 1 false "closer" (everything from "**Name it** asks..." onward is swallowed). Revised intro: 28 blocks, 0 closers. `full.txt` confirms the shipped 238p PDF stops the intro at "...keep doing it." and goes straight to Part One.
- Preserved content: 504 words after "keep doing it." in canon, 507 in the revision (+3 for "The first line,"). The four-line explanation, missed-week paragraph, roster (Roy, Tomás, Kenny, Micah, Anthony, Walt), and "One more thing before you start" are all intact. Whole intro: 1,380 to 1,407 words.
- The time-short sentence reads cleanly. No dashes.
- Parse check on all changed chapters: each still has exactly one closer with four sections (name it, do this week, tell a brother, carry this). The block count went up by one in ch05, 09, 13 and 25 (new paragraphs) and down by one in ch20 (removed stamp line). This is expected.

## Check 6: New scenes and beats

- **Tomás ch05:** 29 years old, baby, kitchen table. This matches ch01, ch32, ch33 and ch35. The broke-Tuesday detail (the 14th and the 15th, $40 short, laptop turned toward her, "That's mine. We're short.") is concrete and answers Marcus. It sounds like a man talking.
- **ch07 kindness:** the couch sentence and "or roommate" answer Caleb. Grammar is fine.
- **Owen ch09:** adds the one beat of friction the panel asked for. Soft note 2 on a repeated "again/kitchen".
- **Kenny ch13, then ch35:** ch13 gives Kenny's first scene (one-bedroom, an older man from church asking "the three questions" defined earlier in ch13, "nothing" most weeks). ch35 names him, and the details agree with ch13: one-bedroom, weekly calls for a year, three questions, three years ago. The intro promise ("calls his son every Tuesday") is kept in ch35 ("It is Tuesday, so at 7:30"). Continuity PASS. Soft note 3 on "since" in ch13.
- **ch24 opener:** approved. Mechanics clean.
- **ch25 Eli callback:** original prose. It paraphrases the 1 Thess 4:4 idea ("control of your own body") with no quoted block and no new theology.
- **ch22 to 29 Your Turn options:** the cross-references match up. Ch26 Tell ("what you wrote about the girls at church") matches ch26 Name it. Ch27 Tell ("the boy you named this week") matches ch27 Do. Ch28 Tell ("how long you stayed on the step") matches ch28 Do. Ch29 "men at the water" matches ch29 Tell. The `:::notes` fences and the `**Label**` layout are intact in every closer. See the must-fix below for ch22 and ch23.
- **No em or en dashes:** `grep -P "\x{2014}|\x{2013}"` finds 0 in every file in book/.
- **AI vocabulary and chatbot phrasing in new text:** none. The only hits in the book ("navigating" ch02, "navigate" ch17 L26, "journey" ch31 NIV) are in canon text that did not change.
- **Original prose, no Opus:** I checked every new sentence of 6 words or more against the `book/` root files, which include the Opus 9/23 rewrite. There are no matches except two against older in-house drafts. "Come back for the rest when you can" is canon text re-cased. "Kenny's children are with their mother this week." matches `35-these-men-are-my-brothers.pre-fable-20260914.md`, which is a restoration of the house's own earlier line, not outside or Opus text. No reprinted outside material.

## Check 7: Nothing else

No Unslop pass was applied: the jab cadence, hot lines and stacked fragments elsewhere are unchanged, and style/ was not applied. No Opus text. No new theology.

## Check 8: Late changes (landed 10:45 CT)

- **36-about-the-author.md:** byte-identical to `book/36-about-the-author.md` inside `/workspace/cloud-agent-artifacts/bc-2e56f2b3-.../steadfast-men-grok47-ms-2026-09-21.tar.gz`. I extracted the text of `Steadfast-Men-GROK47-FULL-2026-09-21.pdf` (pdfinfo: 238 pages) with pdftotext. The About the Author body matches the markdown token for token (259 = 259, identical). No dashes. Reads clean. PASS. For information: `book/export/Steadfast-Men-GROK47-PRE-UNSLOP-ABOUT-AUTHOR-2026-09-21.pdf` (240p, 18:13 CT) is a later build that carries the 18:13 bio rewrite Levi flagged. This revision follows the 238p ship, as instructed.
- **ch35:** exactly one full four-marks sentence ("Once more, and then I am out of the way..." at L64). Carry this now reads "Tuesday is when it will show. Get up." The `:::notes` fence is intact, and the **Be a brother** block and its fences are unchanged. PASS.

---

## DIG list (must-fix)

1. **`23-lay-it-down.md` L119 (Do this week, new divorced branch):** "If the marriage ended, set down your right to win against their mother at the next exchange." "Their" has no antecedent. Nothing in the sentence or the closer mentions children, so a reader cannot tell whose mother is meant. This is the divorced seat (James), in new published text the reader has to act on. **Required fix:** name the referent, e.g. "against your children's mother". Leave the rest of the wording alone.
   - The same pattern shows up in **`22-know-her.md` L128** (new Do branch): "ask their mother one question about the kids". Here the pronoun comes before its referent. **Required fix:** "ask your kids' mother one question about them" (or similar). This is a one-phrase change, not a rewrite.

## Soft notes (do not block; for Levi and Aaron to consider)

1. Levi's report says "18 chapter sites" for the four-marks cuts, but the count is 19 (ch12 to 26 except 27, plus 28 to 31). The report table itself is correct.
2. ch09 L90 and L92: the new paragraph ends "...before the kitchen felt like theirs again." and the next canon line begins "Quiet started in that kitchen again". That is a doubled "kitchen...again". Optional trim.
3. ch13 L86: "If your church has not known which row to put you in since, ..." The "since" leans on Kenny's divorce while the sentence has already shifted to the reader. "since the divorce" would be clearer.
4. The divorced branches in ch22 and ch23 (and ch24's "ask your children") assume there are children. A divorced man without kids gets no branch there. This is optional, and the panel did not flag it.
5. ch22 L24: "Rejecting passivity in a marriage looks like study. Knowing her is that work." Slightly redundant back to back. Optional.
6. ch29 L7: the rite-of-passage scene now summarizes the father's spoken sentence ("The four marks followed, every word, in his father's voice.") instead of quoting it. This is acceptable because ch27 keeps the verbatim father-to-son anchor. Flagged only so Aaron knows.
7. The intro time-short path says "one chapter from the house". The Part is titled House, so capitalizing it might help. Mechanics only; the substance is approved.

## Panel coverage (judgment)

Levi's changes answer panel Top 10 items #3 (refrain density), #4 (House-block branches), and #7 (timebox), plus these notes: Marcus's broke Tuesday, Caleb's lived Tuesday with desire and asking an older man, James's ghost-apartment visibility, and the mailbox beat that resolved too quickly. The structural cause behind #2 (prose tripping the binder) is fixed. The running-head bleed itself is binder logic and still needs the `make_ebook_pdf.py` fix before rebuild (outside this gate's scope). #1 (Unslop) was correctly not attempted, per the PRE-UNSLOP override. Protected seats #5, #6, #8 and #9 all held.

**Re-hand path:** fix DIG 1 (ch23 L119, ch22 L128), and Reed will re-cmp those two files and sign.

## Re-hand 2026-09-25 10:47 CT: SIGNED
- Dig 1 cleared. 23-lay-it-down.md:119 now reads "your children's mother". 22-know-her.md:128 now reads "ask your kids' mother one question about them and let her finish." Diffs against canon show only the listed changes. 0 em dashes.
- Report cut count corrected to 19.
- 22-know-her.md:92 "their mother" is canon text, byte-identical to _grok47-ms. It is left as is: "the kids" in the very next sentence resolves it, and it is outside this revision's scope.
- VERDICT: SIGNED. No Unslop, no edits by Reed, no Drive.
