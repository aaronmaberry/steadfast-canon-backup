# Batch report: E081-E088 (podcast v3, written new)

Branch: `podcast-v3-e081-e088`. Prepared for Aaron Maberry. E081-E088 had no v1 scripts, so all eight were written new into `scripts-v3/`. Sources:

- the CALENDAR-104.md rows;
- SHOW-BIBLE section 15 (the payoff map and what's true by then);
- the drafted opens in `_build/intros_data.py`;
- the host files and production/WARDROBE.md;
- the v1 drafts of E049-E080 and the continuity rows for the threads running into the batch.

No existing file was edited or deleted. Overrides and rule fixes are in `scripts-v3/CHANGELOG-V3.md`.

## Status

All eight scripts are finished. Each passes `_build/lint.sh` with no FAIL. Each has exactly one WARN, the DRAFT open (see warning 1 below). Each was timed with `_build/timing.py`, and those times fill the YouTube chapter list. Every script got a listener reread, and the batch got a check for repeated phrases (see the changelog).

| Episode | Format | Spoken words | Minutes (timing.py) | Wes / Jonathon words | Jonathon share | Jonathon lines under 12 words | Longest Wes turn | Lint |
|---|---|---|---|---|---|---|---|---|
| E081 The Dark Stretch | Main | 7,943 | 52:21 | 4,032 / 3,911 | 49.2% | 9.7% (9 of 93) | 122 | Pass, 0 FAIL, 1 WARN (DRAFT open) |
| E082 Field Notes: Noticing a Brother | Field Notes | 3,401 | 22:35 | 1,708 / 1,693 | 49.8% | 16.7% (8 of 48) | 110 | Pass, 0 FAIL, 1 WARN (DRAFT open) |
| E083 Money Tells the Truth | Main | 7,131 | 47:21 | 3,852 / 3,279 | 46.0% | 16.5% (14 of 85) | 124 | Pass, 0 FAIL, 1 WARN (DRAFT open) |
| E084 Field Notes: The Budget Talk | Field Notes | 3,179 | 21:08 | 1,661 / 1,518 | 47.8% | 17.1% (7 of 41) | 119 | Pass, 0 FAIL, 1 WARN (DRAFT open) |
| E085 Paid in Full | Main | 7,029 | 46:53 | 3,865 / 3,164 | 45.0% | 16.1% (15 of 93) | 119 | Pass, 0 FAIL, 1 WARN (DRAFT open) |
| E086 Field Notes: Season Review: The Long Road | Field Notes | 3,208 | 21:18 | 1,621 / 1,587 | 49.5% | 16.3% (7 of 43) | 124 | Pass, 0 FAIL, 1 WARN (DRAFT open) |
| E087 Small Ways to Serve at Home | Main | 7,114 | 47:06 | 3,727 / 3,387 | 47.6% | 15.3% (13 of 85) | 123 | Pass, 0 FAIL, 1 WARN (DRAFT open) |
| E088 Field Notes: Serving Report | Field Notes | 3,206 | 21:29 | 1,829 / 1,377 | 43.0% | 11.6% (5 of 43) | 104 | Pass, 0 FAIL, 1 WARN (DRAFT open) |

Word counts cover spoken lines only. Stage directions, bracketed cues and parentheticals are excluded. A "Wes turn" means every Wes line in a row before Jonathon speaks.

- No Wes turn is over 125 words.
- Four turns run 122 to 124 words: E081, E083, E086 and E087 each have one.
- No host line has a dash, a semicolon (outside NIV quotes, which keep their own punctuation), a mid-sentence colon, a curly quote, "uh," "um," "sir," "week," "weeks" or "weekend." The one exception is the E085 open (warning 2).
- The 988 line is in both mental-health episodes, E081 (the dark stretch) and E082 (the direct question), in a spoken line and in the description.

**Jonathon in the mains.** In each main he pushes back for real at least twice and tells two of his own stories.

| Episode | Jonathon's push-back | Jonathon's stories |
|---|---|---|
| E081 | "Fog is weather. Nobody's ashamed of weather." Wes grants half. The fifty-eight-year-old caller: Jonathon says the evening, not the table; Wes concedes he gave a morning man's answer. | Four months on his mother's couch at twenty-three, the clinic and six counseling sessions. The Friday-noon call to the man sleeping in his truck. |
| E083 | Wes keeps saying "not hiding"; Jonathon asks what the difference is from where she's sitting. Wes concedes there's little difference ("a wall with good manners"). The giving talk: he reaches for his keys when a preacher says "giving." | The twenty-three dollars under his mother's coffee cup at nine. The seven-thousand-dollar card in the junk drawer. |
| E085 | If it's all grace, why the Friday scorecard? Wes answers with Ephesians 2:10 ("a practice, not a payment"); Jonathon keeps the number. Then James and "faith without works." | The plaque in the hall closet and the retired rep's hospital deal. The six-pack in the cooler on the back porch. |
| E087 | Mark 10 isn't about dishes; don't turn the cross into a chore chart. Settled on "We don't copy the ransom. We copy the towel." Then "unnoticed" can make a woman disappear in her own house: he corrects Wes's use of Matthew 6 (it's about alms), and Wes takes the correction. They still disagree on how often to say the list. | Dani's far spot, the cold side of the bed and the burnt pancake. Virgil and Ruby on the second Saturday in October. |

