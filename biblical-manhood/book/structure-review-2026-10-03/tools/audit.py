#!/usr/bin/env python3
"""Structure audit of the Steadfast Men manuscript (03d print source). Read-only."""
import re, sys, json, statistics as st
from pathlib import Path
BOOK = Path(sys.argv[1] if len(sys.argv) > 1 else "/workspace/biblical-manhood/book/_opus55-second-pass-2026-10-01/book")
FILES = ["00-introduction.md"] + sorted(p.name for p in BOOK.glob("[0-3][0-9]-*.md") if re.match(r"(0[1-9]|[12][0-9]|3[0-5])-", p.name))
BOOKS = r"(Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|Samuel|Kings|Chronicles|Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs|Ecclesiastes|Song of Songs|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|Corinthians|Galatians|Ephesians|Philippians|Colossians|Thessalonians|Timothy|Titus|Philemon|Hebrews|James|Peter|Jude|Revelation)"
REF = re.compile(BOOKS + r"\s+\d+:\d+")
# biblical voices/books/framing words that signal scripture in prose
BIBLE = re.compile(r"\b(Jesus|Christ|Paul|Moses|David|Abraham|Adam|Eve|Cain|Abel|Jacob|Esau|Joseph|Jesse|Nathan|Peter|Philip|Timothy|Solomon|Elijah|Elisha|Gideon|Nehemiah|Joshua|Noah|Isaac|Saul|Goliath|Boaz|Ruth|Jeremiah|Isaiah|Hebrews|Proverbs|Psalms?|psalm|psalmist|Scripture|scripture|the Bible|Genesis|Exodus|Deuteronomy|Ecclesiastes|Galatians|Ephesians|Colossians|Romans|Corinthians|Philippians|Luke|Matthew|James|the apostle|the prophet|Eden|Pharisees?|disciples?|parable|Jeremiah|Malachi|Micah|Job|Elkanah|Hannah|Eli|Samuel|Zacchaeus|Lazarus|Nicodemus|Mary|Martha|Barnabas|Abba)\b")
CLOSER_LABELS = ("Name it", "Do this week", "Tell a brother", "Carry this", "Be a brother")
END_HEADS = re.compile(r"^## (Before you turn the page|Before you close the book)\s*$")

def words(s): return len(re.findall(r"[A-Za-z0-9'’]+", s))
def sentences(s): return [x for x in re.split(r"(?<=[.?!])[\"”]?\s+(?=[\"“A-Z0-9])", s.strip()) if x]

