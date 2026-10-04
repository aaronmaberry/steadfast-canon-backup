# Second-pass changelog (Opus 5.5, 2026-10-01)

One section per item in `SECOND-PASS-BRIEF.md` (L1–L3, Fix 1–10), plus Aaron's narrator decision. References read `file:first-pass line → second-pass line`, using chapter numbers (`07` = `07-live-for-a-reward-that-lasts.md`). Where a line was removed or folded elsewhere, the new location is given.

## L1 / Fix 8. About the Author and the clergy lines

| Where | Before | After |
|---|---|---|
| `36` (whole file) | Invented bio: husband, father of two, Texan, tech job, taught in living rooms, kitchen-table origin, not a pastor or counselor (324 words) | Interim short note (134 words), **since reverted** (see the 2026-10-01 restore section below): the book stands on Scripture; what Steadfast Men is (a twenty-four-week training for men in every season); walksteadfast.com. No career, family, place, church, credential or teaching history. |
| `24:7 → 24:7` | "I've stood up front at enough services to know that silence." | "I've sat through enough funerals to know that silence." (The funeral line is protected and kept.) |
| `26:3 → 26:3` | "Officiating a wedding gets me the best spot in the building…" | "From the second pew at a wedding, you catch a moment most of the room misses." |

## Narrator (Aaron's decision 4)

Aaron's real life, his wife, his kids and his baptism, stays in first person with no new details (`01:15`, the dedication, and the "my own house / my own kitchen / my own family" self-owns). Every other first-person life story is now about a man Wes knows, told in third person. The table is in `SECOND-PASS-RULES.md`.

| Where | Before | After |
|---|---|---|
| `01:15 → 01:15` | "…the job I took and the one I passed on…" | Cut (career biography). The wedding, first child, funerals and river baptism stay. |
| `02:15 → 02:15` | "I once sat on my tailgate with the tools still zipped…" | "I've been the man on the tailgate with the tools still zipped in the bag, telling myself…" (a figurative self-own with no invented facts) |
| `03:9 → 03:9` | "My own bench has a ring like that…" | "A friend of mine has a ring like that on his bench…" |
| `03:45 → 03:45` | "One August I helped a friend move a gun safe…" | "One August a friend of mine and his brother-in-law moved a gun safe…" |
| `07:3 → 07:3` | "I know the drive home… Years later I saw one just like it at a yard sale" | "Most men know the drive home… Years later one just like it turns up at a yard sale" |
| `13:75 → 13:75` | "This is what finally worked for me." | Cut. |
| `14:3, 5, 7, 79 → 14:3, 5, 7, 77` | The narrator caught Harlan at his truck, rode the feed route, and heard "Well. You paid attention." at "my wedding" | The same story is now **Travis's**, in third person. "Ride with me Saturday" and "Well. You paid attention" are verbatim. |
| `15:3, 17, 87 → 15:3, 17, 85` | "My first truck had a bubble…"; "stood in his shop feeling like a fool…" | **Cody's** first truck and Cody in the shop. "Paint's not going to fix that. It's coming from the inside." is verbatim. |
| `29:5, 24, 26 → 29:5, 24, 26` | "I was there the morning…"; "Five of us… And me." | "His dad told me about the morning…" The five men are Alton, the dad, the dad's brother, the dad's weekly friend, and a neighbor (a single man) who taught the boy to fish. |
| `29:65, 73 → 29:49, 55` | "I've watched a family… / I've watched fathers… stand by the water" | "I know a family that… / I know fathers who…" |
| `31:3–9 → 31:3–9` | "Vernon taught me to drive his tractor… My row looked perfect…" | "My friend Clay learned to drive a tractor from Vernon…" Clay's row and Clay's needle, in third person. Vernon stays. |
| `35:9 → 35:9` | "we… buried wives" | "stood at gravesides" (a narrator "we" that implied widowhood). |
| `35:74 → 35:74` | "the callus a fence stretcher left on my grandfather's hand" | "the callus a fence stretcher leaves on an old rancher's hand" |

## L2 / Fix 7. NIV word for word and punctuation for punctuation

