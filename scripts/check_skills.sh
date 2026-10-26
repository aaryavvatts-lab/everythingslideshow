#!/usr/bin/env bash
# check_skills.sh - which skills from catalog.md are installed on this machine?
#
# Usage: bash scripts/check_skills.sh [--missing] [--tools]
#   --missing  print only the missing ones
#   --tools    also report the programs the render and QA scripts need
#
# A skill counts as installed if ~/.claude/skills/<name>/SKILL.md exists, or a plugin ships it
# (names like ecc:frontend-slides are looked up under ~/.claude/plugins).
set -u
HERE="$(cd "$(dirname "$0")/.." && pwd)"
CAT="$HERE/catalog.md"
SK="${HOME}/.claude/skills"
ONLY_MISSING=0; TOOLS=0
for a in "$@"; do case "$a" in --missing) ONLY_MISSING=1;; --tools) TOOLS=1;; esac; done

names=$(grep -oE '^\| \[?`[a-z0-9:_.-]+`' "$CAT" | grep -oE '`[^`]+`' | tr -d '`' | sort -u)
PLUGIN_ROOTS=("${HOME}/.claude/plugins" "${HOME}/Library/Application Support/Claude" "${HOME}/.config/Claude")
in_plugins() {  # $1 = base name; true if any plugin ships a skill or command with that name
  for root in "${PLUGIN_ROOTS[@]}"; do
    [ -d "$root" ] || continue
    if find "$root" \( -path "*/skills/$1/SKILL.md" -o -path "*/commands/$1.md" \) 2>/dev/null | grep -q .; then return 0; fi
  done
  return 1
}
have=0; miss=0; unk=0
for n in $names; do
  base="${n##*:}"
  if [ -f "$SK/$base/SKILL.md" ] || in_plugins "$base"; then
    have=$((have+1)); [ "$ONLY_MISSING" = 0 ] && echo "ok       $n"
  elif [[ "$n" == *:* ]] || [ "$n" = dataviz ]; then
    # plugin or built-in skills are not always visible on disk; do not claim they are absent
    unk=$((unk+1)); echo "unknown  $n   (plugin or built-in skill; check the Skill tool list)"
  else
    miss=$((miss+1)); echo "MISSING  $n"
  fi
done
echo "---"; echo "$have installed, $miss missing, $unk unverified (of $((have+miss+unk)) in catalog.md)"
if [ "$TOOLS" = 1 ]; then
  echo "--- tools"
  for t in node python3 npx git ffmpeg soffice pdftoppm xelatex pdflatex; do
    if command -v "$t" >/dev/null 2>&1; then echo "ok       $t"; else echo "absent   $t"; fi
  done
  python3 - <<'PY'
for m, pip in (("pptx", "python-pptx"), ("PIL", "pillow"), ("fitz", "pymupdf")):
    try:
        __import__(m); print(f"ok       python:{pip}")
    except ImportError:
        print(f"absent   python:{pip}   (pip3 install {pip})")
PY
fi
