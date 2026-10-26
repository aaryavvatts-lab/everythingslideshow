#!/usr/bin/env bash
# install_companions.sh - install the open-source slide skills that everythingslideshow routes to.
#
# Usage:
#   bash scripts/install_companions.sh [--core | --all] [--dry-run] [--dir ~/.claude/skills]
#
#   --core     (default) the 14 skills that cover almost every request
#   --all      every companion skill listed in catalog.md that lives on GitHub (about 90, a few hundred MB)
#   --dry-run  print what would be installed and change nothing
#   --dir      target skills folder (default ~/.claude/skills)
#
# Safe by design: shallow clones into a temp folder, copies only the skill folder, never overwrites a
# skill that already exists, never runs code from the clones. Read a skill before you trust it.
set -euo pipefail

MODE=core; DRY=0; DEST="${HOME}/.claude/skills"
while [ $# -gt 0 ]; do
  case "$1" in
    --core) MODE=core;; --all) MODE=all;; --dry-run) DRY=1;;
    --dir) DEST="$2"; shift;;
    -h|--help) sed -n 2,14p "$0"; exit 0;;
    *) echo "unknown option $1"; exit 2;;
  esac; shift
done

# tier|owner/repo|path inside repo ('.' = repo root)|installed folder name
TABLE='core|zarazhangrui/frontend-slides|.|frontend-slides
core|alchaincyf/huashu-design|.|huashu-design
core|lewislulu/html-ppt-skill|.|html-ppt
core|op7418/guizang-ppt-skill|.|guizang-ppt-skill
core|nicobailon/visual-explainer|skills/visual-explainer|visual-explainer
core|hugohe3/ppt-master|skills/ppt-master|ppt-master
core|jameshemson/slides|.claude/skills/presentation-craft|slides-presentation-craft
core|jameshemson/slides|.claude/skills/narrative|slides-narrative
core|jameshemson/slides|.claude/skills/slop-check|slides-slop-check
core|jameshemson/slides|.claude/skills/build-deck|slides-build-deck
core|EvoScientist/EvoSkills|skills/academic-slides|academic-slides
core|Gabberflast/academic-pptx-skill|.|academic-pptx
core|Noi1r/beamer-skill|beamer|beamer
core|jimliu/baoyu-skills|skills/baoyu-slide-deck|baoyu-slide-deck
all|archlizheng/frontend-slides-editable|.|frontend-slides-editable
all|Akxan/ppt-agent-skill|.|ppt-agent
all|likaku/Mck-ppt-design-skill|.|mck-ppt-design
all|marcogalluccio/claude-slides|.|claude-slides
all|edu-ai-builders/visual-cognition-slides|.|visual-cognition-slides
all|kaisersong/slide-creator|.|kai-slide-creator
all|vigorX777/ppt-svg-generator|.|ppt-svg-generator
all|open-slide/open-slide|packages/core/skills/create-slide|open-slide-create-slide
all|open-slide/open-slide|packages/core/skills/slide-authoring|open-slide-slide-authoring
all|open-slide/open-slide|packages/core/skills/create-theme|open-slide-create-theme
all|mucsbr/ppt-agent-workflow-san|html-to-bento-slides|html-to-bento-slides
all|mucsbr/ppt-agent-workflow-san|html-slide-to-pptx|html-slide-to-pptx
all|mucsbr/ppt-agent-workflow-san|ppt-workflow|ppt-workflow
all|humantonylee/future-slide|skills/html-slide|fs-html-slide
all|humantonylee/future-slide|skills/gpt-image-slide|fs-gpt-image-slide
all|humantonylee/future-slide|skills/slide-design|fs-slide-design
all|humantonylee/future-slide|skills/tightened-slide|fs-tightened-slide
all|jameshemson/slides|.claude/skills/revise|slides-revise
all|jameshemson/slides|.claude/skills/teach-slides|slides-teach-slides
all|software-ai-life/Awesome-PPT-Design-Skills|soft-3d-clay-ppt-skill|soft-3d-clay-ppt-skill
all|software-ai-life/Awesome-PPT-Design-Skills|futuristic-tech-editorial-ppt-skill|futuristic-tech-editorial-ppt-skill
all|software-ai-life/Awesome-PPT-Design-Skills|japanese-style-ppt-skill|japanese-style-ppt-skill
all|software-ai-life/Awesome-PPT-Design-Skills|japanese-hand-drawn-editorial-ppt-skill|japanese-hand-drawn-editorial-ppt-skill
all|software-ai-life/Awesome-PPT-Design-Skills|minimalist-luxury-branding-ppt-skill|minimalist-luxury-branding-ppt-skill
all|software-ai-life/Awesome-PPT-Design-Skills|modern-illustration-editorial-ppt-skill|modern-illustration-editorial-ppt-skill
all|glebis/claude-skills|present|glebis-present
all|glebis/claude-skills|presentation-generator|glebis-presentation-generator
all|glebis/claude-skills|tufte-report|glebis-tufte-report
all|borghei/Claude-Skills|markdown-html/md-slides|borghei-md-slides
all|jimliu/baoyu-skills|skills/baoyu-infographic|baoyu-infographic
all|jimliu/baoyu-skills|skills/baoyu-diagram|baoyu-diagram
all|jimliu/baoyu-skills|skills/baoyu-cover-image|baoyu-cover-image
all|jimliu/baoyu-skills|skills/baoyu-article-illustrator|baoyu-article-illustrator
all|jimliu/baoyu-skills|skills/baoyu-image-gen|baoyu-image-gen
all|jimliu/baoyu-skills|skills/baoyu-compress-image|baoyu-compress-image
all|orchestra-research/ai-research-skills|20-ml-paper-writing/presenting-conference-talks|presenting-conference-talks
all|marswaveai/skills|slides|marswave-slides
all|aaronvanston/skills-presentations|skills/presentation-outline|presentation-outline
all|aaronvanston/skills-presentations|skills/presentation-content|presentation-content
all|aaronvanston/skills-presentations|skills/presentation-design|presentation-design
all|aaronvanston/skills-presentations|skills/presentation-notes|presentation-notes
all|aaronvanston/skills-presentations|skills/presentation-pitch-deck|presentation-pitch-deck
all|yuan1z0825/nature-skills|skills/nature-paper2ppt|nature-paper2ppt
all|yuan1z0825/nature-skills|skills/nature-image2ppt|nature-image2ppt
all|M1n-n9/academic-ppt-master|.|academic-ppt-master
all|Faust-Donf/beamer-academic|.|beamer-academic
all|zouchenzhen/thesis-defense-pptx-skill|skills/thesis-defense-pptx|thesis-defense-pptx
all|minorun365/minorun-marp-skill|skills/slide-story|slide-story
all|minorun365/minorun-marp-skill|skills/slide-figures|slide-figures
all|minorun365/minorun-marp-skill|skills/slide-design-dark|slide-design-dark
all|robonuggets/marp-slides|.|marp-slides
all|ryanbbrown/revealjs-skill|skills/revealjs|revealjs
all|Pikapika260214/rw-consulting-ppt|skills/rw-consulting-ppt|rw-consulting-ppt
all|irenerachel/visual-style-ppt-skill|.|visual-style-ppt
all|kgraph57/mckinsey-style-visualization-skill|.|mckinsey-style-viz
all|NyxTides/ppt-image-first|.|ppt-image-first
all|crazyykhllc-bit/CyberPPT|.|cyberppt
all|ningzimu/codex-ppt-skill|skills/codex-ppt|codex-ppt
all|nextlevelbuilder/ui-ux-pro-max-skill|.claude/skills/slides|uiux-slides
all|wuyoscar/GPT-Image2-Skill|skills/gpt-image|gpt-image
all|GordenSun/GordenSuperPPTSkills|GordenSuperPPTSkill|gorden-super-ppt'

