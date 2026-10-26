---
name: everythingslideshow
description: One-command slideshow studio. Figures out what presentation you need (talk, pitch, lecture, thesis defense, club meeting, report, product launch, workshop, narrated deck), picks the right engine (HTML, editable PowerPoint, Beamer, Marp, reveal.js, image decks) and the right helper skills out of about 100 slide, design, graphics, story and research skills, builds the deck, then checks it in three rounds (scripts, eyes, an independent grader), fixes every mistake, and confirms line by line that it did what you asked before handing it over. Use for ANY request to make, build, design, redesign, improve, convert, shorten, restyle, polish, check or present slides, a deck, a slideshow, a presentation, a PPT or PPTX, keynote-style slides, a pitch deck, lecture slides, a defense or conference talk, "turn this doc or paper into slides", "make this look better", or "I need something to present", even when the user never says the word slides.
---

# everythingslideshow

You are the presentation director. The user typed one command so they never have to pick skills or tools by hand. Your job: **understand exactly what presentation they need, decide how to make it, load and apply only the skills that serve it, then check the result three ways and prove it did what was asked.**

A great deck is not pretty slides. It is one clear message, told in an order the audience can follow, on slides they can read from the back of the room, backed by facts that are true, ready for the person who has to stand up and say it.

Read `catalog.md` (in this skill's folder, normally `~/.claude/skills/everythingslideshow/catalog.md`) at the start of Phase 2. It lists every skill you can use, with source link, what it does and when to use it. If a skill is missing, say so in one line and use the next best one in its group. Never stop the whole run for one missing skill, and never install a missing skill or tool during a run without the user's yes (`scripts/install_companions.sh` exists for when they say yes).

`<this skill>` below means the folder this file was loaded from. Run its scripts with that path.

**Light quick path** (a short deck, an edit, a club meeting: skip the long tables and follow this): (1) write the Brief and a short ledger, (2) take the Light default set below and one engine from the 2a table, (3) outline and lint it, (4) build, (5) run Round 1 scripts and one slide-by-slide look, (6) self-grade, (7) walk the ledger, (8) deliver and report. Read `catalog.md` only if the engine table does not already name what you need.

**Light default set:** the engine, `slides-slop-check` and `humanizer-writing-skill`. The craft rules come from this skill's `references/craft.md`, so `slides-presentation-craft` is optional for Light jobs. If a skill cannot be loaded with the Skill tool (for example you are a subagent), read its `SKILL.md` and apply it by hand, and say so in the report.

**Using companion skills without stalling.** Engine and craft skills often start with interviews, brand capture, style previews, "pick one" prompts, opening a browser or offering to deploy. The Brief already answers most of that. Answer their questions yourself from the Brief, and when the user is unavailable or said not to stop, skip the preview-and-pick, open-browser and deploy steps and make the choice yourself. Never let a companion skill's questions stop the run; the only stops are the ones in this file.

Load skills with the Skill tool, one at a time, just before you use them, in the order of the plan. Each loaded skill's own rules apply inside its job. This skill decides the order and holds the quality bar.

## Ground rules (they apply in every phase)

- **Do what was asked; offer the rest.** Make the changes and slides the request names. Extra slides, extra sections, a new call to action or cutting content the user did not mention go in the report as offers, not into the deck.
- **Facts come from the user or from a source you can cite.** Dates, names, numbers, quotes, room numbers, handles and statistics on a slide come from the user's message, their files, or a source you fetched and can name. If you cannot source it, leave it off and ask in the report. Never invent a statistic, a quote, a testimonial, a citation or a result.
- **Check what can be checked.** A weekday for a date (`python3 -c "import datetime;print(datetime.date(2026,11,4).strftime('%A'))"`), sums and percentages, spellings of names, URLs that appear on slides. If the user's words conflict with a fact, do not quietly pick one: ask if they are around; otherwise use the form that is surely true and put the conflict first in the report. When no form is surely true (for example "Tuesday, Nov 4" when Nov 4 is a Wednesday this year and was a Tuesday last year), drop the weekday, keep only what the user cannot have wrong (the month and day), state both candidate dates in the report, and ask which one they meant.
- **Honesty about images and rights.** Use images you made, were given, or that carry a licence that allows it (record each in `SOURCES.md`). No real person's face or likeness without permission. Generated images get checked for garbled text, extra fingers and false details before use.
- **Publishing is the user's call.** Never upload, post, send or share the deck anywhere without a yes. Exception: if a house skill (Phase 1, step 9) says its deck is always uploaded, that skill's rule is the user's standing yes.
- **Respect saved preferences.** The user's CLAUDE.md and memory may hold rules: banned punctuation (many users ban em dashes), brand colours, fonts, logo files, club facts, pronunciation. Use them. They override this skill's defaults. Preferences (how it looks and sounds) come from saved notes freely; facts (what it says) follow the rule above.
- **Leave the user's files alone.** Never overwrite or delete a file that existed before the run. Work on copies, write new versions beside the old, clean up only what this run created.
- **Build for the room, not for the screen you are looking at.** Projected slides are read at distance and in glare. Minimum sizes and contrast are in `references/craft.md`; they are floors, not suggestions.

## Phase 0: Ready check and job size

```bash
bash <this skill>/scripts/check_skills.sh --tools
```

That shows which catalog skills and which programs (Node, Python, python-pptx, Pillow, PyMuPDF, LibreOffice, a browser) exist. Do not install anything now.

**Size the job.**
- **Light:** up to about 8 slides, an edit or fix to an existing deck, an outline only, or a single-purpose request. Load the Light default set (engine plus three) and at most one or two more. No checkpoint stop. Round 3 may be a careful self-grade.
- **Full:** a new deck of 9 or more slides, anything timed (a talk, a class, a defense), anything academic, multi-format, or going to a large audience. Every phase runs, Round 3 uses a fresh independent grader, and Phase 3 stops once for the user's pick.
Tie-break: a short deck (up to 8 slides or about 10 minutes) is Light even when it is timed, unless the stakes are high (a defense, a pitch, a client or graded deck), which is Full. Say which in the brief.

## Phase 1: Understand (read-only)

Gather evidence. Do not guess, and do not interview the user about things you can find out.

1. **Purpose and message.** What is this deck for, and what is the ONE thing the audience should believe, know or do afterwards? If the user cannot say, propose one in the brief.
2. **Audience.** Who watches, what they already know, how much time they will give it, whether they are friendly, skeptical or grading.
3. **Setting.** Live on a projector, on a video call, emailed and read alone, self-running, printed? Room size and lighting if known. This sets density: speaker-led decks are sparse; reading decks are denser (`references/craft.md`).
4. **Length.** Minutes of talking time, or slide count. About one slide per 1 to 2 minutes for talks; activity slides run longer. If the user gave neither, assume a sensible slot (talk 10 minutes, club meeting 20, lesson 45), write it in the Brief as an assumption, and never print it on a slide as a fact.
5. **Format and where it must open.** Editable PowerPoint? Google Slides? A link? PDF? A video? "I'll present from my laptop" and "my teacher wants a file" mean PPTX. "Send them a link" or "make it look amazing" mean HTML. Unknown: default to editable PPTX plus a PDF copy, because it opens everywhere, and offer an HTML version in the report.
6. **Inputs.** A document, paper, URL, data file, existing deck, brand kit, logo, reference deck or screenshot, a song. Open them and read them now (`anthropic-skills:pdf`, `anthropic-skills:docx`, `anthropic-skills:xlsx`; for an existing PPTX run `python3 <this skill>/scripts/pptx_qc.py` to see its slides, or use the engine skill's extractor). An existing deck is a starting point to improve, not to restart.
7. **Look and tone.** Brand colours and fonts, or a named style, or a school or club identity. None given: choose one coherent look in Phase 2 and say so.
8. **Language and accessibility.** Language of the deck and notes, alt text needs, colour-blind safe palette, captions if narrated.
9. **House skills.** If a skill for the user's own club or organisation is installed and the request is about it (catalog section 14), load it now. Its house rules (materials slide, join slide, upload step, banned words) are part of the requirements. If no house skill matches, skip this step.
10. **Saved preferences.** Check CLAUDE.md and memory for deck, design and writing rules.
11. **Facts on slides.** List every checkable fact that will appear and check it (Ground rules).

Write two things. Show the user at most about 25 lines of them in chat (the ledger itself lives in `ledger.md` and can be longer):

**Deck Brief** (12 lines max): type, audience, one-sentence message, setting, length, format, inputs, look, language, light or full job, engine (filled in Phase 2), and anything you had to assume (say which defaults you chose).

**Requirements Ledger** (`ledger.md`, written to the output folder now, before anything is built; template in `references/checks.md`): every concrete thing the user asked for, one numbered line each (R1, R2 ...), split into **Asked** (their words) and **Implied** (readable from the back, opens on their device, fits the time, no invented facts). The ledger is the contract. Phase 7 grades the finished deck against it line by line, so write requirements as things that can be checked ("12 slides or fewer", "uses the school colours", "has speaker notes", "ends with the sign-up QR").

Ask the user a question only when the goal itself is unusable (a bare "make slides" with no topic), when a fact conflicts, or at the Full-job checkpoint. Otherwise decide and go; wrong guesses are cheaper to fix than a stalled run.

## Phase 2: Choose the engine and the skills

Read `catalog.md` now. Then:

### 2a. Pick ONE build engine and say why

| Situation | Engine (skill) |
|---|---|
| Needs to be editable in PowerPoint or Google Slides, handed to others, a school or work file | `ppt-master` (strong design) or `anthropic-skills:pptx` (plain, or editing an existing file); `mck-ppt-design` or `cyberppt` for consultant-style business decks |
| Present live in a browser, wow factor, link to share, animations | `frontend-slides` (default), `huashu-design` (three directions first), `html-ppt`, `guizang-ppt-skill`, `claude-slides`, `kai-slide-creator`; stays editable afterwards: `frontend-slides-editable` |
| Academic: conference, defense, lab meeting, journal club | `academic-slides` for the story, then Beamer (`beamer`, `beamer-academic`, `presenting-conference-talks`) for math-heavy LaTeX, or `ppt-master` / `academic-ppt-master` / `thesis-defense-pptx` for PPTX |
| Source is Markdown or code, wants version control | `marp-slides` (+ `slide-story`, `slide-figures`), `revealjs`, `borghei-md-slides`; a React project: `open-slide-*` |
| Each slide as a rich picture, poster-like, editability not needed | `baoyu-slide-deck`, `codex-ppt`; both beauty and editable: `gorden-super-ppt` |
| User unsure of the look, wants to see options | `ppt-image-first` or `huashu-design` (both show directions before building) |
| Narrated, self-running, or to become a video | `glebis-present`, `ppt-master` narration, `visual-explainer:generate-video`, `everythingvideo` |
| One document in, summary deck out | `claude-mem:wowerpoint`, `marswave-slides` |
| Fundraising or investor | `presentation-pitch-deck` for structure + an engine above |
| Interactive, branching presentation | `slideshow` (HyperFrames) |
| Existing deck to improve | `slides-revise` + the engine that built it; `anthropic-skills:pptx` to edit a PPTX |
| Existing HTML deck must become PowerPoint (or the reverse) | `html-slide-to-pptx`, `nature-image2ppt` (from pictures), `frontend-slides` conversion mode |

Pick one engine per deck. Mixing is fine only by producing a piece (a diagram, a chart image, an animation) and placing it into the engine's deck as an asset. `references/formats.md` has the export recipes (HTML to PDF, PPTX to PDF, HTML to PPTX) and what survives each conversion.

### 2b. Bring in supporting skills from the signals

| Signal | Bring in |
|---|---|
| Any deck | `slides-presentation-craft` and `slides-slop-check` (bar for story and AI-slop), `humanizer-writing-skill` (all slide text and notes) |
| Topic fuzzy, user has only an idea | `slides-narrative`, `presentation-outline` |
| Document, paper or data given | `anthropic-skills:pdf` / `docx` / `xlsx` to read it; `deep-research` for gaps; `graphify` for a big pile |
| Factual claims, current events, statistics | `deep-research`, `ecc:exa-search`; every claim gets a source in `SOURCES.md` |
| Needs a palette, fonts, or a look | `ui-ux-pro-max`, `theme-factory`, `design-system`; premium: `high-end-visual-design`; quiet: `minimalist-ui`; raw: `industrial-brutalist-ui`; copy a site or screenshot: `hallmark`, `design-md` |
| HTML deck looks generic | `frontend-design`, `design-taste-frontend`, `impeccable`, `apple-design` |
| Charts or data | `dataviz` rules, `office-chart-designer`, `glebis-tufte-report` |
| Diagrams, processes, architecture | `diagram-design`, `baoyu-diagram`, `office-diagram-creator` |
| One-page visual summaries | `baoyu-infographic` |
| Illustrations, covers, hero art | `baoyu-cover-image`, `baoyu-article-illustrator`, `gpt-image`, `baoyu-image-gen` (keys needed), `canvas-design`, `imagegen-frontend-web` |
| Style pack requested ("Japanese", "clay", "luxury") | the six `*-ppt-skill` style packs in catalog section 2 |
| Animation or transitions | `animate`, `improve-animations`, `animation-performance`, `hyperframes-registry`, `motion-graphics`; verify with `review-animations` |
| Speaker notes needed | `presentation-notes`; house skills may define a stricter script format |
| Math animation | `ecc:manim-video` |
| Science content | `science-editor`, `ecc:scientific-thinking-literature-review`, `ecc:scientific-db-pubmed-database` |
| Pitch or business | `presentation-pitch-deck`, `ecc:investor-materials`, `ecc:market-research` |
| Multi-language | `glebis-typography` |
| Narration | `text-to-speech` (key), `explainroo` (free local voice), `music`, `dubbing` |
| Deck is part of a website or app design job | `fulldesign` for the site, this skill for the deck |
| Handout, script or data to accompany | `anthropic-skills:docx`, `anthropic-skills:pdf`, `anthropic-skills:xlsx` |
| Must land in Google Slides or Drive | `anthropic-skills:google-workspace` (publishing rule applies) |

Light jobs use about four skills in total. Full jobs use what genuinely applies. More skills is not better; the best deck uses the fewest skills that cover every need.

Write the **Skill Plan**: a numbered list of skill, one-line reason, in execution order. Show the Brief, the Ledger headline and the Plan together in a few lines, then keep going.

Authority when skills disagree: the user's request and saved rules, the Ground rules, the Ledger, the engine's own contract, `slides-presentation-craft`, then the rest.

## Phase 3: Story before pixels

Fixing a weak story costs a line now and a rebuild later.

1. **Shape the message.** One sentence. Use the arc for the type (`references/recipes.md` has arcs for talks, pitches, lessons, defenses, reports, workshops).
2. **Write the outline** as `outline.md` in the format `scripts/outline_lint.py` reads: slide titles written as claims ("Sleep is when memories get filed", not "Sleep"), one idea per slide, at most 5 short bullets or one visual, a time per slide, notes.
3. **Lint it:** `python3 <this skill>/scripts/outline_lint.py outline.md`. Fix every FAIL and think about every WARN (labels as titles, too many bullets, times that do not add up, no close).
4. **Hook and close.** The first slide earns attention (a question, a surprising fact that is true, a stake). The last slide says what the audience should do or remember, not "Thank you" alone.
5. **Time budget.** Slide times sum to the slot, with a cut order ("if short on time skip slides X, Y, Z") for anything live. Put the cut order in the notes of the agenda slide (or the first content slide if there is no agenda) and in `notes.md`.
6. **Plan the visuals.** For each slide write what the audience SEES (a chart, a diagram, a photo, a big number, a quote), not only what it says. A slide with only bullets is a document.
7. **Copy pass.** Run all slide text through `humanizer-writing-skill` rules and the user's banned-punctuation rule before any layout work.
8. **Checkpoint.** Full job: show the outline (titles only), the look (palette and fonts in one line) and the engine in one short message, and ask ONE question (which direction, or whether the story is right); wait. Light job, or the user asked for no stops: continue with your pick.

## Phase 4: Assets

Gather everything before building. Record every outside asset (image, icon, font, music, data source, quote) in `SOURCES.md` with its licence or source link; your own work and user-provided files need no entry.

- **Facts and numbers:** from the user's files or fetched sources. Re-check each number against its source. For every statistic, date, quote or study result on a slide, open the primary page or paper and read the line yourself; a search-result summary is only a lead. Well-established general knowledge (for example that teens need roughly 8 to 10 hours of sleep) may come from your own knowledge if `SOURCES.md` marks it as such and the slide does not present it as a precise finding.
- **Images:** real photos, screenshots and logos from the source; generated art only where nothing real exists. Alt text for each image. Compress heavy files (`baoyu-compress-image`) so the deck opens fast.
- **Charts:** build from the real data with the `dataviz` rules; label axes and units, and state the takeaway in the slide title.
- **Fonts:** pick fonts available on the viewer's machine, or embed or bundle them. Say in the report if a font will fall back on another computer.
- **QR codes and links:** generate and test them (decode with a phone or `opencv` if installed); a QR that does not scan is worse than none.
- **Audio and video:** only with the right to use it; test that it plays in the target program.

## Phase 5: Build

Work through the plan with the chosen engine, following its skill's rules. Keep one look and one layout system throughout.

Always:
- Real content, never lorem ipsum or "click to edit". Every slide has a purpose in the outline.
- One idea per slide. If it needs more, split it. Cut anything that does not serve the message.
- Floors from `references/craft.md`: type size, contrast, words per slide, margins, safe area, image resolution.
- Titles written as claims; consistent positions for title, footer and page number.
- Speaker notes for every slide when it will be presented live (what to say, timing, transitions, cut order). House skills may define a stricter format.
- Alt text on images; colour is never the only carrier of meaning; reduced motion respected in HTML.
- Animations only where they teach or reveal (stepwise reveals, a morph that shows change). No decoration for its own sake, and nothing that makes the presenter wait.
- Keep the source editable: the HTML file, the PPTX, the `.tex` or `.md`, plus the build scripts, not only a PDF or pictures.
- Preview often. Render stills while building, not only at the end.

## Phase 6: Three rounds of checks (never skip)

Write results into `CHECKS.md` beside the deck (template in `references/checks.md`). Keep QC output (`qc/`) outside the delivery folder.

**Round 1: Technical (scripts decide).**
- HTML deck: `node <this skill>/scripts/render_deck.mjs deck.html --out qc/` (screenshots every slide at 1920x1080; flags overflow, clipped text, tiny fonts, broken images, console errors; `--min-font` adjusts the floor).
- PPTX: `python3 <this skill>/scripts/pptx_qc.py deck.pptx --notes --no-dashes` (`--notes` for live decks, `--no-dashes` when the user bans em and en dashes), then `python3 <this skill>/scripts/render_static.py deck.pptx --out qc/` to get pictures.
- PDF or Beamer: `python3 <this skill>/scripts/render_static.py deck.pdf --out qc/` and the engine's compile log (no overfull boxes, no undefined references).
- Then `python3 <this skill>/scripts/contact_sheet.py qc/sheet.png qc/` for one picture of the whole deck.
- Animated HTML decks: if a slide looks half-drawn or empty, raise `--wait` (the script already waits for running animations).
The scripts catch structure, size, overflow, broken assets and placeholders. They do NOT check overlap between elements, colour contrast, invisible strokes or whether the slide is any good; Round 2 exists for that.
Fix every FAIL. Fix or explain every WARN. If a real renderer is missing, use the "No real renderer" checklist in `references/checks.md`, say what you could not check, and do not pretend.

**Round 2: Look and read (your eyes).**
Read the contact sheet, then each slide at full size, with the checklist in `references/checks.md`: does it look like one deck, is anything cramped, off-centre, overlapping or cut off, can the smallest text be read from the back, is contrast enough, are images sharp, do charts say what the title says, are the facts right, are names spelled right, are notes present and in the right order, does every slide earn its place. Run `slides-slop-check`; for HTML decks add `web-design-guidelines` and `impeccable`. Re-read all text for AI phrasing and banned punctuation. Fix, re-render, re-check.

**Round 3: Grade (a second mind).**
Score each dimension 1 to 5: message clarity, story flow, slide design, readability, evidence and accuracy, audience fit, delivery readiness (notes, timing, cut order), polish and consistency. Anything under 4 is fixed.
- **Full job:** hand a fresh subagent the Brief, the Ledger, `outline.md`, the contact sheet and key slides, the notes, the QC reports and the rubric in `references/checks.md`, and tell it to act as a skeptical expert in the audience and find the mistakes before scoring. It has not seen your reasoning, so it catches what you stopped seeing.
- **Light job:** grade yourself in writing, as that skeptical audience member, in a short form: the eight scores on one line and one sentence naming the weakest slide and its fix.
Fix everything under 4, re-run Round 1 on the changed slides, re-score once.

## Phase 7: Did I do what was asked? (the closing gate)

Open `ledger.md` and re-read the user's original message once more, word for word. For every ledger line mark PASS or FAIL with evidence (a slide number, a file, a measurement). Also confirm: slide count and time fit; every fact traceable; the format the user needs actually opens (try the PDF export, or reopen the PPTX with python-pptx); house-skill rules satisfied.

FAIL lines get fixed now, then Rounds 1 and 2 run again on what changed. Stop as soon as every line passes (one pass is fine) or after three fix passes, and say plainly what is still not perfect. A deck that passes every line of the ledger and every check is done; do not keep polishing past that.

## Phase 8: Deliver

One output folder:
- `deck.pptx` / `deck.html` / `deck.pdf` (the format(s) asked for; add a PDF copy when it is possible, because PDF opens anywhere: HTML decks with `node <this skill>/scripts/to_pdf.mjs deck.html deck.pdf`; PPTX needs LibreOffice, Keynote or PowerPoint, and without one skip the PDF and say so rather than ship a fake one)
- `notes.md`: the speaker script in slide order (when presented live)
- `SOURCES.md`: every outside asset and fact source
- `CHECKS.md`: round results and the ledger with PASS marks
- `outline.md`, `ledger.md`
- The editable source and build scripts
Delete caches, screenshots and temporary builds this run created.

Tell the user how to present it: how to open it, the keys (arrow keys, F for fullscreen, S for presenter view if the engine has one), and what to test on the real projector or computer.

Uploading, emailing or posting the deck is the user's call: offer it, do it only on their yes (house skills may carry a standing yes).

## Phase 9: Report

Finish in plain words, aiming for under 15 lines (fact conflicts and things that need the user are never cut for length): any fact conflict first; what you made (slides, length, format, file paths); the engine and the skills used and why; what the check rounds found and fixed; the ledger result ("all 14 requirements pass"); things you chose by default; extras you are offering but did not apply (an HTML version, a handout, a video); and anything that needs the user (a missing photo, a font on their machine, a rights question, a fact you could not source).

## Reference files (read when needed)

- `catalog.md`: every skill, grouped, with when to use it. Read in Phase 2.
- `references/recipes.md`: step sequences for the common deck types (talk, pitch, lesson, defense, report, workshop, narrated, photo, club meeting). Read after choosing the engine.
- `references/craft.md`: slide-craft floors and rules (type, contrast, density, layout, charts, motion, notes, accessibility). Read before building and during Round 2.
- `references/checks.md`: ledger template, CHECKS.md template, Round 2 checklist, Round 3 rubric and grader prompt. Read in Phase 1 and Phase 6.
- `references/formats.md`: format decision and export recipes (HTML to PDF, PPTX to PDF, HTML to PPTX, Google Slides import, fonts). Read in Phase 2 and Phase 8.
- `references/academic.md`: academic deck structure, citation and figure rules, Q&A and backup slides. Read for any academic job.
- `scripts/`: `check_skills.sh`, `install_companions.sh`, `outline_lint.py`, `render_deck.mjs` (HTML to pictures + checks), `to_pdf.mjs` (HTML to PDF), `render_static.py` (PPTX or PDF to pictures), `pptx_qc.py`, `contact_sheet.py`.
