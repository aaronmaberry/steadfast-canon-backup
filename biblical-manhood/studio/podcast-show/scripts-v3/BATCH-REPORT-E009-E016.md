# Batch report: E009-E016 (podcast v3 rewrite)

Branch: `podcast-v3-e009-e016`. Prepared for Aaron Maberry. All eight episodes were rewritten from the v1 drafts in `scripts/` into `scripts-v3/`. No existing file was edited or deleted. Changes from v1 and the length overrides are logged in `scripts-v3/CHANGELOG-V3.md` under "Batch E009-E016."

## Status

All eight scripts are finished. Each passes `_build/lint.sh` with no FAIL and no WARN. Each was timed with `_build/timing.py`, and those times set the header length and the YouTube chapter timestamps. Every script got one listener reread, followed by a batch-wide check for repeated phrases (below).

| Episode | Format | Spoken words | Minutes (timing.py) | Wes / Jonathon words | Jonathon share | Jonathon lines under 12 words | Lint |
|---|---|---|---|---|---|---|---|
| E009 The Weight With Your Name on It | Main | 7,520 | 50:51 | 3,842 / 3,678 | 48.9% | 17.6% (27 of 153) | Pass, 0 FAIL, 0 WARN |
| E010 Field Notes: Not Your Load | Field Notes | 3,404 | 23:05 | 1,710 / 1,694 | 49.8% | 15.7% (11 of 70) | Pass, 0 FAIL, 0 WARN |
| E011 Somebody Has to Step Out Ahead | Main | 7,236 | 48:55 | 3,785 / 3,451 | 47.7% | 12.9% (18 of 140) | Pass, 0 FAIL, 0 WARN |
| E012 Field Notes: Valentine's, Ash Wednesday, and Going First | Field Notes | 3,252 | 22:05 | 1,679 / 1,573 | 48.4% | 9.7% (6 of 62) | Pass, 0 FAIL, 0 WARN |
| E013 The Prize That's Gone by Thursday | Main | 7,200 | 48:43 | 3,803 / 3,397 | 47.2% | 16.4% (22 of 134) | Pass, 0 FAIL, 0 WARN |
| E014 Field Notes: What Stuck | Field Notes | 3,439 | 23:20 | 1,736 / 1,703 | 49.5% | 13.4% (9 of 67) | Pass, 0 FAIL, 0 WARN |
| E015 The Part That's Mine | Main | 7,123 | 48:03 | 3,799 / 3,324 | 46.7% | 14.2% (17 of 120) | Pass, 0 FAIL, 0 WARN |
| E016 Field Notes: Inside Job | Field Notes | 3,338 | 22:34 | 1,733 / 1,605 | 48.1% | 11.3% (7 of 62) | Pass, 0 FAIL, 0 WARN |

Word counts cover spoken lines only. Stage directions, bracketed cues and parentheticals are excluded. The longest Wes turn in the batch is 86 words (E016), well under the 120-word limit.

**Lint budgets.** E011 has one mid-line ellipsis and every other episode has none. Long pauses sit at the maximum of 3 in E009, E013 and E015. Beats sit at the maximum of 10 in E011. Every other count is under its cap.

**Mic share and chemistry.** In every episode Jonathon has between 46% and 50% of the spoken words, and fewer than 20% of his lines are short. In each main he pushes back for real at least once and tells at least two of his own stories:

| Episode | Jonathon's push-back | Jonathon's stories |
|---|---|---|
| E009 | Wes paying for his son's dent was grace, "isn't that the gospel?" (left unsettled) | No will and the guardian question; his dad's car, in his dad's name; his mom's call to her sister; the divorced neighbor |
| E011 | Whether asking counts as going first ("asking is a weight"); he admits waiting months on his boss | The Sunday Feb 7 talk with Dani; the wrong-Saturday Valentine's at Whataburger; the contractor's cap on the chair |
| E013 | "This is for you" sounds like a sales trick; he wins the wording on not telling even your one man | The Monday leaderboard email; #1 in the country in fall 2023; Theo's croup; an hour on the rep's call list; laundry on Dani's pillow |
| E015 | His first pastor's "you've got a Father in heaven now" was a towel thrown at a man on fire; he won't ask the rep before telling the VP (left standing) | The 2019 district deal and the Monday lunch; Theo and the milk; the Cancun picture; his sister and the nickel |

The Field Notes keep a real disagreement too. In E010 Jonathon thinks they should ask Dani's parents before naming them guardians, and Dani decides not to. E014 pays that off at the signing without settling it. In E016 Jonathon tells Wes he was right about asking the rep, and Wes refuses the win.

## Brief rules checked in every script

- No dashes in spoken lines, descriptions or narratives.
- "This week" appears nowhere. The chapter is "The challenge."
- Every line aimed at the listener speaks to one man.
- Jonathon uses no country phrasing.
- Plugs are in present tense: E009 (book, chapter five) and E015 (training, "The Problem Inside"). The other six have no plug slot.
- The 988 line is in the two mental-health episodes. E009 has it in "The man who can't." In E016 it is spoken by Jonathon and also appears in the description and the pinned comment.
- Outros follow the rotation (D, F1, E, F2, A, F3, B, F4), and the locked credits disclosure is the last spoken line.

