#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news infographic (1024x1024 PNG).

Reads nothing but the STORIES list below (researched from Reuters/AP/AFP
and other reporting of Wednesday 18 November 2026) and renders it with
Pillow + DejaVu. Run: python3 tools/draw.py  ->  entry.png
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (244, 239, 230)
NAVY = (19, 35, 63)
INK = (20, 33, 61)
MUTED = (74, 74, 74)
CARD = (255, 255, 255)
BORDER = (216, 210, 196)
GOLD = (232, 181, 74)
FOOT = (90, 90, 90)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
f_title = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 54)
f_kicker = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 22)
f_sub = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 22)
f_tag = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 20)
f_head = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 29)
f_body = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 20)
f_foot = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 18)

STORIES = [
    ("DIPLOMACY  ·  CHINA", (31, 111, 139),
     "Xi and Putin meet in Shenzhen",
     "Trump lands for Thursday's trilateral summit; Ukraine and Iran top the agenda."),
    ("GULF  ·  MIDDLE EAST", (179, 57, 57),
     "U.S. strikes Iran; Gulf hit back",
     "U.S. jets hit a missile site on Qeshm Island; Iran fired on Bahrain and Kuwait."),
    ("WAR  ·  UKRAINE", (46, 107, 52),
     "Kerch Bridge hit again",
     "Ukraine strikes the Crimea link for a second day; part of the road span collapses."),
    ("POLITICS  ·  U.S.A.", (91, 76, 173),
     "Democrats take the Senate, 56-44",
     "Peltola beats Sullivan in Alaska \u2014 the final race, and the ninth Democratic flip."),
    ("TECH  ·  MARKETS", (14, 124, 102),
     "Nvidia's record $115.8bn quarter",
     "Revenue doubled year on year; the board says no to Huang's return as CEO."),
    ("WEATHER  ·  ASIA", (199, 123, 33),
     "Cyclone Akvan bears down on India",
     "Severe storm in the Bay of Bengal; landfall on the Andhra coast expected Friday."),
]

TICKER = ("Also: U.S. loses measles-free status after 26 years  \u00b7  "
          "Ebola in DR Congo passes 11,000 cases  \u00b7  "
          "India\u2013Japan 2+2 talks open in Tokyo")


def wrap(draw, text, font, width):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=width))
    return lines


def text_w(draw, text, font):
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def draw_card(draw, x, y, w, h, tag, color, head, body):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                           outline=BORDER, width=2)
    draw.rounded_rectangle([x, y, x + w, y + 10], radius=5, fill=color)
    draw.rectangle([x, y + 5, x + w, y + 10], fill=color)
    pad = 20
    draw.text((x + pad, y + 22), tag, font=f_tag, fill=color)
    # headline, up to 2 lines
    max_chars = 26
    hl = wrap(draw, head, f_head, max_chars)[:2]
    ty = y + 54
    for line in hl:
        draw.text((x + pad, ty), line, font=f_head, fill=INK)
        ty += 36
    # summary, up to 3 lines
    bl = wrap(draw, body, f_body, 46)[:3]
    by = ty + 8
    for line in bl:
        draw.text((x + pad, by), line, font=f_body, fill=MUTED)
        by += 26


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    # header band
    draw.rectangle([0, 0, W, 168], fill=NAVY)
    draw.rectangle([0, 168, W, 174], fill=GOLD)
    draw.text((24, 18), "THE WORLD IN ONE DAY", font=f_kicker, fill=GOLD)
    draw.text((24, 48), "Wednesday 18 November 2026",
              font=f_title, fill=(255, 255, 255))
    draw.text((24, 118), "Six stories that defined the day \u2014 from Shenzhen to the Gulf, Kyiv to Alaska.",
              font=f_sub, fill=(201, 210, 224))
    # grid: 2 cols x 3 rows
    margin, gutter = 24, 20
    cw = (W - 2 * margin - gutter) // 2
    ch, row_gap = 228, 14
    top = 194
    for i, (tag, color, head, body) in enumerate(STORIES):
        cx = margin + (i % 2) * (cw + gutter)
        cy = top + (i // 2) * (ch + row_gap)
        draw_card(draw, cx, cy, cw, ch, tag, color, head, body)
    # footer ticker, wrapped to fit the width, then the sources line
    fy = top + 3 * ch + 2 * row_gap + 14
    draw.line([margin, fy, W - margin, fy], fill=BORDER, width=2)
    tick_lines = wrap(draw, TICKER, f_foot, 108)[:2]
    ty = fy + 12
    for line in tick_lines:
        draw.text((margin, ty), line, font=f_foot, fill=FOOT)
        ty += 24
    draw.text((margin, ty + 6), "Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 The Hindu \u00b7 Al Jazeera  \u2014  events of 18 Nov 2026, any time zone",
              font=f_foot, fill=FOOT)
    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
