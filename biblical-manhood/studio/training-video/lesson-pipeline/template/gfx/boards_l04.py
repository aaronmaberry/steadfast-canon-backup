
# =====================================================================================================
# Lesson 04 · Stop Waiting — boards. Every word on screen is Wes's own words (or a plain label).
# =====================================================================================================
A = "&#8217;"   # apostrophe


def stack(name, kick, items, n, size=60, top=260, kind="full", mt=28):
    """lines that build one at a time; the newest is bright, earlier ones muted"""
    body = kicker(kick) + '<div style="margin-top:26px">' + "".join(
        line(r, i, n, size, mt, "var(--text)" if i == n - 1 else "var(--muted)", 500) for i, r in enumerate(items)) + "</div>"
    (full if kind == "full" else panel)(name, body, " ".join(items[:n]) or kick, top=top)


def stackset(prefix, kick, items, size=60, top=260, kind="full", first=0):
    for n in range(first, len(items) + 1):
        stack(f"{prefix}_{n}", kick, items, n, size, top, kind)


# ---------------- title + agenda ------------------------------------------------------------------------
for n, sub_vis in enumerate([0, 1]):
    B[f"TITLE_{n}"] = (page(f"""<div class="safe">
 <div class="logo" style="position:absolute;left:0;top:0;width:250px;height:90px;opacity:.95"></div>
 <div style="position:absolute;left:0;top:300px">
  <div class="label a">Lesson 04</div>
  <div style="font-weight:600;font-size:132px;line-height:1.02;letter-spacing:-0.03em;margin-top:22px;visibility:{vis(0, sub_vis)}">Stop Waiting</div>
 </div>
 <div style="position:absolute;left:0;bottom:0">{progress(4)}</div></div>"""), False)
    KIND[f"TITLE_{n}"] = "FULL"; TEXT[f"TITLE_{n}"] = "Lesson 04" + (" Stop Waiting" if sub_vis else "")
agenda = [("A wait that quits looking like a decision", ""), ("The question God asked a man who was already found", ""),
          ("The nicer names a wait borrows", "Patience. Peace. Getting ready. Even faith."),
          ("What the people near you learn from it", "And a man who moved three years late."),
          ("One name, one small move", "And the noon you do it by.")]
for n in range(0, 6):
    full(f"AG_{n}", kicker("Here" + A + "s how this goes") + h1("What you and I will cover.", 76, 18, 30) +
         rows_html(agenda, n, size=48, aside=30, pad=18), " ".join(a + " " + b for a, b in agenda[:n]), top=60)
stackset("LAST", "Lesson Three stayed on the last mark", ["The question of who pays a man.", "The other three were left for their own hours.",
                                                          "This is the first of them."], 54, 230, "panel")
band("TUESDAY", "You met the name on a quiet Tuesday.", "Today it gets the hour.", text="You met the name on a quiet Tuesday. Today it gets the hour.")
band("QUIET", "If you did, keep it quiet.", "Don" + A + "t tell me.", text="If you did, keep it quiet. Don't tell me.")
stackset("FIRSTT", "First time through?", ["Jump in.", "The earlier lessons are not a test you failed."], 60, 250, "panel")
band("CHAIRIN", "Pull your chair in a little.", "Closer than feels natural.", text="Pull your chair in a little. Closer than feels natural.")
# ---------------- the tile -----------------------------------------------------------------------------------
band("GARAGE", "I" + A + "ve got to start with a confession", "about my garage.", text="I've got to start with a confession about my garage.")
band("SALE", "I bought it on sale,", "forty percent off.", text="I bought it on sale, forty percent off.")
full("TABLE", kicker("Nobody in my house calls it the tile anymore") + h1("My wife and I call it the table.", 110, 24),
     "My wife and I call it the table.", top=320)
band("LAMP", "Last month she set a lamp there.", "I think the lamp means I lost.", text="Last month she set a lamp there. I think the lamp means I lost.")
stackset("STACK", "That stack is a small picture", ["Nothing" + A + "s broken.", "Nothing" + A + "s lost. It" + A + "s waiting on me.",
                                                    "I" + A + "ve let it wait so long it quit looking like a decision."], 56, 230, "panel")
