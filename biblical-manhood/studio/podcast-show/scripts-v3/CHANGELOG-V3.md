# Batch e001-e008.md

# CHANGELOG-V3: final scripts, E001-E008

Internal. The v3 folder holds the final scripts for E001-E008. They are rewrites of the first drafts in `scripts/`, which stay untouched. Aaron's direction for v3: drill deeper into the canon topics, and give the two hosts more banter, chemistry, real disagreement, stories, callbacks and running threads.

## Length windows overridden

v3 scripts run longer than the show bible allows, on purpose. These lines in `SHOW-BIBLE.md` do not apply to `scripts-v3/`:

| Where | What it says | v3 target |
|---|---|---|
| Section 2, line 37 | "Every episode is tight, 25-35 minutes" | Mains 45-60 min, Field Notes 20-25 min |
| 4a, line 56 | Main episode 25-35 minutes, about 3,600-5,000 spoken words | 45-60 min, about 7,000-9,000 words |
| 4b, line 75 | Field Notes 12-16 minutes, about 1,900-2,500 words | 20-25 min, about 3,000-3,800 words |
| 4c, line 90 | E001 launch episode about 40-45 minutes | Same as any main: 45-60 min |
| Line 260 | "Plan mains for 3,700+ spoken words" | Plan mains for 7,000+ |
| Line 333 | "Field Notes run 13:50-14:30" | Field Notes run 20:00-25:00 |

Timing is still estimated by `_build/timing.py` at 145 wpm for Wes and 170 for Jonathon, and chapter stamps come from `_build/apply_chapters.py`. Nothing in `_build/` was changed. `lint.sh` has no length check, so the overrides needed no tooling change. The bible itself is unedited. If v3 becomes the house length, update those six lines.

## Rules added for v3

- Jonathon carries 35-50% of the spoken words. Under 20% of his lines are under 12 words. No Wes turn runs past about 120 words without a handoff.
- In every main, Jonathon pushes back for real at least once and brings two stories of his own.
- Jonathon sounds like a sales manager from the Houston suburbs, never country.
- At most one on-mic reference to the show per episode.
- No phrase reused across the batch, except deliberate callbacks named on air and the fixed lines (the open, the slate, the standing outros, the credits).

## Deliberate continuity changes from v1

These are the places where v3 departs from a first-draft fact. Everything else in v1 holds, and each script's header lists what it adds.

- **The gutter is not fixed (E004 v3 onward).** v1 E004 has it fixed on Saturday. In v3 the two men find the fascia board behind it rotten ("That's a carpentry job, not a gutter job"). The carpenter's name goes on a sticky note on the fridge (E005). Wes's wife writes "CALL" on it in red (E006). Jonathon connects it to Wes's knees, and Wes defers ("That's a different Friday," E008). This keeps canon with E014 (the gutter at 15 months) and E018. Wes's real reason (the knees, the ladder, not wanting to pay a man for something he could do at forty) is held for E014.
- **Mom's Tuesdays (E005 v3 onward).** Wes's wife has driven his mother to PT most Tuesdays since August, and Wes has done two. E002's first trip stands. This gives the older brother's "You've always let me handle Mom" something to land on in E007.
- **Mr. Abernathy's question (E001 and E007 v3).** His every-visit question stays "What'd you do since last time?" "What are you waiting on?" is the question he asked once, after Wes's dad died, and the one Wes borrowed for his first breakfast with Jonathon.
- **Jonathon's age.** He is thirty-six throughout. The v1 E003 line said 37. His birthday is in February.
- **The brothers.** The Christmas-money text in E005 goes to the little brother, so E007 can introduce both brothers fresh.
- **The tired man.** The question "How do I stop waiting when I'm genuinely tired?" comes up in E007's pushback and is handed to E008's From the table.
- **The visor card** reads "Win the room" (E003 and E005), so the late-order call in E005 lands.

## Mark ownership left for later episodes

The v3 scripts touch each mark without taking a later episode's job. E009 owns the boulder and the pack (Galatians 6:2 and 6:5). E011 owns going first and its misuse. E012 owns the first apology. E013 owns inheritance in depth. E014 owns the gutter. The steadfast sentence is said in full once per episode where it appears. Pay always means inheritance, never earning.

## Housekeeping

- Cross-batch phrase pass. Repeated tics were varied in later episodes: "on the record", "here's my problem with all of this", "I sat with a man a few years ago", "I can see it on your face", "I want to be careful, because", "Here's where I tell on myself", and "I want to push on it". On-air callbacks stay ("nine thousand notes", the cold plunge, the eggs in front of a waitress, "It's not done / not fixed. It's started.").
- The W01 training owns the driveway image, so E008's call happens "out by the barn". The W04 training owns the voicemail image, so E007 says "half a call".

# Batch e009-e016.md

# Podcast v3 changelog

Changes from the v1 scripts in scripts/ to the v3 rewrites in scripts-v3/, logged per batch. The v1 files are untouched.

## Batch E009-E016 (branch podcast-v3-e009-e016)

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides SHOW-BIBLE section 4a (mains 25 to 35 minutes, about 3,600 to 5,000 words), section 4b (Field Notes 12 to 16 minutes, about 1,900 to 2,500 words), the section 5 clock tables with their minute marks, and the line that puts Field Notes at 13:50 to 14:30. The minute marks no longer apply to v3, but the rule that no chapter runs six minutes without a turn still does.

| Episode | v1 length (header) | v3 length (timing.py) | Override |
|---|---|---|---|
| E009 The Weight With Your Name on It | about 26 min | 50:51 | 4a and the section 5 main clock |
| E010 Field Notes: Not Your Load | about 14 min | 23:05 | 4b and the section 5 Field Notes clock |
| E011 Somebody Has to Step Out Ahead | about 26 min | 48:55 | 4a and the section 5 main clock |
| E012 Field Notes: Valentine's, Ash Wednesday, and Going First | about 14 min | 22:05 | 4b and the section 5 Field Notes clock |
| E013 The Prize That's Gone by Thursday | about 26 min | 48:43 | 4a and the section 5 main clock |
| E014 Field Notes: What Stuck | about 15 min | 23:20 | 4b and the section 5 Field Notes clock |
| E015 The Part That's Mine | about 26 min | 48:03 | 4a and the section 5 main clock |
| E016 Field Notes: Inside Job | about 15 min | 22:34 | 4b and the section 5 Field Notes clock |

The extra time comes from added chapters, deeper work on each passage, hard cases (single, divorced, men with rough fathers, men who have failed), a story from each host, real push-back from Jonathon, and banter. Each header now reads "About N min (v3 length, see scripts-v3/CHANGELOG-V3.md)."

### Rule fixes applied in every script

- **"This week's challenge" is now "The challenge."** The chapter marker, the on-screen text, the spoken line, the YouTube chapter list and the description are all retitled. "This week" is gone from every spoken line and description.
- **Singular "you."** Every line aimed at the listener, new or carried over, speaks to one man.
- **No dashes** in any spoken line, description or narrative.
- **Plugs are present tense.** E009 (book, chapter five) said "The book's coming. It'll be at..."; v3 says it's at walksteadfast.com. E015 (training) said session fifteen "comes out this week"; v3 names it by title, "The Problem Inside," says it's at walksteadfast.com, and gives no session number or date. No other episode in this batch has a plug slot.
### 988 line on mental-health episodes

