#!/bin/sh
# Codex CLI adapter. It uses the primary authenticated home without reading or
# mutating its user config, and pins the campaign's Astra model/effort explicitly.
# 2026-09-05: retries (up to 4x, 120 s apart) when the backend answers
# "Selected model is at capacity" — two lanes died mid-work on that today.
set -u
pf=$1
model=${CODEX_MODEL:-gpt-6-astra}
effort=${CODEX_REASONING_EFFORT:-ultra}
case "$effort" in
  low|medium|high|xhigh|max|ultra) ;;
  *) echo "invalid CODEX_REASONING_EFFORT=$effort" >&2; exit 64 ;;
esac
echo "cli=$(codex -V 2>&1) model=$model effort=$effort config=ignored approval=never sandbox=danger-full-access" >&2
tmp=$(mktemp) || exit 70
attempt=1
while :; do
  codex exec --ignore-user-config -c 'approval_policy="never"' \
    -c "model_reasoning_effort=\"$effort\"" -m "$model" \
    --sandbox danger-full-access - < "$pf" 2>"$tmp"
  rc=$?
  cat "$tmp" >&2
  if [ $rc -ne 0 ] && [ $attempt -lt 5 ] && grep -q 'at capacity' "$tmp"; then
    echo "adapter: backend at capacity (attempt $attempt/5, rc=$rc); retrying in 120 s" >&2
    attempt=$((attempt+1)); sleep 120; continue
  fi
  break
done
rm -f "$tmp"
exit $rc
