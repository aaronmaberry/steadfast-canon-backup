
# =====================================================================================================
# Lesson 12 · A Man with No Brothers — boards. Every word on screen is Wes's own words (or a plain label).
# =====================================================================================================
A = "&#8217;"   # apostrophe


def stack(name, kick, items, n, size=60, top=260, kind="full", mt=28):
    body = kicker(kick) + '<div style="margin-top:26px">' + "".join(
        line(r, i, n, size, mt, "var(--text)" if i == n - 1 else "var(--muted)", 500) for i, r in enumerate(items)) + "</div>"
    (full if kind == "full" else panel)(name, body, " ".join(items[:n]) or kick, top=top)


def stackset(prefix, kick, items, size=60, top=260, kind="full", first=0):
    for n in range(first, len(items) + 1):
        stack(f"{prefix}_{n}", kick, items, n, size, top, kind)


def say(key, text, size=96, top=290):
    full(key, h1(text, size, 0), text, top=top)


def rowset(prefix, kick, items, size=56, pad=24, top=220, num=True, first=0):
    for n in range(first, len(items) + 1):
        full(f"{prefix}_{n}", kicker(kick) + '<div style="margin-top:30px">' +
             rows_html(items, n, num=num, size=size, pad=pad, cur=n - 1 if n else None) + "</div>", items[n - 1] if n else kick, top=top)


def b(name, l1, l2=""):
    band(name, l1, l2, text=(l1 + (" " + l2 if l2 else "")).replace(A, "'"))


def verse(prefix, ref, lines, hl=()):
    for n in range(0, len(lines) + 1):
        scripture(f"{prefix}_{n}", ref, lines, n, " ".join(lines[:n]) or ref.replace("&#8211;", "-"), hl=hl)


# ---------------- title + agenda ------------------------------------------------------------------------
for n, sub_vis in enumerate([0, 1]):
    B[f"TITLE_{n}"] = (page(f"""<div class="safe">
 <div class="logo" style="position:absolute;left:0;top:0;width:250px;height:90px;opacity:.95"></div>
 <div style="position:absolute;left:0;top:300px">
  <div class="label a">Lesson 12</div>
  <div style="font-weight:600;font-size:120px;line-height:1.02;letter-spacing:-0.03em;margin-top:22px;visibility:{vis(0, sub_vis)}">A Man with No Brothers</div>
 </div>
 <div style="position:absolute;left:0;bottom:0">{progress(12)}</div></div>"""), False)
    KIND[f"TITLE_{n}"] = "FULL"; TEXT[f"TITLE_{n}"] = "Lesson 12" + (" A Man with No Brothers" if sub_vis else "")
rowset("AG", "Here" + A + "s how this goes", ["The quiet after you lock up.", "A brother beside you, and a man ahead of you.",
       "What happened, what" + A + "s heavy, what" + A + "s next.", "Hollis, and a man who notices.", "The question you bring, and the yes you can give.",
       "A name, or the honesty of no name."], 48, 16, 120)
stackset("LAST", "Last lesson was When Home Never Handed You Off", ["You were asked to put a date in your Bible, and then tell one brother where you stood with the door.",
         "Maybe you wrote the date.", "Maybe the line is still blank."], 50, 220, "panel")
stackset("DOOR", "That house never said go", ["You can walk out without making the door a weapon.", "The man you can call is another matter."], 60, 250, "panel")
stackset("NEWT", "New to this?", ["Hold to one lesson at a time.", "This lesson is the one to begin.", "Lessons before it can wait."], 60, 250, "panel")

