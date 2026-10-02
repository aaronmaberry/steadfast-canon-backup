# IP checklist (brief §3)

Each item from the 2026-10-01 IP report, as a book action, with where it was found in the base (`_grok47-panel-rev-2026-09-25/book/`, "base") and the evidence in this rewrite (`_opus55-ip-rewrite-2026-10-01/book/`, "new"). Line numbers are 1-based. Sweep outputs are in `SWEEP.md`.

## 1. Lewis's wording and close paraphrases removed everywhere — DONE

- **Found in base:** the full creed in copyright L26, intro L19, ch3 L15/L105, ch7 L99, ch27 L28, ch32 L100, ch34 L37, ch35 L64, wrap L6/L14; single-mark phrases in ch3 L28/36/42/48/54, ch4 L7, ch7 L7, ch19 L111, ch21 L80, ch22 L24, ch30 L41, ch32 L98, ch33 L18, ch35 L33 (inventory row A).
- **Handled:** every sentence rewritten. No "rejects/accepts/leads/expects" phrasing, no "A real man...", no imperative set, no "invests eternally", no noun rail of the four, and no synonym rebuilds ("refuses inaction", "embraces duty", "owns responsibility", "leads with courage" are all in the extra-fence regex).
- **Evidence:** brief regex over `book/` returns 5 hits, all on `00-copyright.md` L28 (the locked acknowledgment). The extra-fence regex returns 1 hit, the same line. "Passive"/"passivity" survive only as plain descriptions of the sin (e.g. ch2, the freeze; ch21 L62 "the true name for that is passive").
- **New marks in their place:** the intro names all four once (L13). Ch3 heads are L28 `## Stop Waiting`, L43 `## Pick Up the Weight`, L56 `## Go First`, L69 `## Work for God's Pay`. Ch4–7 name their marks by title (ch4 ×3, ch5 ×3, ch6 ×4, ch7 ×2; see SWEEP §6). Chapters that lean on one mark name only that one, in fresh words (e.g. ch21 L62, ch22 L37, ch24 L50, ch28 L29, ch30 L20).

## 2. Every mention of Lewis, RMDK, Men's Fraternity, Authentic Manhood, Fellowship Bible Church, "a pastor in Little Rock" and Better Man removed outside the copyright page — DONE

- **Found in base:** intro L17 ("Robert Lewis, at Fellowship Bible Church in Little Rock ... *Raising a Modern-Day Knight*"), ch3 L13 ("Robert Lewis is the one who formed the sentence this way"), copyright L26.
- **Evidence:** the brief regex (which includes `\bLewis\b`, `Little Rock`, `Better Man`, `knight`, `squire`) hits only `00-copyright.md` L28. Intro, back cover (`wrap-back-copy.md`), About the Author (`36`) and Condensed Training (`37`) have zero hits. The words "weeknight" (which contains "knight") and "better man" were also kept out of the prose.
- No "gave it to us" or handoff phrasing anywhere (extra-fence regex, 0 hits).

## 3. Copyright page acknowledgment — DONE

- `00-copyright.md` L26 `**A note on the four marks**`, then L28, verbatim:
  > The four principles behind these marks owe a debt to Robert Lewis's teaching on manhood (*Raising a Modern-Day Knight*, 1997). Steadfast Men is independent and is not affiliated with or endorsed by Robert Lewis, Men's Fraternity, or Authentic Manhood.
- Lewis's sentence is not quoted. The rest of the page is kept: rights (L6-10), publisher and hub (L12-13), ISBN TBD (L19-20), first edition (L22), the disclaimer and composite-men note (L32-36).

## 4. NIV acknowledgment (Biblica) — DONE

- `00-copyright.md` L15, verbatim: "Scripture quotations taken from The Holy Bible, New International Version® NIV® Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.™ Used by permission. All rights reserved worldwide."
- L17: "Unless otherwise noted, Scripture quotations in this book are from the NIV."
- **Count:** 158 margin blocks, **179 unique verses** (limit 500). No complete book. Margin Scripture is about 4,200 of ~70,600 words (~6%; limit 25%). Every block is checked against the NIV (2011 text on Bible Gateway): 141 exact, 7 contiguous word-for-word excerpts, and 10 with every word identical where the only difference is excerpt punctuation. Every reference line reads `**Book C:V NIV**`. Four base errors were corrected (John 18:8, Numbers 8:26, 1 Kings 19:4, Isaiah 46:4). Details in `SCRIPTURE-COUNT.md`.

