# Second-pass working rules (Opus 5.5, 2026-10-01)

These are the rules given to every chapter editor on the second pass. The authority for them is `meta/SECOND-PASS-BRIEF.md`, `meta/FOCUS-GROUP-2026-10-01.md`, and Aaron's locked decisions of 2026-10-01 (below). Every rule in the first-pass `meta/DRAFTING-RULES.md` still applies unless this file changes it.

**This is a tightening pass, not a rewrite.** Keep the same voice, the same people, the same structure. Edit surgically: change what the fix list asks for, smooth the seams, and leave everything else alone. Every chapter should come out **the same length or shorter** than its first-pass count, between 1,700 and 2,000 words in total (closer included). It must not go over 2,000.

## Paths

- Work only in `biblical-manhood/book/_opus55-second-pass-2026-10-01/book/`. File names stay the same.
- Line numbers in this file and in FOCUS-GROUP refer to the first-pass text. The copy started out identical, so find each line by its content.
- Checks: `python3 biblical-manhood/book/_opus55-second-pass-2026-10-01/meta/tools/checks.py sweep FILE.md` (must be clean: 0 SWEEP, 0 extra, 0 FORMAT) and `... sim FILE.md` (shows words).
- Do not open transcripts, briefs, notes, PHD-MASTERY, or FRAMEWORK. No git. Don't touch any other path.
- **Don't edit the text inside `:::margin` blocks.** The lead fixes all NIV punctuation centrally. You may move a block, as long as it still sits right after the sentence that cites it. Don't add or delete blocks unless your list says so.

## Aaron's locked decisions (2026-10-01)

1. **Narrator.** Aaron's real life is his wife, his kids, and his baptism. Keep those in first person, and don't add new details about them. Every other first-person life story becomes a story about a man Wes knows, told in the third person. Habit-level self-owns with no invented facts ("I've held back on every one of those and called it being careful", "I've gone mute in front of my own family") stay. Use the assignments below so every chapter tells the same story.
2. **Clergy lines.** Recast `26:3` ("Officiating a wedding…") and `24:7` ("I've stood up front at enough services…") as the view of a guest or friend.
3. **NIV.** The lead handles this (see above). The no-dash rule still applies to all prose outside margin blocks.
4. **Ch7 is retitled "Work for God's Pay".** If your chapter names the old title "Live for a Reward That Lasts" as a chapter reference, change it to **Work for God's Pay**. The ordinary phrase "the reward that lasts" can stay.

## Global consistency table (use exactly)

| Who | Rule |
|---|---|
| **Dale** | Only ch13's Dale (ER clipboard, Thursday brother; also `34`, `35:32` Micah's breakfast man). |
| **Russ** (new) | Renee's husband in ch24. He replaces ch24's "Dale" everywhere in ch24. |
| **Gil** (new) | The county grader in ch30. He replaces ch30's "Dale" everywhere in ch30, including the head "Why I told Dale yes". |
| **Travis** (new) | The young man in ch14 who caught Harlan at his truck, rode the feed route, and at **Travis's** wedding heard "Well. You paid attention." Third person: Wes knows Travis and tells his story. "Ride with me Saturday" and "Well. You paid attention" stay verbatim. |
| **Cody** (new) | ch15's body-shop man. The first truck with the bubble on the fender, and the three springs of wasted paint, are **Cody's**. "Paint's not going to fix that. It's coming from the inside." stays verbatim. Wes tells it in the third person ("Cody's first truck…", "Cody stood in that shop…"). |
| **Clay** (new) | ch31. Vernon taught **Clay** to drive the tractor and call out the gauges. The perfect row and the climbing needle are Clay's. Third person. Vernon stays. |
| **Grandfather** | `35:74`: no "my grandfather". Make it generic: "the callus a fence stretcher leaves on an old rancher's hand". |
| **Ch29 creek** | The narrator was **not** there. Alton or the boy's dad told Wes about it. The five men in the creek are Alton, the dad, the dad's brother, the friend the dad meets with every week, and a neighbor who taught the boy to fish. Drop "And me." |
| **Wade** | ch15 and ch26 are the same man. In ch26, add one clause such as "the same Wade from the body-shop chapter… who watched his daughter shrink". Match ch15's facts. |
| **Walt** | His real on-page facts: fifty-five, one truck to eleven, the 6:15 fork, the shop quieter than the house, twenty years of "one more hour" (`01:5`); he sold part of the company and is chasing his wife again, first time since '94 that it's only the two of them (`32:55`). **There is no bank parking lot and no "three hundred contacts".** |
| **Hollis** | ch34: he wrote "Tell Cole he's a good man" in the notebook, it sat about three weeks, he said it, and Cole sat in his truck and cried for twenty minutes. Cole is a man Hollis knew. "Hollis asked Roy about it every Thursday" (ch34): that's **Hollis's Thursday table** (ch33:50). |
| **Mr. Pruitt** | A widower: married fifty-one years, and the spring after he buried his wife he planted forty pecan trees. Ed comes for coffee on Wednesdays. Seventy-six in ch35. |
| **Micah** | The single man from the intro roster: six years at the single men's table at weddings, now married (ch35). He **is** ch21's moving-box man. Name him Micah in ch21. |
| **Mr. Alvarez** | The caregiver who bathes his wife every morning. Married in 1968. Her mind has let go of his name. He's been caring for her like this **three years**. Named in ch23 (first appearance), called back in ch32 and ch35. **Cut** the caregiver picture from ch25 and ch30 (the content point can stay without the bathing image). |
| **Coffee for the wife** | Belongs to **Roy** only (ch33, ch35). Cut it from Alton in ch30 (keep "A man with no job by noon is a man in a chair by two") and cut the generic version at `09:78`. |
| **Plumb bob / plumb line** | ch17 is where it's taught. ch29 keeps Alton's plumb bob and his few words to the boy, but not a second lesson on how a plumb bob settles. ch33 has no plumb bob for Roy's grandson; cut it, or use a different image. |
| **Adam's silence** | ch19 is its home, with one glance in ch4. Cut the versions in ch3 (lead) and ch15. |
| **Feelings-first books jab** | Only in the intro. Cut `02:33`. |

