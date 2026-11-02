# Batch report: E073-E080 (podcast v3 rewrite)

Branch: `podcast-v3-e073-e080`. Prepared for Aaron Maberry. All eight episodes were rewritten from the v1 drafts in `scripts/` into `scripts-v3/`. No existing file was edited or deleted. Length overrides and rule fixes are logged in `scripts-v3/CHANGELOG-V3.md`.

## Status

All eight scripts are finished. Each passes `_build/lint.sh` with no FAIL and no WARN, and each was timed with `_build/timing.py`. That timing also set the YouTube chapter timestamps, applied with `_build/apply_chapters.py`. Every script got one listener reread, and the batch got a check for repeated phrases (below).

| Episode | Format | Spoken words | Minutes (timing.py) | Wes / Jonathon words | Jonathon share | Jonathon lines under 12 words | Longest Wes turn | Lint |
|---|---|---|---|---|---|---|---|---|
| E073 Feelings Are the Dash, Not the Wheel | Main | 8,061 | 53:02 | 4,053 / 4,008 | 49.7% | 13.8% (12 of 87) | 113 | Pass, 0 FAIL, 0 WARN |
| E074 Field Notes: Dash and Wheel | Field Notes | 3,609 | 23:56 | 1,814 / 1,795 | 49.7% | 12.8% | 101 | Pass, 0 FAIL, 0 WARN |
| E075 Every Season Still Counts | Main | 7,108 | 46:55 | 3,574 / 3,534 | 49.7% | 16.5% | 97 | Pass, 0 FAIL, 0 WARN |
| E076 Field Notes: Season Swap | Field Notes | 3,203 | 21:14 | 1,642 / 1,561 | 48.7% | 15.0% | 111 | Pass, 0 FAIL, 0 WARN |
| E077 When the Job Goes Away | Main | 7,105 | 46:48 | 3,657 / 3,448 | 48.5% | 13.3% | 108 | Pass, 0 FAIL, 0 WARN |
| E078 Field Notes: Between Jobs | Field Notes | 3,703 | 24:28 | 1,861 / 1,842 | 49.7% | 11.6% | 101 | Pass, 0 FAIL, 0 WARN |
| E079 Grief at the Table | Main | 7,062 | 46:41 | 3,701 / 3,361 | 47.6% | 6.5% | 100 | Pass, 0 FAIL, 0 WARN |
| E080 Field Notes: Grief Report | Field Notes | 3,399 | 22:30 | 1,730 / 1,669 | 49.1% | 17.9% | 95 | Pass, 0 FAIL, 0 WARN |

Word counts cover spoken lines only. Stage directions, bracketed cues and parentheticals are excluded. No Wes turn runs over 120 words in any episode. There are no em or en dashes and no mid-sentence colons in spoken lines, and no "this week" anywhere.

**Mic share and chemistry.** In every episode Jonathon has between 47% and 50% of spoken words, and under 20% of his lines are short. In each main he pushes back for real at least once and tells at least two of his own stories:

| Episode | Jonathon's push-back | Jonathon's stories |
|---|---|---|
| E073 | "Anyway" with no reading is cardboard with better manners (the man at the top of the board); and he won't tell Dani about "left out" on her first night, which turns Wes around on mic | The midnight drive down 45 at seventeen, left out, the man at the top of the board, the warranty Saturday, the seven o'clock text, Ruby's two words |
| E075 | A job that's only a job isn't a sin at fifty-two, and the weight is at the supper table first (Wes concedes the order); some gray men are thirty-year-old jerks with practice | Manager at twenty-eight and the regional-pay search, four years of not having people over (his motive audit), dating the way he sold at twenty-five, Tuesday bedtimes at thirty-seven |
| E077 | "The job was never your name" (the work carries character); "Did you make it easy to ask?" (Wes concedes partly); the foundation | The installer's interview sentence, his mother's six weeks at the library when he was thirteen, living in Q4, interviewing for his own job at thirty-one, hiring the fifty-nine-year-old |
| E079 | Grief is "sideways and straight," not men and women; Mr. Abernathy's four Thursdays (somebody should've driven out to the fence; Wes agrees); leave the boy home, unsettled | His father leaving and the breakfast man's "Sounds like you're grieving him," the rep who lost his wife, the baseball against the garage door at nine, his mother's line for Ruby |

