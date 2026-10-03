# Walk Steadfast podcast: status

Resume file. Updated after each milestone. Internal.
- Aaron's direction: 2026-10-02 9:12 PM CT.
- Corrections:
  - 9:15 PM: plugs spaced out; E001 carries the full walkthrough and plugs.
  - 9:16 PM: E001 gets full introductions of both men.
  - 9:17 PM: a standing outro on every episode, with rotating variants; E001 gets the fullest.

Brief: two-host video podcast with Wes Hart and Jonathon. Spend $0. No posts, no publishing, no Drive uploads, no voice generation.

| Milestone | State | Paths |
|---|---|---|
| 0. Setup, inputs read | done 10-02 9:30 PM CT | canon, unslop, voice lock, opus55 pause convention |
| 1. Research dossier | done | research/DOSSIER.md, research/_notes-raw.md |
| 2. Show bible (incl. plug cadence, standing outro A-E) | done | SHOW-BIBLE.md |
| 3. Host briefs + Jonathon voice spec | done | hosts/WES-HART-HOST.md, hosts/JONATHON-CHARACTER.md, hosts/JONATHON-VOICE-SPEC.md |
| 4. Visual/production + Descript plan + wardrobe | done | production/PRODUCTION-SPEC.md, production/WARDROBE.md |
| 5. Distribution + reading narrative format | done | distribution/DISTRIBUTION.md, distribution/READING-NARRATIVE-FORMAT.md |
| 6. Calendar 104 + plug slots + cadence | done | CALENDAR-104.md (generator: _build/cal.py) |
| 7. Scripts E001-E008 | done (v2 after two focus-group rounds) | scripts/E001-E008 |
| 8. Focus groups (2 simulated rounds), Reader Panel packet | done; real panel awaits relay | focus-groups/ROUND-1.md, ROUND-2.md, READER-PANEL-PACKET.md, CHANGELOG.md |
| 9. Remaining scripts in batches | IN PROGRESS. Batch 2 (E009-E016): E009-E011 written + linted; E001-E010 revised after reader panel round 3. E012 done. Batch 2 (E009-E016) DONE, round 4 simulated pass applied (focus-groups/ROUND-4.md). Batch 3 (E017-E024) DONE, with a read-through polish pass and round 5 simulated (focus-groups/ROUND-5.md). Batch 4 (E025-E032) IN PROGRESS: Batch 4 (E025-E032) DONE, with a polish pass and round 6 simulated (focus-groups/ROUND-6.md). Batch 5 (E033-E040) DONE, with a polish pass and round 7 simulated (focus-groups/ROUND-7.md). Next: batch 6 (E041-E048), starting E041 These Men Are My Brothers, on parent go-ahead. | scripts/ ; per-batch log in CHANGELOG.md |

## How to resume

- Read SHOW-BIBLE.md (sections 4-10), the host briefs, CALENDAR-104.md (topic, verse, mark and plug per episode) and WARDROBE.md (outfit per episode).
- Write the next scripts from the calendar row. Rotate standing outro variants: mains A-E from E003 (E003 A, E005 B...), Field Notes F1-F4 from E002. See SHOW-BIBLE section 9.
- Lint each script with `_build/lint.sh`.

Notes
- The Reader Panel agent (00d08357-...) needs SendToAgent, which this executor doesn't have. The packet for the parent to relay is in focus-groups/READER-PANEL-PACKET.md.

## Next-batch notes (E009+)

- **E009-E010 should lean Jonathon** (balance rule; E007-E008 ran 64-65% Wes).
- **Threads to pay off:**
  - Wes's knee appointment, Feb 3 (E010).
  - Jonathon and Dani's follow-up talk, Feb 7, and Wes at Mom's doctor, Feb 9 (E011 and E012).
  - The friend request (once a month at most; resolve in Easter season).
  - Jonathon's "go first gets misused" objection (E011).
  - "Does Wes undersell the big days?" (E047 or E051).
- **Continuity logs.** Before writing, read the "Continuity set on air" sections at the bottom of both host briefs.
- **Per-script tools.** After each script, run `python3 _build/apply_chapters.py <script>` and `bash _build/lint.sh <script>`.

## Batch log (milestone c)