## How to handle the seasons (Fix 5)

- **Never drop** a single, divorced, widowed, no-child, older, or high-performer branch. Those branches are why readers buy the book.
- Standalone season sections stay **only** in ch8, 9, 21, 22, 23, 25, 26, and 32.
- Everywhere else, fold the season content into the scene it belongs to, or into the Do this week / Tell a brother lines, as a clause or a sentence. Cut throwaway one-liners that add nothing.
- Don't list the seasons in the same order as the previous chapter. Avoid the stock order single → new dad → divorced → older → high performer.
- Give the high performer at least one line with weight inside a scene somewhere in your chapters, not only at the end of a list.
- "Single?" options that only say "ask your mom" get a second option: a sister in Christ, a married couple he serves, or his roommates.

## The inheritance anchor (Fix 3)

- The full anchor stays in intro, ch3, ch7, `30:22`, and `34:47`. ch33 keeps one clause.
- Everywhere else, keep an anchor **only** if the same paragraph uses pay, reward, or wages. If you cut the anchor, cut or soften that paragraph's pay/reward language with it, so no "work hard and God will save you" reading is left.
- Cut or trim these: `04:108`, `05:103`, `06:31`, `16:17`, `20:58`, `21:112`, `23:78` (keep short), `24:29`, `25:71`, `32:16` (shorten), and the tail of `35:44` (keep `35:83`).
- No accounting or commerce words for God's side (ledger, books, payroll, return, the math, the check cleared, pays best, keeping count). Use family words: son, Father, inheritance, welcome, "well done".

## Other rules

- **Pronouns.** In prose, God and Jesus take He, His, and Him. Sweep your files. Margin blocks keep the NIV's lowercase.
- **Headings.** Use `## Before you turn the page` wherever a chapter has "## Before you turn". Ch35 keeps `## Before you close the book`. Other unique heads such as "Before the bell" stay.
- **Protected lines.** Keep every protected line in FOCUS-GROUP "Keep, and don't break". If a fix seems to need a protected line changed, don't change it; report it.
- **Creed.** It appears only in intro, ch3, ch7, ch34, and ch35 (once each, ch3 up to two). Don't add it anywhere else.
- **Persona.** Warm first, one clean hit, stay, next move. No new Wes Hart biography.
- **Sweep.** No em or en dashes in prose. No closer label at the start of a prose line. The brief regex and the extra fences must stay at 0.

## Report back (per chapter)

1. Before and after word counts (`checks.py sim`).
2. A changelog: one line per fix item, with the item ID (e.g. Fix 1, Fix 5, Fix 10, L1, Narrator), the first-pass line, the new line number, and what changed (short quotes).
3. The anchor sentences that remain for any pay/reward language, with line numbers.
4. Anything you couldn't do without touching a protected line.
5. The final `checks.py sweep` output.