- **E009** carries the 988 line in "The man who can't" (the man who can't carry his own load). v1 had none.
- **E016** carries it, said by Jonathon in From the table, right after the "I'm worthless" line, and also in the description and the pinned comment. v1 held it for E021; the brief requires it here because the episode deals with self-blame and worthlessness.

### Episode-specific changes

- **E010.** The v1 outro and description promised a printable two-column list at walksteadfast.com that doesn't exist. v3 removes the claim; the tool is described in words only.
- **E012.** Timing fixed. v1 had Jonathon's mom texting Dani "Friday morning" in a Friday release; v3 has her text about an hour after Thursday's call. The coffee note is now Wednesday morning, with Dani's reply waiting that night, so it fits her shift pattern.
- **E013.** The brother text now follows the grab bar (installed Sat Feb 13), not the doctor appointment, because the brother was in the room at the appointment in E012. New chapters: The truck door, Keeping score at home, The text to my brother, and a hard case about a boss who takes the credit.
- **E014.** The back-porch gutter gets a date, Sat Feb 27 at 8 AM, which follows the host canon (son-in-law on the ladder, Wes three rungs up). The Valentine's-week season review and the canon sentence are said once.
- **E015.** The calendar's working title "The Problem Is Inside the House" becomes "The Part That's Mine." v1's phone-jail beat is replaced (E014 had already used it): Ruby now jails her grandpa's phone at Dani's parents' house.
- **E016.** v3 adds payoffs for E015's VP disagreement (Wes was right about asking the rep; he doesn't take the win), Wes's Thanksgiving apology to his older brother (the pecan pie), and Wes's oldest son's text ("Proud of the first text").

# Batch e017-e024.md

# Changelog, v3 scripts

Entries are per batch. Each batch adds its own section and leaves the others alone.

## E017-E024 (branch podcast-v3-e017-e024)

All eight episodes were rewritten from the first drafts in scripts/. The drafts are untouched. Nothing outside scripts-v3/ was edited.

### Length overrides

The v3 brief sets mains at 45 to 60 minutes and Field Notes at 20 to 25 minutes. That overrides the old lengths in SHOW-BIBLE.md ("Field Notes run 13:50-14:30. Mains run 25:00 or longer").

| Episode | Kind | Old length (scripts/, timing.py) | Old rule | v3 length | v3 words |
|---|---|---|---|---|---|
| E017 Skip the House, Run the Room | Main | 25:31 | Mains 25:00 or longer | 53:50 | 8,086 |
| E018 Field Notes, Which Shape Are You | Field Notes | 14:22 | Field Notes 13:50-14:30 | 23:07 | 3,463 |
| E019 What Your Anger Is Guarding | Main | 25:42 | Mains 25:00 or longer | 47:09 | 7,091 |
| E020 Field Notes, Cooling Off Without Checking Out | Field Notes | 15:55 | **16:00 or under** (research/opus55/BRIEF.md, CHANGELOG.md, SHOW-BIBLE.md) | 23:26 | 3,510 |
| E021 The Itch and the Drift | Main | 25:34 | Mains 25:00 or longer | 45:26 | 6,849 |
| E022 Field Notes, Drift Check | Field Notes | 13:36 | Field Notes 13:50-14:30 | 22:57 | 3,437 |
| E023 Two Gardens | Main | 26:06 | Mains 25:00 or longer | 45:39 | 6,852 |
| E024 Field Notes, Good Friday | Field Notes | 14:29 | Field Notes 13:50-14:30 | 22:01 | 3,284 |

E020's cap of 16:00 or under is the one explicit per-episode cap in this batch, and it is overridden. The E020 file says so in its Format row and its production notes.

E021 and E023 land just over the 45-minute floor. Their word counts sit a little under 7,000 because Jonathon's share is high and he reads faster (170 wpm against Wes's 145). The minutes are what the brief measures.

### Plugs

- E021 (book, chapter 9) and E023 (training, session 19) said "coming" in the first drafts. Both are now present tense, with no dates, prices or "out now". E023 now says "You'll find it at walksteadfast.com."
- E017, E018, E019, E020, E022 and E024 carry no plug, as in the calendar.

### Mid-show subscribe

- In E021 and E023 the mid subscribe line moved ahead of the Word, so it sits more than two minutes from the plug.

### Show rules applied across the batch

- **"This week" and "weekend" removed.** These words are gone from the spoken lines, notes and chapter titles. The challenge chapter is now titled "The challenge", and every challenge reads "between now and Friday".
- **No inside baseball.** Lines about the show's own making are cut, and so are the "It's Field Notes" self-announcements. The AI disclosure appears only in the credits.
- **Dashes, colons and semicolons.** None are in spoken lines. Mid-sentence colons and semicolons are also removed from the published prose (descriptions, pinned comments, reading narratives), and "(Wes: X)" is now "(Wes, X)". Header tables, which are not published, keep their colons.
- **No forced threes.** In E020, the three-question test is cut to a two-question test.
- **The 988 line.** E021 (porn and addiction) is this batch's heavy-topic episode under SHOW-BIBLE section 13. It keeps the 988 line on mic and in the description, with SAMHSA in the description. E019 and E020 (anger) carry no 988 line, the same as in the first drafts.

### Episode fixes

