#!/usr/bin/env python3
"""FLOW contrast pass: recut closer boxes to Reed-signed copy. Gold never on bone."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("/workspace/biblical-manhood/book/art")
PPI = 300
WIDTH_IN = 4.75

BONE = (244, 239, 228)
INK = (11, 31, 56)  # navy body on bone
INK_SOFT = (90, 84, 76)
NAVY = (11, 31, 56)
RUST = NAVY  # Ash: no rust/gold accent type on bone; labels+rail navy
RULE = (120, 110, 96)  # darkened for contrast
CARRY_BAND = (236, 228, 212)

FONT_LABEL = "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf"
FONT_BODY = "/usr/share/fonts/opentype/urw-base35/P052-Roman.otf"
FONT_ITAL = "/usr/share/fonts/opentype/urw-base35/P052-Italic.otf"

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


def draw_label(draw, text, xy, font, fill, tracking_px):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking_px
    return x


def text_h(font):
    a, d = font.getmetrics()
    return a + d


# Reed FLOW-signed closer copy (2026-09-07). Third beat may branch.
CHAPTERS = {
    "01": [
        ("NAME IT", "Because a man can't change a day he hasn't looked at: walk through your last ordinary weekday hour by hour and say out loud two places where you made a decision that didn't feel like one.", "plain"),
        ("DO THIS WEEK", "Because the shape gets made in small repeated things: pick one of those two places and do it differently next Tuesday. Answer the call. Put the phone face down. Have the ten minutes at the counter.", "writein", "What you'll do differently:"),
        ("TELL A BROTHER", "Because a Tuesday nobody knows about is a Tuesday you'll forget by Thursday: tell one man what you noticed about your ordinary day and what you're going to do with the next one.", "plain"),
        ("CARRY THIS", "A man's life is decided on Tuesdays. The big days mark things; the ordinary ones make them.", "carry"),
    ],
    "02": [
        ("NAME IT", "Because the shame lifts when you can see the pile for what it is: say out loud two of the contradictory instructions you were handed about being a man, and where each one came from.", "plain"),
        ("DO THIS WEEK", "Because a man who's been performing for six audiences needs to hear his own voice: write down, in one sentence, what you actually believe a man is supposed to do, before you read the next chapter. Keep it to compare later.", "writein", "Your sentence:"),
        ("TELL A BROTHER", "Because every man you know is carrying the same pile and thinks he's the only one: read him your sentence and ask for his. You'll both feel the hum get quieter.", "plain"),
        ("CARRY THIS", "You are not crazy. The confusion is in the world, and the answer is simpler and harder than anything on the shelf.", "carry"),
    ],
    "03": [
        ("NAME IT", "Because you can't work on a mark you haven't looked at: say which of the four is faintest on you right now, in a full sentence, and say why you think that is.", "plain"),
        ("DO THIS WEEK", "Because a sentence in a book stays in the book until you put it where your eyes go: write the four marks on an index card in your own handwriting and put it on the truck visor or the shaving mirror, somewhere you'll see it Tuesday morning.", "writein", "Where the card goes:"),
        ("TELL A BROTHER", "Because another man can see marks on you that you can't see on yourself: read him the sentence and ask which of the four he'd say is faintest on you, and let him finish before you answer.", "plain"),
        ("CARRY THIS", "A mark is what's left on you by what you've done over and over. Nobody gets a callus from thinking about a shovel.", "carry"),
    ],
    "13": [
        ("NAME IT", "Because a man can go thirty years without noticing there's no one to call: say out loud, \"If I fell tonight, the man I could call is ___,\" and if the blank is empty or it's your wife's name, you know what this chapter is for.", "plain"),
        ("DO THIS WEEK", "Because a brother has to be asked and almost never volunteers: pick the man and say the sentence to him before Tuesday, \"I'm trying to be a better man and I don't have a brother; would you talk with me twenty minutes a week for three months?\" and set the day and time before you hang up.", "writein", "The man, the day, the time:"),
        ("FIND A BROTHER", "Because this week you may not have one to tell, the third line changes: if you do have a brother, tell him about the twenty minutes and start; if you don't, the asking is the whole job, and it's supposed to feel awkward.", "plain"),
        ("CARRY THIS", "Twenty minutes. One man. Once a week. Same time. Three questions and a prayer: What happened? What's heavy? What's next?", "carry"),
    ],
    "14": [
        ("NAME IT", "Because the man ahead of you is usually already in your life and unasked: say his name, the one about twenty years ahead you've never asked anything real; and if you're the older man, say the name of the young man you've watched and never spoken to.", "plain"),
        ("DO THIS WEEK", "Because the chain gets picked up one specific question at a time: if you're the younger man, ask him one question before Tuesday, in person or by phone; if you're the older man, walk across the parking lot and give one young man something to say yes to, a breakfast or a job or a call.", "writein", "The name, and the ask:"),
        ("ASK THE MAN", "Because this week the brother isn't the point, the third line changes: don't tell a brother about the man ahead of you, ask the man himself, then do what he says and go back and tell him how it went.", "plain"),
        ("CARRY THIS", "There's a man twenty years ahead of you standing in a parking lot with his hands in his pockets, waiting to be asked. Walk over.", "carry"),
    ],
    "15": [
        ("NAME IT", "Because the honest sentence is the whole distance between wasting away and being forgiven: say the word about yourself, to God, out loud and specifically, \"I sinned, I ___,\" and not \"I struggle with.\"", "plain"),
        ("DO THIS WEEK", "Because confession works as a habit and not as a crisis: every night this week, before sleep, take two minutes to name the day's sins to God by name and then thank Him for the forgiveness that's already yours in Christ, and notice what happens to the shame.", "writein", "Tonight's two minutes:"),
        ("TELL A BROTHER", "Because sin can't survive being said to a man who doesn't leave: confess one of them to him, to his face or on the phone, and let him pray for you.", "plain"),
        ("CARRY THIS", "You've been fixing the wrong thing. The problem inside has a name, and the name has a cure, and the cure has been paid for.", "carry"),
    ],
    "33": [
        ("NAME IT", "Because a man who builds in the dark can start to resent the dark: say three things you're building that nobody sees, and then say honestly whether you've been resenting the silence or building for the crowd instead.", "plain"),
        ("DO THIS WEEK", "Because the Tuesdays after a marker are what make the marker real: write your Tuesday rhythm on one card, five to ten unwitnessed things that don't move, scaled to your season, put it in your truck, and run it for seven days without telling anyone you're running it.", "writein", "What's on the card:"),
        ("TELL A BROTHER", "Because the man beside you is building unwitnessed things too and needs to hear that someone sees them: read him the card and ask him to check next week whether you kept it, then ask what he's building that nobody claps for, and tell him you see it.", "plain"),
        ("CARRY THIS", "What's built for applause is straw. What's built for the Father in the dark is gold. The slab nobody photographs is what the whole house stands on.", "carry"),
    ],
    "34": [
        ("NAME IT", "Because a man who knows how he fails at plans can build against it: say out loud which kind of man you've been, the one who writes nothing or the one who writes forty pages, and then say the one move, with a verb and a person and a day, that you already know belongs at the bottom of your page.", "plain"),
        ("DO THIS WEEK", "Because a plan that isn't written isn't going to happen: write the page, one surface, ten lines or fewer, every section above, scaled to your season, then sign it and date it and do the move at the bottom before Tuesday.", "writein", "The move (verb, person, day):"),
        ("TELL A BROTHER", "Because a plan a herald can run with is one another man has read: read him the whole page, hand him a copy, ask him to ask you about the bottom line next week and about the whole page in ninety days, and if he's writing one too, trade.", "plain"),
        ("CARRY THIS", "If it isn't written down, it isn't going to happen. A move has a verb, a person, and a day. Humans plan their course; the LORD establishes their steps.", "carry"),
    ],
    "35": [
        ("NAME IT", "Because a man needs to know both where he stands and where he's headed: say which of the men in this chapter you're closest to and which one you're becoming, out loud, and then say your season one more time, like a man who knows his garden.", "plain"),
        ("DO THIS WEEK", "Because the book only works if the page from chapter 34 gets run: do the move at the bottom of it, and then, before Tuesday, read chapter 3 again slowly and hold your week up against the four marks like a plumb line against a wall.", "writein", "The move, and when:"),
        ("BE A BROTHER", "Because you've been telling a brother for thirty-two chapters and the company grows only when someone goes first, the last closer changes: find the man at your church or your crew or your street who's standing where you stood, ask him, \"Would you talk with me twenty minutes a week?\", and pick up when he calls.", "plain"),
        ("CARRY THIS", "A real man rejects passivity, accepts responsibility, leads courageously, and expects the greater reward, God's reward. It'll be a Tuesday. Get up.", "carry"),
    ],
}


def render_one(ch, rows):
    sections = []
    for row in rows:
        if len(row) == 4:
            label, body, kind, prompt = row
            sections.append({"label": label, "body": body, "kind": kind, "prompt": prompt})
        else:
            label, body, kind = row
            sections.append({"label": label, "body": body, "kind": kind})

    label_f = load(FONT_LABEL, 8)
    body_f = load(FONT_BODY, 9.5)
    ital_f = load(FONT_ITAL, 9.5)
    carry_f = load(FONT_ITAL, 11.5)
    small_f = load(FONT_BODY, 8)

    pad_l = pt(22)
    pad_r = pt(18)
    pad_t = pt(16)
    pad_b = pt(16)
    rail_x = pt(10)
    rail_w = max(2, pt(0.65))
    inner_l = pad_l
    text_w = W - inner_l - pad_r
    label_track = 3.6
    body_lh = int(text_h(body_f) * 1.30)
    carry_lh = int(text_h(carry_f) * 1.24)
    section_gap = pt(12)
    rule_gap = pt(8)

    measure = Image.new("RGB", (W, 8000), BONE)
    md = ImageDraw.Draw(measure)

    y = pad_t
    y += text_h(small_f) + pt(10)
    measured = []
    for i, sec in enumerate(sections):
        top = y
        y += text_h(label_f) + pt(5)
        font = carry_f if sec["kind"] == "carry" else body_f
        lines = wrap(md, sec["body"], font, text_w)
        lh = carry_lh if sec["kind"] == "carry" else body_lh
        body_top = y
        y += lh * len(lines)
        writein_top = None
        if sec["kind"] == "writein":
            y += pt(8)
            writein_top = y
            y += text_h(ital_f) + pt(6) + pt(14)
        bottom = y
        measured.append((top, body_top, lines, writein_top, bottom))
        if i < len(sections) - 1:
            y += rule_gap
            y += 1
            y += section_gap

    y += pad_b
    H = y

    img = Image.new("RGB", (W, H), BONE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=RULE, width=1)
    d.rectangle([rail_x, pt(8), rail_x + rail_w, H - pt(8)], fill=RUST)
    d.text((inner_l, pad_t), f"{ch}  ·  YOUR TURN", font=small_f, fill=RUST)

    for i, sec in enumerate(sections):
        top, body_top, lines, writein_top, bottom = measured[i]
        tick_y = top + text_h(label_f) // 2
        tick_h = max(3, pt(2.2))
        tick_w = max(6, pt(4.5))
        d.rectangle(
            [rail_x - 1, tick_y - tick_h // 2, rail_x + tick_w, tick_y + tick_h // 2 + 1],
            fill=RUST,
        )
        draw_label(d, sec["label"], (inner_l, top), label_f, RUST, label_track)

        font = carry_f if sec["kind"] == "carry" else body_f
        lh = carry_lh if sec["kind"] == "carry" else body_lh
        yy = body_top
        for line in lines:
            d.text((inner_l, yy), line, font=font, fill=INK)
            yy += lh

        if sec["kind"] == "writein":
            d.text((inner_l, writein_top), sec["prompt"], font=ital_f, fill=INK_SOFT)
            line_y = writein_top + text_h(ital_f) + pt(10)
            d.line([(inner_l, line_y), (W - pad_r, line_y)], fill=RULE, width=1)

        if i < len(sections) - 1 and sec["kind"] != "writein":
            rule_y = bottom + rule_gap
            d.line([(inner_l, rule_y), (W - pad_r, rule_y)], fill=RULE, width=1)

    # Carry band under last section
    last_top = measured[-1][0] - pt(6)
    d.rectangle([1, last_top, W - 2, H - 2], fill=CARRY_BAND)
    d.rectangle([rail_x, last_top, rail_x + rail_w, H - pt(8)], fill=RUST)
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

    png = OUT / f"{ch}-closer-box.png"
    img.save(png, "PNG", dpi=(PPI, PPI))
    print(f"{ch} {img.size} -> {png}")
    return png, img.size


def main():
    for ch, rows in CHAPTERS.items():
        render_one(ch, rows)
    note = OUT / "FLOW-CONTRAST-PASS-2026-09-07.md"
    note.write_text(
        "\n".join(
            [
                "# FLOW contrast pass — Ash 2026-09-07",
                "",
                "Reed full FLOW signed. Packets HOLD. No dump to Aaron.",
                "",
                "## Rules applied",
                "- Gold accent on navy only (man-plan THIS WEEK panel).",
                "- No gold-on-bone body or accent type.",
                "- Closer hairlines darkened RULE=(120,110,96).",
                "- Body ink on bone; carry band quiet wash.",
                "- Closer copy = Reed FLOW-signed (Because why framing).",
                "- Branch third beats kept: 13 Find a brother / 14 Ask the man / 35 Be a brother.",
                "",
                "## Files updated",
                "- `01` `02` `03` `13` `14` `15` `33` `34` `35` closer boxes",
                "- `34-man-plan.png` (earlier: navy THIS WEEK + gold; dark write lines)",
                "- `03-four-marks.png` left (no gold-on-bone)",
                "",
                "Cover folders untouched. Ready for rebind.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"note {note}")


if __name__ == "__main__":
    main()