## Per-chapter fix lists

### ch01
- Narrator: at `01:15`, keep the wedding, the first child, the funerals, and the baptism (Aaron's own), but cut "the job I took and the one I passed on" (career biography).
- Fix 10: soften `01:65` "Skip the retreat." It contradicts `01:23`, which honors big days. Big days are good, but they don't do Tuesday's work.
- Fix 9: pronouns.

### ch02
- Fix 4: cut the feelings-first books jab at `02:33`.
- Narrator: make `02:15` (sitting on the tailgate with the tools zipped in the bag) a figurative self-own ("I've been the man on that tailgate…") with no invented facts, or recast it.
- Fix 9: pronouns.

### ch04
- Fix 10: trim `04:20` ("Hard news. Stay with me.").
- Fix 4: keep Adam's silence at `04:66` as a single glance only.
- Fix 5: fold the `04:92` season paragraph into scenes and closers.
- Fix 3: shorten the `04:108` anchor; keep it only if pay/reward language stays in that paragraph.

### ch05
- Fix 10, theology: in `05:5`, the line "Carry what's yours, even when somebody else dropped it" needs to say when a dropped load becomes yours (when it lands in your house or your lane). Keep Galatians 6:2 (carrying another's burden) and 6:5 (your own load) distinct, and tie this to the ch5 passage at `05:79` that teaches the two words. Don't change the mark's one-line meaning in the text of ch3 (the lead does ch3).
- Fix 10: `05:126`, the single option ("take back one chore you've been paying someone else to do") doesn't fit a young man with roommates and no money. Give him one that does.
- Fix 3: shorten the `05:103` anchor.
- Fix 5: fold `05:68`.
- Length: must come in at ≤2,000 (it's 2,029 now).
- Keep "Absence purchased with a bigger paycheck is still absence", "Keeper is your job. Savior is already taken", and Tomás's broke Tuesday.

### ch06
- Fix 3: shorten or cut the `06:31` anchor.
- Fix 9: `06:44` "cost him less" should read "Him", plus any others.
- Fix 10: trim `06:89` ("That pulse is courage, felt from the inside.").
- Fix 5: fold `06:74`. Keep the alone-friendly Do this week (`06:135`) as worded.
- Keep the oak, "Watch me", and "Your number is second".

### ch08
- Fix 9: pronouns at `08:9`, `08:48`, `08:95`, and anywhere else.
- Keep the standalone season section; vary its order. Keep "Nobody ever sat in this seat for me" and "You are somebody's empty chair now".

### ch09
- Fix 4: cut the generic coffee advice at `09:78` (the coffee belongs to Roy). Keep the older-man branch with a different, concrete move.
- Fix 9: pronouns at `09:84`–`98`.
- Keep the season section (vary its order), Owen's mailbox with its friction, and "Pain was looking for a Father".

### ch10
- Fix 9: pronouns throughout (`10:21`–`91`); this is the worst chapter for them.
- Fix 5: fold `10:76`.
- Keep the pickup line, Curtis, and "the original was in the line before the bell".

### ch11
- Fix 6e: drop the four-part rite-of-passage list at `11:58` ("someone older, words worth keeping, weight on younger shoulders, and a seat among the men"), and the checklist feel at `11:40`. Let David and Paul carry the idea.
- Fix 10: `11:74`, "You get them from the Father": "them" has no clear antecedent. Fix it.
- Fix 5: fold `11:80`.
- Keep Nate, the utility sink, and "I've had my eye on you for years. You're a good man."

### ch12
- Fix 10: trim `12:7` ("that's what God had in mind for a grown son"), which puts a knock in God's mouth.
- Fix 6f: collapse Grant's method paragraph at `12:73` to 2–3 sentences with no sequence. The scene, his one sentence, and "You eat yet?" stay.
- Fix 5: fold `12:81`, keeping the divorce pull back to the mother's table that James likes.
- Keep "That's Pick Up the Weight, on your parents' front steps".

### ch13
- Fix 6c: cut "knowing full well they'd doze off" at `13:28`. Keep the request (Mark 14:34).
- Fix 10: `13:91` "lost the company that came with the job or with her" is muddy. Clarify it.
- Fix 5: fold `13:91`.
- Length: must come in at ≤2,000 (it's 2,022 now).
- Keep Dale and the clipboard, Kenny and "which row to put you in", and "One man, twenty minutes, every week."

### ch14
- Narrator: the Harlan story becomes **Travis's** (see the table). Recast `14:3`, `14:7`, and `14:79` in the third person.
- Fix 5: fold `14:75`. Keep "If you're the man ahead" (`14:43`–`62`).

### ch15
- Narrator: the first truck and the body shop become **Cody's** (`15:3`, `15:17`, `15:87`).
- Fix 6b and Fix 4: cut the four-beat Adam roll at `15:19` and Adam's silence at `15:29`. Keep "Sin bends a man inward" and one picture.
- Fix 9: `15:21` "Cain shrugged him off". Check whether "him" refers to God, and capitalize if so.
- Fix 5: fold `15:83`, keeping "I'm not going to hand you the whole blame" for the divorced man.
- Keep Wade's check-in (`15:47`–`51`); ch26 links to it.

### ch16
- Fix 3: cut the `16:17` anchor, and soften the hypocrites' "already collected" pay line so no anchor is needed.
- Fix 10: trim the `16:28` aphorism about a bent neck.
- Fix 5: fold `16:46`, keeping its strong Brandon line ("whether your title has started answering questions only your soul should").
- Heading: `16:104` should be `## Before you turn the page`.

### ch17
- Fix 10: soften `17:103` ("has just shown you his real north").
- Fix 5: fold `17:43`–`55`.
- Heading: `17:125` should be `## Before you turn the page`.
- Keep "Put the string on the wall".

### ch18
- Fix 5: cut the throwaway at `18:150` ("Winning at work? The garden was never a scoreboard"), and fold `18:140`–`150` without losing the single branch (`18:142`) or Abe.

### ch19
- Fix 10, theology: at `19:60`, change "as if the guilt were His own" to "with our guilt laid on Him".
- Fix 5: fold `19:126`–`134`, keeping "Hand hers to God".
- Length: must come in at ≤2,000 (it's 2,052 now).
- Keep the two gardens unmapped (no mark names inside them), the one link sentence, and the Do this week.

### ch20
- Fix 6a: drop the "pattern from Eden" list at `20:60` (ground to tend, a word to keep, brothers, rest) and the card heading "the Eden pattern" at `20:119`. Tell it as Genesis narrative plus the reader's own ground.
- Fix 10, theology: `20:17` Zechariah. Paraphrase it accurately: "Who dares despise the day of small things," and people rejoice to see the plumb line in Zerubbabel's hand (Zech 4:10). No chapter and verse in prose unless you add a margin block. Paraphrase without a reference.
- Fix 3: cut the `20:58` anchor, or keep it only if "well done" pay language stays in that paragraph.
- Fix 5: fold `20:68`–`83`.
- Heading: `20:98` should be `## Before you turn the page`.

### ch21
- Fix 1: name the moving-box man **Micah** (`21:3`, `21:102`–`104`).
- Fix 1: give Mr. Pruitt one or two sentences in the widower section (`21:31`–`37`).
- Fix 10: soften `21:13` ("That's most of a husband's job already") and `21:104` (it resolves too fast).
- Fix 3: cut the `21:112` anchor.
- Heading: `21:116` should be `## Before you turn the page`.
- Protect the rest of ch21: the box, the skillet, the three seats, "This isn't a lobby", the divorced and widowed seats, and "No wife yet still leaves you a man".

### ch22
- Fix 4: vary the wife's "same three questions" at `22:56` so it doesn't echo the brother check-in in ch13 (what mattered, what's heavy).
- Fix 6: vary `22:68` so love "landing" isn't a words / time / touch / acts summary that reads like a famous five-item framework.
- Fix 5: `22:99` single branch: add a second option besides his mom.
- Heading: `22:109` should be `## Before you turn the page`.
- Keep the postpartum paragraph, "I do not need you to fix it…", and the bird notebook.

### ch23
- Fix 4: name the caregiver at `23:84` **Mr. Alvarez** (first appearance; married 1968, bathes her every morning, three years).
- Fix 3: keep the `23:78` anchor, but short.
- Keep the season section, the wet floor, and "Being right is not the same as being a husband".

### ch24
- L1: recast `24:7` ("I've stood up front at enough services to know that silence") as a guest's view: "I've sat through enough funerals…". The funeral line is protected.
- Fix 1: Renee's husband is **Russ**, not Dale.
- Fix 3: cut the `24:29` anchor.
- Fix 5: fold `24:88`–`94`; `24:90` "Single?" gets a second option.
- Keep "I will give you the whole chapter in two sentences first.", the furnace sentence, and the funeral line.

### ch25
- Fix 10: `25:48` (Mitch and Dana) resolves too fast. Let it take longer: months, setbacks, no tidy "she comes looking for him now".
- Fix 4: cut the caregiver picture at `25:91`. Keep the midlife/body point without the bathing image.
- Fix 3: shorten the `25:71` anchor.
- Keep the season section, Eli's counter, and "A contract keeps score on her".

### ch26
- L1: recast `26:3` ("Officiating a wedding gets me the best spot in the building") as a guest's view ("From the second pew…").
- Fix 1: add one clause linking Wade to ch15.
- Keep Ephesians 6:4, the season section, and "I don't come to watch you hit. I come to watch you."

### ch27
- Fix 5: fold `27:61`–`69`, keeping the divorced call ritual and the no-son branch.
- Keep Ray's video and the daily/weekly/yearly rhythm.

### ch28
- Fix 5: fold `28:86`.
- Keep Lyle, "Well. I figured you could", "Pick the right hill. Stay on the step", and the Stop Waiting "flips" line.

### ch29
- Narrator: the creek is told to Wes, not witnessed by him (see the table).
- Fix 4: cut the repeat lesson on how a plumb bob settles (`29:36`). Keep Alton's own few words when he hands it over.
- Fix 6d: compress `29:42`–`59` into one short paragraph of principles: small, early, outdoors, men he knows, his father last, and the weeks after matter more. No "Then… Then…" sequence, no "each man brings three things" template, and no "you're one of us" formula. A sentence can point to the leader guide at walksteadfast.com for planning details.
- Fix 5: fold `29:63`, keeping the divorced dad, the single man, the granddad, and the daughter line.

### ch30
- Fix 1: the grader is **Gil**, not Dale (including the heading).
- Fix 4: cut Alton's coffee-with-his-wife detail at `30:57`. Keep "A man with no job by noon is a man in a chair by two." Cut the caregiver picture at `30:82`, keeping the point that unpaid or house work is real work.
- Fix 9: `30:95` "he saw it through" should read "He" if it means Jesus.
- Fix 5: fold `30:84`.
- Keep the `30:22` anchor in full.

### ch31
- Narrator: Vernon's tractor becomes **Clay's** story (`31:3`, `31:7`, and any other "I" in it).
- Fix 9: `31:13` "kill him", "his panel", and `31:107`.
- Fix 10: `31:101` should say "tell them", not "tell him", for the doctor.
- Fix 5: cut the throwaway at `31:81` ("Try it at home, where there's no bonus") and fold `31:71`–`81`.
- Keep the broom bush, 988, and "Your feelings read the engine. The Word drives the truck."

### ch32
- Fix 3: shorten the `32:16` anchor.
- Fix 4: Mr. Alvarez at `32:87` becomes a callback to ch23, with three years.
- Keep the chapter's season walk (the seasons are its content), "February has a job", and "Gardens change".

### ch33
- Fix 1: `33:46`, cut Roy's grandson's plumb bob (or use another image). `33:79`, change "a morning at a fence" to "a morning at a creek". `33:50`, make "Thursday table" Hollis's Thursday table, or cut the phrase.
- Fix 2: `33:31` "that's why it pays best" and `33:94` "He's already keeping count" need family wording, not accounting.
- Fix 3: keep exactly one anchor clause in ch33.
- Fix 4: Roy keeps the coffee (`33:56`).
- Fix 10: trim `33:83` "Gold." (the stacked fragment).
- Keep the four a.m. pour and "The crowd gets straw. The Father gets the gold you pour in the dark."

### ch35
- Fix 1: Walt at `35:30` and `35:55` points to his real facts (the 6:15 fork, the shop quieter than the house, part of the business sold, chasing his wife again). No parking lot. Hollis at `35:44` matches ch34 (he told Cole he's a good man, and Cole cried in his truck). Check the Dale/Micah line at `35:32`.
- Narrator: `35:74` "my grandfather's hand" becomes generic (see the table).
- Fix 3: cut the tail of the `35:44` anchor, and keep `35:83`.
- Fix 10: trim `35:66` "Which is exactly why everything is."
- Keep: the creed exactly once, Mr. Alvarez's callback at `35:20` (married 1968), Kenny on Tuesday, the open chair, "Be a brother", and Carry this exactly "Tuesday is when it will show. Get up."