band("STACKTOO", "I" + A + "d bet you" + A + "ve got a stack too.", "Maybe a conversation you keep walking around.",
     text="I'd bet you've got a stack too. Maybe a conversation you keep walking around.")
stackset("COUCH", "When you hear passive", ["You probably picture a man on a couch.", "Remote on his chest. Blinds down."], 60, 250, "panel")
band("ALARM", "The man I worry about", "is up before the alarm.", text="The man I worry about is up before the alarm.")
band("CABLES", "Jumper cables in his truck,", "a tarp, and a spare everything.", text="Jumper cables in his truck, a tarp, and a spare everything.")
stackset("LIST", "A short list in his life has been waiting for years", ["The call back to the doctor.", "The apology he owes his sister.",
                                                                          "The friend who" + A + "s drinking again."], 66, 250)
band("NOTICE", "No details.", "Just notice it.", text="No details. Just notice it.")
band("BUSY", "That man is busy.", "He isn" + A + "t lazy.", text="That man is busy. He isn't lazy.")
stackset("HIDE", "Busy is the best hiding place I know", ["Nobody gets in trouble for being needed.",
                                                          "Busy gets you thanked. Busy gets you a plaque."], 66, 270)
band("PLAQUE", "I" + A + "ve never seen a plaque for the call", "a man finally makes to his brother.", text="I've never seen a plaque for the call a man finally makes to his brother.")
band("EMAIL", "I answer work email", "in about ninety seconds.", text="I answer work email in about ninety seconds.")
band("VOICEMAIL", "My brother left me a voicemail back in the spring.", "I still haven" + A + "t called him back.",
     text="My brother left me a voicemail back in the spring. I still haven't called him back.")
band("SIX", "I" + A + "ve listened to it six times.", "Six times I could have called him.", text="I've listened to it six times. Six times I could have called him.")
# ---------------- Genesis 3:9 ----------------------------------------------------------------------------------
gen = ["&#8220;But the Lord God called to the man,", "Where are you?&#8221;"]
for n in range(0, 3):
    scripture(f"GEN_{n}", "Genesis 3:9", gen, n, " ".join(gen[:n]) or "Genesis 3:9", hl=("Where are you?",))
stackset("KNEW", "God wasn" + A + "t lost", ["God knew exactly where the man was standing.", "The question wasn" + A + "t for God. It was for the man."],
         56, 240, "panel")
stackset("CALLED", "Notice who God called", ["Not the serpent.", "Not the tree.", "The man."], 72, 240, "panel")
band("INCHARGE", "God came looking for the one", "he had put in charge of that garden.", text="God came looking for the one he had put in charge of that garden.")
stackset("OWNQ", "You ask a question you already know", ["So the other person hears himself say it.", "You want the ownership."], 70, 280)
band("SHOES", "Where are your shoes?")
band("DIRECTIONS", "I" + A + "m not asking for directions.", "I" + A + "m asking them to walk over there and deal with it.",
     text="I'm not asking for directions. I'm asking them to walk over there and deal with it.")
stackset("PARKED", "That" + A + "s how God comes after a man who" + A + "s parked", ["You can argue with a lecture.", "A question, you have to answer."], 80, 280)
band("ANSWER", "Quit standing behind all the good stuff,", "and answer from where you actually are.",
     text="Quit standing behind all the good stuff, and answer from where you actually are.")
stackset("FULLLIFE", "You may be standing in a very full life", ["On one thing, you haven" + A + "t moved in years.",
                                                               "Moving would cost you something, and standing still hasn" + A + "t sent a bill yet.",
                                                               "God knows which thing. You already know it too."], 50, 220, "panel")
# ---------------- the nicer names ----------------------------------------------------------------------------------
stackset("BORROW", "The nicer names", ["Waiting hardly ever calls itself waiting.", "It borrows a better word, something that sounds good on a Sunday."], 66, 260)
def name_board(key, kick, word):
    full(key, kicker(kick) + h1(word, 150, 24), word, top=330)