want() { [ "$MODE" = all ] || [ "$1" = core ]; }
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$DEST"
installed=0; skipped=0; failed=0

while IFS='|' read -r tier repo sub name; do
  [ -z "$tier" ] && continue
  want "$tier" || continue
  if [ -e "$DEST/$name" ]; then echo "skip   $name (already installed)"; skipped=$((skipped+1)); continue; fi
  if [ "$DRY" = 1 ]; then echo "would  install $name  <- github.com/$repo/$sub"; continue; fi
  clone="$TMP/$(echo "$repo" | tr / _)"
  if [ ! -d "$clone" ]; then
    git clone --depth 1 -q "https://github.com/$repo" "$clone" 2>/dev/null || { echo "FAIL   $name (clone $repo)"; failed=$((failed+1)); continue; }
  fi
  src="$clone"; [ "$sub" != "." ] && src="$clone/$sub"
  if [ ! -f "$src/SKILL.md" ]; then echo "FAIL   $name (no SKILL.md at $sub)"; failed=$((failed+1)); continue; fi
  mkdir -p "$DEST/$name"
  (cd "$src" && tar --exclude=.git --exclude=node_modules -cf - .) | (cd "$DEST/$name" && tar xf -)
  echo "ok     $name"; installed=$((installed+1))
done <<< "$TABLE"

echo "done: $installed installed, $skipped already there, $failed failed. Restart Claude Code to load new skills."
[ "$failed" -eq 0 ]
