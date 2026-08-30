#!/bin/sh
# Dedicated different-model review adapter. Unlike the Sol adapter, this has
# no environment-variable model override: its hash certifies the exact model
# family and reasoning effort charged by a review receipt.
set -u
pf=$1
model=gpt-5.5
effort=xhigh
echo "cli=$(codex -V 2>&1) model=$model effort=$effort config=ignored approval=never sandbox=danger-full-access" >&2
exec codex exec --ignore-user-config -c 'approval_policy="never"' \
  -c "model_reasoning_effort=\"$effort\"" -m "$model" \
  --sandbox danger-full-access - < "$pf"
