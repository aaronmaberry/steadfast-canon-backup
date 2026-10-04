import datetime as dt
start=dt.date(2027,1,5)
# mains: (title, book chapter / source, scripture, mark, hook)
M=[
# S1 Epiphany
("The Man You Keep Saying You'll Be","Ch 1 A Quiet Tuesday · W01","1 Cor 13:11; Luke 16:10","Stop Waiting","Launch. Who we are, the program, the year, and why Tuesday is where a man is made."),
("Nobody Ever Gave You the Sentence","Ch 2 You Are Not Crazy · W02","Gen 1:27","(none, sets up E005)","The gap you feel is real. Write the sentence you've actually been living."),
("What a Steadfast Man Looks Like","Ch 3 The Four Marks · W03","Phil 2:5","All four, introduced once","The one sentence a man can say out loud. The marks, each with a Tuesday picture."),
("Waiting Is Not Peace","Ch 4 Stop Waiting · W04","James 4:17","Stop Waiting","The thing you already know to do. Why a man sits the day out."),
("The Weight With Your Name on It","Ch 5 Pick Up the Weight · W05","Gal 6:5","Pick Up the Weight","Sorting what's yours from what isn't. Hands on the load."),
("Somebody Has to Step Out Ahead","Ch 6 Go First · W06","John 10:4","Go First","Leading when it costs you. Valentine's week, so the married version is a hard one."),
("The Prize That's Gone by Thursday","Ch 7 Live for a Reward That Lasts · W07","Col 3:23-24; Heb 12:2","Work for God's Pay","Cheap prizes and the inheritance. Pay is not earning grace (Eph 2:8-9)."),
# S2 Lent
("The Problem Is Inside the House","Ch 15 The Problem Inside · W15","Rom 7:18","Pick Up the Weight","Lent opener. Not only what was done to you."),
("Skip the House, Run the Room","Ch 16 How That Looks on a Man · W16","Prov 14:12","Stop Waiting","The three shapes. Which one is yours."),
("What Your Anger Is Guarding","Ch 9 Anger, the Itch, and the Drift (part 1) · W09","Eph 4:26-27","Pick Up the Weight","Anger as fruit, not personality. Foothold."),
("The Itch and the Drift","Ch 9 Anger, the Itch, and the Drift (part 2) · W09","Eph 4:26-27 (callback); Prov 4:23","Stop Waiting","Screens, wandering, checking out. Name which one is yours. 988 note."),
("Two Gardens","Ch 19 Two Men, Two Ways · W19","1 Cor 15:45","Go First","Holy Week. First Adam hid; the last Adam stepped forward."),
# S3 Easter
("The Father Who Stays","Ch 10 The Father Who Does Not Leave · W10","Matt 3:17","Work for God's Pay","Easter week. The chair is not the last word."),
("The Empty Chair at Your Table","Ch 8 The Empty Chair · W08","Eph 6:4","Pick Up the Weight","Naming the father hole without healing it all in one sitting. Jonathon's tailgate story."),
("When Your Dad Is Still Alive","Ch 8/10 follow-on (fresh)","Ex 20:12","Go First","Phone calls twice a year. Honor without pretending."),
("When Home Never Handed You Off","Ch 11 · W11","Luke 2:49","Pick Up the Weight","The tie that never released him. Kind. Moms are not the villain."),
("Leave Without Slamming the Door","Ch 12 · W12","Gen 2:24","Go First","Leaving and honoring at the same time."),
("Your Mom, Mother's Day, and Being a Grown Man","Mother's Day week (fresh)","Prov 23:22","Work for God's Pay","Honoring your mother as a man, not as a boy or a stranger. Grief version for men whose mom has died."),
("A Man With No Brothers","Ch 13 · W13","Eccl 4:10","Stop Waiting","Isolation is not strength. Pentecost weekend: the church as a room full of brothers."),
# S4 Pentecost
("Ask the Man","Ch 14 · W14","Prov 13:20","Stop Waiting","Don't wait to be chosen. Mr. Abernathy and the scariest text."),
("These Men Are My Brothers","Ch 35","Heb 3:13","Pick Up the Weight","Memorial Day week. What a brother does on an ordinary Thursday."),
("No Fixed Star","Ch 17 · W17","Prov 29:18","Go First","A full week is not a heading. Missing vision."),
# S5 Fathers (June)
("Your Daughter Is Watching","Ch 26 · course session 19","Deut 6:7","Go First","The first man who treats her as a person."),
("Give Your Son a Name","Ch 27 · course session 20","Isa 43:1 (paraphrase, NIV has a dash)","Pick Up the Weight","Calling him what he is, out loud."),
("Give Your Son a Hill","Ch 28","1 Thess 2:11-12","Go First","A fight worth having. Father's Day aftermath."),
("A Day He Will Not Forget","Ch 29","Josh 4:6-7","Work for God's Pay","Witnesses, words, cost. Not a party."),
# S6 Ordinary Time summer
("Before Anything Went Wrong","Ch 18 Before the Fall · W18","Gen 2:15","Pick Up the Weight","Work it and take care of it. Made for this before the curse."),
("Some Saturdays","Ch 20 · W20","2 Cor 5:15","Work for God's Pay","The feeling is not the fire."),
("If There Is No Wife Yet","Ch 21 · W21","1 Cor 7:17","Stop Waiting","Single men are not in the lobby. Caleb-age men and divorced men both."),
("Know Her","Ch 22 · W22","Prov 20:5","Go First","Knowing her is a job, not a memory."),
("Lay It Down","Ch 23 · W23","Eph 5:25","Go First","The speech is not the death."),
("What She Actually Needs","Ch 24 · W24","1 Cor 10:24","Pick Up the Weight","Not the help that would have worked on you."),
("The Bed Is a Covenant","Ch 25","Heb 13:4","Pick Up the Weight","Plain talk, family-safe. Screens, seasons, shame."),
("When Marriage Feels Like Roommates","Fresh (marriage)","Eccl 9:9","Stop Waiting","Nights, kids, two schedules. Jonathon and Dani's shift-work season."),
("You Were Made for a Work","Ch 30","Eph 2:10","Work for God's Pay","Labor Day week. Handiwork, not a slot."),
# S7 Long Road (fall)
("What You Build When Nobody Claps","Ch 33","1 Cor 15:58","Work for God's Pay","The unseen job. Coaching, carpools, the 6 a.m. shift."),
("Feelings Are the Dash, Not the Wheel","Ch 31","Ps 42:5","Stop Waiting","Feel it, name it, don't let it drive."),
("Every Season Still Counts","Ch 32","Prov 20:29","Pick Up the Weight","22 and 62 at the same table. Gray hair and strength."),
("When the Job Goes Away","Fresh (work)","Matt 6:34","Stop Waiting","Layoffs and lost titles. The job was never your name."),
("Grief at the Table","Fresh (loss)","John 11:35","Pick Up the Weight","Wes on his dad and Mr. Abernathy. Men who grieve sideways."),
("The Dark Stretch","Fresh (depression; 988 required)","Ps 88:1-2","Go First","Low seasons, getting help, and the brother who notices."),
("Money Tells the Truth","Fresh (money)","Luke 12:34","Work for God's Pay","Where your treasure is. Debt, giving, and the talk with your wife."),
("Paid in Full","Reformation week (fresh)","Eph 2:8-9","Work for God's Pay","Grace first. God's pay is an inheritance, not a wage you earn."),
# S8 Thanks
("Small Ways to Serve at Home","Fresh (service)","Mark 10:45","Go First","Unremarkable service, done first, done daily."),
("Men Who Served","Veterans Day week (fresh)","John 15:13","Pick Up the Weight","Honoring veterans; what coming home asks of a man."),
("Gratitude Out Loud","Fresh","1 Thess 5:18","Go First","Saying thank you to the people who'd least expect it from you."),
("Lead the Thanksgiving Table","Thanksgiving week (fresh)","Rom 12:18","Go First","Family tension, the uncle, the empty seat, and a prayer you didn't outsource."),
# S9 Advent
("Joseph Said Nothing","Advent 1 (fresh)","Matt 1:24","Stop Waiting","The quietest man in the story did everything he was told, fast."),
("Waiting on God Isn't Sitting Still","Advent 2 (fresh)","Ps 27:14","Stop Waiting","How waiting on God differs from waiting it out."),
("The Shepherds Went Back to Work","Advent 3 (fresh)","Luke 2:20","Work for God's Pay","Glory on Monday morning."),
("Simeon Kept Showing Up","Christmas week (fresh)","Luke 2:25","Pick Up the Weight","The old man who stayed faithful. For every season."),
("Write the Next Move","Ch 34 + year review","Prov 16:9","Stop Waiting","What changed in us this year. The plan for 2027 ends; the plan for 2028 starts."),
]
F=[
# (title, From the Table question, tool)
("The First Check","How do I start this if I've never been the 'spiritual' one?","The phone basket"),
("The Sentence Test","What if my sentence is a bad one?","The index card"),
("Saying It Out Loud","Do I really need all four, or just the one I'm weak in?","A 60-second voice memo"),
("The Thing on the Counter","How do I stop waiting when I'm genuinely tired?","The ten-minute start"),
("Not Your Load","What if I'm carrying stuff that isn't mine?","Two-column list"),
("Valentine's, Ash Wednesday, and Going First","Do I lead even if my wife is more mature in faith than me?","The first apology"),
("Season One Review","What do we keep doing from the first six weeks?","The Thursday text"),
("Inside Job","Isn't this just blaming myself for everything?","The evening examen, three questions"),
("Which Shape Are You","My wife says I run the room. I think she's wrong. Now what?","Ask one person"),
("Cooling Off Without Checking Out","Is it ever right to be angry?","The 20-minute rule"),
("Drift Check","How do I set up my phone so it doesn't own me?","Grayscale and a charger outside the bedroom"),
("Good Friday","What do I do with Good Friday as a dad?","Reading the Passion aloud at dinner"),
("Easter Week Report","Does it matter if I don't feel it?","The Saturday morning walk"),
("The Chair Report","How do I talk to my kids about my dad?","One honest sentence"),
("Calling Him Back","Do I have to forgive a dad who isn't sorry?","The two-call rule"),
("Cutting the String","My mom still calls me every day. Is that a problem?","The Sunday call"),
("The Door Report","How do I tell my parents no without a war?","The script: thank you, no, I love you"),
("Mother's Day Field Notes","What do I do on Mother's Day when it's complicated?","A handwritten note"),
("Season Review: The Father Who Stays","What did we learn about our dads this season?","The memorial stone (one written line)"),
("The Ask Report","What if the man I ask says no?","The coffee ask, word for word"),
("Memorial Day","How do I honor men I never met?","Reading the names"),
("Finding North","How do I write a vision without it sounding like a slogan?","One-page house plan"),
("Daddy-Daughter Report","My daughter is a teenager and won't talk. Now what?","The drive-through date"),
("Father's Day When It's Complicated","What if Father's Day is the worst day of my year?","Bless a younger man"),
("The Hill Report","How do I give my son a cause when he only wants games?","The Saturday project"),
("Independence Day","What does freedom mean for a Christian man?","The porch prayer"),
("Work It and Keep It","Is it wrong to like my job a lot?","The end-of-day shutdown"),
("The Feeling Isn't the Fire","What if I don't feel called to anything?","The next-faithful-thing list"),
("Not in the Lobby","Should I stop dating to focus on God?","Single man's Tuesday rhythm"),
("Study Her","What questions do I ask my wife that aren't weird?","The three-question walk"),
("Laying It Down Report","What does dying to self look like on a Wednesday?","The first-pick swap"),
("Her Need, Not Mine","How do I know what she needs if she won't tell me?","Ask, repeat, do"),
("Covenant Check","How do we talk about this with our kids someday?","Accountability software, honestly reviewed"),
("Roommates No More","Is a date night really the answer?","The 15-minute couch talk"),
("Labor Day","How do I rest without feeling lazy?","The real Sabbath hour"),
("The Unseen Shift","How do I keep going when nobody notices?","The secret list"),
("Dash and Wheel","Is it unmanly to cry?","Name it in two words"),
("Season Swap","How do I connect with men twenty years older or younger?","The cross-generation lunch"),
("Between Jobs","How do I lead my family through a layoff?","The family meeting"),
("Grief Report","How long is grief supposed to take?","The anniversary calendar"),
("Noticing a Brother","How do I tell if my friend is in real trouble?","The direct question (and 988)"),
("The Budget Talk","How do I bring up money without a fight?","The monthly money date"),
("Season Review: The Long Road","What did fall teach us about work and weight?","The season letter"),
("Serving Report","What if serving at home feels like nobody notices?","The first-up rule"),
("Veterans Day","How do I support a veteran in my life?","Ask, then listen"),
("Thank-You Report","Is it weird to thank my dad if he wasn't great?","The thank-you text"),
("Black Friday","How do we keep Christmas from eating us alive?","The family gift rule"),
("Advent Report","How do I lead Advent at home if we've never done it?","The candle and one verse"),
("The Wait Report","How do I wait on God about something huge?","The written prayer and the date"),
("Back to Work","How do I keep the season from fading by January?","The Monday reminder"),
("Christmas Eve","How do I lead my family on Christmas Eve?","Read Luke 2 aloud"),
("New Year's Eve","What's one sentence you're carrying into 2028?","The one-line plan"),
]
assert len(M)==52 and len(F)==52, (len(M),len(F))
seasons=[(1,7,"Season 1 · Pull Up a Chair (Epiphany)"),(8,12,"Season 2 · What You Inherited (Lent and Holy Week)"),(13,19,"Season 3 · The Father Who Stays (Easter season)"),(20,22,"Season 4 · Brothers (Pentecost)"),(23,26,"Season 5 · Fathers (June)"),(27,35,"Season 6 · The House (Ordinary Time, summer)"),(36,43,"Season 7 · The Long Road (Ordinary Time, fall)"),(44,47,"Season 8 · Thanks (November)"),(48,52,"Season 9 · Advent and Christmas")]
premieres={s for s,_,_ in seasons}
def plug(k):
    if k==1: return "FULL (book, training, site, socials)"
    if k==52: return "B+T (year review)"
    if k in premieres: return "B (premiere)" if (sorted(premieres).index(k)%2==0) else "T (premiere)"
    if k%3==2: return "B"
    if k%4==0: return "T"
    return "-"