- **E020.** The son's text now reads "foreman yelled. guarding? scared i'm not good at this." A spoken "Guarding:" became "Guarding?".
- **E022.** The porch count is fixed against the calendar to four of seven nights, Thursday Mar 11 through Wednesday Mar 17 (Thursday, Friday, Saturday and Monday). The missed nights are Sunday (forgot, then admitted he drifted), Tuesday (three videos) and Wednesday (his wife was at her sister's). Psalm 90:10 is paraphrased, not carded.
- **E023.** The rep story is dated to Jonathon's first year as a manager, nine years ago at 28, to match canon (Jonathon is 37). A slip of "weekend" in the Peter lines became "three days". Wes's "My nephew" is corrected to "Your nephew", because the nephew is Jonathon's.
- **E024.**
  - The listener question is framed as one men commonly ask, not as a quoted letter.
  - The episode is named as the season 2 review (What You Inherited, E015-E024) and follows the SHOW-BIBLE season review rule.
  - The cold open is reworded so it shares no content words with the hook.
- **E019 and E021.** The climbing-gym hold is a jellybean in both.

### Repeats across the batch

Phrases repeated across E017-E024 were checked with a six-word window and about 35 were varied. What still repeats is meant to: callbacks ("What's it guarding?", "Forgot, or drifted?", "Moved twice? It's a tree."), scripture, quotes said again on purpose, and the challenge opener "Here's the challenge, between now and Friday."

# Batch e025-e032.md

# Podcast v3 changelog

Changes from the v1 scripts in scripts/ to the v3 rewrites in scripts-v3/, logged per batch. The v1 files are untouched.

## Batch E025-E032 (branch podcast-v3-e025-e032)

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides SHOW-BIBLE section 4a (mains 25 to 35 minutes, about 3,600 to 5,000 words), section 4b (Field Notes 12 to 16 minutes, about 1,900 to 2,500 words), and the section 5 clock tables (main about 26 minutes, Field Notes about 14 minutes, with their minute marks for the report, From the Table and the tool). Those minute marks no longer apply to the v3 scripts, but the rule that no chapter runs six minutes without a turn still does.

| Episode | v1 length (header) | v3 length (timing.py) | Override |
|---|---|---|---|
| E025 The Father Who Stays | about 27 min | 53:32 | 4a and the section 5 main clock |
| E026 Field Notes: Easter Week Report | about 15 min | 22:45 | 4b and the section 5 Field Notes clock |
| E027 The Empty Chair at Your Table | about 27 min | 49:24 | 4a and the section 5 main clock |
| E028 Field Notes: The Chair Report | about 15 min | 22:45 | 4b and the section 5 Field Notes clock |
| E029 When Your Dad Is Still Alive | about 28 min | 50:11 | 4a and the section 5 main clock |
| E030 Field Notes: Calling Him Back | about 14 min | 22:04 | 4b and the section 5 Field Notes clock |
| E031 When Home Never Handed You Off | about 26 min | 47:37 | 4a and the section 5 main clock |
| E032 Field Notes: Cutting the String | about 13 min | 22:10 | 4b and the section 5 Field Notes clock |

The extra time comes from added chapters, deeper work on each passage, stories from both hosts, real push-back from Jonathon, hard cases, and banter. No chapter is padding. Each episode's production notes list what was added under "v3 length."

### Rule fixes applied in every script

- **Plugs are present tense.** The v1 plug lines said a book chapter or training session was "coming" or "comes out this week." v3 says it's at walksteadfast.com, with no "coming," "out now," dates or prices. The YouTube descriptions match. Plugs appear only in E025 (book), E027 (book) and E031 (training session 11). E029 has none, and Field Notes never carry one.
- **"This week's challenge" is now "The challenge."** The chapter marker, the on-screen text and the spoken line are retitled. "This week" is gone from every spoken line except one locked open (see below). Descriptions and reading narratives say "The challenge" too.
- **The open stage note says "each episode."** v1 read "Same beats every week, new words." v3 reads "Same beats each episode, new words." That clears lint's legacy-intro check without the word "week."
- **Training is never called a "week."** Sessions are named by number and title (session 8, session 11).
- **"Weekend" is out of the scripts.** In E031 the canon line "And don't come home every weekend" is now "And don't come home every Friday." Flagged in the batch report.
- **No date in the open or the reading-narrative subtitle.** The v1 reading narratives carried a date under the episode title, and v3 drops it. Release dates stay in the header table, which isn't read on air.
- **The credits line appears only in the credits slot,** exactly "Produced with AI voice and video tools." There's no other AI mention anywhere.
- **YouTube chapter timestamps** come from _build/timing.py on the v3 text.

### Locked text left as is

- **E032's open** (from _build/intros_data.py) says "Friday we report, two parts this week." Opens are locked, so it stays verbatim. Aaron decides whether to change it in intros_data.py.
- **E029's open** says "Twice a week, following Jesus as a man." That's the show's schedule, not a training reference, and lint passes it.

# Batch e033-e040.md

# CHANGELOG, v3 rewrites (batch E033-E040)

Rewrites of the first drafts in scripts/. The originals are untouched. Each v3 file keeps the same slug.

## Length overrides

The first drafts ran about 25 minutes for mains and 13-14 minutes for Field Notes. Each v3 file overrides its draft's Format length with the v3 brief's ranges: mains run 45-60 minutes (about 7,000-9,000 words), and Field Notes run 20-25 minutes (about 3,000-3,800 words).

| Episode | Draft length | v3 length | Spoken words | timing.py |
|---|---|---|---|---|
| E033 Leave Without Slamming the Door | about 25 min | about 54 min | 8,220 | 54:38 |
| E034 Field Notes: The Door Report | about 13 min | about 23 min | 3,527 | 23:41 |
| E035 Your Mom: Mother's Day and Being a Grown Man | about 26 min | about 49 min | 7,385 | 49:11 |
| E036 Field Notes: Mother's Day Field Notes | about 13 min | about 25 min | 3,738 | 24:55 |
| E037 A Man With No Brothers | about 25 min | about 49 min | 7,292 | 48:32 |
| E038 Field Notes: Season Review: The Father Who Stays | about 13-14 min | about 22 min | 3,379 | 22:27 |
| E039 Ask the Man | about 25 min | about 47 min | 7,057 | 46:58 |
| E040 Field Notes: The Ask Report | about 13-14 min | about 23 min | 3,540 | 23:34 |

The added length is new material: stories, real disagreements and callbacks. It isn't padding. Each header's "New in v3" note lists what was added.

## Other changes from the drafts

- **E039 plug, present tense.** The draft's training plug used future and premiere framing. The v3 plug reads: "Steadfast is twenty-four video sessions, built for a man on his own or a table of men. Session fourteen is Ask the Man... It's at walksteadfast.com." The YouTube description plug was changed to match.
- **Chapter rename.** "This week's challenge" became "The challenge" in every main, and the on-screen text became "Tuesday's challenge."
- **"this week" removals.** Every spoken "this week" in the drafts was rewritten ("before Friday," "Tuesday," "these few days"). The one exception is below.
- **Intro "this week" lines kept and flagged.** Two intros_data.py lines are kept word for word because the brief requires the intro verbatim:
  - E035: JONATHON "I'm Jonathon. My mom raised me alone, so this week matters."
  - E037: WES "Today we find out who'd know if you fell this week."
  If Aaron wants these gone, the fix belongs in _build/intros_data.py, not the scripts.
- **"weekend" removals.** These were removed in E036, E037, E038 and E040 (for example, "Some men need the weekend" became "Some men need a night").
- **Number motifs removed.** Removed lines: the "eleven dollars" coin joke (E035), the "twelve years" joke (E036), "Jesus picked twelve," which became "a handful" (E037), and "about twelve," which became "about ten" (E039). The lint INFO count for eleven and twelve is 0 in all eight.
- **"mentor" removed (E039, E040).** Chapter 14 tells you not to lead with the word, so it's out of the scripts, titles, descriptions and hashtags. #Mentoring became #Brotherhood (E039) and #Fatherhood (E040).
- **Kolaches (E037).** The men's breakfast "donuts" became kolaches, to avoid the donut beat already used in E033.
- **E040 Shane beat dropped.** The draft's Shane's-garage rivet report moved into E039 v3 (the railing). E040 replaces it with Dani's fridge rehearsal and Wes's own old no.
- **Cross-batch phrase repeats.** After drafting, a seven-word repeat scan across E033-E040 removed eleven accidental repeats. The repeats that remain are deliberate callbacks: Dad's "Drive careful" and the barn, the coffee can, the screen door "she went inside through," "We never once went to school hungry," "If I fell down tomorrow," "something embarrassing," the E039 challenge restated in E040, and the standing "turns his mug a quarter turn."

# Batch e041-e048.md

# CHANGELOG, v3 rewrites (batch E041-E048)

These are rewrites of the first drafts in scripts/. The originals are untouched, and each v3 file keeps the same slug.

## Length overrides

The first drafts ran about 25 minutes for mains and 13-14 minutes for Field Notes, which matched the show bible's older caps. Each v3 file overrides its draft's Format length with the v3 brief's ranges. Mains run 45-60 minutes (about 7,000-9,000 words). Field Notes run 20-25 minutes (about 3,000-3,800 words).

| Episode | Draft length | v3 length | Spoken words | timing.py |
|---|---|---|---|---|
| E041 These Men Are My Brothers | about 25 min | about 55 min | 8,407 | 55:46 |
| E042 Field Notes: Memorial Day | about 13-14 min | about 21 min | 3,272 | 21:47 |
| E043 No Fixed Star | about 25 min | about 47 min | 7,184 | 47:38 |
| E044 Field Notes: Finding North | about 13-14 min | about 22 min | 3,328 | 22:13 |
| E045 Your Daughter Is Watching | about 25-26 min | about 52 min | 7,932 | 52:31 |
| E046 Field Notes: The Daddy-Daughter Report | about 13-14 min | about 23 min | 3,547 | 23:34 |
| E047 Give Your Son a Name | about 25-26 min | about 46 min | 7,035 | 46:36 |
| E048 Field Notes: Father's Day When It's Complicated | about 13-14 min | about 23 min | 3,461 | 22:59 |

The added length is new material: stories, real disagreements and callbacks. Each header's "New in v3" note lists what was added.

## Other changes from the drafts

- **Canon fixes.**
  - E041: the draft had Jonathon's father "in the house... in the recliner," which contradicts canon, because his father left when he was nine. The v3 pushback is rebuilt on the real fact.
  - E041: the Austin "Did you eat?" / "K." exchange is now one text, not two, to match the dates.
  - E043: the draft dated Jonathon's Shane call Wed May 26, but E042 (May 28) reports it as missed. It moves to Mon May 31.
  - E046: "my brother taught me the tractor" conflicted with E043 (his granddad taught him), so it was cut.
  - E047: "since your graduation" contradicted E030 (Wes said "I'm proud of you" to his oldest on Apr 15). The phone call is now the second time.
  - E047: the draft credited "Who died?" to Wes's brother. It's Jonathon's father's line (E030).
- **Wes's job stays unnamed.** A v3 line in E045 had him talking about quota, and it was cut.
- **Plug tense.**
  - E045's plug now reads "If you want it on paper, it's at walksteadfast.com."
  - E047's training plug names one session by number and title, in the present tense ("The closest is session ten, The Father Who Does Not Leave").
  - Future-tense wording was also removed from the production notes, where lint was catching it.
- **"this week," "weekend" and "Week two" removals.** Every spoken instance in the drafts was rewritten, along with chapter names and on-screen text. The "Same beats every week" stage note in the intros became "every episode." The two exceptions are locked intro lines, listed below.
- **Locked intro lines kept and flagged.** These lines are kept word for word because the brief requires the intro verbatim:
  - E042: JONATHON "This is Walk Steadfast, Memorial Day weekend."
  - E047: WES "...this week as fathers of boys."

  The fix belongs in _build/intros_data.py.
- **E047 scripture.** Isaiah 43:1 is carded as its dash-free second half, exact. The first half (Jacob and Israel) is described in Wes's words.
- **Mic share.** E045 and E046 ran over 55% Jonathon in early v3 passes. Listener answers and tool narration moved to Wes until both were under 50%.
- **Cross-batch phrase repeats.** After drafting, a seven-word repeat scan across E041-E048 found about twenty accidental repeats, and all of them were rewritten. Examples:
  - two listener cases that both opened "Nineteen, single"
  - "I've been sitting on it since"
  - "That's it? That's the whole answer?"
  - "in the truck in a parking lot"
  - "looked at me like I'd..."
  - the married-guys "Sit with it a day" wording

  The repeats that remain are deliberate:
  - the standing "turns his mug a quarter turn," outros and credits
  - each Friday's restatement of Tuesday's challenge
  - Ruby's "What do you think about when you're by yourself?" (E045 to E046)
  - Wes's one-sentence heading (E043 to E044)
  - the sticky note "Be nice to Theo most of the time"
  - the safety-hotline rail
- **One "not only."** E043's "not only one you don't" was rewritten ("along with the one you don't"). It wasn't the banned construction, but it was close enough to be worth removing.

# Batch e049-e056.md

# Podcast v3 changelog

Overrides and deliberate departures from SHOW-BIBLE.md and the v1 drafts in scripts/, logged per Aaron's v3 brief. The v1 files, SHOW-BIBLE.md and _build/intros_data.py are not edited. Each batch adds its own section.

## Batch E049-E056 (branch podcast-v3-e049-e056)

### Length overrides

SHOW-BIBLE section 4a sets mains at 25-35 minutes (about 3,600-5,000 spoken words), and section 4b sets Field Notes at about 14 minutes. The v3 brief replaces both windows. Every episode in this batch runs past the old limit on purpose. The bible's chapter clock is scaled to the longer run, and the order of the beats is unchanged.

| Episode | Old window | v1 length (timing.py) | v3 length (timing.py) | Spoken words |
|---|---|---|---|---|
| E049 Give Your Son a Hill | 25-35 min | 25:35 | 53:43 | 8,100 |
| E050 Field Notes: The Hill Report | about 14 min | 13:52 | 22:59 | 3,441 |
| E051 A Day He Will Not Forget | 25-35 min | 25:28 | 46:39 | 6,980 |
| E052 Field Notes: Independence Day | about 14 min | 14:03 | 22:41 | 3,416 |
| E053 Before Anything Went Wrong | 25-35 min | 25:58 | 47:37 | 7,165 |
| E054 Field Notes: Work It and Keep It | about 14 min | 14:18 | 21:18 | 3,197 |
| E055 Some Saturdays | 25-35 min | 25:50 | 46:27 | 7,013 |
| E056 Field Notes: The Feeling Isn't the Fire | about 14 min | 14:16 | 20:51 | 3,118 |

E051 sits 20 words under the brief's "about 7,000" guide. Its time (46:39) is inside the 45-60 minute window, so it was not padded.

### Open lines reworded in the script only

Two opens in _build/intros_data.py carry calendar wording the brief keeps out of the scripts. The v3 script reads a reworded line. intros_data.py is not edited.

- **E052.** Jonathon's first line "This is Walk Steadfast on the holiday weekend." reads "This is Walk Steadfast, holiday edition." (The brief avoids "weekend.")
- **E053.** Wes's offer line "Through Labor Day, following Jesus as a man starts where you live." reads "All season, following Jesus as a man starts where you live." (The brief keeps dates out of the open.)

If Aaron wants intros_data.py to match, those are the two lines to change there.

### Chapter and wording changes across the batch

- **"This week's challenge" is now "The challenge"** (chapter title, description chapter list and spoken line) in E049, E051, E053 and E055, because of the "this week" ban.
- **Calendar words removed.** Every v1 "this week," "last week," "week one," "weekend" and "two weeks ago" in spoken lines, cards, pinned comments and descriptions is reworded (for example "last time," "Tuesday" or "before Friday"). The per-episode list is in each script's production notes. Training sessions are named by number or title only.
- **Mr. Abernathy's question (E053).** v1 had "What did you keep this week?" on mic, on the card and as a chapter title. v3 says "What did you keep?" everywhere. The question first aired in this episode's v1 draft, so no earlier canon changes.
- **Plug tense.** The v1 plugs in E051 (book, chapter 29), E053 (training, session eighteen) and E055 (training, session twenty) used "it's coming." All three are present tense ("It's at walksteadfast.com"), with no dates or prices.
- **Plug and sub-mid spacing.** SHOW-BIBLE section 4a lists E051, E053 and E055 among the mains whose plug sits within 30 seconds of the subscribe line. All three are separated in v3: the sub-mid sits before the Word and the plug after it, about two and a half minutes apart in E051, about five in E053 and about four and a half in E055.
- **E051 description verse.** The v1 YouTube description still named Joshua 4:6-7 after the 2026-10-03 swap. v3 names Psalm 78:4, matching the card.
- **E055 training plug** says "session twenty" without its title, because the title contains "vibe" (the episode was retitled "Some Saturdays" on 2026-10-03).
- **Standing outros** keep the rotation (E049 D, E051 E, E053 A, E055 B; E050 F1, E052 F2, E054 F3, E056 F4), each lightly reworded.

### Continuity fixes

- **Jonathon's start in sales.** v1 E053 said twenty-two. v3 says twenty-three, matching the Lorraine story in E049 v3 (first sales manager, Pasadena refinery accounts).
- **Jonathon's nephew** is twenty-two everywhere in the batch (one v3 working line said nineteen; fixed before commit).
- **Wes's flat stretches in E055** sit at "the Thursday table I sit at now," after Mr. Abernathy died, not at Mr. Abernathy's table during the fire decade.
- **"Where are we going?" in E055.** E043 gave Wes's answer as "I can do Saturday." E055 v1 gave "Home." v3 keeps both, in order: "Home," her correction, then "I can do Saturday."

# Batch e057-e064.md

# Podcast v3 changelog

Overrides and deliberate departures from SHOW-BIBLE.md and the v1 drafts in scripts/, logged per Aaron's v3 brief. The v1 files, SHOW-BIBLE.md and _build/intros_data.py are not edited. Each batch adds its own section.

## Batch E057-E064 (branch podcast-v3-e057-e064)

### Length overrides

SHOW-BIBLE section 4a sets mains at 25-35 minutes (about 3,600-5,000 spoken words), and section 4b sets Field Notes at about 14 minutes. The v3 brief replaces both windows. Every episode in this batch runs past the old limit on purpose. The bible's chapter clock (for example Pushback at 10:10-18:00, the plug at about 14:00-15:30, From the Table ending about 10:20) is scaled to the longer run. The order of the beats is unchanged.

| Episode | Old window | v3 length (timing.py) | Spoken words |
|---|---|---|---|
| E057 If There Is No Wife Yet | 25-35 min | 51:09 | 7,702 |
| E058 Field Notes: Not in the Lobby | about 14 min | 22:38 | 3,376 |
| E059 Know Her | 25-35 min | 47:03 | 7,069 |
| E060 Field Notes: Study Her | about 14 min | 21:48 | 3,258 |
| E061 Lay It Down | 25-35 min | 49:38 | 7,435 |
| E062 Field Notes: Laying It Down Report | about 14 min | 24:44 | 3,716 |
| E063 What She Actually Needs | 25-35 min | 50:17 | 7,562 |
| E064 Field Notes: Her Need, Not Mine | about 14 min | 22:59 | 3,442 |

### Open lines reworded in the script only

The brief bans "this week" in scripts. Two opens in _build/intros_data.py contain it, so the v3 script reads a reworded line. intros_data.py is not edited. Both rewordings pass the retell check (no two content words shared with the cold open or with the first line after the slate).

- **E060.** Wes's fact line "I asked my wife a follow-up question this week." reads "I asked my wife a follow-up question on the porch."
- **E061.** Jonathon's fact line "I'm a talker, which is the problem this week." reads "I'm a talker, which is the problem today."

E062's open line "I came in a different door all week." is read verbatim. It isn't the banned phrase, and lint passes it.

### Chapter and wording changes across the batch

- **"This week's challenge" is now "The challenge"** (chapter title, on-screen text and spoken line) in every main, because of the "this week" ban. Challenges say "before Friday," "between now and Tuesday" or "once a day."
- **Plug and sub-mid spacing.** SHOW-BIBLE section 4a lists E057 and E063 among the mains whose plug sits within 30 seconds of the subscribe line. Both are separated in v3. In E057 the sub-mid is about 19:00 and the book plug about 36:15. In E063 the book plug is about 25:10 and the sub-mid about 30:40, with The drawer between them.
- **Plug wording.** E057 (chapter 21) and E063 (chapter 24) use present tense and "my book": "It's called Steadfast Men, and it's at walksteadfast.com." The v1 E063 plug said "it's coming"; that word is gone.
- **Standing outros** keep the rotation (E057 C, E059 D, E061 E, E063 A; E058 F1, E060 F2, E062 F3, E064 F4), each with light rewording.

### Continuity fixes

- **E057, the dying grandfather.** SHOW-BIBLE section 14, item 18. The grandfather who said "You did all right, son." is Wes's **mother's father**. Wes names his paternal granddad (the place, ninety-one) on air separately, so the two men stay apart.
- **E058, the silent cold open.** SHOW-BIBLE section 14, item 15. v1 opened on a silent phone slide, which leaves about 6 seconds of room tone on the audio feed. v3 keeps the slide and adds two audible lines. It's still not a number or a quote (round 9).
- **E058, the tool.** v1's three-part tool is reshaped to two parts, to keep the batch off forced groups of three.
- **E059, the well.** The well in Proverbs 20:5's picture is on Wes's paternal granddad's place, not the E057 grandfather's.
- **E062, the day of the okra.** v1 put Wes forgetting the kitchen door, and the bowl of okra, on Thursday. E063 puts the friend's diagnosis on Thursday evening (he came in the kitchen door and went to the porch for two hours). v3 moves the okra to Wednesday, folds the sister's-knee news into the okra scene, and treats E062 as taped Thursday afternoon before Wes got home.
- **E063, the casserole date.** The v1 header put the casserole on Sat Jul 31. The script's own timeline (diagnosis Thursday, casserole "Saturday") makes it **Sat Aug 7**. v3 uses Aug 7.
- **E064, the no-text beat.** v1 had Jonathon type "Thinking about" and erase it, using a word from the v3 banned list. v3 says he "held the backspace down till it was gone."
- **E063, the verse.** The calendar's Philippians 2:4 was already E032's card. v3 keeps the v1 replacement, 1 Corinthians 10:24.

# Batch e065-e072.md

# Podcast v3 changelog

Overrides and deliberate departures from SHOW-BIBLE.md and the v1 drafts in scripts/, logged per Aaron's v3 brief. The v1 files, SHOW-BIBLE.md and _build/intros_data.py are not edited. Each batch adds its own section. Other batch branches create this same file, so when the branches merge, keep every batch section.

## Batch E065-E072 (branch podcast-v3-e065-e072)

### Length overrides

SHOW-BIBLE section 4a sets mains at 25-35 minutes (about 3,600-5,000 spoken words), and section 4b sets Field Notes at about 14 minutes. The v3 brief replaces both windows: mains run 45-60 minutes (7,000-9,000 words) and Field Notes run 20-25 minutes (3,000-3,800 words). Every episode in this batch runs past the old limit on purpose. The bible's chapter clock is scaled to the longer run, and the order of the beats is unchanged.

| Episode | Old window | v3 length (timing.py) | Spoken words |
|---|---|---|---|
| E065 The Bed Is a Covenant | 25-35 min | 48:48 | 7,407 |
| E066 Field Notes: Covenant Check | about 14 min | 24:57 | 3,761 |
| E067 When Marriage Feels Like Roommates | 25-35 min | 48:08 | 7,266 |
| E068 Field Notes: Roommates No More | about 14 min | 22:05 | 3,331 |
| E069 You Were Made for a Work | 25-35 min | 47:55 | 7,254 |
| E070 Field Notes: Labor Day | about 14 min | 23:59 | 3,630 |
| E071 What You Build When Nobody Claps | 25-35 min | 46:45 | 7,089 |
| E072 Field Notes: The Unseen Shift | about 14 min | 22:19 | 3,361 |

### Open line reworded in the script only

- **E072.** Jonathon's fact line in _build/intros_data.py is "I learned the school custodian's name this week." The brief bans "this week," so the v3 script reads "I learned the school custodian's name on Wednesday." intros_data.py is not edited. **Recommendation:** make the same change in intros_data.py so the rendered open matches the script.

The other seven opens are read verbatim from intros_data.py.

### Wording changes across the batch

- **"This week" and "weekend"** are gone from every spoken line, chapter title and on-screen text. Challenges say "before Friday," "between now and Tuesday" or name the day. "Labor Day week" (E069) is a holiday name, not the banned phrase, and lint passes it.
- **Plugs are present tense.** E069 (book chapter 30) and E071 (book chapter 33) said the book was "coming" in v1. Both now say it's at walksteadfast.com, and E071's description line drops "coming." E065 and E067 already used present tense.
- **Mid-sentence colons and dashes** are removed from spoken lines. The one colon lint sees in E066 is a clock time inside a text message read aloud ("Thursday, 7:20").
- **Handoffs.** Long Wes runs were broken with Jonathon questions and reactions so no Wes run passes about 120 words. The one exception is in E070 (134 words), where Wes reads his oldest son's text aloud; splitting a read-aloud text would break it.
- **Cross-episode repeats.** A scan of six-word phrases across the eight scripts turned up stacked repeats. The later uses were reworded in E067, E068, E069, E070, E071 and E072. The repeats left are intentional: the locked opens, the slate, the credits line, the standing chapter phrases and canon quotes used as callbacks.
- **Standing outros** keep the rotation: E065 B, E067 C, E069 D, E071 E; E066 F1, E068 F2, E070 F3, E072 F4.

### Single checks

SHOW-BIBLE "the single check" gives each Field Notes one text from a younger man. v1 did not have them in this stretch. Added in v3:

- **E066.** Wes's oldest son (the phone on the dresser, a man from the apprentice class).
- **E068.** Jonathon's nephew (the high-school friend he only texts about the Astros).
- **E070.** Wes's oldest son (a crew member's truck repossessed, the forty-minute drive the wrong way). The nephew rests.
- **E072.** Jonathon's nephew (staples behind the drywall, "the extra syrup boy").

