#!/bin/bash
set -uo pipefail
META=${1:?metadata path required}
CHAR=${2:?characteristic required}
BRANCH=${3:?branch required}
LIMIT=${4:?timeout required}
TAG=${5:?tag required}
CPU=${6:-}
ROOT=/home/ubuntu/jc2
OUT=$ROOT/box/s56-recert-20260905/fleet-logs
mkdir -p "$OUT"
date -u +%Y-%m-%dT%H:%M:%SZ > "$OUT/$TAG.start"
hostname > "$OUT/$TAG.host"
cd "$ROOT" || exit 98
if [[ -n "$CPU" ]]; then
  export S56_CPU=$CPU
fi
python3 box/s56-recert-20260905/s56_emitter.py solve \
  --meta "$META" --char "$CHAR" --timeout "$LIMIT" --branch "$BRANCH" \
  > "$OUT/$TAG.stdout" 2> "$OUT/$TAG.stderr"
rc=$?
printf '%s\n' "$rc" > "$OUT/$TAG.rc"
date -u +%Y-%m-%dT%H:%M:%SZ > "$OUT/$TAG.end"
exit "$rc"
