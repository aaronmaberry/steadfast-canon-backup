"""L12 · A Man with No Brothers — the cut, on the narration clock (the L12 master's own audio). One continuous narration.

Each shot: (start, kind, params). A shot runs until the next shot's start. Every start is a cut placed in a pause.
kinds:
  W  Wes full frame (master)                             params: bands [(t, BAND or None)]
  P  split: board text left, Wes card right               params: states [(t, PANEL)]
  F  full-frame board                                     params: states [(t, FULL)]
  R  b-roll (real stock footage)                          params: clip, label [(t, BAND or None)], src_in
Numbers are subtitle cue numbers (plan/lines.json).
"""
import cues
from cues import c
from cues import cut as k

S = []


def W(t, *bands):
    S.append((t, "W", dict(bands=list(bands))))


def P(t, *states):
    S.append((t, "P", dict(states=list(states))))


def F(t, *states):
    S.append((t, "F", dict(states=list(states))))


def R(t, clip, *label, src_in=None):
    S.append((t, "R", dict(clip=clip, label=list(label), src_in=src_in)))

# ---- write this lesson's shots here (see the SOP, step 8) ----
# No SRT came with L12: cues come from plan/align_script.py (one per script line; long lines split). Shots are written by
# SCRIPT LINE number (L009 = 9) and mapped to cue numbers here, so the spec reads against L12-SPOKEN-SCRIPT-v1-one-man.md.
import re as _re
_SL = [l.strip().replace("[beat]", "").replace("  ", " ") for l in open("/home/claude/l12/in/L12-lines.txt") if l.strip()]
_n = lambda s: _re.sub(r"[^a-z0-9]", "", s.lower().replace("’", "'"))
_Q = {}
_ci, _acc = 1, ""
for _li, _t in enumerate(_SL, 1):
    _Q[_li] = _ci
    while _ci in cues.LINES:
        _acc += _n(cues.LINES[_ci]["text"]); _ci += 1
        if _acc == _n(_t):
            _acc = ""; break
assert _acc == "" and _ci - 1 == max(cues.LINES), "script lines and cues do not line up"
Q = lambda n: _Q[n]
kk = lambda n, ph=None, sub=0: k(ph, Q(n) + sub) if ph else k(Q(n))
cc = lambda n, ph=None, sub=0: c(ph, Q(n) + sub) if ph else c(Q(n))

# ---- open, agenda, last lesson ------------------------------------------------------------------------------
F(0.0, (0.0, "TITLE_0"), (cc(3), "TITLE_1"))
F(kk(5), (kk(5), "AG_0"), (cc(6), "AG_1"), (cc(7), "AG_2"), (cc(8), "AG_3"), (cc(9), "AG_4"), (cc(10), "AG_5"), (cc(11), "AG_6"))
P(kk(12), (kk(12), "LAST_0"), (cc(13), "LAST_1"), (cc(14), "LAST_2"), (cc(15), "LAST_3"), (cc(16), "DOOR_0"), (cc(17), "DOOR_1"), (cc(18), "DOOR_2"))
P(kk(19), (kk(19), "NEWT_0"), (cc(20), "NEWT_1"), (cc(21), "NEWT_2"), (cc(22), "NEWT_3"))
# ---- the quiet after you lock up -------------------------------------------------------------------------------
W(kk(23), (cc(24), "STEADY"), (cc(26), "ANSWER"))
F(kk(27), (kk(27), "LOCK_0"), (cc(28), "LOCK_1"), (cc(29), "LOCK_2"), (cc(30), "LOCK_3"))
W(kk(31), (cc(31), "PRIVATE"), (cc(33), "ALLOWED"), (cc(34), "SHUT"), (cc(36), "YOUNG"), (cc(38), "MARRIED"), (cc(39), "SINKING"),
  (cc(41), "CLEAN"))
F(kk(44), (kk(44), "AIM_0"), (cc(45), "AIM_1"), (cc(46), "AIM_2"), (cc(47), "AIM_3"))
W(kk(48), (cc(48), "DRAFTS"), (cc(49), "BLANK"))
F(kk(51), (kk(51), "NONAME"))
# ---- four marks -------------------------------------------------------------------------------------------------
W(kk(52), (cc(52), "ONE"))
F(kk(54), (kk(54), "MARKS_0"), (cc(54, "ends the wait"), "MARKS_1"), (cc(54, "takes up"), "MARKS_2"), (cc(54, "moves before"), "MARKS_3"),
  (cc(54, "and receives", 1), "MARKS_4"))
