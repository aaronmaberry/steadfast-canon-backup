"""Lesson 03 · The Four Marks — boards, panels and lower bands, in the intro's design system (render.py).

Families build one row at a time; unrevealed rows are laid out but hidden, so nothing shifts when a row lands.
FULL  = full-frame field board (1920x1080, opaque)
PANEL = text for the split layout, left side only, transparent (Wes card is composited on the right)
BAND  = one or two lines over the faded bottom of a full-frame Wes shot, transparent
Every word on screen is something Wes says, or a plain label. The word "week" never appears.
"""
import importlib.util, pathlib, sys
from playwright.sync_api import sync_playwright

G = pathlib.Path("/home/claude/work/graphics")
spec = importlib.util.spec_from_file_location("render", G / "render.py")
R = importlib.util.module_from_spec(spec)
_argv = sys.argv; sys.argv = [sys.argv[0], "__none__"]
spec.loader.exec_module(R)            # defines CSS/page/progress; its __main__ block does not run on import
sys.argv = _argv
page, progress = R.page, R.progress
OUT = pathlib.Path("/home/claude/l04/gfx/out"); OUT.mkdir(parents=True, exist_ok=True)
B = {}          # name -> (html, alpha)
KIND = {}       # name -> FULL / PANEL / BAND
TEXT = {}       # name -> words a viewer must read (readability gate)
Q = lambda s: f"&#8220;{s}&#8221;"


def vis(i, n):
    return "visible" if i < n else "hidden"


def rows_html(items, n, num=True, size=54, aside=34, pad=22, w_name=None, cur=None):
    out = []
    for i, it in enumerate(items):
        name, sub = (it if isinstance(it, tuple) else (it, ""))
        col = "var(--text)" if (cur is None or i == cur) else "var(--muted)"
        numh = f'<div class="label a" style="width:64px;flex:none">0{i+1}</div>' if num else ""
        subh = (f'<div style="font-weight:300;font-size:{aside}px;line-height:1.25;color:var(--muted);margin-top:8px">{sub}</div>'
                if sub else "")
        out.append(f'<div style="visibility:{vis(i, n)};display:flex;align-items:baseline;gap:30px;padding:{pad}px 0;'
                   f'border-top:1px solid var(--line2)">{numh}<div style="flex:1;color:{col}">'
                   f'<div style="font-weight:500;font-size:{size}px;line-height:1.14;letter-spacing:-0.02em">{name}</div>{subh}</div></div>')
    end = '<div style="border-top:1px solid var(--line2)"></div>' if n >= len(items) else ""
    return "".join(out) + end


def full(name, body, text, top=150):
    B[name] = (page(f'<div class="safe"><div style="position:absolute;left:0;top:{top}px;width:100%">{body}</div></div>'), False)
    KIND[name] = "FULL"; TEXT[name] = text


def panel(name, body, text, top=230):
    """left-side text for the split layout (Wes card sits at x 1000-1840, y 190-886)"""
    B[name] = (page(f'<div style="position:absolute;left:128px;top:{top}px;width:780px">{body}</div>',
                    cls="alpha", glow=False, grain=False, vig=False), True)
    KIND[name] = "PANEL"; TEXT[name] = text
    # the same text as a full-frame board, for moments where Wes can't be on screen (scaled up 1.25x)
    B[name + "F"] = (page(f'<div style="position:absolute;left:128px;top:{max(150, top - 20)}px;width:780px;'
                          f'transform:scale(1.25);transform-origin:0 0">{body}</div>'), False)
    KIND[name + "F"] = "FULL"; TEXT[name + "F"] = text


def band(name, line1, line2="", text=None):
    l2 = (f'<div style="font-weight:300;font-size:40px;color:var(--muted);margin-top:10px;'
          f'text-shadow:0 2px 16px rgba(0,0,0,.8)">{line2}</div>') if line2 else ""
    B[name] = (page(f'<div style="position:absolute;left:160px;right:160px;bottom:{96 if line2 else 112}px;text-align:center">'
                    f'<div style="font-weight:500;font-size:56px;line-height:1.18;letter-spacing:-0.018em;'
                    f'text-shadow:0 2px 18px rgba(0,0,0,.85)">{line1}</div>{l2}</div>',
                    cls="alpha", glow=False, grain=False, vig=False), True)
    KIND[name] = "BAND"; TEXT[name] = text or (line1 + " " + line2)


