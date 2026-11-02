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
