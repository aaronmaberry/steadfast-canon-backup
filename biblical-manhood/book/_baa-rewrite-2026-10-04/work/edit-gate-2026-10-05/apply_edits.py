#!/usr/bin/env python3
"""Edit-gate polish, 2026-10-05. Each edit must match exactly once. Writes edits.tsv log."""
import sys
from pathlib import Path
B = Path("/workspace/biblical-manhood/book/_baa-rewrite-2026-10-04/book")
E = [
 ("02-you-are-not-crazy.md","can't get a clear look at what a man is supposed to be","can't get a clear look at what a man ought to be","quiet-check: only non-Scripture 8-word overlap with a transcript (generic phrase); reworded"),
 ("03-the-four-marks.md","One August a friend of mine and his brother-in-law","One August a man I know and his brother-in-law","repeat: second 'a friend of mine' in the same chapter"),
 ("07-work-for-gods-pay.md","Most men know the drive home","Nearly every man knows the drive home","opener: ch2 opens 'Most men I know', ch7 'Most men know'"),
 ("07-work-for-gods-pay.md","Say one line before your feet hit the floor.","Say one line before you swing your legs out of bed.","repeat: 'feet hit the floor' twice in ch7 and again in ch10"),
 ("08-the-empty-chair.md","and Joseph quietly exits before Jesus' public years","and Joseph, Mary's husband, quietly exits before Jesus' public years","clarity: two different Josephs in one paragraph"),
 ("39-scripture-notes.md","\"Joseph quietly exits before Jesus' public years\"","\"Joseph, Mary's husband, quietly exits before Jesus' public years\"","note key follows ch8 edit"),
 ("09-anger-the-itch-and-the-drift.md","he bought comfort that never asks your name","he bought comfort that never asks his name","grammar: pronoun agreement (he ... his)"),
 ("11-when-home-never-handed-you-off.md","This is my son, and I love him.","This is My son, and I love him.","house style: God's pronoun capitalized when God speaks (matches ch10)"),
 ("12-a-man-with-no-brothers.md","That's pride in work clothes.","That's pride with a straight face.","repeat: ch5 has 'pride in a work shirt'"),
 ("15-two-men-two-ways.md","That one stung, could we sit down once the kids are in bed?","That one stung. Could we sit down once the kids are in bed?","grammar: comma splice"),
 ("15-two-men-two-ways.md","A boy grows toward whatever his father calls him.","A son tends to become what his father calls him.","repeat: ch22 owns 'A boy grows toward whatever he's called'"),
 ("16-destiny-is-not-a-vibe.md","That's a whole life in about twenty words.","That's a whole life in about two dozen words.","fact: Acts 13:36 NIV is 24 words"),
 ("19-lay-it-down.md","Not one of those small losses gets lost.","Not one of those small losses goes to waste.","clarity: 'losses gets lost' jingle"),
 ("23-you-were-made-for-a-work.md","On His last night before the cross, Jesus told His Father","Hours before His arrest, Jesus told His Father","repeat: 'On His last night before the cross' also in ch10"),
 ("24-feelings-are-the-dash-not-the-wheel.md","Look at Jesus. He cried at a friend's grave.","Look at Jesus. He wept outside His friend Lazarus's tomb.","repeat: identical sentence in ch19"),
 ("39-scripture-notes.md","\"He cried at a friend's grave\": John 11:35.\n\n\"the sorrow was about to kill Him\"","\"He wept outside His friend Lazarus's tomb\": John 11:35.\n\n\"the sorrow was about to kill Him\"","note key follows ch24 edit (ch19 key unchanged)"),
 ("24-feelings-are-the-dash-not-the-wheel.md","Young and single, the same goes for the wife you hope for. She's not your thermostat.","Young and single? Don't hand that job to the wife you hope for, either. She's not your thermostat.","repeat: ch14 has 'If you're single, the same goes for the wife you're hoping for'"),
 ("25-every-season-still-counts.md","and the year of mourning before he picked up a shovel","and the months of mourning before he picked up a shovel","fact: he planted the spring after the burial, so not a full year"),
 ("25-every-season-still-counts.md","I know a man who can't leave his house.","One man I know can't leave his house anymore.","repeat: ch23 has 'I know a man who can't leave his wife'"),
 ("25-every-season-still-counts.md","Whether you're nineteen or seventy-nine, the Father who orders the seasons can give you yours","Whether you're nineteen or seventy-nine, He can give you yours","repeat: 'the Father who set the seasons turning' in the sentence before"),
 ("28-these-men-are-my-brothers.md","That silence is the nearest his father gets to a hug, and Cole took it.","That silence is as much as his father knows how to say, and Cole took it.","repeat: ch11 Grant's supper was 'about as close to a hug as his dad could manage'"),
 ("28-these-men-are-my-brothers.md","Tomás, twenty-nine, walked his two-year-old","Tomás walked his two-year-old","consistency: Tomás is 29 with a baby in ch1; his child is two here"),
 ("36-about-the-author.md","spent across a table from other men: kitchen tables, garage chairs, church classrooms, and early weekday diners with a Bible and a cup of coffee.","spent across a table from other men, at kitchen tables, in garage chairs, in church classrooms, and in early weekday diners with a Bible and a cup of coffee.","house style: no mid-sentence colon"),
 ("36-about-the-author.md","to men in every season: single and married, young and older, still standing and starting over.","to men in every season, single and married, young and older, still standing and starting over.","house style: no mid-sentence colon"),
]
log = []
for f, old, new, why in E:
    p = B / f; t = p.read_text()
    n = t.count(old)
    if n != 1:
        sys.exit(f"ABORT {f}: expected 1 match, got {n}: {old[:60]}")
    p.write_text(t.replace(old, new)); log.append((f, old, new, why))
out = Path(__file__).with_name("edits.tsv")
out.write_text("file\tbefore\tafter\twhy\n" + "".join("\t".join(x).replace("\n", "\\n") + "\n" if False else "\t".join(s.replace("\n","\\n") for s in x) + "\n" for x in log))
print(f"applied {len(log)} edits -> {out}")
