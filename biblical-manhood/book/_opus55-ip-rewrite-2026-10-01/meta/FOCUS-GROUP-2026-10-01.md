# Focus group: Opus 5.5 IP-clean rewrite, 2026-10-01

**Manuscript:** `biblical-manhood/book/_opus55-ip-rewrite-2026-10-01/book/` (44 files, 70,666 words; extracted from `cloud-agent-artifacts/bc-2121edb9-.../steadfast-men-opus55-ip-rewrite-2026-10-01.tar.gz`, same as Origin branch `opus55-ip-rewrite-2026-10-01`).
**Read with:** `meta/REWRITE-REPORT.md`, `meta/OPEN-QUESTIONS.md`, `meta/SWEEP.md`, `meta/SCRIPTURE-COUNT.md`.
**Rules:** `book/FOCUS-GROUP.md` (bounce only; panel does not rewrite; no spend, no publish) and the 9/21 bounce format (`reader-panel/grok47-bounce/PANEL-BOUNCE-GROK47-PRE-UNSLOP-2026-09-21.md`).
**Every note below cites `file:line` in the rewrite folder.** File names are shortened to their number (e.g. `07:96` = `07-live-for-a-reward-that-lasts.md` line 96; `intro` = `00-introduction.md`).

## How this panel was run (read this first)

- One executor read the whole manuscript once, front matter to back cover, every line, and wrote the notes from each seat's point of view. The seats were **not** run as independent parallel agents: this executor had no subagent tool, and the Grok Build CLI is reserved for code jobs. Treat the seats as structured lenses on one careful read, not as eleven separate readers.
- The roster is the locked five (Caleb, Marcus, Drew, James, Earl) plus the seats Aaron asked for on 2026-10-01: a 19-year-old, a widower, a high performer, a pastor/table leader, a theology reader on "God's pay" and inheritance, and an IP/originality reader.
- Independent checks run for this panel (scripts in `/workspace/ip-review/focus-group/` and `/workspace/ip-review/rename/fg_checks.py`):
  - Retired-wording and Lewis-name sweep: 0 hits outside the copyright acknowledgment (`00-copyright:28`).
  - 8-word overlap with all 88 transcript files, Scripture margins excluded: **0**. 6-word overlap: 8 hits, all stock phrases or Scripture ("so that nothing will hinder your prayers," "is my son whom I love").
  - Creed count: intro 1, ch3 2, ch7 1, ch34 1, ch35 1, wrap 1. Inside the limits.
  - Em/en dashes in the manuscript: 0.
  - NIV re-fetch of all 158 margin blocks (raw punctuation, `/workspace/ip-review/focus-group/niv-dash-audit.tsv`): 122 identical, 7 contiguous excerpts, 29 with punctuation differences. 3 of those 29 are dropped NIV em dashes; 26 are added or removed quotation marks at the edges.

## Settled by Aaron on 2026-10-01. The panel was told not to reopen these.

1. **About the Author is made up.** It gets rewritten as an honest short pen-name note for Wes Hart, with no invented career, family, church, places or credentials. Saying what Steadfast Men is and pointing to walksteadfast.com is fine.
2. **NIV margin blocks keep the NIV's own em dashes,** word for word and punctuation for punctuation, as the NIV 2011 prints them. The no-dash rule still holds for prose outside Scripture blocks. Every margin block gets re-verified.
3. **Chapter 7 is renamed "Work for God's Pay".** The rename covers the H1, `00-contents.md`, `BOOK-TOC.md` and every cross-reference.

The panel's comments below that touch these three items only cover how to carry them out.

---

## Verdict: HOLD for one more Opus pass, then build

- **The IP job is done.**
  - None of Lewis's wording is left, and there is no transcript overlap.
  - The acknowledgment and the Biblica notice are word for word.
  - The marks read as Steadfast's own.
  - No seat felt the book was standing on someone else's frame.
- **The bones are the strongest the panel has seen.** The Tuesday thesis, Tomás's broke Tuesday (`05:3`), the wound run, Kenny, Harlan, and the House chapters with real single and divorced branches all hold up.
- **What holds it back is mostly new problems the rewrite created:**
  - Recurring men collide or call back to scenes that never happened.
  - The "not wages, inheritance" disclaimer has become the new stamp, and ch7 still talks like a payroll office.
  - A few pictures repeat until they blur.
  - Every chapter now ends its body with the same season roll call.
  - A handful of the course's shapes still show through as ideas, never as wording.
- **None of this needs a restructure.** All of it is a tightening pass, and done right the book gets a little shorter.

**Buy or pass, as buyers today:** Jace, Caleb, Marcus, James, Luis: buy. Drew, Brandon, Earl, Frank: buy after the second pass. Theology: sign after the ch7 fixes. IP: clear for the manuscript (trademark clearance of STEADFAST is a separate, pre-print item for the attorney).

---

## Top 10 fixes, ranked

### 1. Fix the recurring men: name collisions and callbacks to scenes the reader never saw

ch35's roll call only lands if the reader trusts these men. Right now it can't.

- **Three different men named Dale.**
  - ER clipboard, then a Thursday brother: `13:5`, `13:95`. Also named at `34:53`, `34:65` and as Micah's breakfast man at `35:32`.
  - Renee's "good provider": `24:3`–`31`.
  - County grader: `30:3`–`97`.
  - Fix: keep ch13's Dale. Rename ch24's and ch30's with new names not used anywhere else in the book.
