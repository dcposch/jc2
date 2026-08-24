#!/bin/sh
# Codex CLI adapter (account-default model). It uses the primary authenticated
# home without reading or mutating its user config.
set -u
pf=$1
echo "cli=$(codex -V 2>&1) config=ignored approval=never sandbox=danger-full-access" >&2
exec codex exec --ignore-user-config -c 'approval_policy="never"' \
  --sandbox danger-full-access - < "$pf"
