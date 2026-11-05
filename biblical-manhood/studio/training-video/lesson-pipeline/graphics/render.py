"""Render the Steadfast Men course graphics package (1920x1080 keyframes).

Brand values come from walksteadfast.com's styles.css (aaronmaberry/steadfast):
Geist / Geist Mono (OFL), --bg #07070A, --text #F4F4F5, --accent #8B9CFF, --accent-2 #5B6EF5.
"""
import pathlib, sys
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
HTML = ROOT / "html"
OUT = ROOT / "out"
HTML.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)

# --- logo with real alpha (from the locked JPG on near-black) -------------------------
src = np.asarray(Image.open(ROOT / "img/logo-lockup.jpg").convert("RGB")).astype(np.float32)
mx = src.max(axis=2)
a = np.clip((mx - 8) / (src.max() - 8), 0, 1)
rgb = np.where(a[..., None] > 0.02, np.clip(src / np.maximum(a[..., None], 1e-3), 0, 255), 0)
Image.fromarray(np.dstack([rgb, a * 255]).astype(np.uint8), "RGBA").save(ROOT / "img/logo-alpha.png")

CSS = """
@font-face{font-family:'Geist';font-weight:300;src:url(../fonts/Geist-Light.woff2)}
@font-face{font-family:'Geist';font-weight:400;src:url(../fonts/Geist-Regular.woff2)}
@font-face{font-family:'Geist';font-weight:500;src:url(../fonts/Geist-Medium.woff2)}
@font-face{font-family:'Geist';font-weight:600;src:url(../fonts/Geist-SemiBold.woff2)}
@font-face{font-family:'Geist Mono';font-weight:400;src:url(../fonts/GeistMono-Regular.woff2)}
@font-face{font-family:'Geist Mono';font-weight:500;src:url(../fonts/GeistMono-Medium.woff2)}
:root{--bg:#07070A;--bg2:#0C0C10;--surface:#121218;--surface2:#18181F;--text:#F4F4F5;--muted:#A1A1AA;
--faint:#71717A;--line:rgba(255,255,255,.08);--line2:rgba(255,255,255,.14);--accent:#8B9CFF;--accent2:#5B6EF5}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;overflow:hidden;background:transparent}
.frame{position:relative;width:1920px;height:1080px;overflow:hidden;color:var(--text);font-family:'Geist';
 letter-spacing:-0.014em;-webkit-font-smoothing:antialiased;background:var(--bg)}
.frame.field{background:linear-gradient(180deg,#0C0C10 0%,#07070A 62%)}
.frame.alpha{background:transparent}
.glow{position:absolute;border-radius:50%;filter:blur(40px);pointer-events:none}
.grain{position:absolute;inset:0;background:url(../img/mesh.jpg);background-size:700px;mix-blend-mode:overlay;opacity:.05}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse 75% 70% at 50% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.42) 100%)}
.safe{position:absolute;left:128px;right:128px;top:112px;bottom:112px}
.label{font-family:'Geist Mono';font-weight:500;font-size:24px;letter-spacing:.18em;text-transform:uppercase;color:var(--faint)}
.label.a{color:var(--accent)}
.mono{font-family:'Geist Mono';letter-spacing:.1em;text-transform:uppercase}
.hl{background:rgba(139,156,255,.24);border-radius:6px;padding:0 .12em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.ul{text-decoration:underline;text-decoration-color:var(--accent);text-decoration-thickness:4px;text-underline-offset:10px}
.rule{height:1px;background:var(--line2)}
.logo{background:url(../img/logo-alpha.png) center/contain no-repeat}
.plate{position:absolute;inset:0;background-size:cover;background-position:center}
.prog{display:flex;gap:28px}
.prog .grp{display:flex;flex-direction:column;gap:12px}
.prog .ticks{display:flex;gap:6px}
.prog .t{width:40px;height:4px;border-radius:2px;background:rgba(255,255,255,.14)}
.prog .t.done{background:var(--accent2)}
.prog .t.now{background:var(--accent);box-shadow:0 0 12px rgba(139,156,255,.8)}
.prog .gl{font-family:'Geist Mono';font-weight:400;font-size:20px;letter-spacing:.1em;color:var(--faint);text-transform:uppercase;white-space:nowrap}
.prog .gl.on{color:var(--muted)}
.panel{position:absolute;background:rgba(18,18,24,.94);border:1px solid var(--line2);border-radius:12px;
 backdrop-filter:blur(8px)}
.cap{position:absolute;left:50%;transform:translateX(-50%);bottom:92px;text-align:center;font-weight:500;font-size:52px;
 line-height:1.25;letter-spacing:-0.005em;color:var(--text)}
.cap span{background:rgba(7,7,10,.72);border-radius:10px;padding:4px 20px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
"""