## 5. Sentence vs. structure; 8–10-word runs vs. Tim's transcripts — DONE

- **Base:** 49 runs. The only non-Scripture runs were the creed (in copyright, intro, ch3, ch7, ch27, ch32, ch34, ch35, wrap).
- **New:** an 8-word window scan of all 44 files against all 33 `transcripts/*.md` finds **0 runs in prose** (everything outside margin blocks). 32 of 158 margin blocks match a transcript, all of them Tim reading the same NIV verse, which is allowed. The first full pass found two incidental prose runs, both reworded: ch4 L59 (a Genesis 3:8 phrase) and ch13 L15 (the idiom "to look you in the eye and say").
- **Process control:** chapter writers were told not to open `transcripts/`, `briefs/`, `notes/`, `PHD-MASTERY.md` or `FRAMEWORK.md` (`DRAFTING-RULES.md`). No numbered list follows the course's order. No Mead, Keillor, Newsweek or Levinson material (extra-fence regex, 0 hits). No Tim Hawks family stories.
- **Structural fixes beyond the n-gram scan:** ch12 L75, the porch talk is no longer counted as "four things". Ch13 L41-61, the "three questions" list is now prose. Ch18 no longer runs Genesis 2 as work / command / woman. Ch28 no longer uses "The hills, by age". Ch32 no longer uses the "thirty-five to fifty-five" age band.

## 6. Sub-points recast or avoided — DONE

| Sub-point | Base | New |
|---|---|---|
| "three things every son needs from his father" | ch10 L48 "Three sentences a boy needs from his father. You are mine. I love you. I am pleased with you."; ch27 "## The three names" (Mine / What I see / Man) and a weekly blessing of "Three sentences. Identity. Sight. God."; ch33 L51 and ch35 L21 "three sentences" | ch10 L39 now tells Matthew 3:17 as one act: "The Father claimed His Son out loud, called Him loved, called Him a delight, and the public work came after." Ch27 L19 is now "## The name under all the others": one name, said many ways, with no count or ordinals. The blessing is a short sample in a father's own voice, with no count. The closing three-beat in ch27 L73 was cut to "you're Mine, and I'm glad you're home." Ch33 and ch35 have no count. |
| conventional-vs-authentic manhood contrast list | not present as a list; ch2's "six maps" checked | ch2's six maps are separate prose paragraphs about the culture's competing pictures, not a two-column contrast. |
| "bearers of destiny" / "nurturers of life" | not present | still absent (extra-fence regex, 0). |
| "a will to obey, a work to do, a woman to love" | banned; ch18 ran work → command → woman | ch18 reshaped: Dust and breath / Blessed first / A place, and a job site / A day to stop / Not good / His first words / Nothing to hide. The command sits inside "take care of it". Ch20's "first shape" list has no bride item. |
| "direction, protection, provision" triad | ch18 L66, ch24 provide/protect | never listed together (extra-fence regex, 0). Ch24 has no "protect" and no triad. |

## 7. First Adam / last Adam — DONE

- **Base:** ch19 labeled each sin "The first/second/third/fourth mark flipped". It had "Four marks, all backward. Passive, evasive, hidden, grabbing", a "## Two ways, laid side by side" contrast section, and the mapping paragraph "Rejecting passivity is Rise, let us go...". Ch3 had heads "He rejects passivity / He accepts responsibility / He leads courageously / He expects the greater reward" and a section "Why four, and why these". **Also found in this pass:** ch35 base L66 mapped the four marks to four Gethsemane actions ("Up off the ground. Out to meet what was coming. His men covered. The work finished...").
- **New:**
  - Ch19 has heads Eden (L16), Gethsemane (L51), Whose you are (L94), Small gardens (L118), Every man in the room (L126) and Last Adam (L136). It teaches Paul's two Adams as story, sin and gospel, with no mark labels, no pairing and no table. The only link is one unenumerated sentence at L116: "Everything this book asks of a man, Jesus did first, and He did it for you."
  - Ch3's heads are the new mark names. "Why these four" (L86) explains the order as one life seen from four sides, each mark leaning on the one before. It makes no Adam/Jesus derivation.
  - Ch35 L74 now reads: "They're the family resemblance, and it comes from the Son who already did everything this book has asked of you, and did it for you." It makes no one-to-one mapping.
  - A search of every paragraph that pairs a mark with Jesus, Adam, garden or cross finds only single-mark references (listed in the drafting log).

## 8. Son chapters (27–29) kept original — DONE

