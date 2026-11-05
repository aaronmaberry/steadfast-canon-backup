"""L02 word/line timing on the narration clock (= the olive master's own audio) and cut placement helpers."""
import json, re, pathlib
P = pathlib.Path("/home/claude/l04/plan")
FPS = 25
WORDS = json.load(open(P / "words.json"))
LINES = {l["n"]: l for l in json.load(open(P / "lines.json"))}
AUDIO_END = 1287.88


def norm(s):
    return re.sub(r"[^a-z0-9']", "", s.lower().replace("’", "'"))


TOK = [norm(w["w"]) for w in WORDS]


def q(t):
    return round(t * FPS) / FPS


def line_word(n):
    a = LINES[n]["a"]
    i = min(range(len(WORDS)), key=lambda k: abs(WORDS[k]["s"] - a))
    return i


def find(phrase, n):
    """index of the first word of `phrase` inside script line n"""
    toks = [norm(x) for x in phrase.split()]
    a, b = LINES[n]["a"] - 0.6, LINES[n]["b"] + 0.6
    for i in range(len(WORDS) - len(toks) + 1):
        if a <= WORDS[i]["s"] <= b and TOK[i:i + len(toks)] == toks:
            return i
    raise KeyError(f"phrase {phrase!r} not found in line {n}: {LINES[n]['text']}")


def c(phrase, n=None):
    """time a build lands: 0.10 s before the cue word starts"""
    if n is None:
        phrase, n = None, phrase
    i = line_word(n) if phrase is None else find(phrase, n)
    return q(WORDS[i]["s"] - 0.10)


def cut(phrase, n=None):
    """frame-exact cut in the pause before the cue word (middle of the gap, never closer than 0.10 s to the word)"""
    if n is None:
        phrase, n = None, phrase
    i = line_word(n) if phrase is None else find(phrase, n)
    s = WORDS[i]["s"]
    pe = WORDS[i - 1]["e"] if i > 0 else 0.0
    t = (pe + s) / 2 if s - pe > 0.2 else s - 0.10
    return q(min(t, s - 0.10))


def words_between(a, b):
    return [w["w"] for w in WORDS if a <= w["s"] < b]
