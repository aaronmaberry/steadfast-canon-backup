# Drafting log, 2026-10-01

This log is part of the independent-creation record (brief §3.14). The git history on branch `opus55-ip-rewrite-2026-10-01` holds every intermediate state.

## Sources used

- Base manuscript (read only): `biblical-manhood/book/_grok47-panel-rev-2026-09-25/book/` (43 files, plus the stray `36-about-the-author.pre-bio-swap.md`, which was not used).
- Rules: the attached 2026-10-01 `OPUS55-REWRITE-BRIEF.md`, `OPUS55-IP-REPORT-2026-10-01.md`, `CANON.md`, `STEADFAST-AUTHOR-PERSONA.md`, `BOOK-TOC.md`, `SCRIPTURE.md`, `CLOSER-AND-STRUCTURE.md` and `FOCUS-GROUP.md`. Also the panel provenance (`LEVI-PANEL-REV-REPORT-2026-09-25.md`), chapter cards `book/NN-card.md` (chapter jobs only; old-creed lines ignored), and the binder `book/tools/make_ebook_pdf.py` (format only).
- **Not used for wording:** `transcripts/`, `briefs/`, `notes/`, `PHD-MASTERY.md`, `FRAMEWORK.md`. The transcripts were opened only by the automated 8-gram checker (`tools/checks.py ngram`, `tools/make_reports.py`) and for a one-line header check of session 22, which confirmed that its life-stage map and Hebrew stage names had to stay out of ch32. Not used at all: `_grok47-unslop-2026-09-21/`, `style/UNSLOP.md`, the 9/23 Opus wave chapters, and `book/*.pre-*`.

## Who drafted what

- **Lead (this agent):**
  - Drafted `00-copyright`, `00-introduction` (twice; the second draft was rebuilt from a new outline), `03`, `07`, `34` (twice; the second rebuilt from a new outline), `36`, `37` and `wrap-back-copy`.
  - Carried `00-half-title`, `00-title-page`, `00-dedication` and `00-contents` unchanged (locked, no IP content).
  - Wrote `DRAFTING-RULES.md` and the check tools.
  - Reviewed and edited all 44 files after drafting.
- **Eight parallel chapter writers**, each working from `DRAFTING-RULES.md`, the persona, the canon and the base chapter, with chapter-specific IP notes:
  - 01, 02, 04, 05
  - 06, 08, 09, 10
  - 11, 12, 13, 14
  - 15, 16, 17, 18
  - 19, 20, 21, 22
  - 23, 24, 25, 26
  - 27, 28, 29, 30
  - 31, 32, 33, 35

  Each writer self-checked with `checks.py sweep` and `checks.py sim` and reported per chapter: words, similarity, marks named, pay anchors, margin changes and doubts. Several writers said their first drafts, though freshly worded, followed the base sentence order and scored 0.45 to 0.65. They rebuilt those drafts from new outlines and reordered sections.

## Review fixes made by the lead after drafting

1. **Ch35 L74.** The base's Gethsemane passage mapped the four marks to four actions of Jesus ("Up off the ground. Out to meet what was coming. His men covered. The work finished..."). The writer had carried that mapping forward. It is now a family-resemblance sentence with no mapping (brief §3.7). A search of every paragraph that pairs a mark with Jesus, Adam, a garden or the cross found only single-mark references.
2. **Ch12.** Grant's porch talk was summarized as "say those four things anyway", which made it a countable four-step list. The count is removed.
3. **Ch27 L73.** The closing three-beat ("You belong to me. I see what you're becoming. You're growing up in my house.") is cut to "you're Mine, and I'm glad you're home." This keeps it from echoing a three-point "what every son needs" list.
4. **Ch28 closing blessing.** "The Father who laid wood on Isaac" was corrected: Abraham loaded the wood, and the Father laid a cross on His own Son.
5. **Scripture.** Every block was verified against the NIV, and the base's errors were fixed: John 18:8 word order, Numbers 8:26 "brothers", 1 Kings 19:4 "wilderness", and a stray comma in Isaiah 46:4. Nested quotation marks were normalized in Judges 7:17, 1 Kings 2:2-3, Mark 14:34, 2 Samuel 12:7, John 4:34 and Ephesians 5:31.
6. **Two incidental 8-word matches with the transcripts in prose.** These were reworded: ch4, a Genesis 3:8 phrase, and ch13, "to look you in the eye and say".
7. **Pronoun casing.** He, His and Him for God and Jesus were made consistent book-wide; about 45 instances had been written lowercase.
8. **Pay anchors.** One was added to ch34 (the plan's top line). The ch7 recap now names Work for God's Pay a second time.
9. **Ch18 head.** "Before you turn" was aligned to "Before you turn the page".

## Checks run (final state)

- `tools/checks.py sweep`: brief regex 5 hits, all on the copyright acknowledgment. Extra fences 1 hit, the same line. Dashes 0. Format problems 0.
- `tools/make_reports.py` 8-gram scan: 0 prose runs. 32 margin blocks match (Scripture only).
- `tools/niv_verify.py`: 158 blocks and 179 unique verses. 141 exact, 7 excerpts, 10 identical in words with excerpt punctuation only.
- `tools/binder_parse_check.py`: intro plus 35 chapters, 0 problems.
- Creed counts: intro 1, ch3 2, ch7 1, ch34 1, ch35 1, wrap 1, elsewhere 0.