name_board("N_PAT", "Most days the word is", "Patience.")
name_board("N_PEACE", "Or the word is", "Peace.")
name_board("N_HUM", "Sometimes the word is", "Humility.")
name_board("N_READY", "Sometimes the word is", "Getting ready.")
full("N_FAITH_0", kicker("Then there" + A + "s the one with the best excuse of all"), "Then there's the one with the best excuse of all", top=330)
name_board("N_FAITH_1", "Then there" + A + "s the one with the best excuse of all", "Faith.")
band("GIVETIME", "I" + A + "m giving it time.")
band("FENCE", "Sometimes that" + A + "s true.", "A fence post needs a minute to set.", text="Sometimes that's true. A fence post needs a minute to set.")
band("CALENDAR", "A lot of the time a man asks the calendar", "to do a job only he can do.", text="A lot of the time a man asks the calendar to do a job only he can do.")
stackset("CAL", "The calendar can" + A + "t apologize to your sister", ["It turns the page.", "Your sister is still sitting on the other side."], 64, 250, "panel")
band("STIR", "I don" + A + "t want to stir anything up.")
band("WAITROOM", "The house stays calm, and a little lonely,", "like a waiting room with nice magazines.",
     text="The house stays calm, and a little lonely, like a waiting room with nice magazines.")
band("NODDED", "You nodded and said,", "yeah, we should talk about that.", text="You nodded and said, yeah, we should talk about that.")
band("XMAS", "Three Christmases ago.")
stackset("SINCE", "She hasn" + A + "t brought it up since", ["It didn" + A + "t get fixed.", "She figured out where it goes when she does."], 60, 250, "panel")
stackset("SHELVED", "You call that peace", ["She calls it something else.", "Settled is peace.", "Shelved is this."], 80, 250)
band("SPOKEUP", "You spoke up once, it went bad,", "and quiet started to feel like the smart play.", text="You spoke up once, it went bad, and quiet started to feel like the smart play.")
stackset("SAFE", "I" + A + "m not going to bark at you for that", ["It kept you safe once. I get that.",
                                                              "If the danger is gone and the quiet stayed, what" + A + "s left is a habit with good manners."], 54, 230, "panel")
band("WHOAMI", "Who am I to bring it up?", "I" + A + "m not the expert.", text="Who am I to bring it up? I'm not the expert.")
stackset("WHO", "Who am I to bring it up?", ["You" + A + "re her husband. That" + A + "s who.", "You" + A + "re his dad. You" + A + "re the one who saw it.",
                                               "If you saw it, you" + A + "re already in it."], 54, 230, "panel")
band("MINE", "This one is mine.")
band("KAYAK", "I researched kayaks for about two years.")
band("REVIEWS", "Read the reviews. Watched the videos.", "Knew the weight of every model down to the ounce.",
     text="Read the reviews. Watched the videos. Knew the weight of every model down to the ounce.")
band("ZERO", "I own zero kayaks.", "I have never been more prepared to not be on a lake.", text="I own zero kayaks. I have never been more prepared to not be on a lake.")
stackset("STUDY", "A man can get really good at studying a thing he never does",
         ["Kayaks can take that. A marriage can" + A + "t.", "A kid can" + A + "t. The friend who" + A + "s drinking can" + A + "t."], 60, 250, "panel")
band("BOOKS", "I" + A + "ve known a man who read three books on being a dad", "and hasn" + A + "t asked his kid a real question since spring.",
     text="I've known a man who read three books on being a dad and hasn't asked his kid a real question since spring.")
band("LOOKING", "They" + A + "ve been looking for three years.")
stackset("ONCE", "If you" + A + "re young, or you" + A + "re single", ["Once I get the better job.", "Once I find the right girl.",
                                                                       "Once I" + A + "ve got a little money saved.", "Once I" + A + "ve got my head on straight."], 64, 230)
