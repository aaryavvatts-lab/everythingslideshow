#!/usr/bin/env python3
"""contact_sheet.py - tile slide images into one numbered contact sheet.

Usage:
  python3 contact_sheet.py OUT.png s01.png s02.png ... [--cols 3] [--width 1800]
  python3 contact_sheet.py OUT.png DIR_OF_PNGS            [--cols 3]

Why: reading 20 separate screenshots is slow and hides rhythm problems. One sheet shows
whether the deck looks like one family, where the density spikes, and which slides repeat a layout.
Needs Pillow (pip install pillow).
"""
import os
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("contact_sheet: Pillow missing. Run: pip3 install pillow")


def main(argv):
    cols, width = 3, 1800
    paths, i = [], 1
    out = argv[0] if argv else None
    rest = argv[1:]
    while i <= len(rest):
        a = rest[i - 1]
        if a == "--cols":
            cols = int(rest[i]); i += 2; continue
        if a == "--width":
            width = int(rest[i]); i += 2; continue
        paths.append(a); i += 1
    if not out or not paths:
        sys.exit(__doc__)
    if len(paths) == 1 and os.path.isdir(paths[0]):
        d = paths[0]
        # only slide images (s01.png, s02.png ...), never a previous sheet or the output file itself
        paths = sorted(os.path.join(d, f) for f in os.listdir(d) if re.match(r"^s\d+\.png$", f, re.I))
    out_abs = os.path.abspath(out)
    paths = [p for p in paths if os.path.abspath(p) != out_abs]
    imgs = [Image.open(p).convert("RGB") for p in paths]
    if not imgs:
        sys.exit("contact_sheet: no images")
    gap = 16
    cell_w = (width - gap * (cols + 1)) // cols
    ratio = imgs[0].height / imgs[0].width
    cell_h = int(cell_w * ratio)
    rows = (len(imgs) + cols - 1) // cols
    sheet = Image.new("RGB", (width, gap + rows * (cell_h + gap + 22)), (30, 30, 34))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
    except Exception:
        font = ImageFont.load_default()
    for n, im in enumerate(imgs):
        r, c = divmod(n, cols)
        x = gap + c * (cell_w + gap)
        y = gap + r * (cell_h + gap + 22)
        sheet.paste(im.resize((cell_w, cell_h), Image.LANCZOS), (x, y + 22))
        draw.text((x, y + 2), f"{n + 1}", fill=(235, 235, 240), font=font)
    sheet.save(out)
    print(f"contact_sheet: {len(imgs)} slides -> {out} ({sheet.width}x{sheet.height})")


if __name__ == "__main__":
    main(sys.argv[1:])
