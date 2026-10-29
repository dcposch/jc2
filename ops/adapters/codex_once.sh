#!/bin/sh
# HQ-only single CLI invocation. The caller must supply the existing lane
# isolation, charged-input custody, output capture, and independent caps.
# This is not a retry supervisor; CLI-internal transport retries are unchanged.
set -eu
if [ "$#" -ne 1 ]; then
  echo 'usage: codex_once.sh PROMPT_FILE' >&2
  exit 64
fi
if [ "${CODEX_MODEL-gpt-6-astra}" != gpt-6-astra ] ||
   [ "${CODEX_REASONING_EFFORT-ultra}" != ultra ]; then
  echo 'codex_once: requires gpt-6-astra and ultra; no model override' >&2
  exit 64
fi
# Redirection is opened before exec; an unreadable prompt never starts Codex.
exec codex exec --ignore-user-config -c 'approval_policy="never"' \
  -c 'model_reasoning_effort="ultra"' -m gpt-6-astra \
  --sandbox danger-full-access - < "$1"
