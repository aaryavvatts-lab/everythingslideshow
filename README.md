# everythingslideshow

**One command for any presentation.** A Claude Code skill that works out what slideshow you need, picks the right tools out of about 100 slide, design, graphics, story and research skills, builds the deck, checks it three ways, fixes the mistakes, and proves it did what you asked.

You type `/everythingslideshow` (or just say "make me slides for my biology talk") and it does the director's job so you never pick tools by hand.

```
 you ask
   |
   v
 1 UNDERSTAND    audience, message, setting, length, format, inputs
   |             -> Deck Brief  +  Requirements Ledger (the contract)
   v
 2 CHOOSE        ONE engine (HTML / PowerPoint / Beamer / Marp / image deck)
   |             + only the helper skills the job needs  -> Skill Plan
   v
 3 STORY         outline with claim titles, timing, hook and close -> linted
   |
   v
 4 ASSETS        sourced facts, images with licences, charts, QR codes
   |
   v
 5 BUILD         the chosen engine, craft floors enforced (type, contrast, density)
   |
   v
 6 CHECK x3      Round 1 scripts (overflow, tiny text, broken images, placeholders)
   |             Round 2 your eyes, slide by slide
   |             Round 3 an independent grader scores 8 dimensions, finds mistakes
   v
 7 DID I DO WHAT WAS ASKED?   every ledger line PASS or FAIL with evidence
   |
   v
 8 DELIVER       deck + PDF copy + notes + sources + CHECKS.md
```

It follows the same pattern as the fulldesign and [everythingvideo](https://github.com/aaryavvatts-lab/everythingvideo) skills: a director skill that audits, chooses, applies and verifies, instead of one more template.

## Install

```bash
git clone https://github.com/aaryavvatts-lab/everythingslideshow ~/.claude/skills/everythingslideshow
```

Restart Claude Code. That is enough to use it: the skill works with the programs you already have (Node and Python are the only real needs) and falls back to built-in tools when a companion skill is missing.

For the full power, install the companion skills it routes to (open-source, from GitHub):

```bash
bash ~/.claude/skills/everythingslideshow/scripts/install_companions.sh --core    # the 14 that cover almost everything
bash ~/.claude/skills/everythingslideshow/scripts/install_companions.sh --all     # about 90, a few hundred MB
bash ~/.claude/skills/everythingslideshow/scripts/check_skills.sh --missing --tools   # what do I have?
```

The installer shallow-clones, copies only the skill folders, never overwrites an existing skill and never runs code from the clones. Read a skill before you trust it.

## What it can make

| You say | It builds |
|---|---|
| "slides for my 15 minute talk on X" | HTML or PowerPoint deck with claim titles, notes, a cut order |
| "pitch deck for my startup" | Investor structure, charts from your real numbers only, standalone readable |
| "turn this PDF/paper into a presentation" | Story-first deck, figures cited, backup slides |
| "thesis defense" | Roadmap markers, Q&A and backup section, Beamer or PPTX |
| "make this deck look better" | Reads the old deck, fixes what is wrong, keeps what works, never overwrites |
| "I need an editable PowerPoint my teacher can open" | PPTX + PDF copy, fonts that exist everywhere |
| "something amazing I can send as a link" | Single-file animated HTML deck |
| "narrated slideshow" | Script, voice, timed slides, captions |

## How it picks tools

The [`catalog.md`](catalog.md) lists every skill it can use, in 14 groups, with a source link, what it does and when to use it:

HTML decks (frontend-slides, huashu-design, html-ppt, guizang-ppt, ...) · Editable PowerPoint (ppt-master, pptx, mck-ppt-design, cyberppt, style packs, ...) · Academic (academic-slides, Beamer, thesis defense, paper-to-slides, ...) · Markdown and code decks (Marp, reveal.js, open-slide) · Image-first decks · Narrated and video decks · Story, copy and notes · Visual design and style · Diagrams, charts, infographics, images · Research and facts · Motion · Review and quality · Office and file helpers · House skills

It picks **one engine** per deck and only the supporting skills that genuinely apply. A missing skill never stops a run.

## The checks (why decks come out right)

- **Requirements ledger.** Every concrete thing you asked for becomes a numbered, checkable line. At the end each one is marked PASS or FAIL with evidence (a slide number, a measurement).
- **Round 1, scripts.** `render_deck.mjs` screenshots every HTML slide and flags overflow, clipped text, tiny fonts, broken images and console errors. `pptx_qc.py` flags shapes off the slide, likely text overflow, small fonts, placeholder text, missing notes and alt text, duplicate titles. `render_static.py` turns PPTX/PDF into pictures. `contact_sheet.py` makes one overview picture. `outline_lint.py` lints the story before anything is built.
- **Round 2, eyes.** A slide-by-slide checklist, an AI-slop check, a copy pass, fact re-verification.
- **Round 3, a second mind.** Eight rubric dimensions scored 1 to 5 by an independent grader with no memory of how the deck was made; anything under 4 is fixed.
- **Ground rules.** No invented statistics, quotes or citations. Facts come from you or a cited source. Weekdays and sums are checked. Nothing is uploaded or sent without your yes. Your files are never overwritten.

## Repo layout

```
SKILL.md            the director: phases, rules, engine table, signal table
catalog.md          every skill it can route to
references/
  recipes.md        arcs and skill sequences per deck type
  craft.md          type, contrast, density, layout, chart, motion floors
  checks.md         ledger, CHECKS.md, Round 2 checklist, Round 3 rubric, grader prompt
  formats.md        format choice and export recipes
  academic.md       conference, defense, lab meeting structures
scripts/
  check_skills.sh install_companions.sh outline_lint.py
  render_deck.mjs render_static.py pptx_qc.py contact_sheet.py
evals/prompts.md    sample requests to try
```

## Requirements

- Claude Code with skills enabled.
- Node 18+ and Python 3.9+. Optional: `python-pptx`, `pillow`, `pymupdf` (`pip3 install python-pptx pillow pymupdf`), `playwright-core` plus Chrome for HTML rendering, LibreOffice for PPTX to PDF.
- Some companion skills need their own tools or API keys (image generation, ElevenLabs voice). The skill tells you when one is needed and never installs or spends without asking.

## Credits

This skill orchestrates the work of many open-source authors. The catalog links each one; their skills are installed from their own repositories under their own licences (note: `guizang-ppt-skill` is AGPL-3.0). Special thanks to the authors of frontend-slides, huashu-design, html-ppt-skill, ppt-master, visual-explainer, open-slide, the baoyu skills, the academic slide skills and the many style packs.

## License

MIT for this repository. Companion skills keep their own licences.