band("SECONDHALF", "Somehow that sentence", "never gets to the second half.", text="Somehow that sentence never gets to the second half.")
stackset("SLIP", "Nobody is coming with a permission slip", ["You started it a while ago.",
                                                              "The man you" + A + "ll be in ten years is getting built right now, on the days you keep calling practice."], 54, 230, "panel")
band("ONTHELORD", "I" + A + "m waiting on the Lord.")
band("PSALMS", "Scripture says to wait on the Lord,", "and I won" + A + "t take that from you.", text="Scripture says to wait on the Lord, and I won't take that from you.")
stackset("NEXTSTEP", "Maybe you honestly don" + A + "t know the next step", ["That" + A + "s real.", "Ask the Lord. Ask a brother.",
                                                                                  "Stay on your feet while you ask."], 62, 240, "panel")
band("PIN", "The next step is sitting right there,", "and a man pins God" + A + "s name on the delay.", text="The next step is sitting right there, and a man pins God's name on the delay.")
band("SIGNED", "That" + A + "s a heavy name to pin on something.", "God never signed it.", text="That's a heavy name to pin on something. God never signed it.")
# ---------------- Joshua 18:3 ----------------------------------------------------------------------------------
josh = ["&#8220;So Joshua said to the Israelites:", "How long will you wait before you begin", "to take possession of the land",
        "that the Lord, the God of your ancestors, has given you?&#8221;"]
for n in range(0, 5):
    scripture(f"JOSH_{n}", "Joshua 18:3", josh, n, " ".join(josh[:n]) or "Joshua 18:3", hl=("How long will you wait", "has given you"))
stackset("GIVEN", "Hear that last part", ["Has given you.", "The land was already theirs. God had done his part.",
                                           "They were camped out, waiting to feel like it.", "They were waiting on themselves."], 54, 220, "panel")
stackset("TEST", "Here" + A + "s a test. You can do it in the truck",
         ["When you say you" + A + "re waiting on God, ask whether some piece of it already has your name on it.",
          "If it does, do that piece. The piece you can see.", "Not the whole map."], 56, 230)
band("RAIN", "You can trust God for the rain", "and still put the seed in the ground.", text="You can trust God for the rain and still put the seed in the ground.")
stackset("HOWLONG", "Ask yourself Joshua" + A + "s question", ["How long.", "Not a mood. A number.", "Months. Years."], 84, 250)
band("ELEVEN", "I did this with the tile.", "Eleven months.", text="I did this with the tile. Eleven months.")
band("ADAY", "For tile.", "A thing I could have finished in a day.", text="For tile. A thing I could have finished in a day.")
band("ROUND", "Be honest.", "Rounding down is just one more way to wait.", text="Be honest. Rounding down is just one more way to wait.")
# ---------------- the shelf ------------------------------------------------------------------------------------
full("LEARN", kicker("The people near you learn your wait") + h1("Even if you never say a word about it.", 104, 24),
     "The people near you learn your wait, even if you never say a word about it.", top=320)
band("SHELF", "My daughter asked me to put a shelf up in her room.")
band("BRACKETS", "Simple job.", "Two brackets, one board.", text="Simple job. Two brackets, one board.")
band("KIDDO", "I said, Saturday, kiddo.", "I said it a few Saturdays in a row.", text="I said, Saturday, kiddo. I said it a few Saturdays in a row.")
band("BUZZ", "One morning my phone buzzes,", "middle of a meeting.", text="One morning my phone buzzes, middle of a meeting.")
inv = lambda rem: (kicker("A calendar invite, from my own kid") +
    '<div style="margin-top:36px;width:1100px;border:1px solid var(--line2);border-radius:18px;padding:44px 52px;background:rgba(255,255,255,.03)">'
    '<div class="label">Subject line</div>'
    '<div style="font-weight:600;font-size:84px;letter-spacing:-0.02em;margin-top:16px">Dad, the shelf.</div>'
    '<div style="font-weight:300;font-size:56px;color:var(--muted);margin-top:14px">Saturday, ten in the morning.</div>'
    f'<div style="visibility:{"visible" if rem else "hidden"};font-weight:500;font-size:42px;color:var(--accent);margin-top:30px">'
    'She even set a reminder, fifteen minutes before.</div></div>')
