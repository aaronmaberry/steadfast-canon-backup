#!/usr/bin/env python3
"""Typeset the ch10 sample (and its back-of-book pages) in the 03d house style via headless Chrome."""
import re, subprocess, html
import pyphen
HY = pyphen.Pyphen(lang='en_US', left=3, right=3)
def shy(t):
    # soft hyphens in long lowercase words only (no names), so justified lines stay even
    return re.sub(r"(?<![&\w])([a-z]{7,})(?![\w;])", lambda m: HY.inserted(m.group(1), hyphen='\u00ad'), t)
from pathlib import Path
R = Path(__file__).resolve().parent.parent
S = R / "sample"; OUT = R / "build"; OUT.mkdir(exist_ok=True)
FONTS = "/workspace/print-build/fonts-psfixed"
MARK = "/workspace/biblical-manhood/book/art/opener-mark.png"

def curl(s):
    s = re.sub(r"(^|[\s(\[])\"", r"\1“", s)
    s = s.replace('"', "”")
    s = re.sub(r"(\w)'(\w)", r"\1’\2", s)
    s = re.sub(r"(^|[\s(\[“])'", r"\1‘", s)
    s = s.replace("'", "’")
    return s

def inline(s):
    s = html.escape(s, quote=False)
    s = curl(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"<i>\1</i>", s)
    return s

CSS = f"""
@font-face {{ font-family: Gara; src: url(file://{FONTS}/EBGaramond-Regular.ttf); }}
@font-face {{ font-family: Gara; font-style: italic; src: url(file://{FONTS}/EBGaramond-Italic.ttf); }}
@font-face {{ font-family: Gara; font-weight: bold; src: url(file://{FONTS}/EBGaramond-Bold.ttf); }}
@font-face {{ font-family: Libre; src: url(file://{FONTS}/LibreFranklin-Regular.ttf); }}
@font-face {{ font-family: Libre; font-weight: 500; src: url(file://{FONTS}/LibreFranklin-Medium.ttf); }}
@font-face {{ font-family: Libre; font-weight: bold; src: url(file://{FONTS}/LibreFranklin-Bold.ttf); }}
@font-face {{ font-family: Play; font-weight: bold; src: url(file://{FONTS}/PlayfairDisplay-Bold.ttf); }}
@page {{ size: 6in 9in; margin: 0.68in 0.58in 0.68in 0.72in; background: #E6DDCC; }}
@page :right {{ margin-left: 0.72in; margin-right: 0.58in;
  @bottom-left {{ content: "RUNHEAD"; font: italic 7.5pt Gara; color: #A8A49A; }}
  @bottom-right {{ content: counter(page); font: 7.5pt Gara; color: #464E58; }} }}
@page :left {{ margin-left: 0.58in; margin-right: 0.72in;
  @bottom-left {{ content: counter(page); font: 7.5pt Gara; color: #464E58; }}
  @bottom-right {{ content: "RUNHEAD"; font: italic 7.5pt Gara; color: #A8A49A; }} }}
html {{ counter-reset: page FOLIO0; -webkit-print-color-adjust: exact; print-color-adjust: exact; background: #E6DDCC; }}
body {{ margin: 0; font-family: Gara; font-size: 10.5pt; line-height: 14.4pt; color: #161C24; }}
p {{ margin: 0; text-indent: 1.2em; text-align: justify; hyphens: manual; break-inside: auto; orphans: 2; widows: 2; }}
.rule + p, .epi + p, .brk + p {{ text-indent: 0; }}
.mark {{ width: 0.42in; display: block; margin: 0.22in 0 10pt 0; }}
.chap {{ font: bold 8pt Libre; letter-spacing: 2.4pt; color: #134E4A; margin: 6pt 0 12pt 0; }}
h1 {{ font: bold 20pt/24pt Play; color: #0B1F38; margin: 0 0 6pt 0; }}
.rule {{ width: 42pt; height: 2.2pt; background: #134E4A; margin: 0 0 16pt 0; }}
.epi {{ margin: 0 0.35in 14.4pt 0.35in; font: italic 9.5pt/12.6pt Gara; color: #464E58; }}
.epi .ref {{ display: block; font: 500 7pt Libre; letter-spacing: 1.4pt; text-transform: uppercase; color: #134E4A; margin-top: 4pt; font-style: normal; }}
.brk {{ height: 28.8pt; display: flex; align-items: center; justify-content: center; break-inside: avoid; break-after: avoid; }}
.brk span {{ display: block; width: 4.2pt; height: 4.2pt; background: #134E4A; transform: rotate(45deg); }}
.backhead {{ font: bold 8pt Libre; letter-spacing: 2.4pt; color: #134E4A; margin: 0.1in 0 6pt 0; }}
h2 {{ font: 500 11pt/14pt Libre; color: #0B1F38; margin: 2pt 0 10pt 0; }}
.box {{ background: #F4EFE4; border: 0.6pt solid #C0B8A8; border-radius: 3pt; padding: 12pt 14pt 0 18pt; position: relative; margin-left: 6pt; }}
.box:before {{ content: ""; position: absolute; left: -6pt; top: -4pt; bottom: -14pt; width: 2.4pt; background: #2C2924; }}
.lab {{ font: bold 7.5pt Libre; letter-spacing: 2pt; text-transform: uppercase; color: #7A4A32; margin: 10pt 0 5pt 0; }}
.box p {{ text-indent: 0; text-align: left; font-size: 9.6pt; line-height: 12.8pt; }}
.lines {{ border-top: 0.6pt solid #C0B8A8; height: 13pt; }} .lines + .lines {{ }}
.carry {{ background: #ECE4D4; margin: 12pt -14pt 0 -18pt; padding: 1pt 14pt 12pt 18pt; }}
.carry p {{ font: italic 12pt/15pt Gara; }}
.note {{ text-align: left; margin: 0 0 5pt 0; font-size: 9.6pt; line-height: 12.6pt; padding-left: 1em; text-indent: -1em; }}
.tag {{ font: 500 6.5pt Libre; letter-spacing: 1.6pt; color: #7A4A32; text-transform: uppercase; margin-bottom: 8pt; }}
"""