Each Field Notes carries a miss on the table by 3:30. E082: Wes's "I was working sixty hours." E084: Wes explains the deer lease inside an hour. E086: Wes's "only two lunches," then Jonathon's hand stops on "paid." E088: Jonathon's window kit is still in the truck.

## Warnings I could not clear (decisions for Aaron)

1. **The DRAFT open WARN, in all eight.** Every open is a drafted entry in `_build/intros_data.py` awaiting your approval (SHOW-BIBLE section 5). Each script carries the hand-written DRAFT note, and its open facts were checked against the script. One fact to confirm: E088's open says "Dani parks in the far spot at church," and the episode keeps that true, because Dani turns down Jonathon's offer.
2. **"week" in the E085 open.** The approved E085 draft open in intros_data.py says "Reformation week" (Wes) and "a plaque for three good weeks" (Jonathon). The brief bars editing that file, so I left both. Suggested replacements are "Following Jesus as a man, the Sunday of Reformation Day" and "a plaque for twenty-one good days."
3. **New details about Wes's own life.** Wes Hart is your pen-name host, so please strike any of these that misrepresent you.
   - **E081:** the recliner year at about thirty-five, and the TV turned up while his nine-year-old sat on the floor. He never saw a doctor.
   - **E083:** the register in the left desk drawer for twenty-six years. The roughly nine months in 2009 when he stopped giving without telling his wife. A deer lease and a boat kept at his brother's place.
   - **E084:** "That's a barn, Wes," and the money date set for the first Sunday night of the month.
   - **E085:** the October review: a thirty-four-year-old reviewer, "above expectations" on developing others, and "Reliable. Nobody here knows what you think." His index card from before he was married.
   - **E086:** "There it is" at the sink, and his own season letter.
   - **E087:** his wife's nightly rounds of the back door, porch light and stove for twenty-seven years. A second asking of "What are you waiting on?" by Mr. Abernathy at about forty.
   - **E088:** the barn day itself, including the brothers' and the oldest son's sentences. His mother has known since about 2003 that his wife writes the cards.
4. **Wes's dad in E088.** The round 12 rule rests Wes's dad through E088. The E051 setup makes the barn day turn on his father's loppers, so E088 includes the older brother's one word, "Dad's," and nothing more. There's no memory and no grief beat. E082 carries the one plain anniversary report.
5. **The training premiere session.** CALENDAR-104 marks E087 as "T (premiere)" but names no session. I chose Lay It Down, the session that matches Mark 10:45's laying down for others. It's named by title only.
6. **Longest Wes turns of 122 to 124 words** in E081, E083, E086 and E087. All are under your 125 check but over the "about 120" guide.
7. **CHANGELOG merge.** This branch creates `scripts-v3/CHANGELOG-V3.md`, and so do `podcast-v3-e025-e032` and `podcast-v3-e073-e080`. Keep every batch section when merging.

## Continuity assumptions

Anything not already in canon, the calendar or the payoff map is an assumption.

