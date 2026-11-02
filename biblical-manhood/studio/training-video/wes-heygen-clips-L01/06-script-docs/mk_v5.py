import re
src=open('rewrite-2026-10-27/L01/L01-SPOKEN-SCRIPT-v4-camera.md').read().split('\n---\n',1)[1]
R={
'L013':'So before you get going, I want you to hear one thing from me. [beat]',
'L024':'You and I do this one lesson at a time. [beat] Twenty-four of them. [pause 0.7]',
'L076':"I'd guess you're a little like that too. [beat] You'll research a tool for an hour. [beat] You won't look at your own day for five minutes. [pause 1.2]",
'L100':"Got it? [beat] Good. [beat] Hang on to that word. [beat] I'm coming back to it. [pause 2.0]",
'L106':"Busy is an easy place for a good man to hide. [beat] He's competent, so nobody looks closer. [pause 0.7]",
'L107':"If you're getting things done, nobody asks questions. [beat] Least of all you. [pause 0.7]",
'L140':"You're probably not refusing to show up. [beat] You're waiting. [beat] I know I do it. [pause 0.7]",
'L168':"That's true for more fathers and sons than you'd think. [beat] Nobody stood next to you on a plain day and said, here, this is what a man does. [pause 0.7]",
'L171':'Third one. [beat] "I\'m too old. [beat] I\'m retired. [beat] That\'s for a younger man." [pause 0.7]',
'L208':"Next lesson we look at why that's been so hard. [beat] Why a good man keeps waiting, even when he knows better. [pause 0.7]",
'L018':"Maybe you figured this was for somebody younger. [beat] You're on time. [pause 0.7]",
}
out=[]
for ln in src.split('\n'):
    m=re.match(r'(L\d{3}) ',ln)
    if m and m.group(1) in R: ln=m.group(1)+' '+R[m.group(1)]
    out.append(ln)
body='\n'.join(out)
spoken=lambda s: re.sub(r'\[[^\]]*\]','',re.sub(r'^L\d{3} ','',s))
lines=[spoken(l) for l in body.split('\n') if re.match(r'L\d{3} ',l)]
w=sum(len(re.findall(r"[A-Za-z0-9'’-]+",l)) for l in lines)
pz=sum(float(x) for x in re.findall(r'\[pause ([\d.]+)\]',body)); bt=body.count('[beat]')
hdr=f"""# Steadfast Men · Lesson 1 · A Quiet Tuesday · SPOKEN SCRIPT v5 (one man, face to face) · 2026-10-29 CT
Made from v4-camera. Wes talks to one man across a table. Singular you only. "We", "us" and "let's" mean only Wes and the one man watching (you and me), never a group.
**Kept:** every teaching point, the three NIV scriptures word for word (Luke 16:10, James 4:17, 1 Corinthians 13:11), every story beat, both workbook pauses, the final write-down, the one move, the same order, and the four locked lines ("Here's how this goes", "one lesson at a time", "one move. One.", "Next lesson we look at").
**Changed (R23):** L013, L018, L024, L076, L100, L106, L107, L140, L168, L171, L208. The four plural "men" lines are gone; every "we" line was read and kept only where it means Wes and the viewer.
**Numbers:** {w} spoken words · {len(lines)} lines · {bt} beats (~0.45 s) and {pz:.1f} s of marked meaning pauses. At the locked intro pace (150 wpm, pauses included, the way the intro is measured) the audio runs **about {w/150:.1f} min ({int(w/150)}:{int(round((w/150%1)*60)):02d})**.
**Pace note:** [beat] and [pause N] are meaning pauses for source prep (prep_source.py overrides), not TTS tags. Pace comes from delivery plus prep (recipe Step 1-3), not per-section tempo.
Markers: new line = new thought. Paragraphs are blank-line separated for fa19.py.

---"""
open('L01-build-2026-10-29/L01-SPOKEN-SCRIPT-v5-one-man.md','w').write(hdr+body)
# plain text for fa19 / TTS
txt='\n\n'.join(spoken(l).strip() for l in body.split('\n') if re.match(r'L\d{3} ',l))
txt=re.sub(r'  +',' ',txt)
open('L01-build-2026-10-29/L01-v5-script.txt','w').write(txt)
print(w,len(lines),bt,pz,w/150)