W(kk(55), (cc(55), "POINTED"))
F(kk(56), (kk(56), "PASS_0"), (cc(57), "PASS_1"), (cc(58), "PASS_2"), (cc(59), "PASS_3"))
W(kk(60), (cc(60), "NUMBERS"), (cc(61), "ASKHIM"))
F(kk(63), (kk(63), "MOOD_0"), (cc(64), "MOOD_1"), (cc(65), "MOOD_2"), (cc(66), "RESP_0"), (cc(67), "RESP_1"), (cc(68), "RESP_2"), (cc(69), "RESP_3"))
W(kk(70), (cc(70), "PHONE"))
F(kk(71), (kk(71), "COURAGE_0"), (cc(72), "COURAGE_1"))
W(kk(73), (cc(73), "HELP"))
F(kk(74), (kk(74), "PRIZE_0"), (cc(75), "PRIZE_1"), (cc(76), "PRIZE_2"))
W(kk(77), (cc(77), "READYN"), (cc(78), "AHEAD"))
F(kk(79), (kk(79), "SILENCES_0"), (cc(80), "SILENCES_1"), (cc(81), "SILENCES_2"))
# ---- Ecclesiastes and Proverbs ----------------------------------------------------------------------------------
F(kk(82), (kk(82), "ECC_0"), (cc(83), "ECC_1"), (cc(83, "But pity", 1), "ECC_2"))
W(kk(84), (cc(84), "PROMISE"), (cc(85), "HANDC"), (cc(86), "PITY"))
R(kk(87), "m2847", (cc(87), "CALENDAR"))
F(kk(88), (kk(88), "LIKE_1"), (cc(89), "LIKE_2"), (cc(90), "LIKE_3"))
W(kk(91), (cc(91), "SCENE"))
F(kk(93), (kk(93), "SLIDE_1"), (cc(94), "SLIDE_2"), (cc(95), "SLIDE_3"))
W(kk(96), (cc(96), "ANNOUNCE"), (cc(98), "REACH"))
F(kk(99), (kk(99), "PRO_0"), (cc(100), "PRO_1"), (cc(100, "for a companion"), "PRO_2"))
W(kk(101), (cc(101), "MARK"), (cc(102), "FEET"), (cc(103), "NODS"))
F(kk(104), (kk(104), "STAY_0"), (cc(105), "STAY_1"), (cc(106), "STAY_2"))
W(kk(107), (cc(107), "SAVIOR"), (cc(109), "CANTFIND"))
F(kk(110), (kk(110), "KIND_0"), (cc(111), "KIND_1"))
W(kk(112), (cc(112), "CROWD"))
# ---- a buddy and a brother ----------------------------------------------------------------------------------------
W(kk(113), (cc(113), "BUDDY"), (cc(114), "BESIDE"))
F(kk(115), (kk(115), "LUNCH_1"), (cc(116), "LUNCH_2"), (cc(117), "LUNCH_3"))
W(kk(118), (cc(118), "KEEP"))
F(kk(120), (kk(120), "SEAT_0"), (cc(121), "SEAT_1"))
W(kk(122), (cc(122), "SOUR"))
F(kk(123), (kk(123), "ASKABOUT_1"), (cc(124), "ASKABOUT_2"), (cc(125), "ASKABOUT_3"), (cc(126), "ASKABOUT_4"))
W(kk(127), (cc(127), "TELLHIM"), (cc(129), "NEXT"))
R(kk(130), "m3804", (cc(130), "SAUCE"))
W(kk(131), (cc(131), "THREAD"), (cc(133), "KEYS"), (cc(134), "EASY"), (cc(136), "WEIGHT"), (cc(137), "GIFT"))
F(kk(139), (kk(139), "READY"))
W(kk(140), (cc(140), "FILL"), (cc(141), "CREW"), (cc(142), "CREW2"))
F(kk(143), (kk(143), "ALLIN_1"))
# ---- fine, the coat rack --------------------------------------------------------------------------------------------
W(kk(144), (cc(144), "TELLS"), (cc(146), "STRAIGHT"))
F(kk(147), (kk(147), "MANNERS"))
F(kk(148), (kk(148), "TIME_0"), (cc(149), "TIME_1"), (cc(150), "TIME_2"))
W(kk(151), (cc(151), "WEIGHTS"), (cc(153), "UNDER"), (cc(154), "DONT"), (cc(156), "TRIED"), (cc(158), "SHRINK"))
F(kk(160), (kk(160), "FAILED_0"), (cc(161), "FAILED_1"))
W(kk(162), (cc(162), "RACK"), (cc(163), "QUESTIONS"), (cc(165), "WALKED"), (cc(167), "SLEEVE"), (cc(168), "HALF"), (cc(169), "CAST"))
F(kk(171), (kk(171), "RESPECT"), (cc(172), "NODDED_1"), (cc(173), "NODDED_2"))
W(kk(174), (cc(174), "STILL"), (cc(176), "CHANCE"), (cc(178), "CLEANER"))
# ---- one man, one table, three questions ---------------------------------------------------------------------------
W(kk(179), (cc(179), "WANT"), (cc(180), "PICTURE"), (cc(181), "HUGE"), (cc(182), "BABY"))
F(kk(183), (kk(183), "SMALLER_0"), (cc(184), "SMALLER_1"), (cc(185), "SMALLER_2"), (cc(186), "SMALLER_3"), (cc(187), "SMALLER_4"))
F(kk(188), (kk(188), "FLOATS"))
W(kk(189), (cc(189), "PAYCHECK"))
F(kk(190), (kk(190), "HAPPENED_0"), (cc(191), "HAPPENED_1"), (cc(192), "HEAVY_0"), (cc(193), "HEAVY_1"), (cc(194), "HEAVY_2"), (cc(195), "HEAVY_3"),
  (cc(196), "HEAVY_4"), (cc(197), "LISTEN_0"), (cc(198), "LISTEN_1"), (cc(199), "LISTEN_2"))
