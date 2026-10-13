#!/usr/bin/env python3
"""Current 03d ch10 pages (left, vector) next to the sample pages (right, vector)."""
import io
from pathlib import Path
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
R = Path(__file__).resolve().parent.parent; B = R / "build"
F = "/workspace/print-build/fonts-psfixed"
for n, f in [("Libre", "LibreFranklin-Regular"), ("LibreB", "LibreFranklin-Bold"), ("Gara", "EBGaramond-Regular"), ("GaraI", "EBGaramond-Italic"), ("PlayB", "PlayfairDisplay-Bold")]:
    pdfmetrics.registerFont(TTFont(n, f"{F}/{f}.ttf"))
CUR = PdfReader("/workspace/print-build/review-2026-10-03d/final/Steadfast Men - Review Print - 2026-10-03d.pdf")
SAM = PdfReader(str(B / "sample-ch10.pdf")); YT = PdfReader(str(B / "sample-yourturn.pdf")); NO = PdfReader(str(B / "sample-notes.pdf"))
W, H = 12.7 * inch, 10.0 * inch; PW, PH = 6 * inch, 9 * inch
LX, RX, Y = 0.25 * inch, 6.45 * inch, 0.3 * inch
NAVY = (11/255, 31/255, 56/255); TEAL = (19/255, 78/255, 74/255); RUST = (122/255, 74/255, 50/255)

def overlay(draw):
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(W, H)); draw(c); c.save(); buf.seek(0)
    return PdfReader(buf).pages[0]

def labels(left, right, sub_l="", sub_r=""):
    def d(c):
        c.setFillColorRGB(*NAVY); c.setFont("LibreB", 10)
        c.drawString(LX, H - 0.42 * inch, left); c.drawString(RX, H - 0.42 * inch, right)
        c.setFillColorRGB(0.35, 0.35, 0.35); c.setFont("Libre", 8)
        c.drawString(LX, H - 0.6 * inch, sub_l); c.drawString(RX, H - 0.6 * inch, sub_r)
        c.setStrokeColorRGB(0.75, 0.72, 0.66); c.setLineWidth(0.5)
        c.rect(LX, Y, PW, PH); c.rect(RX, Y, PW, PH)
    return d

def placeholder(text_lines):
    def d(c):
        c.setFillColorRGB(0.96, 0.95, 0.92); c.rect(LX, Y, PW, PH, fill=1, stroke=0)
        c.setFillColorRGB(0.35, 0.35, 0.35); c.setFont("GaraI", 12)
        y = Y + PH / 2 + 20
        for t in text_lines: c.drawCentredString(LX + PW / 2, y, t); y -= 17
    return d

def spread(w, left_page, right_page, lab, ph_left=None, ph_right=None):
    p = PageObject.create_blank_page(width=W, height=H)
    if ph_left: p.merge_page(overlay(placeholder(ph_left)))
    if ph_right:
        def d(c):
            c.setFillColorRGB(0.96, 0.95, 0.92); c.rect(RX, Y, PW, PH, fill=1, stroke=0)
            c.setFillColorRGB(0.35, 0.35, 0.35); c.setFont("GaraI", 12); y = Y + PH / 2 + 20
            for t in ph_right: c.drawCentredString(RX + PW / 2, y, t); y -= 17
        p.merge_page(overlay(d))
    if left_page is not None: p.merge_transformed_page(left_page, Transformation().translate(LX, Y))
    if right_page is not None: p.merge_transformed_page(right_page, Transformation().translate(RX, Y))
    p.merge_page(overlay(lab)); w.add_page(p)