# ---------------- the quiet after you lock up ---------------------------------------------------------------
b("STEADY", "You can look steady from where I stand.", "People know your name.")
b("ANSWER", "You answer when a need goes around.")
rowset("LOCK", "Then the day ends", ["You lock up.", "You sit a minute.", "And there" + A + "s not a man you would call and tell the truth to."], 66, 26, 240, num=False)
b("PRIVATE", "I" + A + "ve lived right there.", "I called it a private life.")
b("ALLOWED", "Private meant nobody was allowed in.")
b("SHUT", "I called the quiet peace.", "It was a shut door with a nice name on it.")
b("YOUNG", "Maybe you" + A + "re young, and you figure this arrives later,", "when the life gets bigger. It doesn" + A + "t.")
b("MARRIED", "Or maybe you" + A + "re married,", "and you figure your wife covers it.")
b("SINKING", "She loves you.", "She was never built to be the only one who knows when you" + A + "re sinking.")
b("CLEAN", "Or maybe the work went well.", "The day looked clean. You still couldn" + A + "t say who has you.")
rowset("AIM", "So here is the aim", ["Name that aloneness.", "Then make an ask.", "You go first."], 90, 26, 240, num=False)
b("DRAFTS", "Nobody drafts you off a wall because you looked ready.")
b("BLANK", "If you fell, the man you could call", "might still be a blank. Look that blank in the face before you" + A + "re done.")
say("NONAME", "A name, or the honesty of no name.", 100, 300)

# ---------------- four marks -------------------------------------------------------------------------------
b("ONE", "One sentence puts four marks on a real man.", "Here they are.")
rowset("MARKS", "A steadfast man", ["ends the wait,", "takes up what is his to carry,", "moves before he is called,",
       "and receives God" + A + "s pay, while a crowd" + A + "s approval stays out of the wage."], 64, 24, 220, num=False)
b("POINTED", "I want them pointed at the man who has you,", "and at the man you haven" + A + "t asked.")
rowset("PASS", "Passivity can look like patience", ["You wait to be chosen.", "You call the waiting humility.",
       "It" + A + "s often just fear with a calm face."], 70, 26, 240, num=False)
b("NUMBERS", "A man can hit his numbers", "and still be passive where it actually counts.")
b("ASKHIM", "Nobody at the job is going to ask him", "if he has a brother. That question is his.")
stackset("MOOD", "The ask doesn" + A + "t wait on a mood", ["The mood shows up later, after the sentence is already out.", "So you say it scared."], 70, 260)
rowset("RESP", "The ask belongs to you", ["Accept that.", "Set the time.", "Say the sentence."], 96, 26, 240, num=False)
b("PHONE", "That" + A + "s responsibility with a phone in your hand.")
stackset("COURAGE", "Courage sounds smaller than men think", ["Courage is saying the awkward thing before you feel ready."], 84, 280)
b("HELP", "And God" + A + "s pay is a life God can actually help.")
rowset("PRIZE", "Privacy can feel like a prize", ["Privacy pays you in being untouched.",
       "God" + A + "s pay is a man who can be helped, and who can turn around and help."], 66, 30, 240, num=False)
b("READYN", "If you fell, somebody" + A + "s name ought to be ready.")
b("AHEAD", "And somewhere near you is a man", "about twenty years ahead, living a stretch you" + A + "ve never asked him about.")
stackset("SILENCES", "Both of those silences are the same passivity", ["You don" + A + "t outgrow those silences by getting busier.",
         "You break them by going first."], 70, 260)

# ---------------- Ecclesiastes and Proverbs ---------------------------------------------------------------
verse("ECC", "Ecclesiastes 4:10", ["&#8220;If either of them falls down, one can help the other up.",
      "But pity anyone who falls and has no one to help them up.&#8221;"], hl=("no one to help them up",))
