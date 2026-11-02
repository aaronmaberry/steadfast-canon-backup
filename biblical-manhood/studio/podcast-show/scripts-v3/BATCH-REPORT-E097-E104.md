# Batch report: E097-E104 (podcast v3, new scripts)

Branch: `cursor/podcast-v3-e097-e104-b614`. The prompt asked for `podcast-v3-e097-e104`, but the agent system requires a `cursor/` prefix and a `-b614` suffix on new branches, so it's the same work under a longer name. Prepared for Aaron Maberry.

These eight episodes had no v1 scripts. Each was written new from these sources:

- its row in `CALENDAR-104.md`;
- SHOW-BIBLE section 15, for what's true by the end of the year;
- the host files;
- the E073-E080 v3 drafts and the v1 continuity rows, for the threads running in.

No existing file was edited or deleted. The new files are the eight scripts, `scripts-v3/CHANGELOG-V3.md` and this report. Length overrides and changed open lines are logged in the changelog.

## Status

All eight scripts are finished. Each was checked with `_build/lint.sh` and timed with `_build/timing.py`, and `_build/apply_chapters.py` set the YouTube chapter timestamps. Every script got a listener reread, and the batch got a check for repeated phrases (below).

| Episode | Format | Spoken words | Minutes (timing.py) | Wes / Jonathon words | Jonathon share | Jonathon lines under 12 words | Longest Wes turn | Lint |
|---|---|---|---|---|---|---|---|---|
| E097 Waiting on God Isn't Sitting Still | Main | 7,079 | 46:47 | 3,664 / 3,415 | 48.2% | 14.1% (12 of 85) | 106 | Pass, 0 FAIL, 1 WARN (draft open) |
| E098 Field Notes: The Wait Report | Field Notes | 3,285 | 21:46 | 1,673 / 1,612 | 49.1% | 15.0% (6 of 40) | 118 | Pass, 0 FAIL, 1 WARN (draft open) |
| E099 The Shepherds Went Back to Work | Main | 7,008 | 46:19 | 3,703 / 3,305 | 47.2% | 8.9% (7 of 79) | 119 | Pass, 0 FAIL, 1 WARN (draft open) |
| E100 Field Notes: Back to Work | Field Notes | 3,090 | 20:32 | 1,657 / 1,433 | 46.4% | 11.1% (4 of 36) | 110 | Pass, 0 FAIL, 1 WARN (draft open) |
| E101 Simeon Kept Showing Up | Main | 6,975 | 46:27 | 3,879 / 3,096 | 44.4% | 8.1% (7 of 86) | 112 | Pass, 0 FAIL, 1 WARN (draft open) |
| E102 Field Notes: Christmas Eve | Field Notes | 3,187 | 21:08 | 1,604 / 1,583 | 49.7% | 9.8% (4 of 41) | 107 | Pass, 0 FAIL, 1 WARN (draft open) |
| E103 Write the Next Move | Main | 6,999 | 46:29 | 3,750 / 3,249 | 46.4% | 8.0% (7 of 88) | 115 | Pass, 0 FAIL, 1 WARN (draft open) |
| E104 Field Notes: New Year's Eve | Field Notes | 3,097 | 20:41 | 1,638 / 1,459 | 47.1% | 7.0% (3 of 43) | 116 | Pass, 0 FAIL, 1 WARN (draft open) |

Word counts cover spoken lines only. Stage directions, bracketed cues and parentheticals are excluded.

Every main runs about 46 to 47 minutes and every Field Notes about 20.5 to 22 minutes, inside the v3 brief's ranges. Mains are at the low end, so there's room to grow if you want them longer.

No Wes turn runs over 120 words. There are no em or en dashes, no mid-sentence colons, no spoken "eleven" or "twelve", and "week" is never used for a training session.

The open check passes. `_build/intro_lint.py` was run on a /tmp copy of `_build`, with the proposed intros_data lines patched in and the retell check pointed at `scripts-v3`. It gave 0 fails and 0 warns.

