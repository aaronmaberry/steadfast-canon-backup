# Batch report, E017-E024

For Aaron Maberry. Branch podcast-v3-e017-e024. All eight episodes are rewritten as complete files in scripts-v3/. The first drafts in scripts/ are untouched, and so is every other existing file.

## Per-episode numbers

Words are spoken words. Minutes are from `_build/timing.py` (Wes about 145 wpm, Jonathon about 170). Share is Jonathon's share of spoken words. "Short" is the share of Jonathon's lines under 12 words; the target is under 20%. "Longest Wes turn" checks the 120-word ceiling.

| Episode | Kind | Words | Minutes | Wes / Jonathon words | Jonathon share | Short Jonathon lines | Wes turns over 120 words | Lint |
|---|---|---|---|---|---|---|---|---|
| E017 Skip the House, Run the Room | Main | 8,086 | 53:50 | 4,109 / 3,977 | 49.2% | 12 of 130 (9.2%) | none | Clean, 0 FAIL, 0 WARN |
| E018 Field Notes, Which Shape Are You | Field Notes | 3,463 | 23:07 | 1,755 / 1,708 | 49.3% | 4 of 58 (6.9%) | none | Clean, 0 FAIL, 0 WARN |
| E019 What Your Anger Is Guarding | Main | 7,091 | 47:09 | 3,723 / 3,368 | 47.5% | 8 of 103 (7.8%) | none | Clean, 0 FAIL, 0 WARN |
| E020 Field Notes, Cooling Off Without Checking Out | Field Notes | 3,510 | 23:26 | 1,769 / 1,741 | 49.6% | 6 of 61 (9.8%) | none | Clean, 0 FAIL, 0 WARN |
| E021 The Itch and the Drift | Main | 6,849 | 45:26 | 3,664 / 3,185 | 46.5% | 8 of 104 (7.7%) | none | Clean, 0 FAIL, 0 WARN |
| E022 Field Notes, Drift Check | Field Notes | 3,437 | 22:57 | 1,758 / 1,679 | 48.9% | 11 of 65 (16.9%) | none | Clean, 0 FAIL, 0 WARN |
| E023 Two Gardens | Main | 6,852 | 45:39 | 3,691 / 3,161 | 46.1% | 15 of 108 (13.9%) | none | Clean, 0 FAIL, 0 WARN |
| E024 Field Notes, Good Friday (season 2 review) | Field Notes | 3,284 | 22:01 | 1,715 / 1,569 | 47.8% | 8 of 61 (13.1%) | none | Clean, 0 FAIL, 0 WARN |

Totals: 42,572 spoken words, about 284 minutes (4 hours 44 minutes).

Each main has Jonathon pushing back on Wes at least twice, and each main carries at least two stories from his own life. Field Notes check the previous Tuesday's challenge, with a single-man check in every one. The standing outros rotate C, F1, D, F2, E, F3, A, F4, each reworded.

## Warnings not cleared

- **Lint INFO, eleven/twelve number check.** Every file prints an INFO line counting spoken "eleven" and "twelve". It's informational, not a WARN. Each instance was checked against canon and the calendar (for example, the eleven cars at car care, the eleven people at the pot roast, the twelve Saturdays, the twelve-dollar alarm clock).
- **E021 and E023 sit near the floor.** They run 45:26 and 45:39, inside the 45-60 window but close to the bottom. Their word counts (6,849 and 6,852) are a little under "about 7,000" because Jonathon carries more of the words and reads faster. I left them there rather than pad them.
- **structure_audit.py doesn't cover v3.** It reads only scripts/, so it was not run on these files. Lint, timing, the share and short-line counts, a six-word repeat scan across the batch, and a colon scan of the published prose were run instead.
- **Repeats across the batch.** The six-word scan's remaining hits are on purpose. They are callbacks ("What's it guarding?", "Forgot, or drifted?", "Moved twice? It's a tree."), scripture, quotes repeated as quotes, and the challenge opener "Here's the challenge, between now and Friday."