- **Tooling.** `meta/tools/niv_verify.py` was rewritten to compare against the raw NIV. Only two typographic normalizations remain: curly quotes become straight, and dashes are closed up at verse boundaries. The one allowance is a dropped dangling edge mark. The first pass's comma-for-dash `house_style()` is gone. `meta/tools/niv_fixes.py` applies the fixes from the fetched text. The format check in `checks.py` that rejected quote-wrapped blocks was removed, because the NIV itself wraps Ephesians 5:31, and its dash check now counts prose only.
- **Three restored NIV dashes:**
  - `07:50 → 07:52` Ephesians 2:8-10: "through faith—and this is not from yourselves, it is the gift of God—not by works". The space Bible Gateway and BibleHub print after the second dash marks the verse-9 boundary in both sources. In running text the NIV closes its dashes, so the block prints it closed; this is flagged in OPEN-QUESTIONS.
  - `22:17 → 22:17` John 10:14: "…and my sheep know me—"
  - `32:26 → 32:26` Ecclesiastes 12:1: `…"I find no pleasure in them"—`
- **Added quotation marks removed** (marks are never added):
  - 1 Kings 2:2-3 (`11:46`), 2 Samuel 12:7 (`16:77`), 2 Samuel 12:13 (`16:90`), Amos 7:7-8 (`17:62`), John 4:34 (`20:52`) and 1 Samuel 17:34-35 (`28:56`). Each now ends with the speech still open, as the NIV prints it.
- **Nested levels restored:** Matthew 25:21 (`07:56`) and Joshua 4:6-7 (`29:14`) are back to single quotes.
- **NIV quotation marks restored:**
  - Ephesians 5:31 (`25:38`): Paul's quotation of Genesis is back in double quotes.
  - Nehemiah 6:3 (`34:33`): the reply's quotes are restored.
  - Numbers 6:24-26 (`35:90`): the blessing's double quotes are restored. The continuation marks from vv. 22-23 are dropped.
- **Re-cut so no excerpt opens or closes inside speech** (no mark added):
  - Judges 7:17 → **Judges 7:17-18** (`06:47`), so Gideon's speech closes.
  - Luke 15:20 (`10:87 → 10:83`) now starts at "But while…".
  - Habakkuk 2:2 (`34:20`) now starts at "Write down…".
  - John 14:9 (`10:24`) now starts at "Don't you know me…".
- **Dangling edge marks dropped** (allowed): Luke 16:10, Matthew 7:24, Deuteronomy 31:8, Matthew 6:19-21, Exodus 20:12, Mark 7:23, Matthew 7:24-25, Genesis 3:15, Matthew 26:46, Acts 13:36, Luke 22:32, Zephaniah 3:17 and Numbers 8:25-26. Each is named in `SCRIPTURE-COUNT.md`.
- **Result:** 158 blocks, 132 EXACT, 17 EXACT-EDGE-DROP, 9 EXCERPT, 0 mismatch. 180 unique verses; Judges 7:18 is new.

## L3. Chapter 7 renamed

| Where | Before | After |
|---|---|---|
| `07:1 → 07:1` | `# 7. Live for a Reward That Lasts` | `# 7. Work for God's Pay` (the file name is unchanged) |
| `00-contents:24` | Live for a Reward That Lasts | Work for God's Pay |
| `37:17` | 7. Live for a Reward That Lasts | 7. Work for God's Pay |
| `03:84 → 03:84` | "**Live for a Reward That Lasts** follows that hunt." | "**Work for God's Pay** follows that hunt." |
| `07:7 → 07:7` (first page) | Inheritance first taught at `07:44` | The opening section now carries it: "God's pay is an inheritance, what a Father gives His sons because they're His, and in Christ you're a son by grace before you've lifted a finger. Nobody earns an inheritance. You work like a son because you already are one." |
| `07:106 → 07:108` | "Live for the reward that lasts." | Kept as the echo line. |

A search of every file finds no other use of the old title. `biblical-manhood/BOOK-TOC.md:19` is outside the folder and was not edited (box step 1).

## Fix 1. Recurring men

