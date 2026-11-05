"""Review-release subtitles -> plan/cues_srt.json [{n,a,b,text}] and plan/script.txt (one line per cue), on the narration clock.
usage: python3 plan/srt2cues.py in/LNN-v1.srt
Fails if the word "week" appears anywhere (hard rule)."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
src = open(sys.argv[1], encoding="utf-8-sig").read().replace("\r", "")
T = lambda h, m, s, ms: int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
cues = []
for blk in re.split(r"\n\s*\n", src.strip()):
    ls = blk.split("\n")
    m = re.match(r"(\d+):(\d+):(\d+),(\d+)\s*-->\s*(\d+):(\d+):(\d+),(\d+)", ls[1])
    cues.append(dict(n=int(ls[0]), a=round(T(*m.groups()[:4]), 3), b=round(T(*m.groups()[4:]), 3), text=" ".join(x.strip() for x in ls[2:])))
assert [c["n"] for c in cues] == list(range(1, len(cues) + 1)), "cue numbers are not 1..N"
bad = [c["n"] for c in cues if re.search(r"\bweeks?\b", c["text"], re.I)]
assert not bad, f'"week" in cues {bad}: stop and tell Aaron'
json.dump(cues, open(ROOT / "plan/cues_srt.json", "w"))
open(ROOT / "plan/script.txt", "w").write("".join(f'{c["n"]:3d} {c["a"]:8.2f} {c["text"]}\n' for c in cues))
print(len(cues), "cues; last ends", cues[-1]["b"])
