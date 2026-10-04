# Levi panel revision report, 2026-09-25

Steadfast Men, byline Wes Hart. This is a content revision that answers the Reader Panel notes. It is not a style scrub. Unslop rules were not applied.

## Source files used

- Canon markdown: `/workspace/biblical-manhood/book/_grok47-ms/book/` (44 files, Sep 21). Copied whole, along with `meta/` and `style/`, into `/workspace/biblical-manhood/book/_grok47-panel-rev-2026-09-25/`. All edits were made there. `_grok47-ms` was not touched, and neither was anything in `book/` root or `book/export`.
- Shelf PDF text: `/workspace/biblical-manhood/book/reader-panel/grok47-bounce/full.txt` (238 pages)
- Tarball, checked for completeness only: `/workspace/cloud-agent-artifacts/bc-2e56f2b3-d953-505f-a4e0-d410a6a93360/steadfast-men-grok47-ms-2026-09-21.tar.gz`. No markdown file was missing, so nothing came from the tarball.
- Panel notes: `/workspace/biblical-manhood/book/FOCUS-GROUP.md` and `/workspace/biblical-manhood/book/reader-panel/grok47-bounce/PANEL-BOUNCE-GROK47-PRE-UNSLOP-2026-09-21.md`. The only other file in that folder is `full.txt`.
- Read to diagnose the running-head problem, not edited: the binder at `/tmp/steadfast-g47-pack/tools/make_ebook_pdf.py`, which is the Grok 4.7 pack copy.
- **Excluded:** the Opus 5.5 rewrite. That covers `WAVE-A-NOTES-OPUS55-2026-09-23.md`, `WAVE-B-NOTES-OPUS55-2026-09-23.md`, and the chapter files in `book/` root with 9/23 mtimes. No text was taken from them. Also excluded: `_grok47-unslop-2026-09-21/` (the killed Unslop pass) and the Unslop skill and rules. `style/UNSLOP.md` was copied along with the canon set but not applied.

## Canon check: markdown against the shelf PDF

I compared the token stream of each file against `full.txt`.
- Chapters 1 through 35, plus the dedication, contents, and Condensed Training, match 100%.
- **The Introduction matches only about 65%.** The markdown is complete. The PDF dropped everything after "The four lines at the end". The binder's `parse_md` treats any line that starts with `**Name it` as the start of the chapter closer, and `page_intro` never draws closers. So the intro's prose line "**Name it** asks you to say..." made the binder silently delete about 480 words: the four-line explanation, the missed-week paragraph, the roster of men (Roy, Tomás, Kenny, Micah...), and "One more thing before you start". This is the prose-caused structure break. It is fixed below.
- **Copyright page:** the binder draws its own short copyright page, so the PDF page is not the markdown `00-copyright.md`. Lewis credit and the composites note appear in both. Not changed.
- **`36-about-the-author.md` does not match.** The markdown (mtime Sep 21 18:13) is a later rewrite than both the PDF and the tarball copy (14:34). The PDF has the tarball version. I kept the canon markdown as instructed, but this is a flag for you (see Unsure).
- `wrap-back-copy.md` is not in the PDF. That is expected.

## Panel items addressed

