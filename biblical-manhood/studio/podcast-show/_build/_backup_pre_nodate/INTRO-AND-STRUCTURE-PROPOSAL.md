# Walk Steadfast: the new open and the show's shape

For Aaron. Written 2026-10-03, midday CT, and revised the same afternoon after the Opus 5.5 review landed (`research/opus55/opus55-review.md`, merged in section 7 below). The full research with sources is in `research/TOP-PODCAST-STRUCTURES.md`. The rules live in `SHOW-BIBLE.md` (v3, sections 4d, 5, 13, 14 and 15).

**Where this stands.**
- **Applied.** The new open for E001-E080, now with the Opus line edits I accepted (all 27 Fix rows and most of the rest), and the spoken credit for E001-E080. All 104 opens pass lint with 0 FAIL and 0 WARN, including a new check that catches an open retelling the cold open. Run times barely moved (E020 is 15:56).
- **Drafted, pending you.** Opens for E081-E104, from the Opus appendix, marked DRAFT in `_build/intros_data.py`. No E081 or later scripts were written. The E001 body pickups (five Wes lines) are drafted in `episodes/E001/QA.md` and not yet in the script.
- **Proposed only.** The clock for E081 on, the season payoff map and a ranked list of light fixes to E001-E080. No episode body was rewritten.

## What I need from you

Most of these are a yes or a no.

1. **The E001 open** (section 3). Yes or no. It blocks the E001 re-record.
2. **The E001 body pickups** (section 7). Five Wes lines that change in the same session. Yes or no.
3. **Keep "This is Walk Steadfast." as the fixed first line?** Opus and I both say yes.
4. **Keep the open lengths** (mains 42-62 words, Field Notes 32-52, E001 60-75)? Opus and I both say yes.
5. **Jonathon's surname is Reese**, for the About page only? Yes or no. On air he stays "Jonathon".
6. **Shorts descriptions carry the disclosure line?** Yes or no. You named only the episode notes and the show description.
7. **Approve the show description draft** in `launch-kit/SHOW-DESCRIPTION.md`? Yes or no.
8. **Is the cold open still required on mains?** Yes keeps it on every main. No makes it optional. 34 of 80 run past 15 seconds today.
9. **Adopt the clock (section 5) for E081 on?** Yes or no.
10. **Which E001-E080 fixes to apply.** Ranked list in section 5. The first is the "coming" sweep, which is ready to run.
11. **Approve the E081-E104 draft opens?** Yes or no.
12. **The four book slots on fresh topics** (E081, E093, E095, E099). Use the suggested chapter links, or drop them? Details in section 6.
13. **The continuity fixes Opus found** (section 6). Apply all, or pick?

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

**How it stays fresh.** A checker (`_build/intro_lint.py`) runs with every lint. It fails any open that reuses a run of five or six words from a nearby episode, misses a beat, runs long, puts "my book" in Jonathon's mouth or breaks the writing rules. It also fails an open whose fact or hook retells the cold open or the first line after the slate. All 104 pass with no warnings.

**How it's built.** The words live in one file, `_build/intros_data.py`, and `_build/intro.py` writes them into the scripts. Changing a word is a one-line edit and a re-run, never hand surgery on 80 scripts. E081-E104 are in the same file as DRAFT entries, and the script tool marks them DRAFT when it writes them.

## 3. Five opens side by side

The retired standard intro, for comparison (variant A, 66 words, no "today" line). WES "This is Walk Steadfast. I'm Wes Hart. Twenty-something years at tables with men, and I wrote a book about what I heard." JONATHON "And I'm Jonathon. Husband, dad of two, sales manager, still learning." WES "Twice a week we talk straight about following Jesus as a man. At home, at work, with your friends." JONATHON "Steadfast is the book, a video training for men, and this table. It's all at walksteadfast.com."

These are the final texts after the Opus merge.