| Who | Where | Change |
|---|---|---|
| Dale | ch13, ch34, ch35 | Only ch13's Dale remains (the ER clipboard, the Thursday brother, Micah's breakfast man). |
| Russ (new) | `24:3, 19, 29, 31, 122 → 24:3, 19, 29, 31, 115` | Renee's husband, formerly "Dale". |
| Gil (new) | `30:3, 9, 13, 20, 22, 26, 97` | The county grader, formerly "Dale", including the head "## Why I told Gil yes". |
| Wade | `26:11 → 26:11` | "Wade, the man in chapter fifteen whose little girl shrank when his voice climbed…" (now one man across ch15 and ch26). |
| Roy's grandson | `33:46 → 33:46` | The plumb bob is gone. He now "rides the school bus past a barn his great-grandfather raised". |
| Creek | `33:79 → 33:79` | "a morning at a fence" → "a morning at a creek". Also `35:66`: "a fence line" → "a creek bank". |
| Walt | `35:30, 35:55 → 35:30, 35:55` | No parking lot and no "three hundred contacts". The lines now use his on-page facts: part of the company sold, chasing his wife again, "At 6:15 the shop is still quieter than the house, and he locks up anyway"; "Walt came from a shop that was quieter than his house". Also `35:16`: "three hundred phone contacts" → "a name buried somewhere in your phone". |
| Hollis | `35:44 → 35:44` | "walked across the lot to a stranger" → "Hollis finally told Cole he's a good man, and Cole sat in his truck and cried." (matches ch34) |
| Mr. Pruitt | `07:73 → 07:75` | Introduced: "Mr. Pruitt, a widower who planted forty pecan trees the spring after he buried his wife, keeps them like that." |
| Mr. Pruitt | `21:35 → 21:35` | Added to the widower seat: married fifty-one years, the forty pecan trees, Ed's Wednesday coffee. |
| Mr. Pruitt | `35:22 → 35:22` | "Ed still comes for coffee every Wednesday, as he has for four years" (fixes a Wednesday/Tuesday clash on the same evening). |
| Micah | `21:3, 21:102 → 21:3, 21:102` | The moving-box man is now Micah, who "quit asking permission". This matches ch35, where "Micah wrote the date" and "stop living like a guest in his own place". |
| Hollis's Thursday table | `33:50 → 33:50` | "the Thursday table" → "Hollis's Thursday table". |

## Fix 2. Ch7 speaks family, not accounting

| Where | Before | After |
|---|---|---|
| `07:7 → 07:9` | "send you a bill… only if he trusts there's a return" | "all cost you something today, and a man keeps at them only if he trusts the Father who's watching" |
| `07:13 → 07:15` | "on that payroll" | "still working for that one" |
| `07:33 → 07:35` | "He keeps the books" | "He doesn't forget a thing" |
| `07:62 → 07:64` | "Moses ran the numbers right" | "Moses chose well" |
| `07:73 → 07:75` | "the ledger that matters is his Father's" | "his Father has already forgiven him more" |
| `07:75 → 07:77` | "it's the only math that works" | "That way of living only makes sense if this life isn't the end of the story. It isn't." |
| `07:86 → 07:88` | "He did the math with bigger numbers" | "He was looking at the long view" |
| `07:96 → 07:98` | "the check cleared, and it was a small one" | "you've traded a Father's 'well done' for a glance from the room" |
| `07:110 → 07:112` | "He isn't paying you off" | "forgets nothing, and He's keeping an inheritance for His son" |
| `07:128 → 07:130` | "pays for secret work" | "rewards secret work" |
| `03:84`, `03:90` | "keeps the record"; "who's paying and what the pay is" | "remembers it"; "whose son you are and what He's keeping for you" |
| `33:31`, `33:75`, `33:94`, `33:98` | "pays best"; "He moved the account"; "keeping count"; "count every day" | "It's just a son and his Father"; "He changed where he looked"; "let your Father be the one who sees"; "remember every day" |
| `04:20`, `08:48`, `20:15` | "the same ledger"; "an honest record"; "God counts the work" | "To God, the thing left undone is as real as the thing done"; "God saw all of it, and it matters to Him"; "God honors the obedience" |

The only money images left on God's side are the mark name and the creed ("God's pay"). The false pay keeps the yard-sale box and the "small rewards" that "pay out the same night".

## Fix 3. Inheritance anchor used less

- **Full anchors kept:** `intro:17`, `03:82`, `07:7` and `07:48–55`, `30:22`, `34:47`.
- **ch33:** one clause (`33:31`).
- **Cut:** `04:108 → 04:104` (now "God is glad over that, the way a father is glad over a son"), `16:17`, `20:58` (the "no paycheck" sentence; the family "well done" stays), `21:112`, `24:29`, and the tail of `35:44`.
- **Shortened:** `05:103 → 05:101`, `06:31`, `23:78`, `25:71`, `32:16`.
- **Kept in full:** `35:83`.