rows = []
detail = {}
for f in FILES:
    t = (BOOK / f).read_text()
    lines = t.split("\n")
    # split body / before-you-turn / your-turn
    body, byt, yt = [], [], []
    zone = "body"; in_margin = False; in_notes = False
    margins = []; cur = None
    heads = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("# "): continue
        if s == ":::margin": in_margin = True; cur = []; continue
        if s == ":::notes": in_notes = True; continue
        if s == ":::" and in_margin:
            in_margin = False; margins.append((zone, cur)); continue
        if s == ":::" and in_notes: in_notes = False; continue
        if in_margin: cur.append(s); continue
        if in_notes: continue
        if END_HEADS.match(s): zone = "byt"; continue
        if s == "## Your Turn": zone = "yt"; continue
        if s.startswith("## "):
            if zone == "body": heads.append(s[3:])
            else: heads.append("[end] " + s[3:])
            continue
        {"body": body, "byt": byt, "yt": yt}[zone].append(ln)
    def paras(ls):
        out, cur2 = [], []
        for ln in ls:
            if ln.strip() in ("", "---"):
                if cur2: out.append(" ".join(cur2)); cur2 = []
            else: cur2.append(ln.strip())
        if cur2: out.append(" ".join(cur2))
        return out
    bp = paras(body)
    bp_prose = [p for p in bp if not (p.startswith("**") and p.endswith("**") and words(p) < 25)]  # creed lines kept separately
    creed_bold = len(bp) - len(bp_prose)
    bw = [words(p) for p in bp]
    sents = [len(sentences(p)) for p in bp]
    # inline scripture
    body_text = "\n".join(bp)
    inline_refs = len(REF.findall(body_text))
    # inline direct quotes of scripture: a quoted string inside a sentence that names a biblical voice/book
    inline_quotes = []
    bible_sents = 0
    bible_paras = sum(1 for p in bp if BIBLE.search(p))
    for p in bp:
        for snt in sentences(p):
            if BIBLE.search(snt):
                bible_sents += 1
                if re.search(r"\"[^\"]{3,}\"", snt) and re.search(r"\b(said|says|wrote|writes|asked|asks|told|tells|called|calls|prayed|promised|cried|answered|replied|put it|line)\b", snt):
                    inline_quotes.append(snt)
    SPEECH = re.compile(r"\b(said|says|wrote|writes|asked|asks|told|tells|called|calls|describes|described|promised|promises|put it|warns|warned|commands|teaches|taught|marveled|line he wrote|word for)\b")
    paraphrase = [x for p2 in bp for x in sentences(p2) if BIBLE.search(x) and SPEECH.search(x)]
    # verse lead-ins: the paragraph right before a margin block
    leadins = 0; after_notice = 0
    seq = []
    for ln in lines:
        seq.append(ln.strip())
    for i, s2 in enumerate(seq):
        if s2 == ":::margin":
            j = i - 1
            while j >= 0 and seq[j] == "": j -= 1
            prev = seq[j]
            last = re.split(r"(?<=[.?!:])\s+", prev)[-1]
            if re.search(r"(:$|\bsaid\b|\bsays\b|\bsay\b|\bwrote\b|\bwrites\b|\bdescribes?\b|\bpictures?\b|\bline\b|\bsentence\b|\bwords\b|\bverse\b|like this|\bthis\.$|\bhere\b|^Look|^Watch|^Start|^Notice|^Then David|\bprayed\b|\btold\b|\bnames\b|\bspoke\b|\bexplained\b|\bgives?\b|\bwhy\.$|\banswer\b|\bplainest\b|\bscale\b|\bdeadline\b|\bslide\b|\bpromise\b|\bsaid why\b)", last) or BIBLE.search(last):
                leadins += 1
    notice = len(re.findall(r"\bNotice\b", body_text))
    # parallel runs: 3+ consecutive paragraphs starting with the same first two words
    firsts = [" ".join(p2.split()[:2]).lower() for p2 in bp]
    firsts1 = [p2.split()[0].lower() if p2.split() else "" for p2 in bp]
    runs = 0; i = 0
    while i < len(bp):
        j = i
        while j + 1 < len(bp) and (firsts[j+1] == firsts[i] or (firsts1[j+1] == firsts1[i] and firsts1[i] in ("if","some","say","then","let","use","take","stay"))): j += 1
        if j - i + 1 >= 3: runs += j - i + 1; i = j + 1
        else: i += 1
    bold_body = len(re.findall(r"\*\*[^*]+\*\*", body_text))
    margin_body = [m for z, m in margins if z == "body"]
    margin_all = len(margins)
    margin_words = sum(words(" ".join(m[1:])) for z, m in margins)
    ytp = paras(yt)
    yt_labels = sum(1 for p in ytp if p.strip("*") in CLOSER_LABELS)
    bp_words = sum(bw)
    rows.append(dict(
        file=f, ch=("Intro" if f.startswith("00") else str(int(f[:2]))),
        total_words=words(t.split("## Your Turn")[0]) if "## Your Turn" in t else words(t),
        body_words=bp_words,
        margin_blocks=margin_all, margin_words=margin_words,
        inline_quotes=len(inline_quotes), inline_refs=inline_refs,
        bible_sentences=bible_sents, bible_paras=bible_paras,
        subheads=len([h for h in heads if not h.startswith("[end]")]),
        end_heads=[h for h in heads if h.startswith("[end]")],
        bold_body=bold_body, paraphrase=len(paraphrase), verse_leadins=leadins, notice=notice, parallel_run_paras=runs, bold_margin_labels=margin_all, bold_closer_labels=yt_labels,
        paragraphs=len(bp), avg_para=round(bp_words/len(bp),1) if bp else 0,
        median_para=st.median(bw) if bw else 0,
        short_paras=sum(1 for w in bw if w <= 25),
        one_sentence_paras=sum(1 for n in sents if n == 1),
        byt_words=sum(words(p) for p in paras(byt)), byt_may=len(re.findall(r"\bMay (the|He|you|God|your)\b", " ".join(paras(byt)))),
        yourturn_words=sum(words(p) for p in ytp if p.strip("*") not in CLOSER_LABELS),
        yourturn_parts=yt_labels,
        write_in_blocks=t.count(":::notes"),
        interruptions_per_1k=round((margin_all + len([h for h in heads if not h.startswith('[end]')])) / max(bp_words,1) * 1000, 1),
    ))
    detail[f] = dict(paraphrase=paraphrase, inline_quotes=inline_quotes, heads=heads, margin_refs=[m[0] for z, m in margins])

out = Path(__file__).resolve().parent.parent
json.dump(dict(rows=rows, detail=detail), open(out / "audit.json", "w"), indent=1)
# markdown table
part = {"Intro": "Front"}
for r in rows:
    c = r["ch"]
    if c == "Intro": r["part"] = "Front"
    else:
        n = int(c); r["part"] = "One" if n <= 7 else "Two" if n <= 17 else "Three" if n <= 20 else "Four" if n <= 29 else "Five"
cols = ["ch","part","body_words","margin_blocks","verse_leadins","inline_quotes","paraphrase","bible_sentences","subheads","bold_body","bold_margin_labels","bold_closer_labels","paragraphs","avg_para","median_para","short_paras","one_sentence_paras","parallel_run_paras","notice","byt_words","yourturn_words","write_in_blocks","interruptions_per_1k"]
hdr = ["Ch","Part","Body words","Verse boxes (NIV)","Set-up lines before a box","Inline quoted verse words","\"X said/wrote\" Scripture sentences","Sentences naming a Bible person/book","Subheads","Bold in prose","Bold verse labels","Bold closer labels","Paragraphs","Avg para (words)","Median para","Paras ≤25 words","One-sentence paras","Paras in list-like runs (3+)","\"Notice\" in prose","\"Before you turn\" words","Your Turn words","Write-in blocks","Boxes+subheads per 1k words"]
md = ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
for r in rows: md.append("| " + " | ".join(str(r[c]) for c in cols) + " |")
def tot(rs, label):
    s = {c: sum(r[c] for r in rs) for c in cols if isinstance(rs[0][c], (int, float)) and c not in ("avg_para","median_para","interruptions_per_1k")}
    bw = s["body_words"]; pa = s["paragraphs"]
    allw = [w for r in rs for w in []]
    return "| **" + label + "** | | " + " | ".join(
        str(round(bw / pa, 1)) if c == "avg_para" else "" if c == "median_para" else
        str(round((s["margin_blocks"] + s["subheads"]) / bw * 1000, 1)) if c == "interruptions_per_1k" else str(s[c])
        for c in cols[2:]) + " |"
md.append(tot(rows, "Whole book"))
for p in ["One","Two","Three","Four","Five"]:
    md.append(tot([r for r in rows if r["part"] == p], "Part " + p))
open(out / "AUDIT-TABLE.md", "w").write("\n".join(md) + "\n")
print("\n".join(md))
