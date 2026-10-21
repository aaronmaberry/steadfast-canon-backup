# LOCKED: Aaron signed 2026-10-02 10:38 CT. Applies to all Wes videos.

# Steadfast Men: Wes Hart stage-movement rules (DRAFT, for Aaron's sign-off)
Status: DRAFT 2026-10-02. Nothing in here has been rendered. No credits spent.
Set: the locked still `stage-stills/wood-v5-comp.jpg` (1376×768). Wes is on the camera-left side in front of the reclaimed wood wall, and the stool and podium are on camera-right.
Audio: these rules sit on top of `LOCKED-LECTURE-STYLE.md` (the pause codes and the voice). They never change the audio.

**Directions are always camera-left / camera-right** (as the viewer sees it). The earlier draft said "stage-left". In theater terms Wes is actually on stage RIGHT, which is house left, so "stage-left" was wrong and is dropped.

---

## 0. Realism (HARD rules, Aaron 2026-10-02). Any fail blocks the clip.
A clip that fails any item below never reaches Aaron.

| # | Rule | Pass means |
|---|---|---|
| R1 | **Feet on a real floor** | Every planted or stance foot is in contact with the carpet, with no daylight under the sole. Each step rolls heel to toe. A loaded stance foot does not slide (it drifts ≤ 2 px at 1080p while weight is on it). No floating and no skating. Steps are 0.6–0.75 m at 80–95 steps/min, matching slow adult gait (0.82 m/s slow pace, Murtagh 2021 meta-analysis). |
| R2 | **Shadows match the props** | There's a tight dark contact shadow under each sole, plus a soft cast shadow. That cast shadow matches the stool's and podium's shadows in the same frame for direction, length, and softness. The shadow travels with the foot. A generic blurred blob doesn't count. |
| R3 | **Light on Wes = light in the room** | The key comes from the same top-front lights that make the warm pools on the wall. Wes's color temperature matches the wood. His brightness falls off the way the wall does: brighter as he walks into a wall pool, darker in the gaps. The carpet bounces warm fill onto his shoes, shins, and under his jaw. Top light puts a rim on his hair and shoulders. |
| R4 | **One camera, one grain** | Wes and the set share the same grain, sharpness, and black level. The clip runs at 24 fps with a 180° shutter, so hands and feet carry natural motion blur. No plastic skin, swimming wood or carpet texture, or morphing fingers or teeth. |
| R5 | **No cut-out look** | No halo, matte line, color fringe, or "ghost" of another background around his hair, beard, hands, henley, or shoes. |
| R6 | **Depth and occlusion are right** | His scale is right for the podium (the podium top sits at about his lower chest). When he walks behind the stool or podium, they hide him correctly. His feet never pass through a stool leg. |
| R7 | **Set and identity locked** | The planks, stool, podium, and Bible don't move or change between frames or segments. His face, beard, charcoal henley, jeans, and shoes stay identical across segments. |
| R8 | **Lip sync** | Master audio is the locked mix. Picture may sit up to 40 ms behind the sound or up to 60 ms ahead of it (EBU R37 tolerance). Faces stay within about 30° of the lens on speaking shots, because lip sync breaks past that (walking-lipsync-tools.md, Kling note). |
| R9 | **Stage edge** | His feet stay at least about 0.5 m upstage of the stage lip, never closer than the podium's front line. |
| R10 | **No crowd with Wes** | Never put Wes and a moving crowd in the same shot. No audience SFX, ever. |

