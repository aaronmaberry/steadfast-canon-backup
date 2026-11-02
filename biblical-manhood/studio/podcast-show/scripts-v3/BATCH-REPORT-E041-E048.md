# Batch report: v3 rewrites E041-E048

For Aaron Maberry. Branch: podcast-v3-e041-e048. All eight episodes are rewritten in scripts-v3/ with the same slugs. The first drafts in scripts/ are untouched. Length overrides and rule fixes are in scripts-v3/CHANGELOG-V3.md.

## Per-episode numbers

"Jon share" is Jonathon's share of spoken words (target 35-50%). "Short" is the share of Jonathon's lines under 12 words (limit under 20%). "Long Wes" counts Wes turns over 120 words (target 0). Lint is `_build/lint.sh`, and timing is `_build/timing.py`.

| Episode | Type | Spoken words | Minutes | Jon share | Short | Long Wes | Beats | Cold open | Lint |
|---|---|---|---|---|---|---|---|---|---|
| E041 These Men Are My Brothers | Main | 8,407 | 55:46 | 49.3% | 15.6% | 0 | 7 / 10 | 36 words | 0 FAIL, 0 WARN |
| E042 Field Notes: Memorial Day | Field Notes | 3,272 | 21:47 | 47.8% | 15.9% | 0 | 5 / 9 | 22 words | 0 FAIL, 0 WARN |
| E043 No Fixed Star | Main | 7,184 | 47:38 | 47.5% | 5.2% | 0 | 10 / 10 | 28 words | 0 FAIL, 0 WARN |
| E044 Field Notes: Finding North | Field Notes | 3,328 | 22:13 | 48.9% | 14.8% | 0 | 6 / 9 | 33 words | 0 FAIL, 0 WARN |
| E045 Your Daughter Is Watching | Main | 7,932 | 52:31 | 49.7% | 9.9% | 0 | 8 / 10 | 14 words | 0 FAIL, 0 WARN |
| E046 Field Notes: The Daddy-Daughter Report | Field Notes | 3,547 | 23:34 | 49.9% | 9.6% | 0 | 3 / 9 | 31 words | 0 FAIL, 0 WARN |
| E047 Give Your Son a Name | Main | 7,035 | 46:36 | 48.6% | 9.3% | 0 | 8 / 10 | 33 words | 0 FAIL, 0 WARN |
| E048 Field Notes: Father's Day When It's Complicated | Field Notes | 3,461 | 22:59 | 49.5% | 10.0% | 0 | 4 / 9 | 38 words | 0 FAIL, 0 WARN |

Every main has at least one real Jonathon pushback that Wes has to answer, plus at least two of Jonathon's own stories. Each header's "New in v3" note names them:

- **E041:** "don't leave" is the floor, which goes back to his father leaving when he was nine.
- **E043:** he keeps the number argument open.
- **E045:** "On your heart first" is easy to say.
- **E047:** "the man of the house" was a name, and it was a job.

The Field Notes carry real disagreements too:

- **E044:** monthly or September for the reread.
- **E046:** sometimes the lecture is the loving thing.
- **E048:** Wes says the afternoon alone "sounds like hiding."

A separate checker confirmed the following in all eight:

- No em or en dashes, mid-sentence colons, curly quotes, uh or um.
- No "not just" or "not only".
- No "week N", "front step", "leather notebook", "napkin" or "deleted text".
- "this week" and "weekend" appear only in the two locked intro lines below.
- "Produced with AI voice and video tools." is the last spoken line in every episode, and AI isn't mentioned anywhere else.
- Plugs are present tense, with nothing about what's coming, no dates and no prices.
- 988 appears in the mental-health episodes (E041, E042, E046, E048). The National Domestic Violence Hotline appears where a home may be unsafe (E045, E047).

## Warnings not cleared (judgment calls for Aaron)

1. **"this week" and "weekend" inside the intros.**
   - E042: "This is Walk Steadfast, Memorial Day weekend."
   - E047: "...this week as fathers of boys."

   Both come verbatim from _build/intros_data.py, as the brief requires. Removing them means editing intros_data.py.
2. **Course numbering (no fix needed).** There are three numbering systems for the same topics:
   - The calendar's "course session 19" (E045) and "20" (E047) follow the source course listed in CANON.md (19 is A Man and His Daughters, 20 is A Man and His Sons).
   - training/MAP.md has them as rows 20 and 21.
   - The YouTube lectures say "Session 21 of 24" and "Session 22 of 24."

   None of these numbers is said on mic. Only E047 plugs a session, and it names the video training's W10, The Father Who Does Not Leave, as the closest, because the 24 video sessions have no sons session. My earlier drafts called this a calendar slip. CANON.md shows it isn't.
3. **E043 uses all 10 of 10 beats.** Adding a beat in the edit will trip the WARN.
4. **E046 and E045 Jonathon share is 49.9% and 49.7%.** Both are under the 50% limit but close. Any added Jonathon line in the edit should be balanced with Wes.
5. **E042 has two Jonathon turns over 160 words.** The brief caps only Wes turns. They're the Chris and Shane story turns, and splitting them would break the telling.
6. **Isaiah 43:1 partial card (E047).** Only the dash-free second half is carded, exact. If you prefer the calendar's paraphrase, the replacement line is in the E047 production notes.
7. **E048 intro age math.** The locked intro says Wes's dad has been gone "almost nine years." Canon has the youngest at six when his grandfather died, and he's sixteen now, which suggests about ten. It's a minor inconsistency in locked text.
8. **"eleven/twelve" INFO counts.** E045 has 3, E046 has 1 and E047 has 5. These are ages and counts, such as Wes's oldest at twelve and "twelve Saturdays," not number jokes. This is information only.
9. **Shane's grandfather aboard the ship (E042).** This is show fiction about a fictional family. An alternative line is in the E042 notes.