## Repeated phrases across the batch

A check for six-word phrases shared between episodes was run on the finished batch, and incidental repeats were varied. What remains is intentional:

- A main's challenge quoted in the Field Notes that checks it (E009 and E010, E011 and E012, E013 and E014).
- The canon phrase "the weight with your name on it."
- The standard 988 wording.
- Quoted callbacks: "Mom, tell the doctor what you told me," the seventy-thirty apology rule, and "the district deal should have been his."
- The fixed Field Notes opener, "Pull up a chair. It's Field Notes."
- The recurring "single check" with the nephew.

## Warnings not cleared

None from lint. Two notes for the edit:

- **Possible merge conflict on `scripts-v3/CHANGELOG-V3.md`.** Batch E025-E032 (`podcast-v3-e025-e032`) also creates this file, so merging both branches will hit an add/add conflict. Both files use the same layout with one "## Batch" section each, so the fix is to keep both sections.
- **The open's stage note** still reads "Same beats every week, new words," as in the v1 template. It is never spoken, and lint passes it. Batch E025-E032 changed it to "each episode." Match that if you want the batches identical.

## Continuity assumptions

- **E009.** Jonathon's mother was 31 with two kids when his dad left, which puts her at about 59 now. Dani's parents are 72 and 74. The son's twelve Saturdays at the brother's place end around E031, which sets up an April callback.
- **E010.** The signing is Feb 18, as in v1. Wes's oldest son is 21. Wes married in 2000, so 27 years of birthdays.
- **E011.** The Valentine's dinner is Saturday the 13th because Dani works Sunday night. Wes is on coffee for the car-care Saturday in March.
- **E012.** v1 timing is corrected (see the changelog). Wes corrects Jonathon on air: his mother is 78.
- **E013.** The grab bar went in on Saturday Feb 13, and Wes's text to his brother comes after it, not after the appointment (the brother was in the room in E012). Theo's croup (spring 2026, at 3) is carried from v1.
- **E014.** The signing was at 10 AM (v1 gave no time). The gutter is set for Saturday Feb 27 at 8 AM, per the host canon; E016 (Friday Feb 26) calls it "tomorrow," and the result belongs in E018. The car-care Saturday is March 6, reported in E020. The production notes carry the Friday review gate for Aaron.
- **E015.** The rookie from 2019 (now 31) is a different rep from the E007/E008 review and the E013 call list. Wes told his wife about the headache on Thursday Feb 18 and called his son on Sunday Feb 21. Jonathon had the Monday lunch on Feb 22, and the VP call is Thursday Feb 25. The calendar title is changed to "The Part That's Mine."
- **E016.** The rep's answer to "What do you want me to do?" comes in E018 or later and should be small. The hidden thing from E013 is never revealed.

## Continuity rows (what each episode established on air)

Full rows are in each script's "New continuity" header line. Summary:

**E009 The Weight With Your Name on It.** Wes has had a will since 2002. His wife did all of it, the guardian is her sister, and he found out at 50, read the nine pages, and asked her to walk him through it. Wes's dad had both knees replaced in his sixties and "was never the same." Dani runs the family money on a color-coded spreadsheet, and Jonathon didn't know the mortgage number, the payment day or the password. Ruby (7) makes her own bed now. Jonathon and Dani have no will after three years of "we should." Dani's parents live in New Braunfels and are 72 and 74. The guardian question (Jonathon's sister in Pasadena, or Dani's parents) is why they've avoided it. The church lawyer appointment is Thursday Feb 4 at 4:30. Wes's 16-year-old backed the truck into a post at the feed store in December. Wes paid for the dent and said "don't worry about it," and now the boy is working it off over twelve Saturdays at Wes's older brother's place. Wes drives his mother to PT on Tuesdays; she counts his reps and noticed his limp. His knee appointment is Feb 3. A 68-year-old man at Wes's table stopped paying his 34-year-old son's bills. Whether paying for the dent was grace is left unsettled.

**E010 Field Notes: Not Your Load.** Knee results: arthritis in both knees, the right one worse, no surgery. PT is twice a week at his mother's clinic, so on Tuesdays they go together. "It's not Dad," said in the truck. Wes sent his first emoji (a thumbs-up) at 4:01. Wes's wife has kept every birthday on his side for 27 years; the birthdays are in his phone now, and his little brother's is March 11. Wes's "not mine" is his oldest son's (21) job decision. The guardians are Dani's parents, with Jonathon's sister as backup, to revisit in five years. Dani tells her parents after the signing rather than asking first (her call). Signing Feb 18. The mortgage is paid on the third. Dani's answer: "Your mom. I'm the one who calls her back." Jonathon called his mom back himself. The nephew's emergency contact was his ex; it's now his roommate. His budget has one category, "food and stuff."

