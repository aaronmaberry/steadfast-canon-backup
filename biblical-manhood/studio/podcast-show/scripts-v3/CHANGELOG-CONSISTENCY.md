# Continuity pass: Pancake, Theo's birthday, ages and anniversaries

Branch `podcast-v3-consistency`, cut from `podcast-v3-final`. A small continuity pass across E001-E104. Minimal edits only: no episode was shortened, no voice changed, no turns were re-split, and the word "week" was left alone. Every Wes turn is still at or under 120 words; the Wes lines below are one-word swaps. `_build/lint.sh scripts-v3/E*.md` exits 0, with no new findings against the pre-edit run apart from the word counts.

## Facts settled on

1. **Pancake.** Ruby asked for a dog for over a year. In January (E007) Jonathon and Dani said "after Theo turns five, in August," and she named the dog Pancake that day. There was no dog through the summer (E009, E046, E050). Pancake arrived in August, the week of Theo's birthday (E053, E084), and is "she" everywhere a pronoun is used (E079 new line, E102, E103). Only E079 contradicted this.
2. **Theo's birthday and the time off.** Theo turns five in August, after Sat Aug 14 (E065 still calls him "my four-year-old" that morning). The exact date is never stated. Jonathon has a reported workday in every week of August (E061-E070: the Aug 3 call, the Aug 4 Corpus call, the Aug 11 drive home, the Aug 19 "before work", the Aug 23 meeting, the Aug 26 ride-along, the Aug 30 rep). So the time off in E053 is shortened from "the week of Theo's birthday, five days" to the birthday itself, phone off. Pancake still comes that week. After the birthday, Theo is five in every episode (E073 on). Ruby is seven all year.
3. **Marriage lengths and anniversaries.** The two facts in the brief were mixed up: the "almost nine years" in E048 and the "nine years" in E093 are about **Wes's dad's death**, not a marriage, and **Thu Oct 14** (E079-E082) is the anniversary of that death. These already agreed and were not changed:
   - Wes's dad died on Sunday night, Oct 14, 2018 (that date was a Sunday). He has been gone "almost nine years" before October 2027 and "nine years" from October on (SHOW-BIBLE: "nine years in October 2027").
   - Wes has been married since 2000: "twenty-seven years" through 2027 and "almost twenty-eight" in November (E087). WES-HART-HOST has "27 years in Jan 2027", so the anniversary is in January.
   - Jonathon and Dani have been "married ten years" all year (E001, E006, E011, E026, E043, E063, E068, E087). Jonathon married at twenty-seven. No anniversary date is given for them, only "our first anniversary" (E033).
   - **The real "about ten years" conflict:** Wes's youngest is sixteen all year (E046 through E103, licensed since spring), so nine years earlier, at his granddad's funeral in October 2018, he was **seven**. E047, E079 and E080 said "six," which puts the death about ten years back. Changed to seven. The oldest (21) was about twelve at the time.

## Every changed line

Paths are relative to `scripts-v3/`. Script lines are partial: only the changed span is quoted.

### 1. Pancake the dog

| File | Line | Before | After |
|---|---|---|---|
| `E079-grief-at-the-table.md` | 18 | **Pancake:** Ruby has named the dog they don't have. | **Pancake:** the dog that came in August; Ruby named her months before she arrived. |
| `E079-grief-at-the-table.md` | 365 | JONATHON: For the record, we don't have a dog. Ruby's already named the one we don't have. Pancake. So I've been emotionally attached to a dog that doesn't exist for about two years. | JONATHON: For the record, we've only had a dog since August. Pancake. Ruby named her months before she got here, so I was emotionally attached to a dog that didn't exist for most of a year. |

### 2. Theo's birthday time off

| File | Line | Before | After |
|---|---|---|---|
| `E053-before-anything-went-wrong.md` | 19 | the week of Theo's birthday in August, phone off, Pancake week | Theo's birthday in August (the day itself), phone off, Pancake week |
| `E053-before-anything-went-wrong.md` | 346 | Friday morning I put in for the week of Theo's birthday in August. Five days. Phone off. | Friday morning I put in for Theo's birthday in August. The day itself. Phone off. |
| `E054-field-notes-work-it-and-keep-it.md` | 283 | Jonathon's August days off. | Jonathon's August day off. |
| `../SHOW-BIBLE.md` | 564 | the week off for Theo's birthday when Pancake arrives (E053) | the day off for Theo's birthday, the week Pancake arrives (E053) |
| `../hosts/JONATHON-CHARACTER.md` | 235 | booked the week of Theo's birthday in August (Pancake week) | booked Theo's birthday in August, the day itself (Pancake week) |

### 3. Ages, marriage length and anniversaries

