#!/usr/bin/env python3
"""Session 02 full pass: small.en on original mp3 chunks, merge with existing medium.en."""
from __future__ import annotations
import json, os, re, time, sys
from pathlib import Path
from faster_whisper import WhisperModel

os.environ.setdefault("OMP_NUM_THREADS", "2")

ROOT = Path("/workspace/biblical-manhood")
CDIR = ROOT / "audio" / "02-chunks"
OUT = ROOT / "transcripts" / "02-chunks"
RAW = ROOT / "asr-raw" / "02"
TR = ROOT / "transcripts"
OUT.mkdir(parents=True, exist_ok=True)
RAW.mkdir(parents=True, exist_ok=True)

CHUNKS = [
    (0,    "c0-00m00-08m15.mp3", "s0"),
    (480,  "c1-08m00-16m15.mp3", "s1"),
    (960,  "c2-16m00-24m15.mp3", "s2"),
    (1440, "c3-24m00-32m15.mp3", "s3"),
    (1920, "c4-32m00-40m15.mp3", "s4"),
    (2400, "c5-40m00-47m50.mp3", "s5"),
]

PROMPT = "Biblical Manhood. Speaker Tim Hawks. Father wound. Richard Hawks. Ted Turner. Ephesians. Matthew. Ben."

def light_fix(t: str) -> str:
    t = (t or "").replace("\u00a0", " ").strip()
    reps = [
        ("right of passage", "rite of passage"),
        ("Ever?Clear", "Everclear"),
        ("ever clear", "Everclear"),
        ("lossness", "lostness"),
        ("ristlessness", "listlessness"),
        ("Hawkes", "Hawks"),
        ("Hawke's", "Hawks"),
        ("Hocks", "Hawks"),
        ("Convocation through modeling", "Conviction through modeling"),
        ("teen hood", "teenhood"),
        ("faithfullyly", "faithfully"),
        ("indelably", "indelibly"),
        ("college equation", "college graduation"),
        ("hisbapt", "his baptism"),
        ("father woon", "father wound"),
        ("already ordinarily", "ordinarily"),
    ]
    for a,b in reps:
        t = t.replace(a,b)
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\b(\w+)(?: \1){3,}\b", r"\1", t, flags=re.I)
    t = t.replace(" .", ".").replace(" ,", ",")
    return t.strip()

def is_junk(text, lp, cr=None):
    t = (text or "").strip()
    if not t: return True
    if re.fullmatch(r"[\s.,;:!?\-–—'\"()]+", t): return True
    letters = re.sub(r"[^A-Za-z]", "", t)
    if len(letters) <= 1: return True
    if t.count(",") > 20: return True
    toks = t.split()
    if len(toks) >= 8 and sum(1 for w in toks if len(w)==1)/len(toks) > 0.55: return True
    if lp is not None and lp < -1.8 and len(toks) <= 2: return True
    if cr is not None and cr > 2.6 and len(t) > 50: return True
    return False

def transcribe_chunk(model, offset, path, tag):
    dest = OUT / f"{tag}-small.jsonl"
    print(f"\n=== {tag} offset={offset} {path.name} ===", flush=True)
    t0 = time.time()
    segs, info = model.transcribe(
        str(path), language="en", beam_size=5,
        vad_filter=True,
        vad_parameters=dict(threshold=0.25, min_silence_duration_ms=450, speech_pad_ms=500, min_speech_duration_ms=120),
        condition_on_previous_text=False, temperature=0.0,
        no_speech_threshold=0.8, log_prob_threshold=-1.4,
        initial_prompt=PROMPT,
    )
    recs=[]
    n=0; kept=0; words=0
    with dest.open("w") as jf:
        for s in segs:
            text = light_fix(s.text or "")
            lp = float(s.avg_logprob) if s.avg_logprob is not None else None
            nsp = float(s.no_speech_prob) if s.no_speech_prob is not None else None
            cr = float(s.compression_ratio) if s.compression_ratio is not None else None
            rec = {
                "src": "small.en", "chunk": tag, "offset": offset,
                "start": round(float(s.start)+offset, 3),
                "end": round(float(s.end)+offset, 3),
                "text": text,
                "avg_logprob": round(lp,4) if lp is not None else None,
                "no_speech_prob": round(nsp,4) if nsp is not None else None,
                "compression_ratio": round(cr,4) if cr is not None else None,
            }
            rec["junk"] = is_junk(text, lp, cr)
            recs.append(rec)
            jf.write(json.dumps(rec, ensure_ascii=False)+"\n"); jf.flush()
            n+=1
            if not rec["junk"]:
                kept += 1
                words += len(text.split())
            if n % 12 == 0:
                print(f"  {tag} n={n} t={rec['start']:.0f} lp={rec['avg_logprob']} j={rec['junk']} {text[:100]}", flush=True)
    print(f"  DONE {tag} n={n} kept={kept} words={words} dur={info.duration:.0f} {time.time()-t0:.0f}s", flush=True)
    return recs

