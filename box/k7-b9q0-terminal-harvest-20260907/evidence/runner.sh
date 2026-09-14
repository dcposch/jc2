#!/bin/bash
# runner.sh <job>: one capped, detached exact-Q long solve.
# 72000 s wall; 70 GiB RSS watchdog on the whole process tree.
set -u
JOB=$1
ROOT=/home/ubuntu/k7-b9q0-longsolve
D=$ROOT/runs/$JOB
WALL=72000
CAP_KIB=$((70*1024*1024))
cd "$D"
date -u +%Y-%m-%dT%H:%M:%SZ > start.utc
/usr/bin/time -v -o "$D/time.txt" \
  timeout -s TERM --kill-after=120 $WALL nice -n 4 \
  Singular --no-rc -q "$D/job.sing" > "$D/stdout.txt" 2> "$D/stderr.txt" &
TPID=$!
python3 "$ROOT/watchdog.py" $TPID $CAP_KIB 15 "$D/caprun.json" &
WPID=$!
wait $TPID; RC=$?
echo $RC > "$D/runner.rc"
date -u +%Y-%m-%dT%H:%M:%SZ > end.utc
wait $WPID 2>/dev/null
echo "RUNNER_DONE $JOB rc=$RC"
