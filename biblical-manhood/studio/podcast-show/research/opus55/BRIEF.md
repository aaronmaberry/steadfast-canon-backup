# Brief: Walk Steadfast open system, episode architecture and season progression (Opus 5.5 review pass)

You are reviewing the work of an earlier writer, not starting from zero. Work at expert level and take the time you need. This is for Aaron Maberry, who owns the show.

## The show
Walk Steadfast is a two-host video podcast (YouTube first, audio feed too) about following Jesus as a man. Wes Hart (52, Hill Country, married since 2000, three kids) and Jonathon (37, San Antonio, sales manager, married to Dani, Ruby 7, Theo 4). Twice a week in 2027: a Tuesday main (about 25-27 min) and a Friday "Field Notes" (about 14 min) that reports on Tuesday's challenge. 104 episodes, E001 Tue Jan 5 2027 to E104 Fri Dec 31 2027. E001-E080 are scripted. E081-E104 are not written yet. Hosts, canon and continuity are in evidence/.

Plugs: the book (*Steadfast Men: The way of Godly Men*), the video training (24 sessions) and walksteadfast.com. Plug wording is present tense and descriptive. No "out now", no dates, no prices.

## What Aaron asked for
The old fixed "standard intro" (three near-identical variants) was put on hold at 10:47 AM CT on 2026-10-03. Aaron wants an intro that hits the same points every episode in different words, built on research into how top podcasts open, and a review of the episode architecture and the season progression across all 104.

## What already exists (read these first)
- `evidence/TOP-PODCAST-STRUCTURES.md`. The research, with sources.
- `evidence/INTRO-AND-STRUCTURE-PROPOSAL.md`. The plan written for Aaron.
- `evidence/SHOW-BIBLE.md` v3. Section 5 is the open system, 4d the proposed clock, 13 the locked disclosure, 14 the decisions and 15 the season progression.
- `evidence/ALL-OPENS-E001-E080.txt` and `evidence/intros_data.py`. The 80 written opens. `evidence/intro_lint.py` and its output are the checker (currently 0 FAIL, 0 WARN).
- `evidence/structure-audit.md`. Chapter timings per episode on the script clock (Wes 145 wpm, Jonathon 170 wpm).
- `evidence/EPISODE-DIGEST.txt`. Title, date, cold open and first lines after the intro for each episode. It was taken before the new opens went in. The cold opens and Pull up a chair are unchanged.
- `evidence/CONTINUITY-ROWS-E001-E080.md`. What each episode established on air. Use it to fact-check every fact line in the opens.
- `evidence/hosts/`, `evidence/CANON.md` and `evidence/BOOK-TOC.md` are the host briefs, the canon and the book's contents. `evidence/CALENDAR-104.md` has every episode's topic, verse and plug slot.
- `evidence/grok47-critique.md` is a critique of the first draft by grok-4.7. It's a different model. Weigh it, don't defer to it.
- `scripts/` has six full scripts (E001, E002, E013, E040, E079, E080) to show the real shape.
- `evidence/UNSLOP.md` and `evidence/STEADFAST-UNSLOP-SKILL.md` are the writing rules. They apply to everything you write for the show.

## Locked, do not reopen
- The show name, Walk Steadfast.
- The disclosure line "Produced with AI voice and video tools." exactly. Wes speaks it once in the credits after 3 s of closing music, at normal credits volume, like a producer credit, with no gap and no ducking. It's the last line of every episode's notes and in the show description. No other AI mention anywhere.
- The slate rule (number, date, title, starting with the man who didn't say the last line of the open).
- The plug tense rule above.
- E020 must stay at 16:00 or under.

## Writing rules (hard)
No em or en dashes. No mid-sentence colons. Straight quotes. Sentence-case headings. No banned AI words (UNSLOP.md). No "not just X but Y". No forced groups of three. No "uh" or "um". Use the pause marks in the scripts ([beat], [pause 1s]) sparingly. Facts must be true to the canon and the continuity rows as of each episode's release date.

## What to deliver, in one Markdown file named `opus55-review.md`
1. **Verdict on the open system** (SHOW-BIBLE section 5). What's right, what's wrong, what you'd change, with reasons tied to the research or to the listener. Keep or change the anchor sentence? Are the lengths right? Is the offer line every episode right, given the calendar's rule that mid-episode plugs space the book and the training out?
2. **E001 first, final quality.** The E001 opening is about to be recorded again, and it waits on this. Give your recommended E001 open and slate, line by line with speakers. If you keep the current text, say so and why.
3. **Line edit of all 80 opens.** For each one you'd change, give the episode, the old line, the new line and a one-clause reason (a fact error, staleness, repetition, weak hook, wrong speaker, length, cadence). Check every fact against the continuity rows. Keep the beats and the lint limits (mains 42-62 words, Field Notes 32-52, E001 60-75, hooks 14 words at most, no 6-word run shared within 8 episodes, no 5-word run shared within 4). Leave the good ones alone and say which ones are strongest.
4. **Opens for E081-E104.** Write all 24 in the same format, following CALENDAR-104 for topics and the season progression in SHOW-BIBLE section 15 for what's true by then. Mark anything that depends on unwritten episodes as an assumption.
5. **Episode architecture.** Review SHOW-BIBLE 4a, 4b and the proposed clock in 4d against the structure audit. Say what you'd adopt for E081 on and which of the light fixes to E001-E080 are worth Aaron's time, ranked.
6. **Season progression E001-E104.** Review SHOW-BIBLE section 15. Which threads are paid off well, which are dropped, which are overdone, and what E081-E104 must pay off. Include the challenge ledger, the season reviews, and the E001 and E103-E104 bookends.
7. **Self-critique and revision.** Reread your sections 1-6 as a hard editor. List the weaknesses you find, then give the revised versions of anything you'd change. The revised version is the one Aaron should read.

Do not generate any media, call any paid API or sign up for anything. Web research is allowed if you want to check a claim in the research file.