full("INVITE_0", inv(False), "Dad, the shelf. Saturday, ten in the morning.", top=200)
full("INVITE_1", inv(True), "She even set a reminder, fifteen minutes before.", top=200)
band("LAUGHED", "I laughed,", "and then I didn" + A + "t.", text="I laughed, and then I didn't.")
band("MANAGE", "Asking me wasn" + A + "t enough.", "She had to manage me.", text="Asking me wasn't enough. She had to manage me.")
band("BOSS", "She" + A + "s better at it than my boss.")
stackset("GUESS", "They start guessing about the man who won" + A + "t move", ["Is he mad?", "Is he tired?", "Does he even care about this?"], 68, 240, "panel")
band("WASME", "That man was me.", "I did care. I cared from a distance.", text="That man was me. I did care. I cared from a distance.")
stackset("HOLE", "After a while the guessing stops", ["And a life gets built around the hole where you should be.",
                                                      "Kids do it. Wives do it. Friends do it fastest."], 64, 260)
band("BUSYTOO", "A friend who can" + A + "t reach you stops trying", "and calls it being busy too.", text="A friend who can't reach you stops trying and calls it being busy too.")
band("THATSAT", "I put the shelf up that Saturday,", "ten in the morning.", text="I put the shelf up that Saturday, ten in the morning.")
band("SURGICAL", "She stood in the doorway the whole time,", "handing me screws like a surgical nurse.", text="She stood in the doorway the whole time, handing me screws like a surgical nurse.")
stackset("TWENTY", "Two brackets, one board", ["It took twenty minutes.", "Twenty minutes."], 110, 290)
stackset("NEEDMOVE", "She didn" + A + "t need a shelf that bad", ["She needed to know that when she asked, I" + A + "d move.",
                                                                   "I" + A + "d been protecting that for a month."], 58, 240, "panel")
# ---------------- Curtis -----------------------------------------------------------------------------------------
band("CURTIS", "A man I" + A + "ll call Curtis", "coached youth baseball for close to twenty years.", text="A man I'll call Curtis coached youth baseball for close to twenty years.")
band("FLINCH", "Curtis probably taught him", "to quit flinching at a fastball.", text="Curtis probably taught him to quit flinching at a fastball.")
band("BUCKET", "Good man. Honest man.", "Every practice, a bucket of balls and a thermos.", text="Good man. Honest man. Every practice, a bucket of balls and a thermos.")
band("COUNSELOR", "His wife asked if they could see a counselor.")
band("ROOMMATES", "She felt like they" + A + "d turned into roommates.", "Nice roommates.", text="She felt like they'd turned into roommates. Nice roommates.")
stackset("SEASON", "Curtis said sure, after the season", ["Then fall ball.", "Then a travel team needed a coach.", "Then spring came back."], 64, 240, "panel")
band("QUITASK", "The worst day wasn" + A + "t a fight.", "It was the day she quit asking.", text="The worst day wasn't a fight. It was the day she quit asking.")
band("GUEST", "He came home and she had moved her things", "into the guest room.", text="He came home and she had moved her things into the guest room.")
stackset("TIREDOF", "No yelling. She said", [Q("I" + A + "m tired of waiting on the season to be over.")], 96, 300)
band("FEELREADY", "He kept waiting to feel ready,", "for a morning he" + A + "d wake up knowing exactly what to say.", text="He kept waiting to feel ready, for a morning he'd wake up knowing exactly what to say.")
band("THURSDAY", "That morning never showed up.", "A Thursday did.", text="That morning never showed up. A Thursday did.")
band("DUGOUT", "He got to the field early, sat in the dugout,", "and called the counselor" + A + "s office.", text="He got to the field early, sat in the dugout, and called the counselor's office.")
band("SWEAT", "His hands were sweating so bad", "he almost dropped the phone in the dirt.", text="His hands were sweating so bad he almost dropped the phone in the dirt.")
stackset("MONDAY", "The lady said", [Q("We" + A + "ve got Monday at four."), "Curtis said, " + Q("I" + A + "ve got practice."),
                                        "Then he heard himself. " + Q("No. We" + A + "ll be there.")], 64, 240)
