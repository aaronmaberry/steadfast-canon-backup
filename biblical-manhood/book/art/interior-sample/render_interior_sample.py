#!/usr/bin/env python3
"""6x9 print sample: chapter opener (recto) + Your turn closer (verso).
Reuses existing closer PNG. Does not redo 01-15 art.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("/workspace/biblical-manhood/book/art/interior-sample")
ART = Path("/workspace/biblical-manhood/book/art")
PPI = 300
W, H = 6 * PPI, 9 * PPI  # 1800 x 2700

BONE = (244, 239, 228)
INK = (44, 41, 36)
INK_SOFT = (90, 84, 76)
RUST = (122, 74, 50)
RULE = (196, 184, 168)

FONT_TITLE = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_BODY = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"
FONT_ITAL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"
FONT_LABEL = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"

# Recto opener: gutter LEFT. Verso closer: gutter RIGHT.
GUTTER = int(0.75 * PPI)
OUTSIDE = int(0.60 * PPI)
TOP = int(0.70 * PPI)
BOTTOM = int(0.70 * PPI)


def pt(n):
    return int(round(n * PPI / 72))


def load(path, size_pt):
    return ImageFont.truetype(path, pt(size_pt))


def text_h(font):
    a, d = font.getmetrics()
    return a + d


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_label(draw, text, xy, font, fill, tracking_px):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking_px
    return x


def opener():
    img = Image.new("RGB", (W, H), BONE)
    d = ImageDraw.Draw(img)
    # recto: left is gutter
    left = GUTTER
    right = W - OUTSIDE
    measure = right - left

    mark = Image.open(ART / "opener-mark.png").convert("RGBA")
    # keep native size (~0.42 x 0.78 in)
    img.paste(mark, (left, TOP), mark)

    y = TOP + mark.size[1] + pt(10)
    lab = load(FONT_LABEL, 8)
    draw_label(d, "CHAPTER 1", (left, y), lab, RUST, 3.2)
    y += text_h(lab) + pt(8)

    title_f = load(FONT_TITLE, 22)
    d.text((left, y), "A quiet Tuesday", font=title_f, fill=INK)
    y += text_h(title_f) + pt(4)
    d.rectangle([left, y, left + pt(42), y + 3], fill=RUST)
    y += pt(16)

    body = load(FONT_BODY, 11)
    lh = int(text_h(body) * 1.38)
    paras = [
        "You can tell a lot about a man by the day nobody is filming.",
        "Tuesday. Alarm's already going. Same kitchen light, same coffee you won't finish. The truck's warm even at 7 if it's August. Same commute, or the same walk to the desk in the other room. If there are people in your house, they already know if you showed up.",
        "A lot of us can rise for a camera. Fewer of us can rise for a cereal bowl.",
        "I know that pull. I've been in a room and somewhere else at the same time. Phone face-down. Then face-up. Then face-down again, like the flipping is the same thing as being there. It isn't.",
        "A boy asked me to watch one more throw once. I watched the clock. He noticed. I pretended he didn't.",
        "Tuesday doesn't argue with you. It just tells on you.",
    ]
    for para in paras:
        lines = wrap(d, para, body, measure)
        for line in lines:
            if y + lh > H - BOTTOM - pt(18):
                break
            d.text((left, y), line, font=body, fill=INK)
            y += lh
        y += int(lh * 0.42)

    # footer recto: page number outside
    foot = load(FONT_BODY, 8)
    d.text((right - d.textlength("3", font=foot), H - BOTTOM + pt(8)), "3", font=foot, fill=INK_SOFT)
    run = load(FONT_ITAL, 8)
    d.text((left, H - BOTTOM + pt(8)), "Steadfast Men", font=run, fill=RULE)
    return img


def closer():
    img = Image.new("RGB", (W, H), BONE)
    d = ImageDraw.Draw(img)
    # verso: right is gutter
    left = OUTSIDE
    right = W - GUTTER
    measure = right - left

    y = TOP + pt(20)
    lab = load(FONT_LABEL, 8)

    box = Image.open(ART / "01-closer-box.png").convert("RGBA")
    # native 4.75 in. Fit to measure if needed, never stretch aspect.
    max_w = measure
    if box.size[0] > max_w:
        scale = max_w / box.size[0]
        box = box.resize(
            (int(box.size[0] * scale), int(box.size[1] * scale)),
            Image.Resampling.LANCZOS,
        )
    x = left + (measure - box.size[0]) // 2
    img.paste(box, (x, y), box)

    foot = load(FONT_BODY, 8)
    d.text((left, H - BOTTOM + pt(8)), "4", font=foot, fill=INK_SOFT)
    run = load(FONT_ITAL, 8)
    tw = d.textlength("Steadfast Men", font=run)
    d.text((right - tw, H - BOTTOM + pt(8)), "Steadfast Men", font=run, fill=RULE)
    return img


def spread(op, cl):
    """Opener on the right (recto), closer on the left (verso) as a facing pair
    would actually print: left=even closer, right=odd opener is wrong for
    chapter start. Chapter opener is recto, closer comes later. For the
    sample, show opener | closer as two consecutive right-reading pages
    side by side, opener left in the composite only so a reviewer can
    see both treatments at once. Labeled in the md.
    """
    gap = int(0.15 * PPI)
    canvas = Image.new("RGB", (W * 2 + gap, H), (210, 204, 194))
    canvas.paste(op, (0, 0))
    canvas.paste(cl, (W + gap, 0))
    return canvas


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    op = opener()
    cl = closer()
    op.save(OUT / "opener-6x9.png", "PNG", dpi=(PPI, PPI))
    cl.save(OUT / "closer-6x9.png", "PNG", dpi=(PPI, PPI))
    sp = spread(op, cl)
    sp.save(OUT / "spread-6x9.png", "PNG", dpi=(PPI, PPI))
    print("opener", op.size)
    print("closer", cl.size)
    print("spread", sp.size)


if __name__ == "__main__":
    main()
