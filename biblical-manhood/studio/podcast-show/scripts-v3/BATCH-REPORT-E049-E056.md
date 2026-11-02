# Batch report: E049 to E056 (v3 rewrite)

Branch: `podcast-v3-e049-e056`. All eight episodes are rewritten from the first drafts in `scripts/` into `scripts-v3/`. No existing file was edited or deleted. Length overrides and the batch's rewordings are logged in `CHANGELOG-V3.md`.

## Per episode

Words are spoken words, counted from the WES and JONATHON lines. Minutes are from `_build/timing.py` (Wes about 145 wpm, Jonathon about 170). Lint is `_build/lint.sh`.

| Episode | Type | Words | Est. minutes | Wes / Jonathon (%) | Jonathon lines under 12 words | Lint |
|---|---|---|---|---|---|---|
| E049 give-your-son-a-hill | Main | 8,100 | 53:43 | 50.2 / 49.8 | 10.3% | 0 FAIL, 0 WARN |
| E050 field-notes-the-hill-report | Field Notes | 3,441 | 22:59 | 50.2 / 49.8 | 13.0% | 0 FAIL, 0 WARN |
| E051 a-day-he-will-not-forget | Main | 6,980 | 46:39 | 53.4 / 46.6 | 13.7% | 0 FAIL, 0 WARN |
| E052 field-notes-independence-day | Field Notes | 3,416 | 22:41 | 50.6 / 49.4 | 10.6% | 0 FAIL, 0 WARN |
| E053 before-anything-went-wrong | Main | 7,165 | 47:37 | 51.6 / 48.4 | 4.1% | 0 FAIL, 0 WARN |
| E054 field-notes-work-it-and-keep-it | Field Notes | 3,197 | 21:18 | 52.6 / 47.4 | 7.3% | 0 FAIL, 0 WARN |
| E055 some-saturdays | Main | 7,013 | 46:27 | 51.7 / 48.3 | 6.6% | 0 FAIL, 0 WARN |
| E056 field-notes-the-feeling-isnt-the-fire | Field Notes | 3,118 | 20:51 | 51.4 / 48.6 | 10.0% | 0 FAIL, 0 WARN |

Every main falls inside 45 to 60 minutes and every Field Notes inside 20 to 25. Jonathon is inside 35 to 50 percent on all eight. His lines under 12 words stay below 20 percent everywhere (the highest is E051 at 13.7 percent). No Wes run goes over 120 words without a Jonathon line. In every main, Jonathon pushes back for real once and tells at least two stories of his own. Lint and timing were run after every edit.

## Warnings not cleared

Lint prints no FAIL or WARN on any file. The items below are things Aaron may want to look at.

- **Edges of the windows.** E051 is 20 words under the brief's "about 7,000" for a main, but its 46:39 is inside the time window, so nothing was padded. E056 runs 20:51, close to the 20-minute floor. E049, E050 and E052 have Jonathon at 49.4 to 49.8 percent, inside the cap but near it.
- **Open lines differ from intros_data.py.** E052 and E053 read reworded open lines in the script ("holiday edition," "All season") because the frozen opens say "holiday weekend" and "Through Labor Day." intros_data.py is unchanged, so the two sources disagree until someone updates intros_data.py. See CHANGELOG-V3.
- **INFO line.** Lint prints its informational "eleven/twelve spoken" count on every file (0 to 2 per file). These are plain counts and ages, such as "about twelve," "eleven minutes in a parking lot" and "eleven lines," not the round 7 pattern.
- **Book material, flag for Aaron.** Book chapters 20 and 29 both carry a four-part "real man" definition sentence from a banned source. It is never used on mic, in a description or in a reading narrative here, but the book itself still has it.

## Cross-batch repeats left on purpose

The listener reread checked six-word phrases across all eight files, and the tics it found were reworded (for example "as far as I can tell," "I'll take the divorced dad," "here's the part I don't love," "he said I could bring it here"). The repeats that remain are deliberate:

- The safety lines (988, "the kind of dark that scares you," the National Domestic Violence Hotline) are word for word wherever they air.
- The locked credits line, the "This is Walk Steadfast" anchor, the "From the table" and "Check the box" segment openers, and the "Married guys, on a calm night" challenge shape.
- Field Notes restate the previous Tuesday's challenge in its own words ("put a date on a page for your son's day," "name one place you were given to work and keep," "name one thing God's already put in front of you that you've been waiting to feel like doing").
- Quoted callbacks of earlier on-air lines: "You didn't do one for me," "the man who picked up Theo's screws," the compressor driven out at midnight, "the storm door one at a time," Ruby's card "still on the counter half done," the grocery-pad name.

## Continuity assumptions

- **Dates.** Release dates are v1's, from Tue Jun 22, 2027 (E049) to Fri Jul 16 (E056). Saturdays named in the headers (the ramp and cedar Saturday two on Jun 26, the barn on Sat Jul 3) are v1's too. No date is said in an open or a slate.
- **Wes.** Fifty-two. His job is never named on air. Mr. Abernathy (the lineman) is dead, and the Thursday table Wes sits at now is a different table. Wes and his wife still don't pray out loud together (held to about E083). The youngest's day at the barn is "a Saturday in October after the first cold front," which matches the SHOW-BIBLE payoff (Sat Oct 30, reported in E088).
- **Jonathon.** Started in sales at twenty-three under Lorraine on Pasadena refinery accounts. His father's "You too, bud" (E049) is unanswered through E056. Pancake hasn't arrived ("We don't have a dog yet"). His nephew is twenty-two and past a hundred days.
- **New names.** Lorraine (Jonathon's first sales manager) and Virgil (77, the screw man, from v1 E055) are checked against the lint list and the host files. The Hendersons are Jonathon's neighbors (HOA).
- **Two-chairs moments.** Both allowed in E049-E056 are used in E049 and E050. The pushbacks in E051, E053 and E055 resolve within two minutes and aren't two-chairs moments.
- **The man in the truck** (E053 on). No reason is given and he isn't a rescue. His story stays unknown at least through E058.
- **Hand-off to E057.** E056 saves 1 Corinthians 7:17 for E057 and leaves open the attic ceiling, Virgil's answer about Ruby, the truck, and Jonathon's second Wednesday text. The E057-E064 branch already covers Virgil's answer and the attic (E058), and nothing here contradicts it.

## Continuity rows (what each episode established on air)

### E049 give-your-son-a-hill
Everything in the v1 row stands. That includes "You too, bud." at 1:04 PM, unanswered, and Dani's "Well. There's your bud." The 24-year-old's "They're missing a guy" stands, along with the cedar, the chainsaw disagreement with Wes's wife and its compromise, and the youngest's "Can we come back next Saturday?" Theo's shoes, "Be there, and don't take over," and Jonathon's yes to the widows' repair crew also stand.

New in v3:
- **The HOA lattice.** The HOA wrote Jonathon in May about trash cans visible from the street. He built a lattice screen from a video. A second letter says "the structure appears to be leaning," and it leans toward the Hendersons'.
- **The iced coffee.** Jonathon brings Wes a late Father's Day iced coffee. Wes calls cold coffee "something that happened to the coffee," then drinks most of it.
- **The garbage disposal.** At ten, Jonathon went into a jammed disposal with a butter knife, the switch still up. His mom turned it off, said nothing, and cried at the sink later. Nobody had shown him the reset button.
- **Lorraine.** His first sales manager rode in his passenger seat for a month and never took over a call. In the car she asked "What would you do different?"
- **"Bud."** It is the word his dad used for him as a boy, and the one he uses with Theo.

### E050 field-notes-the-hill-report
Theo's shoes, round two:
- Monday: "You do it." "I don't WANT to." Six minutes of crying, and a shoe thrown at the neighbor's visiting dog that missed. Jonathon took over at minute six.
- By Thursday, Theo did them himself.

Jonathon told Dani his hill is "I don't know yet."

Wes read his card on the porch. His wife said "That's your card" and went back to her book. Jonathon names what Wes wanted ("a review"), and Wes concedes he wanted applause.

The chain: Wednesday night, the shop vise, a phone on a coffee can, the man in Oregon. "Night." "Night." "That's his now." Wes saw the boy filing toward himself on two teeth and said nothing. The boy caught it on the third tooth.

The video-game question: a forty-one-year-old dad asked what to do about his 14-year-old, who only wants video games. It ended unresolved on the closet.

New in v3:
- The lattice now leans on a brick.
- Wes brings his own steel thermos "in case."
- Jonathon's Monday nine o'clock moves to nine-thirty, "a standing thing at home."
- Jonathon kept a spiral notebook of his game stats at ten and threw it away at thirteen.
- His mom's boyfriend, around then, took the friend's house away as "too much."

### E051 a-day-he-will-not-forget
The ramp, Saturday Jun 26:
- Six men, and Ruby's pink tape measure. One board really was cut to her number by accident and fit ("Well, look at that.").
- Theo dropped a can of screws, and an older crew man knelt and handed them back one at a time.
- The widow, 84, went down the ramp to an empty mailbox, laughing.
- Theo prayed "And help the lady get her mail."

The barn ask: "Dad never did one of those for us." "One true thing." "I've only got about one." "I'll be there." The loppers are kept in the tack room. Wes doesn't ask what the one sentence is.

Wes's wife: "I want to hear what you're going to say to him. Before. Not to fix it." The oldest: "You didn't do one for me." He'll come, for his brother.

Jonathon pushes back on Wes's "That's the right reason": "I think that's you being noble so you don't have to feel it." Wes: "Maybe."

New in v3:
- **The Patriotic Porch contest.** The HOA flyer says the lattice "is not festive," so Jonathon taped a small flag to it.
- **Wes at seventeen.** His dad handed him the truck keys for his first solo feed run and said "Don't wreck it." Wes still can't decide whether that was a day.
- **The plan.** The youngest's day is a Saturday in October at the barn at six, after feeding. "Theo's morning" is a calendar entry eight years out, with one name.

### E052 field-notes-independence-day
Wes prayed out loud alone on the porch Tuesday night, and the neighbor's light went on and off. He says plainly that he still can't pray out loud with his wife. Reading his card, his wife said "Say it slower. You rush the end." On v3's reading, the end is where he says what the boy is for, and saying it means he can be wrong.

Jonathon's second question to his father-in-law, on the New Braunfels back porch: "I'll be eighty-two." "Yes, sir." "Well, put it on my calendar too." After the two-second handshake, Jonathon sat in the car with the engine off, and Ruby asked why they weren't going.

The nephew (twenty-two, past a hundred days) asked what freedom means for a Christian. He told Jonathon earlier that the hardest part is "the empty hours." Jonathon prayed in the truck after work, starting three times.

Season look-back:
- Wes: "proud," spent on both boys.
- Jonathon: "I'm not the only one who didn't get it."
- Wes: "I've been on the scoreboard too, it's just quieter."

The porch flag has faded pink, and judging is Sunday.

### E053 before-anything-went-wrong
Jonathon's VP turned "every rep takes all their vacation days" into a dashboard column ("Love it. Leading from the front."), which Wes calls "He made rest a leaderboard." Jonathon said "Thanks" on the call, unmuted. Jonathon's stories are the midnight compressor ("Did you bill it as an emergency order?") and the Pasadena machine shop at twenty-three. In the shop story, Lorraine read his oversold order in the car: "He doesn't need that. Call him back." Then: "We'll sell him the next one."

At the barn, Wes asked his brother whether their dad liked the work: "I don't know. He never said." Wes remembers his dad's hand on the corner post on Sunday afternoons, left unresolved.

Jonathon pushes back on "He was placed" with a church lady's line to his mom, "God's got you right where He wants you." He was nine and heard it. Wes concedes "placed" isn't "stuck."

Mr. Abernathy, the lineman, asked "What did you keep?" (Wes's first answer was fixing a new man's wrong order on a car hood.)

The porch contest: the Hendersons won with pool-noodle bunting, and a card in Jonathon's storm door read "Thank you for participating. The committee noticed the brick."

New threads:
- The man in the truck eats lunch alone in his running truck, and Jonathon warns Wes not to fix him.
- Jonathon puts his phone in Dani's glove box.
- Callers include a stay-at-home dad (31) and a farm kid (19) who wants to be an electrician.

### E054 field-notes-work-it-and-keep-it
The truck man: two inches of window and "You need something?" Then "Door's open." They talked about the Rangers ("bad this year") for twenty-five minutes. Wednesday the door was unlocked: "You don't have to do this." "I know. It's air-conditioned." The man's cooler moved from the passenger floorboard to the back seat for Wes. Wes's wife wrote the man's name on the grocery pad on the fridge "so you'll remember to ask about his kids." Wes still hasn't asked.

The youngest heard Wes say he likes his job ("Okay?") and asked for the rest of the potatoes.

At work:
- Jonathon's rep (31) said "I didn't do it for the margin, boss." "I know. I did."
- Jonathon forwarded the "South Central leading on rest" bar chart to Dani.
- At twenty-six, Jonathon took one vacation day in a year and spent it on his laptop in a Corpus hotel lobby.
- His shutdown is "Okay, Lord, it's Yours" and the console lid.

Wes said "That's enough for today" at the dresser and felt "like a man reading a fortune cookie to his socks."

### E055 some-saturdays
VBS: Ruby asked "Daddy, are you on fire for Jesus?" "Some days." "Which days?" "Eat your chicken." Dani: "Mine's some days too." Wes at nine won a VBS sword drill with a dog-eared page, and his mother made him give the ribbon back.

Wes's fire decade broke in the truck with his wife at about forty-five. "Where are we going?" "Home." "No. You and me. Our family." Then "I can do Saturday." The committees took two years to quit.

Jonathon's flat year came about a year after faith, noticed at bath time with Ruby at about eight months. The breakfast man kept asking "You coming Thursday?"

Jonathon pushes back: "you're making the feeling sound dangerous." Wes: "I'm overcorrecting from my own burn." Wes's wife has never said she feels it in church.

At the barn at 6:02, the brother poured Wes's cup from his thermos, and it had gone cold. Virgil (77, white Ford, a pencil notebook with first names and crosses in the margin) has fixed widows' porches since his wife died in '98: "Some Saturdays."

A caller on depression medication is told not to stop because of a feeling in church, and to talk to his doctor (988 line aired). Wes goes for seven of seven on the porch prayer, and Jonathon will send the Wednesday text.

### E056 field-notes-the-feeling-isnt-the-fire
Wes prayed five of seven nights. One miss was the recliner at 9:15, boots on, with his wife's blanket, waking at 1 AM. The other was lightning ("I could have prayed in the kitchen"). His prayer: "Lord, I'm tired. Thank You for the water." Jonathon guessed four and Dani six. Wes hasn't asked his wife the Sunday question.

Asked what he's been waiting to feel like doing, Wes's wife said "The guest room ceiling," then turned the page. Jonathon offered to help with the attic, and Wes is going alone.

The truck man: "Dentist." "Do you have kids?" "Three." Wes didn't answer back ("I want him to have asked one for free").

Jonathon's Wednesday text got "maybe," and the man didn't come. Jonathon told Ruby about Virgil at bedtime. She asked "Can I go?" to join the crew. He said seven's too young for a nail gun, and she said "I don't want the nail gun. I want to hand him the screws." Jonathon will ask Virgil Saturday. Jonathon's list card goes on his truck visor, next to Dani's yellow sticky note from back in May.

The crop-insurance man (41) has sat at kitchen tables after hail since twenty-two. He says "That's just my job" and keeps a folding chair in his trunk. Wes remembers the co-op man at the Hart kitchen table after hail when he was about fourteen.

## Unfinished

Nothing. All eight episodes are written, lint clean, timed, and reread.
