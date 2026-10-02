# Pause and breath techniques for ElevenLabs `eleven_v4`

Voice: "Wes Hart - Option D". One take per `# SECTION`.

## How the pipeline already handles pauses

- `prep.py` joins every line inside a paragraph into one run of text. It starts a new prompt paragraph after any line whose pause is 1.0 or more (`ROOM_HANDS` counts as 3.0, `ROOM_CHUCKLE` as 1.7). So the model never sees our line breaks inside a paragraph. It only sees paragraph breaks.
- `retime.py` then sets the silence at every line boundary to the `|pause` value. Whatever gap the model leaves at a line break gets replaced in post.
- So an in-take technique only changes the sound in two places:
  1. **Inside a line**, where `retime.py` has no boundary to work with.
  2. **In the intonation leading into a line boundary**, for example whether the voice trails off or lands. `retime.py` sets the gap after a line but can't change how the line ends.

The pause the take controls on its own sits mid-line. Everything at a line boundary already belongs to post.

## Recommendation (used in all 24 training sessions)

**Keep the approved method, post silence from `|pause` through `retime.py`, as the main tool. Add one in-take technique, the ellipsis, sparingly.** Don't use bracketed pause or breath tags.

### 1. Post silence through `|pause` (main tool, unchanged)

- **What it does:** sets an exact silence at each line boundary.
- **When to use it:** everywhere. The build sets these values by line type:

  | Line type | Pause (seconds) |
  |---|---|
  | Short punch line | 0.4-0.55 |
  | Ordinary sentence end | 0.55-0.8 |
  | Clause carried into the next line | 0.25-0.45 |
  | Spoken reference | 0.55-0.65 |
  | End of a paragraph | 1.0-1.3 |
  | Last line of a section | 1.0-1.4 |

  `ROOM_HANDS` and `ROOM_CHUCKLE` are used only where the room really reacts.
- **Limit:** none. This is the backbone.
- **`prep.py`:** no change.

### 2. Mid-line ellipsis `...` (the chosen in-take technique)

- **What it does:** gives a short hesitation or comic-timing beat inside a line, something post can't place. Examples:
  - "Not today... anyway."
  - "the evening just sort of... happens."

  On the v3/v4 family, an ellipsis is the most dependable way to get a natural held beat with no tag. The voice stays the same and so does the volume, which is the rule from `podium-pauses.md`.
- **Also allowed at a line end**, when the thought carries into the next line, as in "because a buddy asked..." followed by "and you couldn't come up with an excuse fast enough." Here the ellipsis doesn't set the gap; `retime.py` does that. It keeps the intonation open so the voice doesn't land on a false sentence end. The build gives these lines a 0.5-0.6 pause.
- **When to use it:**
  - just before a word Wes is choosing ("sort of... happens");
  - just before a dry tag at the end of a joke ("Not today... anyway").

  Never use it on scripture, the creed or the questions, and never put it next to an "uh" or "um" in the same line.
- **Limit:** at most 1 mid-line ellipsis per section, at most 2 ellipses of any kind per section, and at most 4 per script. `meta/tools/lint.py` enforces all three.
- **`prep.py`:** no change. The text passes through as written. `check.py` doesn't count it as a tag, and the word count ignores it.

### 3. Paragraphing (structural, already in use)

- **What it does:** a pause of 1.0 or more ends a prompt paragraph in `prep.py`. v4 treats a paragraph break as a reset and a breath, so a new thought starts fresh instead of rushing on from the last one.
- **When to use it:** at every real turn in the thought, about 3-5 per section. Don't break after every sentence, or the take turns choppy.
- **`prep.py`:** no change.

### 4. Restart dash `you— you` (existing; disfluency, not a pause)

- **What it does:** a cut-off and restart. v4 renders a short break in the voice.
- **Limit:** 3 per script at most, from the brief. Most of these scripts use self-repairs in plain words instead ("Well, closer to seven."), so the dash is rare.
- **`prep.py`:** no change.

## Considered and not used

- **`[pause]`, `[short pause]`, `[long pause]`:** they add nothing at line boundaries, because `retime.py` overwrites that gap anyway. Mid-line, the length they give varies from take to take. Bracketed words can also get read aloud or change the delivery of the words around them, and every extra tag makes takes less stable. `check.py` would also count them as tags, and the brief limits tone tags to `[warmly]`, `[dry]` and `[amused]`.
  - If Aaron still wants to try them, `prep.py` passes them through untouched.
  - The only change needed is in `check.py`: leave `pause`, `short pause` and `long pause` out of the tag count.
  - Not applied: `pipeline/` stays untouched.
- **`[exhales]` and `[sighs]`:** on a sustained teaching voice they tend to come out as a staged, audible breath, like a mic change or a pasted-in edit. Aaron flagged exactly that sound on the `[quietly]` lines. A section's breath already comes from paragraphing. If testing ever shows a clean result, use one at most per script, at a heavy turn. Not used.
- **SSML `<break>`:** v4 ignores it.
- **Anything soft or whispered:** never.

