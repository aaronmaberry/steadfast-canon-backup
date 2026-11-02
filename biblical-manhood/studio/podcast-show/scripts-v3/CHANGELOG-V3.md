# Podcast v3 changelog

Changes logged per batch for the v3 scripts in scripts-v3/. No file in scripts/ or anywhere else was edited.

## Batch E097-E104 (branch cursor/podcast-v3-e097-e104-b614)

E097-E104 had no v1 scripts. They were written new from CALENDAR-104.md, SHOW-BIBLE section 15 and the continuity of E073-E080. Other batches create this same file on their own branches. If they merge, keep every batch section.

### Length overrides

The v3 brief sets mains at 45 to 60 minutes (about 7,000 to 9,000 spoken words) and Field Notes at 20 to 25 minutes (about 3,000 to 3,800 words). That overrides three things in SHOW-BIBLE:

- section 4a, the main length of 25 to 35 minutes;
- section 4b, the Field Notes length of 12 to 16 minutes;
- the section 5 clock tables, with their minute marks for the report, From the Table and the tool.

The rule that no chapter runs six minutes without a turn still applies. Each header says "v3 length."

| Episode | Bible length | v3 length (timing.py) | Override |
|---|---|---|---|
| E097 Waiting on God Isn't Sitting Still | 25-35 min | 46:47 | 4a, section 5 main clock |
| E098 Field Notes: The Wait Report | 12-16 min | 21:46 | 4b, section 5 Field Notes clock |
| E099 The Shepherds Went Back to Work | 25-35 min | 46:19 | 4a, section 5 main clock |
| E100 Field Notes: Back to Work | 12-16 min | 20:32 | 4b, section 5 Field Notes clock |
| E101 Simeon Kept Showing Up | 25-35 min | 46:27 | 4a, section 5 main clock |
| E102 Field Notes: Christmas Eve | 12-16 min | 21:08 | 4b, section 5 Field Notes clock |
| E103 Write the Next Move | 25-35 min | 46:29 | 4a, section 5 main clock |
| E104 Field Notes: New Year's Eve | 12-16 min | 20:41 | 4b, section 5 Field Notes clock |

### Open text that differs from _build/intros_data.py

These are DRAFT opens. Each change was made in the script only, and intros_data.py was not touched. The proposed replacement lines are in BATCH-REPORT-E097-E104.md. With those lines patched into a /tmp copy of _build, intro_lint.py gives 0 fails and 0 warns. That run included the retell check against these scripts.

| Episode | intros_data line | Script line | Why |
|---|---|---|---|
| E097 | "Following Jesus as a man, Advent week two." | "Following Jesus as a man, two Sundays into Advent." | "week two" is a banned "week N" form (brief) |
| E098 | "I'm Wes Hart. A printout's been waiting in my Bible since August." | "I'm Wes Hart. I feed cattle with my brother most Saturdays now." | The printout leaves his Bible on air in E097, so the fact is stale by E098 |
| E099 | "Following Jesus as a man, Advent week three." | "Following Jesus as a man, deep in Advent." | "week three" is a banned "week N" form |
| E101 | "Following Jesus as a man, Christmas week." | "Following Jesus as a man, in the last days before Christmas." | "week" phrasing (brief) |

### Calendar notes

- **E101.** The calendar calls Simeon "the old man." The script follows SHOW-BIBLE section 14 item 20. Luke 2:25-26 is read, Simeon is never called old, and Anna's eighty-four is Luke's.
- **E103.** It carries both plugs, as the calendar allows for the year review: book chapter 34, Write the Next Move, and training session one, A Quiet Tuesday. They sit about four minutes before and ten minutes after the sub-mid.