band("OKAY", "She didn" + A + "t cry. She didn" + A + "t hug him.", "She said okay.", text="She didn't cry. She didn't hug him. She said okay.")
band("AWFUL", "The first appointment was,", "his word, awful.", text="The first appointment was, his word, awful.")
band("SHIN", "Curtis said he" + A + "d rather take a line drive off the shin.")
band("KEPT", "They went back,", "and they kept going back.", text="They went back, and they kept going back.")
stackset("GLAD", "About a year in, she said something he wrote down", [Q("I quit waiting on you a long time ago."), Q("I" + A + "m glad you came anyway.")], 74, 260)
stackset("SHORT", "Curtis wasn" + A + "t short on love", ["He was short on the first move.", "He had been calling that shortage by a nice name.",
                                                          Q("The kids need me.")], 58, 240, "panel")
band("READYNEVER", "He waited to feel ready,", "and ready never came first.", text="He waited to feel ready, and ready never came first.")
band("AFTER", "Ready shows up after you move.", "Usually a while after.", text="Ready shows up after you move. Usually a while after.")
stackset("LATE", "Late still counted", ["If you feel late, hear that.", "Curtis made that call three years behind, and it still mattered."], 66, 260)
stackset("LOP", "The call took four minutes", ["Three years of waiting, and the move itself was four minutes on a dugout bench.",
                                                "The dread is huge. The move is small.", "Lopsided."], 62, 240)
band("MEASURE", "A man measures the dread,", "and skips the move.", text="A man measures the dread, and skips the move.")
# ---------------- James 4:17 ----------------------------------------------------------------------------------
jas = ["&#8220;If anyone, then, knows the good they ought to do", "and doesn" + A + "t do it,", "it is sin for them.&#8221;"]
for n in range(0, 4):
    scripture(f"JAS_{n}", "James 4:17", jas, n, " ".join(jas[:n]) or "James 4:17", hl=("knows the good", "it is sin for them"))
band("MIDDLE", "Hard verse.", "It takes the middle away.", text="Hard verse. It takes the middle away.")
band("NOTCAREFUL", "If you know it and you" + A + "re sitting on it, God has a word for that.", "The word isn" + A + "t careful.",
     text="If you know it and you're sitting on it, God has a word for that. The word isn't careful.")
stackset("SMALL", "Name the thing small enough that a morning could hold it", ["Your whole marriage is too big for a Thursday.",
                                                                                 "A four-minute phone call can fit.", "Find the smallest move that is still a real move."], 62, 240)
band("CALLDOES", "Finding the number doesn" + A + "t count.", "The call does.", text="Finding the number doesn't count. The call does.")
full("NOON_0", kicker("The small move") + h1("Do it before noon.", 130, 24), "Do it before noon.", top=300)
full("NOON_1", kicker("The small move") + h1("Do it before noon.", 130, 24) +
     line("By about three in the afternoon, my excuses have had all day to get dressed, and they sound responsible.", 0, 1, 48, 36, "var(--muted)"),
     "By about three in the afternoon, my excuses have had all day to get dressed, and they sound responsible.", top=270)
band("CUTLINE", "The first real move will feel like you cut in line.")
band("TURN", "You didn" + A + "t.", "You finally took your turn.", text="You didn't. You finally took your turn.")
# ---------------- every kind of house ------------------------------------------------------------------------------------
band("NAMEDOOR", "The same wait shows up in every kind of house.", "It changes its name at the door.", text="The same wait shows up in every kind of house. It changes its name at the door.")
houses = [("In a young man" + A + "s apartment,", "it" + A + "s called someday."), ("With a new baby,", "it" + A + "s called when things settle down."),
          ("With a big career,", "it" + A + "s called next quarter."), ("For the man worn out at church,", "it" + A + "s called let somebody else."),
          ("After a divorce,", "it" + A + "s called when I" + A + "m not so angry."), ("If you" + A + "re older,", "it" + A + "s called nobody asked me.")]
