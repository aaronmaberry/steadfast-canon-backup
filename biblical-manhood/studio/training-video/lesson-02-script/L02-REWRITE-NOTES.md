# L02 · You Are Not Crazy · Rewrite notes (spoken script v1, one man) · 2026-11-02

Source: `L02.txt` (Lesson 02 transcript, Wes Hart). Format, voice and quality bar: `L01-SPOKEN-SCRIPT-v5-one-man.md`. Rules: LESSON-VIDEO-SOP section 0 (R7, R8, R23, R26, R32, R33), L02-RULES.md, PRODUCTION-SCRIPT-RULES.md, Aaron's ban on that one calendar word (SOP Decision Log, Oct 29 8:41 PM).

## Numbers
- Spoken words: **3,090** (same counter as L01 v5: it gives L01 exactly 3,028).
- Lines: 197 (L001-L197), 11 chapters, 28 paragraphs in the TTS text.
- Projected runtime at 150 wpm: **20.6 min (20:36)**. L01 v5 projected 20.2 min (20:11).

## Kept
- Every teaching point, in the source order:
  - the noise on an ordinary day (two sets of orders)
  - the claim, "You are not crazy"
  - Ephesians 4:14 (the wind, the infant, the boat and the weather)
  - where the fight came from (the work moved out of sight, the rooms got shy, both orders at once, the church's part)
  - Genesis 3:10 and its three moves (hide by waiting, cover by performing, carry shame)
  - Genesis 1:27 (made on purpose, his idea, the hunger is good)
  - own both parts (don't use the world as a hiding place, don't plead guilty to all of it)
  - the shrug versus a sentence
  - where you're sitting (young, single, married, hurt, older, going great)
  - the one sentence (simpler and harder than the pile)
  - the big idea restated
  - relief
- Every story beat:
  - the man at work and the older man in the group; staying late, then the dishwasher and the silverware drawer, with his wife in the doorway
  - the kitchen sink, the dry plate and the dish soap, and the bill that got heavier
  - the back steps and the kitchen, the committee, the rented man
  - Ray: the parts counter, the dryer belt, his father's rule and his boss's rule, his wife and his brother, the scrap of paper with the white crease, "Wes, if I was smarter, these would fit", the speech Wes stopped, the wrong belt, folded once instead of twice
  - the young man at the breakfast and the older man's shrug
- All three scriptures, NIV, word for word as printed in L02.txt (string-checked, see below).
- All three workbook questions, each with its own write-and-pause (L180, L182, L184), plus the final write-down line (L191: "The confusion is in the world. I'm not crazy for wanting one clear word.").
- The four marks sentence, word for word (L193).
- Locked lines from L01: "Here's how this goes" (L004), "one lesson at a time" (L017), "So here's your one move. One." (L186), "Next lesson we look at" (L196).

## Changed
- **R33 open.** L001-L003 welcome and the spoken title. L004-L010 give the agenda, one sentence for each main point.
- **Recap matched to L01 v5.** L02.txt says the four marks were said aloud last lesson and that the move was "go sit with men". L01 v5 actually gave only the first mark (Stop Waiting) and a different move: a meal with the phone in another room, and a text to one man. The recap (L011-L015), L167 and L185 follow what the viewer actually heard. The four marks are said in full at L193, where L02.txt puts them ("like I promised").
- **"Next lesson we look at those four marks"** (L196). L02.txt names no next lesson. The topic comes from the book order in `biblical-manhood/book/00-contents.md` (A Quiet Tuesday, You Are Not Crazy, The Four Marks).
- **R23, one man.** Each line in L02.txt that addressed a room became a line to one man:
  - "Some of you did. Some of you sat near men" became L015 ("Maybe halfway. Halfway counts too.").
  - The "same chair" joke about the room is cut.
  - "If you're new, grab a seat" became L016.
  - "How many of you could name two instructions… Just a hand. That's most of the room" became L071-L072 ("Try this… Yeah. That came quick.").
  - "How many of you went quiet… Hands, if you're willing" became L090-L091.
  - "Look around… somebody two seats down" is cut. L159 keeps "where you're sitting changes the bruise".
  - "The tables are ready… work this part together… don't explain the chapter to each other" became L177-L178.
  - "Read it to a brother at your table" and "Go to your tables" became the one move (L187-L190) and the last line (L197).
- **"We" and "us" limited to Wes and the viewer.** "We got nervous" (the church) became L069 ("it got nervous"). "We got embarrassed… That's on us" became L137 ("People got embarrassed later, me included"). "Most of us didn't invent the fight" became L054. "We wait. We perform" became L172 ("You wait, you perform"). Ray's story uses "he and I". The only remaining "we" lines are:
  - the scripture (L046)
  - Wes's own house ("a bill we'd been dodging", "if we were out of dish soap"), following the L01 v5 precedent "We ate."
  - the locked "Next lesson we look at"
- **Grep-safe word swaps.** These keep the meaning:
  - "when the guys were loose" became "when the talk was loose"
  - "the guys who last around here" became "the ones who last around here"
  - "a men's breakfast" became "a church breakfast"
  - "two men I wanted proud of me" became "I wanted them both proud of me"
  - "a whole committee of men" became "a whole committee"
  - "blame everybody at lunch" became "blame the whole world at lunch"
- **Length.** The source runs about 3,790 words, and my first full one-man draft came to 3,960. To reach about 3,000 I removed restatements and filler ("uh", "you know", "I mean") and some texture lines:
  - the three-year-old calendar at the parts counter
  - "years of reading"
  - "the man who had it handled if somebody important walked through"
  - the "same chair" joke
  - "Somebody two seats down"
  - "That's an old habit of mine"
  - "I noticed that"
  No teaching point, story event or scripture was removed.
- **Stock phrases.** "At the end of the day" (source line about the rented man, now L099) became "when the day's done". The repeated "it's not X, it's Y" pivots were thinned to the one in L139, which comes from the source.
- **No new stories, facts, names, dates, statistics, scripture or doctrine.** Every fact about Wes comes from L02.txt or L01 v5.

## Checks (run on both `L02-SPOKEN-SCRIPT-v1-one-man.md` and `L02-v1-script.txt`)
| Check | Command (case-insensitive) | Result |
|---|---|---|
| Banned calendar word, any form (incl. -end, -ly, plural) | `grep -ic "wee[k]"` | **0 / 0** |
| Group address | `grep -ciE "you guys\|\bguys\b\|\bbrothers\b\|gentlemen\|everyone\|everybody\|some of you\|all of you\|any of you\|each of you\|y'all\|you all\|\bfolks\b\|\bfellas\b"` | **0 / 0** |
| "men" as a word | `grep -oiE "\bmen\b"` | md 2, txt 1. All are the brand "Steadfast Men" (title line, L001). |
| "brother" (singular) | `grep -oiE "\bbrother\b"` | 2. Both refer to Ray's brother in the story (L119, L120). This is third person, not an address. |
| we / us / our / let's | `grep -oiE "\b(we\|us\|our\|let's\|we'd)\b"` | 6. These are scripture (L046), Wes's own house (L083 ×2, L085), "Let's go find where" (Wes and the viewer, L026) and the locked "Next lesson we look at" (L196). |
| Scripture word for word | Python substring test of each verse against L02.txt and the script | Ephesians 4:14, Genesis 3:10 and Genesis 1:27 all match exactly, in both files. |
| TTS text is clean | `grep -cE "\[\|L[0-9]{3}\|#\|\*"` on the .txt | **0** (no markers, line numbers, headings or markdown) |
| L01 phrasing reuse | 5-word overlap scan against the L01 v5 spoken text | Only the locked lines, the "Welcome… to Steadfast Men. This is Lesson…" title pattern and one source phrase ("an older man I trusted", from L02.txt) overlap. |
| AI filler | `grep -iE "let that sink in\|in a world where\|journey\|dive in\|game.changer\|at the end of the day\|here's the thing"` | **0** |
| No music cues or stage directions | eyes-on | Only [beat] and [pause N] appear, and only in the .md. |

## Open for Aaron and Reed
- L196's next-lesson topic comes from the book order, not from L02.txt. Confirm that Lesson 3 is The Four Marks.
- "A church breakfast" (L154) stands in for "a men's breakfast" to keep the grep clean. Changing it back is one word if you want it.
