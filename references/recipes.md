# Recipes by deck type

Why this file exists: different decks need different arcs and different skill sequences. Pick the matching recipe after Phase 2a, then adjust. Each recipe gives the story arc, the slide budget, the skill order, and the traps.

Contents: Talk or keynote · Pitch deck · Lesson or class · Club meeting · Thesis defense or conference talk · Business report · Workshop · Narrated or self-running deck · Photo or event recap · Fix or restyle an existing deck · Document to deck

## Talk or keynote (10 to 45 min)

- Arc: hook, why it matters, 2 to 4 big ideas each with a story or example, what to do next. Rule of three works.
- Budget: about one slide per 1 to 2 minutes; fewer when slides are stories.
- Skills in order: `slides-narrative` (if fuzzy) or `presentation-outline`, then `frontend-slides` or `huashu-design` (HTML) or `ppt-master` (PPTX), `presentation-notes`, `slides-slop-check`.
- Traps: reading the slides aloud; slides full of text; no ending; a demo with no backup.

## Pitch deck (investors, clients, partners)

- Arc (investor): problem, solution, why now, product, traction, market, business model, team, ask. Traction early if you have it. Standalone decks must make sense with no presenter.
- Budget: 10 to 15 slides plus appendix.
- Skills: `presentation-pitch-deck`, `ecc:investor-materials`, `ecc:market-research`, engine `ppt-master` or `mck-ppt-design` or `huashu-design`, `dataviz` for charts.
- Traps: invented numbers (never), vague market claims, an ask with no amount or use of funds.

## Lesson or class

- Arc: hook question, learning goal, short teaching burst, activity, check for understanding, wrap-up with one takeaway. Chunk into 8 to 12 minute bursts.
- Skills: `visual-cognition-slides`, `slides-presentation-craft`, engine `frontend-slides` or `ppt-master`, `presentation-notes`, `diagram-design`.
- Include: instructions slides for each activity (group size, time, what to do, what done looks like), answer keys in notes, a cut order.
- Traps: no activity, trick questions, activity directions that need supplies nobody has.

## Club meeting

- Arc: sign-in or warm-up, agenda with times, main content or activity, discussion, announcements, how to join or follow, close.
- If a house skill for that club exists (catalog section 14), load it first: it defines materials slides, join slides, notes format and upload steps.
- Traps: leaving the date, room or time wrong; missing contact or join info on the last slide.

## Thesis defense or conference talk

See `academic.md`. Skills: `academic-slides`, then `beamer` family or `ppt-master` / `academic-ppt-master` / `thesis-defense-pptx`, `science-editor`.

## Business report or strategy deck

- Arc: answer first (executive summary), supporting arguments (each slide title is a claim), evidence, risks, recommendation, next steps. Pyramid principle.
- Skills: `mck-ppt-design` or `cyberppt` or `mckinsey-style-viz`, `dataviz`, `diagram-design`, `anthropic-skills:xlsx` for data.
- Traps: chart titles that describe instead of conclude; no recommendation; dense slides with no hierarchy.

## Workshop

- Arc: goal, agenda, short input, exercise, debrief, repeat, commitments. Exercises get full instruction slides and a visible timer cue.
- Skills: as for lesson, plus `slideshow` for interactive or branching exercises.

## Narrated or self-running deck

- Pipeline: script first, timed at about 2.5 spoken words per second, then slides timed to the script, then voice (`explainroo` free local voice, `text-to-speech` with a key, or `glebis-present`), then music (`music`) ducked under the voice, then captions.
- Check: transcribe the finished audio and compare with the script; every slide's on-screen time matches its narration; the deck plays through with no input.
- For a real video file use `everythingvideo` after the deck exists, or `visual-explainer:generate-video`.

## Photo or event recap

- Arc: one standout image first, the story in order, numbers (attendance, results) as big figures, thanks, what is next.
- Skills: engine with strong image handling (`frontend-slides`, `huashu-design`), `baoyu-compress-image`.
- Traps: low-resolution photos, stretched images, no permission for people's faces, long captions.

## Fix or restyle an existing deck

1. Read it before touching it: `python3 scripts/pptx_qc.py old.pptx` for a PPTX, the HTML source otherwise; render it to pictures with `render_static.py` or `render_deck.mjs`.
2. Write what is wrong, ranked by impact, and what the user asked to change. Keep what works.
3. Work on a copy named with a version suffix. Never overwrite the original.
4. Skills: `slides-revise`, `slides-slop-check`, the engine that made it (or `anthropic-skills:pptx`), `impeccable` for HTML.
5. Report a before and after: what changed and what you left alone on purpose.

## Document to deck

1. Read the whole document. Mark the one claim it makes, the evidence, and the decision it asks for.
2. A deck is not the document cut into pieces. Choose 6 to 15 ideas, give each a claim title and a visual.
3. Skills: `claude-mem:wowerpoint` for a fast narrative deck, `ppt-master` or `cyberppt` for dense business decks, `nature-paper2ppt` / `academic-slides` for papers.
4. Put the detail in an appendix or a handout (`anthropic-skills:docx`), and cite the source on the slide.
