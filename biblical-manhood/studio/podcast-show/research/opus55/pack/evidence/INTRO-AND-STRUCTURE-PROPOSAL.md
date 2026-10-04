# Walk Steadfast: the new open and the show's shape

For Aaron. Written 2026-10-03, midday CT. The full research with sources is in `research/TOP-PODCAST-STRUCTURES.md`. The rules live in `SHOW-BIBLE.md` (v3, sections 4d, 5, 13, 14 and 15).

**Where this stands.**
- **Applied.** The new open for E001-E080 and the spoken credit for E001-E080. Both pass lint. Run times barely moved (E020 is 15:55).
- **Proposed only.** The new clock for each episode and a short list of light fixes to E001-E080 (section 5 below). No episode body was rewritten.
- **Still to come.** The Opus 5.5 review pass is packed and ready to launch. Nothing in this document came from Opus.

## What I need from you

1. **Approve the E001 open** (section 3). The E001 opening gets recorded again once you do, so this one blocks audio.
2. **The anchor sentence.** Every open starts with "This is Walk Steadfast." Keep it fixed, or let it move too?
3. **The length of the open.** Mains run 42-62 words (about 18-24 seconds), Field Notes 32-52 and E001 70. Keep these, or cap it shorter?
4. **Jonathon's surname** for the About page (proposed: Reese). On air he stays "Jonathon".
5. **Shorts and the disclosure line.** You named the episode notes and the show description. Should Shorts descriptions carry the line too?
6. **The show description draft** in `launch-kit/SHOW-DESCRIPTION.md`.
7. **The cold open on mains.** Required, or optional? All 80 have one today, and 34 run past 15 seconds.
8. **The proposed clock** (section 5) for E081 on, and the light fixes to E001-E080.

## 1. What the research says, in one page

- **The best shows fix the frame and change the words.** Armchair Expert keeps "Welcome, welcome, welcome to Armchair Expert" and changes how Monica gets introduced. My Brother, My Brother and Me keeps its show line and lets each brother describe himself differently every week. Tim Ferriss rewords his greeting and his mission line every time. This is the model for your note, the same points in new words.
- **Only short sign-ons survive being said word for word.** Huberman, How I Built This and The Daily say the same words every time, and they're all under 15 seconds. Our old standard intro ran 25-30 seconds plus the slate. At that length, repeating it twice a week would wear.
- **Cold open, then the sign-on, then one line on today.** The Daily, Hidden Brain, This American Life, How I Built This and Lex Fridman all open on the story, then say who they are, then say what today is in one sentence. We already had the first two. The missing piece was the "today" line.
- **Short wins.** Of the top 20 Apple shows in one 2025 analysis, 7 had intros longer than 30 seconds. In Spotify's own example, a one-minute intro lost about 10% of listeners early. YouTube's intro number is simply the share still watching at 30 seconds.
- **Video leads, but the truck still listens.** Video passed audio-only podcast use in 2025. A lot of men will still hear this in a truck, so everything shown has to be said too.
- **Recurring bits build loyalty if a new man can follow them.** Listener trust in the hosts is what keeps people, and an inside joke can shut a newcomer out. Every callback needs a clause of explanation.
- **Seasons that work have a spine and a payoff.** BibleProject stops to review. Pardon My Take built yearly events people wait for. TV writers plan the season arc first and then the episodes. That's why section 6 maps the year.
- **Faith shows for men open plainly.** Art of Manliness, Ask Pastor John and Ten Minute Bible Talks open in one or two plain sentences, then go straight to the question or the passage. No hype.

## 2. The open system

**One fixed sentence, then the same beats every week in new words.**

