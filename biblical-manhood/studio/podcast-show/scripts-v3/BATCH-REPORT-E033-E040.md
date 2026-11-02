# Batch report: v3 rewrites E033-E040

For Aaron Maberry. Branch: podcast-v3-e033-e040. All eight episodes are rewritten in scripts-v3/ with the same slugs. The first drafts in scripts/ are untouched. Length overrides and rule fixes are in scripts-v3/CHANGELOG-V3.md.

## Per-episode numbers

"Jon share" is Jonathon's share of spoken words (target 35-50%). "Short" is the share of Jonathon's lines under 12 words (limit under 20%). "Long Wes" counts Wes turns over 120 words (target 0). Lint is `_build/lint.sh`; timing is `_build/timing.py`.

| Episode | Type | Spoken words | Minutes | Jon share | Short | Long Wes | Beats | Lint |
|---|---|---|---|---|---|---|---|---|
| E033 Leave Without Slamming the Door | Main | 8,220 | 54:38 | 48.6% | 18.9% | 0 | 6 / 10 | 0 FAIL, 0 WARN |
| E034 Field Notes: The Door Report | Field Notes | 3,527 | 23:41 | 48.2% | 15.3% | 0 | 4 / 9 | 0 FAIL, 0 WARN |
| E035 Your Mom: Mother's Day and Being a Grown Man | Main | 7,385 | 49:11 | 46.8% | 9.6% | 0 | 6 / 10 | 0 FAIL, 0 WARN |
| E036 Field Notes: Mother's Day Field Notes | Field Notes | 3,738 | 24:55 | 49.0% | 9.1% | 0 | 3 / 9 | 0 FAIL, 0 WARN |
| E037 A Man With No Brothers | Main | 7,292 | 48:32 | 47.2% | 8.7% | 0 | 9 / 10 | 0 FAIL, 0 WARN |
| E038 Field Notes: Season Review: The Father Who Stays | Field Notes | 3,379 | 22:27 | 49.3% | 14.6% | 0 | 5 / 9 | 0 FAIL, 0 WARN |
| E039 Ask the Man | Main | 7,057 | 46:58 | 47.0% | 9.0% | 0 | 9 / 10 | 0 FAIL, 0 WARN |
| E040 Field Notes: The Ask Report | Field Notes | 3,540 | 23:34 | 48.4% | 16.0% | 0 | 3 / 9 | 0 FAIL, 0 WARN |

Every main has at least one real Jonathon pushback and two Jonathon stories. Each header's "New in v3" note names them. A separate checker confirmed the following in all eight:

- No dashes, mid-sentence colons, curly quotes, banned words or "Testament".
- No "not just X but Y", uh or um.
- No "week 1" or "weekend", and no eleven or twelve motifs.
- No banned story names and none of the banned names or organizations.
- "Produced with AI voice and video tools." appears in the credits only.
- Plugs are present tense, with nothing about what's coming, no dates and no prices.

## Warnings not cleared (judgment calls for Aaron)

1. **"this week" inside the intros.** E035 ("so this week matters") and E037 ("who'd know if you fell this week") come verbatim from _build/intros_data.py, as the brief requires. Fixing them means editing intros_data.py.
2. **Proverbs 31:28 card (E036).** The NIV verse ends in a colon. The card is exact, so the colon stays. You might prefer carding 28-29 together.
3. **E033 short-line share is 18.9%.** It's under the 20% limit but the closest of the eight.
4. **Beat budget.** E037 and E039 use 9 of 10 beats. Adding a beat in the edit will trip the WARN.
5. **Checker "retell" notes.** These are information only. Each cold open's key line comes back in the body when the full story is told, as the format intends.
6. **E038 and E039 colon-free cards.** Joshua 4:6 (lowercase "to") and Proverbs 13:20 are carded exactly. Wes reads Joshua 4:6 with a capital (the Phil 2:4 precedent).

## Continuity assumptions (invented in v3, please confirm or veto)

These details are new. None of them is about a real person.

- **E033:** Wes went home every Friday night his first semester. His mom's VCR clock call came in year one of marriage. Jonathon and Dani alternate Christmas Eve, and his mom has never asked for the other year.
- **E034:** Wes's late no came in year five of marriage, at Christmas morning at the farm. He said it badly through his wife, then redid it himself.
- **E035:**
  - Jonathon's mom cleaned offices, and she ironed his baseball pants at midnight. He never thanked her.
  - Wes's mom kept a coffee can of quarters for each boy's school pictures. Wes mailed his little brother's can to him after their dad died.
  - Wes's dad tipped big at the diner by the feed store. Wes eats there alone on Father's Day and tips like him.
