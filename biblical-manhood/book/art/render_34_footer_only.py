#!/usr/bin/env python3
"""Redo 34 man-plan FOOTER ONLY. Pixel-clean brand line."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PNG = Path("/workspace/biblical-manhood/book/art/34-man-plan.png")
PREV = Path("/workspace/biblical-manhood/book/art/34-man-plan-preview.png")
FONT = Path("/usr/share/fonts/opentype/urw-base35/P052-Roman.otf")

BONE = (230, 221, 204)
NAVY = (11, 31, 56)
RULE = (180, 168, 148)

img = Image.open(PNG).convert("RGB")
W, H = img.size
d = ImageDraw.Draw(img)

d.rectangle([0, 2360, W, H], fill=BONE)

# 12 pt at 300 ppi = 50 px. One face. No italic ghost.
fnt = ImageFont.truetype(str(FONT), 50)
line = "Steadfast Men, The way of Godly Men"
bbox = d.textbbox((0, 0), line, font=fnt)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
x = (W - tw) // 2
y = H - 100 - (bbox[3] - bbox[1])

d.line([(208, y - 40), (W - 208, y - 40)], fill=RULE, width=2)
d.text((x, y), line, font=fnt, fill=NAVY)

img.save(PNG, "PNG", dpi=(300, 300))
img.resize((W // 3, H // 3), Image.Resampling.LANCZOS).save(PREV, "PNG")
print("ok", line, "size", tw, th, "at", x, y)
