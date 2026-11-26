# generate_image.py — renders entry.png (1024x1024) from scratch with Pillow.
# Design (deliberately different from the v2 newspaper front page):
# a dark "ONE DAY ON EARTH" timeline infographic: a burnt-orange hero panel
# for the Cairo tanker fire, a wide summit card, then Gulf / Ukraine / Europe
# cards, and a bottom strip for SpaceX, the Ibiza tanker and Bangkok.
# All facts are from 26 Nov 2026 reporting (see README sources).
# Run:  python3 generate_image.py   (rewrites entry.png in place)
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (13, 30, 46)          # deep navy
PANEL = (22, 46, 68)       # lighter navy panel
CARD = (244, 241, 232)     # warm off-white card
INK = (16, 32, 48)
GOLD = (232, 178, 74)
ORANGE = (194, 65, 12)
ORANGE_D = (124, 45, 18)
TEAL = (45, 170, 165)
RED = (178, 34, 34)
MUTED = (168, 188, 205)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, lh):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += lh
    return y


def card(draw, box, fill=CARD, outline=None):
    draw.rounded_rectangle(box, radius=14, fill=fill,
                           outline=outline or (0, 0, 0, 0), width=2)


def kicker_headline(draw, x, y, max_w, kicker, kcolor, headline, hsize=30):
    draw.text((x, y), kicker, font=font(SANS_B, 17), fill=kcolor)
    y += 26
    y = para(draw, x, y, headline, font(SERIF_B, hsize), INK, max_w, hsize + 6)
    return y


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- header -------------------------------------------------------------
d.text((32, 26), "THURSDAY  •  26 NOVEMBER 2026  •  THE WORLD IN 24 HOURS",
       font=font(SANS_B, 19), fill=GOLD)
d.text((32, 56), "ONE DAY ON EARTH", font=font(SERIF_B, 62), fill=(255, 255, 255))
d.text((32, 126), "Seven stories from one Thursday — trade, fire, war and a first summit.",
       font=font(SANS, 21), fill=MUTED)
d.line([(32, 158), (992, 158)], fill=GOLD, width=3)

# ---- hero: Cairo (left, tall orange panel) ------------------------------
card(d, [32, 178, 392, 578], fill=ORANGE)
d.text((56, 196), "EGYPT  •  CAIRO", font=font(SANS_B, 18), fill=(255, 220, 180))
d.text((56, 224), "31", font=font(SERIF_B, 120), fill=(255, 255, 255))
d.text((56, 344), "KILLED IN THE\nTANKER FIRE", font=font(SERIF_B, 28),
       fill=(255, 255, 255))
para(d, 56, 420,
     "A fuel tanker overturned and burst into flames on Cairo's Ring Road "
     "in Giza. At least 31 people died and about 21 were injured; the "
     "driver was detained.",
     font(SANS, 19), (255, 235, 210), 304, 26)

# ---- right column: summit (wide) + trade --------------------------------
card(d, [412, 178, 992, 368])
kicker_headline(d, 436, 196, 532, "DIPLOMACY  •  FIRST TRILATERAL SUMMIT", RED,
                "Trump, Xi and Putin meet face to face", 29)
para(d, 436, 296,
     "The three leaders meet for about 80 minutes and endorse a declaration "
     "toward peace — the first time they have sat down together.",
     font(SANS, 19), (70, 70, 70), 532, 25)

card(d, [412, 388, 992, 578])
y = kicker_headline(d, 436, 406, 532, "TRADE  •  WASHINGTON", RED,
                    "US proposes tariffs on 14 partners", 29)
para(d, 436, y + 8,
     "Washington targets China, the EU, India and Japan over industrial "
     "overcapacity. Rates are proposed, not final.",
     font(SANS, 19), (70, 70, 70), 532, 25)

# ---- middle row: Gulf / Ukraine / Europe ---------------------------------
mid = [
    ("GULF  •  MIDDLE EAST", "Attacks spread across the Gulf",
     "Houthi forces strike Saudi ports and the Ras Tanura refinery. A drone "
     "attack in Kuwait kills two Italians; Iran denies any role."),
    ("UKRAINE  •  WAR", "Kyiv and a Russian airbase hit",
     "Russian ballistic missiles strike Kyiv; Ukraine says it hit five jets "
     "at the Savasleyka airfield."),
    ("EUROPE  •  BRUSSELS", "A €2 trillion budget fight",
     "EU leaders clash over the next long-term budget and Ukraine funding. "
     "Spain's Pablo Hernandez de Cos is picked to lead the ECB."),
]
x = 32
for kicker, head, body in mid:
    card(d, [x, 598, x + 304, 852])
    y = kicker_headline(d, x + 20, 616, 264, kicker, RED, head, 26)
    para(d, x + 20, y + 8, body, font(SANS, 17), (70, 70, 70), 264, 23)
    x += 328

# ---- bottom strip: space / sea / Bangkok ---------------------------------
strip = [
    ("SPACE", "FCC clears SpaceX's million-satellite plan for orbital data centres."),
    ("AT SEA  •  IBIZA", "Diesel tanker Med Emre capsizes off Ibiza; one crew member dies."),
    ("THAILAND  •  BANGKOK", "Blast and fire at a Bangkok oil facility injure at least nine."),
]
x = 32
for kicker, body in strip:
    card(d, [x, 858, x + 304, 962], fill=PANEL)
    d.text((x + 20, 872), kicker, font=font(SANS_B, 16), fill=GOLD)
    para(d, x + 20, 898, body, font(SANS, 17), (235, 240, 244), 264, 22)
    x += 328

d.text((32, 978), "One day. Seven stories. — Thursday 26 November 2026.",
       font=font(SANS, 18), fill=MUTED)
d.text((700, 978), "26 NOV 2026", font=font(SANS_B, 18), fill=GOLD)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
