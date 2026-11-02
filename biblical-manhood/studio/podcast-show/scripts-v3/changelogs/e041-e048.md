# CHANGELOG, v3 rewrites (batch E041-E048)

These are rewrites of the first drafts in scripts/. The originals are untouched, and each v3 file keeps the same slug.

## Length overrides

The first drafts ran about 25 minutes for mains and 13-14 minutes for Field Notes, which matched the show bible's older caps. Each v3 file overrides its draft's Format length with the v3 brief's ranges. Mains run 45-60 minutes (about 7,000-9,000 words). Field Notes run 20-25 minutes (about 3,000-3,800 words).

| Episode | Draft length | v3 length | Spoken words | timing.py |
|---|---|---|---|---|
| E041 These Men Are My Brothers | about 25 min | about 55 min | 8,407 | 55:46 |
| E042 Field Notes: Memorial Day | about 13-14 min | about 21 min | 3,272 | 21:47 |
| E043 No Fixed Star | about 25 min | about 47 min | 7,184 | 47:38 |
| E044 Field Notes: Finding North | about 13-14 min | about 22 min | 3,328 | 22:13 |
| E045 Your Daughter Is Watching | about 25-26 min | about 52 min | 7,932 | 52:31 |
| E046 Field Notes: The Daddy-Daughter Report | about 13-14 min | about 23 min | 3,547 | 23:34 |
| E047 Give Your Son a Name | about 25-26 min | about 46 min | 7,035 | 46:36 |
| E048 Field Notes: Father's Day When It's Complicated | about 13-14 min | about 23 min | 3,461 | 22:59 |

The added length is new material: stories, real disagreements and callbacks. Each header's "New in v3" note lists what was added.

## Other changes from the drafts

- **Canon fixes.**
  - E041: the draft had Jonathon's father "in the house... in the recliner," which contradicts canon, because his father left when he was nine. The v3 pushback is rebuilt on the real fact.
  - E041: the Austin "Did you eat?" / "K." exchange is now one text, not two, to match the dates.
  - E043: the draft dated Jonathon's Shane call Wed May 26, but E042 (May 28) reports it as missed. It moves to Mon May 31.
  - E046: "my brother taught me the tractor" conflicted with E043 (his granddad taught him), so it was cut.
  - E047: "since your graduation" contradicted E030 (Wes said "I'm proud of you" to his oldest on Apr 15). The phone call is now the second time.
  - E047: the draft credited "Who died?" to Wes's brother. It's Jonathon's father's line (E030).
- **Wes's job stays unnamed.** A v3 line in E045 had him talking about quota, and it was cut.
- **Plug tense.**
  - E045's plug now reads "If you want it on paper, it's at walksteadfast.com."
  - E047's training plug names one session by number and title, in the present tense ("The closest is session ten, The Father Who Does Not Leave").
  - Future-tense wording was also removed from the production notes, where lint was catching it.
- **"this week," "weekend" and "Week two" removals.** Every spoken instance in the drafts was rewritten, along with chapter names and on-screen text. The "Same beats every week" stage note in the intros became "every episode." The two exceptions are locked intro lines, listed below.
- **Locked intro lines kept and flagged.** These lines are kept word for word because the brief requires the intro verbatim:
  - E042: JONATHON "This is Walk Steadfast, Memorial Day weekend."
  - E047: WES "...this week as fathers of boys."

  The fix belongs in _build/intros_data.py.
- **E047 scripture.** Isaiah 43:1 is carded as its dash-free second half, exact. The first half (Jacob and Israel) is described in Wes's words.
- **Mic share.** E045 and E046 ran over 55% Jonathon in early v3 passes. Listener answers and tool narration moved to Wes until both were under 50%.
- **Cross-batch phrase repeats.** After drafting, a seven-word repeat scan across E041-E048 found about twenty accidental repeats, and all of them were rewritten. Examples:
  - two listener cases that both opened "Nineteen, single"
  - "I've been sitting on it since"
  - "That's it? That's the whole answer?"
  - "in the truck in a parking lot"
  - "looked at me like I'd..."
  - the married-guys "Sit with it a day" wording

  The repeats that remain are deliberate:
  - the standing "turns his mug a quarter turn," outros and credits
  - each Friday's restatement of Tuesday's challenge
  - Ruby's "What do you think about when you're by yourself?" (E045 to E046)
  - Wes's one-sentence heading (E043 to E044)
  - the sticky note "Be nice to Theo most of the time"
  - the safety-hotline rail
- **One "not only."** E043's "not only one you don't" was rewritten ("along with the one you don't"). It wasn't the banned construction, but it was close enough to be worth removing.
