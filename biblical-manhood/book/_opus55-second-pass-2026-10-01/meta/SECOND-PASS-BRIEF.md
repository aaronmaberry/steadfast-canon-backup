# Second-pass brief: *Steadfast Men* (Opus 5.5)

> **Copy note (2026-10-01).** This is an edited working copy. Per Aaron, references to the byline's nature were removed, and the About the Author item (L1) is superseded: the original bio is restored. The unedited original is on the box at `/workspace/ip-review/`.


Prepared 2026-10-01 (CT). Owner: Aaron Maberry. Byline: **Wes Hart**.
This is a **tightening pass, not a rewrite.** Same voice, same people, same structure. The book should come out a little shorter.

## Inputs

**Start from:**
- Your first pass, `biblical-manhood/book/_opus55-ip-rewrite-2026-10-01/` (Origin branch `opus55-ip-rewrite-2026-10-01`).
- **Copy it** to `biblical-manhood/book/_opus55-second-pass-2026-10-01/` (`book/`, `meta/`) and work only there.
- Persist only by committing to a new branch `opus55-second-pass-2026-10-01`.

**Read first:**
1. `meta/FOCUS-GROUP-2026-10-01.md`: the panel. Top 10, per-chapter notes with file:line, keep list, flagged lines.
2. `meta/NIV-AUDIT-2026-10-01.tsv`: a raw NIV re-fetch of all 158 margin blocks.
3. The original rules: `/workspace/ip-review/OPUS55-REWRITE-BRIEF.md` (attached). **Every rule there still applies** unless this brief changes it.

Line numbers below refer to the first-pass files.

## 1. LOCKED by Aaron on 2026-10-01 (do not reopen)

### L1. About the Author (superseded 2026-10-01: original bio restored)

The current `36-about-the-author.md` is invented. Rewrite it at about 80–150 words.

**Allowed**
- The book is meant to stand on Scripture.
- What Steadfast Men is: a twenty-four-week training for men in every season, which this book grew alongside.
- Where to find it: **walksteadfast.com**, for the class and to bring it to a church or group.

**Not allowed**
- Any career, job, family, wife, kids, state or town, church, title, credential, teaching history ("taught in living rooms, garages…"), personal-rescue story, or hobbies.
- "Not a pastor / not a counselor" also stays out unless Aaron supplies it.

**Same section, two body lines that imply clergy standing.** Recast these as a guest's or friend's view:
- `26:3` "Officiating a wedding gets me the best spot in the building."
- `24:7` "I've stood up front at enough services…"

