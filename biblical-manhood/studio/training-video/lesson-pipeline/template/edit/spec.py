"""L04 · Stop Waiting — the cut, on the narration clock (the L04 FULL master's own audio). One continuous narration.

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

# ---- open, agenda, last lesson ------------------------------------------------------------------------------
F(0.0, (0.0, "TITLE_0"), (c("It's called", 3), "TITLE_1"))
F(k(4), (k(4), "AG_0"), (c(5), "AG_1"), (c(6), "AG_2"), (c(7), "AG_3"), (c(10), "AG_4"), (c(11), "AG_5"))
P(k(12), (k(12), "LAST_0"), (c("the question", 12), "LAST_1"), (c(13), "LAST_2"), (c(14), "LAST_3"))
W(k(15), (c(15), "TUESDAY"), (c(17), None), (c(18), "QUIET"))
P(k(19), (k(19), "FIRSTT_0"), (c("Jump in", 19), "FIRSTT_1"), (c("The earlier", 19), "FIRSTT_2"))
W(k(20), (c(20), "CHAIRIN"))
# ---- the tile ------------------------------------------------------------------------------------------------
W(k(22), (c(22), "GARAGE"), (c(23), None), (c(24), "SALE"), (c(25), None))
F(k(26), (k(26), "TABLE"))
W(k("Last month", 27), (c("Last month", 27), "LAMP"))
P(k(29), (k(29), "STACK_0"), (c("Nothing's broken", 29), "STACK_1"), (c(30), "STACK_2"), (c(31), "STACK_3"))
W(k(32), (c(32), "STACKTOO"))
P(k(34), (k(34), "COUCH_0"), (c("you probably", 34), "COUCH_1"), (c(35), "COUCH_2"))
W(k(36), (c(37), "ALARM"), (c(38), None), (c(39), "CABLES"), (c(40), None))
F(k(41), (k(41), "LIST_0"), (c("The call back", 42), "LIST_1"), (c(43), "LIST_2"), (c(44), "LIST_3"))
W(k(45), (c(46), "NOTICE"), (c(47), None), (c(48), "BUSY"))
F(k(51), (k(51), "HIDE_0"), (c(52), "HIDE_1"), (c(53), "HIDE_2"))
W(k(54), (c(54), "PLAQUE"), (c(55), "EMAIL"), (c("My brother left", 56), "VOICEMAIL"), (c(58), "SIX"))
# ---- Genesis 3:9 ---------------------------------------------------------------------------------------------
F(k(60), (k(60), "GEN_0"), (c("But the Lord", 61), "GEN_1"), (c("Where are you", 61), "GEN_2"))
W(k(62))
P(k(65), (k(65), "KNEW_1"), (c(66), "KNEW_2"))
P(k(67), (k(67), "CALLED_0"), (c("Not the serpent", 67), "CALLED_1"), (c(68), "CALLED_2"), (c("The man", 68), "CALLED_3"))
W(k(69), (c(69), "INCHARGE"))
F(k(71), (k(71), "OWNQ_0"), (c("so the other", 71), "OWNQ_1"), (c(72), "OWNQ_2"))
W(k(73), (c("Where are your shoes", 73), "SHOES"), (c(74), None), (c(76), "DIRECTIONS"))
F(k(77), (k(77), "PARKED_0"), (c(78), "PARKED_1"), (c("A question", 78), "PARKED_2"))
W(k(79), (c(79), "ANSWER"))
P(k(80), (k(80), "FULLLIFE_0"), (c(81), "FULLLIFE_1"), (c("Moving would", 82), "FULLLIFE_2"), (c(84), "FULLLIFE_3"))
# ---- the nicer names ------------------------------------------------------------------------------------------
F(k(86), (k(86), "BORROW_1"), (c(87), "BORROW_2"))
F(k(88), (k(88), "N_PAT"))
W(k(89), (c(89), "GIVETIME"), (c(90), "FENCE"), (c(92), "CALENDAR"))
P(k(93), (k(93), "CAL_0"), (c(94), "CAL_1"), (c("Your sister", 94), "CAL_2"))
F(k(95), (k(95), "N_PEACE"))
W(k(96), (c(96), "STIR"), (c(97), "WAITROOM"), (c(98), None), (c(100), "NODDED"), (c(101), "XMAS"))
P(k(102), (k(102), "SINCE_0"), (c(103), "SINCE_1"), (c(104), "SINCE_2"))
F(k(105), (k(105), "SHELVED_0"), (c(106), "SHELVED_1"), (c(107), "SHELVED_2"), (c(108), "SHELVED_3"))
W(k(109), (c(112), "SPOKEUP"))
P(k(113), (k(113), "SAFE_0"), (c(114), "SAFE_1"), (c(115), "SAFE_2"))
F(k(117), (k(117), "N_HUM"))
W(k(118), (c(118), "WHOAMI"))
P(k(120), (k(120), "WHO_1"), (c(121), "WHO_2"), (c(122), "WHO_3"))
F(k(123), (k(123), "N_READY"))
W(k(124), (c(124), "MINE"), (c(125), "KAYAK"))
R(k(126), "m7899", (c(126), "REVIEWS"))
W(k(128), (c(128), "ZERO"), (c(129), None))
P(k(131), (k(131), "STUDY_0"), (c(132), "STUDY_1"), (c(133), "STUDY_2"))
W(k(134), (c(134), "BOOKS"), (c(136), None), (c(138), "LOOKING"))
F(k(139), (k(139), "ONCE_0"), (c(141), "ONCE_1"), (c("Once I find", 141), "ONCE_2"), (c(142), "ONCE_3"), (c(143), "ONCE_4"))
W(k(144), (c(144), "SECONDHALF"))
P(k(145), (k(145), "SLIP_0"), (c(146), "SLIP_1"), (c(147), "SLIP_2"))
F(k(149), (k(149), "N_FAITH_0"), (c(150), "N_FAITH_1"))
W(k(151), (c(152), "PSALMS"), (c(153), None))
P(k(154), (k(154), "NEXTSTEP_0"), (c(155), "NEXTSTEP_1"), (c(156), "NEXTSTEP_2"), (c(157), "NEXTSTEP_3"))
W(k(158), (c("The next step", 159), "PIN"), (c(160), "SIGNED"))
# ---- Joshua 18:3 -----------------------------------------------------------------------------------------------
F(k(162), (k(162), "JOSH_0"), (c(163), "JOSH_1"), (c("How long", 163), "JOSH_2"), (c("to take", 163), "JOSH_3"), (c("that the Lord", 164), "JOSH_4"))
P(k(165), (k(165), "GIVEN_0"), (c("Has given", 165), "GIVEN_1"), (c(166), "GIVEN_2"), (c("They were camped", 168), "GIVEN_3"), (c(169), "GIVEN_4"))
F(k(170), (k(170), "TEST_0"), (c(171), "TEST_1"), (c(173), "TEST_2"), (c(174), "TEST_3"))
W(k(175), (c(175), "RAIN"))
F(k(176), (k(176), "HOWLONG_0"), (c(177), "HOWLONG_1"), (c(178), "HOWLONG_2"), (c(179), "HOWLONG_3"))
W(k(180), (c(180), "ELEVEN"), (c(181), "ADAY"), (c(182), None), (c(183), "ROUND"))
# ---- the shelf ------------------------------------------------------------------------------------------------
F(k(184), (k(184), "LEARN"))
W(k(185), (c(185), "SHELF"), (c(187), None), (c(188), "KIDDO"), (c(190), None), (c(191), "BUZZ"))
F(k(192), (k(192), "INVITE_0"), (c(194), "INVITE_1"))
W(k(195), (c(195), "LAUGHED"), (c("enough", 197), "MANAGE"), (c(198), "BOSS"))
P(k(199), (k(199), "GUESS_0"), (c(200), "GUESS_1"), (c(201), "GUESS_2"), (c(202), "GUESS_3"))
W(k(203), (c(203), "WASME"))
F(k(206), (k(206), "HOLE_0"), (c("and a life", 206), "HOLE_1"), (c(208), "HOLE_2"))
W(k(209), (c(209), "BUSYTOO"))
R(k(210), "m48654", (c(210), "THATSAT"), (c(211), "SURGICAL"), src_in=0.0)
F(k(212), (k(212), "TWENTY_1"), (c(213), "TWENTY_2"))
P(k(214), (k(214), "NEEDMOVE_0"), (c(215), "NEEDMOVE_1"), (c(216), "NEEDMOVE_2"))
# ---- Curtis ---------------------------------------------------------------------------------------------------
W(k(217), (c(217), "CURTIS"))
R(k(218), "m23462", (c(218), "FLINCH"), (c(220), "BUCKET"))
W(k(222), (c(222), "COUNSELOR"), (c(223), "ROOMMATES"), (c(225), None))
P(k(225), (k(225), "SEASON_0"), (c(226), "SEASON_1"), (c("Then a travel", 226), "SEASON_2"), (c(227), "SEASON_3"))
W(k(228), (c(229), "QUITASK"), (c(230), "GUEST"))
F(k(231), (k(231), "TIREDOF_0"), (c(232), "TIREDOF_1"))
W(k(233), (c(234), "FEELREADY"), (c(236), "THURSDAY"))
R(k(238), "m17371", (c(238), "DUGOUT"))
W(k(240), (c(240), "SWEAT"))
F(k(241), (k(241), "MONDAY_0"), (c("we've got", 241), "MONDAY_1"), (c(242), "MONDAY_2"), (c(243), "MONDAY_3"))
W(k(245), (c(245), "OKAY"), (c(247), "AWFUL"), (c(248), "SHIN"), (c(249), "KEPT"))
F(k(250), (k(250), "GLAD_0"), (c(252), "GLAD_1"), (c(253), "GLAD_2"))
P(k(254), (k(254), "SHORT_0"), (c("He was short", 254), "SHORT_1"), (c(255), "SHORT_2"), (c(256), "SHORT_3"))
W(k(257), (c(257), "READYNEVER"), (c(259), "AFTER"))
F(k(261), (k(261), "LATE_0"), (c("If you feel", 261), "LATE_1"), (c(262), "LATE_2"))
F(k(263), (k(263), "LOP_0"), (c("Three years", 263), "LOP_1"), (c(266), "LOP_2"), (c(267), "LOP_3"))
W(k(268), (c(268), "MEASURE"))
# ---- James 4:17 ---------------------------------------------------------------------------------------------
F(k(269), (k(269), "JAS_0"), (c(271), "JAS_1"), (c("and doesn't", 271), "JAS_2"), (c(272), "JAS_3"))
W(k(273), (c(273), "MIDDLE"), (c(274), None), (c("If you know it", 276), "NOTCAREFUL"))
F(k(278), (k(278), "SMALL_0"), (c(279), "SMALL_1"), (c(280), "SMALL_2"), (c(281), "SMALL_3"))
W(k(282), (c(282), "CALLDOES"))
F(k(284), (k(284), "NOON_0"), (c("By about three", 284), "NOON_1"))
W(k(286), (c(287), "CUTLINE"), (c(288), "TURN"))
# ---- every kind of house --------------------------------------------------------------------------------------
W(k(289), (c(289), "NAMEDOOR"))
F(k(291), (k(291), "HOUSE_1"))
W(k(293), (c(294), "CHECKED"))
F(k(295), (k(295), "HOUSE_3"), (c(296), "HOUSE_4"))
W(k(297), (c(297), "SOMEBODY"))
F(k(298), (k(298), "HOUSE_5"))
W(k(299), (c(299), "FAIR"))
P(k(301), (k(301), "HURT_1"), (c(302), "HURT_2"), (c(303), "HURT_3"), (c(304), "HURT_4"))
F(k(305), (k(305), "HOUSE_6"))
W(k(306), (c(307), "TOMATTER"), (c(308), "MATTER"), (c(309), None), (c(310), "KNOCK"), (c(311), "STAYANS"),
  (c(312), "SEVENTIES"), (c(313), "SETCHAIRS"), (c(314), "THREEYOUNG"))
F(k(316), (k(316), "FATHER_0"), (c(317), "FATHER_1"), (c(318), "FATHER_2"))
# ---- landing -------------------------------------------------------------------------------------------------------
W(k(319), (c(319), "HOLDON"))
F(k(320), (k(320), "NICER_0"), (c(321), "NICER_1"), (c(322), "NICER_2"), (c(323), "NICER_3"))
W(k("You could find it", 324), (c("You could find it", 324), "LIGHTSOFF"))
F(k(326), (k(326), "MARKS_1"), (c(327), "MARKS_2"), (c(328), "MARKS_3"), (c(329), "MARKS_4"))
F(k(330), (k(330), "FIRSTM_0"), (c("A steadfast man", 330), "FIRSTM_1"), (c(331), "FIRSTM_2"))
W(k(332), (c(332), "GUILT"), (c(334), None), (c(335), "ONENAME"))
P(k(337), (k(337), "NEWYOU_1"), (c(338), "NEWYOU_2"))
W(k(339), (c(339), "TILEOFF"), (c(340), "HEARD"))
# ---- the prayer ----------------------------------------------------------------------------------------------------
W(k(342), (c(347), "COURAGE"), (c(349), None))
# ---- workbook + move -------------------------------------------------------------------------------------------------
F(k(354), (k(354), "WB_0"), (c(355), "WB_1"), (c(357), "WB_2"))
F(k(358), (k(358), "Q1_1"), (c(360), "Q1_2"))
F(k(361), (k(361), "Q2_1"), (c(363), "Q2_2"))
F(k(365), (k(365), "Q3_1"), (c(367), "Q3_2"))
W(k(369), (c(369), "FLINCHNOT"), (c(370), "NOFIX"), (c(371), "HEARIT"))
F(k(373), (k(373), "MOVE_0"), (c(375), "MOVE_1"), (c(376), "MOVE_2"))
W(k(377), (c(377), "NAP"))
F(k(378), (k(378), "HAND_0"), (c(379), "HAND_1"), (c("Where are you", 379), "HAND_2"), (c(380), "HAND_3"), (c(381), "HAND_4"))
W(k(382), (c(382), "WRITEONCE"), (c(383), "MIRROR"))
F(k(384), (k(384), "NEXT_0"), (c(385), "NEXT_1"))
W(k(386), (c(386), "WALKPAST"))
_last = cues.WORDS[-1]["e"]
S.append((cues.q(_last + 0.49), "LOGO", {}))
END = cues.q(_last + 5.09)