## Length overrides

Every episode overrides the old bible lengths, and E020 overrides its explicit 16:00 cap. All of it is logged in scripts-v3/CHANGELOG-V3.md.

## Continuity assumptions

No earlier v3 batch had pushed when this batch was written, so there were no continuity rows to read before E017. The neighbours were the v1 drafts (E016, E025) and the E025-E032 v3 branch (origin/podcast-v3-e025-e032, which had E025-E028 at the time of writing). These are the calls I made where the record was open or thin:

1. **Two different divorced dads.** The one at Wes's table in E017 (eight years divorced, two boys) and the one in E019 (six years divorced, a son and a daughter, the Astros) are different men.
2. **The money line belongs to Monday.** In E020, Jonathon's money line comes from Monday night.
3. **Jonathon's own porn history is one sentence.** In E021 it stays at "I've been there. Longer than you'd guess," and "It's not a secret in my house. It's just not a podcast." Later episodes should not open it further on mic without Aaron's say.
4. **Dani sends him back past herself.** Dani's answer in E018 points Jonathon to someone who knew him before her, and his sister answers in the same episode.
5. **The friend request.** Jonathon's dad's request stays unanswered through E024. Jonathon set Easter Sunday night (Mar 28) as his date to decide. The E025-E032 batch has him accept it at 9:40 PM that night, which fits.
6. **Ruby's question is still owed.** Ruby asked "Daddy, do you have a dad?" and Jonathon owes her the answer himself, after Easter.
7. **Wes and his daughter.** Wes has not told her about the five hours in 2018. Still open at E024.
8. **The brother call.** It's set for Tuesday Mar 30, "Call about Mom", in ink.
9. **Praying out loud.** Wes and his wife still don't pray out loud together. "Still no. Put it on the list."
10. **E013's hidden thing.** Wes said "probably by Easter". In E024 he answers "Off mic" and the show leaves it there.
11. **Rep timeline.** The rep Jonathon let take the blame dates from his first year as a manager, nine years ago at 28, to match canon (Jonathon is 37).
12. **New minor people.** These are invented for this batch, with no names, and none of them is a real person:
    - the 60-year-old contractor learning to weld (E017, E019)
    - the two divorced dads
    - the 71-year-old farmer at Wes's table (E023)
    - the 77-year-old widower (E021)
    - the welder father (E021)
    - Harper and Harper's dad
    - the twins and the twin's dad
    - the 81-year-old mechanic and the 12-year-old who handed him wrenches (E020)
    - the PT therapist
    - the feed-store man (E024)

    Aaron may want to approve them before they recur.

### New canon the E025-E032 batch doesn't have

The E025-E032 v3 branch was written from the v1 drafts of this batch. I read E025-E028 and found no contradictions. These v3 facts are new and that batch doesn't reference them. Later batches should pick them up or leave them alone, not contradict them.

- **The rep.** Jonathon found the rep online (Colorado) and hasn't written him. Still open.
- **The debates.** Three disagreements are logged as unsettled:
  - which shape is worst (E017)
  - the married man with a secret itch (E021)
  - "say the time" as its own tree (E023)

  The heart disagreement in E025 would be a fourth.
- **The truck situation.** Wes's 16-year-old's old pickup came from the uncle, and the boy is working it off on the twelve Saturdays.
- **People at Wes's table.** The 71-year-old farmer and the 77-year-old widower (Tuesday 6:30 breakfast).
- **Jonathon's driveway.** Forty minutes on his phone after a real late call: "The call was real. The driveway wasn't."
- **Good Friday.** Wes and his wife read the Passion on the porch on Good Friday night. Wes and his oldest son keep noon to three quiet, the way his dad did with the radio.
- **The feed-store man** whose card kept declining (E024).
- **The twin's dad** brought his own glove and played catch with his daughter for the whole Thursday practice (E024). E028's "heard your show" fits after this.
- **Screen time.** Both men send their number with the Thursday text. The second numbers are Wes 2h 58m and Jonathon 4h 31m.