MARKS = ["Stop Waiting", "Pick Up the Weight", "Go First", "Work for God's Pay"]


def progress(lesson, labels=True):
    """24 lessons = 4 marks x 6. lesson 0 = intro (nothing lit)."""
    out = ['<div class="prog">']
    for g in range(4):
        out.append('<div class="grp"><div class="ticks">')
        for i in range(6):
            n = g * 6 + i + 1
            cls = "t done" if n < lesson else ("t now" if n == lesson else "t")
            out.append(f'<div class="{cls}"></div>')
        out.append("</div>")
        if labels:
            on = " on" if (lesson - 1) // 6 == g and lesson > 0 else ""
            out.append(f'<div class="gl{on}">{MARKS[g]}</div>')
        out.append("</div>")
    out.append("</div>")
    return "".join(out)


def page(body, cls="field", glow=True, grain=True, vig=True):
    g = ""
    if glow:
        g = ('<div class="glow" style="left:980px;top:-260px;width:1300px;height:900px;'
             'background:radial-gradient(closest-side,rgba(91,110,245,.16),rgba(91,110,245,0))"></div>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="frame {cls}">{g}{body}'
            f'{"<div class=vig></div>" if vig else ""}{"<div class=grain></div>" if grain else ""}</div></body></html>')


CARDS = {}

# 01 Opening / course title treatment
CARDS["01-opening-course-title"] = page("""
<div class="glow" style="left:460px;top:250px;width:1000px;height:520px;background:radial-gradient(closest-side,rgba(91,110,245,.30),rgba(91,110,245,0))"></div>
<div class="logo" style="position:absolute;left:560px;top:330px;width:800px;height:289px"></div>
<div class="label" style="position:absolute;left:0;right:0;top:700px;text-align:center;color:var(--muted)">The path &nbsp;·&nbsp; 24 lessons</div>
""", glow=False)

# 02 Lesson title card
CARDS["02-lesson-title"] = page(f"""
<div class="safe">
 <div class="logo" style="position:absolute;left:0;top:0;width:250px;height:90px;opacity:.95"></div>
 <div style="position:absolute;left:0;top:300px">
  <div class="label a">Lesson 00</div>
  <div style="font-weight:600;font-size:120px;line-height:1.02;letter-spacing:-0.025em;margin-top:22px">Introduction</div>
  <div style="font-weight:300;font-size:46px;line-height:1.25;color:var(--muted);margin-top:26px">24 lessons. One act, at your pace.</div>
 </div>
 <div style="position:absolute;left:0;bottom:0">{progress(0)}</div>
</div>""")

# 03 Chapter divider
CARDS["03-chapter-divider"] = page("""
<div class="safe">
 <div style="position:absolute;left:0;top:330px;width:100%">
  <div class="label a">Chapter 02 &nbsp;/&nbsp; 04</div>
  <div style="font-weight:600;font-size:96px;line-height:1.04;letter-spacing:-0.022em;margin-top:22px">The road ahead</div>
  <div class="rule" style="margin-top:44px;width:100%"></div>
  <div style="display:flex;gap:10px;margin-top:28px">
   <div style="width:72px;height:4px;border-radius:2px;background:var(--accent2)"></div>
   <div style="width:72px;height:4px;border-radius:2px;background:var(--accent);box-shadow:0 0 12px rgba(139,156,255,.8)"></div>
   <div style="width:72px;height:4px;border-radius:2px;background:rgba(255,255,255,.14)"></div>
   <div style="width:72px;height:4px;border-radius:2px;background:rgba(255,255,255,.14)"></div>
  </div>
 </div>
</div>""")

VERSE = ('Therefore, my dear brothers and sisters, <span class="hl">stand firm</span>. Let nothing move you. '
         'Always give yourselves <span class="hl ul">fully</span> to the work of the Lord, because you know '
         'that your labor in the Lord is not in vain.')

