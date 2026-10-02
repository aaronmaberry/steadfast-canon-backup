# Open questions for Aaron

These are listed roughly by how much they matter. None of them blocks the focus group.

## Decisions

1. **Chapter 7's title vs. its mark name (proposal only; the H1 is unchanged).**
   - Chapters 4 to 6 are titled with their mark names (Stop Waiting, Pick Up the Weight, Go First). Chapter 7 is "Live for a Reward That Lasts", but its body now names the mark plainly as Work for God's Pay (L7 and L106).
   - **My proposal is to retitle chapter 7 "Work for God's Pay".**
     - In favor: all four mark chapters would read as a set in the contents and the class weeks, and a reader would meet the mark name in the TOC.
     - Against: the word "pay" would appear in the TOC without the inheritance anchor next to it. The current title is gentler, and it echoes Hebrews.
   - Changing the title touches the ch7 H1, `00-contents.md`, `37-condensed-training.md`, the binder's running head and the ch3 cross-reference (L84). The filename can stay as it is.
2. **Gethsemane outside chapter 19.** Chapter 13 ("Even Jesus asked", Mark 14:34) and chapter 35 (one paragraph) keep a garden scene from the base. Their cards fence a Hawks "garden-standby / Gethsemane-while-they-slept" bit. The writers cut every sleeping-disciples beat and kept only the request and the prayer. Keep, or cut further?
3. **Chapter 26 keeps Ephesians 6:4,** which its card says not to reprint. The base had it, and the brief said to keep the base's references.
4. **Chapter 19 Do this week** asks a man to say three Gethsemane lines in daily situations: "Rise, let us go." "Not as I will." "Let these men go." None is tied to a mark, so it isn't a mapping, but please look at it.
5. **Chapter 12, Grant's porch talk.** It is kept as Grant's own story: name the need, thank him, decide, offer. The writer couldn't tell whether that shape came from the leave-home material the card fences. I removed the "four things" count. If it echoes the course, it could be cut back to the single sentence Grant says.
6. **About the Author.** The facts are unchanged from the approved 9/21 bio: husband, father of two, Texan, leads technology teams, not a pastor or counselor, kitchen-table origin. Please confirm these are true of you. If they aren't, the bio is the fake biography the persona forbids.
7. **Dedication.** It is carried unchanged because it's locked. `BOOK-TOC.md` lists "Dedication (for Evan)", but the text never names Evan.
8. **Back cover theology.** The back panel prints the creed with no inheritance line beside it. An optional fix is to add one sentence under the creed, e.g. "God's pay is a Father's inheritance, not wages," or to leave the explanation to the book.
9. **Part look-backs.** `CLOSER-AND-STRUCTURE.md` calls for a one-page look-back at the end of each part. Neither the base nor this pass has them. Adding five would change the page count and the binder's part handling, so they weren't added.

## Things I'm less sure are original enough

- **Chapter 3 pictures.** The shop bench, tailgate, gun safe, stock tank and pecan tree are Steadfast's own (the IP report's Set 2 names come from them). They're kept, in new wording.
- **New small pictures.** The writers added original details, no new Wes Hart biography:
  - a church fish fry (ch4);
  - piano lessons and a stepdad (ch5);
  - a fog and fence-post road (ch17);
  - coal, tool outlines and a closing day (ch18);
  - a hospital clipboard (ch27);
  - "an October morning" and "seventy-something" for Lyle's dad (ch28).
- **Chapter 11's mother section** ("The woman who kept the porch light on") is new content written to the persona and card. It adds no facts about Nate's mother.
- **The introduction keeps the most base wording** (6-gram reuse 0.20). That comes from the Aaron-signed roster of men, the timebox path and the four-lines explanation.
- **Chapter 3's composites paragraph** was dropped, because the introduction already says the men are composites.

## Scripture house style (please confirm)