b("PROMISE", "Strength was never the promise", "that you wouldn" + A + "t fall.")
b("HANDC", "The promise in the verse is a hand", "close enough to get under you.")
b("PITY", "Pity, in this verse, is a warning with mercy in it.")
b("CALENDAR", "You can have a full calendar and still be that man.")
rowset("LIKE", "A full calendar", ["People like you.", "They count on you.", "None of that is a hand on the day you go down."], 70, 26, 240, num=False)
b("SCENE", "Falling doesn" + A + "t always look like a scene.", "Sometimes falling is a slow slide.")
rowset("SLIDE", "A slow slide", ["The temper.", "The secret.", "The distance at the table."], 96, 26, 240, num=False)
b("ANNOUNCE", "Most men don" + A + "t announce the slide.", "Those men just get harder to find.")
b("REACH", "A hand can still reach that slide,", "if a man is close enough to notice.")
verse("PRO", "Proverbs 13:20", ["&#8220;Walk with the wise and become wise,", "for a companion of fools suffers harm.&#8221;"], hl=("Walk with the wise",))
b("MARK", "So the man you tie yourself to", "is going to leave a mark.")
b("FEET", "Walk with a wise man", "and his counsel gets into your feet.")
b("NODS", "Walk with a man who only nods,", "and you will go farther down a bad road feeling supported.")
b("AGREE", "You can have plenty of agreement.")
stackset("STAY", "You can have plenty of agreement", ["What you" + A + "re short on is a man who loves you enough to disagree and then stay.", "That man is the brother."], 66, 250)
b("SAVIOR", "Christ stays the Savior.", "The Father stays the Father.")
b("CANTFIND", "A brother stands with you on a day you can" + A + "t find God,", "until you can hear Him again.")
rowset("KIND", "One man like that", ["Two, if God is kind."], 96, 30, 260, num=False)
b("CROWD", "You don" + A + "t need a crowd to stop living unknown.")

# ---------------- a buddy and a brother ---------------------------------------------------------------------
b("BUDDY", "A buddy is a good thing.")
b("BESIDE", "A buddy is the man beside you", "while something gets done, or while something gets enjoyed.")
rowset("LUNCH", "A buddy", ["You split a lunch.", "You loan a ladder.", "You both show up when a family needs a hand."], 70, 26, 240, num=False)
b("KEEP", "Keep those men.", "Thank God for them.")
stackset("SEAT", "A brother is a different seat", ["A brother knows what you do when a day goes sour."], 80, 280)
b("SOUR", "Whether you pick a fight, or you go polish", "a thing that was already fine, or you get real helpful and real gone.")
rowset("ASKABOUT", "A brother can ask", ["About the money.", "About the way you spoke at home.", "About the late hour.",
       "About whether you prayed, or just performed a prayer."], 62, 24, 220, num=False)
b("TELLHIM", "And you tell him.", "He says the hard sentence once, with love, and he doesn" + A + "t sand it down.")
b("ONCE", "He says the hard sentence once, with love,", "and he doesn" + A + "t sand it down.")
b("NEXT", "Then he shows up the next time", "like the sentence didn" + A + "t end you.")
b("SAUCE", "I" + A + "ve been very known on the subject of sauce.")
b("THREAD", "My text thread can settle the sauce.", "The thread can" + A + "t settle me.")
b("KEYS", "I" + A + "d come in the door, set my keys down the same way,", "and my wife could read the whole day off that sound.")
b("EASY", "I called it being easy.", "Low maintenance.")
b("WEIGHT", "What it was, my wife was carrying the weight", "of being the only person who knew me.")
b("GIFT", "She is a gift.", "That weight was never supposed to be her whole assignment.")
say("READY", "If you went down, is a man" + A + "s name ready?", 100, 300)
b("FILL", "Your wife doesn" + A + "t fill this blank.")
b("CREW", "The men at your work can respect you", "and never hear what you" + A + "re afraid of.")
b("CREW2", "A good crew is still a gift.")
stackset("ALLIN", "You need one man", ["One man who is allowed all the way in."], 90, 290)

# ---------------- fine, the coat rack -----------------------------------------------------------------------
b("TELLS", "Here is what a man tells himself.", "He says he is fine.")
b("STRAIGHT", "I" + A + "ve said it with a straight face", "on days I wasn" + A + "t fine.")
say("MANNERS", "Fine is pride that learned manners.", 110, 300)
rowset("TIME", "A man says there" + A + "s no time", ["There" + A + "s time.",
       "What there hasn" + A + "t been is an ask small enough to fit inside a real life."], 70, 30, 240, num=False)
