#!/usr/bin/env bash
set -u

kind=$1
stem=$2
root=${3:-/home/ubuntu/k7-cofactors-20260906}
mkdir -p "$root/logs"
job="$root/jobs/${stem}_${kind}.sing"
log="$root/logs/${stem}_${kind}.log"
err="$root/logs/${stem}_${kind}.err"
timing="$root/logs/${stem}_${kind}.time"
rcfile="$root/logs/${stem}_${kind}.rc"

timeout --signal=TERM --kill-after=30s 2400s \
  /usr/bin/time -v -o "$timing" \
  Singular --no-rc -q "$job" >"$log" 2>"$err"
rc=$?
printf '%s\n' "$rc" >"$rcfile"
exit "$rc"