Field Notes also carry a disagreement each:

| Episode | Disagreement |
|---|---|
| E074 | Austin's kids: Jonathon says let the son see some tears; Wes says not about their mother, not yet. Settled partly ("Sad and steady. Not sad and needing them.") |
| E076 | "Older men go first": Jonathon answers with his breakfast text to Wes. Settled on "Whoever sees it first." |
| E078 | The 2009 coworker: Wes has the number and hasn't called. Jonathon: "Same lie, newer phone." Wes agrees to call before they next sit down. |
| E080 | Wes pushes back on Jonathon's "take the exit" past his dad's old house. Settled: take the exit, with his sister. |

## Warnings I could not clear (decisions for Aaron)

1. **New detail about Wes's own life.** Wes Hart is your pen-name host, and v3 adds personal details for him. None of them changes canon as I read it, but please strike any that misrepresent you. The main ones:
   - E073: his dad's whistle as the house's only gauge, the porch talk with his wife, his knee predicting rain.
   - E075: "when we get the barn finished," the welding lesson and the caterpillar bead, the legal pad, his mother counting his PT reps.
   - E076: the "about nine speeches" drawer and the "I can't sign that" story.
   - E077: mowing the yard twice in 2019, the copier's toner schedule, the 2009 coworker who moved to Amarillo, his review fear.
   - E078: his wife's plan since 2019 and the son's "What would you have said?"
   - E079: the 2009 call ("Took you long enough"), the Monday after his dad died, the funeral sentence to his six-year-old, Mr. Abernathy's "Booth's here" voicemail.
   - E080: the youngest's answer ("I thought it meant I wasn't supposed to either"), the fence pliers, his wife's nine years of waiting.
2. **Details about Wes's wife.** She keeps her hand on his arm on the porch (E073), had her own plan and her own number since 2019 and 2009 (E077, E078), remembers a pecan pie (E079), and has a line in E080. All light, all new.
3. **Mr. Abernathy.** E079 has him leave Wes alone four Thursdays after Wes's dad died and then leave a voicemail. Jonathon calls that wrong and Wes agrees "that time." Please confirm you're comfortable with a mild on-air criticism of him.
4. **The anniversary is not reported in the batch.** E079 sets Wes's dad's anniversary for "a week from Thursday" (Thu Oct 14). E080 releases Fri Oct 8, before it, so the tailgate day is reported in the next batch, not here.
5. **The installer's answer is still open.** The north-side outfit calls by Fri Oct 8 (E080), after E080 records. The next batch owns the outcome.
6. **988 and the domestic violence hotline.** 988 appears in every episode except E076 (depression, job loss, grief, dark stretches), in a spoken line, the challenge text, or both. E076 has none, since nothing in it touches mental health. The DV hotline line runs alongside it wherever home safety comes up.
7. **CHANGELOG merge.** This branch creates `scripts-v3/CHANGELOG-V3.md`, and so does `podcast-v3-e025-e032`. Merging both branches will conflict on that file. Keep both batch sections.
8. **Lint "week N" false positive.** My own check flagged "a week off me" in E077; it's not a training reference, and lint passes it. "Weekend" appears once in E077's header table, which isn't spoken.

## Continuity assumptions and fixes

- I took continuity from the v1 drafts, `hosts/JONATHON-CHARACTER.md`, `hosts/WES-HART-HOST.md`, `production/WARDROBE.md`, the calendar, the show bible, and the earlier v1 episodes these reference (E027, E029, E039, E043, E053, E054, E055, E057, E070).
- **Already told on air, treated as known:** Wes's father's A&M scholarship (E029, E053), the barn memory (E053), Jonathon's parking-lot tears at twenty-nine (E055), Mr. Abernathy going first with the gas receipt and the nineteen days (E039).
- **E073's divorced caller** was changed so he doesn't repeat E074's Austin.
- **Dani** is quoted in E076 (one line) and E079 (two lines), and only reported in E078 and E080, so she isn't quoted in back-to-back episodes.
- **The motive audit** runs once in E075 and once in E077. "Sir" appears once, in E077.
- **Plugs** are present tense: E075 (book chapter 32) and E079 (training session 13). E073 and E077 have none, and Field Notes have none.
- **Scripture** cards are NIV, quoted exactly: Psalm 42:5 (E073), Proverbs 20:29 (E075), Matthew 6:34 (E077), John 11:35 (E079). Other passages are paraphrased in the hosts' own words, never presented as quotes.