| Beat | E001, launch (Tue Jan 5) | E002, Field Notes (Fri Jan 8) | E013, main (Tue Feb 16) | E040, Field Notes (Fri May 21) | E079, main (Tue Oct 5) |
|---|---|---|---|---|---|
| Anchor and lead | WES "This is Walk Steadfast. I'm Wes Hart. I've sat at tables with men for twenty-some years." | JONATHON "This is Walk Steadfast. I'm Jonathon. My wife works nights." | JONATHON "This is Walk Steadfast. I'm Jonathon. I run a regional sales team." | JONATHON "This is Walk Steadfast. I'm Jonathon. I manage commercial air conditioning sales." | JONATHON "This is Walk Steadfast. I'm Jonathon. I've sat across from Wes most Thursdays for years." |
| The other man | JONATHON "I'm Jonathon. I came to faith at twenty-nine, the year I met Wes." | WES "I'm Wes Hart. Married twenty-seven years." | WES "I'm Wes Hart. I went to my mother's doctor appointment last week." | WES "I'm Wes Hart. I'm better at asking men questions than answering them." | WES "I'm Wes Hart. The mug in front of me was Mr. Abernathy's." |
| What the show is | WES "Starting today, twice a week, we talk straight about following Jesus as a man." | JONATHON "Tuesday we give one challenge and take it ourselves. Friday we report." | JONATHON "We talk plainly about following Jesus as a man. Tuesdays long, Fridays the report." | JONATHON "Friday we report." (shares a line with the offer) | JONATHON "Twice a week, following Jesus as a man, hard weeks too." (shares a line with the offer) |
| The offer | JONATHON "Wes wrote a book called Steadfast Men, and a video training goes with it. Both are at walksteadfast.com." | WES "My book and the video training are both at walksteadfast.com." | WES "My book and the video training go with this show. walksteadfast.com." | "Steadfast Men, the book, and the video training live at walksteadfast.com." | "Find the book and the Steadfast video training at walksteadfast.com." |
| The hook | WES "Today we ask why good intentions don't make it to Tuesday." | JONATHON "Today a man asks where to start if he's never been the spiritual one." | JONATHON "Today we look hard at the prizes men work for." | WES "Today we ask what you do when the answer is no." | WES "Today we talk about where men put a loss." |
| Slate | JONATHON "Episode one." WES "Tuesday, January fifth, twenty twenty-seven." JONATHON "The Man You Keep Saying You'll Be." | WES "Episode two. Friday, January eighth." JONATHON "Field Notes. The First Check." | WES "Episode thirteen." JONATHON "Tuesday, February sixteenth." WES "The Prize That's Gone by Thursday." | JONATHON "Episode forty. Friday, May twenty-first." WES "Field Notes. The Ask Report." | JONATHON "Episode seventy-nine." WES "Tuesday, October fifth." JONATHON "Grief at the Table." |
| Words in the open | 72 (about 30 s) | 52 | 59 | 49 | 57 |

**What changed from this morning.** E001's second line now ties Jonathon's faith to Wes ("the year I met Wes"), and its hook is one sentence aimed at the question instead of a two-beat trailer line. E013 and E079 got fresher facts in place of a tic ("twenty years" of breakfasts) and a book line sitting in the fact slot. E002's hook got a verb and a man in it.

## 4. The disclosure, as you locked it

"Produced with AI voice and video tools." is one spoken line in the credits. After the closing music, Wes reads it at normal credits volume, like a producer credit, with no gap and no ducking. It is also a plain sentence at the end of every episode's notes and in the show description. It appears nowhere else. Lint fails any other AI mention, a changed word, a second copy or a missing credit. The credit is in E001-E080, the templates, the E001 notes and description, and the E001 re-record notes.

## 5. Episode architecture

**Applied now.** The open (about 18-24 seconds on mains) and the closing music and credits (about 6 seconds). Everything else in the episodes is as written.

**Proposed for E081 on (SHOW-BIBLE 4d), with the Opus notes folded in.** A Tuesday main, about 26 minutes.

| Clock | Segment | Why |
|---|---|---|
| 0:00-0:15 | Cold open, then the sting | The best exchange, short. 34 of the 80 cold opens run past 15 seconds now (21 mains, 13 Field Notes). This is the cheapest time in the episode. |
| 0:18-0:46 | Open and slate | Applied. |
| 0:46-2:10 | Pull up a chair | The question said out loud by about 2:10. Today the first story starts after 2:30 in 24 of 40 mains, and as late as 5:51. |
| 2:10-7:20 | First story | No fixed turn times. The one rule is no six minutes without a turn. A close story wins the clock. |
| 7:20-10:10 | The Word | The first payoff, by about 10:00 as a target, not a gate. It starts after 10:10 in 15 of the 38 mains that have a Word chapter now. |
| about 10:10 | Subscribe | Right after the Word, with the twice-a-week fact for a man who just found us. It sits after 13:00 in 19 mains now. |
| 10:10-18:00 | Pushback | The calendar's plug, when there is one, lands at 14:00-15:30, two minutes clear of the subscribe line. In 17 mains they sit back to back now. |
| 18:00-24:30 | What I actually did, the challenge, Carry This | From E081 on, the challenge is one move, plus a married and a single version when it's a household move. |
| end | Outro, closing music, credits | |

