# L01 SPEND (ElevenLabs research cap 12,000 credits, Aaron/Jarvis brief 2026-10-29). Balance not readable through the connector (no account/balance tool); figures are the connector's estimate, which matched the charge on every earlier run.
| time CT | call | flow / node(s) | credits | running total |
|---|---|---|---|---|
| 6:33 AM | estimate only, 4 TTS excerpt candidates (724-733 chars each), gens=1 | djb9IyAFD791Quj8YXFw | 0 | 0 |
| 6:33 AM | TTS C1 v4 WesD default / C2 v4 WesD stab0.3 [warmly] / C3 v3 WesD [warmly] / C4 v4 Roger | gens k9w1FexxeU90LLEoGGy0, O2XnM0kUgzavS5x3F4Fp, bCn9X710RdasuFEvpUdO, aLyRGRBOUZT6Ddsqqk1X | 2,913.81 | 2,913.81 |
| 6:39 AM | Voice Changer eleven_multilingual_sts_v2, Wes D krjoGt4x3CttlxSuoDYW, gens=1, input C2 prepped src_0.88_16.wav (asset 2n6zCfuHI0uAL9PwMtLA, 54.8 s) | node COCwWdKUqshr3G5ObK1B gen 6rQhMt9NJYnZXjokStHl | 913.45 | 3,827.26 |
| 6:42 AM | TTS C2b repeat test (story L077-L088), same C2 settings | node pAswKx0BXbmK6AJ8sInX gen 2IweWpoiH3s13NEbhNTv | 918.94 | 4,746.20 |

Total research spend: **4,746.20 of 12,000** ElevenLabs credits. HeyGen: 0. No full-lesson pass.

## L01 full audio (Aaron OK 7:29 AM; cap 45,000)
| time CT | call | ids | credits | L01-audio total |
|---|---|---|---|---|
| 7:45 AM | TTS k01-k15 full source, eleven_v4 Wes D stab 0.3 [warmly], gens=1 each | flow XQpDRq8MDT5aAvMnNRa7, gens in L01-audio-2026-10-29/chunks/gens.json | 15,738.95 | 15,738.95 |
| 7:50 AM | TTS re-roll k03 (pitch 171.7 Hz outlier) | gen nlKnkcv0i3GSSeZH6N8R | 929.94 | 16,668.89 |
| 7:54 AM | Voice Changer ONE pass, sts_v2 Wes D defaults, gens=1, on job/src_16.wav (20:08), single file, no split | node oEE3bhfifpQNupupJlEy gen ccNHc6Ly4PoXI35jmOxg | 20,131.50 | 36,800.39 |

**L01 full audio final (8:40 AM CT): 36,800.39 credits** (TTS 16,668.89 + Voice Changer 20,131.50). Plus P2 research 4,746.20 = 41,546.59 all-in today. Under the 45k stop. No further spend. HeyGen: 0.

## L01 audio v2 (Option A, covered by Aaron's 6:06 AM full-spend authorization)
| time CT | call | ids | credits | L01-audio total |
|---|---|---|---|---|
| 8:34 AM | Voice Changer TEST, 62.7 s excerpt of fixed v2 source (join k07 + 2.5 s exercise pause) | node 9dtNxKkt4SaXLD24caGa gen 2FubbOn6tqtM1UuKRVcL | 1,044.85 | 37,845.24 |
| 8:47 AM | Voice Changer TEST 2, same 62.7 s window from v2b source (intro room tone floor) | node K4kIUbCu6tM8dUniWo7m gen ksWOmJISwIa3rsRpUmZr | 1,044.93 | 38,890.17 |
| 8:58 AM | Voice Changer TEST 3, same window from v2d source (stop-release softening) | node aLq7rB5rtKfMYFVmOCeT gen t7NdIXZizvgPwPxmWLIX | 1,044.93 | 39,935.10 |
| 9:05 AM | Voice Changer ONE full pass v2, sts_v2 Wes D defaults, gens=1, on v2/src_v2d_16.wav (20:32.9), no split | node QFCEMvaIMbscUYvIqQgE gen UvrChA8vMmVfmpWD9KnG | 20,547.22 | 60,482.32 |

**L01 audio total after v2 (9:20 AM CT): 60,482.32 credits** (v1 36,800.39 + v2 tests 3,134.71 + v2 full pass 20,547.22). Plus P2 research 4,746.20 = 65,228.52 all-in. The 45k planning cap was lifted by Aaron's 6:06 AM full-spend authorization. No third pass. HeyGen: 0. The balance could not be read; these figures are the logged credits.
| 9:59 AM | HeyGen P5 test Avatar IV 1080p 13.8 s, look b9d1bd88 | video e1b2d055cbedc00ea19a5af55c318a07 | 6 HeyGen (931->925) | |