1. **The anchor.** "This is Walk Steadfast." Word for word, whoever leads, so the show lands the same way each time.
2. **One true fact about each man.** Small, specific and current. Some examples are "I sell air conditioning for a living," "My youngest just got his license" and "Dani works nights, so we're good at handoffs." Every fact is checked against the host briefs and the continuity logs for that week. Nothing that will go stale (Theo stays 4 until August, and Wes's dad is "almost nine years" gone until October).
3. **What the show is.** On Tuesdays, a new way of saying "following Jesus as a man". On Fridays, "Friday we report" in its many forms.
4. **The offer.** One line naming the book, the video training and walksteadfast.com, in one of twelve shapes that rotate. Wes says "my book". Jonathon says "Wes's book". The full title, Steadfast Men, comes on E001 and on book weeks. Present tense, with no "out now", dates or prices.
5. **The hook.** One "today" sentence, 14 words at most, aimed at the episode's question without answering it.

**It grows with the year.** Through the first season and Lent (E001-E024), mains have five lines while the men are still being met. From Easter (E025) the mission and the offer share a line, so the open gets lighter as the audience gets to know the table. Field Notes have four lines after the first month.

**How it stays fresh.** A checker (`_build/intro_lint.py`) runs with every lint. It fails any open that reuses a run of five or six words from a nearby episode, misses a beat, runs long, puts "my book" in Jonathon's mouth or breaks the writing rules. All 80 pass with no warnings.

**How it's built.** The words live in one file, `_build/intros_data.py`, and `_build/intro.py` writes them into the scripts. Changing a word is a one-line edit and a re-run, never hand surgery on 80 scripts.

## 3. Five opens side by side

The retired standard intro, for comparison (variant A, 66 words, no "today" line). WES "This is Walk Steadfast. I'm Wes Hart. Twenty-something years at tables with men, and I wrote a book about what I heard." JONATHON "And I'm Jonathon. Husband, dad of two, sales manager, still learning." WES "Twice a week we talk straight about following Jesus as a man. At home, at work, with your friends." JONATHON "Steadfast is the book, a video training for men, and this table. It's all at walksteadfast.com."

| Beat | E001, launch (Tue Jan 5) | E002, Field Notes (Fri Jan 8) | E013, main (Tue Feb 16) | E040, Field Notes (Fri May 21) | E079, main (Tue Oct 5) |
|---|---|---|---|---|---|
| Anchor and lead | WES: This is Walk Steadfast. I'm Wes Hart. I've sat at tables with men for twenty-some years. | JONATHON: This is Walk Steadfast. I'm Jonathon, and my wife works nights. | JONATHON: This is Walk Steadfast. I'm Jonathon. I run a regional sales team. | JONATHON: This is Walk Steadfast. I'm Jonathon. I manage commercial air conditioning sales. | JONATHON: This is Walk Steadfast. I'm Jonathon. I've sat across from Wes most Thursdays for years. |
| The other man | JONATHON: I'm Jonathon. I came to faith at twenty-nine, and I'm still learning. | WES: I'm Wes Hart. Married twenty-seven years. | WES: I'm Wes Hart. I've sat at Thursday breakfasts with men for twenty years. | WES: I'm Wes Hart. I'm better at asking men questions than answering them. | WES: I'm Wes Hart. My book came out of what men told me at tables like this one. |
| What the show is | WES: Starting today, twice a week, we talk straight about following Jesus as a man. | JONATHON: Tuesday we hand out one challenge and take it ourselves. Friday we report. | JONATHON: We talk plainly about following Jesus as a man. Tuesdays long, Fridays the report. | JONATHON: Friday we report. (shares a line with the offer) | JONATHON: Twice a week, following Jesus as a man, hard weeks too. (shares a line with the offer) |
| The offer | JONATHON: Wes wrote a book called Steadfast Men, and there's a video training for men. Both are at walksteadfast.com. | WES: My book and the video training are both at walksteadfast.com. | WES: My book and the video training go with this show. walksteadfast.com. | Steadfast Men, the book, and the video training live at walksteadfast.com. | Find the book and the Steadfast video training at walksteadfast.com. |
| The hook | WES: Today we start where most men start. With good intentions. | JONATHON: Today, where to start if you've never been the spiritual one. | JONATHON: Today we look hard at the prizes men work for. | WES: Today we ask what you do when the answer is no. | WES: Today we talk about where men put a loss. |
| Slate | JONATHON: Episode one. WES: Tuesday, January fifth, twenty twenty-seven. JONATHON: The Man You Keep Saying You'll Be. | WES: Episode two. Friday, January eighth. JONATHON: Field Notes. The First Check. | WES: Episode thirteen. JONATHON: Tuesday, February sixteenth. WES: The Prize That's Gone by Thursday. | JONATHON: Episode forty. Friday, May twenty-first. WES: Field Notes. The Ask Report. | JONATHON: Episode seventy-nine. WES: Tuesday, October fifth. JONATHON: Grief at the Table. |
| Words in the open | 70 | 51 | 60 | 49 | 62 |


## 4. The disclosure, as you locked it

"Produced with AI voice and video tools." is one spoken line in the credits. After the closing music, Wes reads it at normal credits volume, like a producer credit, with no gap and no ducking. It is also a plain sentence at the end of every episode's notes and in the show description. It appears nowhere else. Lint fails any other AI mention, a changed word, a second copy or a missing credit. The credit is in E001-E080, the templates, the E001 notes and description, and the E001 re-record notes.

## 5. Episode architecture

**Applied now.** The open (about 18-24 seconds on mains) and the closing music and credits (about 6 seconds). Everything else in the episodes is as written.

**Proposed for E081 on (SHOW-BIBLE 4d).** A Tuesday main, about 26 minutes:

| Clock | Segment | Why |
|---|---|---|
| 0:00-0:15 | Cold open, then the sting | The best exchange, short. 34 of the 80 run 16-21 seconds now. |
| 0:18-0:46 | Open and slate | Applied. |
| 0:46-2:10 | Pull up a chair | The question said out loud by about 2:10. Today the first story starts after 2:30 in 24 of 40 mains, and as late as 5:51. |
| 2:10-7:20 | First story | With a turn at about 3:00-4:30 and again near 6:00. |
| 7:20-10:10 | The Word | The first payoff comes sooner. It starts after 10:10 in 16 of 40 mains now. |
| about 10:10 | Subscribe | Right after the Word, with the twice-a-week fact for a man who just found us. It sits after 13:00 in 19 mains now. |
| 10:10-18:00 | Pushback | The calendar's plug, when there is one, lands at 14:00-15:30, two minutes clear of the subscribe line. In 17 mains they sit back to back now. |
| 18:00-24:30 | What I actually did, the challenge, Carry This | |
| end | Outro, closing music, credits | |

**A Friday Field Notes, about 14 minutes.** The report starts by 1:15, and a miss is on the table by 3:30. At about 6:30, one clause catches up a late listener ("If you're just joining, Tuesday's challenge was..."). Then From the Table, the tool and a short outro. There's still no subscribe line on Fridays.

**Light fixes to E001-E080, proposed and not applied.**
- Trim the 34 cold opens over 15 seconds.
- In 13 Field Notes (E004-E028), the first line after the slate says "This is Field Notes" again. Drop the repeat and keep "Pull up a chair."
- E058's cold open is silent on the audio feed. Add one audible beat.
- Space the plug and the subscribe line in the 17 mains where they touch.
- Look at the 14 chapters that run past six minutes for a turn.
- E005 (24:41) and E038 (13:28) are a little short. Leave them or add a minute.

## 6. The year at a glance

| Season | Episodes | The question underneath |
|---|---|---|
| Pull Up a Chair | E001-E014 | Who are these two men, and what does a quiet Tuesday ask of me? |
| What You Inherited | E015-E024 | What was I handed, and what's actually mine? |
| The Father Who Stays | E025-E038 | Where does a man learn to stay? |
| Brothers | E039-E044 | Who would I call a brother? |
| Fathers | E045-E052 | What will my kids remember? |
| The House | E053-E070 | Work, home and money. |
| The Long Road | E071-E086 | What do I build when nobody claps? |
| Thanks | E087-E094 | Who have I never thanked? |
| Advent and Christmas | E095-E104 | What am I waiting for, and what do I carry into next year? |

**What a man who listens all year gets paid for.**
- **Jonathon's father.** The friend request, the first call he ever made ("Not yet."), "You too, bud," and maybe a thank-you question at Thanksgiving, but only if his dad actually calls.
- **Wes and his wife praying out loud.** Still no in March, still no in July. A small first in November, with no bow on it.
- **Wes's October.** His dad's anniversary and his work review, both told plainly and once.
- **The men around the table.** Merle's quartet, Virgil and Ruby's Saturdays, the man in the truck, the Austin manager, the 24-year-old and the nephew. The plan has Merle's quartet singing Christmas hymns at the nursing home in Simeon week.
- **The small running jokes.** The Bluebonnets, Ruby's dog Pancake ("Yet."), and Wes's "K" texts.
- **Bookends.** In January each man writes the sentence he's been living. In the last week of December those sentences get read back. The year ends by handing off the first challenge of 2028, not with a summary.

## 7. Files

| What | Where |
|---|---|
| Research with sources | `research/TOP-PODCAST-STRUCTURES.md` |
| Rules (open system, credits, proposed clock, season map, decisions) | `SHOW-BIBLE.md` v3 |
| All 80 opens | `_build/intros_data.py` (written into the scripts by `_build/intro.py`) |
| Open checker | `_build/intro_lint.py` (run by `_build/lint.sh`) |
| Credits tool | `_build/credits.py` |
| Structure audit (read only) | `_build/structure_audit.py`, output in `research/_work/structure-audit.md` |
| E001 re-record notes | `episodes/E001/QA.md` |
| Grok critique of the first draft (Grok, not Opus) | `research/_work/grok47-critique.md` |
| Opus 5.5 review pack, waiting for launch | `research/opus55/` |