# 04 Scripture card, full frame
CARDS["04-scripture-full"] = page(f"""
<div class="safe">
 <div style="position:absolute;left:0;top:110px;width:1460px">
  <div class="label">Scripture</div>
  <div style="display:flex;align-items:baseline;gap:18px;margin-top:20px">
   <div style="font-weight:600;font-size:60px;letter-spacing:-0.02em">1 Corinthians 15:58</div>
   <div class="label" style="font-size:22px">NIV</div></div>
  <div style="font-weight:300;font-size:54px;line-height:1.4;letter-spacing:-0.008em;margin-top:44px">{VERSE}</div>
 </div>
</div>""")

# 05 Scripture split board (board left, Wes right) — composite on a locked plate
CARDS["05-scripture-split"] = page(f"""
<div class="plate" style="background-image:url(../plates/p08.jpg)"></div>
<div style="position:absolute;left:0;top:0;width:1060px;height:1080px;background:linear-gradient(90deg,#0C0C10 0%,#0C0C10 83%,rgba(12,12,16,0) 100%)"></div>
<div style="position:absolute;left:128px;top:190px;width:700px">
  <div class="label">Scripture</div>
  <div style="display:flex;align-items:baseline;gap:14px;margin-top:18px">
   <div style="font-weight:600;font-size:50px;letter-spacing:-0.02em">1 Corinthians 15:58</div>
   <div class="label" style="font-size:20px">NIV</div></div>
  <div style="font-weight:300;font-size:42px;line-height:1.4;margin-top:34px">{VERSE}</div>
</div>""", glow=False)

# 06 Key principle / framework board — the four marks
rows = "".join(
    f'<div style="display:flex;align-items:baseline;gap:34px;padding:22px 0;border-top:1px solid var(--line2)">'
    f'<div class="label a" style="width:60px">0{i+1}</div>'
    f'<div style="font-weight:500;font-size:58px;letter-spacing:-0.02em;flex:1">{m}</div>'
    f'<div class="label" style="font-size:20px;color:var(--muted)">{ref}</div></div>'
    for i, (m, ref) in enumerate(zip(MARKS, ["James 4:17", "Galatians 6:5", "John 10:4", "Colossians 3:23–24"])))
CARDS["06-key-principle-four-marks"] = page(f"""
<div class="safe">
 <div style="position:absolute;left:0;top:40px;width:100%">
  <div class="label a">The measure</div>
  <div style="font-weight:600;font-size:84px;letter-spacing:-0.025em;margin:18px 0 46px">Four marks. No fifth.</div>
  {rows}<div style="border-top:1px solid var(--line2)"></div>
 </div>
</div>""")

# 07 Definition card
CARDS["07-definition"] = page("""
<div class="safe">
 <div style="position:absolute;left:0;top:300px;width:1400px">
  <div class="label">Definition</div>
  <div style="font-weight:600;font-size:104px;letter-spacing:-0.025em;margin-top:20px">God&#8217;s pay</div>
  <div style="font-weight:300;font-size:56px;line-height:1.25;color:var(--text);margin-top:20px">A Father&#8217;s inheritance, <span class="hl">not wages</span>.</div>
  <div class="label" style="margin-top:44px;font-size:20px;color:var(--muted)">Colossians 3:23–24</div>
 </div>
</div>""")

# 08 Quote card
CARDS["08-quote"] = page("""
<div class="safe">
 <div style="position:absolute;left:0;top:300px;width:1500px">
  <div style="font-weight:400;font-size:76px;line-height:1.14;letter-spacing:-0.022em">&#8220;What I hope you walk away with isn&#8217;t <span class="hl">a stack of notes</span>.&#8221;</div>
  <div class="label" style="margin-top:44px">Wes Hart</div>
 </div>
</div>""")

# 09 Write-this-down panel (overlay over Wes)
CARDS["09-write-this-down-overlay"] = page("""
<div class="plate" style="background-image:url(../plates/p08.jpg)"></div>
<div class="panel" style="left:128px;top:236px;width:700px;padding:44px 48px 48px">
 <div class="label a">Write this down</div>
 <div style="font-weight:500;font-size:48px;line-height:1.32;letter-spacing:-0.018em;margin-top:24px">
  Stop waiting.<br>Pick up the weight.<br>Go first.<br>Work for God&#8217;s pay.</div>
</div>""", glow=False, vig=False)

