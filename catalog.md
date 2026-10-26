# everythingslideshow catalog

Every skill `/everythingslideshow` can bring in, grouped by the job it does. Each row: the skill (linked to its source when it has a public one), what it does, and when to reach for it.

- Run `bash scripts/check_skills.sh --missing` to see which of these are installed on this machine.
- Run `bash scripts/install_companions.sh --core` (or `--all`) to install the open-source ones.
- A skill with a colon (`ecc:frontend-slides`) comes from a plugin. If a skill is missing, say so in one line and use the next best one in the same group. Only Node, Python 3 and a browser are truly needed; the scripts in this repo are the fallback for everything else.

Contents: 1 HTML decks · 2 Editable PowerPoint · 3 Academic and science · 4 Markdown, code and framework decks · 5 Image-first decks · 6 Narrated and video decks · 7 Story, copy and notes · 8 Visual design and style · 9 Diagrams, charts, infographics, images · 10 Research and facts · 11 Motion · 12 Review and quality · 13 Office and file helpers · 14 House skills

## 1. HTML decks (live in a browser, animated, shareable by link)

| Skill | What it does | Use it when |
|---|---|---|
| [`frontend-slides`](https://github.com/zarazhangrui/frontend-slides) | Zero-dependency HTML decks on a fixed 1920x1080 stage, 16 style presets, shows visual previews so non-designers can pick a look, converts PPTX to web. | Default for a polished live talk, pitch or workshop in the browser. |
| [`huashu-design`](https://github.com/alchaincyf/huashu-design) | HTML-native design skill: always proposes three directions first, then builds slides, prototypes or motion; exports HTML, editable PPTX, MP4. 20 design philosophies, 5-dimension critique. | The deck must look like a design team made it, or the user wants to choose between directions. |
| [`html-ppt`](https://github.com/lewislulu/html-ppt-skill) | "HTML PPT Studio": many themes, layouts and animations driven by templates, speaker mode, keyboard navigation. | Tasteful template-driven decks fast; talks, reports, tech sharing. |
| [`guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) | Horizontal-swipe single-file HTML decks with WebGL backgrounds, presenter view, audience sync, two styles (editorial magazine, Swiss). AGPL-3.0 licence. | A launch-event or keynote feel with a striking editorial look. |
| [`frontend-slides-editable`](https://github.com/archlizheng/frontend-slides-editable) | frontend-slides fork whose output stays editable in the browser (drag objects, reorder, save, export). | The user will keep tweaking the deck by hand after you hand it over. |
| [`kai-slide-creator`](https://github.com/kaisersong/slide-creator) | Stable HTML deck generator with core styles and presenter mode. | Roadshows, product talks, sharing sessions. |
| [`claude-slides`](https://github.com/marcogalluccio/claude-slides) | HTML deck stage 1920x1080 with keyboard navigation, progress bar, fullscreen, step reveals. Neutral brand via CSS variables. | Workshops, demos, event recaps projected live. |
| [`visual-cognition-slides`](https://github.com/edu-ai-builders/visual-cognition-slides) | Slides designed around how people perceive and remember visuals. | Teaching decks where learning and recall matter more than flash. |
| [`visual-explainer`](https://github.com/nicobailon/visual-explainer) | Turns anything into rich, self-contained HTML pages (diagrams, comparisons, recaps). | One explainer page or a visual summary rather than a classic deck. |
| `visual-explainer:generate-slides` | Same project's command that outputs a slide deck as a self-contained HTML page. | Quick technical deck from code, a plan or a project. |
| [`ecc:frontend-slides`](https://github.com/affaan-m/everything-claude-code) | Plugin version of animation-rich HTML slides. | Fallback when `frontend-slides` is not installed. |
| [`fs-tightened-slide`](https://github.com/humantonylee/future-slide) | Single-file HTML horizontal-swipe decks with locked layouts, strict grid, theme presets, image-slot discipline, validation. | Strict, consistent layout discipline across a long deck. |
| [`slideshow`](https://github.com/heygen-com/hyperframes/tree/HEAD/skills/slideshow) | HyperFrames live-presented HTML deck with fragment reveals, branching hotspots and presenter mode. | Interactive, branching or choose-your-own-path presentations. |
| [`html-to-bento-slides`](https://github.com/mucsbr/ppt-agent-workflow-san) | Converts an existing HTML deck into an editable bento-style deck. | The user already has an HTML deck to migrate. |
| [`fs-html-slide`](https://github.com/humantonylee/future-slide) | Staged HTML slide pipeline: design extraction, plan, prompts, render. | A deck built from a reference design with strict stages. |

## 2. Editable PowerPoint (.pptx)

| Skill | What it does | Use it when |
|---|---|---|
| [`ppt-master`](https://github.com/hugohe3/ppt-master) | Full AI workflow to create, reconstruct, beautify and template editable PPTX decks, with optional narration and animation. Most-starred slide skill. | Default for a real, editable PowerPoint with strong design. |
| [`anthropic-skills:pptx`](https://github.com/anthropics/skills/tree/HEAD/skills/pptx) | Anthropic's PPTX skill: read, create and edit .pptx files. | Any plain PowerPoint job; the base for editing someone's existing deck. |
| [`ppt-agent`](https://github.com/Akxan/ppt-agent-skill) | Consultant-style pipeline: requirements, research, outline, storyboard, design; outputs HTML slides. | Report-to-the-boss and training decks where research and structure matter. |
| [`ppt-workflow`](https://github.com/mucsbr/ppt-agent-workflow-san) | Staged workflow (brief, facts, outline, page plan, reviewable artifacts) that adapts to what the machine can do. | Planning-heavy decks, or when tools are limited. |
| [`ppt-svg-generator`](https://github.com/vigorX777/ppt-svg-generator) | Markdown to SVG pages that paste into PowerPoint and convert to editable shapes. | Vector-quality slides from a text draft. |
| [`mck-ppt-design`](https://github.com/likaku/Mck-ppt-design-skill) | python-pptx engine with 67 high-level slide methods in consultant style (charts, timelines, dashboards). | Business, strategy and board decks. |
| [`rw-consulting-ppt`](https://github.com/Pikapika260214/rw-consulting-ppt) | Consulting-style editable PPT workflow. | Consulting-look decks. |
| [`cyberppt`](https://github.com/crazyykhllc-bit/CyberPPT) | Turns DOCX, PDF, XLSX or reports into dense, editable, consulting-style PPTX with SCR arguments and render checks. | A long report or data pack must become a dense deck. |
| [`mckinsey-style-viz`](https://github.com/kgraph57/mckinsey-style-visualization-skill) | Strategy-consulting visuals: board slides, diagrams, quiet animated or interactive decks. | Executive audiences and evidence-led storytelling. |
| [`html-slide-to-pptx`](https://github.com/mucsbr/ppt-agent-workflow-san) | Converts fixed-layout HTML slides to editable PPTX with native text boxes and shapes. | You built the deck in HTML but the user needs PowerPoint. |
| [`nature-image2ppt`](https://github.com/yuan1z0825/nature-skills) | Rebuilds slide images, screenshots or scanned PDFs as object-level editable PPTX. | The only source is pictures of slides. |
| [`visual-style-ppt`](https://github.com/irenerachel/visual-style-ppt-skill) | PPT built around a chosen visual style. | The user names a look to match. |
| [`uiux-slides`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX Pro Max's slide skill: strategic HTML decks with design tokens and Chart.js. | Pitch and strategy decks tied to a design system. |
| [`marswave-slides`](https://github.com/marswaveai/skills) | Slide deck from a topic, URL or text. | Quick deck from a link or paste. |
| [`slides`](https://github.com/Rich627/slides-skill) | General slide-building skill. | Light fallback for a simple deck. |
| [`slide-design`](https://github.com/hunkim/slide-skill) | Design-led slide skill. | Light fallback for design polish. |
| [`soft-3d-clay-ppt-skill`](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | PowerPoint style pack: soft 3D clay look. | A friendly, playful deck. |
| [`futuristic-tech-editorial-ppt-skill`](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | Style pack: editorial futuristic tech magazine. | AI, product and engineering decks. |
| [`japanese-style-ppt-skill`](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | Style pack: washi paper or Japanese lifestyle magazine. | Calm, humanities, brand-story decks. |
| [`japanese-hand-drawn-editorial-ppt-skill`](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | Style pack: pencil and watercolor editorial. | Soft, human, creative-process decks. |
| [`minimalist-luxury-branding-ppt-skill`](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | Style pack: beige, serif, premium restraint. | Brand strategy, founder and premium proposal decks. |
| [`modern-illustration-editorial-ppt-skill`](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | Style pack: soft vector illustration editorial. | Illustrated explainers and product storytelling. |

## 3. Academic and science

| Skill | What it does | Use it when |
|---|---|---|
| [`academic-slides`](https://github.com/EvoScientist/EvoSkills) | Shapes the deck and the talk: narrative arc, slide breakdown, rehearsal, timing, Q&A and backup slides, then the .pptx. | Default for conference talks, thesis defenses, lab meetings, paper-to-slides. |
| [`academic-pptx`](https://github.com/Gabberflast/academic-pptx-skill) | Content and structure rules for evidence-judged audiences (seminars, defenses, grant briefings). Pair with a PPTX engine. | The audience will test the reasoning. |
| [`academic-ppt-master`](https://github.com/M1n-n9/academic-ppt-master) | Paper, PDF or Markdown into editable academic PPTX via an SVG workflow. | Journal club and paper-reading decks. |
| [`thesis-defense-pptx`](https://github.com/zouchenzhen/thesis-defense-pptx-skill) | Thesis defense deck workflow. | Defenses and proposal talks. |
| [`presenting-conference-talks`](https://github.com/orchestra-research/ai-research-skills) | Beamer PDF and editable PPTX from a compiled paper, with speaker notes and a talk script. | ML and systems conference talks. |
| [`beamer`](https://github.com/Noi1r/beamer-skill) | Create, compile, review and polish Beamer LaTeX slides with quality scoring and TikZ audit. | The user wants LaTeX/Beamer or math-heavy slides. |
| [`beamer-academic`](https://github.com/Faust-Donf/beamer-academic) | Beamer slides from a thesis or paper with 13 page layouts and 5 colour schemes. | Thesis defense in Beamer. |
| [`nature-paper2ppt`](https://github.com/yuan1z0825/nature-skills) | Chinese academic PPTX from a paper, with source figures and speaker notes. | Group meetings and journal reports in Chinese. |
| `academic-paper` | Academic paper writing skill. | The deck is built on a paper that still needs writing. |
| `academic-pipeline` | End-to-end research-to-paper pipeline. | A talk grows out of a larger research project. |
| `science-editor` | Edits scientific writing for clarity and accuracy. | Slide text states scientific claims that need checking. |
| `ecc:scientific-thinking-literature-review` | Structured literature review method. | The deck needs a related-work or evidence-map slide. |
| `ecc:scientific-db-pubmed-database` | PubMed search patterns. | Biomedical facts and citations. |
| `ecc:manim-video` | 3Blue1Brown-style math animation. | A derivation or concept needs a real animation to embed. |
| `textbookmaker` | Builds an interactive textbook site from an idea. | The "slideshow" is really a course or long-form learning resource. |

## 4. Markdown, code and framework decks

| Skill | What it does | Use it when |
|---|---|---|
| [`marp-slides`](https://github.com/robonuggets/marp-slides) | Marp decks with SVG charts, dashboard components, animation, dark/light themes. | Markdown source that exports to HTML, PDF or PPTX. |
| [`slide-story`](https://github.com/minorun365/minorun-marp-skill) | Marp workflow part 1: story and structure. | Marp decks that need a strong narrative. |
| [`slide-figures`](https://github.com/minorun365/minorun-marp-skill) | Marp workflow part 2: figures and diagrams. | Marp decks with figures. |
| [`slide-design-dark`](https://github.com/minorun365/minorun-marp-skill) | Marp workflow part 3: dark design theme. | Dark-theme Marp decks. |
| [`revealjs`](https://github.com/ryanbbrown/revealjs-skill) | reveal.js presentation builder. | The user asks for reveal.js, or wants code, math and plugins. |
| [`borghei-md-slides`](https://github.com/borghei/Claude-Skills) | Markdown to a self-contained HTML deck with layouts, notes, navigation and a content-density linter. | Fast deck from an outline file, and a density check. |
| [`open-slide-create-slide`](https://github.com/open-slide/open-slide) | Authors React slides inside an open-slide repo (1920x1080 canvas, transitions, notes). | The project already uses open-slide, or the user wants React-based decks. |
| [`open-slide-slide-authoring`](https://github.com/open-slide/open-slide) | Technical reference for open-slide pages (type scale, reveals, morph transitions). | Any edit inside an open-slide repo. |
| [`open-slide-create-theme`](https://github.com/open-slide/open-slide) | Creates or extracts reusable open-slide themes. | A reusable theme from a reference deck. |
| `ecc:ui-demo` | Records polished UI demo videos from a web app. | A product walkthrough clip to embed in the deck. |

## 5. Image-first decks (each slide generated as a picture)

| Skill | What it does | Use it when |
|---|---|---|
| [`baoyu-slide-deck`](https://github.com/jimliu/baoyu-skills) | Outline with style instructions, then each slide generated as an image. | Beautiful poster-like slides where editability does not matter. |
| [`codex-ppt`](https://github.com/ningzimu/codex-ppt-skill) | Visually unified image-based PPT/PPTX from articles, reports, notes. | Same idea, with PPTX packaging. |
| [`ppt-image-first`](https://github.com/NyxTides/ppt-image-first) | Conversation first, then several visual directions with preview images before any spec. | The user is unsure about the look and wants to see options. |
| [`fs-gpt-image-slide`](https://github.com/humantonylee/future-slide) | End-to-end GPT-image deck from a reference slide, source files and a prompt (plan, prompt, render stages). | Consistent image decks from a reference design. |
| [`fs-slide-design`](https://github.com/humantonylee/future-slide) | Extracts a reusable DESIGN.md from reference visuals. | You have a reference deck or screenshot to match. |
| [`gorden-super-ppt`](https://github.com/GordenSun/GordenSuperPPTSkills) | Makes an image-style deck, then rebuilds it as an editable pptx. | The user wants both beauty and editability from just a topic. |
| [`gpt-image`](https://github.com/wuyoscar/GPT-Image2-Skill) | GPT Image 2/2.5 generation and editing. | Slide art, posters, typography images. |
| [`baoyu-image-gen`](https://github.com/jimliu/baoyu-skills) | Image generation across many providers. | Illustrations and hero images; needs the user's own API keys. |
| `imagegen-frontend-web` | Section-by-section design reference images. | Plan the look as pictures before building. |
| `claude-mem:wowerpoint` | One document into a NotebookLM-style narrative slide deck. | The user hands you one document and wants a shareable summary deck. |

## 6. Narrated and video decks

| Skill | What it does | Use it when |
|---|---|---|
| [`glebis-present`](https://github.com/glebis/claude-skills) | Interactive HTML presentation with ElevenLabs voiceover synced to slides, article and slides dual mode. | A self-running narrated deck or briefing. |
| `visual-explainer:generate-video` | Narrated MP4 explainer, or a recorded walkthrough of a live web app. | The deck should become a video. |
| `everythingvideo` | Full video studio (script, assets, build, three check rounds). | The user wants a real video made from or alongside the deck. |
| `hyperframes` | HTML-to-video engine and router. | Animated slide-like videos and motion inserts. |
| `explainroo` | Fast voiced explainer MP4 with a local voice, no API key. | A narrated explainer fast and free. |
| `text-to-speech` | ElevenLabs voice. | Voiceover for a narrated deck (needs a key). |
| `music` | Background music generation. | Ambient music for a narrated or auto-play deck. |
| `dubbing` | Translate and dub audio. | A second-language version of a narrated deck. |

## 7. Story, copy and speaker notes

| Skill | What it does | Use it when |
|---|---|---|
| [`slides-narrative`](https://github.com/jameshemson/slides) | Shapes a vague idea into a deck story through back-and-forth, writes a deck spec. | The topic is fuzzy. Run before building. |
| [`slides-presentation-craft`](https://github.com/jameshemson/slides) | Presentation craft principles for structure and delivery. | Any deck: the quality bar for story and slide logic. |
| [`slides-build-deck`](https://github.com/jameshemson/slides) | Renders a deck spec into a finished deck. | After `slides-narrative`. |
| [`slides-slop-check`](https://github.com/jameshemson/slides) | Detects AI-slop patterns in slides. | Review round on every deck. |
| [`slides-revise`](https://github.com/jameshemson/slides) | Revises an existing deck against feedback. | Editing and improving a deck. |
| [`slides-teach-slides`](https://github.com/jameshemson/slides) | Learns the user's slide taste. | The user has a personal style to capture. |
| [`presentation-outline`](https://github.com/aaronvanston/skills-presentations) | Narrative-arc outlines with bold statement slides. | Start of any deck. |
| [`presentation-content`](https://github.com/aaronvanston/skills-presentations) | Bold, minimal slide copy written to be spoken to. | Writing the words on the slides. |
| [`presentation-design`](https://github.com/aaronvanston/skills-presentations) | Layout, type hierarchy and composition guidance. | "How should this slide look?" |
| [`presentation-notes`](https://github.com/aaronvanston/skills-presentations) | Conversational speaker notes and talking points. | Notes for live delivery. |
| [`presentation-pitch-deck`](https://github.com/aaronvanston/skills-presentations) | Investor decks that stand alone (Sequoia and YC structure). | Fundraising or async decks. |
| `ecc:investor-materials` | Investor memo and deck material patterns. | Fundraising content depth. |
| `humanizer-writing-skill` | Rewrites AI-sounding text to plain human prose. | Always for slide text, notes and captions. |
| `no-ai-slop` | Removes generic AI phrasing and patterns. | Second pass on copy. |
| `ecc:article-writing` | Long-form writing patterns. | Turning an article into a deck. |
| `ecc:market-research` | Market sizing and competitor research. | Business and pitch decks that need market slides. |

## 8. Visual design, systems and style

| Skill | What it does | Use it when |
|---|---|---|
| `fulldesign` | One-command design lead that audits a project and picks design skills. | The deck is part of a bigger site or app design job, or a house skill calls for it. |
| `impeccable` | Design-quality bar and anti-slop ruleset. | Final polish of any HTML deck. |
| `ui-ux-pro-max` | Searchable palettes, font pairings, styles and UX rules. | Choose palette and type for a deck without a brand. |
| `design-system` | Design tokens and component specs. | Many-slide decks that need consistent tokens. |
| `frontend-design` | Anthropic guidance for distinctive, non-template visual design. | HTML decks that look generic. |
| `theme-factory` | Ten preset themes or a generated one. | Quick consistent colours and fonts. |
| `brandkit` | Brand guideline boards and logo systems. | The deck needs a brand identity. |
| `canvas-design` | Original posters, covers and static art. | Cover art, section art, thumbnails. |
| `design-taste-frontend` | Anti-slop art direction with a look-and-fix loop. | HTML decks that feel AI-made. |
| `high-end-visual-design` | Premium agency-grade look. | "Premium" or "luxury" briefs. |
| `minimalist-ui` | Quiet editorial minimalism. | "Clean, calm, editorial" briefs. |
| `industrial-brutalist-ui` | Raw, technical, bold. | "Brutalist" or "technical" briefs. |
| `hallmark` | Extracts a design system from a URL or screenshot. | "Make it look like this site." |
| `design-md` | Writes a DESIGN.md from an existing design. | Lock a deck's look for later edits. |
| `apple-design` | Apple-style fluid, restrained design. | Keynote-style polish and motion. |
| `emil-design-eng` | Detail polish philosophy. | The small touches on transitions and hover. |
| `awwwards` | Award-level immersive sites. | A showpiece web presentation. |
| [`glebis-typography`](https://github.com/glebis/claude-skills) | Locale-correct quotes, dashes and spacing. | Multilingual decks (Russian, German, French). |

## 9. Diagrams, charts, infographics, images

| Skill | What it does | Use it when |
|---|---|---|
| `diagram-design` | Architecture, flow, timeline, Sankey and heatmap diagrams as clean SVG. | Any process or system diagram. |
| [`baoyu-diagram`](https://github.com/jimliu/baoyu-skills) | Dark-themed standalone SVG diagrams of any type. | A diagram as a file to drop into slides. |
| [`baoyu-infographic`](https://github.com/jimliu/baoyu-skills) | Infographics with 21 layouts and 22 styles. | A one-page visual summary slide. |
| [`baoyu-cover-image`](https://github.com/jimliu/baoyu-skills) | Cover images with palettes and rendering styles. | Title and cover slides. |
| [`baoyu-article-illustrator`](https://github.com/jimliu/baoyu-skills) | Illustrations for an article by type, style and palette. | Illustrating a text-heavy deck. |
| [`baoyu-compress-image`](https://github.com/jimliu/baoyu-skills) | Compress images to WebP or PNG. | A deck is too heavy to email or load. |
| [`glebis-tufte-report`](https://github.com/glebis/claude-skills) | Tufte-style data reports with charts and sparklines. | Data-heavy appendix or handout. |
| `dataviz` | Rules for charts, palettes, stat tiles and dashboards. | Every chart on a slide. |
| [`office-chart-designer`](https://github.com/claude-office-skills/skills) | Chart configs for ECharts and Chart.js. | Interactive charts in HTML decks. |
| [`office-infographic`](https://github.com/claude-office-skills/skills) | Infographic layout planning. | Planning visual hierarchy. |
| [`office-diagram-creator`](https://github.com/claude-office-skills/skills) | Mermaid and PlantUML diagrams. | Text-defined diagrams. |
| [`office-ppt-visual`](https://github.com/claude-office-skills/skills) | Visual concepts and layout specs for slides. | Ideas for visuals on a slide. |
| `hairline-create` | Playful interactive line-art figures. | An interactive illustration. |

## 10. Research and facts

| Skill | What it does | Use it when |
|---|---|---|
| `deep-research` | Multi-source research with citations. | Any deck with factual claims you must verify. |
| `ecc:exa-search` | Web and company search. | Quick fact lookups. |
| [`office-academic-search`](https://github.com/claude-office-skills/skills) | Literature search and synthesis. | Academic evidence. |
| `ecc:research-ops` | Research workflow patterns. | Large evidence gathering. |
| `graphify` | Turns many inputs into a knowledge graph. | Condensing a big pile of source material before outlining. |

## 11. Motion for slides

| Skill | What it does | Use it when |
|---|---|---|
| `animate` | Adds purposeful motion to UI. | Transition polish inside an HTML deck. |
| `improve-animations` | Fixes janky or inconsistent motion. | Motion that feels off. |
| `review-animations` | Audits animation quality. | Check pass on animated decks. |
| `animation-performance` | Keeps animation smooth. | Laggy decks. |
| `motion-graphics` | Short kinetic type, count-ups, logo stings. | Title animations to embed. |
| `motionmaxxing` | Studio-level motion direction. | A launch keynote opener. |
| `hyperframes-registry` | About 450 ready motion blocks. | Before hand-building any transition or title. |

## 12. Review and quality

| Skill | What it does | Use it when |
|---|---|---|
| `jury` | Scores a live or local web page like a design jury. | Rating an HTML deck's quality. |
| `web-design-guidelines` | Accessibility and UX checklist. | Final audit of HTML decks. |
| `break-ui` | Stress-tests UIs with awkward data. | Decks with data-driven or dynamic content. |
| `browser-testing-with-devtools` | Browser inspection and testing. | Debugging a deck that misbehaves. |
| `playwright-cli` | Browser automation and screenshots. | Rendering slides if `render_deck.mjs` cannot run. |
| `ecc:browser-qa` | Browser-based QA patterns. | End-to-end deck checks. |

## 13. Office and file helpers

| Skill | What it does | Use it when |
|---|---|---|
| `anthropic-skills:pdf` | Read, merge, split, create and fill PDFs. | PDF handouts, merging, extracting source pages. |
| `anthropic-skills:docx` | Word documents. | A script, handout or report to accompany the deck. |
| `anthropic-skills:xlsx` | Spreadsheets. | Data source for charts. |
| `anthropic-skills:google-workspace` | Google Docs, Slides, Drive. | The deck must end up in Google Slides or Drive. |
| `ecc:google-workspace-ops` | Google Workspace operations. | Drive upload and sharing. |
| `ffmpeg` | Media conversion. | Compress or convert embedded video and audio. |

## 14. House skills (the user's own clubs)

If one of these is installed and the request is clearly about that club, load it first and let it set the house rules. It overrides generic choices in this catalog.

| Skill | What it does | Use it when |
|---|---|---|
| `neurogidas-slides` | NeuroGIDAS weekly meeting decks with scripted notes, materials slide, join slide, Drive upload. | Anything for NeuroGIDAS. |
| `evhs-sasa-slideshows` | EVHS SASA decks in Marigold and Indigo, built with fulldesign, with game instructions and Jeopardy. | Anything for EVHS SASA. |
| `evhs-club-flyers` | Club flyers. | A flyer goes with the deck. |
