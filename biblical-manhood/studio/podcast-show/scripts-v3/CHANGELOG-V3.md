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
