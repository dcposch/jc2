#!/bin/sh
# Opus 5 Claude Code CLI adapter. The lane prompt owns the exact output path,
# write scope, and shell/network boundary. Unset the capped API-key route so
# Claude Code uses the working first-party Claude.ai authentication.
set -eu
pf=$1
# Raise the CLI's per-response output cap from its 64k default to the model's
# 128k maximum: max-effort thinking counts toward the cap and a 64k overflow
# kills the whole lane with no report.
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000
echo "cli=$(claude --version 2>&1 | head -1) model=opus effort=max mode=bypassPermissions shell=yes auth=claude.ai max_output_tokens=128000" >&2
exec env -u ANTHROPIC_API_KEY claude -p --model opus --effort max \
  --dangerously-skip-permissions --no-session-persistence \
  --tools Read Grep Glob Write Edit Bash \
  < "$pf"
