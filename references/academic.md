# Academic and scientific decks

Why this file exists: academic audiences judge reasoning and evidence, so structure and citation matter more than style. Read this for any conference talk, thesis defense, lab meeting, journal club or grant briefing.

Contents: Structures · Figures and tables · Citations · Time and rehearsal · Q&A and backup slides · Format choice · Traps

## Structures

**Conference talk (10 to 20 min)**: title and one-sentence takeaway; motivation (why anyone should care); the gap; your approach in one picture; key result 1, 2, 3 (one slide each, with the figure); limits; conclusion repeating the takeaway; acknowledgements. About 1 slide per minute; fewer in the middle.

**Thesis defense (30 to 60 min)**: roadmap, background and question, aims, methods, results by aim, integrated discussion, contributions, limits and future work, thanks. Add a roadmap marker slide between chapters so examiners can track.

**Lab meeting or journal club**: why this paper, the question, methods in one figure, results with the paper's figures, critique (strengths, weaknesses, alternative explanations), what it means for our work, discussion questions.

**Grant briefing**: problem, significance, aims, approach, preliminary data, timeline, team, budget, impact.

## Figures and tables

- One figure per message. Enlarge the figure and crop away what is not discussed. Redraw unreadable figures instead of pasting a tiny screenshot.
- Axes labelled, units shown, fonts at or above the floors in `craft.md` after scaling.
- Highlight the comparison that matters (colour, arrow, box); grey the rest.
- Tables show the three numbers you will talk about, not twenty. Full tables go to the appendix.
- Cite the source of any figure that is not yours on the slide, small.

## Citations

- Cite on the slide in short form (Author Year) for every claim from the literature, with a references slide at the end.
- Verify each reference exists and says what you claim (use `deep-research`, `ecc:scientific-db-pubmed-database`, the paper itself). Never invent a citation. Unverified becomes "needs source" in the report.
- Keep numbers (sample sizes, effect sizes, p-values, confidence intervals) exactly as in the paper.

## Time and rehearsal

- Count about 1 to 2 minutes per slide of content. Rehearsal time is part of the plan: put target times in the notes and a cut order for overrunning.
- Write the opening sentence and the closing sentence of the talk word for word in the notes.
- Plan the first 30 seconds and the last 30 seconds; they are what the audience remembers.

## Q&A and backup slides

- After the final slide, add a backup section: extra analyses, robustness checks, full tables, alternative explanations, method details, the data you would show if asked.
- In the notes of the main slides, list the likely questions and which backup slide answers them.
- A final slide that shows the takeaway and your contact, not "Questions?" alone, stays up during Q&A.

## Format choice

| Need | Use |
|---|---|
| Equations, theorems, algorithms, LaTeX workflow | Beamer (`beamer`, `beamer-academic`, `presenting-conference-talks`) |
| Editable, collaborators will change it, department template | PPTX (`ppt-master`, `academic-ppt-master`, `thesis-defense-pptx`, or `anthropic-skills:pptx` on the template) |
| Chinese-language paper reports | `nature-paper2ppt` |
| Story and structure first | `academic-slides`, `academic-pptx` as the content layer on any engine |

Use the department or conference template when one exists. Colour-blind safe palettes for figures.

## Traps

- Reading from the slides; slides that are the paper pasted in.
- Methods before the question is clear.
- Unlabelled axes, tiny legends, figures copied at low resolution.
- No limits slide (examiners will find the limits for you).
- Overrunning: no cut order.
- Claiming more than the data shows. Say "suggests" when the evidence suggests.