**Mic share and chemistry.** In every episode Jonathon has between 44% and 50% of spoken words, and under 16% of his lines are short. E101 is the lowest at 44.4%, because Wes carries the nursing home and the Wednesday night. In each main Jonathon pushes back for real and tells at least two of his own stories:

| Episode | Jonathon's push-back (left unsettled) | Jonathon's stories |
|---|---|---|
| E097 | Exodus 14:14 against 14:15. Some men need to be still, not move. Wes concedes the case, but they don't settle whether a man in it can tell which verse he's in. He also says Wes's printout rule was a way to avoid a talk, and Wes grants half. | Ruby's birth and the nurse's "Hold the cup." His first December as a manager ("December's a wash") and the rep who didn't coast |
| E099 | The warranty counter. Some men need to leave the field, not go back to it. Wes concedes dishonest work and "leave forward." They don't settle how long to give a crushing job. | The men's conference and the sippy cup. Theo the shepherd in a dish towel. Virgil's December crew with Ruby |
| E101 | The Sunday-text father. When is it okay to stop? It stays open between them. | His mom on the video call at ten every Saturday since May. His Day One confession. The Houston mailroom man ("Go by her desk today.") |
| E103 | Every good thing in his life came from a plan he didn't make. Ends with "You think most men need a pen. I think most men need to be told the pen isn't God." | The receipt on the fridge. The names he learned this year, and Virgil's notebook with his name under "rail" |

In the Field Notes, E098 has Jonathon push on Habakkuk 2:3 ("it isn't a promise about a judge"), and Wes narrows what the verse promises. E100, E102 and E104 are check-and-report episodes. Their friction comes from the misses, told first: Wes's forty-minute miss, Jonathon walking home with the cookie tin, and Jonathon showing his card two days late.

## Warnings I could not clear (decisions for Aaron)

1. **The DRAFT-open WARN on all eight.** Lint gives one WARN per script: "open is a DRAFT pending Aaron (SHOW-BIBLE section 5)." This is the open system working as intended. All eight opens are still marked DRAFT in `_build/intros_data.py`, and only you can lock them. Nothing in the scripts can clear it.

2. **Four open lines differ from `_build/intros_data.py`.** I didn't touch intros_data. These are the proposed replacement lines:

| Episode | Proposed intros_data line | Why |
|---|---|---|
| E097 | W "Following Jesus as a man, two Sundays into Advent. walksteadfast.com has my book and the video training." | "Advent week two" is a banned "week N" form |
| E098 | W "I'm Wes Hart. I feed cattle with my brother most Saturdays now." | The current fact (a printout waiting in his Bible since August) goes stale on air in E097, when he hands it to his wife |
| E099 | W "Following Jesus as a man, deep in Advent. The video training and my book, Steadfast Men, are at walksteadfast.com." | "Advent week three" is a banned "week N" form |
| E101 | W "Following Jesus as a man, in the last days before Christmas. My book and the video training are both at walksteadfast.com." | The brief bans "week" phrasing |

E100, E102, E103 and E104 use the open as written.

3. **New details about Wes's own life.** Wes Hart is your pen-name host, and these scripts add personal details for him. As far as I can tell none of them contradicts canon, but please strike any that misrepresent you. The main ones:
   - **E097:** years of praying "Lord, fix it with my brother" without driving out, and the feed-store ride where he hands his wife the printout.
   - **E098:** the drive-through with the youngest ("Even if it's welding?").
   - **E099:** he likes the problem nobody wants, and for twenty years he thought of work as what paid for Saturday.
   - **E101:** gardening gloves for his wife every Christmas since about 2001, and quitting Wednesday nights in 2010. His mother's unanswered Sunday calls in the fog years ("Well, hey."). He goes to prayer meeting with her.
   - **E102:** his first Christmas Eve as a dad, finishing the speech to a candle, and the first Christmas feeding with his brother.
   - **E103:** his daughter (25) gets a call only when her mother tells him to. Praying out loud with his wife since November.
   - **E104:** his daughter's text and the forty-minute call, the card for Thu Jan 13, and the long text to Jonathon.