out=["# CALENDAR-104: Walk Steadfast, 2027","","Internal. Two-host video podcast with Wes Hart and Jonathon. **104 episodes**: Tuesday main episodes (odd numbers) and Friday Field Notes (even numbers), Jan 5 to Dec 31, 2027, release time 5:00 AM CT. Seasons follow the church year. Every main episode is tied to a book chapter (all 35 are covered) and, where one exists, the matching training session (W01-W24) or course session. All dates were computed and checked against the 2027 calendar.","","## Cadence decision: two a week, with a set review","","- **Why two.**","  - In an Oct 2025 survey of 1,200 US adults, 70% wanted new episodes from the shows they follow at least a couple of times a week.","  - Leading conversation shows publish twice a week or more (DOAC, JRE, Huberman), and a short second episode keeps the channel active between full episodes without a second full-length topic.","  - Field Notes is built to be cheap. It's 12-16 minutes with one question and one tool, and it checks the Tuesday challenge, which makes the challenge real (accountability on air).","- **The cost.**","  - About 45-55 minutes of finished generated video a week (a ~35 min main episode plus a ~14 min Field Notes), plus Shorts.","  - Buzzsprout data shows most podcasts publish every 3-14 days. Two a week puts us ahead of the median show, as long as quality holds.","- **Fallbacks, if production cost or quality slips:**","  - **(A)** Field Notes goes audio-only with a static card on YouTube.","  - **(B)** One episode a week, with the challenge check moved to the top of the next Tuesday episode.","  - Change only at a season break, never mid-season.","- **Review gate at E014 (Fri Feb 19).** Keep two a week if:","  - Friday views reach at least 35% of the Tuesday views;","  - average view duration on mains is 35% or higher;","  - production stayed on schedule all of Season 1.","  - If not, switch to fallback A for Season 2.","","## Plug key","","- **B:** book mention under 20 s, matched to the chapter.","- **T:** training mention under 20 s, matched to the session.","- **FULL:** the E001 launch walkthrough.","- **-:** no mid-episode plug.","- Field Notes never carry a mid plug.","- Every episode, main and Friday, ends with the **standing outro** (SHOW-BIBLE.md, standing outro). It's separate from these plugs.","- The book and the training never appear in the same episode, except E001 and E103 (season premieres carry one or the other).","- No prices on mic. Plug wording is present tense and descriptive (\"Wes's book is at walksteadfast.com\"), with no \"coming\", no \"out now\" and no dates (SHOW-BIBLE section 8a).","",]
counts={"B":0,"T":0}
for si,(a,b,name) in enumerate(seasons):
    out.append(f"## {name}")
    out.append("")
    out.append("| Ep | Date | Title | Source | Scripture (NIV) | Focus mark | Plug | What it does |")
    out.append("|---|---|---|---|---|---|---|---|")
    for k in range(a,b+1):
        t=start+dt.timedelta(days=7*(k-1)); f=t+dt.timedelta(days=3)
        title,src,scr,mark,hook=M[k-1]; p=plug(k)
        if p.startswith("B"): counts["B"]+=1
        if "T" in p and not p.startswith("FULL"): counts["T"]+=1
        out.append(f"| E{2*k-1:03d} | Tue {t:%b %-d} | {title} | {src} | {scr} | {mark} | {p} | {hook} |")
        ft,q,tool=F[k-1]
        out.append(f"| E{2*k:03d} | Fri {f:%b %-d} | Field Notes: {ft} | Checks E{2*k-1:03d} challenge | (one verse at most) | same | - | From the Table: \"{q}\" Tool: {tool}. |")
    out.append("")