| Item | What was done |
| --- | --- |
| Top 10 #2, running head / folio bleed (e.g. Ch17 pages carrying "How That Looks on a Man") | **Diagnosed, not fixed in text.** This is binder logic, not prose. `advance()` draws the footer on the new page before `self.running` is set to the new chapter title, so each opener page, and sometimes the page after it, prints the previous title. The same bug puts "Contents" on intro page 3 and "Introduction" on the Part One pages. The fix belongs in `make_ebook_pdf.py`: set `self.running` before `advance()` in the chapter, part, intro, and section openers, or pass the title into `advance()`. Tools were outside the edit scope, so they were not touched. |
| Prose-caused structure break (related to #2) | Intro: "**Name it** asks you..." became "The first line, **Name it**, asks you...". I checked it with the binder's own `parse_md`. The canon intro parses to 17 blocks ending in a false "closer". The revised intro parses to 28 blocks with no closer, so the full intro will now print. |
| Top 10 #3, four-marks refrain density (~26 hits) | Full sentence cut from **19 chapter sites**: ch12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31. Each site got a short bridge or a plain deletion, so the paragraph still reads. **Kept where it earns its place:** intro, ch3 (twice, plus the heading "He rejects passivity"), ch7 (bolded, end of Part One), ch27 (the father speaks it to the son), ch32 ("Marks hold. Gardens change."), ch34 (top line of the man plan), ch35 ("Once more"; the Carry this copy was cut later, see Late changes), plus copyright and wrap. Lewis attribution untouched wherever it appears (copyright, intro, ch3). |
| Top 10 #4 and Caleb, alone / single / divorced / no-child branches uneven late in the House block | Added branches where the closer defaulted to married or father: ch22 Name it (single + divorced) and Do (divorced); ch23 Do (divorced); ch24 Do (divorced) and Tell (no wife); ch26 Tell (no daughter); ch27 Tell (no son); ch28 Tell (no son); ch29 Do (divorced dad + no son). |
| Caleb, wants desire / porn / "no older man will initiate" as a lived Tuesday, not a stamp | ch25: new paragraph calling back Eli's ten o'clock. He lost it a lot first, the phone sleeps on the kitchen counter, and after a year of waiting for someone to offer he asked an older man to hold the filter password. Consistent with ch1 (Eli, 19) and ch33 (phone left in the kitchen). |
| Caleb, Go First / Reward lean husband-first, alone lines feel like footnotes | ch7: a single man's hidden work added to the main secret-reward list (carrying a young family's couch upstairs). "Wife excluded" became "Wife or roommate excluded", in the body and in Do this week. Ch6 untouched (see protected). |
| Marcus, money named more than walked; wants one "broke Tuesday" picture | ch5, Providing without disappearing: new Tomás paragraph. Car payment on the 14th, payday on the 15th, forty dollars short even after a Saturday shift. The pull is to hide. He turns the laptop so she can see it and says "That's mine. We're short." Nothing gets solved that night, but she is not alone with it. |
| Top 10 #7, Marcus timebox path | Intro (Aaron-signed, one-sentence change, voice kept): the shortcut now reads Quiet Tuesday, then the closer each week, then Every Season Still Counts, then one house chapter that fits your seat, then one on your kids if you have them. No new chapter and no reordering. |
| James, ghost-apartment man "barely" visible; still-in-church shame | The intro promises "Kenny, divorced, who calls his son every Tuesday", but Kenny never appeared by name. Now: ch13 gives Kenny his first scene (one-bedroom apartment, an older man calling weekly, "nothing" most weeks), plus a line for the man whose church "has not known which row to put you in": you need one man who calls, not a program. ch35 names the unnamed divorced father as Kenny (twice) and makes the call a Tuesday. |
| False note, "mailbox confession to quiet kitchen resolves one beat faster than life" | ch9, Owen's mailbox: one beat of friction added. She was angry the first night, and not about the contract. He took it without a defense. It was most of a week before the kitchen felt like theirs again. |
| Drew, the jab "Here is the principle, early, so nothing else gets mistaken for it" (quoted by name) | ch24: this one sentence became "I will give you the whole chapter in two sentences first." Fixed only because the panel quoted it as a false note. This was not a sweep. The furnace and funeral lines are untouched. |

## Skipped, and why

- Top 10 #1 and every "Unslop the jabby voice / stacked aphorisms / checklist cadence" item: this is the Unslop pass, which you excluded. No AI-vocabulary or jab-flattening sweep was done.
- Moving Part Four after Part Five (marriage before Long Road): chapter titles and order are locked, and the panel's own soft dig says not to move House chapters forward. The time-tight path was handled in the intro instead.
- Overall length (238 pages): the panel asked not to gut the book. Net change is +430 words.
- Running-head binder fix: diagnosis and fix recipe are above. Tools and export were not edited, and no PDF was built.
- Desk items (Marcus card for the landing page, Caleb-only and James-only re-reads, Condensed Training left as-is): these are not manuscript edits. Condensed Training and About the Author are unchanged.
- Earl (62) is on the FOCUS-GROUP roster but has no notes in this bounce, so there was nothing specific to answer. The older seats (Roy, Walt, Alton, Abe, the widower) are unchanged.

## Per-chapter changes (words counted with `[A-Za-z0-9']+`)

