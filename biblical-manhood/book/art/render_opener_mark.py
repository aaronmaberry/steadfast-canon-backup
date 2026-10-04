#!/usr/bin/env python3
"""Small repeating chapter opener mark. Iron post, four ticks. Not a logo mashup."""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path("/workspace/biblical-manhood/book/art")
PPI = 300
BONE = (244, 239, 228)
RUST = (122, 74, 50)

W, H = int(0.42 * PPI), int(0.78 * PPI)
img = Image.new("RGB", (W, H), BONE)
d = ImageDraw.Draw(img)

rail_x = int(W * 0.42)
rail_w = max(3, int(0.018 * PPI))
pad = int(0.08 * PPI)
d.rectangle([rail_x, pad, rail_x + rail_w, H - pad], fill=RUST)

tick_w = int(0.12 * PPI)
tick_h = max(3, int(0.018 * PPI))
inner_h = H - 2 * pad
for i in range(4):
    cy = pad + int((i + 0.5) * inner_h / 4)
    d.rectangle(
        [rail_x, cy - tick_h // 2, rail_x + tick_w, cy + tick_h // 2 + 1],
        fill=RUST,
    )

png = OUT / "opener-mark.png"
img.save(png, "PNG", dpi=(PPI, PPI))
print(png, img.size)
