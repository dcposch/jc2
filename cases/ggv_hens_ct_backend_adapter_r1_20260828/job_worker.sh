#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "usage: job_worker.sh RUN_DIR REGISTER_GATE SOURCE_SHA256" >&2
  exit 64
fi

run_dir=$(realpath "$1")
register_gate=$(realpath -m "$2")
source_sha=$3
[[ "$register_gate" == "$run_dir"/* ]]
[[ "$source_sha" =~ ^[0-9a-f]{64}$ ]]

while [[ ! -f "$register_gate" ]]; do
  sleep 0.05
done

exec /usr/bin/prlimit \
  --as=$((400 * 1024 * 1024 * 1024)) \
  --fsize=$((8 * 1024 * 1024 * 1024)) \
  --cpu=16200 \
  /usr/bin/time -v \
  /usr/bin/timeout --foreground --signal=TERM --kill-after=60 16320 \
  "$run_dir/source/pipeline_worker.sh" "$run_dir"