### QA checklist: every test clip must pass all of these before Aaron sees it
Free tools only: ffmpeg frame dumps, 400% crops, and a numpy high-pass check.
1. **Feet, frame by frame.** Dump every frame of each walk and each plant start and end. For each stance foot, confirm sole contact, heel-to-toe roll, and drift ≤ 2 px while loaded. One sliding or floating frame = FAIL.
2. **Contact and cast shadow.** Check every 6th frame. A contact shadow must be present. Draw a line along the stool-leg shadow and the podium shadow; Wes's cast shadow must run within about 15° of it and be about as soft. FAIL if it's missing, a blob, or pointing the wrong way.
3. **Edge, halo, and matte line.** Check 400% crops of hair, beard, fingers, sleeves, and shoes on 10 random frames plus every fast-hand frame. Any light or dark outline, fringe, or old-background texture = FAIL.
4. **Light direction and level.** Compare the brightness of his face and shoulders with the wall right behind him at three positions on his path. He has to brighten and dim in the same direction as the wall. The shadow side of his face must face away from the wall pools. FAIL if not.
5. **Color.** Sample a henley patch and a skin patch against a wood patch. They must sit in the same warm white balance, with no cool or green cast on Wes.
6. **Grain.** Measure high-pass noise (image minus a 1.5 px blur) on a flat henley or skin patch and on a flat wall patch. The ratio must be between 0.75 and 1.33. Motion blur must be present on walking feet and fast hands. FAIL if Wes is cleaner or sharper than the set.
7. **Edge of stage.** Feet stay behind the podium-front line in every frame (R9).
8. **AI-slop sweep.** Watch at 100% at full speed, then at 25%. Any finger count change, texture swim, face drift, prop drift, or garbled Bible text readable on screen = FAIL.
9. **Lip sync.** Spot-check 5 hard consonants (p, b, m) per clip against the waveform, within ±40/60 ms.
10. **Movement-rule check.** Confirm the clip matches its beat-sheet tags: planted before every key line, holds frozen, podium and stool timing right (Sections 1–3).

### The locked still checked against this list (honest)
The still is a cutout composite. Per `comp/build.py`, Wes's pixels were lifted from the earlier wood-v2 frame and moved 241 px left. The stool and podium were moved 130 px right with a 50 px blended seam. His "shadow" is a synthetic blurred ellipse (120×14 px, 45% darkening).
- **Feet / R1: soft FAIL.** Both shoes sit close to the carpet, but there's no tight occlusion line under the soles. At 4× zoom the front shoe reads as slightly hovering.
- **Shadows / R2: FAIL.** The ellipse is a uniform smudge. It has no direction and doesn't match the stool's or podium's shadows.
- **Stage edge / R9: FAIL.** His soles end at about y 699 and the stage lip is at about y 702–705 (of 768). He's standing right at the lip, downstage of the podium's front line.
- **Edges / R5: PASS at the resolution we have.** No halo was visible at 3–4× on the torso, arm, hand, or head. It still needs a 400% check on any upscaled or 1080p version, because his edge pixels carry the old frame's background.
- **Light and color / R3: PASS with a caveat.** He came out of the same generated set, so his warmth and key direction (top-front, from camera-right) are plausible. But he was lit for a spot 241 px (about 18% of the frame) further right, so the falloff isn't truly his new spot.
- **Grain / R4: FAIL against "film".** No real grain anywhere. The whole frame has the generator's clean look: slightly smoothed skin and a squiggly AI carpet pattern.
- **Set seam: CHECK.** The prop-shift seam sits at about x 725–775. A few plank joints and a smudge at the baseboard there need Aaron's eye.
- **Resolution.** 1376×768 is below 1080p, and upscaling can add an AI sheen.
- **Bible: MISSING.** The podium top is empty. See rule 6.
- **Bottom line:** fine as a look reference, but it would not pass the Realism QA as a final frame. Fixing it is an edit, and that edit goes to Aaron for approval first. Nobody has edited or generated anything.

---

## 1. Stage map (from the locked still, 1376×768 frame)
Scale: Wes is 619 px tall, about 1.83 m, so roughly 340 px = 1 m at his depth. About 4 m of stage is visible.

| Mark | Where (x px) | Use |
|---|---|---|
| **H** Home | ~470 (where the still has him), feet ~0.3–0.5 m upstage of the still's foot line | Stories, personal asides, welcome |
| **C** Center | ~700 | Teaching points, key lines, closer |
| **F** Forward-right | ~820 | "What you do next" / application lines (the future side) |
| **P** Podium | ~1090, standing behind it | Scripture reads only |
| **S** Stool | ~960 | One personal story per session |

Distances: H→C is about 0.7 m (1–2 steps). C→P is 2–3 steps, going upstage of the stool. H→P is 3–4 steps (about 2.5–3 s). Keep him at least about 0.4 m inside both frame edges.
Story on camera-left matches the coaching rule: past on the audience's left, future on the audience's right (Fripp; Port, *Steal the Show*). The set already puts home base on camera-left, so the set and the rule agree.