- **Dashes.** Where the NIV has an em dash, the margin text uses a comma, so the manuscript has no dash characters. This affects Ephesians 2:8-9, Isaiah 43:1 and similar verses. The words are identical, but Biblica's "word for word" may be read to include punctuation. If so, restore the dashes in those blocks and let the binder convert them.
- **Excerpts.** Seven blocks quote part of the cited verses, word for word: Titus 2:6-7, Psalm 119:105 (the Hebrew letter heading is omitted), 1 Samuel 17:34-35, Joshua 14:12, 1 Corinthians 3:13, Nehemiah 6:3 and Joshua 24:15. A few blocks add a closing quotation mark where the NIV speech runs into the next verse.
- **Pronouns.** Margin blocks keep the NIV's lowercase pronouns for God. Prose capitalizes them (He, His, Him), as the base did.

## Trademark and brand (for the attorney, not the prose)

- **STEADFAST** is Reg. 3870140 (Rebecca Halstead, leadership and motivational speaking), and STEADFAST LEGACY is pending for workbooks. The book title and the "twenty-four-week training" named Steadfast Men use STEADFAST as a product or series name. This is the main clearance question.
- **"Go First"** is a chapter title, a mark, and class week 6 in Condensed Training, which is a session title. Don't name a course, podcast or workbook "Go First" (I'LL GO FIRST is a registered mark).
- **"Four marks"** is only a descriptive label in the book (9MARKS is live for religious instruction).
- **"Twenty-four-week training."** Lewis's Quest is also 24 weeks. With his mark wording gone, the pairing is weak. Still, keep "24-week path" away from any mark language in marketing.

## Panel fixes

None were undone. The protected lines and panel branches are all kept (see REWRITE-REPORT). One brief note didn't apply: it listed Walt facts for chapter 1 (the part of the business he sold, the fall trip, the bank parking lot and three hundred contacts), but those facts live in chapters 32 and 35 of the base, not chapter 1. They stay where they were.

## Box-side build steps needed (brief §6; not done here)

1. **`book/art/render_03_figure.py`.** Set `MARKS = ["STOP WAITING", "PICK UP THE WEIGHT", "GO FIRST", "WORK FOR GOD'S PAY"]` and re-render `03-four-marks.png`. The new labels are longer than "PASSIVITY" and the others, so check the letter-spacing and box widths.
2. **`book/art/press/apply_wrap_back.py`.** Set `CREED = "A steadfast man stops waiting, picks up the weight, goes first, and works for God's pay, not the room's."`, use the hook from `book/wrap-back-copy.md` here, update `art/press/wrap-back-copy.md` to match, and re-apply `a-wrap.png`.
3. **`page_copyright()` in `make_ebook_pdf.py`.** It is hard-coded. It prints "Review draft for private review only", "NIV text appears word-for-word from the source pages" and "Original work. Cloth Store look.", and it has neither the Lewis acknowledgment nor the full Biblica notice. For print, render `00-copyright.md` instead, or hard-code its exact text. Remove "Original work". Also remove the title page's "Review draft. Not for distribution." line for print.
4. **Front cover.** No change (`cover-front-walksteadfast-locked-2026-09-14.png`).
5. **Build wrapper.** `ART`, `PRESS` and `FONTS` are computed from `BOOK` when the module is imported. So a wrapper that sets `m.BOOK = .../_opus55-ip-rewrite-2026-10-01/book` must also set `m.ART`, `m.PRESS`, `m.FONTS` and `m.FIGURES` back to `biblical-manhood/book/art/...`, because the rewrite folder has no `art/`. Give the wrapper its own `OUT` and `BUILD`. Build locally only, with no Drive upload.
6. **Margin cites now parse.** Every margin block now starts with `**Ref NIV**`, which is the form `parse_md` reads as a cite. The base's `Ref (NIV)` lines were printed as body text. Margin layout, and so the page count, may shift a little. Check the even-page signature after the build; the text is +4.1% longer than the 240-page panel build.
