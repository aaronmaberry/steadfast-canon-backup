"""Delivery captions: the review-release SRT shifted +4.0 s (the silent open), in whole milliseconds (no rounding carry bug).
usage: python3 plan/captions.py in/LNN-v1.srt deliver/<SLUG>-vN      -> <stem>-en.srt and <stem>-en.vtt"""
import re, sys
src = open(sys.argv[1], encoding="utf-8-sig").read().replace("\r", ""); stem = sys.argv[2]


def sh(m):
    h, mi, s, ms = map(int, m.groups()); t = ((h * 60 + mi) * 60 + s) * 1000 + ms + 4000
    return f"{t // 3600000:02d}:{t // 60000 % 60:02d}:{t // 1000 % 60:02d},{t % 1000:03d}"


out = re.sub(r"(\d\d):(\d\d):(\d\d),(\d\d\d)", sh, src)
assert not re.search(r"\bweeks?\b", out, re.I), '"week" in captions'
open(stem + "-en.srt", "w", encoding="utf-8").write(out)
open(stem + "-en.vtt", "w", encoding="utf-8").write("WEBVTT\n\n" + re.sub(r"(\d\d:\d\d:\d\d),(\d\d\d)", r"\1.\2", out))
print(out.count("-->"), "captions ->", stem + "-en.srt/.vtt")
