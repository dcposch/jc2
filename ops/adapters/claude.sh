#!/bin/sh
# Claude Code CLI adapter. The lane prompt owns the exact output path and
# allowed write scope; network use is disabled by omission of network tools.
set -u
pf=$1
echo "cli=$(claude --version 2>&1 | head -1) model=fable effort=max mode=dontAsk" >&2
exec claude -p --model fable --effort max --permission-mode dontAsk \
  --allowedTools Read Grep Glob Write Edit --disallowedTools WebFetch WebSearch Bash \
  < "$pf"