The full list of anchors is in `THEOLOGY-PAY.md`.

## Fix 4. Repeated pictures

| Picture | Change |
|---|---|
| Caregiver bathing his wife | Named **Mr. Alvarez** at his first appearance, `23:84 → 23:88`: married 1968, three years, "Her mind has let go of his name. He has never let go of hers." The `32:87` callback ("You remember Mr. Alvarez… three years now") and the `35:20` callback stay. The image is cut at `25:91`, `30:82`, `30:95` and the second ch35 washcloth (`35:44`). |
| Coffee for the wife | Now **Roy's** only (`33:56`, `35:38`). Cut from Alton (`30:57`, where "a man in a chair by two" stays) and from the generic `09:78`, which is now "turn it off after supper, ask her one real question". The reader's coffee at `33:22`, `33:68` and `33:94` became packed lunches. |
| Plumb bob | `29:36 → 29:34`: the lesson is cut, and the line points back to ch17 while keeping Alton's own words. Roy's plumb line is gone from `33:81` ("goes to the Word"). |
| Check-in questions | `22:56`: "When did you feel most like yourself this week? What do you wish I'd noticed?" (no longer echoes ch13) |
| Adam's silence | Cut at `03:32` and `15:29`. One glance remains at `04:66`. ch19 is the home of the beat. |
| Feelings-first books jab | Cut at `02:33`. Kept at `intro:15`. |

## Fix 5. Season roll calls

Standalone season sections remain only in ch8, 9, 21, 22, 23, 25, 26 and 32. Their order was changed so no two consecutive chapters run them the same way. Everywhere else, the season content was folded into scenes and closers, and no branch was dropped:

- **ch4:** "Every house has one" was removed and spread to L11, 30, 41, 94 and 127.
- **ch5:** spread to L41, 58, 60 and 66.
- **ch6:** spread to L57, 59, 72 and 105. The high performer gets L103.
- **ch10:** spread to L39, 52, 60, 72 and 89.
- **ch11:** spread to L62, 64, 78 and 84. The high performer gets L15.
- **ch12:** spread to L61, 65, 73 and 81.
- **ch13:** spread to L13, 81 and 85.
- **ch14:** spread to L21, 31, 45 and 58.
- **ch15:** spread to L36, 40, 66, 68, 81 and 112.
- **ch16:** spread to L11, 13, 15, 26 and 30. Brandon's line stays.
- **ch17:** spread to L24, 26, 28, 30 and 32. The high performer scene is at L32.
- **ch18:** spread to L44, 68, 90 and 127. The high performer is in the Sabbath shop scene.
- **ch19:** spread to L85, 126, 128, 130 and 141.
- **ch20:** spread to L19, 34 and 47. The divorced section became "## Not your name".
- **ch24:** spread to L35, 46, 69, 78, 80 and 86.
- **ch27:** spread to L34, 40, 51 and 55.
- **ch28:** spread to L19, 25, 27, 76 and 82.
- **ch29:** spread to L51, 74 and 84.
- **ch30:** spread to L24, 37 and 110.
- **ch31:** spread to L21, 23, 33, 62 and 71.

Throwaways were cut at `18:150` and `31:81`. The "Single?" lines that only sent him to his mom now offer a second option: `22:99` (a married woman he serves alongside, with her husband there) and `24:90 → 24:115` (a sister in Christ, or carrying a load for a married couple he serves with).

## Fix 6. Course-shaped devices

- **(a)** `20:60` and `20:119`: the "pattern from Eden" list and its card heading are gone. In their place is Genesis narrative ("Adam never had to go looking for his garden…") and a card with place, people, hands and these years.
- **(b)** `15:19`: the four-beat Adam inventory is now "Sin bends a man inward. Left alone, it curls him around himself like a fist."
- **(c)** `13:28`: "knowing full well they'd doze off" is cut. The request (Mark 14:34) stays.
- **(d)** `29:42–59 → 29:38–45`: compressed into one paragraph of principles (small, early, outdoors, men he knows, his father last, the weeks after matter more), with a pointer to the leader guide. No "Then… Then…" sequence, no three-things template, and no "you're one of us".
- **(e)** `11:40` and `11:58`: the rite-of-passage checklist and the four-part list are gone. David and Paul carry the idea.
- **(f)** `12:73 → 12:71`: Grant's method is down to three sentences with no sequence. The scene, his sentence and "You eat yet?" stay.
- **Kept:** ch19's unmapped two gardens and its Do this week, and ch26's Ephesians 6:4.
- **`22:68`:** the words / time / touch / acts summary is replaced with two small, concrete pictures.

