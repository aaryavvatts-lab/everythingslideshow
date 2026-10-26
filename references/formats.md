# Formats and export recipes

Why this file exists: choosing the wrong format is the most expensive mistake in slide making, because everything is rebuilt. Decide in Phase 2; use the recipes in Phase 8.

Contents: Choosing a format · What survives each conversion · Recipes · Fonts · Opening and presenting tips

## Choosing a format

| The user says or needs | Format | Why |
|---|---|---|
| "Teacher/boss wants a file", "I'll edit it later", "PowerPoint", "Google Slides" | PPTX (+ PDF copy) | Everyone can open and edit it |
| "Send a link", "make it impressive", presenting from my own laptop | HTML (single file) (+ PDF copy) | Best visuals, animations, no install |
| Math, equations, a thesis, conference proceedings | Beamer PDF (+ PPTX if asked) | Typesetting quality, version control |
| Markdown notes, code, wants it in git | Marp or reveal.js | Text-first, exports to HTML, PDF, PPTX |
| Handout, read alone | PDF | Opens anywhere, fixed layout |
| Video or self-running | MP4 or narrated HTML | See narrated recipe in `recipes.md` |
| Unknown | PPTX + PDF; offer HTML in the report | Safest default |

## What survives each conversion

| From to | Survives | Lost or risky |
|---|---|---|
| PPTX to PDF | Layout, images, fonts (if installed) | Animations, embedded video, notes (unless exported) |
| HTML to PDF | Static layout when print CSS or a fixed stage is used | Animations, interactivity, WebGL backgrounds |
| HTML to PPTX | Text, shapes, images when built with a converter (`html-slide-to-pptx`) | Animations, custom fonts, complex CSS; check every slide |
| PPTX to HTML | Text and images (`frontend-slides` conversion mode) | Custom shapes, SmartArt, charts may flatten |
| PPTX to Google Slides | Text, images, basic shapes, most layouts | Custom fonts, some effects, animations differ |
| Image-based decks to PPTX | Looks | Text is not editable unless rebuilt (`nature-image2ppt`, `gorden-super-ppt`) |
| Beamer PDF to PPTX | Looks only | Equations become pictures unless rebuilt |

Pick the engine for the format that matters most, then export the others. Never promise a conversion you did not test.

## Recipes

**HTML deck to PDF** (fixed 1920x1080 stage)
- If the engine ships an exporter (`frontend-slides` has `scripts/export-pdf.sh`), use it.
- Otherwise print each slide from headless Chrome:
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --print-to-pdf=deck.pdf --no-pdf-header-footer --virtual-time-budget=4000 "file:///abs/path/deck.html"
```
  Decks that show one slide at a time need `@media print` CSS that shows every slide with `page-break-after: always`. Check the PDF page count equals the slide count.
- Or screenshot every slide with `scripts/render_deck.mjs` and join the PNGs into a PDF with Pillow (`images[0].save("deck.pdf", save_all=True, append_images=images[1:])`). The result is not searchable text; say so.

**PPTX to PDF**
- LibreOffice: `soffice --headless --convert-to pdf deck.pptx`.
- macOS without LibreOffice: open in Keynote or PowerPoint and export; or use `scripts/render_static.py` for pictures only.

**PPTX to PNG per slide**: `python3 scripts/render_static.py deck.pptx --out qc/`.

**HTML to PPTX**: use `html-slide-to-pptx` (editable) or screenshot-based export (not editable; say so).

**PPTX to Google Slides**: Google Drive, New, File upload, then open with Google Slides; or Slides, File, Import slides. House skills may carry their own Drive steps. Uploading is the user's call.

**Single-file HTML for email or USB**: inline CSS and JS, base64 small images, no external fonts unless a fallback stack exists. Test with the network off.

**Compress**: images to WebP or JPEG at 1920 px wide with `baoyu-compress-image`; target a deck under 25 MB if it will be emailed.

## Fonts

- A font that is not on the presenting computer is replaced silently, and that changes line breaks and overflows boxes.
- Safe choices: fonts that ship with the OS or Office, or Google Fonts for HTML decks (loaded with a fallback stack and tested offline).
- PPTX: embed fonts where the program allows, otherwise use a common font or convert key headline text to images (accept that it is no longer editable).
- Say in the report which fonts the deck needs.

## Opening and presenting tips to give the user

- HTML: open in Chrome or Edge, arrow keys or space to move, F for fullscreen, S or P for presenter view if the engine has it, Esc leaves fullscreen. Test on the real projector's resolution.
- PPTX: Slide Show, From Beginning; Presenter View shows notes (needs two screens or a second window).
- Bring the PDF copy on a USB drive and upload it to a cloud drive as backup.
- Test videos, audio and links on the actual machine in the actual room.
