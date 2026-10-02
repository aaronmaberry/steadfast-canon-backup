# Change report: Steadfast Men scripts rewrite (2026-10-01)

Branch `opus55-scripts-rewrite-2026-10-01`. Output folder: `biblical-manhood/scripts/_opus55-scripts-2026-10-01/`.

W01-W24 are the 24 weekly training sessions, taught live to a room of men, and they live in `sessions/`. S01-S04 are shelved in `_shelved/lectures-S01-S04/`. See "Correction from Aaron" below.

All 28 scripts were written from scratch to the final book, `rules/LOCKED-LECTURE-STYLE.md` and the 2026-10-01 brief. None reuses old wording, outlines, stories or illustrations.

## What changed everywhere

**Old W01-W24.** These were Max-hosted and used the old week order.
- They named "Max" 7-20 times per script.
- They carried the old creed ("A real man…", 2-5 times per script).
- They used the retired mark wording ("rejects passivity", "accepts responsibility", "leads courageously", "expects the greater reward"), 10-45 hits per script.
- W02-W24 carried a Lewis credit.
- They were 4,500-6,100 words long, with "Week N of 24" and "Session N of 24" headers and timecoded movements.

None of that survives. Every new script:
- uses the final marks and the final creed (W03/S03 twice, W07 once, nowhere else);
- has Wes Hart on the mic;
- runs 3,300-3,800 words;
- carries no numbered-session wording.

**Old S01-S04.** These were the style benchmark, but their content predated the rename.
- S01 and S02 credited Lewis; that credit is removed entirely.
- S01, S02 and S04 used the retired mark wording, and all four carried the old creed.
- The locked openers and closers in `LOCKED-SESSIONS.md` are not reused.
- First-person stories that broke the narrator rule are gone: S04's garage tile and the lamp on it, and S01's line about "when my father finally did his job".

**Class order.** The W series now follows the book's class order (week NN = chapter NN).
- New training sessions with no old script: W12, W14, W19, W22 and W24. Their closer questions are built from each chapter's "Your Turn".
- The old W12-W19 topics move to their chapter's week:
  - old W12 (A Man With No Brothers) became W13;
  - old W13 (The Problem Inside) became W15;
  - old W14 (How That Looks On A Man) became W16;
  - old W15 (No North Star) became W17, "No Fixed Star";
  - old W16 (Before The Fall) became W18;
  - old W17 (Destiny Is Not A Vibe) became W20;
  - old W18 (If There Is No Wife Yet) became W21;
  - old W19 (Lay It Down) became W23.
- W01-W11 keep their numbers.
- The old W20-W24 topics (The Bed Is a Covenant, Your Daughter Is Watching, and the three son sessions) are not in this set. They cover book chapters 25-29, which `37-condensed-training.md` places after the first 24 class weeks.

**Narrator rule (strict).**
- Wes's only first-person life is his wife, his kids, his wedding and his baptism, kept light. A self-own stays only when it sits inside that family life; the accuracy pass removed the rest.
- Every story is a man Wes knows, told in the third person, with a name found nowhere in the book, the old scripts, the old lectures or the workbooks.
- No book character's story is retold.

**Verses.** Exactly 3 NIV verses per training session, each leading a teaching point and checked word for word. See `VERSES.tsv` and `ACCURACY-PASS.md`. No reference's spoken form contains "twenty-four".

**Pause technique.** Pauses still come from the post-production silence that `retime.py` applies from the `|pause` values, as before. The one new in-take technique is a sparing ellipsis. See `PAUSE-TECHNIQUES.md`.

**W and S kept fully separate.** The two series share no opener, closer, story, man, joke or signature line. Across all 28 files there are no repeated 6-word strings, except in scripture and the creed. Checked with `meta/tools/lint.py --ngrams`.

## Name changes requested by Aaron (2026-10-01)