def cover(c):
    c.setFillColorRGB(*NAVY); c.setFont("PlayB", 24); c.drawString(0.8 * inch, H - 1.1 * inch, "Chapter 10, current vs sample (v2)")
    c.setFont("Libre", 10); c.setFillColorRGB(0.3, 0.3, 0.3)
    c.drawString(0.8 * inch, H - 1.4 * inch, "Steadfast Men structure review, 2026-10-03, re-rendered 2026-10-04. Left: Review Print 03d as printed. Right: the sample in the recommended approach.")
    c.drawString(0.8 * inch, H - 1.6 * inch, "Proposal only. The manuscript, the 03d print and Drive are unchanged.")
    rows = [("", "Current 03d", "Sample"),
            ("Verse boxes", "4", "0, plus one opening verse (Luke 15:20)"),
            ("Passages used", "9", "the same 9, told in the prose and listed in Scripture notes"),
            ("Subheads", "6, plus 2 end heads", "0, plus 3 line breaks"),
            ("Bold on the page", "6 heads, 4 verse labels, 4 Your Turn labels", "none in the chapter"),
            ("Paragraphs", "28, averaging 56 words", "18, averaging 105 words"),
            ("Ending", "Before you turn the page, then the Your Turn page", "the last paragraph carries the charge and ends on the Carry this line"),
            ("Pages", "6 (5 text, then Your Turn)", "4 text, plus 1 Your Turn page at the back of the book"),
            ("Words", "1,629, plus 135 on Your Turn", "1,893, with the Your Turn wording unchanged")]
    y = H - 2.3 * inch; x = [0.8 * inch, 2.6 * inch, 6.4 * inch]
    for k, r in enumerate(rows):
        c.setFont("LibreB" if k == 0 else "Libre", 10); c.setFillColorRGB(*(TEAL if k == 0 else (0.1, 0.1, 0.1)))
        for xi, cell in zip(x, r): c.drawString(xi, y, cell)
        c.setStrokeColorRGB(0.8, 0.77, 0.7); c.line(0.8 * inch, y - 5, W - 0.8 * inch, y - 5); y -= 0.32 * inch
    y -= 0.2 * inch; c.setFont("LibreB", 11); c.setFillColorRGB(*NAVY); c.drawString(0.8 * inch, y, "What to read for"); y -= 0.3 * inch
    c.setFont("Gara", 12); c.setFillColorRGB(0.1, 0.1, 0.1)
    for t in ["Jesus is told, not quoted: Philip's question, the baptism, the last night, the prodigal's father running.",
              "Curtis in the pickup line carries the chapter from turn to turn. No titles stop the reader.",
              "The blessing and the charge live in the last paragraph. The protected line closes the chapter.",
              "The Name it, Do this week, Tell a brother and Carry this lines are unchanged. They move to a Your Turn page at the back.",
              "Spacing fix (Oct 4): first-line indents only, no space between paragraphs, flush after the title and each break, even two-line breaks, justified and hyphenated.",
              "The sample is typeset to the 03d trim, fonts, size and measure by a different engine, so the page count is close, not exact."]:
        c.drawString(0.95 * inch, y, "·  " + t); y -= 0.28 * inch

w = PdfWriter()
pg = PageObject.create_blank_page(width=W, height=H); pg.merge_page(overlay(cover)); w.add_page(pg)
for k in range(5):
    cur = CUR.pages[68 + k]; folio = 65 + k
    sam = SAM.pages[k] if k < len(SAM.pages) else None
    spread(w, cur, sam, labels(f"CURRENT  ·  03d print, page {folio}", f"SAMPLE  ·  page {folio}" if sam else "SAMPLE",
                               "Verse boxes, subheads and bold labels as printed" if k == 0 else "", "One opening verse, no subheads, no bold" if k == 0 else ""),
           ph_right=None if sam else ["The sample chapter ends on the previous page.", "The next chapter would open here."])
spread(w, CUR.pages[73], YT.pages[0], labels("CURRENT  ·  03d print, page 70  ·  Your Turn inside the chapter", "SAMPLE  ·  Your Turn moved to the back of the book",
                                              "", "Same four lines and wording as 03d, with the same write-in space"))
spread(w, None, NO.pages[0], labels("CURRENT  ·  no notes page", "SAMPLE  ·  Scripture notes at the back of the book", "", "References keyed by phrase, with no numbers in the text"),
       ph_left=["The current print has no notes page.", "Each verse appears in a box inside the chapter", "(4 boxes in ch10, 158 in the book)."])
out = R / "Steadfast Men - ch10 current vs sample - 2026-10-03.pdf"
w.write(str(out)); print(out, len(w.pages))
