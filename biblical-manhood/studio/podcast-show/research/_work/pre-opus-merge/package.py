# package.py : write launch-kit/E001 metadata, description and show notes from the final render.
import json,subprocess
KIT='/workspace/biblical-manhood/studio/podcast-show/launch-kit/E001/'
EP='/workspace/biblical-manhood/studio/podcast-show/episodes/E001/'
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',EP+'E001-walk-steadfast.mp3'],capture_output=True,text=True).stdout)
size=__import__('os').path.getsize(EP+'E001-walk-steadfast.mp3')
chap=open(KIT+'chapters.txt').read().strip()
NIV="Scripture quotations taken from The Holy Bible, New International Version®, NIV®. Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.™ Used by permission. All rights reserved worldwide."
TITLE="The Man You Keep Saying You'll Be"
meta=dict(show="Walk Steadfast",title=TITLE,episode=1,season=1,episodeType="full",explicit=False,
  pubDate="Tue, 05 Jan 2027 05:00:00 -0600",duration_seconds=round(dur),duration_hms=f"{int(dur//60)}:{int(dur%60):02d}",
  enclosure=dict(file="E001-walk-steadfast.mp3",length_bytes=size,type="audio/mpeg"),guid="walksteadfast-e001",
  link="https://walksteadfast.com/episodes/e001",language="en",author="Walk Steadfast",
  transcript=[dict(file="E001-transcript.vtt",type="text/vtt"),dict(file="E001-transcript.srt",type="application/srt")],
  chapters=dict(file="chapters.json",type="application/json+chapters"),episode_art=None,
  hosts=["Wes Hart","Jonathon"],scripture=["1 Corinthians 13:11","Luke 16:10"],translation="NIV")
json.dump(meta,open(KIT+'metadata.json','w'),indent=2,ensure_ascii=False)
open(KIT+'metadata.md','w').write(f"""# E001 metadata

| Field | Value |
|---|---|
| Show | Walk Steadfast |
| Episode title | {TITLE} |
| Episode number | 1 |
| Season | 1 |
| Episode type | full |
| Explicit | false (Clean) |
| Publish date | Tue, 05 Jan 2027 05:00:00 -0600 (5:00 AM CT) |
| Duration | {meta['duration_seconds']} s ({meta['duration_hms']}) |
| Audio file | E001-walk-steadfast.mp3, {size:,} bytes, audio/mpeg, 192 kbps, 44.1 kHz |
| GUID | walksteadfast-e001 (set once, never change) |
| Episode link | https://walksteadfast.com/episodes/e001 (confirm the site path before launch) |
| Transcript | E001-transcript.vtt (text/vtt), E001-transcript.srt (application/srt) |
| Chapters | chapters.json (podcast namespace), chapters.txt |
| Episode art | none, the show cover is used |
| Hosts | Wes Hart, Jonathon |
| Scripture | 1 Corinthians 13:11, Luke 16:10 (NIV) |

The audio file lives at `episodes/E001/E001-walk-steadfast.mp3`. The byte size changes if the file is rebuilt, so read it again at upload.
""")
desc=f"""What kind of man are you on a regular Tuesday? Wes Hart and Jonathon open Walk Steadfast at one table with that question.

This is the launch episode, so it runs a little longer. Wes and Jonathon introduce each other, then correct each other. Jonathon tells about the two years he took the long way home on 1604 so bath time would be over when he walked in. Wes tells about his fog years and the recliner. They read 1 Corinthians 13:11 and Luke 16:10, argue about rest and hiding, and leave one question open. At the end they lay out the book, the 24 training sessions and what the show does each week.

Chapters
{chap}

Scripture
1 Corinthians 13:11 and Luke 16:10 (NIV)

This week's challenge
Eat one meal with no phone at the table. If you're married, ask your wife, "What's Tuesday like for you?" and listen without fixing anything. If you're single, eat with someone and ask about his week. Then text one man, "How's your Tuesday?"

Mentioned
Steadfast Men: The way of Godly Men by Wes Hart (coming), chapter 1, "A Quiet Tuesday"
Steadfast training, 24 sessions (coming), session 1
Both will be at walksteadfast.com

New episodes every Tuesday, plus Field Notes every Friday.

walksteadfast.com
@steadfastwalk on Instagram, X, Facebook and TikTok

{NIV}

Produced with AI voice and video tools.
"""
open(KIT+'description.txt','w').write(desc)
notes=f"""# The Man You Keep Saying You'll Be
Walk Steadfast, Episode 1 · January 5, 2027

Most men are measured by their highlight days. Walk Steadfast starts with the day that makes a man, an ordinary Tuesday.

Wes Hart and Jonathon open the show at a walnut table with two mugs and one question. What kind of man are you on a regular day? Not the day with the pictures. A Tuesday.

Wes is 52, lives in the Texas Hill Country, and has been married 27 years. He calls his thirties "the fog years." At 36 an older man at a men's breakfast asked him, "What are you waiting on?" and then met him every other Thursday for six years. Jonathon is 37, a sales manager from Pasadena, Texas, married to Dani, a night-shift labor and delivery nurse, with two kids. His dad left when he was nine. He came to faith at 29. The two men have met most Thursdays for seven years.

For two years Jonathon took the long way home on 1604 so bath time would be over when he got there. "I skipped the Tuesday," he says. Wes tells on himself too. He did the big things, then ate supper in the recliner while his family sat fifteen feet away.

## Chapters

{chap}

## Scripture (NIV)

"When I was a child, I talked like a child, I thought like a child, I reasoned like a child. When I became a man, I put the ways of childhood behind me." 1 Corinthians 13:11

"Whoever can be trusted with very little can also be trusted with much, and whoever is dishonest with very little will also be dishonest with much." Luke 16:10

## This week's challenge

One meal with no phone. The phone goes in another room or in the truck, not face-down on the table. Married men ask their wife, "What's Tuesday like for you?" and listen without fixing anything. Single men eat with someone and ask about his week. If you live alone, invite somebody, and if nobody can come, eat at the table and pray out loud before you eat. Then text one man, "Hey, how's your Tuesday?" On Friday, Field Notes reports whether Wes and Jonathon did it.

## Carry this

You don't become a man someday. You put something down on a Tuesday.
Whatever your 1604 is, take the direct route home.

## Mentioned

Steadfast Men: The way of Godly Men by Wes Hart, chapter 1, "A Quiet Tuesday" (coming)
Steadfast training, session 1 (coming)

walksteadfast.com · @steadfastwalk

{NIV}

Produced with AI voice and video tools.
"""
open(KIT+'show-notes.md','w').write(notes)
print('runtime',meta['duration_hms'],round(dur,1),'s')