def page_doc(body, runhead, folio0):
    css = CSS.replace("RUNHEAD", runhead).replace("FOLIO0", str(folio0))
    return f"<!doctype html><html lang='en-US'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"

def chapter_html(md):
    lines = md.strip().split("\n")
    title = lines[0].split(". ", 1)[1]; num = lines[0][2:].split(".")[0]
    out = [f"<img class='mark' src='file://{MARK}'>", f"<div class='chap'>CHAPTER {num}</div>", f"<h1>{inline(title)}</h1>", "<div class='rule'></div>"]
    rest = "\n".join(lines[1:])
    blocks = re.split(r"\n\s*\n", rest.strip())
    for b in blocks:
        b = b.strip()
        if b.startswith(":::epigraph"):
            body = b.split("\n")[1:-1]
            out.append(f"<div class='epi'>{inline(' '.join(body[:-1]))}<span class='ref'>{inline(body[-1])}</span></div>")
        elif b.startswith(":::break"):
            out.append("<div class='brk'><span></span></div>")
        else:
            out.append(f"<p>{shy(inline(' '.join(b.split())))}</p>")
    return title, "\n".join(out)

def yourturn_html(md):
    lines = [l for l in md.strip().split("\n")]
    head = [l for l in lines if l.startswith("## ")][0][3:]
    parts = re.findall(r"\*\*(.+?)\*\*\n\n(.+?)(?=\n\n|\Z)", md, re.S)
    o = ["<div class='tag'>Mock-up · back-of-book section</div>", "<div class='backhead'>YOUR TURN</div>", f"<h2>{inline(head)}</h2>", "<div class='box'>"]
    for lab, txt in parts:
        if lab == "Carry this":
            o.append(f"<div class='carry'><div class='lab'>{lab}</div><p>{inline(txt.strip())}</p></div>")
        else:
            o.append(f"<div class='lab'>{lab}</div><p>{inline(txt.strip())}</p><div style='height:8pt'></div>" + "<div class='lines'></div>" * 3)
    o.append("</div>")
    return "\n".join(o)

def notes_html(md):
    head = [l for l in md.split("\n") if l.startswith("## ")][0][3:]
    items = [b.strip() for b in re.split(r"\n\s*\n", md) if b.strip() and not b.startswith("#")]
    o = ["<div class='tag'>Mock-up · back-of-book section</div>", "<div class='backhead'>SCRIPTURE NOTES</div>", f"<h2>{inline(head)}</h2>"]
    for it in items: o.append(f"<p class='note'>{inline(it)}</p>")
    o.append("<p class='note' style='margin-top:12pt;color:#464E58'><i>Each note is keyed by the phrase on the page, so the chapter carries no numbers or verse boxes. The opening verse is the chapter's only word-for-word quotation (NIV, with the Biblica notice on the copyright page).</i></p>")
    return "\n".join(o)

def chrome(htmlfile, pdf):
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--allow-file-access-from-files", f"--print-to-pdf={pdf}", str(htmlfile)], check=True, capture_output=True)

title, body = chapter_html((S / "10-the-father-who-does-not-leave.SAMPLE.md").read_text())
(OUT / "ch10.html").write_text(page_doc(body, title, 64)); chrome(OUT / "ch10.html", OUT / "sample-ch10.pdf")
(OUT / "yt.html").write_text(page_doc(yourturn_html((S / "10-your-turn-back-of-book.SAMPLE.md").read_text()), "Your Turn", 0).replace("counter(page)", '""'))
chrome(OUT / "yt.html", OUT / "sample-yourturn.pdf")
(OUT / "notes.html").write_text(page_doc(notes_html((S / "10-scripture-notes.SAMPLE.md").read_text()), "Scripture Notes", 0).replace("counter(page)", '""'))
chrome(OUT / "notes.html", OUT / "sample-notes.pdf")
for f in ["sample-ch10.pdf", "sample-yourturn.pdf", "sample-notes.pdf"]:
    print(f, subprocess.run(["pdfinfo", str(OUT / f)], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])