b("WEIGHTS", "A man says he doesn" + A + "t want to be a weight.", "Under that, you may have learned early that needing somebody cost extra.")
b("EXTRA", "Under that, you may have learned early", "that needing somebody cost extra.")
b("UNDER", "So you would rather go under than reach.")
b("DONT", "A man says men don" + A + "t do this.", "Men did this long before a sealed-up life was treated as the mature one.")
b("TRIED", "Or maybe you tried.", "You opened your chest and a man used what he heard.")
b("SHRINK", "I" + A + "m not going to shrink that.", "That wound is real.")
b("RUN", "The wound can still try to run you.")
stackset("FAILED", "The wound can still try to run you", ["One man who failed you doesn" + A + "t get to lock the rest of your years."], 76, 280)
b("RACK", "There was a man at our church, older than me,", "always by the coat rack once people had gone.")
b("QUESTIONS", "I had questions.", "How a house stays kind when the money gets thin.")
b("WALKED", "I walked past that man for a long time.", "I told myself he looked busy.")
b("SLEEVE", "He was putting an arm through a sleeve.")
b("HALF", "That" + A + "s a man with half a minute", "and nowhere he had to be yet.")
b("CAST", "I had that man cast as too important to bother.", "He was waiting on a jacket.")
say("RESPECT", "The fear dressed itself up as respect.", 100, 300)
rowset("NODDED", "The fear dressed itself up as respect", ["I nodded.", "I left."], 110, 30, 260, num=False)
b("STILL", "I still think about that sleeve.", "I walked by as if that man were scenery.")
b("CHANCE", "He might have said no.", "I never gave him the chance.")
b("CLEANER", "A no would" + A + "ve been cleaner", "than another stretch of guessing on my own.")

# ---------------- one man, one table, three questions -------------------------------------------------------
b("WANT", "Most men I know already want a brother.")
b("PICTURE", "What those men don" + A + "t have is a picture", "small enough to survive the life they live.")
b("HUGE", "The pictures handed to them are huge.")
b("BABY", "A man with a baby in the house,", "or a stretch where the work is eating him, looks at those pictures and does nothing.")
rowset("SMALLER", "So take a smaller picture", ["One man.", "One table.", "One honest question.", "Kept, not crammed."], 84, 22, 220, num=False)
say("FLOATS", "A plan that floats is a plan that dies.", 100, 300)
b("PAYCHECK", "Pick a man you can tell the whole truth,", "with no paycheck between you.")
rowset("Q3", "One table", ["What happened.", "What" + A + "s heavy.", "What" + A + "s next."], 100, 26, 240, num=False)
stackset("HAPPENED", "What happened", ["Not a report."], 120, 300)
stackset("HEAVY", "What" + A + "s heavy", ["This is the one that earns the time.", "Name the load.", "Name the fear under it.", "Both of you tell the truth."],
         70, 230)
rowset("LISTEN", "The man listening has one job", ["He listens.", "Fixing can wait."], 100, 30, 260, num=False)
stackset("NEXTM", "What" + A + "s next", ["Name one move before you leave the table, out loud, so a man heard it.",
         "When you sit back down, you start with whether the move got done."], 64, 240)
rowset("PRAY", "Leave room at the end", ["Pray out loud.", "You for him.", "Him for you."], 96, 26, 240, num=False)
b("WRECK", "Some days one of the two is a wreck,", "and the heavy thing takes the whole talk.")
b("FLOOR", "That" + A + "s what the time is for.", "The floor doesn" + A + "t move.")
b("WEATHER", "Without those questions, two men will talk weather", "until the clock dies and nobody was known. I learned that by failing it.")
b("FAILING", "I learned that by failing it.")
b("IDEAS", "A man started telling me what was heavy,", "and I handed him three ideas before he finished the sentence.")
b("QUIET", "He went quiet.", "I said, I just did the thing.")
stackset("HERE", "I said", ["You don" + A + "t need a plan from me.", "I" + A + "m here."], 96, 260, "panel")
b("RUINED", "I almost ruined the talk by being helpful.")
rowset("CHAIR", "Help can wait", ["A brother stays in the chair."], 100, 30, 280, num=False)

