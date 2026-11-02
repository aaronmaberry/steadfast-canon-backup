import re,json
B=open('L01-SPOKEN-SCRIPT-v5-one-man.md').read()
L={}
for l in B.split('\n'):
    m=re.match(r'(L\d{3}) (.*)',l)
    if m: L[int(m.group(1)[1:])]=m.group(2)
def clean(s): return re.sub(r'\s+',' ',re.sub(r'\[[^\]]*\]','',s)).strip()
W={k:len(re.findall(r"[A-Za-z0-9'-]+",clean(v))) for k,v in L.items()}
tot=sum(W.values()); target=tot/150*60
P={k:v.count('[beat]')*0.45+sum(float(x) for x in re.findall(r'\[pause ([\d.]+)\]',v)) for k,v in L.items()}
k=(target-sum(P.values()))/tot
t=0;T={}
for i in sorted(L): T[i]=(t,t+W[i]*k+P[i]); t=T[i][1]
# shot list: (first,last,kind,picture)
S=[
(1,3,'WES_FULL','Wes full frame, native width (burg_a look), lower third "STEADFAST MEN / Lesson 1 · A Quiet Tuesday" in Geist, accent #5b6ef5, in at the first word, out before line 3 ends'),
(4,5,'SPLIT','Wes panel left 60%, board right 40%. Numbered chips build on cue words: "Husband" · "Dad" · "A job, same as you" · "Your teacher for 24 lessons"'),
(6,9,'WES_FULL','Wes full frame. No graphics; he is talking to the man where he is'),
(10,12,'TYPE_BOARD_BUBBLE','Type board, big first row "Just looking. No promises." then "I started out that way too." Oval bubble top-right'),
(13,19,'TYPE_BOARD_BUBBLE','Type board, call and response. Rows build on each "Maybe...": Young · Married · Divorced, still a dad · Figured it was for somebody younger. Each answer row "You\'re on time." Last row "This is yours." Bubble top-right holds through'),
(20,22,'WES_FULL','Wes full frame. Callout under chest height on "something true": "Something true · where it shows up · one thing to do"'),
(23,26,'SPLIT','Wes panel left. Board right: "One lesson at a time" big, then "24 lessons. One a week."'),
(27,31,'TYPE_BOARD_BUBBLE','Type board, numbered chips 1 "I teach" and 2 "You stop and write". Bubble top-right'),
(28,29,'BRANDED_STILL_BUBBLE','Branded still: Steadfast Men workbook (our product shot, workbook asset), slow 4.5% Ken Burns push, bubble top-right. Inserted inside the board passage on "workbook next to you"'),
(32,36,'TYPE_BOARD_BUBBLE','Type board: chip 3 "One move. One." big first row, then "Not a list." Row "A list on Sunday. On the floor of the truck by Wednesday." Bubble top-right'),
(37,39,'WES_FULL','Wes full frame. Closing type at chest height: "Show up. Tell the truth. Do the move." one phrase at a time'),
(40,42,'TYPE_BOARD_BUBBLE','Big idea card: "A man\'s life gets decided on the days nobody photographs." full width, held through the 1.8 s pause and the repeat. Bubble top-right'),
(43,44,'BRANDED_STILL_BUBBLE','Branded still: lockup-steadfast-men on navy with ambient glow (tl), rows "Your wedding · A baby · A new job · A retreat" build on cue. Bubble top-right'),
(45,48,'WES_FULL','Wes full frame. No graphics through the question and "Yeah. Mine too."'),
(49,50,'SPLIT','Wes panel left. Board right: "A big day can mark you." / "It can\'t give you a habit." / "Most days are just Tuesday."'),
(51,53,'SCRIPTURE_BUBBLE','Scripture card, reference on top "Luke 16:10 (NIV)", read line by line, "very little" in accent on both lines. Bubble top-right'),
(54,61,'SCRIPTURE_BUBBLE','Same scripture card stays; "very little" highlight pulses once on "Two words show up twice"; side rows "Trusted in little, trusted in much" · "Dishonest in little, dishonest in much"'),
(62,64,'WES_FULL','Wes full frame. Callout on the answer: "The very little."'),
(65,71,'TYPE_BOARD_BUBBLE','Point 1 card: chip "1" big "What a Tuesday is". Rows: "Nothing worth dressing up for" · "A small yes: say it or swallow it" · "The name doesn\'t matter. The day does." Bubble top-right'),
(72,76,'SPLIT','Wes panel left. Board right: "Leaf blowers. 30 minutes. Reviews. Decibel ratings." then "The prayer was real. The phone was easier."'),
(77,81,'WES_FULL','Wes full frame for the bike story start. No graphics'),
(82,88,'SPLIT','Wes panel left. Board right, quiet rows: "After supper" · "One thing" · "Porch light. Tire still soft." · "Fixed it. In the dark. By myself."'),
(89,92,'WES_FULL','Wes full frame. Hard cut in the pause before "And I felt useful". Hold through "I did the job. And I missed my girl." No graphics'),
(93,96,'TYPE_BOARD_BUBBLE','Exercise card: "Pause and think" chip. Rows "Yesterday" · "One small yes. A person, not a task." · "Said it, or swallowed it?" Bubble top-right'),
(97,100,'BRANDED_STILL_BUBBLE','Branded still: workbook open to Lesson 1 (our workbook asset, second crop, different frame from shot 9). Rows: "Phone · Work · Later · Tired". On-screen cue "Pause this and write it." Bubble top-right'),
(101,105,'TYPE_BOARD_BUBBLE','Point 2 card: chip "2" big "Busy is not the same as there". Row "\'I was busy, so I must have been there.\'" Bubble top-right'),
(106,108,'WES_FULL','Wes full frame'),
(109,115,'SPLIT','Wes panel left. Board right: "The true sentence" · "The softer one" · "\'Long day.\'" · "Three feet apart"'),
(116,121,'WES_FULL','Wes full frame for the older man\'s question. Callout at chest height on the two quotes: "What couldn\'t they have hired out?" then "I asked where you were."'),
(122,126,'SPLIT','Wes panel left. Board right: "The hero of your to-do list. A stranger in your own house." Then "Not how much. Where."'),
(127,132,'TYPE_BOARD_BUBBLE','Recap card, numbered chips 1-3: "Decided on the days nobody photographs" · "God builds you in the very little" · "Busy is not the same as there". Bubble top-right'),
(133,135,'TYPE_BOARD_BUBBLE','Mark card: "The first mark" small, "Stop Waiting." big, drawn accent rule. Bubble top-right'),
(136,141,'SCRIPTURE_BUBBLE','Scripture card, ref top "James 4:17 (NIV)", read line by line; "knows the good... and doesn\'t do it" in accent. Rows "A better season · Feeling ready · After supper". Bubble top-right'),
(142,144,'WES_FULL','Wes full frame. No graphics for the twenties story'),
(145,147,'SCRIPTURE_BUBBLE','Scripture card, ref top "1 Corinthians 13:11 (NIV)", read line by line. Bubble top-right'),
(148,154,'SPLIT','Wes panel left. Board right: "Talked · Thought · Reasoned" then "I put them behind me. On purpose." then "A man\'s yes is still standing after the feeling\'s gone."'),
(155,157,'WES_FULL','Wes full frame. Callout "Rest is good. Waiting is something else."'),
(158,161,'TYPE_BOARD_BUBBLE','Exercise card: "Pause and write". Rows "A better job? · A wife? · A clearer head? · Your dad to say it?" then "Mine to wait on, or mine to start?" Bubble top-right'),
(162,166,'SPLIT','Wes panel left. Board right: objection 1 chip "\'I\'m just tired.\'" then "An invitation, not a whip."'),
(167,170,'TYPE_BOARD_BUBBLE','Objection 2 card: "\'Nobody ever showed me how.\'" then "The door\'s open whether anybody showed you or not." Bubble top-right'),
(171,176,'WES_FULL','Wes full frame for Howard. Lower-third style callout "Objection 3 · \'I\'m too old.\'" then on the close "Being a man didn\'t clock out."'),
(177,179,'SPLIT','Wes panel left. Board right: objection 4 "\'I live alone.\'" rows "A brother · A friend · A kid at church". Last row "He\'s seen your Tuesday already."'),
(180,187,'TYPE_BOARD_BUBBLE','Monday card: timeline rows build: "Wake up: Who\'s mine today?" · "Breakfast: put the cup down" · "The drive: send the text" · "Work: do it well" · "Home: the true sentence first". Bubble top-right'),
(188,194,'TYPE_BOARD_BUBBLE','Your move card: chip "One move" big first row "One meal. Phone in another room." Then "Text one man you trust: What did you do with your Tuesday?" Bubble top-right'),
(195,197,'TYPE_BOARD_BUBBLE','Write-down card: "My next move on a Tuesday is ..." with three blank lines: day, meal, name. On-screen cue "Pause this and write it." Bubble top-right'),
(198,202,'TYPE_BOARD_BUBBLE','Closing recap card: the three points plus "Mark 1: Stop Waiting." Fresh card style variant from shot 30 (no chips, big first row). Bubble top-right'),
(203,206,'WES_FULL','Wes full frame. No graphics through the gospel lines'),
(207,208,'SPLIT','Wes panel left. Board right: "That\'s where your Tuesday goes missing. Go show up for it." then "Next lesson: why a good man keeps waiting."'),
(209,210,'WES_FULL','Wes full frame. Closing type at chest height: "That was your first yes." then end card STEADFAST MEN lockup after the last word, dip to bg'),
]
sh=lambda n: n if n<3 else n+6
S=[(sh(a),sh(b),k,p) for a,b,k,p in S]
S=S[1:]; S[0]=(9,S[0][1],S[0][2],'Lower third "Wes Hart" (Geist, accent #5b6ef5) in on "I\'m Wes", out before "I\'m a husband" ends. '+S[0][3])
S=[(1,3,'TITLE_CARD','Lesson title card (R33): full-screen navy #07070a board, small Geist Mono kicker "STEADFAST MEN · LESSON 1", big Geist title "A Quiet Tuesday", drawn accent rule under it (#5b6ef5). Title builds 40 ms before "Lesson One"; title line lands on "A Quiet Tuesday". Wes voice only, no bubble on the title card'),
   (4,8,'AGENDA','Lesson agenda board (R33): heading "Today" then numbered chips build on cue words, one row per spoken item: 1 "What a Tuesday is, and the very little" @"First" · 2 "Busy is not the same as there" @"Second" · 3 "The first mark: Stop Waiting" @"Third" · 4 "Your reasons for waiting, and one move" @"Then". Oval bubble top-right enters after the heading, holds through the agenda (≥9 s)')]+S