## Listener reread

Each script was reread once as a listener. Then a scan of every six-word phrase in the spoken lines across all eight scripts turned up repeats such as "I'd give a lot," "That's fair," and "good man" stacking up in neighbouring episodes. The later uses were reworded. The repeats that remain are intentional:

- the locked opens, the slate, and the credits line
- "Going first," "Here's the challenge," "Pull up a chair," and the "Carry this" close
- canon quotes used as callbacks ("Booth's here," "the scariest text I ever sent a man," the installer's interview sentence)
- each Field Notes check quoting the previous Tuesday's challenge

**Keeping the last ten minutes alive:**

| Episode | What happens in the last ten minutes |
|---|---|
| E073 | The callers, then Wes's one true word at supper, Jonathon's Thursday text and Wes's "I'll answer with more than K" |
| E075 | The callers, then Wes's second welding lesson and Jonathon asking the sixty-one-year-old what he's doing wrong |
| E077 | The callers, then Wes's kitchen-table money talk and Jonathon's fear about the installer lunch ("Ask him one thing and eat your burger") |
| E079 | The callers, then the tailgate plan and an unsettled fight about bringing the boy, ending with the funeral sentence |

## Continuity rows (what each episode establishes on air)

Each row adds to the v1 continuity row for the episode, which still stands. The full text is in each script's "New continuity (v3 additions to v1)" header row.

| Episode | Established on air |
|---|---|
| E073 Feelings Are the Dash, Not the Wheel (Tue Sep 14) | Jonathon at seventeen drove his mom's car down 45 near midnight at about ninety and turned around at the causeway; he never told her. The wise thing Wes didn't say in the truck ("You were going to preach in a truck"). Jonathon won't tell Dani about "left out" on her first night, and Wes changes his mind on mic ("Timing's part of the wheel"). The man at the top of Jonathon's first sales board ("I'm good, man") who walked away from his job and his family. "Anyway" with no reading is cardboard with better manners; "A vote. Not the keys." Jonathon read his mom's dash before his own. Wes's dad's whistle was the house's only gauge, and Wes never asked about the no-song days. Wes told his wife "afraid" on the porch. Guilt points back toward the couple, shame points to the door. Wes's knee predicted rain three times since July. The divorced caller's kids talk about their stepdad at supper. Psalm 42:5. 988. No plug. |
| E074 Field Notes: Dash and Wheel (Fri Sep 17) | Night one at supper was Tuesday. Thursday's "glad": the youngest laughed at supper for the first time since the breakup, at the dog. The man Wes called back has worked with him about twelve years. Jonathon didn't tell the VP "embarrassed"; he'll say "You were partly right." "Left out" still not told to Dani. Jonathon's parking-lot tears at twenty-nine in detail (the engine running, about twenty minutes, the man with the water). The disagreement about Austin's kids ("Sad and steady. Not sad and needing them."). Joseph wept more than once. |
| E075 Every Season Still Counts (Tue Sep 21) | Jonathon made manager at twenty-eight and got the region at thirty-four. The swallowed speeches and "There's a drawer." Jonathon's motive audit: four years without having people over because a house with milk on the couch can't win a room. Wes's "when we get the barn finished." "Supper table first. The building second." The welding lesson, the caterpillar bead, "Slow down at the end." Wes's mother counts his PT reps. The young rep's "Does he always talk to people like that?" and "There are no dues." "Time makes you more of whatever you were practicing." The legal pad: "I want to train whoever takes my desk, before anybody needs me to." Wes at twenty-one in the Buick. Thirty-seven: Jonathon will let Tuesday bedtime run long and write down one thing Ruby says. Proverbs 20:29. Book chapter 32 plug, present tense. |
| E076 Field Notes: Season Swap (Fri Sep 24) | The youngest picked "the same bead" and made Wes run it six times; the gate hinge comes "when you can do six in a row." The review line went on the form; "Are you retiring?" "No." The sixty-one-year-old's correction included Jonathon. Ruby: "Daddy, when I'm big will you still do the voices?" Dani: "You came back and you weren't on your phone." Wes has about nine speeches in the drawer. "Whoever sees it first" goes first; Mr. Abernathy went first, then left the asking to Wes. Wes's "I can't sign that. Here's what I can sign." Wes's dad's heels, last and twice. Jonathon's write-up of a nineteen-year man for four minutes late. Wes's wife is at her sister's. |
| E077 When the Job Goes Away (Tue Sep 28) | The installer's interview: "My dad did this. I'd like to be better at it than him." Jonathon's motive: "I wanted him to like me while I took his job." The wagon walk without his phone. "The work can carry your character. It can't carry your name." Jonathon's mother's library weeks and her brown-bag lunches. "I've lived in Q4 since about March." Wes in 2019: the yard mowed twice, the kitchen sink on a Thursday, the toner schedule, three silent men's breakfasts. "Did you make it easy?" and the drawer left open for Wes's son. The caller's plant, his wife's extra shifts and the son-in-law's question; "Sir" once. Wes's 2009 coworker who moved to Amarillo. Jonathon at thirty-one interviewing for his own job. "Everybody I knew needed something from me." Wes's wife carried her own number in 2009. The A&M scholarship named as known. Jonathon hired a fifty-nine-year-old. "Ask him one thing and eat your burger." Matthew 6:34. 988. No plug. |
| E078 Field Notes: Between Jobs (Fri Oct 1) | Wes's wife's plan since 2019 ("You came home and dried dishes for three weeks"). The open drawer: "What would you have said?" "Some days stay, some days go." "I didn't want a speech." Wes has the 2009 coworker's number; "Same lie, newer phone"; he'll call before they next sit down. Jonathon told the installer about his mother at thirteen; "Yeah. She knows." The trade-school idea, and Jonathon is getting him a name. Lunch Thursday: burger, one question, the interview sentence. Dani laughed at the plan and circled the crossed-out line on the sticky note in red (reported, not quoted). Jonathon wasn't looking when he found God at twenty-nine. Wes's dad's drought year: "I think it was both." "We're going to get through this together, and God hasn't moved." |
| E079 Grief at the Table (Tue Oct 5) | The 2009 call on the porch Sun Oct 3: "Wes Hart. Took you long enough." His wife kept a list of who called, and it was short; she died in 2021; "I'll put you on it for her." "Sideways and straight." The hospital "I'm proud of you" over ice chips. The Monday after Wes's dad died, and the gutters. Wes has never asked his brother whether he likes the work. Mr. Abernathy's four Thursdays, "Booth's here," and Wes agreeing he'd rather drive out. Jonathon's father left on a Saturday in October; "Sounds like you're grieving him." "Tell her I'm planning on being a lot of trouble for a long time." "I'm being strong for Grandma." Pancake, the dog they don't have. The 2009 man ate in his truck about a month. The pecan pie. Jonathon's rep and "I should've asked about her, not the numbers." The garage door at nine. The parking lot at Mr. Abernathy's funeral ("Twice?"). Wes's mother counting reps, read as grief. "I'm bringing lunch Tuesday"; don't lead with heaven. The tailgate plan for a week from Thursday, the boy unsettled. Dani quoted twice. John 11:35. 988 and the DV hotline. Training session 13 plug, present tense. |
| E080 Field Notes: Grief Report (Fri Oct 8) | Wes told the youngest the funeral sentence when he asked him to come: "I thought it meant I wasn't supposed to either." "Do I have to talk?" Jonathon still disagrees about the boy, a little less. The Amarillo man's wife's date is on Wes's calendar (in February). The installer lunch Thu Sep 30: "He died my second year." "I said that?" "I'm not better than him yet." Jonathon made it to about the fries. The answer from the north-side outfit comes by Fri Oct 8. The dented tailgate in the parking lot. The sixty-one-year-old rides in the truck most Wednesdays. "I've been waiting nine years for you to bring him up at supper." The fence pliers for the tailgate. Grief keeps finding things (the okra). "Take the exit," with his sister. "A list of who remembered." Dani reported, not quoted. 988. |