## Where it's used

Generated from the final scripts. Every line also carries its post-production `|pause`; the holds column counts lines whose post pause is longer than 1.4 s (mostly the hold after a verse). Paragraph breaks give the breaths and aren't listed.

| Script | Ellipses | Where (section, file line) | ROOM_HANDS | ROOM_CHUCKLE | Holds over 1.4 s |
|---|---|---|---|---|---|
| W01 | 3 | §1 L9 "because a buddy asked..." (line end); §1 L16 "Not today... anyway." (mid-line); §2 L44 "evening just sort of... happens." (mid-line) | 1 | 4 | 0 |
| W02 | 1 | §5 L163 "So I just... don't." (mid-line) | 1 | 2 | 0 |
| W03 | 0 | none: post silence and paragraphing only | 1 | 3 | 3 |
| W04 | 0 | none: post silence and paragraphing only | 0 | 4 | 3 |
| W05 | 0 | none: post silence and paragraphing only | 0 | 4 | 3 |
| W06 | 0 | none: post silence and paragraphing only | 1 | 3 | 3 |
| W07 | 1 | §7 L235 "I was just... doing it for" (mid-line) | 1 | 4 | 4 |
| W08 | 1 | §10 L315 "And then he just... sat there," (mid-line) | 0 | 4 | 3 |
| W09 | 1 | §12 L373 "better than scared alone... in a parked" (mid-line) | 0 | 4 | 3 |
| W10 | 2 | §1 L18 "things get heavy, I..." (line end); §11 L378 "looking back at him like... well, like" (mid-line) | 0 | 4 | 3 |
| W11 | 1 | §11 L375 "tried to answer him... and nothing" (mid-line) | 0 | 3 | 3 |
| W12 | 1 | §8 L284 "then she said, well... I'll bring" (mid-line) | 0 | 4 | 3 |
| W13 | 2 | §2 L53 "list, top to bottom... twice." (mid-line); §8 L242 "And then they... stopped." (mid-line) | 1 | 3 | 3 |
| W14 | 2 | §1 L16 "the man I'd call is... and then a" (mid-line); §8 L239 "and the secret was... a kitchen" (mid-line) | 0 | 3 | 3 |
| W15 | 2 | §2 L43 "cinnamon roll with... a problem." (mid-line); §11 L352 "mouse had made some... poor choices." (mid-line) | 0 | 2 | 3 |
| W16 | 1 | §4 L121 "and he just... sat there." (mid-line) | 1 | 4 | 3 |
| W17 | 2 | §2 L46 "and it just... kept being" (mid-line); §6 L180 "and Sunday went... flat." (mid-line) | 1 | 4 | 3 |
| W18 | 1 | §9 L298 "looks at him and says... not good." (mid-line) | 0 | 4 | 3 |
| W19 | 1 | §3 L103 "and he says... nothing." (mid-line) | 0 | 4 | 3 |
| W20 | 1 | §9 L317 "which he says is... a little generous" (mid-line) | 1 | 4 | 3 |
| W21 | 1 | §4 L132 "exactly. He was more like... paused." (mid-line) | 0 | 3 | 3 |
| W22 | 1 | §5 L159 "hasn't eaten one in, oh... about twelve" (mid-line) | 1 | 3 | 3 |
| W23 | 1 | §9 L299 "the first time in, oh... years." (mid-line) | 0 | 4 | 3 |
| W24 | 1 | §9 L307 "I know... you'd rather" (mid-line) | 0 | 3 | 3 |
| **All 24** | **27** (25 mid-line) | | **10** | **84** | **67** |

## Test clip (W01 §1, "Come On In")

Section 1 runs 298 spoken words (1,506 characters). It contains one line-end ellipsis and one mid-line ellipsis, plus one `ROOM_CHUCKLE` after "equally uncomfortable." It ends on "A man's life gets decided on a Tuesday." with a 1.4 pause.

**What to listen for:**
- Does "Not today... anyway." land as a dry beat, without sounding like a stall?
- Does "a buddy asked..." carry into the next line instead of sounding finished?

**If the mid-line beat comes out too long on v4,** swap the ellipsis for a comma ("Not today, anyway."). That keeps the same line in the same take, so nothing else has to change.

These are recommendations, not measured results: no audio was generated on this run (no spend). Aaron's ear on this clip is the deciding test.

## Update 2026-10-01: fillers removed

"uh", "um" and "eh" are gone from all 24 sessions, and lint now fails on any of them. Each one became either a silent beat (the line splits there and the first half gets a 0.7 post pause, ending in a line-end ellipsis where the limits allow, otherwise a comma) or a short in-line restart ("how you'd, look, how you'd hire somebody"). The split adds line boundaries, so `retime.py` now places those beats. Every session now sits at the 4-ellipsis cap, so the "Where it's used" table above shows the ellipses from before this pass. `meta/FILLER-REPLACEMENTS.tsv` lists every spot.