**A Friday Field Notes, about 14 minutes.** The report starts by 1:15, and a miss is on the table by 3:30. At about 6:30, one clause catches up a late listener, written as content ("Tuesday's challenge was to call one man before Thursday"), not as "If you're just joining." Then From the Table, the tool and a short outro. There's still no subscribe line on Fridays.

**The audit, corrected.** Opus recounted the structure audit, and two of my numbers were off. The Word starts after 10:10 in 15 of 38 mains, not 16 of 40 (E027 has no Word chapter). Of the 14 chapters over six minutes, 9 are Check the Box, not 11, plus 3 Pushbacks (E009, E011, E077) and 2 From the Tables (E014, E048), and 12 of the 14 sit in E002-E030. Only E005 is under its length floor. E038 is inside the Field Notes range. The other counts held.

**Light fixes to E001-E080, ranked. None applied to bodies.**
1. **The "coming" sweep.** 31 lines in 22 scripts still say the book or training is "coming" or "comes out this week", 15 of them spoken. Opus found two episodes. The tool is ready (`_build/tense_sweep.py`, dry run in `research/_work/coming-sweep-dryrun.txt`), and it needs only your yes.
2. **The E001 pickups**, with the open re-record (section 7).
3. **The 27 Fix rows of the Opus line edit.** Already applied, opens only.
4. **E058's silent cold open.** About 6 seconds of room tone on the audio feed. Add one audible beat, or move the bit after the slate.
5. **Plug and subscribe at least two minutes apart** in the 17 mains. Usually the plug moves one exchange later in Pushback.
6. **"This is Field Notes" said twice** in 13 Field Notes (E004-E028). Drop the repeat after the slate.
7. **Cold opens over 15 seconds.** The 21 mains first, the 13 Field Notes after.
8. **The 14 six-minute chapters.** Add a turn where a card or a hard question already sits nearby. Mostly leave them.
9. **E005's length.** Leave it. It's 19 seconds short.

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
- **Wes and his wife praying out loud.** Still no in March, still no in July. A small first in E091's week, reported in two sentences in E092, with no bow on it.
- **Wes's October.** His dad's anniversary (one line on the tailgate in E082) and his work review (told once in E085).
- **The men around the table.** Merle's quartet, Virgil and Ruby's Saturdays, the man in the truck, the Austin manager, the 24-year-old and the nephew. The plan has Merle's quartet singing Christmas hymns at the nursing home in Simeon week.
- **The small running jokes.** The Bluebonnets, Ruby's dog Pancake ("Yet."), and Wes's "K" texts.
- **Bookends.** In January each man writes the sentence he's been living. In the last week of December those sentences get read back. The year ends by handing off the first challenge of 2028, not with a summary.

**The payoff map for E081-E104.** Opus counted eleven planned payoffs and seven dropped threads for 24 episodes, so it gave each episode one main payoff at most and one small line. The full table is in SHOW-BIBLE section 15. In short, E082 Wes's dad, E085 the review, E086 and E094 season reviews, E087 and E099 Virgil, E088 the youngest's day, E091 and E092 the prayer, E093 Wes's mother at Thanksgiving, E097 and E098 the degree printout, E101 Merle's quartet, E102 Dani's Christmas service, E103 the January sentences and the ledger read by the four marks, E104 the first challenge of 2028.

**Two promises with an October deadline.** Both were made on air, and nothing planned them until now.
- **The youngest's day at the barn** (E051). "A Saturday in October, after the first cold front." It lands Sat Oct 30 and gets reported in E088 (Fri Nov 5).
- **The installer lunch** (E077-E078). Jonathon buys him lunch before the end of October. Booked in E083 (Tue Oct 19), reported in E086 (Fri Oct 29).