# ---------------- Hollis -------------------------------------------------------------------------------
b("HOLLIS", "I" + A + "ll call him Hollis.", "Hollis ran the meal list when a family hit a hard stretch.")
b("TRADE", "Hollis showed up in other men" + A + "s trouble", "like it was his trade. What Hollis didn" + A + "t have was a man in his own.")
b("DOORH", "At home there was a boy who had started shutting a door", "harder than the door deserved.")
b("FRAME", "Hollis would stand in the hall, hand on the frame,", "and come up empty.")
stackset("WIFE", "His wife said one sentence. Not loud.", ["I" + A + "m tired of being the only one who knows when you" + A + "re not alright."], 80, 270)
b("NODDEDH", "Hollis nodded, like she had mentioned the weather.", "She didn" + A + "t smile.")
b("MONTHS", "Hollis sat on that sentence for months.")
b("LINED", "Hollis told me later he lined up men in his head", "and talked himself out of each one.")
b("FENCE", "There was a neighbor.", "Hollis didn" + A + "t want the fence between their yards to get heavy.")
b("CHAIRS", "Then Hollis stayed late to put chairs up,", "and a quieter man was still there, rinsing the coffee pot.")
b("CROWDM", "The one who never worked a crowd.", "Hollis heard his own mouth.")
stackset("ASKH", "Hollis heard his own mouth", ["I" + A + "m trying to be a better man, and I don" + A + "t have a brother.",
         "Would you talk with me, one man to another, plain and honest, and see if it holds."], 62, 240)
b("POT", "The quieter man looked at the pot.")
b("HEREB", "You don" + A + "t need a plan from me.", "I" + A + "m here.")
b("GARDENB", "I water the garden most evenings.", "Call while I do that. Don" + A + "t build a program out of it.")
b("PROGRAM", "Don" + A + "t build a program out of it.")
b("HONORB", "The question is the honor.")
b("WHOLEB", "That was the whole assignment.")
stackset("GARDEN", "The quieter man said", ["I water the garden most evenings.", "Call while I do that.", "Don" + A + "t build a program out of it."], 76, 250, "panel")
b("SUPPERS", "The first few calls,", "Hollis reported on other people" + A + "s suppers. The quieter man let him.")
b("SHORT", "One evening Hollis said, I" + A + "m short with my boy,", "and I don" + A + "t know the next sentence.")
b("SPEECH", "The quieter man didn" + A + "t hand Hollis a speech.")
stackset("SOONER", "The quieter man said", ["Say it again next time, and tell me if you caught it sooner."], 80, 280, "panel")
b("MOVED", "Hollis told me what actually moved him.", "If Hollis didn" + A + "t call, the quieter man noticed.")
stackset("EXPECT", "Just one man, expecting Hollis", ["That" + A + "s a brother."], 120, 300)

# ---------------- twenty years ahead -------------------------------------------------------------------------
b("KNOWS", "A brother knows the stretch you" + A + "re in.", "You also need a man who has come out the other side.")
stackset("TWENTY", "About twenty years ahead of you", ["That man has already walked ground you" + A + "re just entering."], 80, 280)
b("YOUNGER", "Maybe you" + A + "re the younger man, and you wait.")
b("FIGURE", "You figure the older one is busy, or that a real man", "sorts his own mess, or that asking would admit your father never said it.")
b("OLDER", "Or maybe you" + A + "re the older man, and you wait too.")
b("OPINION", "You figure a young man doesn" + A + "t want an old opinion,", "or that your mistakes disqualified you. So you wait each other out.")
b("OUT", "So you wait each other out.")
say("BOYS", "Boys become men with nobody ahead telling them what" + A + "s coming.", 90, 290)
verse("TIM", "2 Timothy 2:2", ["&#8220;And the things you have heard me say in the presence of many witnesses",
      "entrust to reliable people who will also be qualified to teach others.&#8221;"], hl=("entrust to reliable people",))