- **E081.** The book plug uses chapter thirty-one in the B slot. Jonathon made the Friday-noon call (set up in the E073-E080 batch), and the man is back in his house. Jonathon's counseling at twenty-three is new canon: four months, his mother in her pharmacy smock, six sessions. So is Wes's recliner year at about thirty-five, placed before Mr. Abernathy's question at thirty-six.
- **E082.** The sixty-one-year-old's new grandson is in San Angelo. The nephew lives in Houston with two roommates (canon). The one moving out is going to Dallas for a job, and the other works as a barista. The rancher who sold down from about ninety cows to twenty is new.
- **E083.** These are all new: Wes's 2009 giving gap, the deer lease and the boat, Jonathon's seven-thousand-dollar card and the spreadsheet's origin in the mortgage year (eleven colors cut to four), and the installer lunch booked for Tue Oct 26 on Bandera.
- **E084.** The four colors, and the red row Dani has kept empty for about eight years. Pancake ate a sticky note. The money date is the first Sunday night of the month.
- **E085.** The review details and the reviewer's age. The retired rep in Corpus Christi, the hospital deal, and the plaque for twenty-one days in the fall of 2023. Jonathon drank on weeknights until about thirty-one, after coming to faith at twenty-nine. Martin Luther is limited to widely documented facts.
- **E086.** The installer starts Mon Nov 1 with a residential outfit on the north side, for less money and home by five. The contractor breakfast slid to November and is stated as a miss. The first cold front is forecast for Fri Oct 29. The Corpus rep answers "Four years, son."
- **E087.** Virgil and Ruby's day is the second Saturday in October (Oct 9), because November's second Saturday falls after the release. Dani's far spot, cold side and burnt pancake are new. Wes's wife's birthday cards are canon (WES-HART-HOST, since 2000), and her nightly rounds are new. Mr. Abernathy's second asking is new; his question is canon.
- **E088.** The barn day is Sat Oct 30 at six, at forty-one degrees.
  - The older brother brought the loppers, and the oldest son came (both per E051).
  - I assumed the little brother came from Fort Worth (E051 said "if Abilene lets him").
  - Each man's sentence is new. Wes's wife heard his four lines Thursday night ("Say it slower. You rush the end."). His own sentence isn't said on air.
  - The youngest's "You didn't rush the end" echoes the E070 weld.
  - Jonathon's pancake report uses Choir Night (Tue Nov 2), because the Saturday pancakes fall after the Friday release.
  - The neighbor across the street is new.

## Rotation and round limits across the batch

- **Sales lens:** E081, E083, E085, E087.
- **Dani quoted:** E083 (two lines), E085 (two), E088 (two). Not quoted in E081, E082, E084, E086 or E087, where her words are reported.
- **Virgil:** E087 only, with no new quotable (E088 names him once at the mailbox).
- **From the Table sources:**
  - E082: Wes, the crop-insurance man in the diner lot.
  - E084: Jonathon, the pickup line.
  - E086: Wes, the Thursday table.
  - E088: Jonathon, the neighbor at the mailboxes.
- **Single checks by text:** the nephew (E086) and Wes's oldest son (E084, E088).
- **Show about itself:** at most one line per episode.
- **"Sir":** none in the batch.
- **"Brother" as an address:** none.
- **Jonathon's father:** a background line only (E083's twenty-three dollars, E086's February plan).

## Continuity rows (what each episode established on air)

## E081-the-dark-stretch
**Wes's recliner year** (about thirty-five, the fog years): a year of suppers in the recliner. His nine-year-old daughter brought her plate and sat on the floor by his chair, and he turned up the TV. He never saw a doctor and won't put a doctor's word on it. The way back was Mr. Abernathy's question and the 5:15 coffee. **Jonathon at twenty-three:** four months on his mother's couch. She sat on the coffee table in her pharmacy smock: "I can't tell if you're sad or if you're lazy. I can help you with either one. But I need you to tell me which." She drove him to a clinic, and he did six counseling sessions. **The Friday-noon call:** Jonathon asked a second time, "No, how are you?", then sat an hour in the man's driveway. The man is back in the house and seeing someone. Psalm 88:1-2 and the 988 line. **Go-firsts:** Wes asks his wife, "What did that year look like from where you were standing?" and tells her that if it comes back he'll see a doctor. Jonathon calls his nephew by voice.

## E082-field-notes-noticing-a-brother
**The nephew by voice (Thu Oct 14):** "Who's in the hospital?" On the second ask he said a roommate is leaving for Dallas in December and the rent won't stretch. "thanks for calling. that was weird. call again tho" **The sixty-one-year-old** missed two Thursdays because of a new grandson in San Angelo. **Wes's wife on the recliner year:** "You quit saying goodnight to the kids. You'd say it to the TV." She kept the kids out of the den all that year, and Wes thanked her. On the doctor: "I'll say it first. You won't like how I say it." **The anniversary (Thu Oct 14),** told once: the tailgate, and the brother's "Me too." **The tool:** the direct question, with 988. **The rancher** who sold down and gave away his saddle: the crop-insurance man drives out Friday with the words Wes gave him.