rows=[];n=0
for a,b,kind,pic in S:
    if (a,b)==(34,35): continue
    n+=1
    if kind!='WES_FULL' and kind!='SPLIT' and (a<=34<=b):
        pass
    rows.append((a,b,kind,pic))
# split shot 27-31 around the workbook still
out=[]
for a,b,kind,pic in rows:
    if (a,b)==(33,37):
        out+= [(33,33,kind,pic),(34,35,'BRANDED_STILL_BUBBLE',[s for s in S if s[:2]==(34,35)][0][3]),(36,37,kind,'Type board continues: chip 2 "You stop and write". Bubble top-right (same bubble, no re-fade)')]
    else: out.append((a,b,kind,pic))
ALT={'TYPE_BOARD_BUBBLE':'SPLIT','SPLIT':'WES_FULL','WES_FULL':'SPLIT','SCRIPTURE_BUBBLE':'SCRIPTURE_BUBBLE','BRANDED_STILL_BUBBLE':'TYPE_BOARD_BUBBLE'}
NOTE={'SPLIT':'Wes panel left 60%, board right 40%; rows carry the key phrase of these lines (built on cue words)','WES_FULL':'Wes full frame, no graphics (rest for the eye)','SCRIPTURE_BUBBLE':'Same scripture card, next lines highlighted; bubble continues','TYPE_BOARD_BUBBLE':'Type board continues with the next rows; bubble continues'}
def dur(a,b): return T[b][1]-T[a][0]
changed=True
while changed:
    changed=False;nx=[]
    for a,b,kind,pic in out:
        if dur(a,b)>26 and b>a:
            mid=T[a][0]+dur(a,b)/2; c=min(range(a,b),key=lambda j:abs(T[j][1]-mid))
            nx+=[(a,c,kind,pic),(c+1,b,ALT[kind],NOTE[ALT[kind]]+(': "'+re.split(r'(?<=[.?!])\s',clean(L[c+1]))[0]+'"' if ALT[kind]!='WES_FULL' else ''))];changed=True
        else: nx.append((a,b,kind,pic))
    out=nx