## Continuity assumptions (invented in v3, please confirm or veto)

These details are new. None of them is about a real person.

- **E041:**
  - Dani's mom rewashed the roasting pan after Jonathon did the dishes.
  - The gutters man at the Thursday table (one line, unnamed).
- **E042:**
  - Wes says plainly that he never served. The host file has no service for him.
  - Wes's uncle by marriage served in Korea and never talked about it (one line).
  - Ruby practiced saying "Christensen" in the car.
- **E043:**
  - Wes's wife brought up "I can do Saturday" once at breakfast, and he changed the subject to the gutters.
  - The listener who had a heading and had an affair anyway.
  - "Get Mom moved" is on Wes's card.
- **E044:**
  - The reread lands on the first Sunday of each month, with a rewrite in September.
  - Wes's "no new committees."
- **E045:**
  - Wes's three questions were his dad's (crops, school, the dog).
  - Dani's college ex had a ferret.
  - Jonathon sits in the truck in the garage for four minutes before going in.
  - Wes's "church voice."
  - Wes's son-in-law asked what his daughter was like at nine ("her bike").
  - Jonathon's sister brings up the year he didn't pick up.
- **E046:**
  - The VP's "Dentist?" calendar comment and "Catch anything?"
  - The contractor's baby is named Lily.
  - Wes stood on the porch two nights, and his wife asked if he'd locked himself out.
  - The brother taught the youngest the hay spear.
- **E047:**
  - Jonathon's grandmother's ring, pawned by his mom one winter and bought back at 24.
  - Wes once called his oldest "my steady one," and the boy didn't cry at his granddad's funeral.
  - "Tyler" is a sample name in a listener answer. Check it against names.json.
  - The theater-son and eye-rolling listener cases.
- **E048:**
  - Wes's first Father's Day after his dad died: he stood, sat down partway, and his wife's hand stayed on his knee.
  - Fried bologna was Wes's dad's Saturday breakfast.
  - Jonathon's Father's Day drive goes out toward Waller and includes a field where he prays. Dani is to get the pin.
- **Cross-batch check.** The E033-E040 branch's E035 v3 has Wes eating alone at the diner by the feed store on Father's Day and tipping like his dad. E048 doesn't mention the diner and doesn't contradict it. If both batches merge, E048's "I might make fried bologna Sunday" can sit beside it, or one can go.

## Not done or not checked

- The brief says no PR is needed. The repo's agent tooling opens one for the branch, and it isn't merged.
- Each script was checked against biblical-manhood/CANON.md (the four marks, the names and sources rules, and the course map), the host files (WES-HART-HOST.md, JONATHON-CHARACTER.md), and the neighboring episodes for the threads it touches. I didn't do a full read of all 104 episodes. The marks are used by their CANON titles (Pick Up the Weight in E047, Go First in E045 and E047). The source course and its speakers are never named.
- The NIV card text comes from the drafts' "checked 2026-10-03" notes. I didn't recheck it against a live NIV source in this run.
- Hotline numbers (988, 1-800-799-7233) should be re-verified before publish, as each production note says.

## Continuity by episode

| Episode | Release | Opens | Closes or pays off | Hands forward |
|---|---|---|---|---|
| E041 | Tue May 25 | Dani's dad's "How did you stay?" The band director's kitchen. The Austin manager ("My wife moved out in March"). The second barn Saturday. | The E040 handoff (Dani's dad's answer, the barn). | Wes's call to his little brother Thu May 27 (the dog). Abilene Sat May 29. Memorial Day (E042). |
| E042 | Fri May 28 | Deputy the dog. The Memorial Day names. Jonathon's missed Shane call. | The E041 challenge. Wes learns the dog's name. | Fort Sam Mon May 31. Shane's call (E043). |
| E043 | Tue Jun 1 | Fort Sam and the mechanic. No fixed star. Wes's card. His wife's breakfast comment. | Jonathon's Shane call on Mon May 31. | Wes's heading reported in E044 ("whoever called last"). |
| E044 | Fri Jun 4 | The one-page house plan. Wes's page. The monthly reread. The 24-year-old car-care regular. | The E043 challenge. The brothers season review. | The Fathers season (E045). |
| E045 | Tue Jun 8 | Your daughter is watching. Wes's three questions. Ruby's "Do you like your job?" "Are you mad at us?" (2019). | The Austin ponytail setup and fishing at the stock tank. | Fishing Thu Jun 10. The first ten minutes. The drive-through (E046). |
| E046 | Fri Jun 11 | Ruby's bluegill and "Not as much as the fish." The Louisiana question. Lily. The drive-through date. | The E045 challenge. Austin's ponytail. | The Thursday-table man's drive-through. The Louisiana question (E048). Sons and names (E047). |
| E047 | Tue Jun 15 | The cap on the knee. "Bud." "Man of the house." The porch step. "Are you sick?" | The bluegill named Steve. The drive-through report. The second "proud" to the oldest. | Father's Day Sun Jun 20. The text to his father. The tally (E048). |
| E048 | Fri Jun 18 | The bus-stop card. "Alone is fine. Missing isn't." Wes's first Father's Day after his dad. The three-word text without the photo. Bless a younger man. | The E047 challenge (the tally at four, "Weird"). The Louisiana question as the reason the photo stays home. | E049: "You too, bud." The nephew and the 24-year-old blessings. "Ask me Monday." The field pin. |
