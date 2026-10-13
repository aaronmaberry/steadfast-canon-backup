# B-A-A rewrite rules (2026-10-04)

**Authority.** Aaron approved this on 2026-10-04 at 7:32 AM CT: 28 chapters per `structure-review-2026-10-03/CHAPTER-MAP.md` (Option B), and a full rewrite in the B-A-A structure with the anchor verse opening each chapter, following the approved ch10 sample v2. This file is the top rule for the `_baa-rewrite-2026-10-04` manuscript. `SECOND-PASS-RULES.md` and `DRAFTING-RULES.md` in this folder still apply wherever this file doesn't change them. The 03d originals in `_opus55-second-pass-2026-10-01/meta/` are left untouched as the record of that pass.

## Chapter map (new number ← 03d number)

1-10 unchanged · 11 ← 11+12 · 12 ← 13+14 · 13 ← 15+16 · 14 ← 17 · 15 ← 18+19 · 16 ← 20 · 17 ← 21 · 18 ← 22 · 19 ← 23+24 · 20 ← 25 · 21 ← 26 · 22 ← 27+28+29 · 23 ← 30 · 24 ← 31 · 25 ← 32 · 26 ← 33 · 27 ← 34 · 28 ← 35.

The intro and ch1 take the new style but are not merged. Line references in the older rule files use 03d numbers. Translate them with this map.

## Chapter format

- `# N. Title`, then one `:::epigraph` (NIV text line, reference line), then prose.
- Scripture is narrated in plain words. The epigraph is the only word-for-word NIV quotation. Every narrated passage gets a Scripture-notes entry keyed by a phrase on the page (`work/notes/NN.md`, assembled into `book/39-scripture-notes.md`).
- No `##` subheads, no body bold, no lists, no margin blocks. Longer connected paragraphs.
- Two to four quiet breaks per chapter (`:::break` then `:::`).
- No "Before you turn the page". Its blessing folds into the last paragraph.
- The last paragraph is the quiet charge and ends on the protected Carry line, word for word as it reads on the Your Turn page.
- No chapter-number cross references.
- Keep every story, every protected line (`meta/tools/protected.json`), every season branch, and the theology, in Aaron's voice under the unslop rules. No em or en dashes, no mid-sentence colons, straight quotes in the markdown, God pronouns capitalized.

## Your Turn (back of book)

- `work/yourturn/NN.md` → `book/38-your-turn.md`, one page per chapter: `## N. Title`, then `**Name it**`, `**Do this week**`, `**Tell a brother**` (ch28: `**Be a brother**`), `**Carry this**`. The first three each take a `:::notes` block with three write-in lines.
- No "Because" openers and no single substitute opener used as a pattern. Mix questions, instruction-first lines, and the reason last.
- For a merged chapter, combine the source pages' prompts onto one page and keep every season branch.

## Merged-chapter carry lines

When two or three 03d chapters merge, one carry ends the chapter and is the Your Turn carry. The others either stay in the prose at the end of their section or are folded into the last paragraph, so no protected line is lost.

## Creed

The full creed sentence appears unbolded in the intro, ch3 (twice in the body), ch7, ch27 (the top line of the plan), and ch28. Nowhere else.

## Word targets

Single chapters: about 1,500 to 2,000 words. Merged pairs: about 2,800 to 3,500. The sons chapter: about 3,800 to 4,300.

## Binder

`book/tools/make_ebook_pdf.py` reads `book.json` from the manuscript folder (`layout: "baa"`) and sets justified B-A-A text: a 1.2em indent, no paragraph space, widow and orphan control, light hyphenation, the italic epigraph, diamond breaks, the back-of-book Your Turn and Scripture notes, and the man plan after the ch27 Your Turn page. Without `book.json` it falls back to the classic layout, which builds byte-identical text to the 03d print.

## Changelog

- 2026-10-04: created. Supersedes SECOND-PASS-RULES "Paths", "Locked format", margin-block, closer-at-chapter-end, "Before you turn the page", `##` sections, and the 1,700 to 2,000 word cap for merged chapters, plus DRAFTING-RULES "Locked format", "Your Turn" placement, and the margin rule.