## E083-money-tells-the-truth
**Wes's register** in the left desk drawer, twenty-six years of bills paid and never shown to his wife ("a wall with good manners"). **2009:** he stopped giving for about nine months. She saw it in the second month and later said, "I wondered when you'd tell me." **Jonathon at nine:** twenty-three dollars of birthday money under his mother's coffee cup, and in the morning it was back on his dresser with a note, "Thank you baby. This is yours." **The seven-thousand-dollar card** under the takeout menus. Dani: "I don't care about the seven thousand. I care that it was in a drawer." The spreadsheet went from eleven colors to four. Also introduced: the deer lease and the boat at his brother's. The installer lunch is booked (Tue Oct 26, Bandera). Luke 12:34.

## E084-field-notes-the-budget-talk
**The register night:** his wife read for two hours. "Nobody's ever asked me to look." He explained the deer lease within the hour (a miss). "That's a barn, Wes." The lease goes at renewal in March. **Money date:** the first Sunday night of the month ("You're nicer on Sundays."). **The four colors** (green, blue, yellow, red), with the red row empty for about eight years. Pancake ate a sticky note. **Wes's oldest:** Sonic thirty-one times, and the foreman laughed. **The tool:** the monthly money date. Proverbs 15:22.

## E085-paid-in-full
**Wes's October review,** told once. "Above expectations" on developing others, which Wes argued down. "Mr. Hart, I'm not paying you back for anything. I'm writing down what happened." Also: "Reliable. Nobody here knows what you think." **Jonathon's plaque:** twenty-one days at number one, fall 2023, on a retired rep's hospital deal, now in the hall closet. **The cooler on the porch:** "You can't get fired from a gift." **Ruby:** "Does God have a sticker chart?" Jonathon: "He doesn't love the good ones. He loves his." Ephesians 2:8-9 and Reformation Day. **The challenge:** the "Paid in full" index card.

## E086-field-notes-season-review-the-long-road
**Wes's retelling to his wife:** good line first, then "It was only two lunches" at the sink. "There it is." **Jonathon's card:** his hand stopped on "paid," and he wrote it Thursday in the truck. **The Corpus call:** "Four years, son." The rep had known all along. The plaque is back on the wall with a sticky note bearing his first name, and there's a jetty fishing trip in the spring. **The nephew's card** is in his hard hat. **The installer** starts Mon Nov 1, home by five. **The sixty-one-year-old's question** and his fall tomatoes. Psalm 90:12. **The tool:** the season letter, and Wes wrote one. **Season 7 review.** Wes keeps "Known is a table." Jonathon keeps "No. How are you?" Still open: the coach letter, the barn Saturday, the contractor breakfast (slid to November) and telling Ruby in February.

## E087-small-ways-to-serve-at-home
**Season 8 (Thanks) opens:** "Who have I never thanked?" **Wes's wife:** twenty-seven years of birthday cards, and the last one up every night. She locks the back door, turns off the porch light and touches six stove knobs with two fingers. Wes watched her from the hallway one October night. **Dani's first picks:** the far parking spot, the cold side of the bed, the burnt pancake. Ruby, Sun Oct 31: "I'll take the dark one. Mommy always gets it." **Mr. Abernathy's second "What are you waiting on?"** came at about forty. Wes answered, "For her to ask." **Virgil and Ruby (Sat Oct 9):** Virgil swept the walk before seven and ate last, standing. He rolled the widow's trash cans to the curb and wrote them in the pencil notebook. Ruby: "Mr. Virgil does the jobs nobody claps for." Mark 10:45, and "We don't copy the ransom. We copy the towel." **The training session Lay It Down** is plugged. **Go-firsts:** Wes takes the back door and thanks her for the cards. Jonathon takes the burnt pancake, offers Dani the door at church, asks about the bed and fixes the window.

## E088-field-notes-serving-report
**The back door:** she checked behind him two nights and slept through the third. "I noticed Tuesday." **The cards:** "Your mother knows. She's known since about 2003." **Jonathon:** Ruby's pancake trade ("Okay, but I get it on your birthday"). The far spot stays Dani's: "I like the walk. It's the only quiet I get all Sunday." He'll carry a young mom's diaper bag instead. She keeps the cold side. The window kit is still in the truck (a miss). **Wes's oldest:** "got to the yard first and filled the water cooler. foreman asked who did it. i didnt say." **The barn (Sat Oct 30, forty-one degrees, after feeding):**
- the older brother: "Dad's." and "A man shows up when it's cold.";
- the little brother: "Your mama prays for you by name. Let her.";
- the oldest son: "You can call me. Any hour. I mean it.";
- Wes said his four lines slowly, because his wife had told him he rushes the end;
- the youngest: "You didn't rush the end."

The loppers ride behind his truck seat. "Same time Saturday." **The neighbor's question** about serving unnoticed. Galatians 6:9. **The tool:** the first-up rule ("When you see it first, you're up.").