**Other threads that now have a home.** The coach letter (one line in E089), the friend's treatments (E090, and an honest line in E100), Wes's mother's move (settled before E093), Pancake's arrival (one line in E084) and the degree printout. Wes said he won't give it unless she asks, so she asks in E097 and he hands it over with no bow. E098 has what she says, only if she wants it told.

**The ledger.** Kept as a table in the bible. In E103 it's read back by the four marks, one line per mark per man, never the full list of 52.

**Cautions.** E094 is overloaded (Black Friday, a season review and a Christmas From the Table in one Field Notes), so the review gets three minutes. E104 ends on the first challenge of 2028, not on the review.

**Book slots on fresh topics.** E081, E093, E095 and E099 carry a book slot, but the calendar says fresh topics carry no plug unless the chapter link is real. Suggested links are chapter 32 for E081 (or move the slot, since a plug sits badly on the depression episode with 988 in it), chapter 6 for E093, chapter 4 for E095 and chapter 30 for E099.

**Continuity Opus found, none applied.** E057's granddad (make him the maternal grandfather, since E079's died in 2014). E063's row puts the casserole on Sat Jul 31, but the diagnosis is Thu Aug 5 and the body says Saturday, so the row should read Sat Aug 7. E075's "kindergarten next August" needs one line saying they held Theo a year. E101's calendar row calls Simeon "the old man," which Luke 2 doesn't say. E065's welcome line repeats the hook's words. The nephew lives in Houston but comes to Sunday lunch weekly, which may be fine since Pasadena is next door. Pin Wes's birthday and wedding date, or stop counting "twenty-seven years".

## 7. The Opus 5.5 review, merged

Opus 5.5 (effort high) reviewed the open system, all 80 opens, the clock and the season, then critiqued its own draft and revised it. I judged each recommendation on its merits against the scripts and the continuity rows. Where its section 7 revised an earlier draft, the revision is what I weighed.