## Continuity rows

What each episode established on air.

| Episode | Established on air |
|---|---|
| E017 | **Shapes.** Three shapes of the man who misreads his place: skip the house, run the room, wear the job as your name.<br>**Jonathon.** He coaches Ruby's Bluebonnets again (first practice Sat Feb 27, 12 kids, every name and one fact each). Theo: "Why do you only do the coach voice at practice?" Sunday's catch went over the fence to the retired neighbor ("My dad's a coach"). The coach voice started at nine ("man of the house"). His run-the-room was calling the VP over the rep, and he texted the rep "What do you want me to do?"<br>**Wes.** He lost his title in 2019 at 44 and didn't tell his wife for three weeks. His daughter at 17 asked "Are you mad at us?" and at 25 says "That was the year you started asking us stuff." The church line "three kids and a mother who counts my reps" made his wife medium mad.<br>**Wes's table.** The 60-year-old contractor ("I'm not on your crew"). The divorced dad's boy: "Can we just be boring with you?"<br>**Unsettled.** Jonathon says run the room is worst; Wes says skip the house.<br>**Nephew.** He brings the oranges.<br>**Challenge.** Name your shape, do one contrary act, and if married, ask your wife. |
| E018 | **The gutter.** Hung level on Feb 27, so Monday's rain ran the wrong way. Redo set for Mar 13.<br>**The rep replied.** "Just don't do it again. And the next big one's mine." Jonathon: "Deal."<br>**Jonathon's twenty minutes.** Three of four nights. On the fourth, Ruby carried his phone in "like evidence."<br>**Dani and his sister.** Dani: "Ask somebody who knew you before me." His sister: "Skip the house... You were nine... But you're not nine now."<br>**Wes and his wife.** She said "Run the room. With your mother." The grab bar went in almond, not chrome.<br>**Nephew.** His roommates say he's "only fun when other people are around." He watched their cooking show, phone in his room.<br>Wes will ask his older brother next. |
| E019 | **Anger.** Ephesians 4:26-27 and the foothold. Mr. Abernathy's (2013) question, "What's it guarding?"<br>**Wes.** The horn in fall 2009 with his 7-year-old daughter in the back. She says now, "I thought it was because I was kicking your seat."<br>**Jonathon.** He snapped "I've got it" at Harper's dad over his sore shoulder and went cold on Ruby over a juice box. Guarding: "Never let them see you hurt." He apologized, and Harper's dad throws BP now. "Doctor's next season." His mom's cold anger ("mad at the toaster"). Ruby's climbing-wall jellybean hold.<br>**Wes's table.** The contractor's "hat weather". The second divorced dad: "We're not friends. We're Astros people."<br>**Pushback.** Jonathon warns "What's it guarding" can become a fancy because.<br>**Challenge.** Ask it the day it happens, write one line, and say it out loud to one person. |
| E020 | **Car-care Saturday (Mar 6).** Eleven cars and nine moms. The 81-year-old mechanic did fourteen oil changes and gave the wrench boy a socket set ("Next month. First Saturday"). It now runs every first Saturday, with Wes on coffee. Bald tires replaced by Wednesday (the right anger).<br>**Jonathon's three notes-app lines.** Money, from his mom's bills when he was nine: "You're not dumb about money. You're dumb about the spreadsheet." The rep's email. Theo's shoes.<br>**Wes at PT.** "I'm scared I'll end up like Dad." His wife: "Me too, a little." He apologized; Mom: "He's always been a baby about his knees."<br>**The little brother.** First birthday call in about twenty years, forty minutes long.<br>**Calm.** The twenty-minute rule ("Garage arguments are the worst arguments. Echoey"). Jonathon pushes that calm can hide passivity.<br>**Wes's son.** "foreman yelled. guarding? scared i'm not good at this." |
| E021 | **The itch and the drift.** Proverbs 4:23.<br>**The nephew.** At 1:14 AM, "how do you stop." Porn since 13. He told a roommate the whole truth, and Jonathon texts Thursdays. Day five, named with permission and no name. Jonathon: "I've been there. Longer than you'd guess." "He's not disgusted by you. He's after you."<br>**Wes's drift.** About three hundred hours of tractor videos and an empty radar since October. His wife: "You're doing the fog again." Twenty minutes on the porch.<br>**Dani's dad.** Golf on TV, and "I'm marrying you because you talk."<br>**Wes's table.** The welder who mended things with his son in a taco parking lot. The 77-year-old widower's Tuesday breakfast.<br>**Jonathon.** Folding laundry with Dani; the twins are at thirty-one weeks.<br>**Unsettled.** Who a married man tells first.<br>The 988 line is said on mic, with SAMHSA in the description.<br>**Bluebonnets.** First game set for Mar 20. |
| E022 | **The nephew slipped** on day six and told Jonathon within forty minutes: "that was faster than last time."<br>**Wes's porch.** Four of seven nights. "I drifted. I told myself I forgot."<br>**Mom's first pot roast Sunday.** Eleven at a table for eight, with the leaf in for the first time since Wes's dad died. The card was "Exhibit A". "Mom, it's your table." She prayed for all eleven by name.<br>**Jonathon.** Bath time five of seven nights ("Can you be the shark?"). "The call was real. The driveway wasn't."<br>**Screen time.** Wes 3h 41m and Jonathon 5h 12m, sent with the Thursday text but not graded. Grayscale. The charger in the hallway and the twelve-dollar alarm clock.<br>**Wes's time back.** He held the flashlight under the hood of his 16-year-old's truck while the boy talked for an hour. The radar now sits in a "Later" folder. |
| E023 | **Two gardens.** 1 Corinthians 15:45 and John 18:8, "let these men go".<br>**The gutter works.** Rain on Mar 21; the knee called it.<br>**Bluebonnets' first game, lost by one.** Jonathon reached the twin first: "Still brave." The twin's dad: "I froze."<br>**Jonathon's father.** The friend request (the redfish photo) has been pending since Christmas, and Easter Sunday night is his date to decide. Ruby's "Do you have a dad?" is still owed. "He came out to get me" (his first Easter, at 29).<br>**The rep Jonathon let take the blame** in his first year as a manager. He found him online and hasn't written.<br>**Wes.** The five hours in 2018 ("I needed you at four o'clock"). To his brother: "Tuesday after. I'll call." The farmer at his table. Peter's sword, and his son and the light pole: "Then it's a bumper."<br>**Unsettled.** "Say the time" as a tree, with the agreed line "Moved twice? It's a tree."<br>**Challenge.** Which man you've been walking like. |
| E024 | **Season 2 review** (What You Inherited, E015-E024), on Good Friday. John 19:30.<br>**Noon to three.** Wes's dad turned the radio off from noon to three. Wes's oldest son is doing it on the job site, and Wes is doing it too.<br>**Jonathon's family read John 18-19.** Ruby's NARATOR tabs. Theo under the table. "Especially Mommy."<br>**The check.** Wes picked up his daughter's call during a meeting (Grandma's rolls), but hasn't told her about the five hours. The brother call is in ink for Mar 30.<br>**The twin's dad** brought his own glove.<br>**The feed-store man.**<br>**Quiet versus fog.** The fog was leaving; his dad's quiet was staying.<br>**Second screen-time numbers.** Wes 2h 58m and Jonathon 4h 31m.<br>**What stuck.** "You ask now." "You stopped landing every story."<br>**What didn't.** Praying out loud ("Still no"), and the coach voice back in the drawer on Mondays.<br>**Still open.** For Wes, the five hours and the brother. For Jonathon, the fish, Ruby's question and the rep.<br>**Keeps.** Wes, "What's it guarding?" Jonathon, "Forgot, or drifted?"<br>**E013's hidden thing.** "Off mic." |
