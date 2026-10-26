#!/usr/bin/env python3
"""pptx_qc.py - structural QA for a .pptx without needing PowerPoint.

Usage:
  python3 pptx_qc.py deck.pptx [--notes] [--no-dashes] [--min-font 14] [--max-words 70] [--json out.json]

Checks (FAIL = fix before delivery, WARN = fix or explain):
  FAIL  shape sticks out of the slide
  FAIL  placeholder text left in (lorem ipsum, TODO, TBD, click to add, XXX)
  FAIL  text box almost certainly overflows (estimated from font size and box size)
  FAIL  em or en dash found (only with --no-dashes)
  FAIL  slide has no speaker notes (only with --notes)
  WARN  font smaller than --min-font pt
  WARN  more than --max-words words on one slide
  WARN  picture without alt text
  WARN  slide has no title
  WARN  two slides share a title
  WARN  empty placeholder shape

The overflow test is a heuristic (average glyph width = 0.5 x font size), so treat a FAIL as
"look at this slide in the render", not as proof. Run render_static.py to see pictures.

Blind spots (it prints a NOTE when it meets one): table cell sizes, charts, SmartArt and grouped
shapes are not measured for overflow; table text IS checked for placeholders, dashes and word count.
Embedded fonts and animations are not checked. A clean report does not mean a good slide.
Needs python-pptx (pip install python-pptx).
"""
import json
import re
import sys

try:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
except ImportError:
    sys.exit("pptx_qc: python-pptx missing. Run: pip3 install python-pptx")

PLACEHOLDER = re.compile(r"lorem ipsum|\bTODO\b|\bTBD\b|\bXXX\b|click to add|your text here|insert .* here", re.I)
DASH = re.compile("[–—]")


def opt(argv, name, default=None, cast=str):
    if name in argv:
        i = argv.index(name)
        return cast(argv[i + 1])
    return default


def text_of(shape):
    if shape.has_text_frame:
        return shape.text_frame.text
    if getattr(shape, "has_table", False) and shape.has_table:
        return "\n".join(c.text for row in shape.table.rows for c in row.cells)
    return ""


def est_overflow(shape):
    """Return (needed_height_in, box_height_in) or None."""
    if not shape.has_text_frame or not shape.width or not shape.height:
        return None
    box_w = shape.width / 914400.0 - 0.2
    box_h = shape.height / 914400.0 - 0.1
    if box_w <= 0 or box_h <= 0:
        return None
    need = 0.0
    for p in shape.text_frame.paragraphs:
        size = None
        for r in p.runs:
            if r.font.size:
                size = r.font.size.pt
                break
        if size is None and p.font.size:
            size = p.font.size.pt
        size = size or 18.0
        chars = len(p.text)
        if chars == 0:
            need += size * 1.2 / 72.0
            continue
        per_line = max(1, int(box_w * 72.0 / (size * 0.5)))
        lines = -(-chars // per_line)
        need += lines * size * 1.2 / 72.0
    return need, box_h


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    path = argv[0]
    need_notes = "--notes" in argv
    no_dashes = "--no-dashes" in argv
    min_font = opt(argv, "--min-font", 14, float)
    max_words = opt(argv, "--max-words", 70, int)
    prs = Presentation(path)
    sw, sh = prs.slide_width, prs.slide_height
    fails, warns, titles = [], [], {}
    unmeasured = set()
    per = []
    for n, slide in enumerate(prs.slides, 1):
        words = 0
        smallest = None
        title = None
        if slide.shapes.title is not None and slide.shapes.title.has_text_frame:
            title = slide.shapes.title.text_frame.text.strip()
        for sp in slide.shapes:
            name = sp.name
            if getattr(sp, "has_table", False) and sp.has_table:
                unmeasured.add("tables")
                for row in sp.table.rows:
                    for c in row.cells:
                        for p in c.text_frame.paragraphs:
                            for r in p.runs:
                                if r.font.size and r.text.strip():
                                    pt = r.font.size.pt
                                    smallest = pt if smallest is None else min(smallest, pt)
            if getattr(sp, "has_chart", False) and sp.has_chart:
                unmeasured.add("charts")
            if sp.shape_type == MSO_SHAPE_TYPE.GROUP:
                unmeasured.add("grouped shapes")
            if sp.left is not None and sp.width is not None:
                if sp.left < -9525 or sp.top < -9525 or sp.left + sp.width > sw + 9525 or sp.top + sp.height > sh + 9525:
                    fails.append(f"slide {n}: '{name}' sticks out of the slide")
            t = text_of(sp)
            if t.strip():
                words += len(t.split())
                if PLACEHOLDER.search(t):
                    fails.append(f"slide {n}: placeholder text in '{name}': {t[:50]!r}")
                if no_dashes and DASH.search(t):
                    fails.append(f"slide {n}: em/en dash in '{name}'")
                if title is None and sp.has_text_frame:
                    # first big text box counts as the title for decks built without layouts
                    sizes = [r.font.size.pt for p in sp.text_frame.paragraphs for r in p.runs if r.font.size]
                    if sizes and max(sizes) >= 28:
                        title = t.strip().split("\n")[0]
                if sp.has_text_frame:
                    for p in sp.text_frame.paragraphs:
                        for r in p.runs:
                            if r.font.size and r.text.strip():
                                pt = r.font.size.pt
                                smallest = pt if smallest is None else min(smallest, pt)
                ov = est_overflow(sp)
                if ov and ov[0] > ov[1] * 1.25 and ov[0] - ov[1] > 0.3:
                    fails.append(f"slide {n}: '{name}' text probably overflows (needs ~{ov[0]:.1f}in, box {ov[1]:.1f}in)")
            elif sp.is_placeholder and sp.has_text_frame:
                warns.append(f"slide {n}: empty placeholder '{name}'")
            if sp.shape_type == MSO_SHAPE_TYPE.PICTURE:
                descr = sp._element.xpath(".//p:cNvPr/@descr")
                alt = descr[0].strip() if descr else ""
                # python-pptx and PowerPoint fill alt text with the file name by default; that is not a description
                if not alt or re.search(r"\.(png|jpe?g|gif|webp|bmp|svg|tiff?)$", alt, re.I):
                    warns.append(f"slide {n}: picture '{name}' has no real alt text")
        if smallest is not None and smallest < min_font:
            warns.append(f"slide {n}: smallest font {smallest:g}pt (< {min_font:g}pt)")
        if words > max_words:
            warns.append(f"slide {n}: {words} words (> {max_words})")
        if need_notes:
            has = slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip()
            if not has:
                fails.append(f"slide {n}: no speaker notes")
        if not title:
            warns.append(f"slide {n}: no title")
        else:
            key = title.lower()
            if key in titles:
                warns.append(f"slide {n}: same title as slide {titles[key]} ({title[:40]!r})")
            titles[key] = n
        per.append({"n": n, "title": title, "words": words, "smallest_pt": smallest})
    out = {"file": path, "slides": len(per), "fails": fails, "warns": warns, "perSlide": per}
    j = opt(argv, "--json")
    if j:
        with open(j, "w") as f:
            json.dump(out, f, indent=2)
    print(f"pptx_qc: {len(per)} slides, {sw/914400:.2f}x{sh/914400:.2f}in")
    print(f"FAIL {len(fails)}  WARN {len(warns)}")
    for x in fails[:60]:
        print("  FAIL " + x)
    for x in warns[:60]:
        print("  WARN " + x)
    if unmeasured:
        print("  NOTE overflow and size were not measured for: " + ", ".join(sorted(unmeasured)) + ". Look at those slides in the render.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