- **Wade.** ch15's Wade (`15:47`–`51`, who saw his daughter shrink) and ch26's Wade (`26:11`, Nora's softball) read like two strangers. Make them one man on purpose with a single clause in ch26 ("the same Wade who…"). That turns two scenes into an arc.
- **Plumb bob.** `33:46`: "Roy's grandson carries a plumb bob like the one his great-grandfather used" collides with Alton's plumb bob for his grandson (`29:3`, `29:30`–`40`). Make it Alton's boy, or cut the plumb bob from ch33.
- **Creek, not fence.** `33:79`: "A morning at a fence when you spoke a name over your son." The day in ch29 was at a creek. Fix the word.
- **Walt's parking lot.** `35:30` ("that bank parking lot: three hundred contacts, nobody to call") and `35:55` ("Walt came from a parking lot") call back a scene that never appears. It also borrows Dale's "hundreds of contacts" from `13:7`. Replace them with Walt's real on-page moment, the 6:15 fork and the shop quieter than the house (`01:5`, `32:55`), or plant one sentence earlier.
- **Hollis.** `35:44`: "Hollis walked across the lot to a stranger by a truck." That doesn't match his story (`34:5`): he wrote "Tell Cole he's a good man," said it, and Cole, a man he knew, sat in his truck and cried. Fix it to what happened.
- **Mr. Pruitt** first appears at `07:73` with no introduction ("Mr. Pruitt keeps his pecan trees like that"). Give him a clause where he first shows up.
- **Micah** is promised in the intro roster (`intro:53`) but never gets a scene, only `32:29` and `35:32`. The unnamed moving-box man in ch21 (`21:3`, `21:102`–`104`) fits Micah exactly, and ch35 already says a man told Micah "to quit asking permission". Name him Micah in ch21. That costs zero words.

### 2. Make ch7 sound like a Father, not a payroll office

Settled title: **Work for God's Pay**. The chapter now has to carry that word without a wage reading. The theology seat's specific lines:

- **Return on investment:** `07:7` "a man keeps paying those bills only if he trusts there's a return." Recast as trust in a Father who keeps His word.
- **Accounting stack:**
  - `07:13` "payroll", `07:33` "He keeps the books", `07:62` "ran the numbers", `07:73` "the ledger that matters", `07:75` "the only math that works", `07:86` "did the math with bigger numbers", `07:96` "the check cleared, and it was a small one."
  - Keep at most one money image, and use it for the *false* pay (the folding table and the trophy box are already perfect for that).
  - Use family and home words for God's side: son, Father, inheritance, welcome, "well done", the walk up to the house.
- **Wage verb:** `07:128` "the Father who sees in secret is the one who **pays for** secret work." Change it to "rewards".
- **Anchor placement:** put the inheritance sentence on ch7's first page, inside its opening section (now `07:7`). Right now the inheritance teaching doesn't arrive until `07:44`. With "Pay" in the TOC, the anchor has to come early.
- **Same fix outside ch7:**
  - `03:90` "unless you know who's paying and what the pay is"
  - `33:31` "that's why it pays best"
  - `33:94` "He's already keeping count"
  - `04:20` "the same ledger" is a sin image and acceptable, but it is the start of the pattern.

### 3. The "not wages, inheritance" disclaimer is now the refrain the panel flagged last time

There are about 20 anchors in the prose: `intro:17`, `03:82`, `04:108`, `05:103`, `06:31`, `07:44`–`53`, `07:110`, `16:17`, `20:58`, `21:112`, `23:78`, `24:29`, `25:71`, `30:22`, `32:16`, `33:31`, `34:47`, `35:44`, `35:83`.

- **Drew:** "I got it the first five times."
- **Theology:** the doctrine is right everywhere. The repetition starts to sound defensive, as if the book doesn't trust its own word.
- **Keep the full anchor** in intro, ch3, ch7, ch30 and ch34, plus one clause in ch33.
- **Everywhere else,** keep an anchor only if the same paragraph uses pay, reward or wages. Otherwise cut it. That means cut or shrink the ones at `04:108`, `05:103`, `06:31`, `16:17`, `21:112`, `24:29`, `25:71` and `32:16`, and one of ch35's two (keep `35:83`, cut the tail of `35:44`).
- **Back-cover line:** see "What Aaron must decide."

### 4. Repeated pictures are blurring together

- **Caregiving husband bathing his wife: 5 times.** `23:84` (unnamed), `25:91`, `30:82`, `32:87` (Mr. Alvarez, "three years"), `35:20` and `35:44`.
  - Name him Mr. Alvarez the first time (ch23) and call back once (ch35). Cut ch25 and ch30.
  - Reconcile the timeline: "for years" (`23:84`), "three years" (`32:87`), married 1968 (`35:20`).
- **Retired man makes his wife's coffee and sits with her:** Alton (`30:57`), Roy (`33:56`, `35:38`) and generic advice (`09:78`). Give it to one man.
- **Plumb line / Amos 7:**
  - ch17 is home (`17:7`, `17:62`).
  - ch29 teaches how a plumb bob settles all over again (`29:36`). Cut the lesson and keep Alton's own words.
  - `32:98` and `35:116` callbacks are fine.
- **Check-in questions.** The brother check-in shape (`13:77`: what mattered, what's heavy) comes back as the wife's "same three questions" (`22:56`). Vary ch22's version.
- **Adam's silence** is taught 4 times: `03:32`, `04:66`, `15:19`/`15:29`, `19:7`/`19:25`. ch19 is its home. Keep one glance in ch4 and cut the ch3 and ch15 versions. (This is also an IP-shape item; see #6.)
- **Jab at feelings-first men's books,** twice: `intro:15` and `02:33`. Keep the intro version.

### 5. The season roll call at the end of almost every chapter is the new stamp

Nearly every chapter has a closing paragraph or section that walks single, new dad, divorced, middle years, older and high performer in turn: `04:92`, `05:68`, `06:74`, `08:71`–`83`, `09:66`–`78`, `10:76`, `11:80`, `12:81`, `13:91`, `14:75`, `15:83`, `16:46`, `17:43`–`55`, `18:140`–`150`, `19:126`–`134`, `20:68`–`83`, `22:85`–`99`, `23:80`–`88`, `24:88`–`94`, `26:62`–`68`, `27:61`–`69`, `28:86`, `29:63`, `30:84`, `31:71`–`81`.

- **Do not cut the divorced, single, widowed or no-child content.** Those branches are why James and Caleb buy.
- **Change the form instead:**
  - Fold branches into the scenes and the Do this week line where they belong.
  - Cut the throwaway one-liners that add nothing, e.g. `18:150` "Winning at work? The garden was never a scoreboard" and `31:81` "Try it at home, where there's no bonus."
  - Never run the seasons in the same order twice in a row.
  - Keep a standalone season section only in chapters where the seasons *are* the content: 8, 9, 21, 22, 23, 25, 26 and 32.
- **"Single?" branches that only say "ask your mom"** (`22:99`, `24:90`) need a second option: a sister in Christ, a married couple he serves, his roommates.

### 6. Reshape the course's leftover shapes (ideas only, no wording)

Overlap is zero. These are about not tracking the course's outline.

- **(a) The four-part "Eden pattern"** at `20:60` (ground to tend and protect, God's word to keep, brothers, a day of rest) and its card heading `20:119` "the Eden pattern."
  - It reads as the fenced work/command/woman triad with one item swapped. The other heading items repeat `20:47`.
  - Say it as Genesis narrative (ch18 already does it beautifully) and drop the "pattern" label and the list.
- **(b) The four-beat Adam inventory** at `15:19`: "Called to stand up, he ducks. Caught, he points. Asked to give, he takes. Needed to speak, he clams up. Adam ran through every one."
  - Four failures from Adam is the old derivation's shape.
  - Keep "Sin bends a man inward" and one picture. Cut the four-part Adam roll.
- **(c) Sleeping disciples in ch13.**
  - `13:28` "knowing full well they'd doze off" keeps the fenced Gethsemane-while-they-slept beat. OPEN-QUESTIONS #2 says every sleeping beat was cut; this one wasn't.
  - Keep the request (Mark 14:34). Cut the dozing clause.
- **(d) The creek day as a ceremony template.**
  - The scene itself (`29:22`–`40`) is Steadfast's and stays.
  - The how-to at `29:42`–`59` (men bring three things; "Then… Then… Then…"; "you're one of us") is the closest structural echo of the knight-ceremony model in the book.
  - Compress it to one short paragraph of principles (small, early, outdoors, men he knows, his father last, weeks after matter more). Leave the step-by-step to the leader guide on walksteadfast.com.
- **(e) The rite-of-passage checklist** in ch11: `11:40` and the four-part list at `11:58` ("someone older, words worth keeping, weight on younger shoulders, and a seat among the men"). Tell it through David and Paul (already there) and drop the summary list.
- **(f) Grant's porch talk** (`12:73`), OPEN-QUESTIONS #5.
  - The scene is his and stays.
  - The paragraph that turns it into a method (need, thanks, decision, offer) is a four-step script. Keep his one sentence and the old man's "You eat yet?"
  - Collapse the explainer to two or three sentences, no sequence.
- **Keep, but don't map:** ch19's two gardens. The Eden/Gethsemane contrast is old church teaching and biblical, and the rewrite keeps it unmapped (`19:116` "the marks in these pages aren't a ladder"). Do not add mark names inside ch19. ch19's Do this week (`19:163`, three Gethsemane lines) is Scripture's own words and isn't tied to marks: keep it (OPEN-QUESTIONS #4).

### 7. NIV margin blocks, per Aaron's settled rule #2

Restore the NIV's em dashes and re-verify all 158 blocks.

- **Blocks where the NIV has em dashes the manuscript dropped:**
  - `07:50` Ephesians 2:8-10: NIV "through faith—and this is not from yourselves, it is the gift of God— not by works"
  - `22:17` John 10:14: NIV ends "my sheep know me—"
  - `32:26` Ecclesiastes 12:1: NIV ends `"I find no pleasure in them"—`
- **Quotation marks added or dropped at the edges:** 26 blocks (full list in `meta/NIV-AUDIT-2026-10-01.tsv`). Examples:
  - Added closing marks: `11:46` 1 Kings 2:2-3 ends `go"`, which the NIV doesn't have; also Judges 7:17, John 14:9, 2 Samuel 12:7 and 12:13, Amos 7:7-8, John 4:34, Habakkuk 2:2, 1 Samuel 17:34-35.
  - Nested single quotes raised to double: Matthew 25:21, Joshua 4:6-7.
  - Rule for the second pass: see the brief, and "What Aaron must decide" #4.
- **Box-side:** the binder runs `no_em()` on all body text, margins included (`tools/make_ebook_pdf.py:108`, `:194`). The print build must exempt margin blocks, or the restored dashes become " - ".

### 8. About the Author and the narrator's implied credentials, per Aaron's settled rule #1

- **About the Author:** rewrite `36-about-the-author.md` as an honest pen-name note (see the brief).
- **Narrator lines that imply clergy standing:**
  - `26:3` "Officiating a wedding gets me the best spot in the building."
  - `24:7` "I've stood up front at enough services to know that silence."
  - These clash with an honest note and with the persona's "not a pastor."
  - Recast as a guest's or a friend's view ("from the second pew," "at enough funerals").
- **Wider first-person life story** (wife, kids, baptism, Harlan at the wedding, Vernon's tractor, the first truck, being at the creek): see "What Aaron must decide" #1.

### 9. Capitalize pronouns for God and Jesus consistently

The house convention (He, His, Him in prose) breaks often. Examples:

- `08:9`, `08:48`, `08:95`
- `09:84`–`86`, `09:98`
- `10:21`, `10:32`, `10:41`–`43` (He and he in one paragraph), `10:52`, `10:60`–`68`, `10:91`
- `13:28` is fine, but `15:21` "Cain shrugged him off"
- `06:44` "cost him less"
- `30:95` "he saw it through"
- `31:13` "kill him," "his panel," `31:107`
- `33:11`, `33:18`

Church readers notice this before they notice anything else (Luis).

### 10. Cut the preachy and over-tidy lines

Full list below, under "Lines that still feel borrowed or preachy." The worst ones:

- `01:65` "Skip the retreat." This contradicts `01:23`, which honors big days.
- `12:7` "that's what God had in mind for a grown son" puts a knock in God's mouth.
- `17:103` "has just shown you his real north" scolds.
- `21:13` "That's most of a husband's job already" overclaims.
- `21:104` and `25:48` resolve a beat faster than life ("she comes looking for him now" is too quick for the bed chapter; James).
- `33:83` "Gold." and `35:66` "Which is exactly why everything is." are stacked fragments.

---

## Seat by seat

### Jace, 19 (works a counter, roommates, church kid)

**Lands**
- Eli at ten o'clock (`01:9`).
- "Nobody is going to issue you a permit to lead your own life" (`04:30`).
- "Numb at twenty-two isn't calm. It's a dashboard light" (`09:70`).
- The Mark-in-the-truck line (`17:45`).
- Eli's phone on the counter and asking a man eleven years older to hold the filter password (`25:77`): "the most useful page in the book for me."
- "Let the roommate choose dinner" (`23:88`).

**Fails**
- `05:126` "take back one chore you've been paying someone else to do" doesn't fit a guy with roommates and no money.
- The "Single?" lines in Part Four mostly send him to his mom.
- The repeated inheritance disclaimer reads like the book doesn't trust him to remember.

**Buy?** Yes, if an older man hands it to him. He'd skip the fatherhood chapters and come back later.

### Caleb, 22, single (locked seat)

**Lands**
- ch21 is still his. The box, the skillet, three seats, "This isn't a lobby" (`21:39`–`47`).
- "A single guy is under this verse too" (`12:23`).
- The single guy hauling a couch on a Saturday (`07:33`).
- ch18's single branch (`18:142`).

**Fails**
- `21:13` "That's most of a husband's job already" oversells.
- The single branches in ch22 to ch24 are the thinnest in the house block.
- He wants the moving-box man to be Micah, so the roster man finally gets a scene.
- The season roll calls feel like roll call, not like someone talking to him.

**Buy?** Yes. Don't thin ch21 or Eli.

### Marcus, 34, young marriage, new dad (locked seat)

**Lands**
- Tomás's broke Tuesday (`05:3`), the exact picture he asked for last time.
- Twenty minutes (`13:75`).
- "I do not need you to fix it" and the postpartum paragraph (`22:87`–`91`).
- The newborn branch in ch23 (`23:82`).
- "That's the tired talking" (`31:73`).
- Tomás's rhythm in the cracks (`33:83`).

**Fails**
- Length. The book went up 4.1%. He wants the second pass to come out shorter: cut repeats, never cut branches.
- The intro's shorter road (`intro:27`) is good. Keep it.

**Buy?** Yes.

### Drew, 46, married, job working, unfinished at home (locked seat)

**Lands**
- Anthony's day and the redo (`01:29`–`77`).
- The man who's good at everything except three things at home (`04:3`).
- The stair.
- The foyer and the kitchen (`16:3`).
- The furnace sentence (`24:13`).
- Anthony in the doorway at mid-career (`32:41`).

**Fails**
- The inheritance disclaimer, over and over.
- ch7's money talk makes the fourth mark sound like a rewards program (`07:96` "the check cleared").
- Every chapter ending with the same seasons walk.

**Buy?** After the second pass. He'd give it to his brother-in-law.

### James, 52, divorced, still in church (locked seat)

**Lands**
- "You are somebody's empty chair now" (`08:79`) holds.
- Kenny (`13:63`–`69`, `35:34`).
- Divorce pulling a man back to his mom's table (`12:81`).
- ch21's divorced seat (`21:19`–`29`).
- `22:97`, `23:86`, `24:92`, `25:81`, `26:66`, `27:65`, `29:63`.
- "The Father who never walks out sat in that courtroom with you" (`32:49`).
- "Hand hers to God" (`19:132`).
- "I'm not going to hand you the whole blame" (`15:83`).

**Fails**
- `25:48` (Mitch and Dana) resolves too fast for him.
- The divorced asides are starting to reuse one formula ("your children's mother… the bleachers").

**Buy?** Yes. The strongest divorced coverage yet. When you trim the season sections (fix #5), don't cut his branches.

### Frank, 68, widowed (new seat)

**Lands**
- "It's not good for a man to be alone. You know that in a way young men can't" (`21:33`).
- "Drift loves a widower, and it nearly always shows up calling itself rest" (`21:35`).
- `25:83`, said fairly.
- Mr. Pruitt's forty pecan trees and "Coffee with Ed Wednesdays. Trees." (`32:79`, `34:122`).

**Fails**
- The widower gets three short paragraphs in ch21 (`21:31`–`37`) and no face until ch32. Use Mr. Pruitt by name in ch21 (one or two sentences) so the widower has a man early.
- The caregiving picture appears five times and starts to feel like a device rather than a man (fix #4).

**Buy?** After the second pass.

### Earl, 62, kids grown, still has a next move (locked seat)

**Lands**
- Roy at 5:30 (`01:3`).
- "If you're the man ahead" (`14:43`–`62`).
- Abe: "Same job. Different garden" (`18:148`).
- Lyle and "I figured you could" (`28:13`).
- Alton: "a man in a chair by two" (`30:57`).
- Hollis's notebook (`34:7`).

**Fails**
- The older men blur: Roy and Alton both make the coffee and both carry plumb bobs (fix #1, fix #4).
- A few "Older?" one-liners feel like mascot lines.

**Buy?** After the second pass.

### Brandon, 41, high performer (VP, two kids; new seat)

**Lands**
- "The man I worry about isn't on the couch" (`04:3`), the best opener for him.
- "A title is not a definition" (`02:47`).
- `16:46` "whether your title has started answering questions only your soul should."
- "Work applauds in a way home rarely does" (`30:24`).
- ch24's trap section.

**Fails**
- His branch is usually the last line of a roll call (`09:76`, `10:76`, `15:83`, `18:150`, `31:81`). Walt is his man, and Walt's payoff points at a scene that doesn't exist (fix #1).
- ch7's comp-plan language will be read through his bonus structure unless the chapter dismantles it (fix #2).

**Buy?** After the second pass.

### Luis, 50, table leader and lay elder (new seat)

**Lands**
- The closer is consistent and easy to run.
- The intro explains it well (`intro:37`–`49`), including the fallback for a man with no brother yet (`intro:45`).
- The Condensed Training week list works.
- The suicide section (`31:83`–`103`, with 988) is what he'd want handed to his men.

**Fails**
- The narrator officiates weddings and stands up front at funerals (`26:3`, `24:7`). His men will assume Wes is clergy, which conflicts with the honest pen-name note (fix #8).
- Lowercase pronouns for God (fix #9).
- The closing-section heading changes: `## Before you turn` at `16:104`, `17:125`, `20:98`, `21:116`, `22:109`, versus `## Before you turn the page` elsewhere.
- Churches will try to copy the ch29 creek day. He'd rather the details lived in the leader guide.

**Buy?** Yes. He'd run it.

### Theology reader: "God's pay" and inheritance

**Doctrine** is sound everywhere it's stated:
- Ephesians 2:8-10 is placed right (`07:49`–`53`).
- Colossians 3:24's "inheritance" is the hinge (`03:82`, `30:22`).
- No prosperity reading (`07:77`–`86`).
- ch19's gospel transfer is clear (`19:105`–`114`).

**Fix list**
- Everything in Top-10 #2 and #3.
- `03:54` and `05:5`: "even when somebody else dropped it" sits against Galatians 6:5's "their own load."
  - Say *when* a dropped load becomes yours: it lands in your house or your lane.
  - Keep that apart from Galatians 6:2 (ch5 already teaches the two words at `05:79`, so tie the definition to that).
- `19:60`: "drank it as if the guilt were His own." "As if" can read as pretend. Write "with our guilt laid on Him" (2 Cor 5:21).
- `20:17`: the Zechariah paraphrase ("rejoice over one builder setting one stone") isn't accurate. Zechariah 4:10 is "the day of small things" and the stone or plumb line "in the hand of Zerubbabel." Paraphrase it honestly or cite it.
- `05:101`: "The cross is 'That's mine'" works. Keep it clear that He took what was ours, not His (the sentence nearly does).

**Ch7 title:** accepts, with the conditions below.

### IP and originality reader

**Clean**
- Sweep: 0.
- Transcript 8-grams: 0, verified independently.
- The copyright acknowledgment matches the locked text exactly (`00-copyright:28`).
- The Biblica notice is exact (`00-copyright:15`).
- 179 unique verses (under 500); Scripture is about 6% of the text.
- The marks and creed are original.
- "Four marks" is used only as a descriptive label.
- "Go First" is a chapter title and a class-week title inside the book, which is fine. Never use it as a product title.

**Reshape**
- Top-10 #6 (a)–(f) and the repeated Adam's-silence beat.
- **Low-risk notes:**
  - `intro:15` and `02:33` nod at a well-known feelings-first men's book without naming it. Fine; keep one.
  - `22:68` lists love "landing" as words, time, touch and acts. Ideas aren't protected, but vary it so it doesn't read as a summary of a famous five-item framework.
  - `25:15` "with my body I thee worship" is public-domain liturgy.
- **Pre-print, not prose:** STEADFAST (Reg. 3870140) clearance for the book title and series. "Work for God's Pay" was not separately cleared. It's fine as a chapter title; clear it before using it as a course or product name.

---

## The panel's view on renaming ch7 "Work for God's Pay" (settled yes by Aaron)

- **For:** 9 seats (Jace, Caleb, Marcus, Drew, James, Brandon, Luis, IP, and Earl with a shrug).
  - All four marks now read as a set in the contents and class weeks 4–7.
  - A reader meets the mark's name where he'd look for it.
  - Leaders can teach the four weeks as one unit.
- **Conditional yes:** Theology and Frank. "Pay" printed alone in the TOC can sound mercenary to older church men. Their conditions, all folded into the second-pass brief:
  1. The inheritance sentence goes on ch7's first page, not at `07:44`.
  2. Cut ch7's commerce metaphors (Top-10 #2).
  3. Keep "Live for the reward that lasts" as ch7's closing echo (`07:106`; it ties to Hebrews 11:26 at `07:65`).
  4. Recommended: one inheritance line on the back cover (Aaron's call; see below).
- **Mechanics** (no one objected):
  - `07:1` becomes `# 7. Work for God's Pay`.
  - `00-contents:24`, `37-condensed-training:17`, `biblical-manhood/BOOK-TOC.md:19`, and the cross-reference at `03:84`.
  - The filename stays: the binder's `CHAPTER_FILES` uses the filename (`tools/make_ebook_pdf.py:70`), and the running head comes from the H1, so no binder change is needed.

---

## Per-chapter notes

Seat initials: J Jace · C Caleb · M Marcus · D Drew · Ja James · F Frank · E Earl · B Brandon · L Luis · T Theology · IP.

- **Copyright.**
  - Correct, and the acknowledgment and Biblica notice are word for word (IP).
  - The box build must print this file instead of the hard-coded `page_copyright()` (brief §6, box step).
- **Dedication.** Locked. See "What Aaron must decide" #2 (it claims a wife and children, and "for Evan" isn't in the text).
- **Introduction**
  - `intro:9`–`17`, the claim and the creed: strong, and owned. Keep.
  - `intro:15`: keep this one jab at feelings-first books. Cut the ch2 echo.
  - `intro:27`, the shorter road: protect (M).
  - `intro:53`: the roster promises Micah. Pay that off (fix #1).
- **1. A Quiet Tuesday**
  - Roy, Walt, Tomás and Eli in one frame (`01:3`–`11`). Protect.
  - Anthony's day and the redo (`01:29`–`77`). Protect (D).
  - `01:65` "Skip the retreat" contradicts `01:23`. Soften.
  - `01:15` "a pastor lowered me into a river" is narrator biography (Aaron decision #1 below).
- **2. You Are Not Crazy**
  - The six maps as prose (`02:21`–`35`) work.
  - `02:33` repeats the intro's jab. Cut it.
  - `02:47` "A title is not a definition." Keep (B).
- **3. The Four Marks**
  - The definition paragraph and creed (`03:13`–`17`) land.
  - Cut Adam's silence at `03:32`. ch4 and ch19 carry it.
  - Fix the "dropped it" theology (`03:54`, T).
  - `03:84`: update the cross-reference to **Work for God's Pay**.
  - `03:90` "who's paying": reword (T).
  - `03:71` "where good men and godly men part ways" ties nicely to the subtitle. Keep.
- **4. Stop Waiting**
  - The opener (`04:3`) is the book's best for B and D.
  - The stair and "Good costumes" (`04:43`–`57`): keep.
  - `04:20` "Hard news. Stay with me" is signposting. Trim it.
  - `04:92` season paragraph: fold it in (fix #5).
  - `04:108` anchor: shorten (fix #3).
- **5. Pick Up the Weight**
  - Tomás opener (`05:3`): protect (M).
  - Load-bearing wall (`05:37`) and "Keeper is your job. Savior is already taken" (`05:64`): keep.
  - Fix the `05:5` definition (T).
  - The `05:126` single option doesn't fit (J). Change it.
  - `05:103` anchor: shorten.
  - The chapter is 2,029 words. Trim to 2,000 or under.
- **6. Go First**
  - The oak in the street (`06:3`–`9`), "Watch me," and "Your number is second" (`06:155`): protect.
  - The alone-friendly Do this week (`06:135`): protect, as worded.
  - `06:31` anchor: shorten.
  - `06:44` "him" should be "Him".
- **7. Work for God's Pay** (renamed)
  - The trophy box (`07:3`) and "Some kind of pay already has you" (`07:148`): keep.
  - Fix #2 in full.
  - `07:92` and `07:128` repeat the same "your wife or your roommate doesn't get told…" list. Keep it once, in Do this week.
  - Introduce Mr. Pruitt at `07:73`.
- **8. The Empty Chair**
  - Curtis at the lot and at the sink, and "Nobody ever sat in this seat for me" (`08:87`): protect.
  - "You are somebody's empty chair now" (`08:79`): protect (Ja).
  - Pronouns at `08:9`, `08:48`, `08:95`.
  - Keep the "It comes with you" section. It *is* the content here.
- **9. Anger, the Itch, and the Drift**
  - Owen's week and the mailbox: keep, including the friction at `09:92` (D asked for it last time).
  - "Pain was looking for a Father" (`09:137`): protect.
  - Pronouns at `09:84`–`98`.
- **10. The Father Who Does Not Leave**
  - The pickup line, Curtis, and "the original was in the line before the bell" (`10:136`): keep.
  - Pronouns throughout (`10:21`–`91`); the worst chapter for this.
  - `10:76` season paragraph: fold it in.
- **11. When Home Never Handed You Off**
  - Nate at his dad's sink, and the utility-sink sentence (`11:76`): protect.
  - The new mother section (`11:17`–`23`) works. Keep (Ja, F).
  - Drop the four-part list at `11:58` (fix #6e).
  - `11:74` "You get them from the Father": "them" has no antecedent.
  - `11:46` 1 Kings excerpt has an added `"`. Fix per the NIV rule.
- **12. Leave Without Slamming the Door**
  - Three sons at the door: keep.
  - `12:7` overreach. Trim it.
  - Grant's porch: keep the scene, collapse the method paragraph (`12:73`, fix #6f).
  - `12:85` "That's Pick Up the Weight, on your parents' front steps": keep. It's a good single naming.
- **13. A Man With No Brothers**
  - Dale and the clipboard (`13:3`–`9`, `13:95`): protect.
  - Kenny and "which row to put you in" (`13:69`): protect.
  - Cut the dozing clause at `13:28` (fix #6c).
  - `13:91` "lost the company that came with the job or with her" is muddy.
  - Chapter is 2,022 words. Trim.
- **14. Ask the Man**
  - Harlan, "Ride with me Saturday," and "Well. You paid attention" (`14:79`): protect.
  - "If you're the man ahead" (`14:43`–`62`) is Earl's favorite section.
  - `14:75` season paragraph: fold it in.
- **15. The Problem Inside**
  - The body shop and "Paint's not going to fix that" (`15:5`): protect.
  - Wade's check-in (`15:47`–`51`): keep, and link it to ch26.
  - Cut the four-beat Adam roll and Adam's silence (`15:19`, `15:29`, fix #6b).
- **16. How That Looks on a Man**
  - The foyer: protect.
  - The shapes and David's year (`16:48`–`94`): keep.
  - `16:17` anchor reads bolted on. Cut it.
  - `16:28` aphorism: trim.
  - `16:104` heading: normalize.
- **17. No Fixed Star**
  - The level, the plumb line, and the fog and fence posts (`17:20`): keep.
  - "Put the string on the wall" (`17:166`): protect.
  - `17:103` scolds. Soften.
  - Hugh and Proverbs (`17:111`): keep.
- **18. Before the Fall**
  - The seed packet, coal, and closing day (`18:138`): keep. This is ch18's own shape and the IP reader likes it.
  - `18:150` throwaway: cut.
  - Abe (`18:148`): keep (E).
- **19. Two Men, Two Ways**
  - Keep, unmapped.
  - `19:60` wording (T).
  - Do this week (`19:163`): keep.
  - Chapter is 2,052 words, the longest. Trim 60–80.
- **20. Destiny Is Not a Vibe**
  - The dock and the slip (`20:3`–`7`, `20:64`): keep.
  - Rework the Eden-pattern list and card heading (`20:60`, `20:119`, fix #6a).
  - Fix the Zechariah paraphrase (`20:17`).
- **21. If There Is No Wife Yet**
  - Protect it whole (C, Ja, F).
  - Name the box man Micah (`21:3`).
  - Mr. Pruitt gets a sentence in "If she died first" (`21:31`–`37`).
  - Soften `21:13`.
  - The `21:112` anchor can go.
- **22. Know Her**
  - The bird notebook and "She kept living after you stopped taking notes" (`22:150`): keep.
  - The postpartum paragraph (`22:89`): protect (M).
  - `22:56`: the three questions duplicate ch13. Vary them.
  - `22:68` love categories: vary (IP).
  - `22:99` single branch: add a second option.
  - `22:17` John 10:14: restore the NIV dash.
- **23. Lay It Down**
  - The wet floor and the crumpled quote: protect.
  - "What it isn't" (`23:33`–`43`): keep.
  - Make the `23:84` caregiver Mr. Alvarez, named.
  - `23:78` anchor is local to "pay scale". Keep it short.
- **24. What She Actually Needs**
  - "Good provider is a furnace sentence," the funeral line, and "I will give you the whole chapter in two sentences first": protect.
  - Rename Dale here (fix #1).
  - Cut the `24:29` anchor.
  - Recast `24:7`.
- **25. The Bed Is a Covenant**
  - "A contract keeps score on her" (`25:136`) and Eli's counter (`25:77`): protect.
  - `25:48` resolves too fast (Ja). Let it take longer.
  - Cut the `25:91` caregiver repeat.
  - Shorten the `25:71` anchor.
- **26. Your Daughter Is Watching**
  - The bride's glance and "I don't come to watch you hit. I come to watch you" (`26:15`): protect.
  - Link Wade to ch15.
  - Recast the officiant line at `26:3`.
  - Ephesians 6:4 (`26:45`): the panel says keep it (Scripture, not course wording; OPEN-QUESTIONS #3).
- **27. Give Your Son a Name**
  - Ray's four seconds of video: keep.
  - The daily/weekly/yearly rhythm (`27:40`–`51`) is original and practical. Keep it.
- **28. Give Your Son a Hill**
  - Lyle in full, "Well. I figured you could," and "Pick the right hill. Stay on the step": protect.
  - `28:29` "Stop Waiting… flips" is a clever single naming. Keep it.
- **29. Give Your Son a Day He Will Not Forget**
  - The creek scene and the plumb bob: keep.
  - Compress the how-to (`29:42`–`59`).
  - Cut the repeat plumb-bob lesson at `29:36`.
- **30. You Were Made for a Work**
  - Rename the grader Dale.
  - Alton's retirement (`30:57`): keep, but give the coffee picture to one man only.
  - Cut the `30:82` caregiver repeat.
  - `30:95` pronoun.
  - The anchor at `30:22` stays (it's a pay chapter).
- **31. Feelings Are the Dash, Not the Wheel**
  - Vernon and the gauges, and "The Word drives the truck": keep.
  - The broom-bush section and 988: protect (L).
  - Pronouns at `31:13`, `31:107`.
  - `31:81` throwaway: cut.
- **32. Every Season Still Counts**
  - "February has a job" and "Gardens change": protect.
  - This chapter *is* the season roll call, so it stays.
  - Shorten the `32:16` anchor.
  - Mr. Alvarez at `32:87` becomes a callback.
- **33. What You Are Building When Nobody Claps**
  - The four a.m. pour and slab: keep.
  - Fix the plumb-bob collision (`33:46`) and fence→creek (`33:79`).
  - "Thursday table" at `33:50` is unexplained. Name Hollis.
  - `33:31` "pays best" and `33:94` "keeping count": reword (T).
  - `33:83` "Gold.": trim.
- **34. Write the Next Move**
  - Hollis's notebook, Roy's porch line, and Mr. Pruitt's two-line page: protect.
  - The creed at `34:45` and its anchor at `34:47` stay.
- **35. These Men Are My Brothers**
  - Roll call: fix Walt (`35:30`, `35:55`), Hollis (`35:44`), and the Dale/Micah link (`35:32`).
  - Cut the tail of the `35:44` anchor.
  - "Tuesday is when it will show. Get up." and the open chair: protect.
- **About the Author.** Rewrite per settled decision #1.
- **Condensed Training.** Change `37:17` to "Work for God's Pay". Otherwise leave it alone.
- **Back cover.** The creed is printed once and correctly. For the optional inheritance line, see the decisions below.

---

## Keep, and don't break

These are protected lines. Protect the force of each line; small wording drift is fine.

- A man's life is decided on Tuesdays (`01:19`, `01:126`).
- Six maps, none of them agree where north is / You're not crazy (`02:35`, `02:7`).
- The creed as locked, at its six placements only.
- Absence purchased with a bigger paycheck is still absence (`05:146`).
- Keeper is your job. Savior is already taken (`05:64`).
- Where are you? He isn't asking for directions (`04:151`).
- He went out ahead of you. Your number is second (`06:155`). The alone branch at `06:135`.
- Nobody ever sat in this seat for me / You are somebody's empty chair now (`08:87`, `08:79`).
- Pain was looking for a Father (`09:137`).
- The original was in the line before the bell (`10:136`).
- I've had my eye on you for years. You're a good man (`11:76`).
- One man, twenty minutes, every week (`13:138`).
- Ride with me Saturday / Well. You paid attention (`14:5`, `14:79`).
- Paint's not going to fix that. It's coming from the inside (`15:5`).
- A man can run a kingdom well and rot inside it (`16:145`).
- Put the string on the wall and trust the weight (`17:166`).
- Work came before the curse (`18:197`).
- Here's your job. Quit waiting to feel a different one (`20:7`). Destiny is not a vibe.
- No wife yet still leaves you a man (`21:157`). The whole of ch21.
- I do not need you to fix it. I need you to know how hard this is (`22:91`).
- Being right is not the same as being a husband (`23:137`).
- Good provider is a furnace sentence / the funeral line (`24:13`, `24:7`, after the credential recast).
- A contract keeps score on her (`25:136`).
- I don't come to watch you hit. I come to watch you (`26:15`).
- Well. I figured you could / Pick the right hill. Stay on the step (`28:13`, `28:19`).
- A man with no job by noon is a man in a chair by two (`30:57`).
- Your feelings read the engine. The Word drives the truck (`31:145`).
- February has a job (`32:5`, `32:142`).
- The crowd gets straw. The Father gets the gold you pour in the dark (`33:136`).
- Coffee with Ed Wednesdays. Trees (`34:122`).
- Tuesday is when it will show. Get up (`35:136`). The open chair (`35:85`–`94`).
- Every divorced, single, widowed and no-child branch in the closers.
- The intro's shorter road.
- The copyright acknowledgment and Biblica notice, word for word.

## Lines that still feel borrowed or preachy

**Borrowed in shape (ideas, never wording; see Top-10 #6)**
- `20:60`, `20:119`: the Eden-pattern list.
- `15:19`: the four-beat Adam roll.
- `13:28`: sleeping disciples.
- `29:42`–`59`: the ceremony template.
- `11:40`, `11:58`: the rite-of-passage checklist.
- `12:73`: Grant's four-step talk.
- `03:32`, `04:66`, `15:29`, `19:25`: Adam's silence, four times.
- `22:68`: love-language categories.

**Preachy, stacked aphorisms, or over-tidy**
- `01:65` "Skip the retreat."
- `04:20` "Hard news. Stay with me."
- `06:89` "That pulse is courage, felt from the inside."
- `07:75` "If this life is all there is… the only math that works."
- `12:7` "that's what God had in mind for a grown son."
- `16:28` "A neck that's always bent to look down at people goes stiff when it's time to look up at God."
- `17:103` "has just shown you his real north."
- `21:13` "That's most of a husband's job already."
- `21:104` "the week he quit waiting landed right next to the week he became the kind of man a godly woman would want."
- `25:48` "A few months later he told me she comes looking for him now."
- `33:83` "Gold."
- `35:66` "Which is exactly why everything is."

---

## What Aaron must decide (the panel can't)

1. **First-person narrator stories.** Settled decision #1 makes the About page honest. The body's "I" still carries a life:
   - married with children (`01:15`), baptized in a river (`01:15`), Harlan at "my wedding" (`14:79`), Vernon's tractor (`31:3`), "my first truck" (`15:3`), "my grandfather's hand" (`35:74`), present at the creek (`29:5`), officiating weddings (`26:3`), up front at funerals (`24:7`).
   - The persona says the voice is "not a fake biography" and that Aaron's real stories replace placeholders.
   - **Decide:** which of these are true of you, which become "a man I know," and which go.
   - Second-pass default: recast only the two clergy-credential lines (`26:3`, `24:7`) and keep the rest pending your answer. Several are protected hot lines (Harlan, the body shop, Vernon).
2. **The dedication** is locked but says "my wife" and "our children" (`00-dedication:5`–`7`), and `BOOK-TOC.md` says "for Evan" though the text never names him. Confirm it's true of you, and say whether Evan's name goes in.
3. **Back-cover inheritance line.** The panel (Theology, Frank, Luis) recommends one line under the creed, now that "Pay" is a TOC title. For example: "God's pay is a Father's inheritance, not wages." The wrap note locks the creed line but not the space beside it. Your call.
4. **Quotation marks at the edges of NIV excerpts** (comes out of settled decision #2). Strict NIV punctuation leaves dangling or unclosed speech marks in about 26 blocks, wherever the cited verse starts or ends mid-speech.
   - Second-pass default: words, dashes, commas, colons and semicolons exactly as the NIV prints them. Only a dangling *edge* quotation mark, belonging to speech that starts or ends outside the cited verses, may be dropped. Marks are never added. Where the cited verse leaves speech unclosed, print it as the NIV does or extend the citation by a verse. Nested single quotes stay single. No other punctuation changes.
   - If you want zero exceptions, say "strict" and the blocks will be re-cut to whole speeches where possible.
5. **STEADFAST trademark clearance** (Reg. 3870140, plus STEADFAST LEGACY pending) for the book title and the "Steadfast Men" series, with an IP attorney before print or sale. This doesn't touch the prose.

Panel recommendations you can overrule without a decision meeting:
- Cut the dozing line in ch13 and keep the request (OPEN-QUESTIONS #2).
- Keep Ephesians 6:4 in ch26 (#3).
- Keep ch19's three Gethsemane lines (#4).
- Keep Grant's scene and collapse its method paragraph (#5).
- Don't add part look-backs; Marcus says the page count matters more (#9).