Directions (parent, 10-02 10:01 PM CT):
- Batches of 8.
- After each batch: simulated focus-group pass, lint, update STATUS and CHANGELOG.
- Keep these swappable: show name, Jonathon's surname, Dani/Ruby/Theo. Single index: `NAME-SWAP-INDEX.md`; swap with `_build/swap_names.py`.
- No AI-disclosure line on mic. Launch dates stay "coming," no prices. No nephew call-in.
- $0 spend.
- Report at E024.

Rotation for this run:
- Outros: E009 D, E011 E, E013 A, E015 B, E017 C, E019 D, E021 E, E023 A.
- Field Notes outros: E010 F1, E012 F2, E014 F3, E016 F4, E018 F1, E020 F2, E022 F3, E024 F4.
- Sub-mid bank: E009 5, E011 6, E013 7, E015 8, E017 1, E019 2, E021 3, E023 4.
- Verse readers: J = Jonathon, W = Wes.
  - E009 W, E010 J, E011 W, E012 W, E013 J, E014 W, E015 W, E016 J.
  - E017 W, E018 W, E019 J, E020 W, E021 W, E022 J, E023 W, E024 J.

Avoid list for batch 2:
- Book chapters 5/6/7/15: wall/kitchen, weight on the floor, Cain/Abel, seventy elders, the oak, doors on the street, the face in the window, towel, Gideon "watch me," Nehemiah rubble, eight seconds, trophy riding shotgun, moths, pecan trees (Mr. Pruitt), the truck's paint blister/rust/body man, Wade.
- Training W05/W06/W07/W15: Rafael shipment folder, Gus fence/cows, Felix tax forms, job to Ohio, Bernard at the diner men's group, the creek, the dishwasher apology, "night, buddy" in the doorway, Sunday dinner, two chairs third row, Julian driving his wife, Barry's cake and freezer, the doorway "good stuff," the thermostat, Jasper's smell, Mario's expense reports, the surgeon, the lunch tray.
- Also never: keys, cereal, looking down, garden-standby, Gethsemane-while-they-slept.