---

## 2. The rules

1. **Plant first, then speak.** Every section opens planted, and he stays still for the welcome, with the first line spoken from a plant. *Why: stillness gives the opening words weight.* Sources: Fripp ("for your opening remarks, stand still"); Orator ("Walk to your spot, plant, breathe out, then start").
2. **Move on transitions, plant on points.** He walks only on a topic change, a section start, a story setup, or a non-key setup line. He stops, feet planted, **≥ 0.5 s before the first word of any key line**, matching the locked 0.4–0.6 s pre-key pause. He never says a key line, punchline, verse, or creed line while walking. *Why: movement marks structure and stillness underlines the point.* Sources: Fripp ("point of wisdom… stand still… verbally underlining"); Quartz ("move on transitions, be still on key points"); Spoken with Authority.
3. **Pace and amount.**
   - A move is 1–4 steps lasting 1.5–3.5 s.
   - Speed is 0.6–0.9 m/s, steps are 0.6–0.75 m, cadence is 80–95 steps/min.
   - About **one move every 30–60 s**: 25–35 full moves plus 10–20 single re-angle steps per 22-min session.
   - Walking takes **6–12% of runtime**, so he's **planted 88–94%** of the time.
   - Each plant lasts at least 10 s between full moves.
   - At most 2 moves in any 30 s, and no back-and-forth ping-pong.
   - He never walks toward the lip on a heavy line or retreats upstage mid-sentence.
   *Why: deliberate moves read as intent, while constant motion reads as nerves and kills the contrast.* Sources: Murtagh et al. 2021 (slow walk 0.82 m/s); Orator ("continuous pacing reads as nerves"); Quartz ("retreating while speaking reads as withdrawal"). The counts come from W01 v2: 26 pauses of 1.0 s or longer plus 11 section starts, across 1,315 s.
4. **Zones carry meaning.**
   - Stories and self-tells: H (camera-left).
   - Teaching points and key lines: C.
   - "What you do Monday" lines: F.
   - Scripture: P only.
   - The most personal story: S (once).
   *Why: the room's spatial memory organizes the talk, with the past on the audience's left.* Sources: Fripp; Port; Quartz ("deliver the problem from one spot and the solution from another").
5. **Hands.**
   - Gestures are open-palm, inside the chest-to-waist "box", within shoulder width.
   - He uses illustrators that show size, contrast, or direction, rather than random beats.
   - **15–25 gesture strokes/min** in story and teaching, 0–3/min while reading, and ≤ 10/min (slower) in the closer.
   - The stroke's peak lands on the stressed syllable, about 0–200 ms early.
   - At rest: the ready position (hands loosely together at the navel) or relaxed at his sides for a few seconds.
   - Never: pointing a finger at the men, crossed arms, hands in pockets, face-touching, or fiddling.
   - Counting on fingers ("one plain day") is fine.
   *Why: popular TED talks used about 465 gestures per 18 min (about 26/min) against about 272 (about 15/min) for the least popular, open palms build trust, and a gesture that's off the stressed word looks dubbed.* Sources: Van Edwards / Science of People (TED study; "stay in the box"; pointing reads aggressive); Bowden (open palms at navel height); Leonard & Cummins 2011 and Kendon via Loehr (gesture apex aligns with the pitch accent); Rohrer et al. 2023.