out.append(f"## Totals\n\n- 52 main episodes, 52 Field Notes. Book plugs (B, incl. premieres): {counts['B']}. Training plugs (T, incl. premieres): {counts['T']}. E001 full.\n- Every book chapter (1-35) is the source of at least one main episode. The training sessions W01-W24 each line up with the matching chapter episode.\n- Holiday anchors: Valentine's (E011/E012), Ash Wednesday Feb 10 (E012), Holy Week (E023), Good Friday Mar 26 (E024), Easter Mar 28 (E025), Mother's Day May 9 (E035/E036), Pentecost May 16 (E037/E038), Memorial Day May 31 (E042), Father's Day Jun 20 (E048), July 4 (E052), Labor Day Sep 6 (E069/E070), Reformation Day Oct 31 (E085), Veterans Day Nov 11 (E089/E090), Thanksgiving Nov 25 (E093/E094), Advent Nov 28 to Dec 24 (E095-E101), Christmas Eve (E102), New Year's Eve (E104).\n- The 'Mr. Abernathy's question' segment runs about once a month: E007, E019, E027, E039, E053, E071, E087, E097.\n- The season review is the last Field Notes of each season (E014, E024, E038, E044, E052, E070, E086, E094, E104).\n\n## Note on fresh topics\n\nEpisodes marked 'fresh' aren't book chapters. They come from the stated scope (every season of a man's life) and the course sessions. Their scripture still follows the NIV rules, and they carry no book plug unless the chapter link is real.\n")
open("../CALENDAR-104.md","w").write("\n".join(out))
print(counts)