Leave the other first-person stories alone. Aaron is deciding which are his (FOCUS-GROUP "What Aaron must decide" #1).

### L2. NIV margin blocks are word for word and punctuation for punctuation

- **The rule.** Every `:::margin` block reproduces the NIV 2011 exactly: words, capitals, commas, semicolons, colons, question and exclamation marks, and **the NIV's own em dashes (—)**.
- **The no-dash rule now applies only to prose outside Scripture blocks.** Prose sentences that quote Scripture inline should still avoid dashes: paraphrase, or move the verse to a margin block.
- **Restore the dropped dashes** (NIV text quoted exactly):
  - `07:50` Ephesians 2:8-10: `For it is by grace you have been saved, through faith—and this is not from yourselves, it is the gift of God— not by works, so that no one can boast.` Keep the space after the second dash exactly as the NIV prints it on Bible Gateway, and confirm against a second NIV source. If the print NIV has no space, use no space and note it.
  - `22:17` John 10:14: ends `my sheep know me—`
  - `32:26` Ecclesiastes 12:1: ends `"I find no pleasure in them"—`
- **Quotation marks at excerpt edges** (pending Aaron's one-word confirmation; this is the default):
  - A dangling opening or closing mark that belongs to speech beginning or ending outside the cited verses **may be dropped**.
  - Marks are **never added**. Where the cited verse leaves speech unclosed, print it as the NIV does, or extend the citation by one verse.
  - Nested quotes keep the NIV's levels: single stays single.
- **Fix these blocks**, which currently add or re-level marks (see the TSV):
  - `06:47` Judges 7:17
  - `10:24` John 14:9
  - `11:45` 1 Kings 2:2-3
  - `16:77` 2 Samuel 12:7
  - `16:90` 2 Samuel 12:13
  - `17:62` Amos 7:7-8
  - `20:52` John 4:34
  - `28:56` 1 Samuel 17:34-35
  - `29:14` Joshua 4:6-7
  - `34:20` Habakkuk 2:2
  - `07:56` Matthew 25:21 (outer double dropped, inner single raised to double; restore the single quotes)
  - `25:38` Ephesians 5:31
  - `01:50` Luke 16:10
- **Re-verify all 158 blocks** against the NIV 2011 and write the result into `meta/SCRIPTURE-COUNT.md`: one row per block with status `EXACT`, `EXACT-EDGE-DROP` (and which mark) or `EXCERPT`.
- **Patch `meta/tools/niv_verify.py`:** `house_style()` and `--fix` currently turn dashes into commas. Make them compare raw, with only the edge-drop allowance.

### L3. Ch7 is renamed "Work for God's Pay"

- `07:1` → `# 7. Work for God's Pay`
- `00-contents.md:24` "Live for a Reward That Lasts" → "Work for God's Pay". Keep the file's unnumbered format.
- `37-condensed-training.md:17` "7. Live for a Reward That Lasts" → "7. Work for God's Pay".
- `03:84`: "**Live for a Reward That Lasts** follows that hunt" → "**Work for God's Pay** follows that hunt"
- Search all files for any other reference to the old chapter title and update it.
- `07:106` "Live for the reward that lasts." stays as an echo line.
- **Keep the file name** `07-live-for-a-reward-that-lasts.md`. The binder's `CHAPTER_FILES` (`book/tools/make_ebook_pdf.py:70`) and the audio scripts key on it, and the running head comes from the H1.
- `biblical-manhood/BOOK-TOC.md:19` is outside your folder. **Don't edit it.** List it in your report. The box syncs it.

**The rename has conditions** (theology seat and Frank). Do these in ch7:
- The inheritance sentence (Col 3:24, grace, Eph 2:8-10) goes in the **opening section** (around `07:7`), not first at `07:44`.
- Fix #2 below.

## 2. The fixes, in priority order

The full detail and every line reference are in FOCUS-GROUP. Below is what to do.

### Fix 1. Recurring men must be consistent

- **Dale.** Keep ch13's Dale (`13:5`, `13:95`, `34:53`, `34:65`, `35:32`). Give new, unused names to Renee's husband (ch24) and the county grader (ch30). Check every name in the book for collisions before you choose.
- **Wade.** ch15 (`15:47`) and ch26 (`26:11`) are one man. Add a clause in ch26.
- **ch33.** `33:46` gives Roy's grandson a plumb bob. It belongs to Alton's boy (ch29), so fix it or cut it. `33:79`: change "fence" to the creek.
- **Walt.** `35:30` and `35:55` refer to a parking-lot scene that never happens. Point them at what's on the page (`01:5`, `32:55`).
- **Hollis.** `35:44`: match it to ch34 (he wrote "Tell Cole he's a good man," said it, and Cole cried in his truck).
- **Mr. Pruitt.** Introduce him at `07:73`. Give him one or two sentences in ch21's widower section (`21:31`–`37`).
- **Micah.** Name the moving-box man in ch21 (`21:3`, `21:102`) Micah, consistent with `intro:53`, `32:29` and `35:32`.
- **ch33.** `33:50`: explain "Thursday table" or cut it.

### Fix 2. Ch7 speaks family, not accounting

- Cut the commerce stack:
  - `07:7` "a return"
  - `07:13` "payroll"
  - `07:33` "keeps the books"
  - `07:62` "ran the numbers"
  - `07:73` "ledger"
  - `07:75` "only math that works"
  - `07:86` "did the math"
  - `07:96` "the check cleared"
- At most one money image, and only for the false pay.
- `07:128`: change "pays for secret work" to "rewards".
- Outside ch7: `03:90`, `33:31` ("pays best"), `33:94` ("keeping count").
- Keep the "pay" wording in the creed and the mark name. Do not re-word those.

### Fix 3. Use the inheritance anchor less

- **Keep it in full** at `intro:17`, `03:82`, ch7 (opening plus `07:44`–`53`), `30:22` and `34:47`.
- **Keep one clause** in ch33.
- **Everywhere else,** anchor only if the same paragraph uses pay, reward or wages.
- **Cut or trim** `04:108`, `05:103`, `06:31`, `16:17`, `20:58`, `21:112`, `23:78` (keep it short), `24:29`, `25:71`, `32:16`, and the tail of `35:44` (keep `35:83`).
- **Update `meta/THEOLOGY-PAY.md`.** Every surviving pay or reward use still needs its anchor (original brief §2): no "work hard and God will save you" reading.

### Fix 4. Stop repeating pictures

- **Caregiver who bathes his wife.** Name him Mr. Alvarez at `23:84`, call back at ch35 (`35:20`) and `32:87`. Cut `25:91` and `30:82`. Reconcile the years.
- **Coffee for the wife.** One man only. Choose between Roy (`33:56`, `35:38`) and Alton (`30:57`), and cut the generic repeat at `09:78`.
- **Plumb bob.** `29:36` re-teaches it; keep ch17 as the place it's taught.
- **Check-in questions.** Vary `22:56` so it doesn't echo `13:77`.
- **Adam's silence.** Keep ch19 and one glance in ch4 (`04:66`). Cut `03:32`'s version and `15:19`/`15:29`.
- **The feelings-first-books jab.** Keep `intro:15` and cut `02:33`.

### Fix 5. Vary the season roll calls (never drop a branch)

- Fold the single, divorced, widowed, no-child, older and high-performer content into scenes and closers.
- Keep standalone season sections only in ch8, 9, 21, 22, 23, 25, 26 and 32.
- Cut empty one-liners (e.g. `18:150`, `31:81`).
- Don't run the seasons in the same order twice in a row.
- "Single?" lines that only say "ask your mom" (`22:99`, `24:90`) get a second option.
- Give the high performer at least one line with weight inside a scene, not only as the last line of a list.

### Fix 6. Reshape the last course-shaped devices

These are about the idea's shape, not the wording.

- **(a) ch20.** `20:60` and `20:119`: drop the "pattern from Eden" list and the card heading. Make it Genesis narrative and the reader's own ground.
- **(b) ch15.** `15:19`: cut the four-beat Adam inventory.
- **(c) ch13.** `13:28`: cut "knowing full well they'd doze off". Keep the request.
- **(d) ch29.** Compress `29:42`–`59` into one short paragraph of principles. No "Then… Then…" sequence and no "bring three things" template. The creek scene stays.
- **(e) ch11.** `11:40`/`11:58`: drop the four-part list. Let David and Paul carry it.
- **(f) ch12.** `12:73`: collapse Grant's method paragraph to 2–3 sentences, with no sequence. The scene, his sentence and "You eat yet?" stay.
- **Keep:**
  - ch19's two gardens, still with no mark names inside it.
  - ch19's Do this week.
  - ch26's Ephesians 6:4.
- **Vary `22:68`** so it isn't a five-languages summary.

### Fix 7. NIV

Do everything in L2.

### Fix 8. About the Author and the clergy lines

Do everything in L1.

### Fix 9. Capitalize pronouns for God

In prose, God and Jesus take He, His, Him. Sweep every file. The worst offenders are ch8, 9 and 10, plus `06:44`, `15:21`, `30:95`, `31:13`, `31:107`, `33:11` and `33:18`.

**Margin blocks keep the NIV's lowercase.**

### Fix 10. Lines and small errors

- **Soften or trim:**
  - `01:65`, `04:20`, `06:89`, `07:75`, `12:7`, `16:28`, `17:103`, `21:13`, `21:104`
  - `25:48`: let it take longer.
  - `33:83` "Gold." and `35:66`
- **Clarify:**
  - `11:74` "them": the antecedent is unclear.
  - `13:91`: muddy.
  - `05:126`: the single option doesn't fit a young man.
  - `31:101`: write "tell them", not "tell him", for the doctor.
- **Theology:**
  - `03:54` and `05:5` "even when somebody else dropped it": say when a dropped load becomes yours, and keep Gal 6:2 and 6:5 distinct (tie to `05:79`).
  - `19:60`: change "as if the guilt were His own" to "with our guilt laid on Him".
  - `20:17`: paraphrase Zechariah 4:10 accurately (the day of small things; the plumb line in Zerubbabel's hand).
- **ch7.** `07:92` and `07:128` repeat a list. Keep it once.
- **Heading.** Use `## Before you turn the page` everywhere (`16:104`, `17:125`, `20:98`, `21:116`, `22:109`).
- **Length.** ch5 (2,029), ch9 (2,006), ch13 (2,022) and ch19 (2,052) must come in at ≤2,000.

## 3. Don't break

Treat the FOCUS-GROUP "Keep, and don't break" list as locked:
- every protected line;
- every divorced, single, widowed and no-child branch;
- the intro's shorter road;
- the copyright acknowledgment and Biblica notice, word for word;
- the dedication text (locked; Aaron is checking it).

If a fix seems to need a protected line changed, don't change it. Put it in OPEN-QUESTIONS.

## 4. Rules carried over from the original brief (short form)

- **Read-only outside your output folder.** No push to main, merge, PR, publish, Drive upload or deploy. No spend. **No Unslop.**
- **Transcripts and course files are reference only.** No wording, outlines, lists, stories or sequencing from them.
- **Same 44 files, same names, same 35-chapter structure and parts.** H1s are unchanged except ch7 (L3). Drop any stray backup files.
- **Length.**
  - Each chapter 1,700–2,000 words, with no chapter over 2,000.
  - Book total within ±5% of 68.7k (65.3k–72.1k). Aim at or below the first pass's 70,666.
- **Binder conventions, exactly** (original brief §6):
  - `# N. Title`, then `##` sections.
  - `:::margin` / `**Book C:V NIV**` / text / `:::`, placed immediately after the sentence that cites it.
  - Closer: `## Your Turn` with **Name it**, **Do this week**, **Tell a brother** (ch35 uses **Be a brother**) and **Carry this**. `:::notes` goes on the first three only.
  - Never start a prose line with a closer label.
  - `00-contents` uses plain-caps PART bands with no `##`.
- **No em or en dashes in prose.** Scripture blocks are exempt (L2).
- **Creed, verbatim, only at these placements:** intro 1, ch3 ≤2, ch7 1, ch34 1, ch35 1, wrap 1.
- **Lewis appears only** in the locked copyright acknowledgment. The retired-wording sweep regex from the original brief §7.4 must return 0 elsewhere.
- **Never use "Go First" as a product title.** "A steadfast man…", never "A real man…".
- Under 500 unique verses.
- Persona: warm first, one clean hit, stay, next move. No fake Wes Hart biography anywhere.

## 5. Deliverables (in `_opus55-second-pass-2026-10-01/meta/` plus a tar.gz artifact)

1. `CHANGELOG.md`: one row per fix item (Fix 1–10, L1–L3) with file:line before and after, and what changed.
2. Updated `REWRITE-REPORT.md` (word counts per file against the first pass and the base), `SWEEP.md` (retired-wording regex, 8-word transcript overlap, creed counts, prose dash count of 0, margin dash count) and `SCRIPTURE-COUNT.md` (per-block NIV status, L2).
3. Updated `THEOLOGY-PAY.md` and `OPEN-QUESTIONS.md` (only what's still open for Aaron).
4. A binder parse check on every chapter: margin blocks, closers and H1s parse. The result is in the report.
5. A final report covering:
   - the before and after of ch7's opening section and the new About the Author;
   - the three restored NIV blocks;
   - the name changes (old → new, file:line);
   - word totals;
   - the artifact path.

## 6. Box-side steps (the parent and box do these after your text lands; list any others you find)

1. Sync `BOOK-TOC.md` line 19 to "7. Work for God's Pay" in the repo, `/workspace/biblical-manhood/BOOK-TOC.md` and `/workspace/steadfast-kb-seed/03-book/BOOK-TOC.md`.
2. **Binder `no_em()`** (`make_ebook_pdf.py:108`, applied at `:194`) currently runs on margin text too. Exempt `:::margin` blocks so the NIV dashes print as em dashes.
3. Set the `render_03_figure.py` MARKS labels to the new marks and re-render.
4. Set `apply_wrap_back.py` CREED to the new creed (plus the back-cover inheritance line, if Aaron approves it), re-apply `a-wrap.png`, and update `wrap-back-copy.md`.
5. `page_copyright()` must render `00-copyright.md` (the Lewis acknowledgment and full Biblica notice). Remove "Review draft. Not for distribution." from the title page (`make_ebook_pdf.py:649`).
6. Build locally only, with ART/PRESS/FONTS/FIGURES reset to the rewrite folder. Check the page count (about 240) and the even-page signature. No Drive upload until Aaron approves.
