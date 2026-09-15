#!/bin/sh
# Display one explicitly supplied swarm state snapshot; performs no cloud actions.
set -eu
if [ "$#" -ne 1 ]; then
  echo "usage: sh ops/status.sh /path/to/swarm/STATE.md" >&2
  exit 2
fi
if [ ! -f "$1" ] || [ -L "$1" ]; then
  echo "status: expected a regular state file: $1" >&2
  exit 2
fi
printf 'Recorded swarm state (verify live jobs separately):\n'
cat -- "$1"
