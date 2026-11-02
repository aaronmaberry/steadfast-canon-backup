# Batch report: E025-E032 (podcast v3 rewrite)

Branch: `podcast-v3-e025-e032`. Prepared for Aaron Maberry. All eight episodes were rewritten from the v1 drafts in `scripts/` into `scripts-v3/`. No existing file was edited or deleted.

## Status

All eight scripts are finished. Each passes `_build/lint.sh` with no FAIL and no WARN, and each was timed with `_build/timing.py`, which also set the YouTube chapter timestamps. Every script got one listener reread, plus a batch-wide check for repeated phrases (below).

| Episode | Format | Spoken words | Minutes (timing.py) | Wes / Jonathon words | Jonathon share | Jonathon lines under 12 words | Lint |
|---|---|---|---|---|---|---|---|
| E025 The Father Who Stays | Main | 8,001 | 53:32 | 4,070 / 3,931 | 49.1% | 16% (20 of 129) | Pass, 0 FAIL, 0 WARN |
| E026 Field Notes: Easter Week Report | Field Notes | 3,384 | 22:45 | 1,754 / 1,630 | 48.2% | 7% (4 of 55) | Pass, 0 FAIL, 0 WARN |
| E027 The Empty Chair at Your Table | Main | 7,359 | 49:24 | 3,934 / 3,425 | 46.5% | 13% (15 of 115) | Pass, 0 FAIL, 0 WARN |
| E028 Field Notes: The Chair Report | Field Notes | 3,397 | 22:45 | 1,703 / 1,694 | 49.9% | 15% (9 of 59) | Pass, 0 FAIL, 0 WARN |
| E029 When Your Dad Is Still Alive | Main | 7,516 | 50:11 | 3,879 / 3,637 | 48.4% | 13% (15 of 119) | Pass, 0 FAIL, 0 WARN |
| E030 Field Notes: Calling Him Back | Field Notes | 3,297 | 22:04 | 1,729 / 1,568 | 47.6% | 17% (8 of 48) | Pass, 0 FAIL, 0 WARN |
| E031 When Home Never Handed You Off | Main | 7,132 | 47:37 | 3,811 / 3,321 | 46.6% | 17% (17 of 99) | Pass, 0 FAIL, 0 WARN |
| E032 Field Notes: Cutting the String | Field Notes | 3,322 | 22:10 | 1,694 / 1,628 | 49.0% | 12% (6 of 49) | Pass, 0 FAIL, 0 WARN |

Word counts cover spoken lines only. Stage directions, bracketed cues and parentheticals are excluded. No Wes turn runs over 120 words in any episode.

**Lint budgets.** Ellipses are 0 in every episode. Long pauses sit at the maximum of 3 in E025, E027 and E029. Beats sit at the maximum of 10 in E027 and E029. Every other count is under its cap.

**Mic share and chemistry.** In every episode, Jonathon is between 46% and 50% of spoken words, and under 20% of his lines are short. In each main he pushes back for real at least once and tells at least two of his own stories:

| Episode | Jonathon's push-back | Jonathon's stories |
|---|---|---|
| E025 | "A heart is a heart" and "But I have a number" | Beaumont's duck tie, the sticky note |
| E027 | "You should have made him pay" | The whole Saturday, his sister |
| E029 | His mom's house "held" with the father weighing nothing; he refuses Wes's lamp example | Four VP emails, ten Beaumont calls, the hurricane |
| E031 | "My mom lives alone. If I'm not her guy, who is?" | "Not bad, kid," the rep, Theo at the Rodeo, the AC man, Ruby and the name |

Field Notes also carry a disagreement each:

| Episode | Disagreement |
|---|---|
| E026 | "Feelings are weather" |
| E028 | "Left," with Wes siding with Dani |
| E030 | Luke 17:3, "if he repents" |
| E032 | "You're telling a thirty-one-year-old to ration his mother" |

## Warnings I could not clear (decisions for Aaron)

