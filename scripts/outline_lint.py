#!/usr/bin/env python3
"""outline_lint.py - check a slide outline BEFORE building anything.

Fixing a weak story costs one line here and a full rebuild later.

Outline format (plain Markdown, one block per slide):

  # Deck title
  duration: 20          minutes of talking time (optional but strongly advised)
  audience: first-year biology students   (optional)

  ## 1. Sleep is when the brain files its memories      <- the slide title, written as a claim
  time: 2               minutes on this slide
  - one short point
  - another
  notes: what to say, in full sentences

Usage:
  python3 outline_lint.py outline.md [--pace 1.5] [--max-bullets 5] [--json out.json]

Checks:
  WARN  title is a label ("Overview", "Results") instead of a claim
  WARN  slide has more than --max-bullets bullets, or a bullet longer than 14 words
  WARN  fewer than 1 or more than ~2.5 slides per minute of talk (--pace is the target minutes per slide)
  FAIL  time: values do not add up to duration (more than 10 percent off)
  WARN  two slides share a title
  WARN  first slide is not a title/hook, last slide is not a close/ask
  WARN  slide has no notes (only flagged when any slide has notes)
"""
import json
import re
import sys

LABELS = {
    "overview", "introduction", "intro", "agenda", "outline", "background", "summary", "conclusion",
    "conclusions", "results", "discussion", "methods", "methodology", "questions", "q&a", "thank you",
    "thanks", "references", "next steps", "recap", "title", "contents", "table of contents",
}
STRUCTURAL = {"agenda", "outline", "references", "thank you", "thanks", "questions", "q&a", "title", "contents"}


def parse(text):
    deck = {"title": "", "duration": None, "audience": "", "slides": []}
    cur = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("# ") and not deck["title"]:
            deck["title"] = line[2:].strip()
        elif line.startswith("## "):
            title = re.sub(r"^\d+[.)]\s*", "", line[3:].strip())
            cur = {"title": title, "time": None, "bullets": [], "notes": ""}
            deck["slides"].append(cur)
        elif cur is None:
            m = re.match(r"duration:\s*([\d.]+)", line, re.I)
            if m:
                deck["duration"] = float(m.group(1))
            m = re.match(r"audience:\s*(.+)", line, re.I)
            if m:
                deck["audience"] = m.group(1).strip()
        else:
            m = re.match(r"time:\s*([\d.]+)", line, re.I)
            if m:
                cur["time"] = float(m.group(1))
            elif re.match(r"notes:", line, re.I):
                cur["notes"] = line.split(":", 1)[1].strip()
            elif line.lstrip().startswith(("- ", "* ")):
                cur["bullets"].append(line.lstrip()[2:].strip())
            elif cur["notes"] and line.strip():
                cur["notes"] += " " + line.strip()
    return deck


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    pace = float(argv[argv.index("--pace") + 1]) if "--pace" in argv else None
    max_b = int(argv[argv.index("--max-bullets") + 1]) if "--max-bullets" in argv else 5
    deck = parse(open(argv[0], encoding="utf8").read())
    slides = deck["slides"]
    fails, warns = [], []
    if not slides:
        print("outline_lint: no '## ' slide headings found")
        return 2
    seen = {}
    any_notes = any(s["notes"] for s in slides)
    for n, s in enumerate(slides, 1):
        t = s["title"].lower().strip(" .:")
        words = t.split()
        if t in LABELS and t not in STRUCTURAL:
            warns.append(f"slide {n}: title '{s['title']}' is a label. Say what the slide proves.")
        elif len(words) <= 2 and t not in STRUCTURAL and n not in (1, len(slides)):
            warns.append(f"slide {n}: title '{s['title']}' is very short. A claim sentence carries more.")
        if len(s["bullets"]) > max_b:
            warns.append(f"slide {n}: {len(s['bullets'])} bullets (> {max_b}). Split the slide or cut.")
        for b in s["bullets"]:
            if len(b.split()) > 14:
                warns.append(f"slide {n}: long bullet ({len(b.split())} words): {b[:50]!r}")
        if t in seen:
            warns.append(f"slide {n}: same title as slide {seen[t]}")
        seen[t] = n
        if any_notes and not s["notes"]:
            warns.append(f"slide {n}: no notes while other slides have them")
    dur = deck["duration"]
    if dur:
        total = sum(s["time"] for s in slides if s["time"] is not None)
        timed = sum(1 for s in slides if s["time"] is not None)
        if timed == len(slides) and abs(total - dur) > dur * 0.10:
            fails.append(f"times add to {total:g} min but duration is {dur:g} min")
        rate = len(slides) / dur
        if rate > 2.5:
            warns.append(f"{len(slides)} slides in {dur:g} min = {rate:.1f} slides/min. Too fast for a spoken deck unless many are quick visuals.")
        if rate < 0.2:
            warns.append(f"{len(slides)} slides in {dur:g} min = {rate:.2f} slides/min. Very few slides; is this a workshop with long activities?")
        if pace:
            want = dur / pace
            if abs(len(slides) - want) > max(3, want * 0.3):
                warns.append(f"{len(slides)} slides vs about {want:.0f} expected at {pace:g} min/slide")
    first = slides[0]["title"].lower()
    last = slides[-1]["title"].lower()
    if not any(w in first for w in ("title", "welcome", "why", "what", "how")) and len(slides) > 6 and len(first.split()) < 2:
        warns.append("first slide has no clear hook or title")
    if last.strip(" .!") in ("thank you", "thanks", "questions", "q&a", "questions?", "the end"):
        warns.append("last slide is only a thank-you or Q&A label; end on what the audience should do or remember (keep thanks as a line on it)")
    elif not re.search(r"next|join|ask|try|remember|takeaway|apply|\bdo\b|call|sign|vote|read|start|tonight|today|tomorrow|week", last):
        warns.append("last slide does not look like a close or an ask; end on what the audience should do or remember")
    out = {"slides": len(slides), "duration": dur, "fails": fails, "warns": warns}
    if "--json" in argv:
        json.dump(out, open(argv[argv.index("--json") + 1], "w"), indent=2)
    print(f"outline_lint: {len(slides)} slides" + (f", {dur:g} min" if dur else ""))
    print(f"FAIL {len(fails)}  WARN {len(warns)}")
    for x in fails:
        print("  FAIL " + x)
    for x in warns:
        print("  WARN " + x)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
