#!/usr/bin/env python3
"""Original closer box for Steadfast Men, chapter 03. No stock. No scene."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("/workspace/biblical-manhood/book/art")
PPI = 300
WIDTH_IN = 4.75
# Height is measured after layout; start tall then crop.

BONE = (244, 239, 228)
INK = (44, 41, 36)
INK_SOFT = (90, 84, 76)
RUST = (122, 74, 50)
RULE = (120, 110, 96)
CARRY_BAND = (236, 228, 212)

FONT_LABEL = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_BODY = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"
FONT_ITAL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"
FONT_ROMAN_SM = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"

W = int(WIDTH_IN * PPI)


def pt(n):
    return int(round(n * PPI / 72))


def load(path, size_pt):
    return ImageFont.truetype(path, pt(size_pt))


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


def draw_spaced(draw, text, xy, font, fill, tracking=0.18):
    """Letterspaced uppercase label."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + pt(tracking * 10) / 10 * font.size * tracking / 4
    # simpler tracking: space by fraction of em
    return x


def draw_label(draw, text, xy, font, fill, tracking_px):
    x, y = xy
    for i, ch in enumerate(text):
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking_px
    return x


def text_h(font):
    a, d = font.getmetrics()
    return a + d


def main():
    label_f = load(FONT_LABEL, 8)
    body_f = load(FONT_BODY, 10.5)
    ital_f = load(FONT_ITAL, 10.5)
    carry_f = load(FONT_ITAL, 13)
    small_f = load(FONT_ROMAN_SM, 8)

    pad_l = pt(22)
    pad_r = pt(18)
    pad_t = pt(16)
    pad_b = pt(16)
    rail_x = pt(10)
    rail_w = max(2, pt(0.65))
    inner_l = pad_l
    text_w = W - inner_l - pad_r
    label_track = 3.6
    body_lh = int(text_h(body_f) * 1.28)
    carry_lh = int(text_h(carry_f) * 1.22)
    section_gap = pt(13)
    rule_gap = pt(9)

    sections = [
        {
            "label": "NAME IT",
            "body": "Which ugly sentence have you been living instead of the four?",
            "kind": "plain",
        },
        {
            "label": "DO THIS WEEK",
            "body": "Write the four longhand until you can say them out loud.",
            "kind": "writein",
            "prompt": "The four marks:",
        },
        {
            "label": "TELL A BROTHER",
            "body": "Say them to him. Have him say them back. No speech.",
            "kind": "plain",
        },
        {
            "label": "CARRY THIS",
            "body": "A real man rejects passivity, accepts responsibility, leads courageously, and expects the greater reward, God's reward.",
            "kind": "carry",
        },
    ]

    # Measure
    measure = Image.new("RGB", (W, 4000), BONE)
    md = ImageDraw.Draw(measure)

    y = pad_t
    y += text_h(small_f) + pt(10)  # tiny 01
    measured = []
    for i, sec in enumerate(sections):
        top = y
        y += text_h(label_f) + pt(5)
        lines = wrap(md, sec["body"], carry_f if sec["kind"] == "carry" else body_f, text_w)
        lh = carry_lh if sec["kind"] == "carry" else body_lh
        body_top = y
        y += lh * len(lines)
        writein_top = None
        if sec["kind"] == "writein":
            y += pt(9)
            writein_top = y
            y += text_h(ital_f) + pt(6) + pt(14)  # prompt + one write-in rule
        bottom = y
        measured.append((top, body_top, lines, writein_top, bottom))
        if i < len(sections) - 1:
            y += rule_gap
            y += 1  # rule
            y += section_gap

    y += pad_b
    H = y

    img = Image.new("RGB", (W, H), BONE)
    d = ImageDraw.Draw(img)

    # Outer hairline
    d.rectangle([0, 0, W - 1, H - 1], outline=RULE, width=1)

    # Iron rail
    d.rectangle([rail_x, pt(8), rail_x + rail_w, H - pt(8)], fill=RUST)

    # Tiny chapter mark
    d.text((inner_l, pad_t), "03", font=small_f, fill=RUST)

    for i, sec in enumerate(sections):
        top, body_top, lines, writein_top, bottom = measured[i]
        # tick on the rail, aligned to label
        tick_y = top + text_h(label_f) // 2
        tick_h = max(3, pt(2.2))
        tick_w = max(6, pt(4.5))
        d.rectangle(
            [rail_x - 1, tick_y - tick_h // 2, rail_x + tick_w, tick_y + tick_h // 2 + 1],
            fill=RUST,
        )
        draw_label(d, sec["label"], (inner_l, top), label_f, RUST, label_track)

        font = carry_f if sec["kind"] == "carry" else body_f
        fill = INK
        lh = carry_lh if sec["kind"] == "carry" else body_lh
        yy = body_top
        for line in lines:
            d.text((inner_l, yy), line, font=font, fill=fill)
            yy += lh

        if sec["kind"] == "writein":
            d.text((inner_l, writein_top), sec["prompt"], font=ital_f, fill=INK_SOFT)
            line_y = writein_top + text_h(ital_f) + pt(10)
            d.line([(inner_l, line_y), (W - pad_r, line_y)], fill=RULE, width=1)

        if i < len(sections) - 1 and sec["kind"] != "writein":
            rule_y = bottom + rule_gap
            d.line([(inner_l, rule_y), (W - pad_r, rule_y)], fill=RULE, width=1)

    # Carry band: a quiet wash behind the last section only
    last_top = measured[-1][0] - pt(6)
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(band)
    bd.rectangle([1, last_top, W - 2, H - 2], fill=(*CARRY_BAND, 255))
    base = Image.new("RGBA", (W, H), (*BONE, 255))
    # rebuild with band under last section: composite then redraw last type
    # Simpler: fill band on main image before last type was drawn — too late.
    # Recolor by pasting a rectangle then redrawing last section.
    d.rectangle([1, last_top, W - 2, H - 2], fill=CARRY_BAND)
    # redraw rail over band
    d.rectangle([rail_x, last_top, rail_x + rail_w, H - pt(8)], fill=RUST)
    # redraw last tick, label, carry line
    sec = sections[-1]
    top, body_top, lines, writein_top, bottom = measured[-1]
    tick_y = top + text_h(label_f) // 2
    tick_h = max(3, pt(2.2))
    tick_w = max(6, pt(4.5))
    d.rectangle(
        [rail_x - 1, tick_y - tick_h // 2, rail_x + tick_w, tick_y + tick_h // 2 + 1],
        fill=RUST,
    )
    draw_label(d, sec["label"], (inner_l, top), label_f, RUST, label_track)
    yy = body_top
    for line in lines:
        d.text((inner_l, yy), line, font=carry_f, fill=INK)
        yy += carry_lh
    d.rectangle([0, 0, W - 1, H - 1], outline=RULE, width=1)

    png = OUT / "03-closer-box.png"
    img.save(png, "PNG", dpi=(PPI, PPI))
    preview = img.resize((W // 2, H // 2), Image.Resampling.LANCZOS)
    prev_path = OUT / "03-closer-box-preview.png"
    preview.save(prev_path, "PNG", dpi=(150, 150))

    # SVG source
    def svg_escape(s):
        return (
            s.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    scale = 72 / PPI  # SVG in points
    sw, sh = W * scale, H * scale

    def px(v):
        return round(v * scale, 2)

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{sw:.2f}pt" height="{sh:.2f}pt" viewBox="0 0 {W} {H}">')
    svg.append("<defs>")
    svg.append('<style type="text/css"><![CDATA[')
    svg.append("@font-face { font-family: 'P052'; src: url('/usr/share/fonts/opentype/urw-base35/P052-Roman.otf'); }")
    svg.append("@font-face { font-family: 'P052I'; src: url('/usr/share/fonts/opentype/urw-base35/P052-Italic.otf'); }")
    svg.append("@font-face { font-family: 'C059B'; src: url('/usr/share/fonts/opentype/urw-base35/C059-Bold.otf'); }")
    svg.append("]]></style></defs>")
    svg.append(f'<rect width="{W}" height="{H}" fill="#F4EFE4"/>')
    last_top = measured[-1][0] - pt(6)
    svg.append(f'<rect x="1" y="{last_top}" width="{W-2}" height="{H-2-last_top}" fill="#ECE4D4"/>')
    svg.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="none" stroke="#C4B8A8" stroke-width="1"/>')
    svg.append(f'<rect x="{rail_x}" y="{pt(8)}" width="{rail_w}" height="{H - pt(16)}" fill="#7A4A32"/>')
    svg.append(f'<text x="{inner_l}" y="{pad_t + text_h(small_f) - 4}" font-family="P052" font-size="{pt(8)}" fill="#7A4A32">03</text>')

    for i, sec in enumerate(sections):
        top, body_top, lines, writein_top, bottom = measured[i]
        tick_y = top + text_h(label_f) // 2
        tick_h = max(3, pt(2.2))
        tick_w = max(6, pt(4.5))
        svg.append(
            f'<rect x="{rail_x-1}" y="{tick_y - tick_h // 2}" width="{tick_w + 1}" height="{tick_h + 1}" fill="#7A4A32"/>'
        )
        # letterspaced label
        x = inner_l
        fs = pt(8)
        svg.append(f'<text x="{x}" y="{top + text_h(label_f) - 6}" font-family="C059B" font-size="{fs}" fill="#7A4A32" letter-spacing="{label_track}">{sec["label"]}</text>')
        font_size = pt(13) if sec["kind"] == "carry" else pt(10.5)
        fam = "P052I" if sec["kind"] == "carry" else "P052"
        fill = "#2C2924"
        lh = carry_lh if sec["kind"] == "carry" else body_lh
        yy = body_top
        for line in lines:
            baseline = yy + int(font_size * 0.8)
            svg.append(
                f'<text x="{inner_l}" y="{baseline}" font-family="{fam}" font-size="{font_size}" fill="{fill}">{svg_escape(line)}</text>'
            )
            yy += lh
        if sec["kind"] == "writein":
            fs2 = pt(10.5)
            svg.append(
                f'<text x="{inner_l}" y="{writein_top + int(fs2*0.8)}" font-family="P052I" font-size="{fs2}" fill="#5A544C">{svg_escape(sec["prompt"])}</text>'
            )
            line_y = writein_top + text_h(ital_f) + pt(10)
            svg.append(
                f'<line x1="{inner_l}" y1="{line_y}" x2="{W - pad_r}" y2="{line_y}" stroke="#C4B8A8" stroke-width="1"/>'
            )
        if i < len(sections) - 1 and sec["kind"] != "writein":
            rule_y = bottom + rule_gap
            svg.append(
                f'<line x1="{inner_l}" y1="{rule_y}" x2="{W - pad_r}" y2="{rule_y}" stroke="#C4B8A8" stroke-width="1"/>'
            )

    svg.append("</svg>")
    svg_path = OUT / "03-closer-box.svg"
    svg_path.write_text("\n".join(svg), encoding="utf-8")

    note = OUT / "03-closer-box.md"
    note.write_text(
        "\n".join(
            [
                "# 03 closer box",
                "",
                "Quiet closer for chapter 3 only. No scene drawing.",
                "",
                "- `03-closer-box.png` — print, 4.75 in wide, 300 ppi, RGB",
                "- `03-closer-box-preview.png` — half-size look",
                "- `03-closer-box.svg` — type source",
                "",
                "Beats: Name it / Do this week / Tell a brother / Carry this.",
                "Copy from 03-the-four-marks.md. Original type. No stock.",
                "Bone paper, iron rail, rust ticks. Grown, quiet, Texas-honest.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"PNG {png} {img.size}")
    print(f"PREVIEW {prev_path}")
    print(f"SVG {svg_path}")


if __name__ == "__main__":
    main()