- No knight, page, squire or stage language. The brief regex catches knight and squire; a word grep of 27–29 for code / cause / ceremony / ceremonies / stage / page finds only the `## Before you turn the page` heading.
- No "manhood ceremony"; ch29 calls it "the day" or "the morning" throughout.
- No vision/code/cause triad, and no sword, shield, crest or ring rite. In ch29 the keepsakes are a Bible, a watch, a tool or a plumb bob; the base's knife was dropped.
- Ch28 "The hills, by age" is gone. Hills are examples in prose under "Fit the hill to the actual kid, not the number on his cake."
- Ch29 L28: the father speaks his own words ("A man does what's his to do, even on the days nobody's looking. That's most of it."). There's no recital of the creed or the four marks; base L47 "The four marks followed, every word" is gone.
- Ch27: the old creed (base L28) is removed and the new creed is not used (SWEEP §5, 0).

## 9. Man plan (ch34) structurally original — DONE

- No past/present/future form and none of the 2021 worksheet's questions (no "What sort of 'old man' do I want to be?"). No SMART grid and no three-year plan.
- The plan is one page or index card, built line by line:
  - L45 the top line, the new creed in the reader's own handwriting; L47 the inheritance anchor;
  - then the circled faint mark, the exit word, a season sentence with a verb, a brother with a day and hour, the man ahead, the rhythm, the house, the work, and the drawer (the Nathan line);
  - and the move at the bottom: verb, person, day.
- Creed count in ch34: 1.
- The art `art/34-man-plan.png` (rendered by `render_34_man_plan.py`) carries no old wording ("THE COURSE THAT SITS STILL" / "THIS WEEK"). No change is needed.

## 10. Sequence — HELD

The chapter order and titles are locked and unchanged (all 35 H1 lines identical; see REWRITE-REPORT). Within chapters, the internal order, examples and sub-structure were rebuilt. Most writers reordered sections (e.g. ch1 opens with the four men; ch5 opens with Tomás's broke Tuesday; ch18, ch19, ch24, ch27-29 and ch34 were rebuilt from fresh outlines).

## 11. Public-claim wording — DONE

"Original to us", "used under license" and any license claim: extra-fence regex, 0 hits. The intro's claim paragraph (L9) says the book didn't discover what's in the sentence ("Every piece is older than all of us, and it's been sitting in plain view in the Bible the whole time") and claims only the wording. Note for the box: the binder's hard-coded `page_copyright()` prints "Original work. Cloth Store look." (see OPEN-QUESTIONS, box step 3).

## 12. Back cover / wrap copy — DONE

`wrap-back-copy.md`:
- The new creed appears once (the "Four marks" block). The internal note no longer repeats it.
- No Lewis and no "real man". The hook is kept and reworded to "the man who's tired of guessing what a man is".
- `CHRISTIAN LIVING / MEN`, `walksteadfast.com` and `Wes Hart` are present.
- There are no blurbs, no endorsements and no barcode.

## 13. Brand and trademark notes (report only, not prose)

- **STEADFAST** (Reg. 3870140, Rebecca Halstead, leadership and motivational speaking) and **STEADFAST LEGACY** (pending, workbooks): the book's title *Steadfast Men* and the name of the "twenty-four-week training" (intro L61, About L5 and L13, Condensed Training) use STEADFAST as a product or series name. This is the main item for the attorney. The prose also uses "steadfast" as an ordinary adjective (ch7 "There's an old word for a man like that. Steadfast."; the creed's "A steadfast man").
- **9MARKS:** "four marks" is used only as a descriptive label inside the book. It is never a product or series name. The wrap brief's block label "Four marks" is an internal heading, not a title.
- **I'LL GO FIRST** (Reg. 4642259, 6246089, 6025781): "Go First" is used as a chapter title (ch6) and a mark name. It also appears as class week 6 in `37-condensed-training.md`, as a session title inside the training. CANON allows that, but the attorney should see it before any course, podcast or workbook is named.
- No other mark name is used as a product, course, podcast, workbook or series title anywhere in `book/`.

## 14. Drafting history kept — DONE

`meta/DRAFTING-RULES.md` (the rules every writer worked from), `meta/REWRITE-REPORT.md` (before and after stats per file), `meta/DRAFTING-LOG.md` (who drafted what, the checks run, the fixes made after review), `meta/tools/` (the check scripts) and the git history on branch `opus55-ip-rewrite-2026-10-01` (commits through the pass).
