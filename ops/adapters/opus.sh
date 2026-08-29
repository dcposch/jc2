#!/bin/sh
# Opus 5 Claude Code CLI adapter. The lane prompt owns the exact output path,
# write scope, and shell/network boundary. Unset the capped API-key route so
# Claude Code uses the working first-party Claude.ai authentication.
set -eu
pf=$1
echo "cli=$(claude --version 2>&1 | head -1) model=opus effort=max mode=bypassPermissions shell=yes auth=claude.ai" >&2
exec env -u ANTHROPIC_API_KEY claude -p --model opus --effort max \
  --dangerously-skip-permissions --no-session-persistence \
  --tools Read Grep Glob Write Edit Bash \
  < "$pf"