b("CHAIN", "That chain doesn" + A + "t mend itself.", "Somebody has to open his mouth.")
b("TITLE", "Don" + A + "t lead with a big title.", "I did.")
b("JOB", "I used a word that sounded like a job.")
b("UNIFORM", "The man I asked got a look like I" + A + "d handed him a uniform", "he hadn" + A + "t agreed to wear.")
b("BACK", "I backpedaled so hard", "I nearly took the question with me.")
stackset("ONEQ", "What I meant was one real question", ["Can I ask you one thing.", "He said, ask it."], 90, 260, "panel")
b("SPEECHP", "I had practiced a whole speech.", "The man got a lot of throat and the word so.")
say("COMPLETE", "One question is a complete ask.", 110, 300)
rowset("ASKS", "One question", ["What did you quit that kept your house in one piece.", "How did you know a good offer was the wrong one.",
       "Or can I work beside you and mostly keep quiet."], 62, 28, 230, num=False)
b("COMEBY", "If the man ahead says come by, you go.", "If he says call, you call.")
b("CLOSER", "Maybe you have a man that far ahead", "you" + A + "ve never really asked. That man is closer than the excuse.")
b("BRING", "Once that man answers,", "bring a real question when you come again.")
say("HONOR", "The question is the honor.", 120, 310)
b("DRIFT", "If you only show up to hang around,", "he will drift. A man his age has had younger men nod and change nothing.")
rowset("REPORT", "Do the thing he said, at least once", ["Then go back and tell him what happened.", "That report is what earns the next talk."],
       70, 30, 250, num=False)
b("FATHER", "Don" + A + "t make the man ahead your father.", "He can give you a great deal.")
b("HOLE", "He can" + A + "t fill the particular hole your father left.")
stackset("THANK", "Thank him out loud", ["I did what you said about supper, and I stayed in the room."], 80, 280)

# ---------------- the older man, Mack ----------------------------------------------------------------------------
rowset("UNF", "Or maybe you" + A + "re the older man", ["You" + A + "re unfinished.", "Nobody graduates."], 100, 30, 260, num=False)
b("COUNTRY", "A younger man is walking", "into country you already crossed. He doesn" + A + "t need your clean record.")
b("TRUTH", "He needs the truth about where you failed,", "and the ordinary things you kept that held the house anyway.")
verse("TIT", "Titus 2:6&#8211;7", ["&#8220;Similarly, encourage the young men to be self-controlled.",
      "In everything set them an example by doing what is good.&#8221;"], hl=("set them an example",))
b("WONT", "A younger man won" + A + "t start the ask.", "You make him nervous, and he has decided you" + A + "re busy.")
stackset("YES", "Give him a yes he can take", ["I" + A + "m replacing a faucet.", "Come hold the light if you want to see how an old man learns patience."],
         70, 250, "panel")