6. **Podium and Bible (scripture reads).** An **open Bible lies on the podium all session**, and he reads each verse from it.
   - **(a) Approach.** Walk to P on the last non-key line before the reference (3–4 steps, about 2.5–3 s), passing upstage of the stool. Plant, with both hands resting lightly on the podium top either side of the Bible, ≥ 0.3 s before the reference.
   - **(b) Reference.** Say the reference **looking at the room** ("Luke sixteen, verse ten"). Eyes drop to the page in the locked 0.6 s pause after it, and his right index finger finds the line.
   - **(c) Reading.** He **reads it in place and never picks the Bible up** (a hand-held book across many AI segments is a known hand/object failure). Eyes are down about 75–85% of the read. He gets at most one glance up per phrase break, ≤ 0.8 s, and no head-bobbing. No gestures while reading; hands stay on the podium or the page edge.
   - **(d) Lift.** Eyes lift to the room on the verse's last 2–3 words. He holds the room through the locked post-verse hold (1.4 s), hands still on the podium.
   - **(e) Step away.** He may say one short echo line at the podium (e.g. "Very little.", finger on the page). Then he steps out 2–3 steps toward C on the next non-key line, and plants before the first teaching key line.
   - **(f) Limits.** Podium time is **12–25 s per verse**, with 3 visits per session, about **≤ 75 s, or ≤ 6% of runtime**, so it never becomes "talking head at a podium" (an Aaron fail). He never teaches from behind the podium for more than 2 lines. Later references to the verse get an open-hand gesture toward the Bible, not a walk back.
   *Why: real readers announce the reference to the people, keep a finger on their place, look up only to reinforce, and read rather than act. Stepping away from the lectern lets the room see the whole man.* Sources: Christ First Church reader guide ("look at the congregation, and announce the passage… keep your finger on your place… close your Bible, look up"); Clay Schmit via Calvin Institute ("Look up… only to reinforce… avoid the bobbing head… Read; don't act"); Quartz (a lectern "invites gripping and hiding; step to the side").
   **The still has no Bible on the podium.** Adding one is a still edit that goes to Aaron for approval before anything else happens. I haven't edited or generated anything. The camera sits near podium-top height, so the Bible would read as a low open book on the slanted top, and its text must never be readable on screen.
7. **Stool: once per session, for the most personal story** (W01 v2: "Let me tell on myself a little." at about 16:13).
   - He walks to S on the setup line, then sits half-on: one foot on the floor, one on the rung.
   - Gestures get smaller and slower. Story length is 60–120 s.
   - He rises on a non-key line near the story's landing, takes 2–3 steps to C, and plants before the teaching point.
   *Why: sitting changes the energy for the most intimate moment; doing it more than once flattens it.* Source: the earlier stool rule plus coaching on purposeful, rare moves (rule 3 sources). This is a convention, not a measured number.
8. **Pause behavior** (locked codes).
   - **Heavy-line hold (1.2–2.0 s):** full freeze. Feet planted, the gesture finishes on the stressed word, then hands settle. Eyes hold one section through the line plus the hold (about 3 s).
   - **ROOM_CHUCKLE (1.7 s):** a small smile and a ≤ 30° head-and-shoulder turn to another section. No step. **Wes doesn't laugh** (locked).
   - **ROOM_HANDS (3.0 s):** he raises his own hand on "Hands up" and scans 2 sections (about 1.5 s each) during the hold. He lowers his hand on the next line.
   - **Topic change (1.0–1.4 s):** the preferred time to start a move.
   *Why: matches the locked audio; stillness during silence is what makes silence read as weight.*
9. **Eyes.**
   - He works the room in 5 sections (left, left-center, center, right-center, right) plus the back row.
   - He gives **one thought per section, holding 3–5 s** (average comfortable mutual gaze is 3.3 s, most people prefer 2–5 s).
   - His eyeline is just off the lens toward the room, never at the floor except while reading.
   - **Lens: only in the closer, at most 1–2 lines, optional.**
   *Sources:* Binetti et al. 2016, *R. Soc. Open Sci.* (3.3 s mean); Science of People ("Lighthouse Technique" 3–5 s); Orator ("hold eye contact for a full thought").
10. **Closer (last 2–3 min).**
    - He walks to C on "Let me land this" and **stays planted to the end**, with no walking.
    - Gestures slow to ≤ 10/min. He gives an open hand toward the room on the send-off ("Go on and find your table").
    - The voice does **not** drop. That idea is struck, because the locked audio rules keep the same voice and volume and ban [quietly]. Weight comes from stillness and the already-locked pauses.
    *Source:* Spoken with Authority (return to center for the conclusion); LOCKED-LECTURE-STYLE rule 7.