## Fix 9. Pronouns for God

Prose was swept in every file:
- ch6 (L44), ch8 (L9, 48, 95), ch9 (L84, 86, 98), ch10 (L21, 32, 41, 43, 45, 52, 62, 64, 68, 87);
- ch15 (L21), ch30 (L35, 86, 93, 120, 140), ch31 (L13, 97), ch33 (L11, 18).

A final heuristic scan of every prose sentence that names God, Father, Lord, Jesus or Christ next to a lowercase he/his/him finds only references to men. Margin blocks keep the NIV's lowercase.

## Fix 10. Lines and small errors

- **Softened or trimmed:**
  - `01:65`: "Go to the retreat. It won't do Tuesday's work for you."
  - `04:20`: cut "Hard news. Stay with me."
  - `06:89`: cut "That pulse is courage…"
  - `07:75`: reworded (see Fix 2).
  - `12:7`: God's "knock" line cut.
  - `16:28`: the bent-neck aphorism cut.
  - `17:103 → 17:87`: no longer scolds.
  - `21:13`: "A husband needs every one of those. Start now."
  - `21:104`: "None of it took hold in a week…"
  - `25:48`: "It went slower than he wanted… Most of a year went by… he'll still tell you it isn't fixed."
  - `33:83`: "Gold." cut.
  - `35:66`: "Which is exactly why everything is." cut.
- **Clarified:**
  - `11:74`: "The sentence itself you get from the Father."
  - `13:91`, folded into `13:13`: "Then he retires from the crew he saw every day, or he buries her…"
  - `05:126 → 05:124`: the single option now fits a young man with roommates.
  - `31:101 → 31:91`: "tell them".
