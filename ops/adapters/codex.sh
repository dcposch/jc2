#!/bin/sh
# Codex CLI adapter. It uses the primary authenticated home without reading or
# mutating its user config, and pins the campaign's Sol model/effort explicitly.
set -u
pf=$1
model=${CODEX_MODEL:-gpt-5.6-sol}
effort=${CODEX_REASONING_EFFORT:-ultra}
case "$effort" in
  low|medium|high|xhigh|max|ultra) ;;
  *) echo "invalid CODEX_REASONING_EFFORT=$effort" >&2; exit 64 ;;
esac
echo "cli=$(codex -V 2>&1) model=$model effort=$effort config=ignored approval=never sandbox=danger-full-access" >&2
exec codex exec --ignore-user-config -c 'approval_policy="never"' \
  -c "model_reasoning_effort=\"$effort\"" -m "$model" \
  --sandbox danger-full-access - < "$pf"