for n in range(1, 7):
    full(f"HOUSE_{n}", kicker("It changes its name at the door") + '<div style="margin-top:26px">' +
         rows_html(houses, n, num=False, size=44, aside=34, pad=10, cur=n - 1) + "</div>", " ".join(a + " " + b for a, b in houses[n - 1:n]), top=70)
band("CHECKED", "They won" + A + "t.", "I checked.", text="They won't. I checked.")
band("SOMEBODY", "There" + A + "s always a somebody else,", "until one day there isn" + A + "t.", text="There's always a somebody else, until one day there isn't.")
band("FAIR", "You might wait a long time", "to feel fair about it.", text="You might wait a long time to feel fair about it.")
stackset("HURT", "If you" + A + "re hurting, go slow", ["One small true thing is plenty.", "A text. A coffee.", "Frozen and healed are two different things.",
                                                        "You don" + A + "t have to thaw all at once."], 52, 220, "panel")
band("TOMATTER", "You" + A + "re waiting on somebody to invite you to matter.")
band("MATTER", "That invite is not coming.", "You still matter.", text="That invite is not coming. You still matter.")
band("KNOCK", "A younger man doesn" + A + "t know how to knock,", "so go find one.", text="A younger man doesn't know how to knock, so go find one.")
band("STAYANS", "Ask him how he" + A + "s actually doing,", "and stay for the answer.", text="Ask him how he's actually doing, and stay for the answer.")
band("SEVENTIES", "I know a man in his seventies", "who got tired of waiting to be asked.", text="I know a man in his seventies who got tired of waiting to be asked.")
band("SETCHAIRS", "He started showing up early", "to set out the chairs.", text="He started showing up early to set out the chairs.")
band("THREEYOUNG", "Within a month, three younger ones", "were showing up early too.", text="Within a month, three younger ones were showing up early too.")
band("NOTFOR", "They didn" + A + "t come for the chairs.")
stackset("FATHER", "Different houses. Same wait", ["Your Father is the only one in the house allowed to wait on you,",
                                                    "and he has been more patient than you or I deserve."], 64, 260)
# ---------------- landing ------------------------------------------------------------------------------------------
band("HOLDON", "If you hold on to one thing,", "hold on to this.", text="If you hold on to one thing, hold on to this.")
stackset("NICER", "Waiting almost always wears a nicer name", ["Patience. Peace. Humility. Getting ready.", "Even faith.",
                                                                "Under the nice name is something you already know is yours, and you haven" + A + "t touched it."], 58, 240)
band("LIGHTSOFF", "You could find it with the lights off.")
marks = ["A man who won" + A + "t let his life idle.", "A man who shoulders his own load.",
         "A man who walks into the hard thing ahead of the people he loves.", "A man content to be paid by God."]
for n in range(0, 5):
    full(f"MARKS_{n}", kicker("Four marks") + '<div style="margin-top:26px">' + rows_html(marks, n, size=54, pad=22, cur=n - 1 if n else None) + "</div>",
         " ".join(marks[:n]) or "Four marks", top=200)
stackset("FIRSTM", "Today was the first", ["A steadfast man stops waiting.", "The other three get stuck behind this one."], 80, 280)
band("GUILT", "Leave the guilt here.", "Guilt is heavy, and it doesn" + A + "t move anything.", text="Leave the guilt here. Guilt is heavy, and it doesn't move anything.")
band("ONENAME", "Walk out with one name and one move.")
stackset("NEWYOU", "Small enough to do the minute you walk out", ["You don" + A + "t need a new you.", "You need one thing you quit walking past."], 64, 250, "panel")
band("TILEOFF", "The tile comes off the table this Saturday.")
band("HEARD", "My wife has heard that before. More than once.", "So now you" + A + "ve heard it too.", text="My wife has heard that before. More than once. So now you've heard it too.")
band("COURAGE", "Give him four minutes of courage.", "On a real day, before lunch.", text="Give him four minutes of courage. On a real day, before lunch.")
# ---------------- workbook + move --------------------------------------------------------------------------------
stackset("WB", "Turn in the workbook to Lesson Four", ["Write it messy. Write it true.", "Three questions. Stop and write."], 66, 280)
def q2(key, k, qtext, follow=None):
    full(key + "_1", kicker(k) + h1(qtext, 84, 24), qtext, top=260)
    if follow:
        full(key + "_2", kicker(k) + h1(qtext, 84, 24, 0, "var(--muted)") + line(follow, 0, 1, 52, 36, "var(--text)", 500), follow, top=240)