**The S02 wallet man is now "Hank".**
- Aaron first asked for Dale, then switched to Hank, because Dale is the chapter 13 man.
- The old S02 told the wallet story about "Ray", which clashed with the book's chapter 27 Ray.
- The fully rewritten S02 originally had no wallet passage. Because the S02 workbook now points to "the way Hank carried two lines in his wallet" and asks about "Hank's scrap" (take-home question 5), S02 gained a new section 11, "Hank's Scrap", written new from scratch:
  - Hank is a propane-truck driver Wes knows, told in the third person.
  - Behind his license he keeps a soft, folded scrap with two pencil lines that fight each other: "a man keeps his troubles to himself" (his dad's) and "tell me when something's wrong" (his wife's, from their first year married).
  - For about fifteen years he tried to obey both and blamed himself. Reading the Gospels on his lunch breaks, he notices Jesus didn't hide His grief from His friends. He sorts the two lines, sees the fight was handed to him rather than being his own flaw, and draws a pencil line through the top one.
  - Table question 1 is "Make your own version of Hank's scrap."
  - It keeps the teaching purpose of the old Ray passage (orders that contradict each other, and the shame they cause). None of its wording or details carry over: no parts counter, no dryer belt, no "speak / don't you make a fuss", and no scene with Wes in it.
- **No script uses Ray or Dale.** Lint now fails any script that does, and fails any script other than S02 that uses Hank. It also fails S02 if it loses the Hank wallet story.
- **W02's rental-car man was renamed from Hank to Gordon,** so Hank belongs only to S02. Later, the accuracy pass replaced the whole rental-car story, because it leaned on the book's picture. It's now Fitz and a borrowed boat. Neither Gordon nor that Hank appears anywhere in the scripts now.
- **S04's Isaac was renamed Jules.** Isaac is a name the book uses, for the Bible's Isaac in Genesis 22.

## Accuracy pass (all 28)

The accuracy pass was run against the final book and the NIV. It found two problem types that lint can't see.

1. **The book's own examples, reused.**
   - LOCKED-LECTURE-STYLE forbids reusing the book's examples, stories, names, images and numbers. Many first drafts carried them anyway, mostly reworded: sample sentences, lists of questions, scenes and numbers.
   - A 7-word overlap scan against every chapter (excluding verse text and the creed) measured it at 5,476 words across W02-W24 and S01-S04.
   - Every case was rewritten with new material that keeps the same teaching. The scan now shows 0 words in 22 scripts, and 7-15 words in W03, W04, W06, W07 and W22 (standard phrases or verse run-ins).
   - W01 (23 words, plus reworded examples) is locked for recording. It is flagged, not changed; see ACCURACY-PASS and QUESTIONS.
2. **Narrator self-owns outside the strict rule.** Wes's habit-level confessions were removed or re-told about another man in W03, W04, W06, W07, W10, W15, W17, W18, W19, W23 and S03. Lines set inside his marriage, kids or home stay: S04's living room, W24's front door and W19's couch.

Also in this pass:
- **Recaps.** Every recap was re-aligned with the script before it as it now reads.
- **Duplicate closers.** Duplicates in W16, W17, W19 and W22 were fixed.
- **Fillers.** Lint now caps "um" at 2. All four S scripts were cut from 3 to 2.
- **Verses.** All 84 verses were re-verified. W12's Ephesians 5:31 is now sourced to the audit (ch25).
- **Repeats.** The final repeat scan across all 28 finds 0 repeated 6-word strings. Every opener, recap, closer and send-off is unique.

## Aaron's answers (2026-10-01), applied

Aaron answered QUESTIONS-FOR-AARON with "fix things that need to be fixed first". S01 came first, because it's next to record. It needed no change, and that was pushed on its own as `ff350ea`.

| Script | Change |
|---|---|
| S01 | Tone check only. Both family first-person lines (the bike ride, and "that's great, buddy") read light and humble, so there's no change and S01 is ready to record. |
| W01 | Sections 2-11 rewritten to drop every piece of book material listed in ACCURACY-PASS; section 1 is unchanged word for word. The "in a minute" line is cut, and the Monday-intentions line no longer speaks of Wes. |
| W02 | The recap's example now matches a W01 small move, and the recap speaks to the viewer (the viewer part is reversed; see the correction below). |
| W03-W15, W21-W24 | The recap no longer reports how the room did with last session's ask; it speaks to the viewer. A few lines were padded to keep section 1 in range (W09, W11, W22). Reversed; see the correction below. |
| W19 | Room recap reworded (reversed below). The kitchen self-own no longer pats Wes on the back. |
| W20 | Room recap reworded (reversed below). The bedtime line no longer self-pities. |
| W06 | Room recap reworded (reversed below). The tone check found no problem. |
| S02 | Hank's lines are framed as two real orders that were "never going to shake hands", not a mistake, and the table question uses the workbook's wording. Philip renamed Ike. |
| `meta/tools/lint.py` | New guards: Philip only in W10 (the apostle), Ike only in S02, and S02 must keep "never going to shake hands". |

Confirmed with no change: the seven verse substitutions, no W25+ set, and the ellipses.

## Correction from Aaron (2026-10-01): W01-W24 are live training sessions

W01-W24 are not YouTube episodes. They are the 24 weekly training sessions, taught live to a room of men in an auditorium. The "speak to the viewer" recap change from the previous round was wrong and is undone below. W01 came first, because it's next to record.

| Script | Change |
|---|---|
| W01 | Scanned for camera or online-audience wording, and nothing needed changing. Every line already speaks to men in the room. "No ceremony. No camera. No crowd." (section 2) means that nobody photographs a plain Tuesday, and "watching the other end of the field" is the bleachers picture. Section 1, "Come On In", is byte-for-byte the approved test clip (same as `62bd9ad`, pauses included). No edits; W01 is ready to record. Pushed on its own as `2d6a50b`. |
| W02 | Room recap restored ("Some of you did. I talked to a guy after who said…"). It keeps the W01 trash-can example, so it still matches W01. |
| W03-W15, W19-W24 | Room recaps restored word for word from before the viewer change: "Some of you…", "I heard from…", "One of you told me…", "A couple of you…". The padding lines added for the viewer versions are gone. |
| W14 | Also: "It doesn't say, uh, subscribe to the wise" became "nod along with the wise", the only line that played to an online audience. |
| W16 | The recap now reports the room: "Some of you did, and found it was smaller to say than to carry. Some of you didn't…" |
| W17 | The recap now reports the room: "Some of you did that, and I'd guess it was the longest few minutes of your month." |
| W18 | The recap now reports the room: "One of you showed me his notebook before we started. Three mornings running, his line said, be quiet and listen. Well, I'd say Mark's working on him." |
| S01-S04 | Shelved: moved to `_shelved/lectures-S01-S04/` unedited, and left out of lint, `STATS.tsv`, `VERSES.tsv`, `OPENERS-CLOSERS.md` and the pause table. |
| Folders and docs | `youtube/` renamed `sessions/`. "Episode" wording in the meta docs now says "training session". |
| `meta/tools/lint.py` | Lints `sessions/` by default, and fails "viewer", "subscribe" and "YouTube" in any W script. |

The other scan hits are all part of a story, not words to an audience, so they stay. They include men watching a game, kids watching from a window, phone and TV screens, a fishing show's episodes (W07), the Weather Channel (W13), how-to videos (W14), a comment section a man seeks approval from (W08) and a foreman's clipboard. Everything else from the last round is kept: Ike, Hank's "never going to shake hands", W01's rewritten sections 2-11, the W19 and W20 tone fixes, and every verse.

The locked style says "session", never "week", so the restored recaps say "last session", not "last week". Lint still enforces that.

**Re-run on W01-W24:** `check.py` 24/24; lint 24/24; repeated 6-word strings 0; book overlap unchanged (W01 8, W03 8, W04 15, W06 9, W07 7, W22 8, every other session 0); verses 72/72 exact; every recap matches the session before it.

## Fillers removed (Aaron, 2026-10-01)

Aaron picked two pause styles from the W01 pause samples, A (silent beat) and C (short restart), and asked for every "uh", "um" and "eh" to be gone from all 24 sessions, W01 section 1 "Come On In" included. Backup before the edit: `/workspace/backups/opus55-scripts-pre-fillers-20261001-1522.tar.gz`.

- **236 fillers replaced** (202 uh, 32 um, 2 eh) in W01-W24. Seeded random pick per spot (`random.Random(20261001)`, 70% A / 30% C per Aaron's follow-up): **167 A, 69 C**. Every spot, old and new text, is listed in `meta/FILLER-REPLACEMENTS.tsv`.
- **A, silent beat.** The line is split where the filler was, and the first half gets a 0.7 post pause, so `retime.py` sets a ~0.7 s silence there. The first half ends in a line-end ellipsis where the ellipsis limits allow (69 spots, which brings every session to the 4-ellipsis cap) and in a comma everywhere else (96), so the voice keeps the thought open. Two fillers sat at the start of a line (W01 L115, W20 L159); those were dropped and the line before got a 0.7 pause.
- **C, restart.** A short self-correction in the same line with a comma beat before it, for example "Think about how you'd, look, how you'd hire somebody." Phrases: well 22, I mean 13, see 11, let's say 9, look 8, what 4, how do I put this 1, honestly 1. No phrase is used twice in a row and no phrase appears more than once in any session.
- **Untouched:** "ER" (the emergency room, W10), and everything that isn't a filler. Four small wording nudges kept lint green: W04 §10 "sitting there in that parking lot" and W24 §5 "This next part is really simple" (a section had dropped to 1,498 chars, under the 1,500 floor), W14 "A couple of you... / called it the most awkward" and W12 "pretty terrible at it anyway" (to keep the cross-file 6-word repeat count at 0).
- **Style rules held:** no new dashes (one restart dash in the whole set, as before), "session" not "week", no viewer/YouTube wording; discourse-marker, "I mean" and "you know" limits all pass.
- **`meta/tools/lint.py`:** the old filler quota (uh/um 9-11, at most 2 um, no two in a paragraph, no back-to-back line-start uh) is gone. Lint now **fails on any uh/um/eh** (also uhh, umm, uhm, ehh; case-insensitive, whole word, so "the ER" never matches). Tested by planting an "uh" in a copy of W10: lint failed on it.
- **Re-run:** `check.py` 24/24 (run with `CHECK_PY=/workspace/training-ep01/locked/check.py`; there is no `check.py` in `meta/tools`), lint 24/24, repeated 6-word strings 0, `STATS.tsv` refreshed (uh_um is 0 everywhere).
- **Audio:** W01 re-recorded in full from this text as `print-build/session-audio/W01-A-Quiet-Tuesday-2026-10-01-v2` (.mp3/.mp4). On v4 the comma-marked beats mostly came out with no pause at all, so `retime.py` had nothing to stretch; those beats were set to 0.70 s by inserting silence at the word boundary (`W01-v2/fixbeats.py`). Worth knowing before the other 23 sessions are recorded.

## Per script

### W01 A Quiet Tuesday
- **Old version:** Max hosted it, it ran 6,137 words with the old creed 5 times, and it used the retired mark wording.
- **New version:** Wes's first-day welcome, followed by the plain-day claim. It teaches from Luke 16:10, Luke 6:47-48 and Luke 2:51. The stories are Desmond's driveway meeting and Arturo's one-line notebook.
- **Section 1 is the audio test clip** (298 words). It uses a mid-line ellipsis, "Not today... anyway."
- **Matthew 7:24 → Luke 6:47-48:** the book cites Matthew 7:24, but "Matthew seven, verse twenty-four" breaks the "twenty-four" ban, so W01 uses the parallel passage. Aaron agreed to keep Luke.
- **Accuracy pass:** cut one line that implied Wes runs a business.
- **Aaron's answers:** W01 was unlocked except for section 1. Sections 2-11 now replace everything that came from the book:
  - The seasons list is new: a single man, a driver, a man caring for a parent, a man out of work.
  - The small moves are new: trash cans, the math test, the radio off for the last mile, owning your part of last night's argument.
  - The book's close became the seam-in-the-highway picture.
  - The match became the holiday dinner versus plain suppers.
  - The show of hands is now about New Year's resolutions.
  - The verbatim "built or lost" line is gone.
  - The foundation joke is now the house tour.
  - The baptism is now the wet-haired drive home.
  - The Father glad over it is now the dad in the bleachers.

  The habit self-owns are removed. Section 1 is "Come On In"; "Back In The Chair" became "After The Water", and "Nobody Claps" became "No Program".

### W02 You Are Not Crazy
- **Old version:** Max hosted it, with a Lewis credit.
- **New version:** four voices that all sound sure of themselves, a man's design, and God's patience with men made of dust (James 1:5, Genesis 1:27, Psalm 103:14). The stories are Fitz's borrowed boat and Calvin's library.
- **Accuracy pass:** fixed the recap's length wording. Replaced the rental-car story and three lines that came from the book (26 words of book overlap before, 0 after).

### W03 The Four Marks
- **Old version:** the four old marks, with "rejects passivity" and the others; 45 retired-wording hits.
- **New version:** the final marks and creed (twice), with marks explained as the wear habits leave (Philippians 2:5, James 1:22, 1 Timothy 4:15). God's pay is taught as the inheritance. The man is Darnell.
- **Accuracy pass:** replaced the book's one-line gloss of each mark, its list of false pay and its inheritance sentence (116 words of book overlap before, 8 after). Removed the self-own "I've been him".

### W04 Stop Waiting
- **New version:** focus mark Stop Waiting, with James 4:17, Psalm 27:14 and Luke 9:51. The stories are Marcus's voicemail and Horace's sign-up sheet. "Godly waiting versus stalling" matches the book's "Waiting with your boots on".
- **Accuracy pass:** Leon's Little League story and four book lines ("keep the peace", "start now before you feel like it" and others) were replaced. Book overlap went from 102 words to 15, all of the 15 in the run-in to a verse. Removed "a question I ask myself".

### W05 Pick Up the Weight
- **New version:** focus mark Pick Up the Weight, with Galatians 6:5, Genesis 4:9 and Galatians 6:2. The stories are Rafael's folder, Gus's cows, Felix's phone bill and Benny. It covers "that's mine, period", the backpack and the piano, and the cross.
- **Accuracy pass:** changed the closer's first line, which repeated W01's ("Alright. Let me land this."). Replaced Terrence with Benny and four of the book's lines (68 words of overlap before, 0 after).

### W06 Go First
- **New version:** focus mark Go First, with John 10:4, John 13:14-15 and Deuteronomy 31:8. The stories are Bernard's "safe" prayer table, Julian and Clarence. It covers foot-washing and following the Shepherd who goes ahead.
- **Accuracy pass:** the draft had used the book's own list of first sentences ("I'm sorry I raised my voice", "Can I pray for us?", "Son, I've noticed something"). Sections 5-8, 10 and 11 were rewritten around new small doors (a dishwasher apology, a voicemail to a grown son, a bedtime doorway prayer), Julian at the red light and Clarence's bulletins. Book overlap went from 197 words to 9. Removed "I've used every one of them". The recap was updated to match W05.

### S01 A Quiet Tuesday
- **Rewritten in full, opening included** (Aaron's decision). The Lewis credit (2 mentions), 14 retired-wording hits, the old creed (3 times) and the father line are removed. The old "Glenn" story is gone.
- **New version:** Lamentations 3:22-23, Psalm 90:12 and Matthew 25:21. The stories are Wendell's van rides (the question his son asked) and Bo's phone drawer.
- **Accuracy pass:** removed repeats of W01, including the baptism wording and the central claim. Replaced the one line taken from the book.

### S02 You Are Not Crazy
- **Rewritten in full.** The Lewis credit, the old marks, the old creed and the Ray sections ("Ray", "The Scrap") are removed.
- **New version:** the drawer of cords, Jerome's interview homework and his breakfasts with Ike (renamed from Philip per Aaron, 2026-10-01), and Sam's grandmother. It teaches from Psalm 139:14, Isaiah 30:21 and Hebrews 13:8.
- **Accuracy pass:** replaced four lines from book chapter 2 (61 words of overlap before, 0 after). Cut "um" from 3 to 2.
- **Added:** "Hank's Scrap" (see "Name changes" above).

### S03 The Four Marks
- **Rewritten in full.** The old creed (3 times) is gone, along with the old "Lonnie", "The Desk" and "The Receipt" material.
- **New version:** the final creed (twice) and "steadfast" as set, like a fence post in concrete. It teaches from Psalm 112:7, Micah 6:8 and 1 Corinthians 15:58. The stories are Virgil (his dad's old Bible, and the son he'd never told "I love you") and Theo's index card in the sun visor.
- **Accuracy pass:** rewrote the "why these four" paragraph and the closer, which echoed W03. Re-told the cart passage about another man (strict narrator rule). Cut "um" from 3 to 2.

### S04 Stop Waiting
- **Rewritten in full.** Wes's first-person garage tile and lamp story is gone, along with "Curtis" and the old creed.
- **New version:** focus mark Stop Waiting, with Ecclesiastes 11:4, Genesis 3:9 and James 4:17. The stories are Lowell's skin spot and Jules's first year with his mother-in-law in the spare room.
- **Accuracy pass:** removed a "Jesus said…" paraphrase, which counted as an extra verse, and fixed a short section. Renamed Isaac to Jules. Replaced the book's "fog can't be scheduled" line. Cut "um" from 3 to 2.

### W07 Work for God's Pay
- **Old version:** old W07, "Live For A Reward That Lasts". Max hosted it, with the old creed, the retired mark wording and a Lewis credit.
- **New version:** focus mark Work for God's Pay. It teaches from Colossians 3:23-24, Ephesians 2:8-9 and Matthew 6:3-4. God's pay is an inheritance that comes to a son, with grace before work. The creed is used once.
  - Stories: Barry's sheet cake and early mornings, and Dino.
- **Accuracy pass:** replaced the chapter's own sentences about sonship and the unthanked drive home (95 words of overlap before, 7 after). Removed "with my own family". Reworded a line that repeated W24.

### W08 The Empty Chair
- **New version:** Psalm 68:5-6, Ephesians 6:4 and Psalm 27:10. It covers four kinds of absent fathers, what takes the seat, "it explains, it doesn't excuse", naming and grieving, and taking your own seat.
  - Stories: Chester and Archie.
- **Accuracy pass:** replaced the book's sample sentences ("my dad left / my dad was home and I never knew him"), its "shape of a missing father" image and "You're somebody's empty chair now" (242 words of overlap before, 0 after).

### W09 Anger, the Itch and the Drift
- **New version:** Ecclesiastes 10:18, James 1:14-15 and Ephesians 4:26-27. One fear sits behind three doors.
  - Stories: Boyd's Thursday, Dewey's game, and Carl.
- **Accuracy pass:** the chapter's 3 a.m. baby scene, "put the fear where men usually put it", and its after-supper and daylight practices were replaced (407 words of overlap before, 0 after).

### W10 The Father Who Does Not Leave
- **New version:** John 14:9, John 14:18 and Luke 15:20. It covers the fortieth copy versus the original, not as orphans, practicing being a son, and the father who runs.
  - Stories: Floyd, Gene and Herb.
- **Accuracy pass:** replaced the book's prayer prompts (159 words of overlap before, 0 after). Removed Wes's prayer-habit self-owns and a "dead sure" line about his past.

### W11 When Home Never Handed You Off
- **Old version:** old W11, same title.
- **New version:** Genesis 32:26, 1 Kings 2:2-3 and 2 Timothy 1:6. It covers Jacob's grip, David's charge, and Paul's hands on Timothy.
  - Stories: Garrett's silver pickup, and Grady.
- **Accuracy pass:** replaced the book's "clumsy sentence" and three more lines (247 words of overlap before, 0 after). Fixed the recap's "entire hour".

### W12 Leave Without Slamming the Door
- **New training session** (old W11 covered chapter 11 only).
- **New version:** Exodus 20:12, Ephesians 5:31 and Genesis 50:20. It covers honoring the seat, leaving first, closing the file and coming back with a knock.
  - Ephesians 5:31 stands in for the book's Genesis 2:24 (the "twenty-four" ban).
  - Stories: Hector and Christmas, Elmer, Fred and Duane.
- **Accuracy pass:** replaced the book's alive-and-safe calendar line and three more lines (265 words of overlap before, 0 after).

### W13 A Man With No Brothers
- **Old version:** old W12, same title.
- **New version:** Ecclesiastes 4:9-10, Mark 14:34 and 1 Samuel 23:16. It covers buddies versus brothers, Jesus wanting three, Jonathan at Horesh, and who to ask and how.
  - Stories: Irving and Homer. Chapter 13's Dale is not used.
- **Accuracy pass:** replaced "one man, twenty minutes" and three more book lines (145 words of overlap before, 0 after). The recap was rewritten to match the W12 script.

### W14 Ask the Man
- **New training session** (old W12 covered chapter 13 only). Proverbs 13:20, Titus 2:6-7 and 2 Timothy 2:2.
  - Stories: Lamar, Luther, Jed and Lenny.
- **Accuracy pass:** replaced the chapter's list of sample questions and its weather image (459 words of overlap before, 0 after). Proverbs 13:20 was checked on Bible Gateway.

### W15 The Problem Inside
- **Old version:** old W13, same title.
- **New version:** Mark 7:23, Romans 5:8 and Psalm 51:10. It covers the smell in the wall, saying the word "sin", even with a great dad, and a new heart rather than another program.
  - Stories: Jasper, Manny and Ira.
- **Accuracy pass:** replaced four of the book's lines (187 words of overlap before, 0 after). Removed the "convincing smile" self-own. The recap now opens "Our last session circled the older man up the road", which also cleared a repeat with W03.

### W16 How That Looks on a Man
- **Old version:** old W14, same title.
- **New version:** 2 Samuel 11:1, 12:7 and 12:13. It covers the locked drawer, the fortress, the scoreboard, the throne, David at home, Nathan's finger, and the one-sentence confession.
  - Stories: Milo, Nolan and Monty.
- **Accuracy pass:** replaced Morris and 14 words of book overlap. Changed the closer, which duplicated W06's.

### W17 No Fixed Star
- **Old version:** old W15, "No North Star".
- **New version:** Judges 21:25, Amos 7:7-8 and Psalm 119:105. It covers the plumb line and the lamp for the next step.
  - Stories: Percy, Quentin and Reggie.
  - The book's Matthew 7:24-25 is not used (the "twenty-four" ban).
- **Accuracy pass:** removed "Mine would be up too".

### W18 Before the Fall
- **Old version:** old W16, same title.
- **New version:** Genesis 2:7, 2:15 and 2:18. It covers image before anything, blessed before the work, a day to stop, and "not good to be alone".
  - Stories: Odell and Rudy.
- **Accuracy pass:** replaced Rufus and four book lines (40 words of overlap before, 0 after). Removed the church parking-lot self-own.

### W19 Two Men, Two Ways
- **New training session** (old W16 covered chapter 18 only). Genesis 3:6, Matthew 26:39 and 1 Corinthians 15:22. It covers Adam silent and hiding, Christ face down and going out to them, and in Christ rather than in Adam.
  - Stories: Silas at the carving board and at Easter, Warren and Tyrone.
- **Accuracy pass:** replaced four book lines (124 words of overlap before, 0 after). Re-anchored one passage to Wes's own supper table. Fixed a duplicate closer.

### W20 Destiny Is Not a Vibe
- **Old version:** old W17, same title.
- **New version:** Acts 13:36, Ephesians 2:10 and John 4:34. It covers three false ideas of destiny, David's epitaph, and work prepared in advance.
  - Stories: Vern's postcards, Tobias and Yusuf.
- **Accuracy pass:** replaced the book's names list and three more lines (153 words of overlap before, 0 after).

### W21 If There Is No Wife Yet
- **Old version:** old W18, same title.
- **New version:** Proverbs 18:22, 1 Corinthians 7:35 and 1 Timothy 5:1-2. It covers the three kinds of single man, "finds" as a moving word, and undivided hours.
  - Stories: Zeke, Uncle Sal, Woody and Stan.
- **Accuracy pass:** replaced four book lines (223 words of overlap before, 0 after).

### W22 Know Her
- **New training session** (old W18 covered chapter 21 only). John 10:14, 1 Peter 3:7 and Proverbs 20:5.
  - Stories: Dwight (brisket, and going back to class), Rashad and Kofi.
- **Accuracy pass:** rebuilt the chapter's question list and its divorced-man paragraph (745 words of overlap before, 8 after, all of the 8 in a verse run-in). Fixed a duplicate closer.

### W23 Lay It Down
- **Old version:** old W19, same title.
- **New version:** Ephesians 5:25, Philippians 2:6-7 and Matthew 16:25. It covers the other half of the chapter, Christ not pulling rank, and keeping your backbone.
  - Stories: Tadeo, Lorenzo and Royce.
- **Accuracy pass:** replaced Ennis, the chapter's "stronger or heavier" test, the recital row and two more lines (611 words of overlap before, 0 after). Removed "My wife could tell you…".

### W24 What She Actually Needs
- **New training session** (old W19 covered chapter 23 only). Proverbs 31:28-29, Proverbs 15:1 and Malachi 2:15.
  - Stories: Booker, and Desi.
- **Accuracy pass:** replaced four of the chapter's lines (751 words of overlap before, 0 after). "A spot on your back" (S04's Lowell) became "that knee".