11. **Camera coverage.**
    - Two framings from the locked set: **Wide** (locked-off, full stage including stool and podium) and **Medium** (knees or belt up).
    - The **medium carries 55–65%** of runtime. Church video teams target about 70% medium/close with the wide at 30%, but Wes's walking needs the wide.
    - **Every full move plays on the wide**, or cuts to the wide at the move's first step (cut on action).
    - Shots run 8–30 s, never over 30 s. That cap is set by the tools (30 s per 1080p generation) and by editing pace.
    - Cut only at a move start or a line boundary with ≥ 0.6 s of silence. Never cut mid key line or inside a heavy hold or ROOM_CHUCKLE; the reaction plays out in one shot.
    - Wide↔medium has to be a clear size change. Stay on one side of the 180° line, match the grade, use 24 fps with a 180° shutter, no zooms or pushes.
    - Optional room cutaways are separate shots with no Wes, ≤ 3 s, and only if Aaron approves (none by default).
    *Sources:* BoxCast church video guide ("70/30 rule… pay close attention to pauses in speech or transitions… avoid cutting… in the middle of a sentence"); APC video manual (sermon: hold longer, avoid excessive cuts); match-on-action guide (clear size or angle change, 180° rule, match light, 180° shutter).

---

## 3. Beat-sheet format (sidecar file; the audio file itself stays "nothing else in the file")
One sidecar per session: `<session>.beats.tsv`, with one row per script line in the same order. Times come from `final.words.json` of the locked mix.
Columns: `# | t_in | t_out | pause | text | BODY | HANDS | EYES | FACE | SHOT`

Tags:
- **BODY:** `PLANT@H|C|F|P|S` · `MOVE H>C 2st start@"word" plant-by@t` · `STEP` (one re-angle step) · `HOLD` (freeze through the pause) · `PODIUM-IN` · `READ` · `PODIUM-OUT` · `STOOL-SIT` · `STOOL-RISE`
- **HANDS:** `READY` (loosely together at the navel) · `SIDES` · `OPEN@"word"` · `ILLUS:<shape>@"word"` · `COUNT n@"word"` · `RAISE` / `LOWER` (his own hand) · `PODIUM` (resting on the top) · `PAGE` (finger on the line) · `TO-BIBLE` (open hand toward it)
- **EYES:** `L` `LC` `C` `RC` `R` `BACK` `PAGE` `LENS`, with `>` marking a sweep
- **FACE:** `neutral` · `warm` · `dry` · `smile-s` · `serious`
- **SHOT:** `W` / `M`; `CUT>W@t` or `CUT>M@t` on the row where the cut happens
- **Key lines** are marked `*` in column #. A `*` row must have BODY = PLANT or HOLD, never MOVE.

---

## 4. Worked example: W01 v2 "A Quiet Tuesday", 0:00–2:02
Source: `print-build/session-audio/W01-v2/sec01–02.timing.txt`. Times are from the locked mix `W01-A-Quiet-Tuesday-2026-10-01-v2.mp3` (`final.words.json`).
Note: W01 v2 opens "Hey. Come on in." That's not the "Alright. Hey. I'm glad you came." OPENING in LOCKED-LECTURE-STYLE.md. This example uses W01 v2 as asked.
Pre-roll: the editor adds 2.0 s of room tone before 0:00. Frame 1 is the locked still's mid-stride pose; he takes the last 2 steps and plants at H by 0:00.