| File | Change | Before | After |
| --- | --- | ---: | ---: |
| `00-introduction.md` | Name-it line reworded so the binder stops dropping the intro tail. Timebox path spelled out. | 1380 | 1407 |
| `05-pick-up-the-weight.md` | Broke Tuesday paragraph (Tomás). | 1863 | 1998 |
| `07-live-for-a-reward-that-lasts.md` | Single man's hidden work added to the list. "Wife or roommate" in the body and in Do this week. Four-marks bold line kept. | 1704 | 1733 |
| `09-anger-the-itch-and-the-drift.md` | Owen's mailbox: one beat of her anger added before the quiet. | 1899 | 1953 |
| `12-leave-without-slamming-the-door.md` | Marks stamp replaced with "All four marks are standing at this door." | 1899 | 1891 |
| `13-a-man-with-no-brothers.md` | Marks stamp cut. Kenny introduced. Line for the man his church doesn't know where to seat. | 1883 | 1941 |
| `14-ask-the-man.md` | Marks stamp cut. | 1896 | 1880 |
| `15-the-problem-inside.md` | Marks stamp cut. The paint-can line stands alone. | 1871 | 1855 |
| `16-how-that-looks-on-a-man.md` | Marks stamp cut. The David inversion list carries it. | 1887 | 1871 |
| `17-no-fixed-star.md` | "Line this book keeps repeating" + stamp became "Hang the four marks on that string..." | 1899 | 1890 |
| `18-before-the-fall.md` | Marks stamp cut. | 1996 | 1980 |
| `19-two-men-two-ways.md` | Stamp became "Come back to the four marks." The garden mapping is kept. | 1990 | 1980 |
| `20-destiny-is-not-a-vibe.md` | Standalone stamp after "Destiny is not a vibe." cut. | 1885 | 1869 |
| `21-if-there-is-no-wife-yet.md` | Stamp only, now "...a real man rejects passivity." Chapter otherwise untouched. | 1865 | 1855 |
| `22-know-her.md` | Stamp became "Rejecting passivity in a marriage looks like study." Single and divorced closer branches added. | 1831 | 1873 |
| `23-lay-it-down.md` | Stamp cut. Divorced Do-this-week branch added. | 1880 | 1881 |
| `24-what-she-actually-needs.md` | "Principle, early" jab fixed. Stamp cut. Divorced Do branch and no-wife Tell branch added. | 1823 | 1854 |
| `25-the-bed-is-a-covenant.md` | Stamp cut. Eli ten o'clock paragraph in the single section. | 1804 | 1932 |
| `26-your-daughter-is-watching.md` | Stamp folded into "The four marks, as she sees you live them..." No-daughter Tell branch added. | 1880 | 1885 |
| `27-give-your-son-a-name.md` | Full sentence kept (anchor). No-son Tell branch added. | 1681 | 1698 |
| `28-give-your-son-a-hill.md` | Stamp became "The first mark cuts the other way here." No-son Tell branch added. | 1853 | 1864 |
| `29-give-your-son-a-day-he-will-not-forget.md` | Stamp became "The four marks followed, every word, in his father's voice." Divorced-dad and no-son Do branches added. | 1839 | 1872 |
| `30-you-were-made-for-a-work.md` | Stamp became a naming of the fourth mark only. | 1844 | 1835 |
| `31-feelings-are-the-dash-not-the-wheel.md` | Stamp cut after "The four marks hold." | 1850 | 1834 |
| `35-these-men-are-my-brothers.md` | Unnamed divorced father named Kenny, and it's a Tuesday. Both marks lines kept. | 1747 | 1748 |

Unchanged: front matter other than the intro, ch1, ch2, ch3, ch4, ch6, ch8, ch10, ch11, ch32, ch33, ch34, 36, 37, wrap. Whole book: 67,469 words before, 67,899 after (+430). Every numbered chapter is still under 2,000 words.

## Locked style checks