def load_jsonl(p: Path, src: str) -> list[dict]:
    if not p.exists() or p.stat().st_size < 10:
        return []
    out=[]
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        try:
            r=json.loads(line)
        except json.JSONDecodeError:
            continue
        text=light_fix(r.get("text") or "")
        lp=r.get("avg_logprob")
        rec={
            "src": src,
            "start": float(r.get("start") or 0),
            "end": float(r.get("end") or 0),
            "text": text,
            "avg_logprob": lp,
            "no_speech_prob": r.get("no_speech_prob"),
            "compression_ratio": r.get("compression_ratio"),
        }
        rec["junk"]=is_junk(text, lp, rec["compression_ratio"])
        if rec["end"] > rec["start"] and rec["end"] <= 2900:
            out.append(rec)
    return out

def merge(sources: list[list[dict]]) -> list[dict]:
    """Greedy interval merge: keep higher-quality overlapping speech."""
    items=[]
    for recs in sources:
        for r in recs:
            if r.get("junk"): continue
            if not r["text"] or len(r["text"].split())==0: continue
            items.append(r)
    items.sort(key=lambda r: (r["start"], -(len(r["text"])), r.get("avg_logprob") or -9))
    kept=[]
    for r in items:
        # if overlaps existing, keep the better one
        conflict=None
        for k in kept:
            overlap = min(r["end"], k["end"]) - max(r["start"], k["start"])
            if overlap > 0.6 * min(r["end"]-r["start"], k["end"]-k["start"], 8):
                conflict=k
                break
        if conflict is None:
            kept.append(r)
            continue
        def score(x):
            lp = x.get("avg_logprob") if x.get("avg_logprob") is not None else -1.2
            return (len(x["text"].split()) * 1.0) + (lp * 8.0)
        if score(r) > score(conflict) * 1.15:
            kept.remove(conflict)
            kept.append(r)
            kept.sort(key=lambda x: x["start"])
    kept.sort(key=lambda x: x["start"])
    # drop exact-text consecutive dups
    out=[]
    last=""
    for r in kept:
        t=r["text"].lower()
        if t==last: continue
        out.append(r); last=t
    return out

def group_paragraphs(segs, gap=1.7, max_chars=900):
    paras=[]; buf=[]; bs=None; be=None; bl=0
    for s in segs:
        t=s["text"]
        new=False
        if buf and be is not None and (s["start"]-be)>=gap: new=True
        if buf and bl>240 and buf[-1].endswith((".","?","!")) and (s["start"]-be)>=0.35: new=True
        if buf and bl+len(t)>max_chars and buf[-1].endswith((".","?","!",":")): new=True
        if new:
            paras.append((bs, " ".join(buf)))
            buf=[t]; bs=s["start"]; bl=len(t)
        else:
            if not buf: bs=s["start"]
            buf.append(t); bl += len(t)+1
        be=s["end"]
    if buf: paras.append((bs, " ".join(buf)))
    return paras

def speaker(t0, text):
    if t0 < 88: return "Host (likely Eric)"
    if 318 <= t0 < 575: return "Clip (Everclear, Father of Mine, ASR)"
    return "Tim Hawks"

