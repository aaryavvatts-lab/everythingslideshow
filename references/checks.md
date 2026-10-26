# Checks, grading and the ledger

Why this file exists: "looks fine to me" is how bad decks ship. These templates make the checks specific, so a second reader (or a script) can confirm them.

Contents: Requirements ledger · CHECKS.md template · Round 2 checklist · Round 3 rubric · Grader prompt · When to stop

## Requirements ledger (`ledger.md`)

Write it in Phase 1, before choosing anything. Each line is one checkable requirement.

```markdown
# Requirements ledger: <deck name>
Original request (verbatim): "<the user's words>"

## Asked
| ID | Requirement | How to verify | Status | Evidence |
|---|---|---|---|---|
| R1 | 12 slides or fewer | count slides | | |
| R2 | Uses school colours (navy and gold) | look at contact sheet; hex values in CSS/theme | | |
| R3 | Includes speaker notes on every slide | pptx_qc.py --notes | | |
| R4 | Ends with the sign-up QR | last slide image | | |

## Implied
| ID | Requirement | How to verify | Status | Evidence |
|---|---|---|---|---|
| I1 | Readable from the back of the room | type floors in craft.md; render at 1920x1080 | | |
| I2 | Opens on the user's machine (format they named) | reopen the file; PDF copy exists | | |
| I3 | Fits the time slot with a cut order | outline_lint.py; notes | | |
| I4 | Every fact has a source | SOURCES.md | | |
| I5 | Banned punctuation absent (if the user has such a rule) | pptx_qc.py --no-dashes / grep | | |
```

Rules: split compound requests into separate lines ("a QR and a join link" is two). Write requirements so the answer is PASS or FAIL, not "sort of". Keep the user's own words in the Asked table. Add lines when house skills or saved preferences add rules.

## CHECKS.md template

```markdown
# Checks: <deck name>
Date: <date>   Job size: Light | Full   Engine: <skill>   Skills used: <list>

## Round 1: Technical
Tools run: <render_deck.mjs | pptx_qc.py | render_static.py | compile log>
FAIL found: <n> -> fixed: <list>
WARN found: <n> -> fixed: <list>; explained: <list>
Not checked (tool missing): <list or "none">

## Round 2: Look and read
Slides reviewed one by one: yes/no
Problems found and fixed: <list with slide numbers>
Slop check: <result>   Copy pass (humanizer, banned punctuation): <result>
Facts re-verified against sources: <list>

## Round 3: Grade
Grader: independent subagent | self
| Dimension | Score | Notes |
| Message clarity | | |
| Story flow | | |
| Slide design | | |
| Readability | | |
| Evidence and accuracy | | |
| Audience fit | | |
| Delivery readiness | | |
| Polish and consistency | | |
Fixes made for scores under 4: <list>   Re-score: <scores>

## Ledger result
<n> of <n> requirements PASS. Remaining gaps: <list or "none">
```

## Round 2 checklist (go slide by slide)

Look at each slide at full size, not only the contact sheet.

Deck level
- [ ] Looks like one deck: same fonts, colours, margins, title position, footer.
- [ ] Rhythm: no run of more than three similar layouts; at least one visual-first slide per five.
- [ ] Titles alone tell the story.
- [ ] Opening earns attention; ending says what to do or remember.
- [ ] Slide count and time fit; cut order exists for live decks.

Slide level
- [ ] Nothing cut off, overlapping, crowded or off-centre by accident.
- [ ] Smallest text is at or above the floor in `craft.md` and readable at distance.
- [ ] Contrast passes, including text over images.
- [ ] Images sharp, not stretched, cropped on purpose; alt text present.
- [ ] Charts: the title states the takeaway, axes and units labelled, source shown.
- [ ] Each fact, number and name is right and sourced; dates and weekdays agree.
- [ ] No placeholder text, no "lorem", no leftover instructions to self.
- [ ] No AI-slop patterns (see `craft.md`).
- [ ] Banned punctuation or words the user listed are absent.
- [ ] Links and QR codes work.
- [ ] Notes present, in order, match the slide, include timing.
- [ ] Animations: reveal order matches speech; nothing waits on the presenter.

## Round 3 rubric

Score 1 to 5 per dimension. 5 = would stand next to a professionally made deck. 3 = acceptable but visibly average. 1 = fails the purpose. Anything under 4 gets fixed.

| Dimension | A 5 looks like | A 3 looks like | A 1 looks like |
|---|---|---|---|
| Message clarity | One sentence says what the deck proves and every slide serves it | Message exists but a few slides drift | Cannot say what the deck is for |
| Story flow | Each slide answers the question the last one raised; strong open and close | Logical but flat; ending fizzles | Slides could be shuffled with no loss |
| Slide design | Clear hierarchy, whitespace, purposeful visuals, one system | Tidy but template-like | Cluttered, inconsistent, decorative |
| Readability | Readable from the back; contrast and size pass everywhere | Mostly readable; a few small or low-contrast spots | Text too small, dense or low-contrast |
| Evidence and accuracy | Every claim sourced, numbers check, charts honest | Mostly right; a few unsourced claims | Wrong or invented facts |
| Audience fit | Language, depth and tone match who is in the room | Slightly too expert or too basic in places | Wrong level or tone for the audience |
| Delivery readiness | Notes, timing, cut order, demo and backup plan all there | Notes thin or timing unclear | Cannot be presented without redoing |
| Polish and consistency | No typos, no misalignments, assets crisp, file opens everywhere | A few small slips | Obvious errors throughout |

## Grader prompt (Full jobs)

Give a fresh subagent the files, not your opinion of them. Do not tell it the scores you expect.

```
You are a skeptical expert in the audience for this presentation. You have not seen how it was made.

Context
- Brief: <paste the Deck Brief>
- Requirements ledger: <path to ledger.md>
- Outline: <path>, speaker notes: <path>
- Pictures: contact sheet <path>, key slides <paths>
- Automated reports: <paths to qc.json / pptx_qc output>
- Rubric: <path to this file, section Round 3 rubric>

Do this in order
1. Before scoring, list every mistake you can find: wrong or unsourced facts, unreadable text, layout problems, story gaps, places the notes contradict the slide, anything that does not match the brief or the ledger. Give each a slide number and a one-line fix.
2. Then score each rubric dimension 1 to 5 with a one-sentence reason.
3. Say in two sentences whether you would be glad to sit through this deck, and why or why not.
Do not praise to be polite. Do not change any files.
```

Apply the fixes it finds, then re-run Round 1 on changed slides and re-score once. Disagree with a finding only when you can point to the evidence (a source, a measurement).

## When to stop

Stop when: the ledger is fully PASS, every Round 3 score is 4 or more, and Round 1 has no FAIL. Or after three fix passes, in which case say plainly what is still not perfect. More polish past that point rarely helps the audience.