### Continuity fixes

- **E065, welcome line** (SHOW-BIBLE section 14, item 18). The v1 welcome repeated the hook's words. The v3 first line after the slate shares no content word with the hook.
- **E071, Jonathon's age.** v1 had "I'm thirty-seven." He is 36 until his February birthday (SHOW-BIBLE, the facts), so the line is now "thirty-six."
- **Fact tics.** One recurring "twenty-seven years" count was cut, and a line that put Wes's father in his "seventies" now says "late" in life, so it can't contradict his age in the host file.
- **Wes's index card.** Any mention of the card respects canon: the back already holds his prayer names and his heading. E072's new secret list is a separate small notebook kept beside the card.

# Batch e073-e080.md

# Podcast v3 changelog

Changes from the v1 scripts in scripts/ to the v3 rewrites in scripts-v3/, logged per batch. The v1 files are untouched.

## Batch E073-E080 (branch podcast-v3-e073-e080)

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides SHOW-BIBLE section 4a (main length), section 4b (Field Notes length), and the section 5 clock tables with their minute marks for the report, From the Table and the tool. Those minute marks no longer apply to the v3 scripts, but the rule that no chapter runs six minutes without a turn still does. Each v1 header also carried its own length ("About 25-26 min" or "About 13-14 min"), and the v3 header now says "v3 length (45-60 min)" or "v3 length (20-25 min)."