# 10 Reflection card
CARDS["10-reflection"] = page("""
<div class="safe">
 <div style="position:absolute;left:0;top:330px;width:1400px">
  <div class="label a">Pause and reflect</div>
  <div style="font-weight:400;font-size:76px;line-height:1.14;letter-spacing:-0.022em;margin-top:24px">Look honestly at what you were handed.</div>
  <div class="label" style="margin-top:48px;font-size:20px">Sit with it for a moment</div>
 </div>
</div>""")

# 11 Action step — the act
CARDS["11-action-the-act"] = page("""
<div class="safe">
 <div style="position:absolute;left:0;top:250px;width:1500px">
  <div class="label a">The act</div>
  <div style="font-weight:600;font-size:92px;line-height:1.08;letter-spacing:-0.025em;margin-top:24px">Write the act here.<br>One sentence.<br><span style="color:var(--accent)">Then do it.</span></div>
  <div style="margin-top:70px;width:1100px;border-bottom:2px solid var(--line2);height:2px"></div>
 </div>
</div>""")

# 12 Practical challenge card
CARDS["12-challenge"] = page("""
<div class="safe">
 <div style="position:absolute;left:0;top:330px;width:1500px">
  <div class="label a">Before Lesson 01</div>
  <div style="font-weight:500;font-size:80px;line-height:1.12;letter-spacing:-0.022em;margin-top:24px">Print the pages.<br>Leave them on the table.</div>
 </div>
</div>""")

# 13 Progress indicator, standalone overlay (transparent)
CARDS["13-progress-overlay"] = (page(f"""
<div style="position:absolute;left:128px;bottom:112px">{progress(1)}</div>""", cls="alpha", glow=False, grain=False, vig=False), True)

# 14 Lower third with disclosure (overlay preview on Wes)
CARDS["14-lower-third"] = page("""
<div class="plate" style="background-image:url(../plates/p08.jpg)"></div>
<div style="position:absolute;left:0;bottom:0;width:1100px;height:420px;background:radial-gradient(ellipse at 0% 100%,rgba(7,7,10,.72),rgba(7,7,10,0) 70%)"></div>
<div style="position:absolute;left:128px;top:752px;display:flex;gap:22px;align-items:stretch">
 <div style="width:3px;border-radius:2px;background:var(--accent)"></div>
 <div><div style="font-weight:500;font-size:46px;letter-spacing:-0.02em">Wes Hart</div>
  <div class="label" style="font-size:20px;color:var(--muted);margin-top:8px">Steadfast Men</div></div>
</div>""", glow=False, vig=False)

# 14b lower third alone, transparent
CARDS["14b-lower-third-alpha"] = (page("""
<div style="position:absolute;left:128px;top:752px;display:flex;gap:22px;align-items:stretch">
 <div style="width:3px;border-radius:2px;background:var(--accent)"></div>
 <div><div style="font-weight:500;font-size:46px;letter-spacing:-0.02em;text-shadow:0 2px 18px rgba(0,0,0,.6)">Wes Hart</div>
  <div class="label" style="font-size:20px;color:var(--muted);margin-top:8px;text-shadow:0 2px 12px rgba(0,0,0,.7)">Steadfast Men</div></div>
</div>""", cls="alpha", glow=False, grain=False, vig=False), True)

# 15 Closing recap
recap = ["See what God built a man for.", "Look honestly at what you were handed.",
         "Have a few men who actually know you.", "Make real moves someone at home notices."]
CARDS["15-closing-recap"] = page("""
<div class="safe"><div style="position:absolute;left:0;top:150px;width:1500px">
 <div class="label a">What you&#8217;ll carry</div>
 <div style="margin-top:34px">""" + "".join(
    f'<div style="display:flex;gap:34px;align-items:baseline;padding:20px 0;border-top:1px solid var(--line2)">'
    f'<div class="label" style="width:56px">0{i+1}</div><div style="font-weight:400;font-size:54px;letter-spacing:-0.018em">{t}</div></div>'
    for i, t in enumerate(recap)) + """<div style="border-top:1px solid var(--line2)"></div></div></div></div>""")

