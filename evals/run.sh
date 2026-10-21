#!/usr/bin/env bash
# Run the skills headless in a temporary workspace and check the files they write.
# Each case runs the skill with `claude -p` and calls the model.
# Usage: evals/run.sh [case ...]   Env: MODEL (default sonnet), BUDGET (USD per case, default 2)
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
MODEL="${MODEL:-sonnet}"
BUDGET="${BUDGET:-2}"
CASES=("$@"); [ ${#CASES[@]} -eq 0 ] && CASES=(pack-setup weekly-review forecast calibration-small calibration-tiny)
OUT="$(mktemp -d)"
status=0

for c in "${CASES[@]}"; do
  ws="$OUT/$c"; mkdir -p "$ws"
  fixture=deals-large.csv; seed=1
  case "$c" in
    pack-setup) seed=0
      prompt="Use the mia-pack-setup skill. I am a sales leader. deals.csv in this folder is my CRM export: use it as the CRM and read nothing else. Skip your opening question. Everything you find is right, so ask no follow-up questions and write the pack files now." ;;
    weekly-review)
      prompt="Use the mia-weekly-review skill. I am a rep named Dana Cho and deals.csv is my CRM export. Ask no questions. Build the report and save it the way the skill says." ;;
    forecast)
      prompt="Use the mia-forecast skill for the current quarter. I am a sales leader and deals.csv is the CRM export. Ask no questions. Build the report and save it the way the skill says." ;;
    calibration-small) fixture=deals-small.csv
      prompt="Use the mia-axes-calibration skill on deals.csv. I am a sales leader, so use the team scope. Ask no questions." ;;
    calibration-tiny) fixture=deals-tiny.csv
      prompt="Use the mia-axes-calibration skill on deals.csv. I am a sales leader, so use the team scope. Ask no questions." ;;
    *) echo "unknown case $c"; exit 2 ;;
  esac
  cp "$REPO/evals/fixtures/$fixture" "$ws/deals.csv"
  if [ $seed -eq 1 ]; then
    mkdir -p "$ws/mia-pack"
    for f in deal-lifecycle buyers-and-competition market-physics winning-plays team-standards scoring-axes crm-guide voice working-style; do
      cp "$REPO/source/config/$f.md" "$ws/mia-pack/"
    done
    shasum -a 256 "$ws/mia-pack/scoring-axes.md" | cut -d' ' -f1 > "$ws/.scoring-axes.sha"
  fi
  echo "== $c"
  (cd "$ws" && claude -p "$prompt" --plugin-dir "$REPO" --model "$MODEL" --permission-mode acceptEdits \
      --allowedTools "Read Write Edit Glob Grep" --max-budget-usd "$BUDGET" --no-session-persistence \
      --output-format text > "$OUT/$c.out" 2> "$OUT/$c.err")
  python3 "$REPO/evals/check.py" "$c" "$ws" "$OUT/$c.out" || status=1
done
echo "workspaces and replies kept in $OUT"
exit $status
