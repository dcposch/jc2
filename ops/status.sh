#!/bin/bash
# JC2 campaign live-activity dashboard. Usage: bash ops/status.sh
echo "=== LOCAL LANES (detached codex/grok/python) ==="
ps aux | grep -E "codex exec|grok -p|directionb_compress|fleet_fc1" | grep -v grep \
  | awk '{printf "  %-8s %5.1fGB  %s...\n", $2, $6/1048576, substr($0, index($0,$11), 60)}'
[ -z "$(ps aux | grep -E 'codex exec|grok -p|directionb_' | grep -v grep)" ] && echo "  (none)"
echo "=== LANE MARKERS (last 5) ==="
tail -5 /tmp/stuck7_lanes.log 2>/dev/null | sed 's/^/  /'
echo "=== FLEET ==="
for spec in "box01 54.175.21.169" ; do
  set -- $spec
  echo "  $1:"
  timeout 15 ssh -i ~/.ssh/claude-cli.pem -o ConnectTimeout=6 ubuntu@$2 \
    'echo "    msolve procs: $(pgrep -c msolve 2>/dev/null || echo 0), python: $(pgrep -c -f fleet_fc1 2>/dev/null || echo 0)"; tail -1 ~/jc72108/pilot.log 2>/dev/null | sed "s/^/    pilot: /"; tail -1 ~/jc72108/fc1_audit.log 2>/dev/null | sed "s/^/    fc1:   /"' 2>/dev/null || echo "    (unreachable)"
done
for b in "Box02 i-010201a5da47795c4" "Box03 i-0ece0b9a3b4a7512f"; do
  set -- $b
  st=$(aws ec2 describe-instances --instance-ids $2 --profile personal --query 'Reservations[0].Instances[0].State.Name' --output text 2>/dev/null)
  echo "  $1: $st"
done
echo "=== STANDING QUEUE (notes.md) ==="
awk '/## STANDING QUEUE/{f=1;next} f&&/^##[^#]/{exit} f&&NF' ~/code/math/notes.md | head -12 | sed 's/^/  /'
echo "=== SUBAGENT ROSTER (idle between assignments; resume via coordinator) ==="
echo "  window agent (direction-b/compression), tower agent (td-ladder/census)"
