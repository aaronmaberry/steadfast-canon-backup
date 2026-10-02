# Scripture count and NIV check

Every `:::margin` block in `book/`, checked against the NIV (2011 text as served by Bible Gateway, `version=NIV`) on 2026-10-01 by `meta/tools/niv_verify.py`.

- Margin blocks: **158**
- Unique verses (ranges expanded): **179**, under Biblica's 500-verse gratis limit. No complete book of the Bible is quoted. Scripture in margin blocks is about 4,200 words of a ~70,600-word book (about 6%), far under the 25% limit.
- Every block's reference line reads `**Book C:V NIV**`.

Status key:
- **EXACT**: identical to the NIV text in house form (straight quotes; quotation marks balanced for a stand-alone excerpt).
- **EXCERPT**: a contiguous, word-for-word part of the cited verses (e.g. the last sentence of Joshua 24:15).
- **WORDS EXACT, punctuation**: every word identical and in order; the only difference is excerpt punctuation (a closing quotation mark added where the NIV speech runs on into the next verse, or the NIV's own trailing comma kept where the verse ends mid-sentence).

House rule for dashes: where the NIV text has an em dash (e.g. Ephesians 2:8-9, Isaiah 43:1), the manuscript renders it as a comma, because the manuscript carries no dash characters (brief §1.5). Words are unchanged.

Corrections made against the NIV during this pass (the base carried these errors): John 18:8 (word order of the speech tag), Numbers 8:26 ("their brothers", base had "their fellow Levites"), 1 Kings 19:4 ("wilderness", base had "desert"), Isaiah 46:4 (stray comma removed). Nested quotation marks were also normalized in Judges 7:17, 1 Kings 2:2-3, Mark 14:34, 2 Samuel 12:7, John 4:34 and Ephesians 5:31.

| File | Line | Reference | Status | Verses |
|---|---:|---|---|---:|
| `01-a-quiet-tuesday.md` | 50 | Luke 16:10 | EXACT | 1 |
| `01-a-quiet-tuesday.md` | 59 | Matthew 7:24 | EXACT | 1 |
| `02-you-are-not-crazy.md` | 60 | Genesis 1:27 | EXACT | 1 |
| `03-the-four-marks.md` | 22 | Philippians 2:5 | EXACT | 1 |
| `03-the-four-marks.md` | 37 | James 4:17 | EXACT | 1 |
| `03-the-four-marks.md` | 50 | Galatians 6:5 | EXACT | 1 |
| `03-the-four-marks.md` | 63 | John 10:4 | EXACT | 1 |
| `03-the-four-marks.md` | 78 | Colossians 3:23-24 | EXACT | 2 |
| `04-stop-waiting.md` | 16 | James 4:17 | EXACT | 1 |
| `04-stop-waiting.md` | 35 | Proverbs 24:30-31 | EXACT | 2 |
| `04-stop-waiting.md` | 62 | Genesis 3:9 | EXACT | 1 |
| `04-stop-waiting.md` | 73 | Psalm 27:14 | EXACT | 1 |
| `04-stop-waiting.md` | 84 | Luke 9:51 | EXACT | 1 |
| `05-pick-up-the-weight.md` | 8 | Galatians 6:5 | EXACT | 1 |
| `05-pick-up-the-weight.md` | 25 | Genesis 4:9 | EXACT | 1 |
| `05-pick-up-the-weight.md` | 48 | 1 Timothy 5:8 | EXACT | 1 |
| `05-pick-up-the-weight.md` | 75 | Galatians 6:2 | EXACT | 1 |
| `05-pick-up-the-weight.md` | 86 | Numbers 11:14 | EXACT | 1 |
| `05-pick-up-the-weight.md` | 97 | Isaiah 53:4 | EXACT | 1 |
| `06-go-first.md` | 14 | John 10:4 | EXACT | 1 |
| `06-go-first.md` | 25 | Hebrews 12:2 | EXACT | 1 |
| `06-go-first.md` | 40 | John 13:14-15 | EXACT | 2 |
| `06-go-first.md` | 47 | Judges 7:17 | WORDS EXACT, punctuation | 1 |
| `06-go-first.md` | 64 | Nehemiah 2:17 | EXACT | 1 |
| `06-go-first.md` | 85 | 2 Timothy 1:7 | EXACT | 1 |
| `06-go-first.md` | 96 | Deuteronomy 31:8 | EXACT | 1 |
| `07-live-for-a-reward-that-lasts.md` | 22 | Matthew 6:19-21 | EXACT | 3 |
| `07-live-for-a-reward-that-lasts.md` | 29 | Matthew 6:3-4 | EXACT | 2 |
| `07-live-for-a-reward-that-lasts.md` | 38 | Colossians 3:23-24 | EXACT | 2 |
| `07-live-for-a-reward-that-lasts.md` | 49 | Ephesians 2:8-10 | EXACT | 3 |
| `07-live-for-a-reward-that-lasts.md` | 56 | Matthew 25:21 | EXACT | 1 |
| `07-live-for-a-reward-that-lasts.md` | 65 | Hebrews 11:26 | EXACT | 1 |
| `07-live-for-a-reward-that-lasts.md` | 82 | 2 Corinthians 4:17-18 | EXACT | 2 |
| `08-the-empty-chair.md` | 12 | Psalm 68:5-6 | EXACT | 2 |
| `08-the-empty-chair.md` | 61 | Psalm 27:10 | EXACT | 1 |
| `09-anger-the-itch-and-the-drift.md` | 26 | Ecclesiastes 10:18 | EXACT | 1 |
| `09-anger-the-itch-and-the-drift.md` | 41 | James 1:14-15 | EXACT | 2 |
| `09-anger-the-itch-and-the-drift.md` | 58 | Ephesians 4:26-27 | EXACT | 2 |
| `10-the-father-who-does-not-leave.md` | 24 | John 14:9 | EXACT | 1 |
| `10-the-father-who-does-not-leave.md` | 35 | Matthew 3:17 | EXACT | 1 |
| `10-the-father-who-does-not-leave.md` | 48 | John 14:18 | EXACT | 1 |
| `10-the-father-who-does-not-leave.md` | 87 | Luke 15:20 | WORDS EXACT, punctuation | 1 |
| `11-when-home-never-handed-you-off.md` | 32 | Genesis 32:26 | EXACT | 1 |
| `11-when-home-never-handed-you-off.md` | 45 | 1 Kings 2:2-3 | WORDS EXACT, punctuation | 2 |
| `11-when-home-never-handed-you-off.md` | 52 | 2 Timothy 1:6 | EXACT | 1 |
| `12-leave-without-slamming-the-door.md` | 12 | Exodus 20:12 | EXACT | 1 |
| `12-leave-without-slamming-the-door.md` | 19 | Genesis 2:24 | EXACT | 1 |
| `12-leave-without-slamming-the-door.md` | 46 | Romans 12:19 | EXACT | 1 |
| `12-leave-without-slamming-the-door.md` | 55 | Genesis 50:20 | EXACT | 1 |
| `13-a-man-with-no-brothers.md` | 20 | Ecclesiastes 4:9-10 | EXACT | 2 |
| `13-a-man-with-no-brothers.md` | 31 | Mark 14:34 | EXACT | 1 |
| `13-a-man-with-no-brothers.md` | 46 | 1 Samuel 23:16 | EXACT | 1 |
| `13-a-man-with-no-brothers.md` | 55 | Proverbs 27:17 | EXACT | 1 |
| `14-ask-the-man.md` | 50 | Titus 2:6-7 | EXCERPT | 2 |
| `14-ask-the-man.md` | 69 | 2 Timothy 2:2 | EXACT | 1 |
| `15-the-problem-inside.md` | 32 | Mark 7:23 | EXACT | 1 |
| `15-the-problem-inside.md` | 41 | Romans 5:8 | EXACT | 1 |
| `15-the-problem-inside.md` | 54 | James 5:16 | EXACT | 1 |
| `15-the-problem-inside.md` | 75 | Psalm 51:10 | EXACT | 1 |
| `16-how-that-looks-on-a-man.md` | 22 | Colossians 3:19 | EXACT | 1 |
| `16-how-that-looks-on-a-man.md` | 53 | 2 Samuel 11:1 | EXACT | 1 |
| `16-how-that-looks-on-a-man.md` | 64 | 2 Samuel 11:27 | EXACT | 1 |
| `16-how-that-looks-on-a-man.md` | 77 | 2 Samuel 12:7 | WORDS EXACT, punctuation | 1 |
| `16-how-that-looks-on-a-man.md` | 90 | 2 Samuel 12:13 | EXACT | 1 |
| `17-no-fixed-star.md` | 16 | Judges 21:25 | EXACT | 1 |
| `17-no-fixed-star.md` | 35 | Proverbs 14:12 | EXACT | 1 |
| `17-no-fixed-star.md` | 62 | Amos 7:7-8 | EXACT | 2 |
| `17-no-fixed-star.md` | 69 | Psalm 119:105 | EXCERPT | 1 |
| `17-no-fixed-star.md` | 76 | 2 Timothy 3:16-17 | EXACT | 2 |
| `17-no-fixed-star.md` | 89 | Matthew 7:24-25 | EXACT | 2 |
| `18-before-the-fall.md` | 14 | Genesis 2:7 | EXACT | 1 |
| `18-before-the-fall.md` | 23 | Genesis 1:27 | EXACT | 1 |
| `18-before-the-fall.md` | 34 | Genesis 1:28 | EXACT | 1 |
| `18-before-the-fall.md` | 49 | Genesis 2:8 | EXACT | 1 |
| `18-before-the-fall.md` | 60 | Genesis 2:15 | EXACT | 1 |
| `18-before-the-fall.md` | 71 | Genesis 2:16-17 | EXACT | 2 |
| `18-before-the-fall.md` | 82 | Genesis 2:2-3 | EXACT | 2 |
| `18-before-the-fall.md` | 95 | Genesis 2:18 | EXACT | 1 |
| `18-before-the-fall.md` | 108 | Genesis 2:19-20 | EXACT | 2 |
| `18-before-the-fall.md` | 119 | Genesis 2:23 | EXACT | 1 |
| `18-before-the-fall.md` | 132 | Genesis 2:25 | EXACT | 1 |
| `19-two-men-two-ways.md` | 10 | Romans 5:19 | EXACT | 1 |
| `19-two-men-two-ways.md` | 21 | Genesis 3:6 | EXACT | 1 |
| `19-two-men-two-ways.md` | 32 | Genesis 3:10 | EXACT | 1 |
| `19-two-men-two-ways.md` | 45 | Genesis 3:15 | EXACT | 1 |
| `19-two-men-two-ways.md` | 56 | Matthew 26:39 | EXACT | 1 |
| `19-two-men-two-ways.md` | 65 | Matthew 26:46 | EXACT | 1 |
| `19-two-men-two-ways.md` | 72 | John 18:4 | EXACT | 1 |
| `19-two-men-two-ways.md` | 79 | John 18:8 | EXACT | 1 |
| `19-two-men-two-ways.md` | 88 | John 19:30 | EXACT | 1 |
| `19-two-men-two-ways.md` | 99 | 1 Corinthians 15:22 | EXACT | 1 |
| `19-two-men-two-ways.md` | 108 | Galatians 2:20 | EXACT | 1 |
| `19-two-men-two-ways.md` | 139 | 1 Corinthians 15:45 | EXACT | 1 |
| `20-destiny-is-not-a-vibe.md` | 26 | Acts 13:36 | EXACT | 1 |
| `20-destiny-is-not-a-vibe.md` | 41 | Ephesians 2:10 | EXACT | 1 |
| `20-destiny-is-not-a-vibe.md` | 52 | John 4:34 | WORDS EXACT, punctuation | 1 |
| `20-destiny-is-not-a-vibe.md` | 77 | Luke 22:32 | EXACT | 1 |
| `20-destiny-is-not-a-vibe.md` | 88 | Revelation 2:17 | EXACT | 1 |
| `21-if-there-is-no-wife-yet.md` | 54 | Proverbs 18:22 | EXACT | 1 |
| `21-if-there-is-no-wife-yet.md` | 83 | 1 Corinthians 7:35 | EXACT | 1 |
| `21-if-there-is-no-wife-yet.md` | 94 | 1 Timothy 5:1-2 | EXACT | 2 |
| `22-know-her.md` | 16 | John 10:14 | EXACT | 1 |
| `22-know-her.md` | 29 | 1 Peter 3:7 | EXACT | 1 |
| `22-know-her.md` | 44 | James 1:19 | WORDS EXACT, punctuation | 1 |
| `22-know-her.md` | 79 | Proverbs 20:5 | EXACT | 1 |
| `23-lay-it-down.md` | 20 | Ephesians 5:25 | EXACT | 1 |
| `23-lay-it-down.md` | 27 | Philippians 2:5-7 | EXACT | 3 |
| `23-lay-it-down.md` | 72 | Matthew 16:25 | EXACT | 1 |
| `24-what-she-actually-needs.md` | 42 | Proverbs 31:28-29 | EXACT | 2 |
| `24-what-she-actually-needs.md` | 61 | Proverbs 15:1 | EXACT | 1 |
| `24-what-she-actually-needs.md` | 72 | Malachi 2:15 | EXACT | 1 |
| `25-the-bed-is-a-covenant.md` | 22 | Genesis 2:24-25 | EXACT | 2 |
| `25-the-bed-is-a-covenant.md` | 29 | Hebrews 13:4 | EXACT | 1 |
| `25-the-bed-is-a-covenant.md` | 38 | Ephesians 5:31 | EXACT | 1 |
| `25-the-bed-is-a-covenant.md` | 53 | 1 Corinthians 7:4 | EXACT | 1 |
| `26-your-daughter-is-watching.md` | 30 | Zephaniah 3:17 | EXACT | 1 |
| `26-your-daughter-is-watching.md` | 45 | Ephesians 6:4 | EXACT | 1 |
| `26-your-daughter-is-watching.md` | 56 | Luke 8:54 | EXACT | 1 |
| `27-give-your-son-a-name.md` | 26 | Mark 1:11 | EXACT | 1 |
| `27-give-your-son-a-name.md` | 45 | Deuteronomy 6:6-7 | EXACT | 2 |
| `27-give-your-son-a-name.md` | 76 | Psalm 127:3 | EXACT | 1 |
| `28-give-your-son-a-hill.md` | 38 | Hebrews 12:11 | EXACT | 1 |
| `28-give-your-son-a-hill.md` | 49 | Genesis 22:6 | WORDS EXACT, punctuation | 1 |
| `28-give-your-son-a-hill.md` | 56 | 1 Samuel 17:34-35 | EXCERPT | 2 |
| `28-give-your-son-a-hill.md` | 93 | 2 Timothy 2:3 | EXACT | 1 |
| `29-give-your-son-a-day-he-will-not-forget.md` | 14 | Joshua 4:6-7 | EXACT | 2 |
| `29-give-your-son-a-day-he-will-not-forget.md` | 55 | 1 Corinthians 16:13 | EXACT | 1 |
| `30-you-were-made-for-a-work.md` | 16 | Colossians 3:23-24 | EXACT | 2 |
| `30-you-were-made-for-a-work.md` | 31 | John 5:17 | EXACT | 1 |
| `30-you-were-made-for-a-work.md` | 40 | Ephesians 4:28 | EXACT | 1 |
| `30-you-were-made-for-a-work.md` | 51 | Numbers 8:25-26 | EXACT | 2 |
| `30-you-were-made-for-a-work.md` | 72 | Ecclesiastes 2:24 | WORDS EXACT, punctuation | 1 |
| `30-you-were-made-for-a-work.md` | 91 | John 17:4 | EXACT | 1 |
| `31-feelings-are-the-dash-not-the-wheel.md` | 36 | Psalm 42:5 | EXACT | 1 |
| `31-feelings-are-the-dash-not-the-wheel.md` | 65 | Proverbs 28:26 | EXACT | 1 |
| `31-feelings-are-the-dash-not-the-wheel.md` | 88 | 1 Kings 19:4 | EXACT | 1 |
| `31-feelings-are-the-dash-not-the-wheel.md` | 97 | Psalm 103:14 | EXACT | 1 |
| `32-every-season-still-counts.md` | 8 | Ecclesiastes 3:1 | EXACT | 1 |
| `32-every-season-still-counts.md` | 25 | Ecclesiastes 12:1 | EXACT | 1 |
| `32-every-season-still-counts.md` | 64 | Joshua 14:12 | EXCERPT | 1 |
| `32-every-season-still-counts.md` | 75 | Isaiah 46:4 | EXACT | 1 |
| `32-every-season-still-counts.md` | 94 | 2 Timothy 4:7 | EXACT | 1 |
| `33-what-you-are-building-when-nobody-claps.md` | 14 | Luke 2:51 | EXACT | 1 |
| `33-what-you-are-building-when-nobody-claps.md` | 27 | Matthew 6:6 | EXACT | 1 |
| `33-what-you-are-building-when-nobody-claps.md` | 38 | 1 Corinthians 3:13 | EXCERPT | 1 |
| `33-what-you-are-building-when-nobody-claps.md` | 71 | Isaiah 49:4 | EXACT | 1 |
| `33-what-you-are-building-when-nobody-claps.md` | 90 | Hebrews 6:10 | EXACT | 1 |
| `34-write-the-next-move.md` | 20 | Habakkuk 2:2 | EXACT | 1 |
| `34-write-the-next-move.md` | 33 | Nehemiah 6:3 | EXCERPT | 1 |
| `34-write-the-next-move.md` | 78 | Proverbs 21:5 | EXACT | 1 |
| `34-write-the-next-move.md` | 101 | James 4:15 | EXACT | 1 |
| `34-write-the-next-move.md` | 108 | Proverbs 16:9 | EXACT | 1 |
| `34-write-the-next-move.md` | 129 | Joshua 24:15 | EXCERPT | 1 |
| `35-these-men-are-my-brothers.md` | 12 | Proverbs 17:17 | EXACT | 1 |
| `35-these-men-are-my-brothers.md` | 47 | Psalm 112:7 | EXACT | 1 |
| `35-these-men-are-my-brothers.md` | 58 | Hebrews 10:24 | WORDS EXACT, punctuation | 1 |
| `35-these-men-are-my-brothers.md` | 79 | 1 Corinthians 15:58 | EXACT | 1 |
| `35-these-men-are-my-brothers.md` | 90 | Numbers 6:24-26 | WORDS EXACT, punctuation | 3 |

## Unique verses

1 Corinthians 15:22, 1 Corinthians 15:45, 1 Corinthians 15:58, 1 Corinthians 16:13, 1 Corinthians 3:13, 1 Corinthians 7:35, 1 Corinthians 7:4, 1 Kings 19:4, 1 Kings 2:2, 1 Kings 2:3, 1 Peter 3:7, 1 Samuel 17:34, 1 Samuel 17:35, 1 Samuel 23:16, 1 Timothy 5:1, 1 Timothy 5:2, 1 Timothy 5:8, 2 Corinthians 4:17, 2 Corinthians 4:18, 2 Samuel 11:1, 2 Samuel 11:27, 2 Samuel 12:13, 2 Samuel 12:7, 2 Timothy 1:6, 2 Timothy 1:7, 2 Timothy 2:2, 2 Timothy 2:3, 2 Timothy 3:16, 2 Timothy 3:17, 2 Timothy 4:7, Acts 13:36, Amos 7:7, Amos 7:8, Colossians 3:19, Colossians 3:23, Colossians 3:24, Deuteronomy 31:8, Deuteronomy 6:6, Deuteronomy 6:7, Ecclesiastes 10:18, Ecclesiastes 12:1, Ecclesiastes 2:24, Ecclesiastes 3:1, Ecclesiastes 4:10, Ecclesiastes 4:9, Ephesians 2:10, Ephesians 2:8, Ephesians 2:9, Ephesians 4:26, Ephesians 4:27, Ephesians 4:28, Ephesians 5:25, Ephesians 5:31, Ephesians 6:4, Exodus 20:12, Galatians 2:20, Galatians 6:2, Galatians 6:5, Genesis 1:27, Genesis 1:28, Genesis 22:6, Genesis 2:15, Genesis 2:16, Genesis 2:17, Genesis 2:18, Genesis 2:19, Genesis 2:2, Genesis 2:20, Genesis 2:23, Genesis 2:24, Genesis 2:25, Genesis 2:3, Genesis 2:7, Genesis 2:8, Genesis 32:26, Genesis 3:10, Genesis 3:15, Genesis 3:6, Genesis 3:9, Genesis 4:9, Genesis 50:20, Habakkuk 2:2, Hebrews 10:24, Hebrews 11:26, Hebrews 12:11, Hebrews 12:2, Hebrews 13:4, Hebrews 6:10, Isaiah 46:4, Isaiah 49:4, Isaiah 53:4, James 1:14, James 1:15, James 1:19, James 4:15, James 4:17, James 5:16, John 10:14, John 10:4, John 13:14, John 13:15, John 14:18, John 14:9, John 17:4, John 18:4, John 18:8, John 19:30, John 4:34, John 5:17, Joshua 14:12, Joshua 24:15, Joshua 4:6, Joshua 4:7, Judges 21:25, Judges 7:17, Luke 15:20, Luke 16:10, Luke 22:32, Luke 2:51, Luke 8:54, Luke 9:51, Malachi 2:15, Mark 14:34, Mark 1:11, Mark 7:23, Matthew 16:25, Matthew 25:21, Matthew 26:39, Matthew 26:46, Matthew 3:17, Matthew 6:19, Matthew 6:20, Matthew 6:21, Matthew 6:3, Matthew 6:4, Matthew 6:6, Matthew 7:24, Matthew 7:25, Nehemiah 2:17, Nehemiah 6:3, Numbers 11:14, Numbers 6:24, Numbers 6:25, Numbers 6:26, Numbers 8:25, Numbers 8:26, Philippians 2:5, Philippians 2:6, Philippians 2:7, Proverbs 14:12, Proverbs 15:1, Proverbs 16:9, Proverbs 17:17, Proverbs 18:22, Proverbs 20:5, Proverbs 21:5, Proverbs 24:30, Proverbs 24:31, Proverbs 27:17, Proverbs 28:26, Proverbs 31:28, Proverbs 31:29, Psalm 103:14, Psalm 112:7, Psalm 119:105, Psalm 127:3, Psalm 27:10, Psalm 27:14, Psalm 42:5, Psalm 51:10, Psalm 68:5, Psalm 68:6, Revelation 2:17, Romans 12:19, Romans 5:19, Romans 5:8, Titus 2:6, Titus 2:7, Zephaniah 3:17