```
#   t_in   t_out  pause  text                                                   BODY                                HANDS                         EYES      FACE    SHOT
0   -2.0   0.00   -      (pre-roll, room tone)                                  MOVE >H 2st plant-by@-0.3           SIDES                         C         warm    W
1   0.00   1.92   0.55   [warmly] Hey. Come on in.                              PLANT@H                             OPEN(both,small)@"in"         C         warm    W
2   2.64   4.28   0.8    Find a chair. Any chair.                               PLANT@H                             ILLUS:sweep-to-room@"Any"     LC        warm    W
3   5.12   7.08   CHKL   They're all about equally uncomfortable.               PLANT@H, CHUCKLE 7.1-8.9 half-turn  READY by "uncomfortable"      LC>RC     smile-s W
4   8.94  12.12   0.6    Some of you got here early and picked a spot ...door.  PLANT@H                             OPEN(toward back)@"door"      BACK      dry     CUT>M@8.8
5  12.90  13.88   0.75   I see you back there.                                  PLANT@H                             READY                         BACK      smile-s M
6  14.64  15.58   0.55   That's not fear.                                       PLANT@H                             OPEN(palm-up)@"fear"          BACK      dry     M
7  16.00  19.00   0.8    That's a man who has sat through a lot of meetings.    PLANT@H                             ILLUS:weary-palms@"meetings"  BACK>LC   dry     M
8  19.00  22.26   0.6    And some of you are here because a buddy asked...      PLANT@H                             ILLUS:thumb-over-shoulder     LC        dry     M
9  22.26  25.44   0.6    and you couldn't come up with an excuse fast enough.   PLANT@H                             OPEN@"fast"                   LC        dry     M
10 25.88  26.66   0.4    That's alright.                                        PLANT@H                             READY                         C         warm    M
11*26.66  29.08   0.7    You're in now, and I'm glad you came.                  PLANT@H                             OPEN(both)@"glad"             C         warm    M
12 29.08  33.30   0.3    And a few of you have never sat in a room like this...PLANT@H                             ILLUS:room@"room"             RC        neutral CUT>W@29.0
13 33.30  36.42   0.55   and you're wondering if somebody's about to make you hold hands. PLANT@H                    ILLUS:clasp-hint@"hold"       RC        dry     W
14 37.24  38.88   0.65   Nobody's gonna make you hold hands.                    PLANT@H                             OPEN(palms-out)@"Nobody's"    C         dry     W
15 39.30  41.28   1.3    Not today... anyway.                                   PLANT@H (button last)               READY                         C         smile-s W
16 42.72  44.12   0.55   Let me tell you who's in this room.                    MOVE H>C 2st start@41.4 plant-by@44.3 SIDES                       C         neutral W
17 44.90  47.08   0.55   Guys barely old enough to rent a car.                  PLANT@C                             ILLUS:low-hand@"rent"         L         warm    W
18 47.86  49.80   0.65   Guys carrying pictures of grandkids.                   PLANT@C                             ILLUS:wallet@"pictures"       LC        warm    W
19 50.66  54.08   0.3    A man whose house is so loud he came here for the quiet, PLANT@C                           ILLUS:L-hand@"loud"           RC        warm    CUT>M@50.4
20 54.66  58.08   0.55   and a man whose house got so quiet he came here for the voices. PLANT@C                     ILLUS:R-hand@"quiet"          R         warm    M
21 59.08  62.28   0.55   Single, married, divorced, a little of everything.     PLANT@C                             ILLUS:sweep@"everything"      L>R       warm    M
22*63.04  66.20   0.8    And every one of you belongs in the chair you're sitting in. PLANT@C                        OPEN(palm-down,firm)@"belongs" C        serious M
23*67.12  68.60   1.3    Nobody here is a visitor.                              HOLD 68.6-69.9                      OPEN@"visitor" -> READY       C (hold)  serious M
24 70.10  71.90   0.6    My name's Wes. Wes Hart.                               PLANT@C                             ILLUS:hand-to-chest@"Wes"     C         warm    CUT>W@70.0
25 72.58  74.18   0.3    I'm a husband and a dad,                               PLANT@C                             READY                         LC        warm    W
26 74.48  77.22   0.65   and I've spent a long time in rooms like this one.     PLANT@C                             ILLUS:room@"rooms"            LC        warm    W
27 77.30  80.88   0.7/.55 Usually toward the back, / closer to the coffee.       PLANT@C (button last)               ILLUS:thumb-to-back@"back"    BACK      dry     W
28 81.64  83.48   0.45   This is Steadfast Men.                                 PLANT@C                             READY                         C         warm    CUT>M@81.3
29*83.96  88.52   0.65   It's a room for men who'd like to be the same man on Tuesday that they are on Sunday. PLANT@C ILLUS:L/R-hands@"Tuesday"/"Sunday" C   serious M
30 89.32  92.78   0.75   And for the next half hour or so, we're gonna talk about one day. STEP@C turn-to-RC start@89.3 plant-by@91.6 COUNT 1@"one"     RC        neutral CUT>W@89.3
31 93.30  96.08   0.55   Not your wedding day. Not your best day.               PLANT@C                             ILLUS:brush-aside@"wedding"/"best" RC>LC neutral W
32 96.86  98.30   0.4    One plain day.                                         PLANT@C                             COUNT 1@"One"                 C         neutral W
33 98.76 100.48   0.8    The kind you couldn't pick out of a lineup.            PLANT@C                             OPEN@"lineup"                 C         dry     W
34 101.40 105.52  0.7    Because here's the claim, and I'd rather say it early so you can chew on it. PLANT@C        READY                         C         serious CUT>M@101.0
35*106.14 108.80  1.4    A man's life gets decided on a Tuesday.                HOLD 108.8-110.0                    OPEN(palm-down beat)@"Tues-" -> READY  C (hold) serious M
36 110.00 111.92  0.55   Now, I don't mean the calendar.                        MOVE C>H 2st start@110.0 plant-by@112.4 SIDES                    L         neutral CUT>W@110.0
37 112.60 115.20  0.65   If your Tuesday is a Thursday, that's fine.            PLANT@H                             OPEN(shrug)@"fine"            L         dry     W
38 115.96 118.12  0.6    I mean the day with nothing on it.                     PLANT@H                             ILLUS:empty-palms@"nothing"   LC        neutral W
39 118.66 121.68  0.8    No ceremony. No camera. No crowd.                      PLANT@H                             COUNT 1-2-3@each "No"         LC>C      neutral W
```
Example totals for 0:00–2:02: 2 moves plus 1 re-angle step, plus the pre-roll walk-in (one every ~35–40 s). Walking is about 7.6 s, 6% of runtime, with every key line (*) planted. Shots: 9, each 8.0–21.4 s; wide 54% and medium 46% (the opening has more moves than a session average; the 55–65% medium target is for the whole session). Gesture anchors are tagged 4–8/min; the performer or model adds the free beats on top, up to 15–25/min.

