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