- **Theology:**
  - `03:54` and `05:5`, tied to `05:77`: a dropped load becomes yours "once it lands in his house or his lane", and Galatians 6:2 and 6:5 are kept distinct.
  - `19:60`: "with our guilt laid on Him".
  - `20:17`: Zechariah 4:10 paraphrased accurately (the day of small things; the plumb line in Zerubbabel's hand).
- **ch7:** the "wife or roommate doesn't get told" list now appears once, in Do this week.
- **Headings:** `## Before you turn the page` at 16, 17, 20, 21 and 22 (and 18 from the first pass).
- **Length:** ch5 is now 1,999, ch9 1,999, ch13 1,991 and ch19 1,958. No chapter is over 2,000. ch2 got one sentence to stay at or above the 1,700 floor (1,706).

## Aaron's other decisions

- **5. Back cover:** "God's pay is a Father's inheritance, not wages." now sits under the creed in `wrap-back-copy.md`.
- **6. Dedication:** generic, with no names. The text is unchanged and was already name-free.
- **7. Panel defaults:** taken. The ch13 dozing line is cut, Ephesians 6:4 in ch26 is kept, ch19's three Gethsemane lines are kept, and Grant's method paragraph is collapsed. No part look-backs were added. Dangling edge marks in NIV excerpts are dropped; marks are never added.

## Follow-up, 2026-10-01 (Aaron: "recast them")

Wes reads as a friend at a table, a man among men, never a counselor or pastor that men come to. The whole book was swept for "across from me", "sit/sat with me", "men bring/come to me", "I hear … from a lot of husbands", "I asked him to…" and similar phrases. Lines where a named friend "told me" something, or where Wes asks a friend a question, were kept: they read as friendship.

| Where | Before | After |
|---|---|---|
| `00-introduction:3` | "The men across from me have been nineteen and they've been seventy." | "The men around those tables with me have been nineteen and they've been seventy." |
| `00-introduction:53` | "They're composites. The conversations happened, at real tables, with real men, and I've mixed the names and details so nobody can be picked out…" | "They're composites, built from real conversations with real men, with the names and details mixed so nobody can be picked out…" (agrees with the copyright note) |
| `02:19` | "Most men I sit across from have it." | "Most of the men I know have it." |
| `18:5` | "Men bring me their marriages, their tempers, their sons." | "Get men talking and it comes around to their marriages, their tempers, their sons." |
| `23:53` | "I once sat across from a man who looked at his screen through an entire hard conversation and then insisted he'd heard every word. Neither of us believed him." | "A buddy of mine once stared at his screen through an entire hard conversation with his wife and then insisted he'd heard every word. She didn't believe him. Neither did he." |
| `25:5` | "That's how Mitch opened, the first time he sat down across from me. I hear some version of it from a lot of husbands when the bedroom has gone cold…" | "That's how Mitch put it one night, after the game was over and the other guys had gone home. Get married men talking honestly and you'll hear some version of it when the bedroom has gone cold…" |
| `25:48` | "I asked him to put the ledger away for a season." | "I asked him if he'd try putting the ledger away for a season." |
| `27:13` | "Men sit across from me at fifty and can still repeat the exact thing…" | "I know men past fifty who can still repeat the exact thing…" |
| `00-copyright:34` (Disclaimer) | "The men in this book are drawn from real tables. Names, places, and identifying details have been changed, and in some cases men have been combined, so that no household can be picked out of a lineup." | "The men and stories in this book are composites. Names, places, and details have been changed or combined so that no household can be picked out. The author's own wife, children, wedding, and baptism are real." The Robert Lewis acknowledgment (L28) and the Biblica notice (L15) are unchanged. |
| `36:7` (new paragraph) | (none) | "The men in these pages are composites, with names and details changed. Where the author speaks of his own wife, kids, wedding, and baptism, those are real." To stay in the 80–150 band (141 words), the sentence describing the class materials was cut. |

**Kept, with the reason:**
- `02:7`, "What I told him across that table": a diner conversation with a friend.
- `13:39`, "I've asked a lot of guys…" and `15:66`, "I've watched a lot of men run programs": a man among men.
- `21:3`, `25:7`, `28:19`, `30:7`, `34:3`: Wes asking a friend a question, or a friend asking Wes.
- `31:93`: the 988 counselor is the professional, not Wes.

**Checks after the follow-up:**
- The sweep finds 5 brief-regex hits and 1 extra-fence hit, all on the copyright acknowledgment.
- Prose has 0 dashes.
- The 8-gram transcript overlap in prose is 0.
- NIV: 132 exact, 17 edge drops, 9 excerpts, 0 mismatches, with no margin block touched.
- The binder parse finds 0 problems.
- Chapters run from 1,706 to 1,999 words (ch18 is 1,996 after the recast; ch25 is 1,999).
- The book is 69,514 words, +1.2% against 68.7k.

## Restore, 2026-10-01 (Aaron: original bio, byline presented as the author's name)

- **`36-about-the-author.md`** is restored, byte for byte, from the source manuscript (`_grok47-panel-rev-2026-09-25/book/36-about-the-author.md`). That is the bio as it stood before the first-pass rewrite: 306 words by `wc -w`, 310 by the report's token count. The "324-word" count in the request belongs to the first pass's reworded version of the same bio; this restores the text before that rewording. The bio has no dashes, no old mark wording and no creed, so no house-rule edits were needed. The interim short note and its composite paragraph are gone.
- **Byline-nature mentions removed.**
  - Book: the only one was About the Author line 3, which is now gone with the restore. The copyright page, intro, wrap and contents never had one.
  - Meta: the rows in CHANGELOG, REWRITE-REPORT and DRAFTING-LOG are reworded.
  - The working copies of `SECOND-PASS-BRIEF.md` and `FOCUS-GROUP-2026-10-01.md` are redacted minimally, each with a copy note at the top. The unedited originals are on the box.
  - A search of the whole folder for those terms, and for any line saying the byline is not the author's own name, finds 0.
- **Copyright disclaimer:** unchanged. It already keeps the composites line, and no sentence in it implies the author's name isn't real. "The author's own wife, children, wedding, and baptism are real." stays. The Robert Lewis acknowledgment and the Biblica notice are untouched.

**Claims in the restored bio that contradict or strain the book as it now stands** (reported only; not changed):

1. **"Steadfast Men, the twenty-four-week training behind this book, began at one of those tables…"** The intro (L61) says the training was built afterward, "on the same backbone", and About used to say the book "grew up alongside it". The bio makes the training the source of the book; the intro makes it a companion.
2. **"church classrooms… It has since been taught in living rooms, garages, church basements, and online"** and **"When he is not working or teaching"**. These present Wes as the class's teacher and leader. The prose recasts did the opposite: ch24:7 ("I've sat through enough funerals"), ch26:3 ("From the second pew at a wedding"), and the follow-up lines at intro:3, 02:19, 18:5, 23:53, 25:5, 25:48 and 27:13 all make him a man among men at the table. The bio's own "He is not a pastor and he is not a counselor" agrees with those recasts. The teaching role is the strain.
3. **"A few older men kept a chair for him when he had nothing worth setting on the table."** The book's only first-person mentor story, Harlan's "Ride with me Saturday" and "Well. You paid attention." (ch14), now belongs to **Travis**. The book never shows a man mentoring Wes; only the dedication's "men who pulled a chair out for me" echoes this.
4. **"He is a husband, a father of two, and a Texan. By day he leads teams in technology."** The book has no first-person career or home-state detail. The career clause at 01:15 was cut under the narrator rule. Aaron's narrator decision and the copyright disclaimer name only his wife, children, wedding and baptism as real. "Father of two", "Texan", "leads teams in technology", the teaching history and the hobbies all go beyond that list. If any of them isn't true, it is the invented biography that the persona and canon forbid ("No fake Wes Hart biography"). The panel had flagged this bio as "made up" (FOCUS-GROUP, settled item 1).
5. **The other men's stories (Cody's truck, ch15; Clay and Vernon's tractor, ch31; the old rancher's callus, ch35; Travis's wedding, ch14).** The bio claims none of these, so there is no direct contradiction. Item 3 is the only overlap.
6. **No conflict:** "a husband… on a long walk with his wife… outside with his kids" matches 01:15, the dedication and the disclaimer. "He set out to stop being the passive husband and distracted dad" matches the narrator's self-owns. "He is a layman" and "not a pastor… not a counselor" match the recast clergy and counselor lines. The bio has no old mark wording or creed, and no dashes, so nothing in it needed a house-rule change.

**Checks:**
- The sweep finds 5 brief-regex hits and 1 extra-fence hit, all on the copyright acknowledgment.
- Prose has 0 dashes.
- The 8-gram transcript overlap in prose is 0.
- NIV: 132 exact, 17 edge drops, 9 excerpts, 0 mismatches. No margin blocks were touched.
- The binder parse finds 0 problems.
- The book is 69,683 words, +1.4% against 68.7k, inside the band.
- Chapters run 1,706 to 1,999 words.

## Review changes, 2026-10-03 (Aaron's book notes: no chapter cross-references; center the four-marks page)

See `REVIEW-2026-10-03-CHANGES.md` for the full before/after table. In short:
- 34 cross-references to other chapters were reworded into plain book language.
- Standalone figure pages (the ch3 four-marks block and the ch34 man-plan) are now centered on the page.
- Rebuilt at 238 pages, FAIL 0. The blank pages and chapter openers match 2026-10-02.
- Backup: `/workspace/backups/pre-xref-centering-2026-10-03/`.

## Review Print 2026-10-03b: four-marks figure placement fix

- The ch3 figure trigger now normalizes curly and straight apostrophes, so the four-marks figure follows the creed sentence as designed. It sits whole at the top of printed p. 22.
- Still 238 pages. Same blank pages and same chapter openers.
- Details: `REVIEW-2026-10-03-CHANGES.md` section 4.

## Review Print 2026-10-03c: full-width four-marks callout

- The ch3 four-marks block is now typeset, not a PNG. It runs the full text width, with navy top and bottom rules, a teal label, and centered navy caps.
- The ch34 worksheet is aligned to the text block.
- Still 238 pages. Same blank pages and same chapter openers.
- Details: `REVIEW-2026-10-03-CHANGES.md` section 5.

## Review Print 2026-10-03d: Your Turn lines no longer open with "Because"

- 105 closer lines across all 35 chapters were rewritten so each reason opens as its own plain statement, with varied wording. Only the opening sentence changed.
- Still 238 pages. The blank pages, chapter openers and Your Turn pages are unchanged.
- Details: `REVIEW-2026-10-03d-BECAUSE-CHANGES.md`. DRAFTING-RULES.md has an override note.