rowset("LECT", "Then skip the lecture", ["Ask him what the work is doing to him.", "How it is at home.", "What" + A + "s heavy."], 70, 26, 240, num=False)
b("QUIETL", "Leave him a little quiet after you ask.")
b("WISDOM", "A younger man asked me if I had wisdom for him.", "I told him, give me a second.")
b("SECOND", "That second is still open.")
b("REEL", "He didn" + A + "t need my highlight reel.", "The highlight reel is how a man hides.")
b("NIGHTS", "I missed a pile of ordinary nights", "and called the missing a season.")
b("DROPPED", "His shoulders dropped when I quit performing.")
say("MISS", "Your miss is often the useful part.", 110, 300)
b("MACK", "Another man, I" + A + "ll call him Mack.")
b("RETIRED", "Mack had been the older face among the men so long", "he figured his record had retired him.")
b("KINDM", "Mack was kind.", "Mack was done offering.")
b("COST", "A younger man, new around there,", "asked Mack what the hard years at home had cost.")
b("WAVE", "Mack almost waved him off.", "Mack had the wave ready.")
b("TOLD", "Then Mack told the truth.")
stackset("BEST", "Mack said", ["He had given his best hours to the job and called it love, and the house got what was left."], 70, 270)
b("DRESS", "Mack didn" + A + "t dress it.", "The young man came back after a stretch of days.")
b("SUPPER", "The young man said he had left his phone", "in the other room for supper and stayed inside the talk.")
say("WHOLE", "That was the whole assignment.", 110, 300)
b("GIVING", "Mack told me afterward", "that he thought he was the one giving.")
b("AWAKE", "Mostly that young man", "was keeping Mack awake to his own life.")
b("WORTHY", "If your mornings have gotten quiet,", "this is a worthy way to spend them.")
stackset("SPEAK", "God keeps putting men near each other and then waiting to see who will speak", ["You can be the one."], 110, 290)

# ---------------- the life you are in -------------------------------------------------------------------------
b("UPROAD", "Look twenty years up the road.", "Living those four marks most of the time.")
b("FAREND", "You need a man still standing", "at the far end of a road like yours.")
b("WINS", "A man with only wins", "can" + A + "t take you where you need to go.")
b("SCAR", "You came for the scar", "and for the habit he kept anyway.")
b("HIGH", "If no name comes, you" + A + "re looking too high.", "That man may be the one people thank and nobody asks.")
b("SILENCE", "Your silence has been part of his life too.")
rowset("YOUNGR", "Maybe you" + A + "re young", ["Awkward is allowed.", "You" + A + "re not late.", "Say it anyway."], 96, 26, 240, num=False)
b("SMOOTH", "Waiting until you feel smooth", "is how a boy stays a boy with a paycheck.")
b("SINGLE", "Or maybe you" + A + "re single.", "Don" + A + "t store the ask until a wedding.")
b("NEEDS", "The life you have needs a brother in it.", "Ask a married man how a house is kept, before you have one.")
b("ROOF", "The men you share a roof with can be good company", "and still not know you. Add the one man.")
b("TELLW", "Or maybe you" + A + "re married.", "Tell your wife you asked.")
b("WISE", "Don" + A + "t hand her the job of being the wise man.", "She is your wife.")
b("ENDED", "If the marriage ended,", "shame is going to tell you to sit this out. Ask anyway.")
b("DISPLAY", "Go to a man who has walked through a marriage ending,", "or a long-married man who won" + A + "t put you on display.")
b("BURNED", "If you" + A + "ve been burned, hear me.", "Asking isn" + A + "t groveling.")
say("DIGNITY", "Asking is courage, not a loss of dignity.", 96, 300)
b("EASYSTOP", "Or maybe you" + A + "re older.", "Be easy to stop.")
b("TALKING", "A younger man is already", "talking himself out of you. Go toward him and give him something he can say yes to.")
b("MIDDLE", "Or maybe you" + A + "re in the middle.", "A man ahead you" + A + "ve never asked about a house that got quiet.")
b("BEHIND", "A younger man behind you", "you" + A + "ve watched and never spoken to.")
say("BOTHWAYS", "The chain needs you looking both ways.", 100, 300)
b("STRONG", "Or maybe the work has been strong.", "Ask a man who doesn" + A + "t report to you.")
b("FULLDAY", "A full day can still leave you unknown.")
b("TIGHT", "And if the season is tight,", "a short clear ask still counts.")
rowset("TEXT", "A short clear ask", ["A text that names a day and a time.", "A sentence in a doorway."], 76, 30, 250, num=False)
rowset("HINT", "A hint isn" + A + "t an ask", ["Say the actual sentence.", "Set the time before you hang up."], 84, 30, 250, num=False)