q2("Q1", "First", "What" + A + "s the one thing you" + A + "ve been going to get to the longest?",
   "Put a number on how long. Whatever" + A + "s true, not whatever sounds better.")
q2("Q2", "Second", "Who" + A + "s guessing right now, because you won" + A + "t move?", "Say the name. Not the whole story. Just the name.")
q2("Q3", "Third", "What" + A + "s the smallest real move you can make on it before noon?", "Not the whole conversation. The first sentence. The first call.")
band("FLINCHNOT", "If a man tells you his number,", "don" + A + "t flinch.", text="If a man tells you his number, don't flinch.")
band("NOFIX", "Don" + A + "t fix it.", "Don" + A + "t top it with your own.", text="Don't fix it. Don't top it with your own.")
band("HEARIT", "He just did the hard part.", "You just have to hear it.", text="He just did the hard part. You just have to hear it.")
mv = ["Text one man the move, and ask him to check on you.", "Do it before you pull out of the parking lot."]
for n in range(0, 3):
    full(f"MOVE_{n}", kicker("So here" + A + "s your one move") + '<div style="margin-top:30px">' + rows_html(mv, n, size=60, pad=26, cur=n - 1 if n else None) + "</div>",
         " ".join(mv[:n]) or "So here's your one move", top=240)
band("NAP", "The drive home is where a good intention", "goes to take a nap.", text="The drive home is where a good intention goes to take a nap.")
hand = ["God already asked it.", "Where are you?", "He already knows.", "Answer Him on your feet."]
for n in range(0, 5):
    full(f"HAND_{n}", kicker("Copy one line in your own hand") + '<div style="margin-top:30px">' +
         "".join(line(r, i, n, 84, 14, "var(--text)" if i == n - 1 else "var(--muted)", 600) for i, r in enumerate(hand)) + "</div>",
         " ".join(hand[:n]) or "Copy one line in your own hand", top=220)
band("WRITEONCE", "Write it once.", "Put it where you" + A + "ll see it before noon.", text="Write it once. Put it where you'll see it before noon.")
band("MIRROR", "The bathroom mirror works.", "Unless your bathroom is still waiting on tile.", text="The bathroom mirror works. Unless your bathroom is still waiting on tile.")
for n, sub in enumerate([0, 1]):
    B[f"NEXT_{n}"] = (page(f"""<div class="safe">
 <div style="position:absolute;left:0;top:300px;width:1500px">
  <div class="label a">Next lesson</div>
  <div style="font-weight:600;font-size:96px;line-height:1.05;letter-spacing:-0.025em;margin-top:22px">What you carry.</div>
  <div style="font-weight:500;font-size:72px;line-height:1.2;color:var(--accent);margin-top:22px;visibility:{vis(0, sub)}">Pick Up the Weight.</div></div>
 <div style="position:absolute;left:0;bottom:0">{progress(5)}</div></div>"""), False)
    KIND[f"NEXT_{n}"] = "FULL"; TEXT[f"NEXT_{n}"] = "Next lesson What you carry." + (" Pick Up the Weight." if sub else "")
band("WALKPAST", "Quit walking past the thing with your name on it.")
band("GOMOVE", "Go make the small move.")

import html as _html, re as _re
for _k in list(TEXT):
    TEXT[_k] = _html.unescape(_re.sub(r"<[^>]+>", " ", TEXT[_k])).replace("’", "'")
for _k, (_h, _a) in list(B.items()):
    if "logo-alpha.png" in _h:
        B[_k] = (_h.replace("logo-alpha.png", "logo-alpha-l02.png"), _a)
