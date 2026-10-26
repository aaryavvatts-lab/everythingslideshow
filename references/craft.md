# Slide craft: the floors and the rules

Why this file exists: most bad decks fail in the same few ways (too much text, tiny type, no point, no visual, no ending). These are the floors that stop that. Read before building, and again during Round 2.

Contents: Message and story · Density · Type · Colour and contrast · Layout · Images · Charts and data · Diagrams · Motion · Speaker notes · Accessibility · AI-slop patterns to remove · Reading decks vs speaking decks

## Message and story

- One deck, one message, stated in a sentence you could say out loud in 10 seconds.
- Titles are claims. "Sleep is when memories get filed" teaches; "Sleep" labels. A reader who only reads titles should get the whole argument.
- One idea per slide. Two ideas means two slides.
- Open with something the audience cares about (a question, a stake, a true surprising fact). Close with what they should do or remember. "Thank you" alone is not a close.
- Order by the audience's questions, not by how you found things out.
- Appendix and backup slides hold the detail you may need in Q&A, so the main deck stays lean.

## Density

| Deck kind | Words per slide | Bullets | Notes |
|---|---|---|---|
| Speaker-led (talk, keynote, class) | 6 to 30, 50 at most | 0 to 3 short lines | The slide supports the voice. Visual first. |
| Mixed (workshop, training) | 30 to 70 | up to 5 | Activity instructions can be longer if they are scannable. |
| Reading deck (sent by email, report, handout) | 70 to 150 | structured cards, tables | Must still make sense with no speaker. |

If content exceeds the mode, split the slide. Do not shrink type to fit.
A bullet is a short phrase (under 12 words), not a sentence from a paper.

## Type

Sizes below are floors for projected slides. They assume a 13.33 x 7.5 in PPTX or a 1920 x 1080 HTML stage.

| Role | PPTX | HTML (1920 wide) |
|---|---|---|
| Title | 32 to 44 pt | 56 to 96 px |
| Body | 24 pt minimum (28 is better) | 32 px minimum |
| Labels, captions | 16 pt minimum | 22 px minimum |
| Source and footer lines | 12 pt minimum | 18 px minimum |

- At most two font families: one for headlines, one for text (or one family in two weights). Use a size scale (for example 1.25 ratio) so sizes feel related.
- Left-align body text. Centre only short titles or single statements. Never justify.
- Line length 40 to 70 characters; line height 1.2 to 1.5.
- Tabular numerals for numbers in columns.
- Do not put long text in all caps. Do not use more than two weights on a slide.
- Fonts must exist on the machine that will present them; otherwise embed or bundle (see `formats.md`).

## Colour and contrast

- One dominant colour, one accent, neutrals. Sharp accents on a calm base beat an evenly spread rainbow.
- Contrast ratio at least 4.5:1 for normal text and 3:1 for large text (24 pt and up). Light grey on white fails; test it.
- Text over photos needs an overlay or a quiet area of the image.
- Never use colour alone to carry meaning (red versus green only). Add a label, shape or pattern.
- Dark backgrounds suit dim rooms and video; light backgrounds suit bright rooms and anything printed.
- Use the user's brand colours exactly when they gave them.

## Layout

- One focal point per slide. Squint test: blur your eyes, and one thing should still stand out.
- Margins of at least 5 percent of the width on every side. Nothing important in the outer 3 percent (projectors crop).
- Use a grid. Align left edges. Repeat positions for title, footer and slide number on every slide.
- Whitespace is not empty; it is what makes the focal point readable.
- Vary layouts for rhythm (full-bleed image, big number, two-column, quote, diagram) but keep one visual system. Avoid ten identical bullet slides in a row.
- Section dividers help in decks over about 12 slides.

## Images

- Real beats generic. A screenshot, a photo from the event, a diagram of the real system, a figure from the paper (with citation).
- Full-bleed images need at least the stage width in pixels (1920 px) and no visible stretching or compression artefacts.
- Crop on purpose. Keep faces and key detail inside the safe area.
- One visual style across the deck (all photos, or all flat illustrations; do not mix random clip-art).
- Add alt text to every meaningful image. Mark decoration as decoration.
- Check generated images for garbled text, wrong anatomy, impossible details. Never present a generated image as a real photo of a real event.
- Credit sources on the slide (small) or in the appendix, and list licences in `SOURCES.md`.

## Charts and data

- One message per chart. State it in the slide title ("Revenue doubled after launch"), not "Revenue by quarter".
- Label data directly instead of using a legend when possible. Label axes with units.
- Bars start at zero. Do not use 3D, pies with more than four slices, or dual axes unless the audience is expert.
- Use at most six colours; highlight the one series that matters and grey the rest.
- Show the source and date in a small line.
- Use the `dataviz` skill rules for palettes and stat tiles.
- Big numbers beat tiny tables: one number at 120 pt with a one-line label.

## Diagrams

- Left to right or top to bottom, five to seven boxes at most per slide; split complex systems across slides or build up in steps.
- Consistent shapes and meaning (a box type always means the same thing). Arrows are labelled if direction alone is not obvious.
- Text inside diagrams obeys the type floors. If it cannot, the diagram is too big for one slide.

## Motion

- Animate to reveal or explain (a step appearing as you say it, a morph that shows change), never to decorate.
- Reveal order matches speaking order. Durations 200 to 500 ms. One transition style across the deck.
- Nothing auto-advances in a live talk. Self-running decks time every slide to the narration.
- HTML: respect `prefers-reduced-motion`. PPTX: avoid transitions that fail in Google Slides or Keynote.
- Embedded video: test playback in the target program; give a fallback still.

## Speaker notes

- Conversational prose the speaker can glance at, not a copy of the slide. What to say, when to pause, what to click.
- Put the timing at the top of the note and a cut order in the agenda notes ("if short on time, skip slides 7, 9, 11").
- Put answers to likely audience questions on the slide where they are likely asked.
- House skills may define a stricter script format (WAIT steps, answer keys). Follow them.

## Accessibility

- Contrast, size and alt text as above. Reading order set so screen readers get the title first.
- Captions or a transcript for narrated or video content.
- Avoid flashing content. Provide non-colour cues. Use plain language.

## AI-slop patterns to remove

Generic output shows itself in the same ways. If you see these, rewrite:

- Purple-to-blue gradients on white; gradient text; glowing orbs; random blobs.
- Three identical rounded cards with an emoji icon each, used on every slide.
- Everything centred; every title the same size; no visual hierarchy.
- Emoji as bullets; icons that decorate and mean nothing.
- Filler titles: "Key Takeaways", "Let's Dive In", "The Future of X", "Overview".
- Stock-photo clichés (handshakes, lightbulbs, people pointing at a whiteboard).
- Openers such as "In today's fast-paced world", closers such as "In conclusion".
- Invented statistics or round numbers with no source.
- Dash sprays: stringing clauses with em dashes. Use commas, periods or colons; many users ban them outright.
- Text that restates the title in the first bullet.
- Headline plus three bullets repeated on every slide.

## Reading decks vs speaking decks

Ask which this is in Phase 1 and design to it. A speaker-led deck that carries a reading deck's density loses the room; a reading deck that is all big pictures confuses the reader. When a deck must serve both, build the speaking deck and add a handout or a notes document for the detail.
