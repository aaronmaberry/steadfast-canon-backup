import json
A = {r["ch"]: r for r in json.load(open("../audit.json"))["rows"]}
import re, glob
B = "/workspace/biblical-manhood/book/_opus55-second-pass-2026-10-01/book/"
def total(n):
    f = glob.glob(B + f"{n:02d}-*.md")[0]
    return len(re.findall(r"[A-Za-z0-9'’]+", open(f).read()))
# ch: (part, title, topic, W, course topics (internal), overlaps)
M = {
1: ("One","A Quiet Tuesday","Manhood is built in ordinary days, not big ones (Roy, Walt, Anthony)","W01","01","Matthew 7:24 house on the rock also in ch17. Tuesday frame comes back in ch35"),
2: ("One","You Are Not Crazy","The confusion is real: six maps, none agree; the same bruise at every age","W02","01, 10, 11","Genesis 1:27 image also in ch18. Seasons roll call also in ch32"),
3: ("One","The Four Marks","The creed, one sentence; a picture for each mark","W03","13, 14","Each mark's verse is boxed again in ch4-7 (by design)"),
4: ("One","Stop Waiting","Mark 1. Passivity in good costumes; start before you feel like it","W04","13, 14","Adam hiding (Gen 3:9) also in ch18, ch19. 'Seen in secret' also in ch7, ch33. Passivity at every age also in ch32"),
5: ("One","Pick Up the Weight","Mark 2. Carry what's yours; more than a paycheck","W05","13, 14","Provider vs presence comes back in ch24. Moses' load (Num 11) stands alone"),
6: ("One","Go First","Mark 3. Jesus went ahead; small doors; your number is second","W06","13, 14","Nehemiah also in ch34. 2 Timothy also in ch11, 14, 17, 28, 32"),
7: ("One","Work for God's Pay","Mark 4. Reward as inheritance, never wages","W07","13, 14, 23","Matthew 6 'in secret' also in ch4, ch33. Col 3:23-24 also in ch3, ch30"),
8: ("Two","The Empty Chair","Father absence; what fills the seat; yours to answer for (Curtis)","W08","02","Father wound also in ch10, ch11, ch12. Curtis continues in ch10"),
9: ("Two","Anger, the Itch, and the Drift","Three escapes from pain; the same root (Owen)","W09","02, 03, 09","The shapes of sin in ch16 and the ditches in ch31 cover nearby ground"),
10: ("Two","The Father Who Does Not Leave","God the Father as the original; sonship (Curtis)","W10","03","Baptism blessing (Matt 3:17) also in ch11 and ch27 (Mark 1:11). Prodigal stands alone"),
11: ("Two","When Home Never Handed You Off","Nobody counted you in; the mother who held the house; Jacob; blessing now (Nate)","W11","03, 04, 05","Mother and father of the home also in ch12. 'Counted in' and ceremony also in ch29. Baptism words also in ch10"),
12: ("Two","Leave Without Slamming the Door","The slam vs the grip; honor; forgive; Grant's porch","W12","03, 04, 05","Same house as ch11. Genesis 2:24 also in ch25"),
13: ("Two","A Man With No Brothers","Isolation; a brother; twenty minutes a week (Dale, Kenny)","W13","06, 07","Brothers return in ch35. Mentor side is ch14"),
14: ("Two","Ask the Man","Ask an older man; be the older man (Travis, Harlan)","W14","06, 07","Same subject as ch13 (the course pairs them). 2 Timothy chain"),
15: ("Two","The Problem Inside","Sin is inside, even with a perfect father; confession (Cody, Wade)","W15","08, 09","ch16 opens as its second half. Wade returns in ch26"),
16: ("Two","How That Looks on a Man","The shapes sin wears; David and Nathan","W16","09","Second half of ch15. Escapes overlap ch9"),
17: ("Two","No Fixed Star","No fixed point; the Word as plumb line; how to read it","W17","10","Plumb bob also in ch29. Matthew 7:24 also in ch1. 'Word steers' also in ch31"),
18: ("Three","Before the Fall","God's design in Genesis 1-2: dust, blessing, work, rest, 'not good', naming","W18","12","Work before the curse also in ch30. Genesis 1:27 also in ch2"),
19: ("Three","Two Men, Two Ways","Two gardens, two Adams; Gethsemane; in Christ","W19","12, 13, 14","Continues ch18's story directly. Adam's silence also in ch4"),
20: ("Three","Destiny Is Not a Vibe","Purpose is faithfulness where God put you (the dock)","W20","10, 14","Ephesians 2:10 also in ch7. Vision theme also in ch17"),
21: ("Four","If There Is No Wife Yet","Single, divorced and widowed men; build while you wait (Micah)","W21","15, 22","Season seats also in ch25 and ch32. Protected whole"),
22: ("Four","Know Her","Live with her according to knowledge; how to learn her","W22","15, 17","ch24 leans on it ('we've already done the heavy lifting on knowing her')"),
23: ("Four","Lay It Down","Ephesians 5 headship as laying down your life (the wet floor)","W23","15, 16","Philippians 2:5 also in ch3. Practical side is ch24"),
24: ("Four","What She Actually Needs","She needs you, not more of what you make (Russ, Renee)","W24","16, 17","ch5's paycheck line, ch22's knowing her, ch23's servant posture"),
25: ("Four","The Bed Is a Covenant","Sex as covenant, not contract; purity across seasons","none (after week 24)","18","Genesis 2:24 also in ch12. Season seats also in ch21"),
26: ("Four","Your Daughter Is Watching","She learns her worth from your face (Wade, Nora)","none","19","Wade from ch15"),
27: ("Four","Give Your Son a Name","Identity spoken over a son (Ray)","none","20","Baptism voice (Mark 1:11) also in ch10, ch11. One of three son chapters"),
28: ("Four","Give Your Son a Hill","A challenge just too big, with a man watching (Lyle)","none","20","One of three son chapters"),
29: ("Four","Give Your Son a Day He Will Not Forget","A ceremony; Alton's creek and plumb bob","none","20, 24","Ceremony and counted-in also in ch11. Plumb line also in ch17"),
30: ("Five","You Were Made for a Work","Work as calling; after the job; when you hate it (Gil)","none","21, 23","Work before the curse also in ch18. Col 3:23-24 also in ch3, ch7. Hidden work also in ch33"),
31: ("Five","Feelings Are the Dash, Not the Wheel","Emotions report; the Word steers; Elijah (Clay, Vernon)","none","21","'Word steers' also in ch17"),
32: ("Five","Every Season Still Counts","The marks at every age, from single to the final stretch","none","22","Season seats also in ch2, ch21, ch25 and every closer"),
33: ("Five","What You Are Building When Nobody Claps","Hidden, faithful work; legacy (Roy, the barn)","none","23","Matthew 6 secret also in ch4, ch7. Work also in ch30"),
34: ("Five","Write the Next Move","The written man plan (Hollis)","none","24, 11","Seasons page also in ch32. Nehemiah also in ch6. Joshua also in ch29, ch32"),
35: ("Five","These Men Are My Brothers","The brothers, a benediction, the open chair","none","24, 07","Brothers from ch13. Tuesday from ch1"),
}
rows = ["| Ch | Part | Title | What it's about | Words (file / body) | Session | Course topic | Overlaps |", "|---|---|---|---|---|---|---|---|"]
for n in range(1, 36):
    p, t, top, w, c, o = M[n]
    rows.append(f"| {n} | {p} | {t} | {top} | {total(n):,} / {A[str(n)]['body_words']:,} | {w} | {c} | {o} |")
open("_current-table.md", "w").write("\n".join(rows) + "\n")
print(sum(total(n) for n in range(1,36)), sum(A[str(n)]['body_words'] for n in range(1,36)))
for pair in [(11,12),(13,14),(15,16),(18,19),(23,24),(27,28,29),(17,20),(30,33),(32,34)]:
    print(pair, sum(A[str(n)]['body_words'] for n in pair), sum(A[str(n)]['body_words']+A[str(n)]['byt_words'] for n in pair))
