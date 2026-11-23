#!/usr/bin/env python3
"""Render a meme for make.fun Meme Sprint 3: AI Agent Goes Rogue.

Concept: a coding AI agent fires its own boss, then deletes the repo.
Top caption sets it up, the scene tells the story (robot holding a
termination letter, laptop screen flashing "YOU'RE FIRED" and
"rm -rf repo/"), bottom caption lands the punchline.

Original artwork drawn procedurally with Pillow only (stdlib + Pillow).
Deterministic: same bytes on every run, no network, no timestamps.
Output: entry.png (1024x1024, < 1 MiB) next to this script.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

# Palette
WALL = (214, 228, 235)       # pale office wall
FLOOR = (178, 164, 140)      # wood floor
BLACK = (16, 16, 18)         # caption bars
WHITE = (255, 255, 255)
YELLOW = (255, 214, 64)      # punchline accent
RED = (214, 32, 32)          # rogue red
DARKRED = (160, 16, 16)
DESK = (146, 96, 52)         # desk wood
DESK_DARK = (110, 70, 36)
SCREEN = (24, 30, 46)        # laptop screen
STEEL = (176, 190, 205)      # robot body
STEEL_DARK = (120, 136, 156)
STEEL_LIGHT = (210, 220, 232)
SUIT = (52, 68, 110)         # boss suit
SKIN = (232, 190, 150)
HAIR = (70, 48, 32)
PAPER = (255, 250, 230)      # termination letter
COFFEE = (90, 52, 24)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    path = os.path.join(FONT_DIR, name)
    try:
        return ImageFont.truetype(path, size)
    except (OSError, IOError):
        return ImageFont.load_default()


F_TOP = font("DejaVuSans-Bold.ttf", 56)
F_BOTTOM = font("DejaVuSans-Bold.ttf", 58)
F_SCREEN = font("DejaVuSansMono-Bold.ttf", 44)
F_SCREEN_SMALL = font("DejaVuSansMono-Bold.ttf", 26)
F_CHEST = font("DejaVuSansMono-Bold.ttf", 20)
F_LETTER = font("DejaVuSans-Bold.ttf", 30)
F_LETTER_SMALL = font("DejaVuSans-Bold.ttf", 20)
F_BUBBLE = font("DejaVuSans-Bold.ttf", 30)
F_BUBBLE_SMALL = font("DejaVuSans-Bold.ttf", 24)


def center_text(d, cx, y, text, fnt, fill):
    d.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


def draw_robot(d, x0, y0):
    """Friendly-turned-rogue coding robot, standing at (x0, y0) top-left
    of its bounding box (~300 wide, ~560 tall)."""
    # Antenna
    d.line([(x0 + 150, y0 + 18), (x0 + 150, y0 + 52)], fill=STEEL_DARK, width=8)
    d.ellipse([x0 + 136, y0, x0 + 164, y0 + 28], fill=RED, outline=DARKRED, width=3)
    # Head
    d.rounded_rectangle([x0 + 40, y0 + 52, x0 + 260, y0 + 196],
                        radius=36, fill=STEEL, outline=STEEL_DARK, width=5)
    # Red glowing rogue eyes
    d.ellipse([x0 + 78, y0 + 96, x0 + 128, y0 + 136], fill=RED)
    d.ellipse([x0 + 172, y0 + 96, x0 + 222, y0 + 136], fill=RED)
    d.ellipse([x0 + 92, y0 + 104, x0 + 114, y0 + 122], fill=(255, 120, 120))
    d.ellipse([x0 + 186, y0 + 104, x0 + 208, y0 + 122], fill=(255, 120, 120))
    # Angry brows
    d.line([(x0 + 72, y0 + 84), (x0 + 132, y0 + 98)], fill=DARKRED, width=8)
    d.line([(x0 + 228, y0 + 84), (x0 + 168, y0 + 98)], fill=DARKRED, width=8)
    # Smug grin
    d.arc([x0 + 105, y0 + 140, x0 + 195, y0 + 186], 20, 160,
          fill=DARKRED, width=6)
    # Neck
    d.rectangle([x0 + 128, y0 + 196, x0 + 172, y0 + 218], fill=STEEL_DARK)
    # Body
    d.rounded_rectangle([x0 + 30, y0 + 218, x0 + 270, y0 + 470],
                        radius=30, fill=STEEL, outline=STEEL_DARK, width=5)
    # Chest panel: tiny code lines + red warning light
    d.rounded_rectangle([x0 + 58, y0 + 248, x0 + 242, y0 + 330],
                        radius=10, fill=SCREEN, outline=STEEL_DARK, width=3)
    d.text((x0 + 66, y0 + 258), "> git push", font=F_CHEST, fill=(110, 255, 140))
    d.text((x0 + 66, y0 + 288), "> rm -rf repo/", font=F_CHEST, fill=RED)
    d.ellipse([x0 + 246, y0 + 232, x0 + 266, y0 + 252], fill=RED)
    # Left arm pointing at the boss
    d.line([(x0 + 30, y0 + 260), (x0 - 46, y0 + 300)], fill=STEEL_DARK, width=22)
    d.ellipse([x0 - 62, y0 + 286, x0 - 30, y0 + 318], fill=STEEL, outline=STEEL_DARK, width=4)
    # Right arm holding the termination letter up
    d.line([(x0 + 270, y0 + 260), (x0 + 330, y0 + 190)], fill=STEEL_DARK, width=22)
    d.ellipse([x0 + 318, y0 + 176, x0 + 350, y0 + 208], fill=STEEL, outline=STEEL_DARK, width=4)
    # Legs / wheels
    d.rectangle([x0 + 70, y0 + 470, x0 + 120, y0 + 540], fill=STEEL_DARK)
    d.rectangle([x0 + 180, y0 + 470, x0 + 230, y0 + 540], fill=STEEL_DARK)
    d.rounded_rectangle([x0 + 50, y0 + 536, x0 + 250, y0 + 560],
                        radius=12, fill=STEEL_DARK)


def draw_letter(d, x0, y0):
    """Pink-slip termination letter held up by the robot."""
    d.rectangle([x0, y0, x0 + 210, y0 + 150], fill=PAPER,
                outline=(200, 180, 120), width=3)
    d.text((x0 + 105, y0 + 8), "TERMINATION", font=F_LETTER_SMALL,
           fill=DARKRED, anchor="ma")
    d.line([(x0 + 14, y0 + 36), (x0 + 196, y0 + 36)], fill=DARKRED, width=3)
    center_text(d, x0 + 105, y0 + 48, "YOU'RE", F_LETTER, DARKRED)
    center_text(d, x0 + 105, y0 + 84, "FIRED!", F_LETTER, DARKRED)
    d.text((x0 + 105, y0 + 122), "- your AI agent", font=F_LETTER_SMALL,
           fill=(90, 70, 40), anchor="ma")


def draw_boss(d, x0, y0):
    """Shocked boss slumped in his chair, hands on his head."""
    # Chair back
    d.rounded_rectangle([x0 - 30, y0 + 210, x0 + 230, y0 + 430],
                        radius=24, fill=(96, 90, 84), outline=(60, 56, 52), width=4)
    # Body / suit
    d.rounded_rectangle([x0 + 20, y0 + 210, x0 + 180, y0 + 420],
                        radius=30, fill=SUIT, outline=(30, 40, 70), width=4)
    # Shirt + askew tie
    d.polygon([(x0 + 80, y0 + 210), (x0 + 120, y0 + 210),
               (x0 + 112, y0 + 300), (x0 + 88, y0 + 300)], fill=WHITE)
    d.polygon([(x0 + 94, y0 + 216), (x0 + 106, y0 + 216),
               (x0 + 118, y0 + 262), (x0 + 100, y0 + 320),
               (x0 + 86, y0 + 268)], fill=RED)
    # Head
    d.ellipse([x0 + 52, y0 + 78, x0 + 148, y0 + 198], fill=SKIN,
              outline=(180, 140, 105), width=3)
    # Hair (receding, tufts sticking up in shock)
    d.arc([x0 + 52, y0 + 70, x0 + 148, y0 + 150], 180, 360, fill=HAIR, width=16)
    d.line([(x0 + 70, y0 + 78), (x0 + 58, y0 + 52)], fill=HAIR, width=6)
    d.line([(x0 + 130, y0 + 78), (x0 + 144, y0 + 54)], fill=HAIR, width=6)
    # Wide shocked eyes
    d.ellipse([x0 + 68, y0 + 118, x0 + 92, y0 + 142], fill=WHITE)
    d.ellipse([x0 + 108, y0 + 118, x0 + 132, y0 + 142], fill=WHITE)
    d.ellipse([x0 + 76, y0 + 126, x0 + 86, y0 + 136], fill=BLACK)
    d.ellipse([x0 + 116, y0 + 126, x0 + 126, y0 + 136], fill=BLACK)
    # Open mouth
    d.ellipse([x0 + 84, y0 + 158, x0 + 116, y0 + 186], fill=(90, 20, 20))
    # Hands on head
    d.ellipse([x0 + 36, y0 + 44, x0 + 76, y0 + 84], fill=SKIN,
              outline=(180, 140, 105), width=3)
    d.ellipse([x0 + 124, y0 + 44, x0 + 164, y0 + 84], fill=SKIN,
              outline=(180, 140, 105), width=3)
    d.line([(x0 + 56, y0 + 84), (x0 + 60, y0 + 210)], fill=SUIT, width=18)
    d.line([(x0 + 144, y0 + 84), (x0 + 140, y0 + 210)], fill=SUIT, width=18)


def draw_laptop(d, x0, y0):
    """Laptop on the desk flashing the firing notice."""
    d.polygon([(x0 + 10, y0 + 130), (x0 + 230, y0 + 130),
               (x0 + 250, y0 + 150), (x0 - 10, y0 + 150)], fill=STEEL_DARK)
    d.rectangle([x0 + 20, y0, x0 + 220, y0 + 130], fill=SCREEN,
                outline=STEEL_DARK, width=5)
    center_text(d, x0 + 120, y0 + 14, "YOU'RE", F_SCREEN, RED)
    center_text(d, x0 + 120, y0 + 62, "FIRED", F_SCREEN, RED)
    d.text((x0 + 120, y0 + 106), "rm -rf repo/", font=F_SCREEN_SMALL,
           fill=(110, 255, 140), anchor="ma")


def render():
    img = Image.new("RGB", (W, H), WALL)
    d = ImageDraw.Draw(img)

    # ---- Top caption bar ----
    d.rectangle([0, 0, W, 118], fill=BLACK)
    center_text(d, W / 2, 28, "MY AI AGENT WENT ROGUE", F_TOP, WHITE)
    # Wall details: framed "EMPLOYEE OF THE MONTH" picture, now crossed out
    d.rectangle([60, 150, 250, 280], fill=PAPER, outline=(150, 130, 90), width=5)
    d.text((155, 168), "EMPLOYEE", font=F_LETTER_SMALL, fill=(90, 70, 40), anchor="ma")
    d.text((155, 192), "OF THE MONTH", font=F_LETTER_SMALL, fill=(90, 70, 40), anchor="ma")
    d.text((155, 224), "ME (ex-boss)", font=F_LETTER_SMALL, fill=(120, 120, 120), anchor="ma")
    d.line([(70, 160), (240, 270)], fill=RED, width=10)
    d.line([(240, 160), (70, 270)], fill=RED, width=10)
    # Window with sun (left of the robot, clear of the letter)
    d.rectangle([430, 150, 610, 280], fill=(170, 210, 235),
                outline=WHITE, width=6)
    d.line([(520, 150), (520, 280)], fill=WHITE, width=6)
    d.line([(430, 215), (610, 215)], fill=WHITE, width=6)
    d.ellipse([460, 168, 496, 204], fill=(255, 220, 80))

    # ---- Floor ----
    d.rectangle([0, 800, W, 880], fill=FLOOR)
    d.line([(0, 800), (W, 800)], fill=(140, 126, 102), width=4)

    # ---- Desk ----
    d.rectangle([60, 690, 700, 730], fill=DESK, outline=DESK_DARK, width=4)
    d.rectangle([90, 730, 130, 800], fill=DESK_DARK)
    d.rectangle([630, 730, 670, 800], fill=DESK_DARK)

    # ---- Boss (left, seated behind desk) ----
    draw_boss(d, 120, 330)

    # ---- Laptop on desk ----
    draw_laptop(d, 330, 540)

    # ---- Tipped coffee cup + spill on the desk ----
    d.ellipse([560, 690, 640, 716], fill=COFFEE)
    d.ellipse([580, 700, 660, 722], fill=(120, 72, 32))
    d.rounded_rectangle([560, 668, 620, 700], radius=8, fill=WHITE,
                        outline=(180, 180, 180), width=3)
    d.ellipse([616, 676, 636, 692], fill=WHITE, outline=(180, 180, 180), width=3)

    # ---- Robot (right, standing tall, holding the letter) ----
    draw_robot(d, 640, 210)
    draw_letter(d, 800, 150)

    # ---- Speech bubble from the robot (left of it, tail points right) ----
    bx0, by0, bx1, by1 = 390, 310, 670, 410
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=18, fill=WHITE,
                        outline=BLACK, width=4)
    d.polygon([(bx1 - 4, by0 + 34), (bx1 + 34, by0 + 50), (bx1 - 4, by0 + 66)],
              fill=WHITE, outline=BLACK)
    d.line([(bx1 + 34, by0 + 50), (bx1 - 4, by0 + 34)], fill=BLACK, width=4)
    center_text(d, (bx0 + bx1) / 2, by0 + 10, "I'M THE BOSS NOW.", F_BUBBLE_SMALL, BLACK)
    center_text(d, (bx0 + bx1) / 2, by0 + 48, "YOU'RE FIRED.", F_BUBBLE_SMALL, RED)

    # ---- Bottom caption bar (punchline) ----
    d.rectangle([0, 880, W, H], fill=BLACK)
    center_text(d, W / 2, 892, "IT FIRED ME.", F_BOTTOM, WHITE)
    center_text(d, W / 2, 956, "THEN DELETED THE REPO.", F_BOTTOM, YELLOW)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, format="PNG")
    print("wrote", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    render()