# ---------------- land it -------------------------------------------------------------------------------
say("BUILT", "You were not built to go down alone and call it strength.", 90, 290)
say("ONEQ2", "One man, one question, one honest answer, and keep coming back.", 84, 290)
b("PICKED", "I hope you" + A + "re done waiting to be picked.", "The awkward feeling means you found the right sentence.")
b("AWKWARD", "The awkward feeling means you found the right sentence.")
stackset("WB", "Turn to Lesson Twelve in the workbook", ["Speak your answers."], 90, 290)


def qn(key, k, qtext, size=88, sub=None):
    full(key + "_1", kicker(k) + h1(qtext, size, 24), qtext, top=240)
    if sub:
        full(key + "_2", kicker(k) + h1(qtext, size, 24) + '<div style="margin-top:40px">' +
             "".join(line(s, i, len(sub), 52, 20, "var(--muted)", 400) for i, s in enumerate(sub)) + "</div>", qtext + " " + " ".join(sub), top=240)


qn("Q1", "First", "If I fell, the man I could call is blank.", 100, ["Say the blank, or say the name.", "Your wife doesn" + A + "t fill the blank."])
qn("Q2", "Second", "Who is the man twenty years ahead you" + A + "ve never asked, or the young man you" + A + "ve watched and never spoken to.", 66)
qn("Q3", "Third", "What is the brother sentence, and what is the one real question.", 76)
stackset("SENT", "The sentence is plain", ["I" + A + "m trying to be a better man, and I don" + A + "t have a brother.",
         "Would you sit with me, and keep at it, until it" + A + "s real?"], 70, 250)
b("SETDAY", "Set the day and the time", "before you put the phone down.")
rowset("WRITE", "One real question for the man ahead", ["Write the question.", "If you" + A + "re older, write the yes you" + A + "ll offer.",
       "A breakfast, a job beside you, or a call."], 66, 26, 240, num=False)
rowset("PAGE", "On the page", ["Put the blank on the page.", "Put the ask on the page.", "A hint stays a hint until a man hears it."], 70, 26, 240, num=False)
stackset("ONEMOVE", "So here" + A + "s your one move",
         ["Say the brother sentence to one man, or say that no name is ready, and set the day and the time before you put the phone down."], 64, 250)
rowset("MARKS2", "A steadfast man", ["ends the wait,", "takes up what is his to carry,", "moves before he is called,",
       "and receives God" + A + "s pay, while a crowd" + A + "s approval stays out of the wage."], 64, 24, 220, num=False)
stackset("FIRST", "From this lesson on", ["That means you go first."], 110, 300)

for n, sub in enumerate([0, 1]):
    B[f"NEXT_{n}"] = (page(f"""<div class="safe">
 <div style="position:absolute;left:0;top:300px;width:1600px">
  <div class="label a">Next lesson</div>
  <div style="font-weight:600;font-size:110px;line-height:1.05;letter-spacing:-0.025em;margin-top:22px">The Problem Inside.</div>
  <div style="font-weight:500;font-size:64px;line-height:1.2;color:var(--accent);margin-top:26px;visibility:{vis(0, sub)}">Go say the sentence.</div></div>
 <div style="position:absolute;left:0;bottom:0">{progress(13)}</div></div>"""), False)
    KIND[f"NEXT_{n}"] = "FULL"; TEXT[f"NEXT_{n}"] = "Next lesson The Problem Inside." + (" Go say the sentence." if sub else "")

import html as _html, re as _re
for _k in list(TEXT):
    TEXT[_k] = _html.unescape(_re.sub(r"<[^>]+>", " ", TEXT[_k])).replace("’", "'")
for _k, (_h, _a) in list(B.items()):
    if "logo-alpha.png" in _h:
        B[_k] = (_h.replace("logo-alpha.png", "logo-alpha-l02.png"), _a)