**Accepted.**
- **The open system as it stands.** Keep the anchor, the five beats, the windows and the offer line in every open. Its case is that on audio the anchor is the only thing that names the show, and the fixed beats already cost about 38 words before any fact, so a 40-word floor would leave no room for the facts. I agree.
- **The E001 open**, word for word, with the section 2 recording notes.
- **The line edit.** 71 rows (27 Fix, 33 Improve, 10 Polish, 1 Check). I applied all 27 Fix rows and the large majority of the rest, using the section 7 revisions for E010, E032 and E068. Every changed fact was checked against the continuity row it leans on (for example E010's PT and mortgage, E024's ham, E063's casserole, E076's sixty-one-year-old rep, E079's mug).
- **The E081-E104 opens** from its appendix, as drafts pending you.
- **Three lint changes.** The hook is measured on its whole line, the docstring's false claim about "Steadfast" is gone, and a new check catches an open that retells the cold open (details below).
- **Delete the calendar's "Say 'coming'" rule.** Done. CALENDAR-104 now carries the present-tense rule from SHOW-BIBLE 8a.
- **The E001 line 398 problem.** Wes promises "Not every week," and every open names the book. The new line is below.
- **The clock notes** (no fixed turn times, the Word as a target, the Field Notes clause as content), the one-move challenge, the payoff map, the ledger by the four marks, the season-review cautions and the continuity list. All are in the bible as proposals for you.
- **The corrected audit counts.**

**Rejected or changed, and why.**
- **E046, Wes's fact** ("My older brother called me twice this week"). It spends the body's reveal ("That's twice in one week"). Now "I'm Wes Hart. At home, I finish other people's sentences.", which is E046 canon.
- **E052, Wes's fact.** It repeated the card line Opus had just given E050. Now "I'm Wes Hart. My wife says I rush the end." (E052 canon). I also kept "Today a young man asks what freedom means to a Christian." over its section 7 hook, because the man asking is the 22-year-old nephew, and "young man" already breaks the "Today a man asks" stem it was worried about.
- **E061, Wes's fact** ("keeps a letter in a shoebox"). A fact error. The shoebox is his mother's (E036). Now "I once wrote my wife a three-page letter."
- **E065, Jonathon's fact** ("Dani knows my whole story"). Nothing in the canon says so, and it lands hard on the marriage-bed episode. Now "I used to hold a grudge against Dani's schedule."
- **E066, the Check row.** The current hook already matches the script's From the Table (a divorced dad, "who goes first"). No change.
- **E076's hook** ("twenty years older or younger"). The script's question is about a man about sixty years older. Now "Today a young man asks how to reach a man sixty years older."
- **E078, Jonathon's fact.** "Last week" may not hold against the dates in the row, so "last" was dropped. Now "My company just cut a man I hired."
- **The "coming" scope.** Opus said E001 and E079. It's 22 scripts and 31 lines, plus the E001 launch-kit notes and the episode template. I fixed the notes and the template (text only) and left the script lines for your yes.
- **The retell threshold.** Opus proposed flagging three shared content words. Run on the original 80 opens, a three-word check flags only 3 episodes, though Opus itself counted 16 retells among its 27 Fix rows. A two-word check on the fact lines and the hook flags 12. So a fact line or hook now fails at two shared words with the cold open or the first line after the slate, any line fails at three, and one rare shared word warns. Eight word pairs I read by hand are on an allow list. The tighter check caught nine more opens, some of them Opus rows, and I rewrote those (E044, E049, E053, E055, E058, E061, E071, E073, E074).
- **E001's timing.** Opus put the open at about 27.9 seconds. On the show's script clock (Wes 145 words a minute, Jonathon 170, 0.45 seconds a line) it's about 30 seconds, still inside the E001 window.
- **E001 line 422.** Opus kept "If you want to know what's there, that's where you check." I shortened it to "That's the one place to check."

**The E001 pickups.** Record these with the open in one pass (full notes in `episodes/E001/QA.md`). The script body still has the old lines until you say yes.

| Line | Old | New |
|---|---|---|
| 148 | This is Jonathon. He's thirty-seven. He grew up in Pasadena, Texas. | This is Jonathon. He's thirty-six, thirty-seven in February. He grew up in Pasadena, Texas. |
| 398 | ...After today, you'll hear about the book or the training every now and then, when it actually fits what we're talking about. Not every week. That's a promise. | ...After today, you'll hear them named once near the top, in one line. Past that, only when it actually fits what we're talking about. That's a promise. |
| 404 | I wrote it, and it's coming. | I wrote it. |
| 422 | walksteadfast.com. The book, the training when it's out, and every episode of this show. If you want to know what's real and what's coming, that's where you check. | walksteadfast.com. The book, the training, and every episode of this show. That's the one place to check. |
| 471 | And everything else is at walksteadfast.com. The book, the training when it's out, and every episode. | And everything else is at walksteadfast.com. The book, the training, and every episode. |

Jonathon's age follows E080, which puts his birthday in February. He is 36 on Jan 5, and 37 in E025, E034 and E057. The E001 notes, description and show notes now say 36, and so does his host brief.

**The new lint check, in one paragraph.** `_build/retell.py` pulls each script's cold open and the first line after the slate, strips them to content words, and compares them with the open. Episodes without a script yet (E081-E104) skip it, so each draft gets checked when its script exists. All 104 opens now pass with 0 FAIL and 0 WARN. Mains average 56.2 words and Field Notes 48.7.

## 8. Files

| What | Where |
|---|---|
| Research with sources | `research/TOP-PODCAST-STRUCTURES.md` |
| Rules (open system, credits, proposed clock, season map, decisions) | `SHOW-BIBLE.md` v3 |
| All 104 opens (E081-E104 DRAFT) | `_build/intros_data.py` (written into the scripts by `_build/intro.py`) |
| Open checker and retell check | `_build/intro_lint.py` and `_build/retell.py` (run by `_build/lint.sh`) |
| "Coming" sweep, dry run by default | `_build/tense_sweep.py`, output in `research/_work/coming-sweep-dryrun.txt` |
| Credits tool | `_build/credits.py` |
| Structure audit (read only) | `_build/structure_audit.py`, output in `research/_work/structure-audit.md` |
| E001 re-record notes | `episodes/E001/QA.md` |
| Grok critique of the first draft (Grok, not Opus) | `research/_work/grok47-critique.md` |
| Opus 5.5 review, raw | `research/opus55/opus55-review.md` |
| Pre-merge backups | `research/_work/pre-opus-merge/`, `research/_work/*.pre-opus.py`, `research/_work/scripts-pre-opus-merge.tgz` |
