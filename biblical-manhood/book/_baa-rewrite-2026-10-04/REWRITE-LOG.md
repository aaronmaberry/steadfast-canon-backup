# B-A-A full rewrite, 2026-10-04 (working log)

Approved by Aaron 2026-10-04 7:32 AM CT: 28 chapters per `structure-review-2026-10-03/CHAPTER-MAP.md` Option B, B-A-A structure like ch10 sample v2. Intro and ch1 restyled, not merged.

Source (read only): `../_opus55-second-pass-2026-10-01/book/` (03d). Never edit it. No Drive. No trash.

## Format (binder parses this)
- Line 1 `# N. Title`. Then `:::epigraph` / NIV verse text line / reference line / `:::`.
- Prose paragraphs only. `:::break` + `:::` for quiet breaks (2-4). No `##`, no bold, no lists, no margin blocks.
- Last paragraph ends on the Carry line (same as the Your Turn Carry this line).
- Your Turn entry per chapter in `work/yourturn/NN.md` (assembled into `book/38-your-turn.md`). Labels Name it / Do this week / Tell a brother (Be a brother in 28) / Carry this. No "Because" openers, vary the openings.
- Scripture notes per chapter in `work/notes/NN.md` (assembled into `book/39-scripture-notes.md`), keyed by quoted phrase from the prose.
- Lint: `python3 meta/tools/baa_lint.py book/NN-*.md` (protected lines in `meta/tools/protected.json`).

## Mapping (new <- 03d)
1<-1, 2<-2, 3<-3, 4<-4, 5<-5, 6<-6, 7<-7, 8<-8, 9<-9, 10<-10, 11<-11+12, 12<-13+14, 13<-15+16, 14<-17, 15<-18+19, 16<-20, 17<-21, 18<-22, 19<-23+24, 20<-25, 21<-26, 22<-27+28+29, 23<-30, 24<-31, 25<-32, 26<-33, 27<-34, 28<-35.
Parts: One 1-7, Two 8-14, Three 15-16, Four 17-22, Five 23-28.

## Fixed rules carried from 03d
Creed only in intro, 3 (<=2), 7, 27 (top line of plan), 28. Inheritance anchor full in intro, 3, 7, 23, 27; one clause in 26. Narrator rules and consistency table from SECOND-PASS-RULES. No "code"/"cause" in 22. No weeknight. God pronouns capitalized in prose. Season branches never dropped.