| Episode | v1 length (header) | v3 length (timing.py) | Override |
|---|---|---|---|
| E073 Feelings Are the Dash, Not the Wheel | about 25-26 min | 53:02 | 4a, the section 5 main clock, the v1 header |
| E074 Field Notes: Dash and Wheel | about 13-14 min | 23:56 | 4b, the section 5 Field Notes clock, the v1 header |
| E075 Every Season Still Counts | about 25-26 min | 46:55 | 4a, the section 5 main clock, the v1 header |
| E076 Field Notes: Season Swap | about 13-14 min | 21:14 | 4b, the section 5 Field Notes clock, the v1 header |
| E077 When the Job Goes Away | about 25-26 min | 46:48 | 4a, the section 5 main clock, the v1 header |
| E078 Field Notes: Between Jobs | about 13-14 min | 24:28 | 4b, the section 5 Field Notes clock, the v1 header |
| E079 Grief at the Table | about 25-26 min | 46:41 | 4a, the section 5 main clock, the v1 header |
| E080 Field Notes: Grief Report | about 13-14 min | 22:30 | 4b, the section 5 Field Notes clock, the v1 header |

The extra time comes from added chapters, deeper work on each passage, stories from both hosts, real push-back from Jonathon, hard cases and banter. Each episode's "New continuity (v3 additions to v1)" header row lists what was added.