def kicker(s, a=True):
    return f'<div class="label{" a" if a else ""}">{s}</div>'


def h1(s, size=92, mt=20, mb=0, col="var(--text)"):
    return (f'<div style="font-weight:600;font-size:{size}px;line-height:1.05;letter-spacing:-0.025em;color:{col};'
            f'margin-top:{mt}px;margin-bottom:{mb}px">{s}</div>')


def line(s, n_i, n, size=46, mt=26, col="var(--text)", w=300):
    return (f'<div style="visibility:{vis(n_i, n)};font-weight:{w};font-size:{size}px;line-height:1.24;'
            f'letter-spacing:-0.012em;color:{col};margin-top:{mt}px">{s}</div>')


# ---------------- opening -----------------------------------------------------------------------------
B["OPEN"] = (open(G / "html/01-opening-course-title.html").read(), False); KIND["OPEN"] = "FULL"; TEXT["OPEN"] = "logo"
B["BLACK"] = ('<!doctype html><html><body style="margin:0;width:1920px;height:1080px;background:#000"></body></html>', False)
KIND["BLACK"] = "FULL"; TEXT["BLACK"] = ""
B["FIELD"] = (page(""), False); KIND["FIELD"] = "FULL"; TEXT["FIELD"] = ""

# ---------------- scripture --------------------------------------------------------------------------------
def scripture(name, ref, lines, shown, text, hl=(), cur=None):
    body = []
    for i, l in enumerate(lines):
        for a in hl:
            l = l.replace(a, f'<span class="hl">{a}</span>')
        col = "var(--text)" if (cur is None or i == cur) else "var(--muted)"
        body.append(f'<div style="visibility:{vis(i, shown)};color:{col};margin-top:{0 if i == 0 else 20}px">{l}</div>')
    full(name, f"""<div class="label">Scripture</div>
  <div style="display:flex;align-items:baseline;gap:18px;margin-top:20px">
   <div style="font-weight:600;font-size:62px;letter-spacing:-0.02em">{ref}</div><div class="label" style="font-size:22px">NIV</div></div>
  <div style="font-weight:300;font-size:58px;line-height:1.34;letter-spacing:-0.008em;margin-top:46px;width:1560px">{''.join(body)}</div>""",
         text, top=150)


B["LOGO"] = (page('<div class="logo" style="position:absolute;left:560px;top:395px;width:800px;height:289px"></div>', glow=False), False)
KIND["LOGO"] = "FULL"; TEXT["LOGO"] = "logo"
B["LT"] = (open(G / "html/14b-lower-third-alpha.html").read(), True); KIND["LT"] = "BAND"; TEXT["LT"] = "Wes Hart Steadfast Men"
# Wes card frame for the split layout (drawn over the take; transparent inside)
B["CARD"] = (page('<div style="position:absolute;left:1000px;top:210px;width:840px;height:600px;border-radius:16px;'
                  'border:1px solid rgba(255,255,255,.16);box-shadow:0 0 0 1px rgba(0,0,0,.4)"></div>',
                  cls="alpha", glow=False, grain=False, vig=False), True)
KIND["CARD"] = "BAND"; TEXT["CARD"] = ""

def stack_band(name, items, n):
    rows = "".join(f'<div style="visibility:{vis(i, n)};display:flex;gap:20px;align-items:stretch;margin-top:14px">'
                   f'<div style="width:3px;border-radius:2px;background:{"var(--accent)" if i == n - 1 else "rgba(255,255,255,.35)"}"></div>'
                   f'<div style="font-weight:500;font-size:46px;letter-spacing:-0.016em;color:{"var(--text)" if i == n - 1 else "rgba(244,244,245,.72)"};'
                   f'text-shadow:0 2px 18px rgba(0,0,0,.85)">{t}</div></div>' for i, t in enumerate(items))
    B[name] = (page(f'<div style="position:absolute;left:128px;bottom:104px">{rows}</div>',
                    '<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(7,7,10,.55),rgba(7,7,10,0) 45%)"></div>' and "alpha",
                    glow=False, grain=False, vig=False), True)
    KIND[name] = "BAND"; TEXT[name] = " ".join(items[:n])


