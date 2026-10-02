# Rewrite report: Opus 5.5 IP rewrite, 2026-10-01

*Steadfast Men* (*The way of Godly Men*), byline Wes Hart. This pass is a full content and IP rewrite of the Grok 4.7 pre-unslop manuscript, panel revision 2026-09-25 (`_grok47-panel-rev-2026-09-25/book/`), in the starred persona's voice. Unslop was not applied. Brief: `OPUS55-REWRITE-BRIEF.md` (2026-10-01).

**How to read the numbers.** Counts use the token pattern `[A-Za-z0-9']+` on the whole file: headings, margin Scripture, and closers. The columns:

- **sim** is `difflib.SequenceMatcher` on the word sequence of the whole file, base against new. It counts shared common words, names, Scripture blocks and closer scaffolding. Two unrelated chapters of this book score about 0.10 against each other.
- **6-gram reuse** is the share of 6-word phrases in the new prose (margin Scripture excluded) that also appear in the base prose. It is the better measure of carried-over wording.

**H1 changed:** no, for all 44 files. File names are unchanged. `36-about-the-author.pre-bio-swap.md` is dropped (brief §7.1).

## Totals

- Base: **67,884** words (43 files; the brief's 68.7k used `wc -w` and included the stray backup).
- New: **70,666** words (44 files): **+2,782 (+4.1%)**, inside the ±5% band. Expect a few more pages than the 240-page panel build. The box build will confirm the count and the even-page signature.
- Numbered chapters: 1,728 to 2,052 words each, closers included.

## Per file

| File | Before | After | Delta | Sim | 6-gram reuse | H1 changed | What changed |
|---|---:|---:|---:|---:|---:|---|---|
| `00-half-title.md` | 7 | 7 | 0 | 1.00 | 1.00 | no | Unchanged: title only. |
| `00-title-page.md` | 24 | 24 | 0 | 1.00 | 1.00 | no | Unchanged: title, subtitle, byline, hub. The "Review draft" line is binder-drawn, not in this file (box step 3). |
| `00-dedication.md` | 110 | 110 | 0 | 1.00 | 1.00 | no | Unchanged: locked front matter with no IP content (see OPEN-QUESTIONS on "for Evan"). |
| `00-contents.md` | 216 | 216 | 0 | 1.00 | 1.00 | no | Unchanged: locked titles, plain-caps PART bands, no `##`. |
| `00-copyright.md` | 318 | 280 | -38 | 0.83 | 0.82 | no | The Lewis note is replaced with the locked acknowledgment under **A note on the four marks**. The exact Biblica NIV notice is added, with "Unless otherwise noted..." on its own line. Rights, publisher, ISBN TBD, first edition, disclaimer and composites note are kept. |
| `00-introduction.md` | 1407 | 1502 | 95 | 0.58 | 0.20 | no | Redrafted in a new order. "What this book claims" makes the book's own claim (old truths, new words) with no Lewis, followed by the new creed once and the four mark names. Adds a one-paragraph inheritance anchor. All four closer lines start "The first/second/third/fourth line, **X**" (panel fix extended). The panel's timebox path and the roster of men are kept, which accounts for most of the remaining overlap. |
| `01-a-quiet-tuesday.md` | 1989 | 1931 | -58 | 0.28 | 0.02 | no | Fresh prose. Opens with the four men, then "decided on Tuesdays". Anthony's day runs backward from 8:40. Eli's ten o'clock and Walt's facts are kept. |
| `02-you-are-not-crazy.md` | 1679 | 1728 | 49 | 0.25 | 0.02 | no | Fresh prose and a new order: diner, damage, the six maps as prose paragraphs (not a contrast list), every age, then Genesis 1:27 last. |
| `03-the-four-marks.md` | 1646 | 1832 | 186 | 0.44 | 0.05 | no | The definition chapter. New definition paragraph with the creed in bold. Lewis line removed. One section per new mark with its verse (James 4:17, Galatians 6:5, John 10:4, Colossians 3:23-24; the last three blocks are new). Inheritance taught in the Work for God's Pay section. "Why these four" rewritten as one life from four sides, with no derivation. Phil 2:5 kept as the frame. Creed ×2 (definition and Carry this). Composites paragraph dropped; the intro carries it. |
| `04-stop-waiting.md` | 1869 | 1952 | 83 | 0.27 | 0.02 | no | Stop Waiting named ×3. "Rejects passivity" line removed. James 4:17 moved up. "Where are you" kept. Gift-not-wages anchor added. |
| `05-pick-up-the-weight.md` | 1998 | 2029 | 31 | 0.19 | 0.01 | no | Pick Up the Weight named ×3. Opens with the panel's Tomás broke-Tuesday scene (all facts kept). "Responsibility" wording gone. "Absence purchased with a bigger paycheck is still absence" kept as Carry this. |
| `06-go-first.md` | 1762 | 1836 | 74 | 0.17 | 0.01 | no | Go First named ×4. John 10:4 block added. Panel lines "On your own, say Sunday and drive" and "Your number is second" kept. The "friends slept" Gethsemane beat dropped (card fence). |
| `07-live-for-a-reward-that-lasts.md` | 1733 | 1951 | 218 | 0.55 | 0.08 | no | Body names its mark as **Work for God's Pay** (×2). New section "The pay is an inheritance" with an Ephesians 2:8-10 block (added). Creed ×1 in "One man". The panel's single-man couch and "wife or roommate" (body and Do this week) are kept. Similarity is high mainly because of the seven verse blocks. |
| `08-the-empty-chair.md` | 1888 | 1967 | 79 | 0.22 | 0.01 | no | Fresh prose, dead serious. Psalm 68 moved to right after Curtis's sink. Both protected lines kept. |
| `09-anger-the-itch-and-the-drift.md` | 1953 | 2006 | 53 | 0.29 | 0.03 | no | Exits reordered to drift, itch, anger. The panel's Owen mailbox friction beat is kept. "Pain was looking for a Father" kept. |
| `10-the-father-who-does-not-leave.md` | 1876 | 1954 | 78 | 0.23 | 0.02 | no | "Three sentences a boy needs from his father" recast as one act of the Father (L39). "Real man" removed. Luke 15:20 moved to the Curtis climax. |
| `11-when-home-never-handed-you-off.md` | 1855 | 1931 | 76 | 0.29 | 0.01 | no | Fresh prose. New section, "The woman who kept the porch light on": mom is not the villain. Jacob, David, Paul. Stop Waiting named ×1. |
| `12-leave-without-slamming-the-door.md` | 1891 | 1955 | 64 | 0.28 | 0.00 | no | Fresh prose. The four-marks paragraph is rewritten without the old nouns. Grant's porch talk is kept as his own story, with no "four things" count. Pick Up the Weight named ×1. |
| `13-a-man-with-no-brothers.md` | 1941 | 2022 | 81 | 0.23 | 0.02 | no | The panel's Kenny scene and the "which row to put you in" line are kept. The three-question list is now prose. "Better man" removed. Carry this keeps "twenty minutes, every week". |
| `14-ask-the-man.md` | 1880 | 1958 | 78 | 0.25 | 0.04 | no | "Ride with me" kept. "Real man" becomes "a faithful man". The how-to steps are now prose pictures. |
| `15-the-problem-inside.md` | 1855 | 1935 | 80 | 0.25 | 0.01 | no | Fresh prose with almost no humor. Wade's story gets its own section. "Paint's not going to fix that" kept. |
| `16-how-that-looks-on-a-man.md` | 1871 | 1964 | 93 | 0.30 | 0.01 | no | The foyer and the seven shapes are kept. David's fall is retold as story, with no line-up of marks against his sins. Inheritance anchor added (L17). |
| `17-no-fixed-star.md` | 1890 | 1979 | 89 | 0.30 | 0.01 | no | Level and plumb line kept, plus a new fog-and-fence-post picture. "String on the wall" kept. No recital of the four. |
| `18-before-the-fall.md` | 1980 | 1994 | 14 | 0.35 | 0.01 | no | Rebuilt in its own shape (dust and breath, blessed first, a job site, rest, not good, naming, nothing to hide). No work/command/woman triad. "Provider and protector" removed. |
| `19-two-men-two-ways.md` | 1980 | 2052 | 72 | 0.45 | 0.01 | no | Every mark-mapping device removed. Two Adams taught as story and gospel. One unenumerated link sentence (L116). Philippians 2:9-11 dropped. Prose-only similarity is about 0.24; the rest is 12 verse blocks. |
| `20-destiny-is-not-a-vibe.md` | 1869 | 1924 | 55 | 0.31 | 0.01 | no | Fresh prose and reordered. The "first shape" list has no bride item. Well-done anchor added (L58). |
| `21-if-there-is-no-wife-yet.md` | 1855 | 1942 | 87 | 0.29 | 0.04 | no | "A real man rejects passivity" becomes "That's what Stop Waiting is for, and it applies to courting too." "No wife yet still leaves you a man" kept. |
| `22-know-her.md` | 1873 | 1948 | 75 | 0.30 | 0.06 | no | "Stop Waiting, in a marriage, looks like study." The panel's single and divorced branches and "ask your kids' mother one question about them" are kept. |
| `23-lay-it-down.md` | 1882 | 1963 | 81 | 0.28 | 0.02 | no | Fresh prose. The panel's divorced branch and "your children's mother" are kept. "Not a pay scale" anchor added (L78). |
| `24-what-she-actually-needs.md` | 1854 | 1936 | 82 | 0.25 | 0.04 | no | The panel opener "I will give you the whole chapter in two sentences first." is kept, along with the furnace and funeral lines and the divorced and no-wife branches. No provide/protect/lead triad. "Weeknight" removed. |
| `25-the-bed-is-a-covenant.md` | 1932 | 1996 | 64 | 0.30 | 0.03 | no | The panel's Eli paragraph and "A contract keeps score on her" are kept. Single section split (no wife yet / a wife once). Serious throughout. "Weeknight" removed. |
| `26-your-daughter-is-watching.md` | 1885 | 1973 | 88 | 0.30 | 0.03 | no | "I come to watch you" and the no-daughter branch are kept. The four-marks line becomes a single naming of Go First. |
| `27-give-your-son-a-name.md` | 1698 | 1766 | 68 | 0.28 | 0.01 | no | Old creed removed. "The three names" becomes "The name under all the others" (no count). The blessing has no count. No "weeknight", code, cause or ceremony. No-son branch kept. |
| `28-give-your-son-a-hill.md` | 1864 | 1941 | 77 | 0.21 | 0.01 | no | "I figured you could" and "right hill" kept. "The hills, by age" removed. Stop Waiting named ×1. Closing blessing's Isaac line corrected (Abraham laid the wood). |
| `29-give-your-son-a-day-he-will-not-forget.md` | 1872 | 1938 | 66 | 0.24 | 0.01 | no | "The day", never a ceremony. No creed or four-mark recital; the father speaks his own line (L28). Knife dropped from the keepsakes. Divorced-dad and no-son branches kept. |
| `30-you-were-made-for-a-work.md` | 1835 | 1898 | 63 | 0.28 | 0.02 | no | Work for God's Pay named. Colossians 3:23-24 block added. Inheritance anchor at L22. "Greater reward" removed. |
| `31-feelings-are-the-dash-not-the-wheel.md` | 1834 | 1917 | 83 | 0.26 | 0.01 | no | Fresh prose and reordered. Vernon kept. "The marks hold" without listing them. |
| `32-every-season-still-counts.md` | 1850 | 1939 | 89 | 0.30 | 0.01 | no | Old creed removed and the new creed not used. Inheritance anchor at L16. "The season nobody plans", "February has a job" and "Gardens change" kept. Age band removed. |
| `33-what-you-are-building-when-nobody-claps.md` | 1836 | 1922 | 86 | 0.22 | 0.05 | no | Work for God's Pay named ×2. Inheritance anchor at L31. The "three sentences" blessing has no count. |
| `34-write-the-next-move.md` | 1814 | 1951 | 137 | 0.13 | 0.09 | no | Redrafted from a fresh outline. The plan's top line is the new creed (L45), with an inheritance anchor (L47). Original one-page form, no past/present/future. Hollis's, Roy's and Mr. Pruitt's lines kept. |
| `35-these-men-are-my-brothers.md` | 1732 | 1804 | 72 | 0.29 | 0.03 | no | Creed ×1 ("Once more"). Carry this is exactly "Tuesday is when it will show. Get up." Kenny is named, with his Tuesday call. "Open chair" kept. The base's Gethsemane mark-mapping (L66) is replaced (L74). Inheritance anchors at L44 and L83. |
| `36-about-the-author.md` | 310 | 324 | 14 | 0.77 | 0.27 | no | Same approved facts, fresh sentences. No Lewis. |
| `37-condensed-training.md` | 351 | 348 | -3 | 0.90 | 0.66 | no | Light reword around the locked chapter-title list (the list is most of the file). |
| `wrap-back-copy.md` | 120 | 121 | 1 | 0.71 | 0.35 | no | New creed once. Internal note no longer repeats it. Hook reworded with no "real man". Category, hub and author kept. |

## Global changes

- All 158 margin blocks use the locked `**Book C:V NIV**` reference line with no wrapping quote marks, and are verified against the NIV (`SCRIPTURE-COUNT.md`). The base used `Ref (NIV)` with the verse in quotes; the binder only reads a cite when the line starts with `**` and contains `NIV`, so the base's margin cites would not have been picked up as cites.
- Every `**Carry this**` lost its `:::notes` block (the base had one in most chapters).
- Pronouns for God and Jesus use the base's convention (He, His, Him) in prose; margin blocks keep the NIV's lowercase.
- Section heads are fresh in most chapters. `## Before you turn the page` is used in every chapter that had a closing-blessing section (ch18's short "Before you turn" was aligned). Ch19 has none, as in the base, and ch35 keeps `## Before you close the book`.
- Em and en dashes: 0. Prose lines starting with a closer label: 0. The binder's own `parse_md` and `parse_closer_sections` (run by `tools/binder_parse_check.py`) parse every chapter with four closer sections in order (`be a brother` in ch35), write-in lines on the first three, none on Carry this, and no intro closer.
