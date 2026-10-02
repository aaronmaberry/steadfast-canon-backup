# Open questions for Aaron (after the second pass)

Everything settled on 2026-10-01 is done and is not repeated here (see `CHANGELOG.md`). These items are still open.

## Scripture punctuation (small confirmations)

1. **Ephesians 2:8-9, the second dash.** Bible Gateway and BibleHub both show "gift of God— not by works", with a space. In both sources the space comes where verse 9 begins. The NIV closes its em dashes in running text ("faith—and"), so the margin block prints "God—not by works" with no space. Please confirm against a print NIV. If the print edition really has a space, the change is one character at `07:52`.
2. **Blocks that end with an open quotation mark.** Six blocks end with speech still open, exactly as the NIV prints them, because marks are never added: 1 Kings 2:2-3 (`11`), 2 Samuel 12:7 and 12:13 (`16`), Amos 7:7-8 (`17`), John 4:34 (`20`) and 1 Samuel 17:34-35 (`28`). The brief's other option is to extend each citation by a verse, or to re-cut it, as was done for Judges 7:17-18, Luke 15:20, Habakkuk 2:2 and John 14:9. Say "extend" if you'd rather have no open marks. Extending adds about 6 to 10 verses (the count would still be under 200), and some of the added verses run long.
3. **Straight quotes.** The manuscript uses straight quotes throughout, Scripture included. The comparison treats curly and straight as the same punctuation. If the print build should show the NIV's curly quotes, the binder or typesetter should convert them; the text needs no change.

## Narrator and voice

4. ~~"Men sit across from me."~~ **Answered (recast).** See the CHANGELOG follow-up.
5. **New composite detail in ch29.** The neighbor at the creek is now "a single man who'd never been asked to anything like it", so single readers have a man in that scene. This is a story told to Wes, not narrator biography. Cut the clause if you'd rather not add it.

## Restored About the Author: claims that strain the book (Aaron to decide; not changed)

1. **"Steadfast Men, the twenty-four-week training behind this book, began at one of those tables…"** The intro (L61) says the training was built afterward, "on the same backbone", and About used to say the book "grew up alongside it". The bio makes the training the source of the book; the intro makes it a companion.
2. **"church classrooms… It has since been taught in living rooms, garages, church basements, and online"** and **"When he is not working or teaching"**. These present Wes as the class's teacher and leader. The prose recasts did the opposite: ch24:7 ("I've sat through enough funerals"), ch26:3 ("From the second pew at a wedding"), and the follow-up lines at intro:3, 02:19, 18:5, 23:53, 25:5, 25:48 and 27:13 all make him a man among men at the table. The bio's own "He is not a pastor and he is not a counselor" agrees with those recasts. The teaching role is the strain.
3. **"A few older men kept a chair for him when he had nothing worth setting on the table."** The book's only first-person mentor story, Harlan's "Ride with me Saturday" and "Well. You paid attention." (ch14), now belongs to **Travis**. The book never shows a man mentoring Wes; only the dedication's "men who pulled a chair out for me" echoes this.
4. **"He is a husband, a father of two, and a Texan. By day he leads teams in technology."** The book has no first-person career or home-state detail. The career clause at 01:15 was cut under the narrator rule. Aaron's narrator decision and the copyright disclaimer name only his wife, children, wedding and baptism as real. "Father of two", "Texan", "leads teams in technology", the teaching history and the hobbies all go beyond that list. If any of them isn't true, it is the invented biography that the persona and canon forbid ("No fake Wes Hart biography"). The panel had flagged this bio as "made up" (FOCUS-GROUP, settled item 1).
5. **The other men's stories (Cody's truck, ch15; Clay and Vernon's tractor, ch31; the old rancher's callus, ch35; Travis's wedding, ch14).** The bio claims none of these, so there is no direct contradiction. Item 3 is the only overlap.
6. **No conflict:** "a husband… on a long walk with his wife… outside with his kids" matches 01:15, the dedication and the disclaimer. "He set out to stop being the passive husband and distracted dad" matches the narrator's self-owns. "He is a layman" and "not a pastor… not a counselor" match the recast clergy and counselor lines. The bio has no old mark wording or creed, and no dashes, so nothing in it needed a house-rule change.

## Trademark and naming (attorney, before print or sale)

6. **STEADFAST** (Reg. 3870140) and **STEADFAST LEGACY** (pending, workbooks) need clearance for the book title and the "Steadfast Men" training. This doesn't touch the prose.
7. **"Work for God's Pay"** is now a chapter title and a class-week title (week 7). It has not been searched separately as a mark, so clear it before using it as a course or product name. The same caution applies to **"Go First"** (I'LL GO FIRST is registered).

## Outside this folder (the box syncs these; not edited here)

8. `biblical-manhood/BOOK-TOC.md:19`: change to "7. Work for God's Pay" (and the same line in `/workspace/steadfast-kb-seed/03-book/BOOK-TOC.md`). Its "Dedication (for Evan)" line also no longer matches the decision that the dedication carries no names.

## Box-side build steps (after the text lands)

1. Sync `BOOK-TOC.md` (item 8).
2. **Binder `no_em()`** (`make_ebook_pdf.py:108`, applied at `:194` and in the margin path). Exempt `:::margin` text so the NIV's em dashes print as em dashes and not as " - ". There are 4 dashes in 3 blocks: Ephesians 2:8-10, John 10:14 and Ecclesiastes 12:1.
3. **`render_03_figure.py`.** Set `MARKS = ["STOP WAITING", "PICK UP THE WEIGHT", "GO FIRST", "WORK FOR GOD'S PAY"]` and re-render. Check the widths, since the labels are longer than the old ones.
4. **`apply_wrap_back.py`.**
   - Set `CREED` to the new creed.
   - Add the line "God's pay is a Father's inheritance, not wages." under it, in a smaller size.
   - Re-apply to `a-wrap.png` and update `art/press/wrap-back-copy.md` to match `book/wrap-back-copy.md`.
5. **`page_copyright()` and the title page.** `page_copyright()` must render `00-copyright.md`. It currently prints hard-coded "Review draft… Original work" text with neither the Lewis acknowledgment nor the Biblica notice. Remove "Review draft. Not for distribution." from the title page (`make_ebook_pdf.py:649`).
6. **Build wrapper.**
   - Set `BOOK` to `_opus55-second-pass-2026-10-01/book`.
   - Reset `ART`, `PRESS`, `FONTS` and `FIGURES` to `biblical-manhood/book/art/...` (the rewrite folder has no art), and give the wrapper its own `OUT` and `BUILD`.
   - Build locally only, then check the page count (about 240) and the even-page signature. The text is +1.2% against the 68.7k target, a little above the panel-rev build.
   - No Drive upload until Aaron approves.
7. **Running head for ch7.** It comes from the H1, so it will now read "Work for God's Pay". The binder's `CHAPTER_FILES` entry (`07-live-for-a-reward-that-lasts.md`) doesn't change.