### Mini example: first podium visit (3:50–4:16)
```
#   t_in   t_out  pause  text                                         BODY                                  HANDS                 EYES          SHOT
44 217.91 220.49  0.65   Hands up if you've ever made a New Year's resolution. PLANT@C                     RAISE@"up"            C             M
45 221.33 222.63  HANDS  Go ahead, get them up.                        PLANT@C (hold 222.6-225.4)          raised                LC>RC (~1.5s each) M
46 225.39 228.73  0.75   Okay. Keep it up if yours made it to February. PLANT@C                             LOWER@"Okay"          C             M
47 229.32 230.08  0.45   Yeah.                                         PLANT@C                             READY                 C             M
48 230.48 232.88  1.2    That's about what I figured. Put them down.   MOVE C>P 3st upstage of stool start@230.5 plant-by@233.6  SIDES -> PODIUM  RC  CUT>W@230.4
49 234.30 235.68  0.6    Luke sixteen, verse ten.                      PODIUM-IN, PLANT@P                  PODIUM                C (room) -> PAGE in pause  W
50 236.94 241.48  .25/.25 Whoever can be trusted with very little / can also be trusted with much, READ        PAGE                  PAGE, glance C 241.5-242.1  W
51 242.18 246.88  .3/1.4 and whoever is dishonest with very little / will also be dishonest with much. READ -> HOLD 246.9-248.3  PAGE  PAGE, lift on "with much", hold C  W
52 248.44 249.44  0.55   Very little.                                  PLANT@P                             TO-BIBLE (finger on page)@"little" C        W
53 249.86 253.82  0.8    Jesus could've said, whoever can be trusted on the big stage. PODIUM-OUT 2st P>C plant-by@254.3  OPEN@"big"  LC  W
54*254.78 255.34  0.4    He didn't.                                    PLANT@C                             READY                 C             W
55 255.90 257.80  0.7    He went straight for the small stuff.         PLANT@C                             ILLUS:small@"small"   C             CUT>M@255.6
```
Podium dwell is 233.6–249.9, about 16 s (within the 12–25 s rule). That wide shot runs 230.4–255.6, 25.2 s, under the 30 s cap.

---