- Em and en dashes: `grep -cP "\x{2014}|\x{2013}" book/*.md` returns 0 for every file. The only dash hits in the folder are in the copied, unedited guide docs `style/GRAPHICS.md` and `style/UNSLOP.md`.
- No new Scripture was added, so NIV blocks are unchanged. Nothing borrowed from Wild at Heart or other shelf material. No new named composite collides with Marcus or Wes. Closer shape (Your Turn, then Name it / Do this week / Tell a brother / Carry this, each opening with Because; Be a brother in ch35) is intact. H1 titles and order are unchanged.
- Aaron-signed files: ch1, ch2, and ch3 are byte-identical to canon. The intro changed only in the two spots listed, both demanded by panel notes (#2 structure, #7 timebox).

## Protected seats: grep evidence (revised folder)

- Eli: `grep -lw Eli` finds ch01 ("His real life is the ten o'clock" intact), ch25 (new callback), ch33.
- If There Is No Wife Yet: only the marks stamp changed. "No wife yet still leaves you a man" is present in ch21. The three seats, the divorced seat, and the closer are untouched.
- Empty Chair: `08-the-empty-chair.md` is byte-identical to canon. "Nobody ever sat in this seat for me" and "somebody's empty chair now" are both present.
- Season nobody plans: `32-every-season-still-counts.md` is byte-identical ("## The season nobody plans", "February has a job", "Gardens change").
- Ch6 Go First: `06-go-first.md` is byte-identical ("On your own, say Sunday and drive", "Your number is second").
- Hot lines found: "decided on Tuesdays" (01); "Six maps" (02); "Absence purchased with a bigger paycheck is still absence" (05); "Where are you" (04); "pain was looking for a Father" (09); "twenty minutes, every week" (13 Carry this); "Ride with me" (14); "Paint's not going to fix that" (15); foyer (16); "string on the wall" (17); "furnace sentence" and "at his funeral" (24); "A contract keeps score on her" (25); "I come to watch you" (26); "I figured you could" and "right hill" (28); "open chair" (35).
- Lewis: "Robert Lewis" in 00-copyright, 00-introduction, 03-the-four-marks. "Raising a Modern-Day Knight" in copyright and intro. Same as canon.
- Composites: Roy, Tomás, Kenny (now in 00, 13, 35), Micah, Anthony, Walt, Dale all present.
- Wes Hart: title page, copyright, About the Author, wrap. The persona is still first person throughout.

## Unsure / flags

1. `36-about-the-author.md`: the canon markdown (Sep 21 18:13) differs from the PDF and tarball version (14:34). I kept the markdown. If the shelf version is the approved one, swap in the tarball copy.
2. Running heads need a one-line binder change I did not make (see above). Rebuilding the PDF is also what will confirm that the full intro prints.
3. The intro is Aaron-signed. Both changes there are small, but he should see them: the timebox sentence and the Name-it line.
4. The ch24 jab fix sits on the line between content and Unslop. I did it only because the panel quoted that sentence by name. Revert it if you want zero style touches.
5. Ch35 now prints the full four-marks sentence twice (the "Once more" section and Carry this), as canon does. I left both because it is the closing chapter.

## Late changes (Aaron calls via Jarvis, 2026-09-25)

- Intro edits: KEEP (both). Ch24 opener rewrite: KEEP.
- `book/36-about-the-author.md`: replaced with the 9/21 Wes Hart version that shipped in the 238p PDF and tarball (taken from the tar's `book/36-about-the-author.md`, checked line by line against `full.txt` lines 7876-7896). 306 to 261 words.
- `book/35-these-men-are-my-brothers.md`: cut the SECOND full four-marks sentence (the one opening the Carry this closer). Carry this now reads "Tuesday is when it will show. Get up." The first one ("Once more, and then I am out of the way...") stays. Full sentence count in ch35 is now 1.
- No em or en dashes in either file.

- Reed dig (2026-09-25): pronoun fixes. `23-lay-it-down.md` line 119 now says "your children's mother". `22-know-her.md` line 128 now says "ask your kids' mother one question about them". The cut count above is corrected to 19 chapter sites (ch12-26 and ch28-31).

---

## Addendum, 2026-09-25 ~10:52 CT: About the Author swapped to the 9/21 18:13 rewrite (per Aaron)

- Aaron chose the stronger 9/21 Wes Hart About the Author rewrite, the version in the 18:13 build `book/export/Steadfast-Men-GROK47-PRE-UNSLOP-ABOUT-AUTHOR-2026-09-21.pdf` (same file as `Steadfast-Men-2026-09-21.pdf` on Drive). It replaces the older bio from the 238p FULL build.
- `book/36-about-the-author.md` in this folder is now a byte-for-byte copy of `_grok47-ms/book/36-about-the-author.md` (mtime 9/21 18:13). Its words match the 18:13 PDF's About the Author page exactly. Wording and paragraphing are unchanged.
- The replaced file was kept as `book/36-about-the-author.pre-bio-swap.md`. The binder reads fixed filenames, so it does not pick up the backup.
- Dash check: 0 em or en dashes in the new bio.
- This supersedes the "Unsure" flag above and Reed's Check 8, which followed the 238p ship bio.
- Test rebuild with the fixed binder (running heads now switch before the page is drawn, and blank versos print no footer): `/workspace/tmp-binder-test/Steadfast-Men-Grok47-panel-rev-2026-09-25.pdf`. It is 240 pages, and every running head matches its chapter (0 mismatches).