def fmt(x): m=int(x//60); return f"{m}:{x-60*m:05.2f}"
lines=[];mix={}
prev=None
for i,(a,b,kind,pic) in enumerate(out,1):
    tin=T[a][0]; tout=T[b][1]
    spoken=' '.join(clean(L[j]) for j in range(a,b+1))
    tr='hard cut in pause' if (prev and (prev=='WES_FULL')==(kind=='WES_FULL') and kind in('WES_FULL','SPLIT')) else 'dip-to-bg 0.4 s (outgoing fully out first)'
    if i==1: tr='fade from bg 0.4 s'
    mix[kind]=mix.get(kind,0)+tout-tin
    lines.append(f"| S{i:02d} | {fmt(tin)}–{fmt(tout)} | {tout-tin:.1f} s | {kind} | L{a:03d}–L{b:03d} | {spoken} | {pic} | {tr} |")
    prev=kind
total=T[216][1]
hdr=f"""# L01 · A Quiet Tuesday · PRODUCTION SCRIPT + STORYBOARD (P1, written before any audio or video work) · 2026-10-29 CT
Script: `L01-SPOKEN-SCRIPT-v5-one-man.md` ({tot} spoken words). Look plan: `registry/looks/L01.json` (signature 199f31b72a63). Wes source: burg_a (v4 burgundy tee, cleaned).
**Timing is projected, not measured.** No L01 audio exists yet. Times assume the locked intro pace, 150 wpm for the whole file with pauses included ({fmt(total)} total). Each line gets a share of time from its word count, plus 0.45 s per [beat] and the marked [pause N] seconds; speech runs about {60/k:.0f} wpm between pauses, close to the old natural delivery (193 wpm before atempo 0.79). At P3 the real word times (fa19) replace these; every cut moves to the middle of the silence before a line's first word, and builds land 40 ms before their cue word, exactly as in the intro PRODUCTION-SCRIPT.md.
**R32 (Aaron 6:28 AM):** the Spoken column is the full natural prose for each passage, word for word, paired with its In–Out time. No fragments or shorthand for spoken text.

**R33 (Aaron 7:29 AM):** the lesson opens on the lesson title card, then the spoken agenda (both are in the audio script, L001-L008), and ends with the approved Steadfast logo fading in and out over a silent hold.

## Fixed rules for every shot
- Colors and fonts from walksteadfast.com TOKENS.json only: bg #07070a, accent #5b6ef5 (this lesson), Geist / Geist Mono. Text-card style: numbered-chip. Ambient glow corner: top-left.
- No music bed. No audience chairs. No signs or logos except our own. No clip or asset used twice (the two workbook stills are different files/crops; check the registry at P6).
- Bubble: oval 540x405, home top-right, 0.7 s in / 0.45 s out, snug, never over text, held at least 9 s (look plan hold 9 s). Where a bubble passage is shorter than 9 s, the bubble continues across the next non-Wes shot without re-fading, as in intro v10.
- Transitions: primary dip-to-bg 0.4 s, secondary hard cut in a pause. The outgoing shot is fully gone before the incoming one starts. Cuts sit only in pauses. One animated element at a time; nothing animates on Wes's panel.
- Wes never above native width (Z1). Variety comes from full / split 60-40 / bubble, not punch-ins.
- B-roll about the book, workbook or podcast is our own branded asset only. This lesson's words only name the workbook, so the branded stills are the workbook (twice, different crops) and the Steadfast Men lockup. The live podcast image (hero-table-LIVE-v11.jpg) and the YouTube banner are not used because L01's words never mention the podcast or the channel; the look plan's B-roll list is a pool, not a quota.

## Shot table
| # | In–Out | Hold | Layout | Lines | Spoken (v5, verbatim) | Picture / graphics | Transition in |
|-|-|-|-|-|-|-|-|
"""
LOGO=f"| S{len(out)+1:02d} | {fmt(total)}–{fmt(total+3.8)} | 3.8 s (silent) | LOGO_END | – | (no speech; silent hold, no music, room-tone bed only) | Approved Steadfast logo (R33): the live walksteadfast.com lockup `img/logo-lockup.jpg` (sha256 f9471087e25f…, 1142x412, copy in `assets/logo-lockup-LIVE-2026-10-29.jpg`) centred on #07070a at native size or smaller (never upscaled past 1.0x). After the last word's 0.6 s tail: hold bg 0.4 s, logo fades in 0.8 s, holds 1.6 s, fades out 0.8 s to bg, 0.2 s bg. Nothing else on screen | dip-to-bg 0.4 s after the last shot |"
summ=f"\n## Summary\n- **{len(out)+1} shots: {len(out)} spoken shots over {fmt(total)} plus the 3.8 s silent logo end ({fmt(total+3.8)} picture)**, {len(out)/(total/60):.1f} layout changes per minute (plus the logo end; look plan 4.1; passages over 26 s were split at a line end and the second half alternates layout, so no layout holds past about 26 s; the intro ran 9.2 per minute over 3 minutes, and in-shot row builds carry the movement in between). In-shot row builds change the picture every few seconds inside a shot.\n- Screen time by layout: " + ", ".join(f"{k} {v/60:.1f} min ({v/total*100:.0f}%)" for k,v in sorted(mix.items(),key=lambda x:-x[1]))+".\n- Count by layout: "+", ".join(f"{k} {sum(1 for o in out if o[2]==k)}" for k in ['TITLE_CARD','AGENDA','WES_FULL','SPLIT','TYPE_BOARD_BUBBLE','SCRIPTURE_BUBBLE','BRANDED_STILL_BUBBLE'])+".\n- Every board gets an in-shot build at least every 8-12 s. At P6, re-time against real word times and split any board that runs past 24 s without a build.\n- Open items for P6: confirm the workbook asset files and the lockup in the branded set; site captures are not needed for L01.\n"
open('L01-PRODUCTION-SCRIPT-STORYBOARD.md','w').write(hdr+'\n'.join(lines)+'\n'+LOGO+'\n'+summ)
json.dump([dict(shot=i+1,first=a,last=b,kind=kind,t_in=round(T[a][0],2),t_out=round(T[b][1],2)) for i,(a,b,kind,pic) in enumerate(out)],open('storyboard.json','w'),indent=1)
print(len(out),fmt(total),mix)
long=[(i+1,round(T[b][1]-T[a][0],1)) for i,(a,b,kind,pic) in enumerate(out) if T[b][1]-T[a][0]>60]
print('long',long)