## 5. What today's tools can actually execute from ONE still (no spend recommended)
- **HeyGen photo avatar (Avatar IV):** gives lip sync plus in-place head, shoulder, and hand motion. It **cannot walk**, so rules 1–4, 6(a)/(e), 7, and 10's move don't happen. It roughly follows rules 5, 8, and 9 at best (gestures and holds come from a motion prompt, not tied to exact words). Worse, the locked still is **mid-stride**. An in-place avatar would keep his legs frozen mid-step, which is an obvious fail. Using HeyGen would need a separate standing still, and that's a new image for Aaron to approve. It would also be "static talking head", which is a fail on its own.
- **OmniHuman 1.5 (fal):** the only one-image tool that walks and lip-syncs in one step. Clips max out at ≤ 30 s at 1080p (≤ 60 s at 720p). Movement is prompt-driven, so **exact plant timing (rule 2), step counts, the path behind the stool, podium reading with a finger on the page, and sitting on the stool cannot be guaranteed**. Identity drift and small-face lip-sync mush in wides are reported. The Realism QA (feet, shadows, grain) would have to be checked on every segment.
- **Precise rule-following needs a real performer** (Kling 3.0 Motion Control / Runway Act-Two / Wan Animate, ≤ 30 s per segment, driven by a filmed person). A person performing this beat sheet is the only route that reliably hits plant-before-key-line, the 3–5 s eye sections, podium/Bible behavior, the stool sit, and real foot contact. It needs a performer and a stage day.
- **What that means for the shot plan:**
  1. Every shot is ≤ 30 s, so a ~22-min session is about 50–60 shots cut wide/medium. Rule 11's cut points double as segment seams.
  2. Moves live on the wide, where the face is small, so lip sync matters less there. Key lines live on the medium.
  3. Podium and stool moments are the hardest shots, and they're where tool limits bite first.
  4. Before any test: Aaron approves the Bible edit to the still (or a re-plate that also fixes the shadow and the lip distance). Nothing is to be generated or edited without his yes.

---

## Sources
- Patricia Fripp, PBS *Side by Side with Nido Qubein*: pbs.org/video/patricia-fripp-leadership-coach-ng46pe
- Quartz, "25 presentation skills…": qz.com/presentation-skills-people-never-develop
- Orator, "Body Language for Public Speaking": theoratorapp.com/blog/body-language-for-public-speaking
- Spoken with Authority, "No Lectern or Table on Stage?": spokenwithauthority.com/blog/no-lectern-maximize-space-and-impact-on-stage
- Michael Port, *Steal the Show* (past on stage right/audience left): marketingspeak.com/dont-just-speak-perform-with-michael-port
- Binetti et al. 2016, "Pupil dilation as an index of preferred mutual gaze duration," *R. Soc. Open Sci.* 3:160086; BPS Research Digest summary
- Van Edwards / Science of People: TED gesture study (TEDxLondon "You are contagious"; blog.ted.com body-language survey); scienceofpeople.com/hand-gestures; /body-language-business
- Mark Bowden (open palms at navel height): talkabouttalk.com/body-language-mark-bowden-191
- Gesture–prosody timing: Leonard & Cummins 2011 (via *Brain Research* N400 paper, apex about 200 ms before the F0 peak); Loehr, *Laboratory Phonology* (degruyter lp-2012-0006); Rohrer, Delais-Roussarie & Prieto 2023, *Lingua* 293
- Walking speed: Murtagh et al. 2021, *Sports Medicine*, "Outdoor Walking Speeds of Apparently Healthy Adults" (slow 0.82 m/s; usual 1.31 m/s, 117 steps/min)
- Scripture reading: Clay Schmit via Calvin Institute of Christian Worship, "Ten Tips for Reading Scripture in Public Worship"; Christ First Church (Charleston, IL), "Guide for Public Scripture Reading"
- Church video: BoxCast / Christ Church Fairview Video Team Guide (70/30 rule); APC Video Production Training Manual; match-on-action guide (flashboards.yaroflasher.com/learn/editing/match-on-action)
- Lip-sync tolerance: EBU R37 (audio up to 40 ms ahead / 60 ms behind picture), quoted from memory and not re-fetched this session
- Internal: LOCKED-LECTURE-STYLE.md; research/podium-pauses.md; grok/W01-v3-speaker-research.md; research/walking-lipsync-tools.md; stage-stills/comp/build.py
- **Not measured:** Tim Hawks, Andy Stanley, Matt Chandler, and Louie Giglio footage. A free low-res download of a public Tim Hawks sermon for frame timing was started and then interrupted, and it wasn't retried. The numbers above come from coaching and research sources, not from timing their footage.