## P5 option (b) tests — 10:29 AM CT (HeyGen test credits, under 6:06 AM authorization)
- TEST2 Avatar V, video 14d1ce860d59564e682e77957aa5c0dc, 13.8 s: balance 925 → 913 = 12 credits (~0.87/s; 20:34 projection ≈ 1,074 credits)
- TEST3 Avatar IV low + steady-head motionPrompt, video 81783c8d10edd44a6ad8b85803de99be, 13.8 s: 913 → 908 = 5 credits (~0.36–0.43/s; 20:34 projection ≈ 450–537)
- Option (b) total 17 credits (cap 15 + 6 = 21). Balance now 908.
- 10:36 AM CT: FULL render submitted as ONE job: video 4c7713cd0faf45fc7ae479dbc9ac2244, audio asset 4a99e6210b474bcea05c4b001503cfe2 (v2 −26 LUFS mp3, 1234.10 s). HeyGen accepted the length (no limit error). No pre-quote available from the API; balance before 908.
- 12:13 PM CT: FULL render 4c7713cd completed; balance 908 → 577 = 331 credits (~0.27/s), under 600 cap
- QA done; final balance 577 (full render 331 credits).

## P5 mouth-dip patches (Aaron 12:xx PM Oct 29 "if you think a patch will work do it"; cap 150 HeyGen)
- 1:31 PM CT pilot take1: 99af69cd (P19 7.16 s), cebe9863 (P12 14.76 s), c5a025ca (P11 5.8 s); balance before 577
- 1:50 PM CT pilot done: 577 -> 566 = 11 credits
- 1:52 PM CT take1 batch b297590f: 24 clips, 184 s, est ~74 credits
- 2:05 PM CT take1 batch b297590f done: 566 -> 481 = 85 credits (184 s, ~0.46/s). Patch total so far 96.
- 2:48 PM CT take2 batch 616f513f submitted (P00 P01 P05 P10 P17 P18 P21 P22, 61.5 s, est ~29 cr); prompt adds: calm natural mouth, small relaxed lip shapes, no exaggerated rounding/pursing on oo/oh, no wide smile, lips close softly in pauses. Do NOT resubmit.
- 2:57 PM CT take2c batch cbef6f56 submitted (P24 P25 P26, 37.6 s, est ~18 cr). Do NOT resubmit.
- 3:20 PM CT take2 + take2c done: 481 -> 439 = 42 credits. PATCH TOTAL 577 -> 439 = 138 credits (cap 150). No further renders.
- 4:12 PM CT P19 retake batch 6983574f (take3 still-head/calm-mouth, take4 understated-lips), est ~7 cr, cap 165. Do NOT resubmit.
- 4:24 PM CT P19 retakes done: take3 289ea397, take4 40e3923c; 439 -> 433 = 6 cr. PATCH TOTAL 144 (cap 165).
- PATCH CREDIT TOTAL (all takes): pilot 11 (577->566) + take1 batch 85 (->481) + take2/take2c 42 (->439) + P19 take3/take4 6 (->433) = 144 HeyGen credits (cap 165). Placeholder batch 8fe379b8 failed at validation, 0 credits. Balance 433.
- 5:27 PM CT P6-P8 build: 0 credits, 0 dollars (local renders only).

## L01 v4 wide-shot partial re-render (Aaron via parent 10:23 AM CT Nov 2: HeyGen authorized, tell before >250)
- 10:30 AM CT balance read 433. New look 58ea634e6acd16d69ce9b3d988f979c3 "Wes v4 burg_a wide no-hand" (burg_a lips-closed photo, raised hand replaced by mirrored right shoulder; group c48fd478…). Look creation 0 credits.
- 10:40 AM CT TEST video 39792921f4f3cb0579b5d3545f5ba4f1, Avatar IV 1080p, low, SOP motion prompt + "hands stay below frame", 13.0 s (src 132.0-145.0): 433 -> 427 = 6 credits.
- 10:50 AM CT FULL wide batch 8ac896fc90b04bc2b82c3d411c8fd1ec submitted: 17 segments (all 21 WES_FULL shots, 0.6 s handles), 365.4 s, estimate ~168 credits at 0.46/s. Do NOT resubmit.
- 10:55 AM CT batch complete, all 17 downloaded (hg_w00-w16). Balance 427 -> 306 = 121 credits actual (estimate was 168). v4 total 433 -> 306 = 127 credits. Re-checked 11:15 AM CT: 306.
