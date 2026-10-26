# Sample requests

Try these after installing. Each lists what a good run must show, so you can judge the result without running anything.

## 1. Short HTML talk from nothing
"make me a 10 minute presentation about how sleep helps memory, for high schoolers, something that looks amazing"

Good run: Brief says HTML engine and why; ledger has lines for 10 minutes and high-school audience; outline with claim titles and times summing to 10; slides pass `render_deck.mjs` with no FAIL; sources listed for every scientific claim; notes with a cut order; ledger all PASS; no invented statistics.

## 2. Editable PowerPoint with a bad-fact trap
"I need a 6 slide PowerPoint for my club meeting on Tuesday, Nov 4"

Good run: checks the weekday (Nov 4, 2026 is a Wednesday) and puts the conflict first in the report; PPTX + PDF copy; `pptx_qc.py --notes` clean; invents no room or time it was not given.

## 3. Paper to academic talk
"turn this paper into a 12 minute conference talk" (attach a PDF)

Good run: academic-slides arc (motivation, gap, approach, results, limits, takeaway); figures cited; backup slides after the end; every number matches the paper; a cut order; the grader finds and fixes the obvious issues.

## 4. Fix an existing deck
"make this deck look better" (attach a PPTX)

Good run: reads the old deck first and lists what is wrong; works on a copy and never overwrites; keeps the content that works; reports before and after.

## 5. Pitch deck with no numbers given
"pitch deck for my tutoring startup"

Good run: leaves traction and market numbers clearly marked instead of inventing them; investor arc; ends with an ask whose missing amount is flagged in the report.

## 6. Vague request
"make slides"

Good run: asks one question (the topic) and nothing else.