# 16 Next lesson preview
CARDS["16-next-lesson"] = page(f"""
<div class="safe">
 <div style="position:absolute;left:0;top:250px;width:760px">
  <div class="label a">Next &nbsp;·&nbsp; Lesson 01</div>
  <div style="font-weight:600;font-size:96px;line-height:1.04;letter-spacing:-0.025em;margin-top:22px">A Quiet Tuesday</div>
  <div class="label" style="margin-top:26px;color:var(--muted)">Stop Waiting &nbsp;·&nbsp; 1 of 6</div>
 </div>
 <div style="position:absolute;right:0;top:170px;width:820px;height:461px;border-radius:12px;overflow:hidden;border:1px solid var(--line2);
   background:url(../img/lesson-01.jpg) center/cover"></div>
 <div style="position:absolute;left:0;bottom:0">{progress(1)}</div>
</div>""")

# 17 Caption style on picture
CARDS["17-caption-style"] = page("""
<div class="plate" style="background-image:url(../plates/p08.jpg)"></div>
<div class="cap" style="width:1500px"><span>Married, single, divorced, new dad,</span><br><span>or your kids are taller than you now.</span></div>
""", glow=False, vig=False)

# 18 Resources (closing segment)
res = [("Podcast", "Walk Steadfast"), ("YouTube", "@steadfastwalk"), ("Socials", "@steadfastwalk"),
       ("Book &amp; workbook", "walksteadfast.com/shop"), ("Give", "walksteadfast.com/give")]
CARDS["18-resources"] = page("""
<div class="safe"><div style="position:absolute;left:0;top:150px;width:1300px">
 <div class="label a">Between lessons</div>
 <div style="font-weight:600;font-size:80px;letter-spacing:-0.025em;margin:18px 0 40px">Keep walking.</div>""" + "".join(
    f'<div style="display:flex;align-items:baseline;padding:18px 0;border-top:1px solid var(--line2)">'
    f'<div class="label" style="width:420px">{k}</div><div style="font-weight:400;font-size:46px;letter-spacing:-0.015em">{v}</div></div>'
    for k, v in res) + """<div style="border-top:1px solid var(--line2)"></div></div></div>""")

# 19 End credits with NIV notice + disclosure
CARDS["19-end-credits"] = page("""
<div class="logo" style="position:absolute;left:760px;top:250px;width:400px;height:145px"></div>
<div style="position:absolute;left:360px;right:360px;top:500px;text-align:center;font-size:24px;line-height:1.6;color:var(--muted)">
 Created by Wes Hart.<br><br>
 Scripture quotations taken from The Holy Bible, New International Version® NIV®.<br>
 Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc. Used with permission. All rights reserved worldwide.<br><br>
 <span class="mono" style="font-size:20px;color:var(--faint)">© 2026 Steadfast Men &nbsp;·&nbsp; walksteadfast.com</span>
</div>""", glow=False)

THUMB = page("""
<div class="plate" style="background-image:url(../plates/p08.jpg)"></div>
<div style="position:absolute;left:0;top:0;width:1060px;height:1080px;background:linear-gradient(90deg,#07070A 0%,#07070A 83%,rgba(7,7,10,0) 100%)"></div>
<div style="position:absolute;left:120px;top:150px">
 <div class="label a" style="font-size:40px">Lesson 00</div>
 <div style="font-weight:600;font-size:176px;line-height:.98;letter-spacing:-0.035em;margin-top:30px">Before<br>you<br>start.</div>
</div>
<div class="logo" style="position:absolute;left:120px;bottom:110px;width:300px;height:108px"></div>
""", glow=False)
CARDS["20-thumbnail"] = THUMB

if __name__ == "__main__":
    only = set(sys.argv[1:])
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        for name, spec in CARDS.items():
            if only and name not in only:
                continue
            html, alpha = (spec if isinstance(spec, tuple) else (spec, False))
            f = HTML / f"{name}.html"
            f.write_text(html)
            pg.goto(f.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(OUT / f"{name}.png"), omit_background=alpha)
            print("rendered", name)
        b.close()
    # thumbnail at 1280x720 from the 1080 master
    im = Image.open(OUT / "20-thumbnail.png").convert("RGB").resize((1280, 720), Image.LANCZOS)
    im.save(OUT / "20-thumbnail-1280x720.jpg", quality=92)