F(kk(200), (kk(200), "NEXTM_0"), (cc(201), "NEXTM_1"), (cc(202), "NEXTM_2"), (cc(203), "PRAY_0"), (cc(204), "PRAY_1"), (cc(205), "PRAY_2"),
  (cc(206), "PRAY_3"))
W(kk(207), (cc(207), "WRECK"), (cc(208), "FLOOR"), (cc(210), "WEATHER"), (cc(212), "IDEAS"), (cc(213), "QUIET"), (cc(215), "HEREB"), (cc(217), "RUINED"))
F(kk(218), (kk(218), "CHAIR_0"), (cc(219), "CHAIR_1"))
# ---- Hollis ---------------------------------------------------------------------------------------------------------
W(kk(220), (cc(220), "HOLLIS"), (cc(222), "TRADE"), (cc(224), "DOORH"), (cc(225), "FRAME"))
F(kk(226), (kk(226), "WIFE_0"), (cc(228), "WIFE_1"))
W(kk(229), (cc(229), "NODDEDH"), (cc(231), "MONTHS"), (cc(232), "LINED"), (cc(233), "FENCE"), (cc(235), "CHAIRS"), (cc(236), "CROWDM"))
F(kk(238), (kk(238), "ASKH_1"), (cc(239), "ASKH_2"))
W(kk(240), (cc(240), "POT"))
R(kk(241), "m10479", (cc(241), "GARDENB"))
W(kk(244), (cc(244), "SUPPERS"), (cc(246), "SHORT"), (cc(247), "SPEECH"))
P(kk(248), (kk(248), "SOONER_1"))
W(kk(249), (cc(249), "MOVED"))
F(kk(251), (kk(251), "EXPECT_0"), (cc(252), "EXPECT_1"))
# ---- twenty years ahead ----------------------------------------------------------------------------------------------
W(kk(253), (cc(253), "KNOWS"))
F(kk(255), (kk(255), "TWENTY_0"), (cc(256), "TWENTY_1"))
W(kk(257), (cc(257), "YOUNGER"), (cc(258), "FIGURE"), (cc(259), "OLDER"), (cc(260), "OPINION"))
F(kk(262), (kk(262), "BOYS"))
F(kk(263), (kk(263), "TIM_0"), (cc(264), "TIM_1"), (cc(264, "entrust to", 1), "TIM_2"))
W(kk(265), (cc(265), "CHAIN"), (cc(267), "TITLE"), (cc(269), "JOB"), (cc(270), "UNIFORM"), (cc(271), "BACK"))
P(kk(272), (kk(272), "ONEQ_0"), (cc(273), "ONEQ_1"), (cc(274), "ONEQ_2"))
W(kk(275), (cc(275), "SPEECHP"))
F(kk(277), (kk(277), "COMPLETE"), (cc(278), "ASKS_1"), (cc(279), "ASKS_2"), (cc(280), "ASKS_3"))
W(kk(281), (cc(281), "COMEBY"), (cc(283), "CLOSER"), (cc(285), "BRING"), (cc(286), "HONORB"), (cc(287), "DRIFT"))
F(kk(289), (kk(289), "REPORT_0"), (cc(290), "REPORT_1"), (cc(291), "REPORT_2"))
W(kk(292), (cc(292), "FATHER"), (cc(294), "HOLE"))
F(kk(295), (kk(295), "THANK_0"), (cc(296), "THANK_1"))
# ---- the older man, Mack ---------------------------------------------------------------------------------------------
F(kk(297), (kk(297), "UNF_0"), (cc(298), "UNF_1"), (cc(299), "UNF_2"))
W(kk(300), (cc(300), "COUNTRY"), (cc(302), "TRUTH"))
F(kk(303), (kk(303), "TIT_0"), (cc(304), "TIT_1"), (cc(304, "In everything", 1), "TIT_2"))
W(kk(305), (cc(305), "WONT"))
P(kk(307), (kk(307), "YES_0"), (cc(308), "YES_1"), (cc(309), "YES_2"))
F(kk(310), (kk(310), "LECT_0"), (cc(311), "LECT_1"), (cc(312), "LECT_2"), (cc(313), "LECT_3"))
W(kk(314), (cc(314), "QUIETL"), (cc(315), "WISDOM"), (cc(317), "SECOND"), (cc(318), "REEL"), (cc(320), "NIGHTS"), (cc(321), "DROPPED"))
F(kk(322), (kk(322), "MISS"))
W(kk(323), (cc(323), "MACK"), (cc(324), "RETIRED"), (cc(325), "KINDM"), (cc(327), "COST"), (cc(328), "WAVE"), (cc(330), "TOLD"))
F(kk(331), (kk(331), "BEST_0"), (cc(331, "he had given"), "BEST_1"))
W(kk(332), (cc(332), "DRESS"), (cc(334), "SUPPER"), (cc(335), "WHOLEB"), (cc(336), "GIVING"), (cc(337), "AWAKE"), (cc(338), "WORTHY"))
F(kk(339), (kk(339), "SPEAK_0"), (cc(340), "SPEAK_1"))
# ---- the life you are in ---------------------------------------------------------------------------------------------
W(kk(341), (cc(341), "UPROAD"), (cc(343), "FAREND"))
W(kk(345), (cc(345), "WINS"), (cc(346), "SCAR"), (cc(347), "HIGH"), (cc(349), "SILENCE"))
F(kk(350), (kk(350), "YOUNGR_0"), (cc(351), "YOUNGR_1"), (cc(352), "YOUNGR_2"), (cc(353), "YOUNGR_3"))
W(kk(354), (cc(354), "SMOOTH"), (cc(355), "SINGLE"), (cc(357), "NEEDS"), (cc(359), "ROOF"))
W(kk(361), (cc(361), "TELLW"), (cc(363), "WISE"), (cc(365), "ENDED"), (cc(367), "DISPLAY"), (cc(368), "BURNED"))
F(kk(370), (kk(370), "DIGNITY"))
W(kk(371), (cc(371), "EASYSTOP"), (cc(373), "TALKING"), (cc(375), "MIDDLE"), (cc(377), "BEHIND"))
F(kk(378), (kk(378), "BOTHWAYS"))
W(kk(379), (cc(379), "STRONG"), (cc(381), "FULLDAY"), (cc(382), "TIGHT"))
F(kk(383), (kk(383), "TEXT_1"), (cc(384), "TEXT_2"), (cc(385), "HINT_0"), (cc(386), "HINT_1"), (cc(387), "HINT_2"))
# ---- land it -----------------------------------------------------------------------------------------------------------
F(kk(388), (kk(388), "BUILT"), (cc(389), "ONEQ2"))
W(kk(390), (cc(390), "PICKED"))
F(kk(392), (kk(392), "WB_0"), (cc(393), "WB_1"))
F(kk(394), (kk(394), "Q1_1"), (cc(396), "Q1_2"))
F(kk(398), (kk(398), "Q2_1"))
F(kk(400), (kk(400), "Q3_1"), (cc(402), "SENT_0"), (cc(403), "SENT_1"), (cc(404), "SENT_2"))
W(kk(405), (cc(405), "SETDAY"))
F(kk(406), (kk(406), "WRITE_0"), (cc(407), "WRITE_1"), (cc(408), "WRITE_2"), (cc(409), "WRITE_3"), (cc(410), "PAGE_1"), (cc(411), "PAGE_2"),
  (cc(412), "PAGE_3"))
F(kk(413), (kk(413), "ONEMOVE_0"), (cc(414), "ONEMOVE_1"))
F(kk(415), (kk(415), "MARKS2_0"), (cc(415, "ends the wait"), "MARKS2_1"), (cc(415, "takes up"), "MARKS2_2"), (cc(415, "moves before"), "MARKS2_3"),
  (cc(415, "and receives", 1), "MARKS2_4"), (cc(416), "FIRST_0"), (cc(416, "that means"), "FIRST_1"))
F(kk(417), (kk(417), "NEXT_0"), (cc(419), "NEXT_1"))
_last = cues.WORDS[-1]["e"]
S.append((cues.q(_last + 0.49), "LOGO", {}))
END = cues.q(_last + 5.09)