4. **Details about Wes's wife.** None of these are quoted at length:
   - **E097:** three lines about the printout ("You've had this since August?").
   - **E098:** one permitted sentence ("She called the admissions office Wednesday. That's all I'm allowed to say.") and "Who told you to tell me first?"
   - **E101:** the okra and tomatoes ("Because it's March.").
   - **E104:** she reads the last page of a book first, and her move for him: "Call your daughter."

   E097 and E098 leave her degree open, with no outcome reported.

5. **Mr. Abernathy.** Canon has him dying in 2022 at 88, and the white mug on the set is his. E097 has a diner breakfast with him around 2019, after Wes's dad died. There he asks, "If He answered you tomorrow, what would you do Saturday?" Then he eats his toast and says nothing more. E103 remembers their last breakfast as ordinary (the price of toast, a ride to the eye doctor). He's never present after 2022 and never brings the moral.

6. **988.** 988 is in E097, E098, E100, E102, E103 and E104, wherever a man in the episode might be in a dark place:
   - a man who regrets the wait;
   - the custody father;
   - a heavy December;
   - the man alone on Christmas Eve;
   - the man whose year was a disaster;
   - the man alone on New Year's Eve.

   E099 and E101 have none, because nothing in them touches mental health.

7. **CHANGELOG merge.** This branch creates `scripts-v3/CHANGELOG-V3.md`, and other v3 batch branches do too, including `podcast-v3-e073-e080`. Merging them will conflict on that file. Keep every batch section.

8. **E081-E096 aren't on the remote.** No v3 branch for E081-E096 existed when I wrote this batch, so threads running into E097 were assumed from the calendar, SHOW-BIBLE section 15 and the E073-E080 drafts. If that batch lands with different facts, check the assumptions below first.

## Continuity assumptions

These are marked in each script's production notes, which are the source for this list.

- **Across the batch:**
  - E081-E096 aired as the calendar plans.
  - Wes's Saturday feedings with his brother (from 6:02 in E055) are routine by December.
  - The man in the truck still eats in his cab on Wednesdays.
  - Pancake (the Rivers dog) is "she."
  - The Rivers nativity stays up till Jan 6.
