#!/bin/sh
# DEPRECATED for jc2 routing (DC 2026-09-05): drop GPT-5.5 (2 gens old).
# Prefer ops/adapters/codex.sh (gpt-6-astra). Kept only so old review-receipt
# hashes that named this adapter remain auditable; do not launch new lanes here.
# Dedicated different-model review adapter. Unlike the Sol/Astra adapter, this has
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