### Rule fixes applied in every script

- **Plugs are present tense.** E075's book plug (chapter 32) and E079's training plug (session 13, A Man With No Brothers) said "it's coming" in v1. v3 says each is at walksteadfast.com, with no "coming," dates or prices. The YouTube descriptions match. No other episode in the batch carries a plug, and Field Notes never do.
- **"This week's challenge" is now "The challenge."** The chapter marker, the on-screen text, the spoken line, the description and the reading narrative are all retitled. "This week" is gone from every script, and so is "week 1."
- **The open stage note says "each episode."** v1 read "Same beats every week, new words." v3 reads "Same beats each episode, new words."
- **Training is never called a "week."** Sessions are named by number and title.
- **No date in the reading-narrative subtitle.** v1 read "### Walk Steadfast, [date], Episode NN." v3 reads "### Walk Steadfast, Episode NN." Release dates stay in the header table, which isn't read on air.
- **The credits line appears only in the credits slot,** exactly "Produced with AI voice and video tools." There's no other AI mention anywhere.
- **Wardrobe matches production/WARDROBE.md.** The v1 headers for E074 through E080 listed shirts that differ from WARDROBE.md. v3 uses the WARDROBE.md entries, and each header names the source.
- **YouTube chapter timestamps** come from _build/timing.py on the v3 text, applied with _build/apply_chapters.py.

### Content changes beyond length