- **E097:** Theo's Advent calendar. Jonathon's hedge lights. Mr. Abernathy's question about 2019 (see warning 5). The nurse's "Hold the cup." Jonathon's first December as a manager. The feed-store ride Sat Dec 4.
- **E098:**
  - Jonathon asks Dani twice, and her schedule answer (no Saturday night shifts) is reported, not quoted.
  - The admissions-office sentence.
  - The youngest's "Cool."
  - The nephew's call to his grandmother.
  - The custody father at the Thursday table.
  - New small canon: Dani's grandmother's shoebox of dated prayer cards, with one on the fridge (her mother's name, 1971 and 1979).
- **E099:** Jonathon's men's conference in his second year of faith. Jonathon's company party on Fri Dec 17. Theo's pre-K program on Thu Dec 9. Virgil's December crew on Sat Dec 11, and the January ride to the hardware store. Book plug B, chapter 30 (SHOW-BIBLE section 14, item 17).
- **E100:**
  - Shane's question in his garage, with his first name.
  - The friend's last treatment of the year and a January scan, one line.
  - The sixty-one-year-old rep's line.
  - The oldest son's "foreman said amen."
- **E101:**
  - The December quartet on Thu Dec 9.
  - The gloves since 2001.
  - The woman in the pink cardigan.
  - Jonathon's mom's water-heater Saturday.
  - Ruby's sky in a frame.
  - Wes quitting Wednesday nights in 2010.
  - His mother's Sunday calls.
  - The okra and tomatoes.
  - The truck man's wife, left open.
  - The Houston mailroom man.
  - The neighbor's gray hair and grown kids.
- **E102:**
  - Dani traded for Christmas Eve off in October, and sang her solo lines in "O Holy Night" on Sun Dec 19.
  - Lyle.
  - Wes's father's Quirinius stumble.
  - The nephew's pickup game and Pastor Jim.
  - Doug's name, dog and garage door.
  - The stepfather at the Thursday table.
  - Christmas Eve supper at Wes's mother's.
- **E103:**
  - Christmas and the receipts:
    - The tamales.
    - The headphones for Dani.
    - The line through "the room" after Ruby's first coach-pitch game.
    - Dani putting the receipt on the fridge in March.
    - Wes keeping Mr. Abernathy's receipt in his Bible.
  - Wes's life since January:
    - The fan still clicks.
    - The last breakfast with Mr. Abernathy.
    - Wes's daughter only gets calls when her mother says.
    - Wes doesn't know the truck man's name.
  - The ledger and the next moves:
    - The ledger choices (one stuck and one missed per mark per man, listed in E103's production notes).
    - Theo's "Daddy says my name now."
    - The next moves and their dates.
  - The brother:
    - His "Okay." at the fence.
    - It was his idea for the youngest to come in October.
  - The sixty-eight-year-old at the diner.
- **E104:**
  - Leon's name and his delivery route.
  - Wes's wife reading the last page first (expanded from the open's fact).
  - The daughter's text and the forty-minute call.
  - The youngest's "Are there cookies?"
  - The oldest's license.
  - Dani's back step in February.
  - Jonathon's mother's question and her permission.
  - The sentences "Ask the name" and "Sit on the step."

**Other continuity rules followed:**

- **Dani** is quoted in E099, E102 and E104, two lines each at most. She is reported, not quoted, in E097, E098, E100, E101 and E103, so she's never quoted in back-to-back episodes.
- **Plugs** are present tense, with no dates and no prices:
  - E099 has book chapter 30.
  - E103 carries both plugs under the year-review exception: book chapter 34, Write the Next Move, and training session one, A Quiet Tuesday.
  - E097 and E101 have none, and Field Notes have none.
- **Scripture** is NIV and quoted exactly on cards:

  | Episode | Cards |
  |---|---|
  | E097 | Psalm 27:14, and Exodus 14:14 and 14:15 |
  | E098 | Habakkuk 2:3 |
  | E099 | Luke 2:20, and Colossians 3:23-24 |
  | E100 | Luke 2:19 |
  | E101 | Luke 2:25, 2:26 and 2:37 |
  | E102 | Luke 2:11 |
  | E103 | Proverbs 16:9 |
  | E104 | Revelation 21:5 |

  Verses with colons, and longer passages, are paraphrased in the hosts' own words and never presented as quotes.
- **Simeon** is never called old (SHOW-BIBLE section 14, item 20). Anna's eighty-four is Luke's.
- **Field Notes** each check the previous Tuesday's challenge, misses first.
- **The season lands.**
  - E103 reads back the E003 sentences and runs the ledger by the four marks. "Since January" is used only in E103 and E104.
  - E104 ends on the first challenge of 2028, not on the review: before Tuesday, do the first ten minutes of the thing you already know is yours.

## Listener reread

Each script was reread once as a listener. Then every six-word phrase in the spoken lines was compared across all eight scripts. That pass caught generic phrases repeated across episodes, such as "I want to tell you about," "these are questions I've heard at," "I think a lot of men," "better off gone" and "keep it where you'll see it." The later uses were reworded, along with an earlier fix to "Took you long enough," which is E079's line.

The repeats that remain are intentional:

- the locked opens, the slates, the plug wording and the credits line;
- each Field Notes check quoting the previous Tuesday's challenge and go-firsts. Examples are E097's "If He answered tomorrow, what would you do the morning after?", E099's Monday thanks and E101's "show up once at the one place you quit";
- setups paid off in the next episode. Examples are Ola's "Well, look who it is" (E101's fear, E102's toll), "the best part of my Christmas" (planned in E102, said at the fence in E103), the Jan 13 and Jan 3 next moves (set in E103, checked in E104) and "she told me where to park";
- the E003 sentences read back ("Pay the bills and don't make trouble").

**Keeping the last ten minutes alive:**

| Episode | What happens in the last ten minutes |
|---|---|
| E097 | The printout handed over on the feed-store ride with no bow, then the go-firsts (the youngest, "either way"; Jonathon finally asking Dani) |
| E099 | Four questions from the table, then Wes walking over for the problem nobody wants and Jonathon dropping the leaderboard |
| E101 | The questions, then Wes agreeing to prayer meeting ("Well, look who it is" as the price of the ticket) and Jonathon's cookie tin for the neighbor |
| E103 | The hard-year questions, then each man's next move with a day on it and the Thursday "Did you do it?" text |

## Continuity rows (what each episode establishes on air)

The full text is in each script's "New continuity" header row.

| Episode | Established on air |
|---|---|
| E097 Waiting on God Isn't Sitting Still (Tue Dec 7) | Theo opened all twenty-four Advent doors on Dec 1 ("I'm getting ready."); Dani taped them shut. Jonathon's hedge lights, half out. For years after his dad died, Wes prayed "Lord, fix it with my brother" without driving out. About 2019 at the diner, Mr. Abernathy asked, "If He answered you tomorrow, what would you do Saturday?" and ate his toast. The 6:02 Saturdays started this summer. At Ruby's birth a nurse handed Jonathon ice chips: "Dads either pace or scroll. Hold the cup." Jonathon's first December as a manager ("December's a wash") and the rep who closed her best month. The printout: on the feed-store ride Sat Dec 4, Wes handed his wife the printout. "You've had this since August?" "That's a dumb rule." It went in her purse and she turned up the radio. Pushback on the printout rule, half granted. Go-firsts: Wes tells the youngest he's for him either way; Jonathon asks Dani what schedule she'd want. Psalm 27:14; Exodus 14:14-15. 988. No plug. |
| E098 Field Notes: The Wait Report (Fri Dec 10) | Jonathon asked Dani wrong first (the driveway, forty seconds, her keys), then right at Thursday breakfast. She'd keep nights but wants no Saturday nights, so she isn't singing Sunday on no sleep. He'd prayed the wrong prayer for two years. Wes told his wife first: "Who told you to tell me first?" "Jonathon." "Huh." "Tell him I said either way too." The drive-through with the youngest: "Even if it's welding?" "Even if." "Cool." His wife called the admissions office Wednesday; that's all Wes may say. The nephew: "did the first piece. not telling," then he called Grandma for an hour. The custody father's sentence on a receipt. Wes's dated sentence sits in his Bible where the printout was. Dani's grandmother's dated prayer cards. Habakkuk 2:3. 988. |
| E099 The Shepherds Went Back to Work (Tue Dec 14) | Jonathon's men's conference, and the sippy cup by Tuesday. "Stand by the queso" for his party Fri Dec 17. Theo was a shepherd on Thu Dec 9 and wore the dish towel to H-E-B and to bed ("I'm still a shepherd."). Dani: "The angels came to the night shift first." Wes likes the problem nobody wants, and for twenty years he thought work only paid for Saturday. Virgil's December crew on Sat Dec 11 (a widow's porch rail, Ruby on the screws): "They went up again." He has asked Jonathon for a January ride to the hardware store. The warranty pushback stays unsettled. Go-firsts: Wes takes the ugly problem Monday; Jonathon drops the leaderboard and thanks each rep. Luke 2:20; Colossians 3:23-24. Book chapter 30 plug, present tense. |
| E100 Field Notes: Back to Work (Fri Dec 17) | Wes's forty-minute miss, then the truck at about ten. "I'll take that one." "It's a mess." "That's why." Jonathon thanked God for the younger tech who almost quit. The meeting with no board: one rep blamed allergies; the sixty-one-year-old said nobody had done that in thirty years; "So are we doing the numbers or not?" The numbers went out by email. Wes's oldest: "thanked Him for the foreman. out loud... foreman said amen." The friend's last treatment of the year, and a January scan. Shane's question in his garage; the Texas still unfinished. Episode one hundred noted once. Luke 2:19. 988. |
| E101 Simeon Kept Showing Up (Tue Dec 21) | Wes's wife gets gardening gloves every Christmas; Jonathon hasn't shopped yet. Merle's quartet on Thu Dec 9: the young man on lead, his grandmother mouthing every word, the woman in the pink cardigan. Wes stayed for the cookies. Merle: "Nobody's tuned it since Reagan." and "Come in January. He looks for you in the back." Jonathon's mom has been on Ruby's Saturday call at ten since May, water heater and all. Jonathon's Day One confession. The Sunday-text father ("When is it okay to stop?") stays unsettled. The okra ("That's what three days does.") and the replanted tomatoes ("Because it's March."). The truck man: "My wife used to make this with pecans." Wes's mother's "Well, hey." Go-firsts: Wes goes with his mother to Wednesday prayer meeting; Jonathon takes Ruby's cookies to the neighbor three doors down. Luke 2:25-26, 2:37. No plug. |
| E102 Field Notes: Christmas Eve (Fri Dec 24) | Jonathon's miss Monday, and Ruby: "Why do you still have the cookies?" Wednesday he knocked. Doug ("Nothing about him starts with an R.") didn't remember the lunch; they watched the fourth quarter; he asked about a garage door opener. Prayer meeting on Wed Dec 22: Wes's mother took his arm ("I don't need it. I want them to see."). Ola: "Well, look who it is." "Yes, ma'am." Lyle, 84, a retired rural mail carrier: "Your mother's had you on that list a long time. Don't make her take you off." Then he asked about the posthole digger. Dani's two lines on "O Holy Night." Pancake ate the bottom row of candy canes. Jonathon bought Dani's present (not named). The nephew is back at the Tuesday pickup game. Christmas morning: the first feeding with the brother since Dad died ("You coming Christmas?"). Wes's first Christmas Eve as a dad, the speech finished to a candle. Luke 2:11. 988. |
| E103 Write the Next Move (Tue Dec 28) | Christmas: the feeding at six, the gloves, Dani's headphones. Jonathon's father called Christmas afternoon at about four (one line). The E003 receipts read back. Wes: "I got to it, mostly." The fan still clicks. Jonathon's "Win the room" has the room crossed out; it's been on the fridge since March. At the fence Wes said "This is the best part of my Christmas"; the brother said "Okay." and got another bale. Mr. Abernathy remembered over his mug: the last breakfast was toast and an eye-doctor ride. The June headings read back. The ledger by the four marks. Jonathon's names, and Virgil's notebook. Wes still calls his daughter only when told. Next moves: Wes, Thu Jan 13 at three, the nursing home back row with his youngest; Jonathon, Mon Jan 3 at 6:10 AM, one verse and one sentence. Wes texts him Thursdays. Proverbs 16:9. 988. Book chapter 34 and training session one plugs, present tense. |
| E104 Field Notes: New Year's Eve (Fri Dec 31) | The man in the truck: "Leon. You could've asked in July." Jonathon's miss: he waited till Thursday to show his card. Dani: "I'd have picked the back step." "But start with this one. I'll take the back step in February." Wes's wife: "Call your daughter." His daughter texted "Heard it. Call me, Dad."; they talked forty minutes and he didn't explain. The youngest: "Are there cookies?" "They're dry." "I'll come." The oldest will tell his foreman Monday he wants to sit for his license. Wes's wife reads the last page first. The one-line plan. Jonathon's mother's question, "What's one sentence you're carrying into 2028?" The sentences "Ask the name" and "Sit on the step." Wes's last text of the year: a full sentence, typed on air to Jonathon. Open into 2028: the friend's scan, Doug's garage door, Virgil's ride, Lyle's mailbox post, the youngest's choice. First challenge of 2028: before Tuesday, do the first ten minutes of the thing you already know is yours. Revelation 21:5. 988. |
