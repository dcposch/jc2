#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 8 ]]; then
  echo "usage: job_worker.sh RUN_DIR LABEL WALL_SECONDS AS_BYTES FSIZE_BYTES CPU_SECONDS JOB GATE" >&2
  exit 64
fi

run_dir=$(realpath "$1")
label=$2
wall_seconds=$3
as_bytes=$4
fsize_bytes=$5
cpu_seconds=$6
job=$(realpath "$7")
gate=$8

[[ "$job" == "$run_dir"/* ]]
[[ "$gate" == "$run_dir"/* ]]
[[ "$label" =~ ^[A-Za-z0-9_.-]+$ ]]
[[ "$wall_seconds" =~ ^[0-9]+$ ]]
[[ "$as_bytes" =~ ^[0-9]+$ ]]
[[ "$fsize_bytes" =~ ^[0-9]+$ ]]
[[ "$cpu_seconds" =~ ^[0-9]+$ ]]

# Registration handshake: the worker is already the setsid leader, but no
# descendant starts until the parent has validated PID=PGID, captured the
# immutable start time, and written the registry row.
while [[ ! -f "$gate" ]]; do
  sleep 0.05
done

# The parent launches this worker with setsid.  `timeout --foreground` is
# essential: it keeps timeout and the actual Singular descendant in this one
# recorded PGID rather than creating an untracked inner process group.
exec /usr/bin/prlimit \
  --as="$as_bytes" \
  --fsize="$fsize_bytes" \
  --cpu="$cpu_seconds" \
  /usr/bin/time -v \
  /usr/bin/timeout --foreground --signal=TERM --kill-after=60 \
  "$wall_seconds" /usr/bin/Singular -q "$job"