| File | Line | Before | After |
|---|---|---|---|
| `E073-feelings-are-the-dash-not-the-wheel.md` | 232 | with a four-year-old in the tub. | with a five-year-old in the tub. |
| `E074-field-notes-dash-and-wheel.md` | 170 | because he's four and he cries | because he's five and he cries |
| `E074-field-notes-dash-and-wheel.md` | 241 | Theo knew what it meant, and he's four. | Theo knew what it meant, and he's five. |
| `E075-every-season-still-counts.md` | 141 | And with a four-year-old, you can't win the room. | And with a five-year-old, you can't win the room. |
| `E093-lead-the-thanksgiving-table.md` | 257 | Because Theo's four and he'll pray | Because Theo's five and he'll pray |
| `E094-field-notes-black-friday.md` | 90 | My four-year-old did more for that peace | My five-year-old did more for that peace |
| `E095-joseph-said-nothing.md` | 299 | He's four. He's got a plastic phone | He's five. He's got a plastic phone |
| `E096-field-notes-advent-report.md` | 128 | a seven-year-old and a four-year-old | a seven-year-old and a five-year-old |
| `E096-field-notes-advent-report.md` | 148 | how you show a four-year-old. | how you show a five-year-old. |
| `E096-field-notes-advent-report.md` | 154 | A four-year-old can understand that verse. | A five-year-old can understand that verse. |
| `E096-field-notes-advent-report.md` | 190 | devotional for a four-year-old. | devotional for a five-year-old. |
| `E047-give-your-son-a-name.md` | 83 | WES: He was six when my dad died. | WES: He was seven when my dad died. |
| `E047-give-your-son-a-name.md` | 470 | was about eleven or twelve when Wes's dad died (the youngest was six, five years younger) | was about twelve when Wes's dad died (the youngest was seven, five years younger) |
| `E079-grief-at-the-table.md` | 18 | told his six-year-old, | told his seven-year-old, |
| `E079-grief-at-the-table.md` | 314 | My youngest was six when my dad died. | My youngest was seven when my dad died. |
| `E079-grief-at-the-table.md` | 318 | I taught a six-year-old that strong means dry. Ruby got a better answer at seven over macaroni than my boy got at six in a church. | I taught a seven-year-old that strong means dry. Ruby got a better answer at seven over macaroni than my boy got at seven in a church. |
| `E079-grief-at-the-table.md` | 377 | He was six when his granddad died. | He was seven when his granddad died. |
| `E079-grief-at-the-table.md` | 388 | "When you were six, I told you | "When you were seven, I told you |
| `E079-grief-at-the-table.md` | 546 | Wes's six-year-old at the funeral | Wes's seven-year-old at the funeral |
| `E080-field-notes-grief-report.md` | 18 | "When you were six, you asked | "When you were seven, you asked |
| `E080-field-notes-grief-report.md` | 65 | "When you were six, you asked | "When you were seven, you asked |
| `../hosts/WES-HART-HOST.md` | 196 | He was six when Wes's dad died. | He was seven when Wes's dad died. |

Files changed: 12 scripts (E047, E053, E054, E073, E074, E075, E079, E080, E093, E094, E095, E096) and 3 reference docs (`SHOW-BIBLE.md`, `hosts/JONATHON-CHARACTER.md`, `hosts/WES-HART-HOST.md`). The reference docs got the same one-phrase fix, so they no longer describe a week off or a six-year-old at the funeral.

## Unresolved or left alone

- **Theo's exact birthday.** No script gives a date, and inventing one would add a new fact. It has to fall between Sun Aug 15 and Tue Aug 31, on a day Jonathon isn't reported at work. Nothing on air pins it, so nothing contradicts it.
- **Rounding of Wes's dad's death before October.** E001 (Jan), E029 line 211, E033, E035, E037 and E038 say "nine years" where the exact figure is eight and a half. E025, E029 line 48 and E048 say "almost nine years." This is how a man talks, not a contradiction, so those lines were left alone. If you want strict counting, change the spoken pre-October "nine years" lines to "almost nine years."
- **Pancake's pronoun.** The brief said "him," but no script ever uses a masculine pronoun for Pancake. E102 and E103 use "she," so the new E079 line uses "her." The middle name Gregory (E089) was left as it is.
- **"Most of a year" in E079.** The old line said Jonathon was attached to the imaginary dog "for about two years." Ruby named the dog in January (E007, released Jan 26), so the new line says "most of a year" (January to August). Ruby's asking began "over a year" before January, so the old figure wasn't strictly wrong as a count of how long she'd been asking.
- **Historical records not edited.** `BATCH-REPORT-E049-E056.md`, `BATCH-REPORT-E065-E072.md` and `BATCH-REPORT-E073-E080.md`, plus the v1 drafts in `../scripts/`, still describe the old wording ("the dog they don't have", the week off). These files are the record of what each batch found. `BATCH-REPORT-E065-E072.md` raised both the Pancake and the week-off conflicts for a decision, and this pass settles them.
