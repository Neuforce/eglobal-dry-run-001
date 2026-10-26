#!/usr/bin/env bash
# Lists human-facing files by review status banner.
# Usage: scripts/review-status.sh [path]   (default: whole repo)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-.}"
cd "$ROOT"

# Templates, examples, skills, agents and scripts are not reviewed as project inputs
FILES=$(find "$TARGET" -name '*.md' \
  -not -path './templates/*' -not -path 'templates/*' \
  -not -path './examples/*'  -not -path 'examples/*' \
  -not -path './skills/*'    -not -path 'skills/*' \
  -not -path './agents/*'    -not -path 'agents/*' \
  -not -path './.claude/*' -not -path './.github/*' | sort)

section() { # $1 label  $2 pattern
  local hits=()
  for f in $FILES; do head -6 "$f" | grep -q "^> \*\*$2" && hits+=("$f"); done
  echo "$1 (${#hits[@]})"
  for f in "${hits[@]:-}"; do [ -n "$f" ] && echo "   - ${f#./}"; done
  echo
}

echo "== Review status: $TARGET =="
echo
section "🟥 REQUIRED — eGlobal input needed" "🟥 REQUIRED"
section "🟨 ASSUMPTION — review & approve"   "🟨 ASSUMPTION"
section "✅ APPROVED"                          "✅ APPROVED"
section "🟩 METHOD — optional review"          "🟩 METHOD"

TBD=$(grep -rl --include='*.md' 'TBD' $FILES 2>/dev/null | wc -l | tr -d ' ')
echo "Files still containing TBD: $TBD"
for f in $FILES; do head -6 "$f" | grep -q "^> \*\*🟥 REQUIRED" && exit 1; done
exit 0