- **E036:**
  - The gutter email came from a 44-year-old listener ("Must've been the Lord").
  - Merle sang the baritone part over the phone.
  - The hinges are hidden under Wes's truck seat. At seventeen his mom found a dip can in his truck. It was his older brother's, who is now 58 and still hasn't confessed.
  - Jonathon's "Dear Sister" draft.
- **E037:**
  - At 26, the week of Jonathon's mom's gallbladder surgery, a senior salesman at the dealership covered his floor.
  - The mower man after Wes's dad died. He has since died.
  - The kolache men's breakfast.
  - Wes's breakfast sentence to his wife, said Sun May 9.
- **E038:**
  - Jonathon's fourth-grade field trip to the battleship Texas.
  - Jonathon was told to forgive his dad at 19.
  - Dad's shoe brush on the laundry-room shelf.
  - Christmas at the barn.
- **E039:**
  - Wes's lunch partner at 25, who mocked his own wife.
  - Mr. Abernathy's three Thursdays of "I don't know".
  - Jonathon's boss pays a coach who calls him "champ".
  - The lamp aisle, which took twenty minutes.
  - "Good. Easier." at the barn.
- **E040:**
  - The mechanic wants help with the small sockets on Wednesdays, and asks about Merle's lead.
  - Jonathon's neighbor still lives three doors down. They wave.
  - Years back, Wes said no to a young married man in the church foyer. The couple moved to Lubbock.
  - The older church man asks the silent son's name so he can pray for him.
  - Dani's fridge rule.
- **Dating assumption (E040).** The Sunday-text son is "about ten months" silent. E027 (Apr 6) said eight months, so this is rounded up for six weeks.

## Not done or not checked

- No PR was opened, per the brief.
- Each script was checked against CANON.md and the host files for the threads it touches. I didn't do a full read of all 104 episodes against CANON.md.
- The NIV text on the cards comes from the drafts' "checked 2026-10-03" notes. I didn't recheck it against a live NIV source in this run.

## Continuity by episode

| Episode | Release | Opens | Closes or pays off | Hands forward |
|---|---|---|---|---|
| E033 | Tue Apr 27 | Mom's "I don't know what I'm for." Wes's son's truck is paid off. | The truck agreement. "She went inside so I could leave." | The door report (E034). Mother's Day (E035). |
| E034 | Fri Apr 30 | Wes's late Christmas no. | The E033 door challenge. | The mom thread into E035. |
| E035 | Tue May 4 | The screen door job, the coffee cans, the diner tips, Merle (71) and the mechanic. | "I don't know what I'm for" (Dani's Sunday). | The Mother's Day notes and the screen door (E036, E037). |
| E036 | Fri May 7 | The gutter email, the hinges, Wes's breakfast sentence plan, and the twin's dad's card. | The E035 challenge. The Bluebonnets win. | The screen door Saturday. The breakfast sentence (E037). |
| E037 | Tue May 11 | No brothers. "If I fell down tomorrow." Wes's text to his little brother. Shane (unnamed). 988 in the challenge. | The breakfast sentence. The screen door is rehung. "We never once went to school hungry." | Shane's name, the brother's reply, the barn (E038). |
| E038 | Fri May 14 | Shane Texas. The brother's father-in-law is dying. Fishing in June. The stones. | The E037 challenge. The season 3 review. | Lamp shopping, the barn, the garage visit and Merle (E039). Abilene May 29. |
| E039 | Tue May 18 | Ask the Man. Jonathon's father-in-law. The mechanic. The card in Jonathon's wallet. The three months held back. | The lamp, Shane's garage, "Good. Easier." | The mechanic Wed May 19. Dani's dad Sun May 23. The barn May 22. Why three months (E040). |
| E040 | Fri May 21 | The mechanic's no and the sockets. Dani's fridge rule. Wes's old no. The Sunday-text dad's half-yes. | The E039 challenge. The three months (the neighbor's "Catch me later"). | Dani's dad's answer, the van Wed May 26 and the barn (E041). Abilene May 29 (E043 or later). Merle's lead. Fishing in June. The Sunday-text man is closed under round 6 and stays unresolved. |