## Status
- 00 intro: DONE (1,644 words, 3 breaks; locked text kept nearly verbatim, headings and bold removed, closer lines rewritten for back-of-book Your Turn; anchor 1 Cor 15:58)
- 01: DONE (1,791; locked wording kept, subheads/boxes/Before-you-turn folded; Luke 16:10 anchor, Matt 7:24 narrated)
- 02: DONE
- 03: DONE (creed x2 in body: reveal + last line; anchor 1 Cor 16:13; four-marks callout still triggers on creed paragraph)
- 04: DONE
- 05: DONE
- 06: DONE
- 07: DONE (creed x1, full inheritance anchor kept)
- 08: DONE
- 09: DONE (anchor Eph 4:26-27)
- 10: DONE (approved sample v2 used as-is; Your Turn openers varied)
- 11: DONE (merge 11+12; anchor Gen 32:26; old ch11 carry line kept mid-chapter after Nate's sink, old ch12 carry ends the chapter; three-sons picture moved to open the leaving half; baptism callback shortened to one line)
- 12: DONE (merge 13+14; Dale frames it; Travis/Harlan section in the middle; old ch14 carry kept at end of that section; anchor Eccl 4:9-10)
- 13: DONE (merge 15+16; shapes catalog compressed into prose; David/Nathan before Wade; kingdom line ends David section; anchor Mark 7:23)
- 14: DONE (anchor Amos 7:7 only, trimmed from 03d box 7:7-8 to one verse)
- 15: DONE (merge 18+19; design half then two gardens; garage garden opens second half; Adam's silence home; carry keeps 'It is finished' quote, flag)
- 16: DONE (anchor Acts 13:36)
- 17: DONE (protected chapter kept near verbatim; anchor 1 Cor 7:35)
- 18: DONE (anchor 1 Pet 3:7; 'dwell with them according to knowledge' cites KJV wording in notes)
- 19: DONE (merge 23+24; She-needs list turned into prose; epigraph Eph 5:25 kept verbatim with no closing period, flag)
- 20: DONE (anchor Heb 13:4)
- 21: DONE (anchor Zeph 3:17)
- 22: DONE (merge 27+28+29; carry = old ch29 carry; old ch27 carry folded into the last paragraph; ch28 carry folded as Lyle's rule; anchor Deut 6:6-7; no code/cause)
- 23: DONE (anchor John 5:17; work-before-curse repeat cut to one glance; carry trimmed to drop its first sentence, which restated work-before-the-curse. FLAG)
- 24: DONE (anchor Ps 42:5; 988 line kept)
- 25: DONE (anchor Eccl 3:1, NIV ends with colon, kept verbatim, flag)
- 26: DONE (anchor Heb 6:10; one inheritance clause)
- 27: DONE (anchor Hab 2:2; creed as plan top line, unbolded; carry: colon removed, LORD->Lord; YT refers to man-plan sample on next page)
- 28: DONE (anchor Prov 17:17; creed x1 unbolded; Be a brother label; blessing narrated)

## Final status (2026-10-04, ~8:15 AM CT)
- Varied the repeated "at the top of this chapter" callback (14 uses down to 5; ch12, 15, 16, 20, 23, 24, 26, 27, 28 rephrased). Lint clean.
- Note key for ch3 "well done" rekeyed to "the Father Himself saying" so it matches body text.
- Your Turn and Scripture Notes reassembled from work/ fragments.
- Rebuilt review-2026-10-04a: 192 pages, FAIL 0, WARN 1 (page count under 240 target). No dashes in extracted text.
- Classic regression: 03d rebuilt with patched binder = 238 pages, FAIL 0, pdftotext identical to the delivered 03d print.
- 03d manuscript folder and 03d print folder: no files modified since 07:30 CT.
- Nothing uploaded to Drive, nothing trashed, 03d not replaced.

## Edit gate and quiet-check (2026-10-05, evening CT)
Polish and correctness pass only. No voice change, no Unslop-style rewrite. Backup before edits: `/workspace/backups/edit-gate-2026-10-05/` (book/, work/, REWRITE-LOG.md). Edit script and per-edit log: `work/edit-gate-2026-10-05/apply_edits.py` and `edits.tsv`.

- 24 edits in 15 files (22 prose edits in 13 chapters plus About the Author, and 2 Scripture-note keys that follow them; the matching work/notes fragments 08 and 24 were synced). Intro, ch1, ch10, ch17, the creed lines, and every protected line were not touched. No typos found in the locked pages.
- Anchor verses: all 29 epigraphs checked word for word against the verified 03d NIV list. Eph 4:26-27, Amos 7:7, Hab 2:2 and Eph 5:25 were also checked against BibleGateway NIV. All 29 match, and all references are correct.
- Mechanical checks: 0 em/en dashes, 0 curly quotes in the markdown, 0 doubled words, 0 misspellings (pyspellchecker and codespell), 0 mid-sentence colons in the chapters, and the 2 in About the Author fixed. All 28 chapter endings match their Your Turn carry lines word for word. Every Scripture-note key is found in its chapter.

### FLAG decisions
- ch15 'It is finished' carry: KEEP as is. It is the 03d carry word for word, the three words read the same in every major translation, and it already has a Scripture note (John 19:30). It isn't an extra NIV quotation that needs its own block.
- ch19 Eph 5:25 epigraph with no closing period: KEEP verbatim. In the NIV, verse 25 ends mid-sentence ("...gave himself up for her" runs into "to make her holy"). This matches the ch5 lowercase "for each one..." and the ch25 colon. If Aaron would rather end it with a period, that is a one-character change.
- ch23 trimmed carry: KEEP the trim ("When the old plot is gone, God gives you a new one. Finish yours."). The dropped 03d sentence ("God handed man work before anything went wrong.") repeats ch15's protected "Work came before the curse" and ch23's own "in a garden, before anything broke". The trim also fits the two-short-sentence carry rule, and He to God gives the line its subject. Your Turn already matches.
- ch25 Eccl 3:1 colon: KEEP verbatim. The NIV verse ends with a colon that leads into verses 2-8. Same reasoning as Eph 5:25.
- ch18 KJV note: KEEP. "dwell with them according to knowledge" is the KJV (public domain). Scripture Notes labels it "1 Peter 3:7, King James Version", and the prose says "Older translations". This meets the copyright page's "Unless otherwise noted, Scripture quotations in this book are from the NIV."

### Quiet-check
- Robert Lewis, Raising a Modern-Day Knight, Men's Fraternity, Authentic Manhood: found only in 00-copyright.md, in the locked acknowledgment. None in any other file, including the back cover copy. The retired mark wording, "real man", "knight/weeknight", Hawks, Red Rocks and One Mission: 0 hits. ch22 has no "code" or "cause".
- Tim transcripts: `checks.py ngram` (8-word overlap against all of biblical-manhood/transcripts). Before the pass there was 1 non-Scripture run (ch2, "at what a man is supposed to be", a generic phrase), and it has been reworded. After the pass there are 0 non-Scripture runs. The 21 remaining runs are all NIV Scripture wording that a transcript also quotes (Gen 1:27, 2:7, 2:16, 2:18, 3:6, 3:8; Col 3:23-24; Heb 11:26, 10:24; Eccl 4:9-10; 1 Cor 15:22, 16:13; 1 Pet 3:7; Eph 5:25). The tool only recognizes `:::margin`, so it labels epigraphs "other".
- Narrator: no real-person story is told as Wes's own family. The first-person family material is only the wedding, the children and the baptism (ch1, intro, dedication). The disclaimer says "the author's own wife, children, wedding, and baptism are real". Clay, Travis, Cody, Hollis and Cole, Lyle, the creek (told to Wes by the boy's dad), Gil, Alton and the "buddy of mine" lines are all men Wes knows, told in the third person.
- Contents: all 28 chapters appear in order under the right Parts, followed by the back matter. All 33 page references in the PDF contents were checked against the printed folios, and all are correct.

### Build
- review-2026-10-05-final: `/workspace/print-build/review-2026-10-05-final/final/Steadfast Men - Review Print - 2026-10-05-final.pdf`, 192 pages, 6x9, FAIL 0, WARN 1 (page count under the 240 target, same as 04a). Same binder, fonts, art and locked cover (sha PASS) as 04a. The pdftotext diff against 04a shows only the edits above. Copy: `/workspace/tmp-send/Steadfast-Men-review-2026-10-05.pdf`.
- 03d manuscript and print folders: 0 files modified today. No Drive, no trash, no spend, no messages, no cover work.