- **E073's divorced caller** was a dad at a custody drop-off in v1. That repeated E074's Austin, so v3 makes him a dad whose kids talk about their stepdad at supper.
- **E076 Mr. Abernathy order.** v3 has him go first, then leave the asking to Wes (the gas receipt and the nineteen days, canon E039). His saying is paraphrased, not quoted.
- **E077 scholarship.** Wes's father's A&M scholarship was already told on air in E029 and E053. v3 treats it as known and never calls it a first telling.
- **E079 barn line.** A line saying Wes had never said a barn memory out loud was cut, because E053 already put it on air.
- **E080 installer call.** v1 implied the answer came "today." v3 says the north-side outfit will call by Friday, which puts it after the episode records.
- **Jonathon's canon** was checked against hosts/JONATHON-CHARACTER.md wherever v3 adds his stories: married ten years to Dani, the men's breakfast at twenty-nine, most Thursdays with Wes for seven years.
- **"Sir"** appears once in the batch, from E077's caller.
- **Rotations.** Dani is quoted in alternate episodes only (E076 and E079 quote her; E077 doesn't quote her; E078 and E080 report what she did without quoting her). Wes's deadpan "K" beat appears once (E073). The motive audit runs in E075 and E077 only. Wes's knee and age beat appears in E073 (the rain it keeps predicting), E075 and E079 (his mother counting his PT reps).

### Note for whoever merges

This file was created on this branch. The E025-E032 batch created its own scripts-v3/CHANGELOG-V3.md on podcast-v3-e025-e032, so the two branches will conflict on this file at merge. The fix is to keep both batch sections under the one title.

# Batch e081-e088.md

# Podcast v3 changelog

Changes and rule overrides for the v3 scripts in scripts-v3/, logged per batch. No existing file was edited or deleted.

## Batch E081-E088 (branch podcast-v3-e081-e088)

E081-E088 had no v1 script in scripts/. All eight were written new from CALENDAR-104.md, SHOW-BIBLE section 15 (the payoff map), the opens in _build/intros_data.py, the host files, production/WARDROBE.md, and the v1 drafts of E049-E080 for the threads running into the batch.

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides four older rules:

- SHOW-BIBLE section 1 says every episode is 25-35 minutes.
- Section 4a says mains are 25-35 minutes, about 3,600-5,000 words.
- Section 4b says Field Notes are 12-16 minutes, about 1,900-2,500 words, and the section 5 clock says about 14 minutes.
- The round 12 forward rules say Field Notes run 13:50 to 14:30 and mains run 25:00 or longer.

| Episode | Older target | v3 length (timing.py) | Override |
|---|---|---|---|
| E081 The Dark Stretch | 25-35 min (sections 1 and 4a, round 12) | 52:21 | sections 1 and 4a, round 12 main length |
| E082 Field Notes: Noticing a Brother | 12-16 min (4b), about 14 (section 5), 13:50-14:30 (round 12) | 22:35 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |
| E083 Money Tells the Truth | 25-35 min | 47:21 | sections 1 and 4a, round 12 main length |
| E084 Field Notes: The Budget Talk | 12-16 min | 21:08 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |
| E085 Paid in Full | 25-35 min | 46:53 | sections 1 and 4a, round 12 main length |
| E086 Field Notes: Season Review: The Long Road | 12-16 min | 21:18 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |
| E087 Small Ways to Serve at Home | 25-35 min | 47:06 | sections 1 and 4a, round 12 main length |
| E088 Field Notes: Serving Report | 12-16 min | 21:29 | sections 1 and 4b, section 5 clock, round 12 Field Notes length |

The Field Notes checkpoints in section 5 (report by 1:15, a miss by 3:30, the single man's text by about 6:00, a re-orienting clause at about 6:30) are kept as written. The later checkpoints (From the Table to 10:20, the tool to 12:20) stretch in proportion to the longer runtime.

### Rule fixes applied in every script

- **"The challenge," not "This week's challenge."** The chapter marker, the on-screen text, the spoken line, the description and the reading narrative all use "The challenge." No host line in the batch says "week," "weeks" or "weekend." The one exception is the approved E085 open text (see the batch report).
- **Training named by title only.** E087's training premiere plug names the session Lay It Down, in the present tense, with no number, no "coming," no date, no price and no claim of results. E081's book plug (chapter thirty-one, Feelings Are the Dash, Not the Wheel) is also present tense.
- **The open's DRAFT note** is written by hand in each script as "(DRAFT Walk Steadfast open for E0NN, awaiting Aaron's approval. Re-check its facts against this script. SHOW-BIBLE section 5.)", and _build/intro.py was not run. Lint still WARNs on it ("open is a DRAFT pending Aaron"). Only Aaron's approval clears that WARN, and the brief doesn't allow editing intros_data.py.
- **No date in the reading-narrative subtitle.** "### Walk Steadfast, Episode NN" and "### Walk Steadfast, Field Notes, Episode NN." This matches the E073-E080 batch. Release dates stay in the header table, which isn't read on air.
- **Dollar amounts are spelled out** in spoken lines, because lint WARNs on a dollar sign followed by a digit.
- **"Napkin" and "testament"** fail lint, so they were replaced ("the back of a diner receipt," "the whole Bible").
- **YouTube chapter timestamps** come from _build/timing.py on the v3 text.
- **The credits line** appears only in the credits slot, exactly "Produced with AI voice and video tools." There's no other AI mention anywhere.
- **Wardrobe** matches production/WARDROBE.md for every episode.

### Batch-level checks

- **Phrase repeats.** I checked all host lines in E081-E088 for any six-word run that appears in two episodes, and reworded about fifty. The ones left on purpose are:
  - the mug ritual before "Carry this";
  - the 988 line (E081, E082);
  - the safe-messaging question (E081, E082);
  - a Field Notes quoting Tuesday's challenge;
  - the E051 barn promise quoted in E086 and E088;
  - the Colossians 3:24 quote (E083, E085);
  - canon labels ("the young man on my floor," "the room with nobody in it").
- **Cross-batch repeat.** E086's line from the retired rep in Corpus Christi was first written as "Took you long enough." The E073-E080 batch uses that line for Wes in E079, so E086 now reads "Four years, son."
- **Jonathon's marriage** is "ten years" throughout, per hosts/JONATHON-CHARACTER.md ("Married 10 years") and E083's spreadsheet, which started that first year.

### Note for whoever merges

This file is created on this branch. The E025-E032 and E073-E080 branches each create their own scripts-v3/CHANGELOG-V3.md, so merging will conflict on this file. The fix is to keep every batch section under the one title.

# Batch e089-e096.md

# Podcast v3 changelog

Changes from the v1 scripts in scripts/ to the v3 scripts in scripts-v3/, logged per batch. The v1 files are untouched.

## Batch E089-E096 (branch podcast-v3-e089-e096)

E089-E096 had no v1 drafts. All eight are new scripts written to the v3 brief, from CALENDAR-104 rows, SHOW-BIBLE section 15 (seasons, threads, the payoff map) and the E073-E080 drafts and continuity rows for the threads running in.

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides SHOW-BIBLE section 4a (main, 25-35 minutes), section 4b (Field Notes, 12-16 minutes) and the minute marks in the section 4d clock. The rule that no chapter runs six minutes without a turn still applies. Each header's Format row says "v3 length" and points here.

| Episode | Old window (bible) | v3 length (timing.py) | Override |
|---|---|---|---|
| E089 Men Who Served | 25-35 min (4a) | 48:24 | 4a, the 4d main clock |
| E090 Field Notes: Veterans Day | 12-16 min (4b) | 24:47 | 4b, the 4d Field Notes clock |
| E091 Gratitude Out Loud | 25-35 min (4a) | 47:27 | 4a, the 4d main clock |
| E092 Field Notes: Thank-You Report | 12-16 min (4b) | 22:28 | 4b, the 4d Field Notes clock |
| E093 Lead the Thanksgiving Table | 25-35 min (4a) | 51:31 | 4a, the 4d main clock |
| E094 Field Notes: Black Friday | 12-16 min (4b), and section 15 asks for a light episode with a three-minute review | 23:01 | 4b, the 4d Field Notes clock. The review itself is held to about three minutes (10:05 to 12:53), as section 15 asks. |
| E095 Joseph Said Nothing | 25-35 min (4a) | 46:49 | 4a, the 4d main clock |
| E096 Field Notes: Advent Report | 12-16 min (4b) | 21:56 | 4b, the 4d Field Notes clock |

No other length cap in the bible applies to these eight.

### Conventions applied in every script

- **Open stage note.** The DRAFT open in `_build/intros_data.py` produces a stage note that says "pending Aaron," which lint reads as an AI mention and fails. The v3 note reads "(Walk Steadfast open written for E0NN from its DRAFT entry in _build/intros_data.py, awaiting Aaron's sign-off. Facts re-checked against this script. Same beats each episode, new words. SHOW-BIBLE section 5.)" It uses "each episode" rather than "every week," to match batch E073-E080.
- **Reading-narrative subtitle has no date.** "### Walk Steadfast, Episode NN" (or "Field Notes, Episode NN"), matching batch E073-E080. Release dates stay in the header table, which isn't read on air.
- **The open lines are verbatim** from `_build/intros_data.py`. E089's open says "Veterans Day week," which is the one spoken "week" in the batch. It is the intros_data text, a calendar phrase, and not a training reference. Lint passes it.
- **Book plugs on fresh topics** (SHOW-BIBLE section 14, item 17). E093 carries chapter 6, Go first, and E095 carries chapter 4, Stop waiting. Each sits after the Word, runs under 20 seconds, is in present tense ("It's in Steadfast Men, at walksteadfast.com.") and has no dates or prices. E089 and E091 have no plug (calendar slot "-"). Field Notes never carry one.
- **Credits disclosure** appears once per script, in the credits slot only, and not in the description or the reading narrative.
- **YouTube chapter timestamps** are taken from `_build/timing.py`'s per-chapter output.

### Change to a script earlier in this batch

- **Cross-batch phrase pass.** After the six-word repeat scan, the later use of thirteen incidental phrases was reworded in E091-E096 (for example "looked at me like I'd," "in front of two hundred people," "in the driveway the whole time"). Chapter timestamps were regenerated from timing.py.
- **E093 safety line.** The man across the table from his abuser now gets the Childhelp line (1-800-422-4453) on mic and in the description, alongside 988, as E092 does.
- **E091 pie line.** The first draft had Wes say he'd "never told anybody I left before the pie." The v1 continuity rows (E007, E016) already have him owning that he left early, and his brother saying "Mom made a pecan pie for you. I ate it." E091 now has Jonathon recall the pie from the winter and Wes say he apologized to his brother "in a parking lot" but never thanked him.

# Batch e097-e104.md

# Podcast v3 changelog

Changes logged per batch for the v3 scripts in scripts-v3/. No file in scripts/ or anywhere else was edited.

## Batch E097-E104 (branch cursor/podcast-v3-e097-e104-b614)

E097-E104 had no v1 scripts. They were written new from CALENDAR-104.md, SHOW-BIBLE section 15 and the continuity of E073-E080. Other batches create this same file on their own branches. If they merge, keep every batch section.

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides three things in SHOW-BIBLE:

- section 4a, the main length of 25 to 35 minutes;
- section 4b, the Field Notes length of 12 to 16 minutes;
- the section 5 clock tables, with their minute marks for the report, From the Table and the tool.

The rule that no chapter runs six minutes without a turn still applies. Each header says "v3 length."

| Episode | Bible length | v3 length (timing.py) | Override |
|---|---|---|---|
| E097 Waiting on God Isn't Sitting Still | 25-35 min | 46:47 | 4a, section 5 main clock |
| E098 Field Notes: The Wait Report | 12-16 min | 21:46 | 4b, section 5 Field Notes clock |
| E099 The Shepherds Went Back to Work | 25-35 min | 46:19 | 4a, section 5 main clock |
| E100 Field Notes: Back to Work | 12-16 min | 20:32 | 4b, section 5 Field Notes clock |
| E101 Simeon Kept Showing Up | 25-35 min | 46:27 | 4a, section 5 main clock |
| E102 Field Notes: Christmas Eve | 12-16 min | 21:08 | 4b, section 5 Field Notes clock |
| E103 Write the Next Move | 25-35 min | 46:29 | 4a, section 5 main clock |
| E104 Field Notes: New Year's Eve | 12-16 min | 20:41 | 4b, section 5 Field Notes clock |

### Open text that differs from _build/intros_data.py

These are DRAFT opens. Each change was made in the script only, and intros_data.py was not touched. The proposed replacement lines are in BATCH-REPORT-E097-E104.md. With those lines patched into a /tmp copy of _build, intro_lint.py gives 0 fails and 0 warns. That run included the retell check against these scripts.

| Episode | intros_data line | Script line | Why |
|---|---|---|---|
| E097 | "Following Jesus as a man, Advent week two." | "Following Jesus as a man, two Sundays into Advent." | "week two" is a banned "week N" form (brief) |
| E098 | "I'm Wes Hart. A printout's been waiting in my Bible since August." | "I'm Wes Hart. I feed cattle with my brother most Saturdays now." | The printout leaves his Bible on air in E097, so the fact is stale by E098 |
| E099 | "Following Jesus as a man, Advent week three." | "Following Jesus as a man, deep in Advent." | "week three" is a banned "week N" form |
| E101 | "Following Jesus as a man, Christmas week." | "Following Jesus as a man, in the last days before Christmas." | "week" phrasing (brief) |

### Calendar notes

- **E101.** The calendar calls Simeon "the old man." The script follows SHOW-BIBLE section 14 item 20. Luke 2:25-26 is read, Simeon is never called old, and Anna's eighty-four is Luke's.
- **E103.** It carries both plugs, as the calendar allows for the year review: book chapter 34, Write the Next Move, and training session one, A Quiet Tuesday. They sit about four minutes before and ten minutes after the sub-mid.


# Split pass (2026-11-02): long Wes turns, E008 share, E066/E070 fixes

## Branch cursor/e008-jonathon-share-8ed7


## Branch cursor/e066-e070-narrow-fixes-966a

### Narrow fixes after the batch
- **E066, length.** About 105 spoken words of filler cut to bring it from 25.1 to 24.4 minutes at 150 wpm (24:15 by `_build/timing.py`). Cuts are repeats and throwaway lines only: the second recap of Tuesday's challenge (the "no Friday deadline" line stays), "Same garage feeling," "Which is fair," Jonathon echoing "Grown kids," Wes's "That's a good word for him," "For Austin's daughter in particular," and similar. Chapter times regenerated.
- **E070, Wes runs.** Two Jonathon lines added, "Read it how he wrote it. I'm ready." before the oldest son's text, and "Your dad had the fence. He's got the mailbox. What do you tell him?" after the fence story. No new facts. One Jonathon filler sentence cut ("I've been waiting since Tuesday to hear about it.") to keep his share under 50%. Longest Wes run 134 to 106. Chapter times regenerated.

## Branch cursor/split-long-wes-turns-e013-e016-d200

### Long Wes turns split (E013-E016)
Every Wes turn over 110 spoken words (consecutive Wes lines with no Jonathon line between them) is split with a Jonathon interjection. No Wes content was cut. Two Wes lines got a short bridge so they follow the new interjection: E013 "He's allowed." and "nine years of dates." Longest Wes turn before and after: E013 141 to 110, E014 125 to 110, E015 169 to 91, E016 129 to 91. YouTube chapter times were refreshed with `_build/apply_chapters.py`.

## Branch cursor/split-long-wes-turns-5300

### Long Wes turns split
The first batch report counted Wes turns line by line. Counted as consecutive Wes lines with no Jonathon line between them, seven episodes had Wes turns over 110 words. Each one is now split by a new Jonathon line (a question, reaction or bit of banter). No Wes words were changed or cut, and E022 is untouched.
| Episode | Longest Wes turn, before | After | Jonathon lines added | Jonathon share | Minutes at 150 wpm |
| E017 | 172 | 104 | 6 | 49.7% | 54.3 |
| E018 | 126 | 106 | 1 | 49.6% | 23.0 |
| E019 | 140 | 110 | 3 | 47.9% | 47.3 |
| E020 | 166 | 108 | 1 | 49.8% | 23.4 |
| E021 | 121 | 98 | 1 | 46.7% | 45.4 |
| E023 | 147 | 107 | 2 | 46.3% | 45.6 |
| E024 | 122 | 95 | 2 | 48.5% | 22.0 |

## Branch cursor/split-long-wes-turns-e025-e032-210e

| E025 The Father Who Stays | about 27 min | 53:49 | 4a and the section 5 main clock |
| E026 Field Notes: Easter Week Report | about 15 min | 22:55 | 4b and the section 5 Field Notes clock |
| E027 The Empty Chair at Your Table | about 27 min | 49:39 | 4a and the section 5 main clock |
| E028 Field Notes: The Chair Report | about 15 min | 22:47 | 4b and the section 5 Field Notes clock |
| E029 When Your Dad Is Still Alive | about 28 min | 50:33 | 4a and the section 5 main clock |
| E030 Field Notes: Calling Him Back | about 14 min | 22:13 | 4b and the section 5 Field Notes clock |
| E031 When Home Never Handed You Off | about 26 min | 48:02 | 4a and the section 5 main clock |
| E032 Field Notes: Cutting the String | about 13 min | 22:22 | 4b and the section 5 Field Notes clock |
### Long Wes turns split
A Wes turn is every Wes line until Jonathon next speaks. Twelve turns ran past 120 words (longest 167, in E032). Each one got a Jonathon line at a natural seam, usually a camera cut: a question, a reaction, a push or a joke that leads into Wes's next line. Wes's words are unchanged, so no content was cut and nothing new was said about Wes or his family. No split piece runs over 102 words. Open, slate and closing lines are untouched, and no "week" was added. Pre-existing turns of 111 to 120 words were left as they were.
| Episode | Longest Wes turn before | After | Jonathon lines added |
| E025 | 141 | 113 | 2 |
| E026 | 141 | 114 | 2 |
| E027 | 140 | 119 | 2 |
| E028 | 154 | 119 | 1 (four words, to hold Jonathon under 50%) |
| E029 | 161 | 120 | 3 |
| E030 | 131 | 107 | 1 |
| E031 | 147 | 114 | 3 |
| E032 | 167 | 116 | 2 |

## Branch cursor/split-long-wes-turns-e073-e080-b4d0

### Turn-length pass (Wes monologues split)
Counting consecutive Wes lines with no Jonathon line between them as one turn, every episode had Wes turns over 120 words, the longest 250 (E077's Matthew 6:34 passage). Each turn over 110 words was split with a short Jonathon interjection: a question, a reaction, a push-back or a bit of banter. No Wes content, scripture or story was cut, and no new facts about anyone were added. Wes's text changed in two places only, both in E077 ("Same fall." and "I did." answering Jonathon's new questions). To keep Jonathon at or under 50%, the new lines are short, and five filler words were trimmed from existing Jonathon lines in E073 ("go ahead and," "really," "just"; the last one makes "cardboard with better manners" match the canon wording). Chapter times were re-applied with `_build/apply_chapters.py`.
| Episode | Longest Wes turn before | After | Jonathon lines added | Jonathon share | Minutes (timing.py) |
| E073 | 217 | 104 | 11 | 49.9% | 53:20 |
| E074 | 219 | 101 | 5 | 49.9% | 24:03 |
| E075 | 213 | 106 | 10 | 49.9% | 47:09 |
| E076 | 151 | 106 | 5 | 49.1% | 21:25 |
| E077 | 250 | 110 | 14 | 49.2% | 47:27 |
| E078 | 214 | 103 | 5 | 49.9% | 24:35 |
| E079 | 203 | 106 | 13 | 48.2% | 47:18 |
| E080 | 199 | 109 | 7 | 49.6% | 22:45 |

## Branch cursor/split-long-wes-turns-f2ad