- 10:45 PM: reader panel round 3 applied to E001-E010 (see focus-groups/READER-PANEL-REPLIES.md). Lessons are now bible rules (section 7).
- E009 done: 25:50, 3,743 words, Wes 53%.
- E010 done: 13:52, 1,978 words, Wes 59%.
- E011 done: about 25 min, Wes 53%. Two chairs (does it count if she asked?).
- E012 done: 13:59, Wes 57%. Mom's plan; brother 'I never asked her either'; nephew chili for seven.
- E013 done: 24:26 (script estimate; breather and pauses add about 20 s), Wes 53%. Receipts' backs (prayer dates); son-in-law prays.
- E014 done: 14:07, Wes 50%. Hidden thing kept hidden; wills signed (tacos); phone jail; gutter by Mar 1; Thursday text; canon sentence once.
- E015 done: 25:24, Wes 55%. Retitled The Part That's Mine (W15 echo). District deal/Cancun; sister returns a nickel; the shepherd and the headache; 'the last sentence'; the long vs short story; Dani's pink 'Me'; T plug; safety rail on Tuesday.
- E016 done: 14:05, Wes 51%. VP shrug; rep annoyed; Ruby and the cereal; brother's pecan pie; son's 'they were bad though'; Ps 139 by Jonathon; examen.
- E017 done: 25:04, Wes 53%. Coach voice; title lost in 2019; contractor's metal roof; two chairs (unsettled); feet-washing towel; 'Three kids and your mother.'
- E018 done: 13:57, Wes 57%. Level gutter; rep 'next big one's mine'; Ruby at the truck window; 'Run the room. With your mother.' (half right, almond grab bar); sister 'I was home with Mom'; Prov 12:15; ask one person.
- E019 done: about 25:10, Wes 57%. Steering wheel/horn (2009) + daughter 'kicking your seat'; 'I've got it' shoulder; Mr. Abernathy 'What's it guarding?' (two taps); foothold = climbing bump; divorced composite 'Astros people'; contractor 'hat weather'; hotline in description.
- E020 done: about 15:55, Wes 58%. Car-care Saturday (14 oil changes, socket set = no-lesson story); bald tires = right anger; Mark 3:5; knee fear 'end up like Dad'; 'Is Mom okay?'; son 'scared i'm not good at this'; 20-minute rule taught by Jonathon (counselor, year three).
- E021 done: about 25:05, Wes 52%. Nephew's 1:14 'how do you stop' (single man first); 'Does God hate me?'; Jonathon 'I've been there' (NEW CANON flagged, fallback line provided); Wes's drift now (tractor videos, radar, 'You're doing the fog again'); Dani's dad's golf; Prov 4:23; B plug ch9; 988 + SAMHSA; porch, asleep mid-sentence.
- E022 done: 13:09, Wes 47%. Jonathon checks Wes first ('Forgot or drifted?'); Mom prays at her own table (11 by name, 'truck situation'); bath-time shark; nephew slip told in 40 min; Ps 90:12 (J), 56 days a year; four phone settings, gray radar.
- E023 done: 25:39, Wes 52%. Two Gardens. 1 Cor 15:45 (W) + John 18:8 'let these men go' (J). The fish (dad's redfish photo; 'in the trees'; date = Easter Sunday night); 'I needed you at four o'clock' (2018, five hours, untold); Ruby 'Do you have a dad?' / 'ask Mom' (owed); kid-side read; twin strikes out, 'brave swing'; twin's dad 'I froze'; brother in the barn, 'Tuesday after.'
- E024 done: 14:03, Wes 47%. Good Friday + season review. Order varied (question first). Dad's radio noon to three; oldest son goes first on the job site; John 19:30 (J); Ruby 'Why do I have to be the mean people?' answered by Jonathon; 4:10 call (rolls); twin's dad late but 'there to her'; What stuck = what each saw change in the other.
- Polish pass + round 5 (E017-E024): canon fixes in E023/E024, ask-tic variety, deadpan trim (E020), 'family rule' trim (E021), beat density, mechanic rotation. Season-to-date Wes 55.5%. Lint clean E001-E024.
- Batch 4 rotation (proposed): outros E025 B, E027 C, E029 D, E031 E; Field Notes E026 F1, E028 F2, E030 F3, E032 F4; sub-mid bank E025 5, E027 6, E029 7, E031 8.
- E025 done: 25:29, Wes 45%. The Father Who Stays. Matt 3:17 (J), B plug ch10. Easter lunch, Mom's "He sent me one too"; friend request accepted 9:40, father liked the bluebonnet photo 9:52; "well done" = Beaumont manager; "I'm glad you're mine. Not because of anything."
- E026 done: 13:38, Wes 51%. Easter Week Report. Wes's wife wrong (round 5) and owns it; the brother call (1h04m, recliner, nobody asked Mom); Mark 9:24 (W); tool: the Saturday walk.
- E027 done: 25:06, Wes 52%. The Empty Chair. Eph 6:4 (W), B plug ch8. The whole Saturday told once (lamp, dent, "Be good for your mom"); Wes's shoes; truck paper "NO MORE CONDITIONS"; the divorced Sunday-text man (round 5, unresolved).
- E028 done: 13:04, Wes 45%. The Chair Report (April order change: check, tool, question). Ruby's sentence; Dani wrong and unsettled; oldest son "I used to hand you the brush"; glove-box programs; Eph 4:29 (J). Expanded from 10:53. Father left unnamed ("Grandpa lives far away").
- 2026-10-03 00:10 CT: box moved to a fresh instance. E025-E028 verified on disk, complete, linted clean. Batch 4 continuity for E025-E028 added to both host briefs. E029 draft was lost in the move and is being rewritten.
- E029 done: 27:54, Wes 55%. When Your Dad Is Still Alive. Ex 20:12 (J), no plug. "Well. I'll let you go." (planted for E031's Jacob); Jonathon has never called his dad, the hurricane call; honor = weight; Mom's eleven seconds and the church apartments ("Because he bought a chair" / "I'm keeping the recliner"); Dad's A&M scholarship; Jonathon calls Wed 7:30 from the truck, "Not yet."
- E030 done: 13:33, Wes 52%. Calling Him Back. Rom 12:18 (W); tool: the two-call rule. "Who died?"; the grandfather's name kept off mic for Ruby; offshore and fishing, the rods; no apology; "Not yet"; "She looks like your mama"; "I just did." Jonathon mad, not sad. Wes to his oldest: "For what?" Wes's wife and her sister, Fredericksburg in May (round 5 beat done). Nephew rests.
- E031 done: 25:24, Wes 48%. When Home Never Handed You Off. Luke 2:49 (J), T plug session 11. Wes's mom in the driveway with a laundry basket ("Your daddy's not going to say this"); Jonathon's list ending in "Not bad, kid" (and he said "Not bad" to his rep); Mom's AC, "her guy vs her son"; Ruby hears the grandfather's name, "Can we go fishing?" / "You could learn"; Wes's stock-tank offer, "Maybe"; Wes's one on-mic affirmation, unanswered.
- E032 done: 13:13, Wes 50%. Cutting the String. Phil 2:4 (W); tool: the Sunday call. The rep (31, single; round 5 single man over 30) and his mom's 7:15 call, "Her best friend's name is Pat"; Wes's brother: "Nobody stands in the driveway for the one who stays"; nephew "i said you. dont make it weird"; Wes's pay-phone truck call (2000); Mom: "You can still come Sunday."
- Polish + round 6 (E025-E032): beat budget enforced (E025 8, E027 9, E028 7), E030 call 12 min (no number motif), lint now WARNs on beats. Season-to-date Wes 54.1%. Lint clean E001-E032. Host briefs updated through E032.
- Batch 5 rotation: outros E033 A, E035 B, E037 C, E039 D; Field Notes E034 F1, E036 F2, E038 F3, E040 F4; sub-mid bank E033 1, E035 2, E037 3, E039 4. Verse readers alternate (E033 W, E034 J, E035 W, E036 J, E037 J, E038 W, E039 W, E040 J).
- Box move (Oct 3, 12:09 AM CT): fresh instance. E025-E028 re-verified complete + lint clean; E029 rewritten after loss. Canon fix: Jonathon's mom is in Pasadena (3.5 h from north San Antonio), not 40 min. E031 AC scene now a FaceTime from the Bluebonnets dugout; E032 Thursday part with no FaceTime, Sunday drive to Pasadena; the rep's mom moved to Corpus Christi. Host brief corrected. E031 25:40, E032 13:21, both clean.
- E033 done: 25:42, Wes 45%. Leave Without Slamming the Door. Gen 2:24 (W), B plug ch12, outro A, sub-mid 1. Truck paid, donuts "These are good" (payoff of E032), paper in the visor, two honks, "Wes. Come inside."; Bluebonnets forfeit win (1-4*); Jonathon's Pasadena Sunday, three questions, Thursday ladies/Bev, watercolor, "I don't know what I'm for"; Dani wrong ("Your mom's fine"); "For, not from"; "I commuted", "Who's your wife, Jonathon?", counselor "Dani's always fine", moved to San Antonio for Dani's job before Ruby; divorced man and his ex-mother-in-law (round 6); Go First: Ruby's watercolor Saturdays at ten (video), Wes's phone in his wife's purse Fri. China cabinet 51 in. Lint clean.
- E034 done: 13:52, Wes 46%. The Door Report. Matt 5:37 (J, oath context stated); tool: thank you, no, I love you; outro F1. ORDER CHANGE (May rule): question, tool, then check. The lot next door ("I'm moving to Ohio"; "Is this about the pantry?"; patio home twenty minutes away). Jonathon's first no was the AC; off Mom's phone plan (account "The Kids", sister still on it). Wes's curfew night (moved to Thu Apr 29 in E033): "same page since nine" / "It was a good page" / son: "Cool." Apartment visit Sat May 8; Fredericksburg Mon-Wed May 3-5, laminated list. Lint clean.
- E035 done: 25:22, Wes 55%. Your Mom, Mother's Day, and Being a Grown Man. Prov 23:22 (W), Work for God's Pay (Col 3:23-24 paraphrased, inheritance), no plug, outro B, sub-mid 2. Fake fern ("It's doing great"); Ruby's watercolor lesson, "That's right. I needed three."; Jonathon's car-trade confession ("That's despise"); WIDOWER Merle (71) introduced at car-care, wants to sing bass in a quartet again, needs three men (carry to E037); orange-slice deacon; Dani on the hardest room; Jonathon takes divorced-dad Mother's Day; pot pie ("store crust"), happy Mother's Day to his sister; Wes rehangs Mom's screen door Sat May 8. Bluebonnets lost May 1 (1-5*), make-up Thu May 6. Host affirmation removed in E033 ("it counts") and E035. Lint clean.
- E036 done: 13:25, Wes 46%. Mother's Day Field Notes. Prov 31:28 (J, NIV colon kept on card); tool: a handwritten note; outro F2. BLUEBONNETS REAL WIN (Thu May 6 make-up, ugly; scared twin "holding a door for the ball", Harper's unnecessary headfirst slide into the umpire's shoe; Ruby struck out twice) 2-5 no asterisk. Fern: "It's been a hard week for both of us." Wes's sentence to Mom: "Took you long enough"; she measured the wall herself, 53 in. Merle found a baritone in Llano (80). The twin's dad: mom in memory care, "You have kind eyes. My son had kind eyes.", "We never once went to school hungry." Lint clean.
- E037 done: 25:13, Wes 52%. A Man With No Brothers. Eccl 4:10 (J), Acts 2:1 paraphrased (Pentecost), Stop Waiting, no plug, outro C, sub-mid 3. Pot pie "Store crust" / "Tell your sister thank you"; sister's note ("Who wrote this for you?", pantry, hug); apartment visit (53.25 in, Ola, Mom signed for the August unit); SCREEN DOOR: older brother held it an hour, "Who do you talk to?" "Dad... at the barn... Not much. Same as always." "Two brothers and no brothers"; Wes to the barn Saturdays at six; Jonathon's contacts ("Harper's Dad", "Twins Dad"), the hired movers; twin's dad = Brent, the card read by a nurse ("That's a nice boy"); Merle's "Bass seeks three" card, youth-pastor tenor, need a lead. W13 Homer overlap flagged and avoided. Lint clean.
- E038 done: 13:03, Wes 48%. Season Review: The Father Who Stays (end of Season 3). Josh 4:6 (W, mid-sentence card exact); tool: memorial stone, one line; outro F3. Harper's dad = Shane ("You don't know my name."; the battleship Texas in his garage; "Shane Texas"); Wes's little brother ("Is this the show?" "My knees."; father-in-law dying, Abilene; Wes goes May 29); nephew "asking for me" / "day fifty nine btw"; Wes: "He got the man"; Jonathon: still mad, no new contact, fishing in June at the stock tank; What stuck first-person only (Wes still passes on praying aloud). Stones: "Dad stayed. So did my brother." / "We learned his name." Lint clean.
- Box interruption #2 (Oct 3, 12:59 AM CT): E038 re-verified complete and lint clean; E039 drafts survived in /workspace/tmp/e039.
- E039 done: 25:12 approx, Wes 50%. Ask the Man (Season 4 premiere). Prov 13:20 (W), Stop Waiting, T plug session 14, outro D, sub-mid 4. Green banker's lamp ("I'd like to see the page"; "She had a coupon."); Ruby's three arms on purpose; barn: brother "Same time next week?"; Mr. Abernathy middle story: nineteen days, "I'd like you to ask me again", "Thursday. Six o'clock...", notebook dated the breakfast morning, "Otherwise it's my breakfast, not yours"; Jonathon's man ahead = Dani's dad ("How did you stay?", Sun May 23); Wes's = the 81-yo mechanic ("How do you get old without getting small?", Wed May 19). Beats at 10 (limit). Lint clean.
- E040 done: 13:03 approx, Wes 50%. Field Notes: The Ask Report. Prov 15:22 (J), F4 reworded to E041. Mechanic: "No, thank you" / "I'm not a talker" / "Black. One sugar." / "You're not getting small." Dani: "giving him the door before he's in the room." Ruby glued one rivet on Shane's Texas. Oldest son's foreman: "Ask me tomorrow" + notepad (E077 hold). Sunday-text man's last allowed appearance, unresolved. Jonathon's old "Catch me later" no. Lint clean.
