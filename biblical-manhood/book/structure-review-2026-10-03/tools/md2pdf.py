#!/usr/bin/env python3
import re, sys, html, subprocess
from pathlib import Path
FONTS = "/workspace/print-build/fonts-psfixed"
def inl(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)\*(?!\w)", r"<i>\1</i>", s)
    return s
def conv(md):
    out = []; lines = md.split("\n"); i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| :]+\|$", lines[i]): rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            out.append("<table>" + "".join("<tr>" + "".join(f"<{'th' if k==0 else 'td'}>{inl(c)}</{'th' if k==0 else 'td'}>" for c in r) + "</tr>" for k, r in enumerate(rows)) + "</table>")
            continue
        m = re.match(r"^(#+) (.*)", l)
        if m: out.append(f"<h{len(m.group(1))}>{inl(m.group(2))}</h{len(m.group(1))}>"); i += 1; continue
        if re.match(r"^(- |\d+\. )", l):
            tag = "ol" if l[0].isdigit() else "ul"; items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i])); i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inl(x)}</li>" for x in items) + f"</{tag}>"); continue
        if l.strip(): 
            buf = [l]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |\d+\. )", lines[i]): buf.append(lines[i]); i += 1
            out.append(f"<p>{inl(' '.join(buf))}</p>"); continue
        i += 1
    return "\n".join(out)
src, dst = Path(sys.argv[1]), Path(sys.argv[2])
css = f"""@font-face{{font-family:Gara;src:url(file://{FONTS}/EBGaramond-Regular.ttf)}}@font-face{{font-family:Gara;font-weight:bold;src:url(file://{FONTS}/EBGaramond-Bold.ttf)}}@font-face{{font-family:Gara;font-style:italic;src:url(file://{FONTS}/EBGaramond-Italic.ttf)}}
@font-face{{font-family:Libre;src:url(file://{FONTS}/LibreFranklin-Regular.ttf)}}@font-face{{font-family:Libre;font-weight:bold;src:url(file://{FONTS}/LibreFranklin-Bold.ttf)}}
@page{{size:letter;margin:0.75in}} body{{font:11pt/15pt Gara;color:#161C24}} h1{{font:bold 18pt Libre;color:#0B1F38}} h2{{font:bold 12.5pt Libre;color:#134E4A;margin-top:16pt}} h3{{font:bold 11pt Libre}}
table{{border-collapse:collapse;font-size:9pt;line-height:11pt;margin:6pt 0}} td,th{{border:0.5pt solid #C0B8A8;padding:3pt 5pt;vertical-align:top}} th{{background:#F4EFE4;font-family:Libre;font-size:8pt}} code{{font-size:9pt}} li{{margin-bottom:3pt}}"""
if "--landscape" in sys.argv: css = css.replace("size:letter", "size:letter landscape").replace("font-size:9pt;line-height:11pt", "font-size:7.2pt;line-height:9pt")
h = dst.with_suffix(".html"); h.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{conv(src.read_text())}</body></html>")
subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer","--allow-file-access-from-files",f"--print-to-pdf={dst}",str(h)],check=True,capture_output=True)
h.unlink()