1. **E032's locked open contains "this week."** The line is "Friday we report, two parts this week." It comes verbatim from `_build/intros_data.py`. The brief bans "this week" in scripts, but opens are locked, so I left it. Lint doesn't flag it. To change it, edit intros_data.py (for example "Friday we report, in two parts").
2. **E031 changes a canon quote.** Wes's mom's line is canon as "And don't come home every weekend." v3 says "And don't come home every Friday" to keep "weekend" out of the script, and the follow-up is "He came home every Friday the first semester." The meaning is the same. Either update the canon wording in `hosts/WES-HART-HOST.md` and the continuity rows, or revert the line.
3. **New detail about Wes's own life.** Wes Hart is your pen-name host, and v3 adds small personal details for him. None of them changes canon, but please strike any that misrepresent you:
   - E025: the sunrise bleachers cushion.
   - E027: the walk with a heifer and the prayer walk at six.
   - E029: the curtain beat when his son washes the truck, his folder of in-home-help brochures, his lips moving when he counts, and his dad's college-phone line "Here's your mother," which Wes caught himself repeating to his youngest.
   - E031: the feed-store "Thank you, sir" he never got, the Buick's contents (a box fan, a footlocker, a stereo bought with hay money, his grandmother's Bible), Mr. Abernathy asking his opinion on a younger man about two years in, his dad's "That'll do" and Wes saying it after an oil check, backing a trailer at forty-five, and his youngest's radio station.
   - E032: the twenty-five-foot tape measure, and the pay phone "running both ways" now.
4. **Two small details about Wes's wife.** In E029 she pats his arm at the folder and spots the counting from the calf pen. In E032 she makes Wes her first call too. Both are light, but they're new.
5. **Paraphrased scripture.** Every card verse is NIV and quoted exactly. Several other passages are paraphrased in the hosts' own words, never quoted:
   - E026: Mark 9:28-29.
   - E027: Colossians 3:21 and Ephesians 3:15.
   - E030: Luke 17:3, with Jonathon saying "I'm paraphrasing," and Mark 11:25.
   - E031: Luke 2:51-52.
   E031 also quotes Genesis 32:26 and Luke 2:48 exactly in the NIV wording, since both were in the v1 draft.
6. **The number "eleven."** Lint's round 7 number check counts eleven and twelve in E029 (7) and E031 (15). Most uses are canon (eleven seconds, Truck Saturday 11, Jesus at twelve, twelve to three). SHOW-BIBLE round 5 warns against a number becoming a motif, so E029's "count to eleven" callbacks are worth one look in the edit.
7. **Beat and pause budgets are at the cap** in E027 and E029 (beats 10 of 10) and in E025, E027 and E029 (long pauses 3 of 3). Adding any beat or pause in the edit will trip a WARN.
8. **Banter threads not used.** The brief lists Wes's knee and Dani running the budget as banter threads. The knee appears once, in E025, because the v1 round 5 notes ban a knee beat in E029-E032. The budget doesn't come up in this batch.

## Continuity assumptions and fixes

- **No other v3 batch had pushed a branch** when I checked, so there were no neighbouring continuity rows to read. I took continuity from the v1 drafts, `hosts/JONATHON-CHARACTER.md`, `hosts/WES-HART-HOST.md`, the calendar and the show bible.
- **E029's v1 reading narrative said Houston.** v3 says San Antonio, which matches the character file and every other script.
- **E030 contradicted E031, so E031 now carries the fix.** In E030 Jonathon says he'll tell Ruby the name after church, not at bedtime. Canon puts it at bedtime. In E031 Theo melts down over a sock seam after church, and Ruby asks for "a true story" at bedtime, so it happens there anyway.
- **E029's shoe night.** Wes says the first half of his E028 sentence ("Your grandpa worked hard, and he stayed"). His son asks the "proud" question before he gets to "I'm trying to." Wes never says "proud" on mic, refuses to rehearse it, and says it to his son at Thursday lunch (E030).
- **E031's "That'll do."** It happens on Truck Saturday 11 (an oil check), not the E029 truck wash, where Wes hid and said nothing.
- **Things kept off mic, as in v1:** the rep's name, the grandfather's name, and the hurricane's name.
- **E032's nephew text.** "day thirty six" is left unexplained ("It's his to say").
- **Chapter protection** from the v1 notes holds:
  - E029 stays clear of chapter 12, which is saved for E033.
  - E031 mentions Jacob only once, as something Jonathon noticed.
  - Nothing from the "avoided on purpose" lists in the v1 headers appears.
