"""INTRO v2 CALM (Director notes + Aaron 9:10 PM). 10 layouts. Cues from AUDIO_WORDS/AUDIO_LINES (swappable); Wes = fb8d5e83 (lip-synced to v5)."""
import json,os
A='/workspace/artifacts/training/audio-podcast-voice-2026-10-26/INTRO-classroom-2026-10-27/v5-old-intro-voice/'
W=json.load(open(os.environ.get('AUDIO_WORDS',A+'INTRO-classroom-v5-old-intro-voice-words.json')))
L={r['line']:r for r in json.load(open(os.environ.get('AUDIO_LINES',A+'INTRO-classroom-v5-old-intro-voice-line-times.json')))}
WES=os.environ.get('WES','/workspace/artifacts/training/intro-final-2026-10-27/heygen/raw-heygen-fb8d5e83.mp4')
I='/workspace/steadfast-main/img/';BAN='/workspace/steadfast-main/brand/social-banners-LOCKED/'
def cue(word,after):
    for w in W:
        if w['start']>=after-1e-3 and w['word'].lower().strip('.,?!"“”—').startswith(word.lower()):return round(w['start']-0.05,3)
    raise KeyError((word,after))
def B(line):
    ks=sorted(L);i=ks.index(line);return 0.0 if i==0 else round((L[ks[i-1]]['end']+L[line]['start'])/2,3)
s=lambda l:L[l]['start']
LAST=max(w['end'] for w in W)
S=[
 dict(id='A',t0=0.0,type='wes',lower=(1.0,4.0,'STEADFAST MEN','Training for men')),
 dict(id='B',t0=B('I08'),type='split',stills=[(B('I08'),I+'lesson-intro.jpg'),(s('I09'),I+'audio.jpg'),(s('I11'),I+'workbook-wh.jpg')],
      rows=[(s('I08'),'A video'),(cue('audio',s('I09')),'An audio-only version'),(cue('transcript',s('I10')),'A transcript'),(cue('weekly',s('I11')),'A weekly workbook activity'),(cue('complete',s('I12')),'The complete workbook, on the site')]),
 dict(id='C',t0=B('I13'),type='stills',bubble=True,stills=[(B('I13'),I+'book-pair.jpg',None),(B('I14'),'/workspace/artifacts/training/intro-final-2026-10-27/v11-work/assets/podcast-hero-table-LIVE-crop-y58-1232.png','Walk Steadfast'),(cue('YouTube',s('I16')),BAN+'youtube-banner-2560x1440.png',None)]),
 dict(id='D',t0=B('I17'),type='wes'),
 dict(id='D2',t0=cue('place',cue('there',s('I18'))+0.1),type='sites',bubble=True,pages=[('/workspace/artifacts/training/intro-final-2026-10-27/assets/site-home@2x.png','walksteadfast.com'),('/workspace/artifacts/training/intro-final-2026-10-27/assets/site-give@2x.png','walksteadfast.com/give')]),
 dict(id='E',t0=B('I21'),type='board',kicker='THE ROAD',rows=[(s('I21'),'24 sessions'),(s('I22'),'We start with ordinary days')],big_first=True),
 dict(id='F',t0=B('I23'),type='split',stills=[],kicker='FOUR MARKS',rows=[(cue('Stop',s('I23')),'Stop waiting'),(cue('pick',s('I23')),'Pick up the weight'),(cue('go',s('I23')+2),'Go first'),(cue('work',s('I23')+2),"Work for God's pay"),(s('I24'),'A gift He gives His kids')]),
 dict(id='G',t0=B('I25'),type='board',bubble_from=118.40,kicker='THE ROAD AHEAD',rows=[(cue('dad',s('I25')),'Look back: your dad, the home you came out of,'),(cue('friends',s('I25')),"the friends you don't really have, what's broken in every one of us"),(s('I26'),'Genesis: what God had in mind when He made a man'),(s('I27'),'Home: your wife, your daughters, your sons')]),
 dict(id='H',t0=B('I28'),type='wes'),
 dict(id='I',t0=B('I31'),type='scripture',bubble=True,ref=(s('I31'),'1 CORINTHIANS 15:58 · NIV'),
      vlines=[(cue('Therefore',s('I32')),'Therefore, my dear brothers and sisters, stand firm.'),(cue('Let',s('I32')),'Let nothing move you.'),(cue('Always',s('I32')),'Always give yourselves fully to the work of the Lord,'),(cue('because',s('I32')),'because you know that your labor in the Lord is not in vain.')],
      hi=(s('I33'),'fully')),
 dict(id='J',t0=B('I34'),type='wes',close=[(cue('stand',s('I35')),'Stand firm.'),(cue('Let',s('I35')),"Let's get to work.")]),
]
I_HOLD_AFTER=1.2
END=round(LAST+1.0,2);FADE=0.8;TOTAL=round(END+FADE,2)
for a,b in zip(S,S[1:]):a['t1']=b['t0']
S[-1]['t1']=TOTAL