**E011 Somebody Has to Step Out Ahead.** After the fog years, Wes's first move back was making the 5:15 coffee; on day eleven his wife cried into it. In the Sunday Feb 7 talk, Jonathon went first ("I've been making you pay for my mom"). They're hosting Easter lunch and inviting his mom, and Jonathon calls her Thursday at 7. Wes apologized to his son for yelling about the rolling stop; at the cattle guard the son said, "Sorry about the stop sign." Mom told Wes what she wants: stay in her house, cleaning help every two weeks, the walker in the bathroom only, and driving herself to church. Wes plans to open the appointment with "Mom, tell the doctor what you told me." The 81-year-old Air Force mechanic is starting a car-care Saturday for single moms. Jonathon leaves the coffee made on Dani's shift mornings. Valentine's dinner is Saturday the 13th.

**E012 Field Notes: Valentine's, Ash Wednesday, and Going First.** The doctor agreed to most of Mom's plan, including a grab bar. The older brother said "We talked about this," then in the parking lot: "I never asked her either." Mom will cook a monthly Sunday pot roast lunch starting in March. Wes took his wife to Mr. Abernathy's diner (Thursday Feb 11): "The coffee's terrible," then "I get it now." Jonathon's mom: "Well, I'll bring the ham." She texted Dani, and Dani answered, "Yes. Bring the ham." Dani wrote back on the coffee note: "Decaf next time." Jonathon took Ruby and Theo to Ash Wednesday alone. Theo: "You have dirt on your face." Wes apologized to his brother for ambushing him. Jonathon led the supper prayer for the first time. The nephew's chili night for seven: he's buying bowls.

**E013 The Prize That's Gone by Thursday.** Jonathon moved the Monday 8 AM leaderboard email to 10 AM after eleven years of reading it first thing; the next Monday he was #6. In fall 2023 he was #1 in the country during the 1604 years and can't remember that fall with his kids. Wes's cheap prize is being "a rock" who prays in public. Mr. Abernathy's receipts held dates of prayer for each man; Wes's went back nine years. Wes keeps a private prayer list on his index card. His son-in-law prayed from the front for the first time. The contractor is teaching welding. Jonathon helped the rep with the call list ("Booked two"). Wes says "This is for you" in the truck. On Saturday Feb 13 Wes installed the grab bar and texted his brother before and after; the brother answered "Good." Whether telling your one man about hidden good work spoils it is left unsettled.

**E014 Field Notes: What Stuck.** Both men did the hidden thing and won't say what it was. Wes's wife: "Are you buying me a boat?" Dani: "Don't. You'll ruin it." Wes told his wife "I like being the rock"; she said, "You ask me in the truck how the prayer went." The will signing was Thursday Feb 18 at 10 AM, followed by tacos at 11 AM in the truck. Dani's mom said yes before Dani finished; her dad said, "You could've asked." What stuck for Jonathon: phone jail at supper (Ruby's masking-tape basket) and the decaf coffee. What didn't: ten minutes in the Bible, nine mornings. What stuck for Wes: asking before deciding, and Tuesday PT. What didn't: the gutter, now loose fifteen months, because of the ladder and his knees. The gutter date is Saturday Feb 27 at 8 AM. The Thursday "Did you do it?" texts have run since Jan 14. The nephew: "did it. not telling."

**E015 The Part That's Mine.** Ruby jailed her grandpa's phone at Dani's parents' house. In 2019 Jonathon took credit for a rookie's district deal (41 schools) and made President's Club; the trip was Cancun. At Monday lunch (Feb 22) he told the rep, now 31, "It was yours. I took it. I'm sorry." The rep: "You owe me Cancun." The VP call is set for Thursday Feb 25, and Jonathon won't ask the rep first. Dani about the Cancun picture: "That's my picture too." Jonathon's sister "would return a nickel." Dani's high-school Bible has "Me" written next to Romans 7. In December 2010 Wes skipped his son's kindergarten shepherd program by faking a headache; he told his wife Thursday Feb 18 ("I knew. I could hear the game"). The son doesn't remember it. Jonathon apologized to Theo about the milk. Wes's older brother is "the nickel."

**E016 Field Notes: Inside Job.** At the VP call, Jonathon read his sentence off a sticky note. The VP: "Let's keep this between us." The rep texted, "Now he's going to be weird with me." Jonathon answered, "What do you want me to do?" and hasn't heard back. Wes doesn't take the win. Jonathon apologized to Ruby for the shoes and the cereal; she asked if Jesus has a dog. Wes told his older brother, "I left Thanksgiving early. That was wrong." The brother: "Mom made a pecan pie for you. I ate it." The gutter is tomorrow, not done yet. Wes's oldest son told his foreman he wired a panel wrong; Wes texted back, "Proud of the first text." Jonathon found Psalm 139 at 2 AM himself. The examen: Jonathon on the drive home, Wes with the lights out.