- **Dangerous fathers and unsafe homes** are carved out explicitly in E029, E030 and E031 (no call, honor isn't access, get help). No episode in the batch calls for the 988 line (the calendar lists it for E021, E081 and E082).
- **Plugs** are present tense: E025 (book), E027 (book), E031 (training session 11). E029 has none, and Field Notes have none.

## Listener reread

Each script was reread once as a listener. Then a scan of every six-word phrase in the spoken lines turned up about fifteen repeats across episodes, and the later occurrence of each was reworded:

- "practiced shutting up on the phone"
- "I have to push on that"
- "don't know what I am in that house"
- "might be the most honest"
- "I sat on the floor"
- "never once said a word about it"
- "the best thing that's happened to"
- "I could tell from"
- "I'm not going to make a speech"
- "I'm not going to tell you it is"
- "the guy whose dad was dangerous"
- "that was the whole"
- "he looked at me like I was"
- "you might be the only one who"

The repeats that remain are intentional:

- the locked opens and the credits line
- canon quotes used as callbacks ("Not bad, kid," "He never learned to say it")
- each Field Notes check quoting the previous Tuesday's challenge
- "Pull up a chair"
- "the Thursday table"

**Keeping the last ten minutes alive:**

| Episode | What happens in the last ten minutes |
|---|---|
| E029 | The breakfast bet, Wes refusing to rehearse "proud," Wes coaching Jonathon before the call ("Don't hang up on the beep," "Don't grade the call while you're on it") |
| E031 | The sock meltdown, "You could learn," the stock tank, Wes's affirmation |
| E030 | The 2 AM prayer and the "mean second call" hard case |
| E032 | Jonathon's three questions out loud and "Does Pat count?" |

## Continuity rows (what each episode establishes on air)

| Episode | Established on air |
|---|---|
| E025 The Father Who Stays (Tue Mar 30) | Matthew 3:17 at the Jordan, before Jesus has done anything public. Matthew 4:3, "If you are the Son of God," is the test that follows. Wes's sunrise bleachers cushion (the knee beat). Jonathon's Beaumont manager: the maroon duck tie and the "Not bad, kid" sticky note in his desk drawer. Wes's "good job on the cold open" receipt. "A heart is a heart," a disagreement left unsettled. "But I have a number," pushed back. "How you say it with no receipt." "Where a man learns to stay": Jonathon fears he's like his dad. Wes's mom: "Nobody's asked me that." Forgiving isn't trusting. Jonathon will decide about the friend request and text Wes at 7:15 ("Tonight at seven"). Book chapter 10 plug, present tense. |
| E026 Field Notes: Easter Week Report (Fri Apr 2) | The 7:15 "?" text and Wes's "K" at 8:06. Wes's brother call: an hour and four minutes, the recliner, neither brother had asked Mom. The wife's reason: the brother dug in over a cattle lease about twenty years ago. The youngest's no-sigh "Okay" on Thu Apr 1. "Three after tomorrow" for the truck Saturdays. Jonathon pushes back on "feelings are weather" and they land on "Say the feeling, don't make it the judge." The contractor prays in about six words. Mark 9:24 is the card, and Mark 9:28-29 is paraphrased. The tool is the Saturday morning walk, and Wes walks Saturday at six. |
| E027 The Empty Chair at Your Table (Tue Apr 6) | Jonathon tells the whole Saturday for the first time: the duffel, the cassettes, the rods, the lamp, the dent, the left turn. Mom never bought another lamp. Wes's shoes. Ephesians 6:4 is the card, and Colossians 3:21 and Ephesians 3:15 are paraphrased. "Why the detail": the toy box going out the door is the lamp coming out sideways. "The chair is not the last word." Mr. Abernathy appears. Wes walks with a heifer on his six o'clock prayer walk. "You should have made him pay": Jonathon disagrees and Wes keeps paying. The stepdad case and "you are the empty chair" ("Start with what it cost"). "How to tell one man." Wes has never told his kids about the shoes. The sister stays unasked. Bluebonnets 9-8. Car-care, nine cars. Book chapter 8 plug. |
| E028 Field Notes: The Chair Report (Fri Apr 9) | Wes told his oldest about the shoes: "I used to hand you the brush." The glove-box programs. "I wish I'd known that at fourteen." Shoe night is Saturday at seven. Jonathon apologized to Dani about the toy box ("I knew it wasn't about the dinosaurs"), and the box goes to church Saturday. Ruby's sentence and "Does he know about me?" "He saw your picture." Wes sides with Dani on "left" for a minute. Wes's youngest at seven: "Is he coming back?" "No, buddy." "Okay." "A heart was exactly the size of what she needed." Wes's own sentence: "Your grandpa worked hard, he stayed, and he loved us with his hands. He never learned to say it, and I'm trying to." Theo overheard. "Most kids give you two tries." "She believes the Tuesdays." "We don't talk that way in our house." Ephesians 4:29. The sister called back ("Take her to pick one out"). The nephew shared the episode to the parent chat. April's order is check, tool, question. |
| E029 When Your Dad Is Still Alive (Tue Apr 13) | Bluebonnets lost 6-5, "a combined three runs," Ruby's parade-float wave, "Great wave." Shoe night: steel-toe boots, "Okay. Boots," the brush handed the other direction, about forty words, half the sentence, "Did Grandpa ever tell you he was proud of you?" "Once. In a hospital bed." "Oh." Truck Saturday 10: the youngest washed the truck unasked, and Wes hid behind the curtain ("Shh"). The VP's Q2 email was a territory change, after four careful emails. Jonathon's ten Beaumont calls ("a restraining order"). The calls with his father: "Hey, bud," the weather, "Well. I'll let you go," the 2020 hurricane, "I've been the seventeen-year-old," and he has never once called. Exodus 20:12, with honor as weight, credited to Wes's pastor. Jonathon's push-back with his mom's house, unsettled ("sometimes the weather is just the weather"). The pot roast: eleven seconds, the kick, the apartments behind the church, Ola, "because he bought a chair," "I'm keeping the recliner," the visit in May. Wes's folder of brochures. "Why the weather": rapport with no order. Wes's dad: "Here's your mother." The Brenham man. The A&M scholarship. Jonathon's plan for Wed 7:30 in the truck, "Not yet," Dani's porch light. Wes will call his oldest and won't rehearse it. The breakfast bet. No plug. |
| E030 Field Notes: Calling Him Back (Fri Apr 16) | Nobody buys breakfast. The dentist voicemail practice. Nine minutes before dialing. "Who died?" "Nobody." The grandfather's name, kept on a receipt and off mic. Offshore two on, two off, and fishing every day home. "Ten words... about fish." The rods. No apology. "Not yet," his voice cracking. "She's the one in the flowers." "She looks like your mama." "Well. That's true." Twelve minutes, untimed. "Call me sometime, bud." "I just did." "Ha. You did." Jonathon came away mad. "He laughed." "Good." Wes to his oldest at lunch: "I'm proud of you." "For what?" "Not for anything. Just am." Then the wheel bearing. Fredericksburg for the wife's sister's fiftieth ("Not you"). Romans 12:18. Jonathon pushes back with Luke 17:3: debt versus relationship, and he takes "the debt part." "Not the same size." The tool is the two-call rule. At 2 AM: "He got rods, and I got the weather." Wes's same-sentence prayer. The mean-second-call case: "I'll call you another time." |
| E031 When Home Never Handed You Off (Tue Apr 20) | Bluebonnets lost 12-3, "throws like she's mad at the ball," "Your coach voice is sad." Truck Saturday 11, one left, and Wes likes the drive and the radio. The feed-store "Thank you, sir." Wes's driveway at eighteen: the Buick, "Drive careful," the laundry basket, "You're a man now... And don't come home every Friday." Jonathon calls it cold, and Wes calls it the warmest thing she ever did. Why Wes's dad never said it (nobody sent him; the scholarship). The tape measure for the china cabinet. Jonathon's list: man of the house, the pitching coach, "Not bad, kid," and Dani's dad's "Take care of her," which was another job. "I'd become the tie." Wes's list: his mom, then Mr. Abernathy at thirty-six. "Nobody's late." "What it sounds like": praise versus counting in. Jonathon won't fake his rep's "real one." Wes is lying awake about the truck paper. Luke 2:49 is the card, and verses 51-52 are paraphrased. Jacob, noticed once. The AC man and the dugout. "I only know how to be her guy." "Her guy is needed. Her son is loved." Jonathon's push-back, unsettled ("To her, the capacitor is a hard thing"). Wes's brother was Mom's guy. Training session 11 plug, present tense. The resentment case. The sock meltdown, then Ruby and the name at bedtime: "Can we go fishing?" "You could learn." The stock tank, not before June. "Maybe." The Pasadena "okay." Wes's one on-mic affirmation, unanswered. |
| E032 Field Notes: Cutting the String (Fri Apr 23) | Jonathon's mom handled the AC man herself: "I understood about half." "You can still come see me." Pasadena on Sunday with three questions, said out loud (the best thing since Easter, someone at church he doesn't know about, her birthday). Wes's brother: "She never said that to me. I never left. Nobody stands in the driveway for the one who stays." "It's not your fault, it's just how it went." Cattle prices. No lesson. Wes bought a twenty-five-foot tape measure. The nephew: "dont make it weird," "day thirty six btw," and Jonathon's "ok" after fifteen minutes and four drafts. Wes still has no sentence for the truck paper, and there will be donuts tomorrow. The rep (31, unnamed): 7:15 calls for nine years, "by seven-thirty-five," "younger," "not bad by seven-thirty-five." Wes's pay phone in 2000: "Next time, call me from the pay phone." Philippians 2:4. Jonathon pushes back for the mom, and they land on "gift and string, both." Dani has returned the Sunday calls for ten years. Wes's wife did his family's birthday cards. The tool is the Sunday call and the overnight muscle. "Her best friend's name is Pat." "Does Pat count?" |
