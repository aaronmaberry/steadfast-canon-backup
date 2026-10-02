# Accuracy pass

Each script is checked against:
- its final-book chapter (`_inputs/final-book/book/`);
- the NIV (`NIV-AUDIT-2026-10-01.tsv`, or Bible Gateway's NIV 2011 for verses not in the audit);
- `SECOND-PASS-RULES.md` and `rules/LOCKED-LECTURE-STYLE.md`;
- the brief's checklist.

Tools:
- `pipeline/check.py`.
- `meta/tools/lint.py`. It checks marks, the creed, fillers (uh/um 9-11, at most 2 "um"), markers, tags, dashes, ellipsis limits, banned words, the Ray/Dale/Hank/Ike/Philip name guards, the W-only ban on "viewer", "subscribe" and "YouTube", and the verse plan. With `--ngrams` it also runs the cross-file 6-word repeat scan.
- The brief's `rg` line.
- A book-overlap scan, which lists every 7-word string a script shares with any final-book chapter. Verse text and the creed are excluded.

## Result for W01-W24, the live training sessions

W01-W24 are the 24 weekly training sessions, taught live to a room of men in an auditorium (Aaron's correction, 2026-10-01). All 24 pass, with no flags. S01-S04 are shelved in `_shelved/lectures-S01-S04/`. They were not edited and are left out of lint, the stats and the checks below. Their entries further down are kept for the record.

| Check | Result |
|---|---|
| `check.py` | 24 of 24 OK, no out-of-range sections |
| `lint.py` | 24 of 24 OK |
| Repeated 6-word strings across all 24 (`--ngrams`) | 0 |
| Verses | 72 of 72 exact NIV, 3 per session, none spoken with "twenty-four" (65 exact audit matches; the other 7 were checked on Bible Gateway or are parts of audited passages) |
| The brief's `rg` line, plus `[quietly]`, Ray and Dale | no hits |
| "viewer", "subscribe", "YouTube" | no hits in W01-W24; lint now fails them |
| Hank, Ike | in no W session (both belong to the shelved S02); Philip only as the apostle in W10 (John 14:9) |
| Creed | W03 ×2, W07 ×1, nowhere else in W01-W24 |
| Openers, recaps, closers, send-offs | all unique (`OPENERS-CLOSERS.md`) |
| Book overlap, in words shared in 7-word strings | W01 8, W03 8, W04 15, W06 9, W07 7, W22 8, all of it standard phrases or the run-in to a verse; every other session 0 |
| W recaps | speak to the men in the room and report how the room did with last session's ask; each matches the session before it |

## Correction from Aaron (2026-10-01): live training sessions, re-checked

| Item | What was done |
|---|---|
| W01 | Scanned first; no camera or online-audience wording, so no edits. Section 1, "Come On In", is byte-for-byte the approved test clip (same as `62bd9ad`). Pushed on its own as "W01 ready to record". |
| Room recaps | W02-W15 and W19-W24 are back to their room recaps from before the viewer change ("Some of you did", "I heard from…", "One of you told me…"). W02 keeps the W01 trash-can example, now told as "a guy after". W16-W18 never had a room line, so each got one ("Some of you did…", "One of you showed me his notebook…"). |
| Camera and online wording | All 24 were scanned for viewer, watching, video, channel, subscribe, comments, YouTube, episode, clip and screen. The one line that played to an online audience was W14's "subscribe to the wise", which is now "nod along with the wise". Every other hit is part of a story, not a word to an audience: men watching a game, kids watching from a window, a phone screen, a fishing show's episodes, the Weather Channel, how-to videos, a comment section a man seeks approval from, a clipboard, and W01's "No camera" (nobody photographs a plain Tuesday). |
| Shelved | S01-S04 moved to `_shelved/lectures-S01-S04/`, unedited. |
| Housekeeping | `youtube/` renamed `sessions/`. Lint now lints `sessions/` by default and fails "viewer", "subscribe" and "YouTube" in W scripts. |
| Kept | Ike, Hank's "never going to shake hands", W01's rewritten sections 2-11, the W19 and W20 tone fixes, and every verse. |

**Re-run on W01-W24:** `check.py` 24/24; lint 24/24; repeated 6-word strings 0; book overlap unchanged (W01's 8 words are the end of Luke 16:10 running into "Very little"; nothing in section 1); verses 72/72; recaps read against the session before each one, and only W01's closing ask has changed since they were written, which W02's recap already matches.

## Aaron's answers (2026-10-01), applied and re-checked

| Item | What was done |
|---|---|
| W01 book material | Sections 2-11 rewritten (see the W01 entry). Section 1, "Come On In", is byte-for-byte the approved test clip, including both ellipses and every pause value. |
| W01 habit lines | The Monday-intentions line is now about men in general ("A man can plan to start over on a Monday for twenty years running"). The "in a minute" line is gone. |
| W02 recap | Still matches W01. Its example is now one of W01's own small moves: hauling the trash cans up before anybody asks. |
| Family first-person tone check | S01 and W06: no change. W19: the kitchen line no longer pats Wes on the back. W20: "evenings I don't feel like much of a dad" became "evenings I just don't feel it". |
| Hank (S02) | The scrap now says outright that the two lines are "two orders" that "were never going to shake hands", and "Neither line was a mistake. Both were real orders, pulling opposite ways." The table question uses the workbook's wording. |
| Philip, now Ike (S02) | Renamed everywhere. Lint now fails "Philip" outside W10 and "Ike" outside S02, and fails S02 if it loses "never going to shake hands". |
| Room recaps (W) | W02-W15 and W19-W24 no longer report how the room or group did ("Some of you did", "I heard from…", "One of you told me…"). They now speak to the viewer ("Maybe you…", "If you…"). W16-W18 already did. The S lectures keep theirs. **Reversed by Aaron's correction above: W01-W24 are live sessions, and the room recaps are back.** |
| Verses | All seven substitutions confirmed; no change. |
| Later chapters, ellipses | No W25+ set. Ellipses kept as they are. |

**Re-run after the fixes:**
- `check.py` 28/28;
- lint 28/28;
- repeated 6-word strings 0;
- the 7-word book-overlap scan (W01: the 8 words are the end of Luke 16:10 running into "Very little"; nothing in section 1);
- verses 84/84 (70 exact audit matches, 12 from Bible Gateway, 2 parts of audited passages);
- the recap-consistency read of every recap against the script before it.

## How the accuracy pass worked

1. **Theology and chapter fit.** Each script was read against its chapter for the big idea, the turns and the "Your Turn" questions. The teaching follows the chapter. The examples do not: they are new.
2. **Verses.** Every verse was checked word for word against the audit row or Bible Gateway.
3. **Book examples.** The overlap scan, followed by a read-through, found that many first drafts had carried over the book's own examples. That includes reworded ones: its sample sentences, lists, images and numbers. LOCKED-LECTURE-STYLE forbids that.
   - Every one was replaced with new material that keeps the same teaching point.
   - The before and after word counts are listed under each script.
4. **Narrator, strict rule.** Every first-person line was reviewed (`_work/acc.py` lists them).
   - A self-own is kept only when it sits inside Wes's wife, kids, wedding or baptism.
   - Self-owns about Wes's own habits, work, church life or past were removed.
5. **Recaps.** Each recap was compared with the previous script in the same series, as it is now written. The recaps were then rewritten wherever the earlier script had changed.

## Checks common to all 28

- **NIV.** 70 verses match their audit rows.
  - Twelve more were checked on Bible Gateway's NIV 2011 pages, fetched 2026-10-01: James 1:5, James 1:22, 1 Timothy 4:15, Lamentations 3:22-23, Psalm 90:12, Psalm 139:14, Isaiah 30:21, Hebrews 13:8, Micah 6:8, Ecclesiastes 11:4, Luke 6:47-48 and Proverbs 13:20.
  - Two are parts of audited passages: Ephesians 2:8-9 (from the audited 2:8-10 in ch07) and Philippians 2:6-7 (from the audited 2:5-7 in ch23).
  - Where the NIV uses an em dash, the script uses a comma, because the scripts carry no dashes. Bible Gateway's small-capital "Lord" is written "LORD".
- **Narrator.** Every story is about a man Wes knows, told in the third person. No man's name is used in more than one script, and none of the names appear in the book, the old scripts, the old lectures or the workbooks.
  - The exceptions are Bible figures, used as Bible figures: Philip (John 14:9) in W10, and Jacob, Timothy, Nathan, Adam and others.
  - The new S02 has a friend named Philip, a name the book uses only for the apostle (see QUESTIONS).
  - S04's one "Steve" is a joke line, not a man ("Mostly guys named Steve").
- **Pay theology.** On God's side, every pay or earn line is framed as grace and inheritance. Accounting words appear only for human things: paychecks, a card balance, an apology owed, a scoreboard. The W12 line "Give God the debt, and close the file" is about the father's debt, handed over in forgiveness, which is chapter 12's own move.
- **Taglines.** Outside the creed, no stretch of four lines names three or more marks.

## W01-A-Quiet-Tuesday: PASS

Source chapter: `01-a-quiet-tuesday.md`. "Christ in the ordinary" also leans on `33-what-you-are-building-when-nobody-claps.md`, the chapter that holds Luke 2:51.

**Checklist**

| Check | Result |
|---|---|
| `check.py` | 3,366 words, 11 sections; sections run 1,506-1,791 characters |
| Section 1 (test clip) | 298 words, unchanged since the approved recording |
| uh/um | 10 (8 uh, 2 um) |
| Tags | 2 `[warmly]` |
| `ROOM_HANDS` / `ROOM_CHUCKLE` | 1 / 4 |
| Markers / tag questions / dashes | 8 / 2 / 0 |
| Ellipses | 3 (2 in section 1: "asked..." and "Not today... anyway.") |

- No marks are named and there's no creed, which fits the opening session.
- Grace is kept: "You don't earn that kind of attention. If you belong to Christ, He's already your Father, and He's already for you."

**Verses**

| Reference | Spoken as | Check |
|---|---|---|
| Luke 16:10 | "Luke sixteen, verse ten." | Audit ch01, WORDS-OK |
| Luke 6:47-48 | "Luke six, starting at verse forty-seven." | Bible Gateway NIV 2011, exact |
| Luke 2:51 | "Luke two, verse fifty-one." | Audit ch33, EXACT-RAW |

- **Luke 6:47-48.** The book cites Matthew 7:24, but "Matthew seven, verse twenty-four" breaks the ban on a spoken "twenty-four". Luke's parallel teaches the same thing and adds "dug down deep". Aaron confirmed: keep Luke.
- **"About eighteen years."** Luke 2:42 and 3:23 support "about eighteen years". Luke 2:52 covers that stretch in a sentence, which supports the script's "a sentence or two".

**Book material rewritten (Aaron, 2026-10-01).** Section 1 was left exactly as approved. Each item now teaches the same point with new material:

| Was (from the book) | Now |
|---|---|
| The seasons list, mirroring the book's Eli (single, quiet apartment), Tomás (2 a.m. baby), Walt (business) and Roy ("nobody's making you get up") | The single man's unexpected evening and helping a buddy move a couch; a driver at a truck stop four states from home; a man caring for a parent (pill organizer, the same story for the third time); a man out of work ("Get dressed anyway"); the good-at-his-job dad who can't name what his daughter was worried about |
| The small moves taken from the book: answering your dad's call, the phone at supper, "two minutes" | Hauling the trash cans up unasked; asking about the math test and waiting out the shrug; the radio off for the last mile and a prayer for whoever's behind the front door; Desmond's driveway; calling the friend you owe a call; owning your part of last night's argument. "None of those cost you more than a coffee break." |
| The near-verbatim book close ("not asking you to become… by Sunday", "choose without noticing you chose", "one small, deliberate move") | "I don't want a vow out of you", and the fork "so small you'll roll right over it, like the seam in a highway… feel the bump. And then turn the wheel a quarter inch." |
| Big days with a script and an audience; the match that can't heat a house (the book's flare) | A big day "does half the work for you" (the ironed shirt, the aunt, the photographer counting to three); a big day is a holiday dinner, but "nobody ever got raised on Thanksgiving. Kids grow on plain suppers." The closer now says "Not on the holiday-dinner days." |
| A show of hands about the big day that didn't change you (the book's conference and recliner), and Wes's "Mine too"; section title "Back In The Chair" | A show of hands about New Year's resolutions that made it to February, with no Wes self-own. The section is now "After The Water". |
| "I didn't decide anything today" (Anthony) | "Ask most men at bedtime what they chose that day… Chose? I went to work. I came home." |
| "That's where trust gets built, or lost" (verbatim) | "He says that's where a man gets proven." |
| The foundation nobody pulled over to admire | House tours: "they open every closet and run every faucet. Nobody ever asks to see the concrete under the floor." |
| "Ten thousand times"; the baptism where he "came up sure"; the Father "glad over it" | "The thing he did so often he quit noticing he was doing it"; driving home from his baptism with wet hair and the radio off, "thinking the old me had stayed behind in that tank"; the Father as "a dad in the bleachers who sees his kid hustle back on defense while everybody else is watching the other end of the field" |

The 7-word overlap scan now finds only the end of the Luke 16:10 quote running into "Very little" (8 words).

**Narrator.**
- Wes's own life appears only as his wedding, his baptism, his kids and his wife.
- The Monday-intentions line is now general ("A man can plan to start over on a Monday for twenty years running"). The "in a minute" line is cut.
- "Not because I don't love them. Because I was somewhere else" stays, because it sits at his own dinner table.
- Desmond and Arturo are new men.

**Repeats.** The repeat scan across all 28 finds no 6-word string shared with any other script. The W02 recap was updated to match.

## W02-You-Are-Not-Crazy: PASS
- **Chapter 2.** Covers the tangle of instructions, what the confusion does to a man, wisdom from God, a man's design, and God remembering we are dust.
- **Verses.** James 1:5 (Bible Gateway), Genesis 1:27 (audit ch02) and Psalm 103:14 (audit ch31).
- **Counts.** 3,367 words, 9 uh/um, 2 `ROOM_CHUCKLE`, 2 tag questions, 1 ellipsis.
- **Book examples.** The scan found 26 words before the rewrite and 0 after.
  - Replaced: the man "who never got a picture solid enough to keep", the "you think a man is here to do" line, and a reworded line about Wes's own kitchen.
  - The rental-car story (Gordon) was replaced by Fitz and the borrowed boat: whoever hollered last got the wheel.
  - Calvin's library stays.
- **Recap.** Recaps W01's unwatched day and its one small choice, and reports how the room did. Its example is one of W01's own small moves, told about "a guy after": hauling the trash cans up unasked.

## W03-The-Four-Marks: PASS
- **Chapter 3.** Covers what a mark is, the four marks in order with their verses named in passing, why these four, and God's pay as an inheritance, not a wage.
- **Verses.** Philippians 2:5 (audit ch03), James 1:22 and 1 Timothy 4:15 (Bible Gateway).
- **Creed.** 2 uses: section 4 and the recap.
- **Counts.** 3,654 words, 10 uh/um.
- **Book examples.** The scan found 116 words before the rewrite and 8 after; the 8 are the plain phrase "the fourth mark is Work for God's Pay".
  - Replaced: the book's one-line gloss of each mark ("step out ahead of your people, scared or not"), its list of false pay ("a crowd, a bigger number, a newer truck, a father who finally says…") and its inheritance sentence from ch30.
- **Narrator.** "I've been him" was removed.

## W04-Stop-Waiting: PASS
- **Focus mark.** Stop Waiting, named in sections 1, 11 and 12.
- **Verses.** James 4:17, Psalm 27:14 and Luke 9:51, all from the audit, ch04.
- **Counts.** 3,615 words, 9 uh/um, 1 dash (the restart "He— he").
- **Book examples.** The scan found 102 words before the rewrite and 15 after; the 15 are the run-in to Luke 9:51.
  - Replaced: the "keep the peace" costume, the "start now before you feel like it" rule, "things in his own house" and "the next obvious good thing".
  - New: Horace's sign-up sheet.
- **Narrator.** "A question I ask myself" was removed.

## W05-Pick-Up-The-Weight: PASS
- **Focus mark.** Pick Up the Weight, named in sections 1, 7, 10 and 12.
- **Verses.** Galatians 6:5, Genesis 4:9 and Galatians 6:2, all from the audit, ch05.
- **Counts.** 3,591 words, 10 uh/um, 4 `ROOM_CHUCKLE` (the limit is 4).
- **Book examples.** The scan found 68 words before the rewrite and 0 after.
  - Replaced: the empty hand that feels like failure, the stepdad's "that's her…", "hands under it even when it isn't fair", and the book's line that ownership looks at today, not at who caused this.
  - Terrence was replaced by Benny, who puts one down.
- **Recap.** Recaps W04's Stop Waiting.

## W06-Go-First: PASS
- **Focus mark.** Go First, named in 8 sections.
- **Verses.** John 10:4, John 13:14-15 and Deuteronomy 31:8, all from the audit, ch06 (31:8 is WORDS-OK).
- **Counts.** 3,618 words, 10 uh/um.
- **Book examples.** The scan found 197 words before the rewrite and 9 after; the 9 are the run-in to Deuteronomy 31:8.
  - The draft had used the book's own list of first sentences: "I'm sorry I raised my voice", "I was wrong", "Can I pray for us?", "Son, I've noticed something", and "we haven't been to church in months, we're behind on the truck".
  - Sections 5-8, 10 and 11 were rewritten:
    - new small doors: the dishwasher apology, a voicemail to a grown son and a bedtime doorway prayer;
    - new "name it and walk it" pictures;
    - Julian at the red light;
    - new fears;
    - Clarence and the bulletins;
    - "one sentence and a long block".
- **Narrator.** "I've used every one of them" was removed. "My mother-in-law's hip" is a prayer request from a man at Bernard's table.
- **Tone check** (Aaron, 2026-10-01). The only family first-person line is "I've stood in that doorway with my own kids and said, night, buddy." It's humble and light, so there's no change.
- **Recap.** Uses "Let me catch everybody up." The W05 summary inside it was updated to match W05 as it is now.

## W07-Work-For-Gods-Pay: PASS
- **Chapter 7.** "Live for a reward that lasts". Covers everybody getting paid by something, whatever you do for the Lord, grace before work (rent-free), the secret giving of Matthew 6, the glance around the room, what the mark won't promise, and "not the room's".
- **Focus mark.** Work for God's Pay, named in sections 1-4 and 12.
- **Creed.** 1 use, in section 9.
- **Verses.** Colossians 3:23-24, Ephesians 2:8-9 and Matthew 6:3-4, all from the audit, ch07.
  - Ephesians 2:8-9 comes from the audited 2:8-10 rows. The NIV's dashes are rendered as commas, so the words are unchanged.
- **Counts.** 3,589 words, 10 uh/um, 4 `ROOM_CHUCKLE`, 3 tag questions, 1 ellipsis.
- **Theology.** God's pay is an inheritance ("It comes to a son because of whose son he is"). Work follows sonship and doesn't buy it.
- **Book examples.** The scan found 95 words before the rewrite and 7 after; the 7 are the tail of the Matthew 6 run-in.
  - Replaced: the chapter's sentences "a son by grace before you've lifted a finger", "you work like a son because you already are one", "the drive home after a day nobody thanked you for" and "if nobody ever sees it, why".
  - Barry's sheet cake and Barry's early mornings stay. Dino is new.
- **Narrator.** "With my own family" was removed.
- **Other.** A line that repeated W24 was reworded. The recap of W06 (Go First, and the gap) matches W06.

## W08-The-Empty-Chair: PASS
- **Chapter 8.** Covers where the road ends, the first classroom, kinds of absent fathers, what takes the seat, "it explains, it doesn't excuse", naming and grieving, and the chair a man now fills.
- **Verses.** Psalm 68:5-6 and Psalm 27:10 (audit ch08), and Ephesians 6:4 (audit ch26).
- **Counts.** 3,707 words, 10 uh/um, 4 `ROOM_CHUCKLE`.
- **Book examples.** The scan found 242 words before the rewrite and 0 after.
  - Replaced: the book's set of sample sentences ("my dad left / my dad was home and I never knew him / my dad…"), "the snap has the shape of a missing father", "some boys give the seat to whoever's in the room", the grief line, and "You're somebody's empty chair now".
  - New: the four kinds of chairs, the picture on the fridge, and Chester and Archie.
- **Recap.** Uses "Let me catch us up." It recaps W07's point that every man chases some kind of pay, and that God's pay is different.

## W09-Anger-The-Itch-And-The-Drift: PASS
- **Chapter 9.** Covers one fear behind three doors (anger, lust, the drift), grooves, starving the itch, waiting out the wave of anger, and naming your own door.
- **Verses.** Ecclesiastes 10:18, James 1:14-15 and Ephesians 4:26-27, all from the audit, ch09.
- **Counts.** 3,792 words (the cap is 3,800), 13 sections, 10 uh/um, 12 markers (the top of the range).
- **Book examples.** The scan found 407 words before the rewrite and 0 after.
  - The draft carried the chapter's 3 a.m. baby scene ("a voice comes out of you that you…"), "he put the fear where men usually put it", "turn it off after supper, ask her one real question and let her finish" and "settle it while it's still daylight".
  - All of it was replaced with Boyd's Thursday, Dewey's game, Carl, and new practices.
- **Recap.** Uses "So, last session was a heavy one." It recaps W08's empty chair.

## W10-The-Father-Who-Does-Not-Leave: PASS
- **Chapter 10.** Covers the father picture a man carries in, the fortieth copy versus the original (John 14:9), not as orphans, leaning, practicing being a son, seeing your dad again, and the father running from a long way off.
- **Verses.** John 14:9, John 14:18 and Luke 15:20, all from the audit, ch10.
- **Counts.** 3,660 words, 10 uh/um, 3 tag questions, 2 ellipses.
- **Book examples.** The scan found 159 words before the rewrite and 0 after.
  - Replaced: the book's prayer prompts ("say Father out loud and give Him one sentence about the day", "tell Him which false father your prayers have been aimed at") and its "in the room with nothing to say to you" picture.
  - The men are Floyd, Gene and Herb.
- **Narrator.** Removed Wes's own prayer-habit self-owns and a "dead sure" line about his own past.
- **Recap.** Recaps W09, "where a man's pain goes".

## W11-When-Home-Never-Handed-You-Off: PASS
- **Chapter 11.** Covers the missing handoff, shopping for it, the mother who held it together, Jacob hanging on for the blessing, David's charge to Solomon, Paul's hands on Timothy, getting it now, and when Dad won't.
- **Verses.** Genesis 32:26, 1 Kings 2:2-3 and 2 Timothy 1:6, all from the audit, ch11.
  - The 1 Kings quote stops at "wherever you go." All the words are exact, and a period was added where the reading stops mid-verse (listed in QUESTIONS).
- **Counts.** 3,785 words, 10 uh/um, 12 markers.
- **Book examples.** The scan found 247 words before the rewrite and 0 after.
  - Replaced: the book's "clumsy sentence" ("nobody ever told me I was a man, would you…"), "a dad who was never handed off can still hand off his…", "if you're forty and…", and the "walk him the rest of the way" line.
  - The men are Garrett and Grady.
- **Recap.** "Last go-round, we camped on a single word": W10's "Father". The old "entire hour" wording is gone.

## W12-Leave-Without-Slamming-The-Door: PASS
- **Chapter 12.** Covers stakes and roots, honoring the seat, leaving coming first, rage paying attention, closing the file (Joseph), deciding and then telling, and coming back with a knock.
- **Verses.** Exodus 20:12 and Genesis 50:20 (audit ch12), and Ephesians 5:31 (audit ch25, WORDS-OK).
  - Ephesians 5:31 stands in for the book's Genesis 2:24, because "twenty-four" can't be spoken.
- **Counts.** 3,788 words, 9 uh/um, 4 `ROOM_CHUCKLE`.
- **Theology.** "Give God the debt, and close the file" means handing the father's wrong to God in forgiveness, as chapter 12 does. It is not accounting language on God's side.
- **Book examples.** The scan found 265 words before the rewrite and 0 after.
  - Replaced: "what his dad did with it was his dad's business", "if your father's alive and it's safe… circle a day on the calendar", "some of you got out of houses no kid should have grown up in", and the book's comment on Genesis 50:20.
  - The men are Hector, Elmer, Fred and Duane.
- **Recap.** Recaps W11's opening question.

## W13-A-Man-With-No-Brothers: PASS
- **Chapter 13.** Covers six hundred names and no brother, buddies versus brothers, someone at the bottom of the fall, Jesus wanting three in Gethsemane, Jonathan going to David at Horesh, and who to ask and how.
- **Verses.** Ecclesiastes 4:9-10, Mark 14:34 and 1 Samuel 23:16, all from the audit, ch13.
- **Counts.** 3,680 words, 9 uh/um, 3 tag questions.
- **Book examples.** The scan found 145 words before the rewrite and 0 after.
  - Replaced: "so shrink it: one man, twenty minutes", "he's probably already at your church or on your crew and nobody's ever asked him", "a version that fits the…", and a ch12 line ("pray for your dad by name").
  - The men are Irving and Homer. Chapter 13's Dale is not used.
- **Recap.** First drafted from chapter 12, then rewritten to match the W12 script ("the front step of the house you grew up in").

## W14-Ask-The-Man: PASS
- **Chapter 14.** Covers the older man up the road, walking with the wise, asking something small, bringing a real question, being the man ahead, and the runners Paul never met.
- **Verses.** Proverbs 13:20 (Bible Gateway), Titus 2:6-7 and 2 Timothy 2:2 (audit ch14).
- **Counts.** 3,590 words, 10 uh/um, 12 markers.
- **Book examples.** The scan found 459 words before the rewrite and 0 after.
  - Replaced: the chapter's list of sample questions ("what would you do differently", "what did the year after your divorce really cost you", "could I come watch you work sometime"), its line that the man ahead needs the truth about where he blew it, its brother-versus-man-ahead weather image, and its warning about the man who only tells his wins.
  - The men are Lamar, Luther, Jed and Lenny.
- **Recap.** Recaps W13: hundreds of names in the phone, a buddy versus a brother, and asking for one.

## W15-The-Problem-Inside: PASS
- **Chapter 15.** Covers the smell in the wall, the turn in the road (repentance), saying the word "sin", out of the heart, even with a great dad, why that's good news, Christ dying for us while we were still sinners, and a new heart rather than another program.
- **Verses.** Mark 7:23, Romans 5:8 and Psalm 51:10, all from the audit, ch15.
- **Counts.** 3,650 words, 10 uh/um, 2 `ROOM_CHUCKLE`.
- **Book examples.** The scan found 187 words before the rewrite and 0 after.
  - Replaced: "an excuse that never runs out / you can't repent of your dad's sin", "you'd still take the second look", "feeling rotten can go on for years without…" and "the best home in the world couldn't have filtered it out".
  - The men are Jasper, Manny and Ira.
- **Narrator.** The "convincing smile" self-own was removed.
- **Recap.** Changed to "Our last session circled the older man up the road" (W14). This wording replaced "Where we left off" and also cleared a 6-gram repeat with W03.

## W16-How-That-Looks-On-A-Man: PASS
- **Chapter 16.** Covers sin's camouflage in a man (the locked drawer, the fortress, the scoreboard and podium, the throne), David staying home, Nathan's "You are the man!", David's one-sentence confession, asking the people who know, and opening it while it's still yours.
- **Verses.** 2 Samuel 11:1, 12:7 and 12:13, all from the audit, ch16.
  - 12:7 and 12:13 end mid-quote at their verse breaks, as the NIV does.
- **Counts.** 3,778 words, 9 uh/um. Section 1 is 1,898 characters (the cap is 1,900).
- **Book examples.** The scan found 14 words before the rewrite and 0 after; the read-through also replaced Morris.
  - The men are Milo, Nolan and Monty.
- **Closer.** Changed, because it duplicated W06's.

## W17-No-Fixed-Star: PASS
- **Chapter 17.** Covers the moving light, Judges 21:25, a room full of clocks, feelings and numbers, the plumb line, the string winning, the lamp for the next step, and why the Bible stays on the shelf.
- **Verses.** Judges 21:25, Amos 7:7-8 and Psalm 119:105, all from the audit, ch17.
  - The book's Matthew 7:24-25 was not used, because of the "twenty-four" ban.
- **Counts.** 3,612 words, 9 uh/um, 9 markers.
- **Book examples.** The scan found 7 words before the rewrite and 0 after.
  - The men are Percy, Quentin and Reggie.
- **Narrator.** "Mine would be up too" was removed.

## W18-Before-The-Fall: PASS
- **Chapter 18.** Covers the build sheet, dust and breath, image before anything, blessed before the work, work it and keep it, a day to stop, "not good to be alone", first words, and nothing to hide.
- **Verses.** Genesis 2:7, 2:15 and 2:18, all from the audit, ch18.
  - Genesis 1:27 was skipped, because W02 already uses it.
- **Counts.** 3,695 words, 9 uh/um, 12 markers, 3 tag questions.
- **Theology.** "The first whole day was the day off" matches chapter 18: Adam was made on day six, so his first full day was the seventh.
- **Book examples.** The scan found 40 words before the rewrite and 0 after.
  - Replaced: "every day so far", "words come out of him", "one man in a flawless garden" and "your first wreck".
  - Rufus was replaced. The men are Odell and Rudy.
- **Narrator.** The church parking-lot self-own was removed.

## W19-Two-Men-Two-Ways: PASS
- **Chapter 19.** Covers two nights and two gardens: Adam silent beside Eve, and Christ face down in Gethsemane. Then Adam hiding and Jesus going out to the soldiers, and in Christ rather than in Adam.
- **Verses.** Genesis 3:6, Matthew 26:39 and 1 Corinthians 15:22, all from the audit, ch19.
- **Counts.** 3,692 words, 10 uh/um, 8 markers.
- **Book examples.** The scan found 124 words before the rewrite and 0 after.
  - Replaced: "Christ to bring you out of Adam, say so", "the Bible doesn't stop at… copy the second man", "mostly by keeping his mouth shut" and the divorced-father aside.
  - The men are Silas, Warren and Tyrone.
- **Narrator.** One passage was re-anchored to Wes's own supper table. His couch line stays, because it sits inside his family life.
- **Tone check** (Aaron, 2026-10-01):
  - The kitchen line said "She's never once had to point that out to me… I usually catch it about two seconds later", which read as Wes congratulating himself.
  - It now reads "She hardly ever has to say a word. She just waits, and about two seconds later I hear myself. Some nights it takes me a good deal longer than two seconds."
  - The couch and baptism lines are fine as they are.
- **Closer.** Changed, because it was a duplicate.

## W20-Destiny-Is-Not-A-Vibe: PASS
- **Chapter 20.** Covers three false ideas of destiny ("you'll know it when you feel it", "it has to be big", "it's somewhere else"), David's epitaph, good works prepared in advance, finishing the work, and "not your name".
- **Verses.** Acts 13:36, Ephesians 2:10 and John 4:34, all from the audit, ch20.
- **Counts.** 3,653 words, 10 uh/um.
- **Book examples.** The scan found 153 words before the rewrite and 0 after.
  - Replaced: "for the people He gave you, until it's finished", "something people still talk about after you're gone", the book's list ("your wife's name if you're married, your kids' names if…") and "a stage, a following".
  - The men are Vern, Tobias and Yusuf.
- **Tone check** (Aaron, 2026-10-01). "There are evenings I don't feel like much of a dad" leaned self-pitying. It is now "There are evenings I just don't feel it", and the bedtime-voices story still makes the point that the feeling follows the doing.

## W21-If-There-Is-No-Wife-Yet: PASS
- **Chapter 21.** Covers three seats (the single man is at least three different men), not half a man, "finds" as a moving word, waiting until you can carry it, undivided hours, and sisters and brothers.
- **Verses.** Proverbs 18:22, 1 Corinthians 7:35 and 1 Timothy 5:1-2, all from the audit, ch21.
- **Counts.** 3,607 words, 10 uh/um.
- **Book examples.** The scan found 223 words before the rewrite and 0 after.
  - Replaced: "tell God two true things, one about what you lost and one about what you did", the Genesis 2 bride gloss, "find out how she talks to God", and "what you do with your eyes and your hands now".
  - The men are Zeke, Sal, Woody and Stan.

## W22-Know-Her: PASS
- **Chapter 22.** Covers a shepherd who knows, living with her "according to knowledge", running on old notes, asking and letting it sit, watching, remembering and asking, deep waters, what feels like love to her, the new-baby season, and every other season.
- **Verses.** John 10:14, 1 Peter 3:7 and Proverbs 20:5, all from the audit, ch22.
  - John 10:14 is read to "know me." The NIV's verse ends there with a dash that runs into verse 15, and the script closes it with a period.
- **Counts.** 3,776 words, 13 sections, 10 uh/um, 3 tag questions.
- **Book examples.** The scan found 745 words before the rewrite and 8 after; the 8 are the run-in to 1 Peter 3:7.
  - The draft was the heaviest borrower. It carried the chapter's question list ("her story, how her dad was with her…", "her ordinary day hour by hour, three in the afternoon…"), its divorced-man paragraph and its "ask your sister or a sister in Christ" line.
  - All of it was rebuilt around Dwight, his brisket and his class, plus Rashad and Kofi.
- **Closer.** Changed, because it was a duplicate.

## W23-Lay-It-Down: PASS
- **Chapter 23.** Covers the other half of Ephesians 5, Christ not pulling rank, "your call, hon", keeping your backbone, a thousand small surrenders, losing your life to find it, and laying it down wherever you're standing.
- **Verses.** Ephesians 5:25 and Matthew 16:25 (audit ch23), and Philippians 2:6-7 (verses 6-7 of the audited 2:5-7).
- **Counts.** 3,542 words, 10 uh/um, 4 `ROOM_CHUCKLE`.
- **Theology.** The "verse twenty-two" line is a joke about what men quote (Ephesians 5:22). It is a mention, not a quote, and it is written out without the number. It sends men to verse 25.
- **Book examples.** The scan found 611 words before the rewrite and 0 after.
  - Replaced: the chapter's test ("did she get stronger or did her load get heavier"), its divorced-man paragraph, "the same row at the recital", and "find a wife who brings you the truth".
  - Ennis was replaced. The men are Tadeo, Lorenzo and Royce.
- **Narrator.** "My wife could tell you…" was removed.

## W24-What-She-Actually-Needs: PASS
- **Chapter 24.** Covers what a paycheck can't count, one question at the table, bringing your head in, praise where the kids can hear, not a volunteer, nothing to brace for, no back door, still chasing, and Christ going first.
- **Verses.** Proverbs 31:28-29, Proverbs 15:1 and Malachi 2:15, all from the audit, ch24.
- **Counts.** 3,583 words, 11 uh/um (the top of the range).
- **Book examples.** The scan found 751 words before the rewrite and 0 after.
  - Replaced: the chapter's "noticed as a woman with a name", "frozen in place, same guy as ten years ago", "arms around her while she cries with every fix… in your pocket" and "sleep under that roof every night and never really be with her".
  - The men are Booker and Desi.
- **Narrator.** The front-door line stays, because it sits inside Wes's own marriage.
- **Other.** "A spot on your back" echoed S04's Lowell and became "Let somebody look at that knee."

## S01-A-Quiet-Tuesday: PASS
- **Rewritten from the opening on**, per Aaron. There is no Lewis credit, and the locked S01 opener and closer are not reused.
- **Chapter 1.** Covers the plain day, mercies new every morning, numbering our days, and being faithful with a few things. It closes on grace.
- **Verses.**
  - Lamentations 3:22-23 and Psalm 90:12 (Bible Gateway).
  - Matthew 25:21 (audit ch07, WORDS-OK).
- **Counts.** 3,561 words, 10 uh/um (2 um).
- **Book examples.** The scan found 8 words before the rewrite and 0 after.
  - The men are Wendell (the question in the van) and Bo (the phone drawer and egg timer).
- **Narrator and tone check** (Aaron, 2026-10-01). S01 has two first-person family passages:
  - the bike story: "I was running behind him, still yelling, I've got you, and I, uh, very much did not have him";
  - "I've said, that's great, buddy, to my kids about a story I could not repeat back to you".

  Both are light and self-deprecating, and neither brags, preaches or self-pities. No change was needed. The earlier draft's wedding and baptism lines had already been cut in the book-example pass. **S01 is unchanged since b7e8361 and ready to record.**
- **Repeats.** All phrasing shared with W01 was removed on the S side while W01 was locked. The repeat scan was re-run after the W01 rewrite and finds 0.

## S02-You-Are-Not-Crazy: PASS
- **Chapter 2.** Covers the drawer of tangled cords, why the confusion isn't your fault but your life is still yours, what the tangle does, being made on purpose, the voice behind you, and the unchanging Christ.
- **Verses.** Psalm 139:14, Isaiah 30:21 and Hebrews 13:8, all from Bible Gateway.
- **Counts.** 3,654 words, 10 uh/um (2 um), 4 `ROOM_CHUCKLE`. Section 6 is 1,815 characters.
- **Book examples.** The scan found 61 words before the rewrite and 0 after.
  - Replaced: the middle-years calendar line, "chasing a target somebody keeps moving", "you're told to earn more and be home more" and the chapter's own "you're not crazy, the confusion is real".
- **Hank's Scrap** (section 11, for the workbook's recap and take-home question 5).
  - Hank, a propane-truck driver Wes knows, keeps a soft, folded scrap behind his license.
  - The scrap holds two pencil lines that fight: "a man keeps his troubles to himself" (his dad's) and "tell me when something's wrong" (his wife's, from their first year married).
  - They are framed as "two orders" that "were never going to shake hands", which is the workbook's wording.
  - For about fifteen years he tried to obey both. "Whichever one he kept, he'd broken the other one, and he figured the problem was him."
  - Reading the Gospels on his lunch breaks, he sees Jesus didn't hide His grief from His friends, and he sorts the two lines: "Neither line was a mistake. Both were real orders, pulling opposite ways. And that fight wasn't a flaw in Hank. It got handed to him." Then he draws a pencil line through the top one.
  - Wes appears only as the man Hank showed it to ("He showed me once").
  - The closer's first question uses the workbook's wording: "Make your own version of Hank's scrap. If you wrote two lines on a scrap of paper, two orders about being a man that won't shake hands, what would they say?"
  - Ray and Dale appear in no script. Lint fails on either name, fails on Hank outside S02, and fails if S02 loses the wallet story or the "never going to shake hands" line.
- **Other men.** Jerome (with Ike, renamed from Philip per Aaron) and Sam's grandmother. Lint keeps "Ike" to S02 and "Philip" to W10's John 14:9.
- **Recap.** Recaps S01's plain days.

## S03-The-Four-Marks: PASS
- **Chapter 3.** Covers "steadfast" as set, like a fence post in concrete; the book that falls open (Virgil's father's Bible); Micah 6:8 as one sentence with four verbs; the four marks; not in vain; and picking the faint one.
- **Verses.** Psalm 112:7 and 1 Corinthians 15:58 (audit ch35), and Micah 6:8 (Bible Gateway).
- **Creed.** 2 uses.
- **Counts.** 3,634 words, 10 uh/um (2 um).
- **Book examples.** The scan found 16 words before the rewrite and 0 after; the 16 were a repeated "not in vain" run-in.
- **Narrator.** The cart passage was re-told about another man. "The books on my shelf" was removed earlier.
- **Men.** Virgil and Theo.
- **Recap.** "Let me get us back on the same page" leads into S02's tangle and Hank's scrap.

## S04-Stop-Waiting: PASS
- **Focus mark.** Stop Waiting, named in sections 1, 11 and 12.
- **Verses.**
  - Ecclesiastes 11:4 (Bible Gateway).
  - Genesis 3:9 (audit ch04).
  - James 4:17 (audit ch04; a mark verse, allowed in its own mark's session).
- **Counts.** 3,608 words, 10 uh/um (2 um).
- **Book examples.** The scan found 8 words before the rewrite and 0 after; the 8 were "fog can't be scheduled, a named thing can".
- **Men.** Lowell (the spot and the appointment). Isaac was renamed Jules, because Isaac is a Bible name the book uses (Genesis 22).
- **Narrator.** The living-room line stays, because it sits inside Wes's own home.
- **Other.** Section 1 was lengthened into range. A "Jesus said…" paraphrase that counted as a fourth verse was removed.