def write_md(segs):
    paras=group_paragraphs(segs)
    header=[
        "# 02 Consequences of an Absent Father",
        "",
        "- Title: Biblical Manhood - 02 - Consequences of an Absent Father",
        "- Speaker: Tim Hawks (host Eric opens and closes to groups)",
        "- Date: 2025-09-19",
        "- Video: https://www.youtube.com/watch?v=LPP1coLE9i4",
        "- Source: faster-whisper small.en + medium.en merged from local audio/video. No YouTube caption track. Speech is ASR, not invented. Remaining thin stretches are left as heard.",
        "",
        "## Transcript",
        "",
    ]
    lines=[]; cur=None
    for t0, para in paras:
        sp=speaker(t0, para)
        if cur!=sp:
            lines.append(f"**{sp}:** {para}"); lines.append(""); cur=sp
        else:
            lines.append(para); lines.append("")
    text="\n".join(header+lines).rstrip()+"\n"
    text=text.replace("\u2014","-").replace("—","-")
    dest=TR/"02-consequences-of-an-absent-father.md"
    dest.write_text(text, encoding="utf-8")
    (TR/"02.txt").write_text(text, encoding="utf-8")
    def fmt(t):
        t=max(0.0,t); m=int(t//60); s=t%60; return f"{m:02d}:{s:06.3f}"
    vtt=["WEBVTT","","NOTE faster-whisper small.en+medium.en merge session 02 duration=2870s",""]
    for s in segs:
        vtt.append(f"{fmt(s['start'])} --> {fmt(s['end'])}")
        vtt.append(s["text"]); vtt.append("")
    (TR/"02.vtt").write_text("\n".join(vtt), encoding="utf-8")
    timed="\n".join(f"[{fmt(s['start'])} --> {fmt(s['end'])}] {s['text']}" for s in segs)+"\n"
    (RAW/"timed.txt").write_text(timed, encoding="utf-8")
    with (RAW/"merged.jsonl").open("w") as jf:
        for s in segs:
            jf.write(json.dumps(s, ensure_ascii=False)+"\n")
    words=len(text.split())
    print(f"WROTE {dest} words={words} paras={len(paras)} segs={len(segs)} span={segs[0]['start'] if segs else 0:.1f}->{segs[-1]['end'] if segs else 0:.1f}", flush=True)
    return words

def coverage_report(segs, dur=2870.0):
    covered=0.0
    prev=0.0
    gaps=[]
    for s in segs:
        if s["start"]>prev+6:
            gaps.append((prev, s["start"], s["start"]-prev))
        covered += max(0.0, min(s["end"],dur)-max(s["start"],prev))
        prev=max(prev,s["end"])
    if dur-prev>6:
        gaps.append((prev, dur, dur-prev))
    print(f"COVERAGE spoken_span={covered:.0f}s / {dur:.0f}s ({100*covered/dur:.1f}%) gaps>{6}s = {len(gaps)}", flush=True)
    for a,b,d in gaps:
        if d>=8:
            print(f"  GAP {a:7.1f}-{b:7.1f} ({d:.0f}s)", flush=True)

def main():
    print("Loading small.en int8 threads=2", flush=True)
    model=WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=2)
    print("loaded", flush=True)
    small=[]
    for off, fname, tag in CHUNKS:
        p=CDIR/fname
        if not p.exists():
            print("MISSING", p, file=sys.stderr); return 2
        small.extend(transcribe_chunk(model, off, p, tag))
    (OUT/"small-all.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in small)+"\n")
    med = load_jsonl(TR/"02-asr-medium.en.jsonl", "medium.en")
    mine = load_jsonl(Path("/tmp/whisper-02/mine.jsonl"), "small.en-mine")
    extra=[]
    for name in ["small-turner.jsonl","small-ben.jsonl","small-needs.jsonl","hole-1800-2870.jsonl"]:
        extra.extend(load_jsonl(OUT/name, name))
    print(f"sources small={len(small)} med={len(med)} mine={len(mine)} extra={len(extra)}", flush=True)
    merged=merge([small, med, mine, extra])
    print(f"merged kept={len(merged)} words={sum(len(r['text'].split()) for r in merged)}", flush=True)
    coverage_report(merged)
    write_md(merged)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
