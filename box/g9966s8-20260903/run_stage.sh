#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 || ! $1 =~ ^[0-9]+$ || $1 -lt 8 ]]; then
  echo "usage: $0 STAGE (integer >= 8)" >&2
  exit 2
fi

stage=$1
root=/home/ubuntu/jc2
engine=$root/box/g9966band-20260903/band_engine.py
attempt=$root/box/g9966s8-20260903/attempts/stage${stage}
expected_engine_sha=3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9

actual_engine_sha=$(sha256sum "$engine" | awk '{print $1}')
if [[ $actual_engine_sha != "$expected_engine_sha" ]]; then
  echo "pinned engine SHA-256 mismatch" >&2
  exit 3
fi

mkdir -p "$attempt"
for artifact in "$attempt/stage${stage}.json" "$attempt/stage${stage}.time" \
                "$attempt/stage${stage}.sing" "$attempt/stage${stage}.err"; do
  if [[ -e $artifact ]]; then
    echo "refusing to overwrite attempt artifact: $artifact" >&2
    exit 4
  fi
done

cpu_set=$(python3 -c 'import os; print(",".join(map(str, sorted(os.sched_getaffinity(0))[:4])))')
if [[ -z $cpu_set ]]; then
  echo "empty CPU affinity set" >&2
  exit 5
fi

set +e
OMP_NUM_THREADS=1 \
OPENBLAS_NUM_THREADS=1 \
MKL_NUM_THREADS=1 \
NUMEXPR_NUM_THREADS=1 \
FLINT_NUM_THREADS=1 \
PYTHONHASHSEED=0 \
/usr/bin/time -v -o "$attempt/stage${stage}.time" \
timeout --signal=TERM --kill-after=30s 3000s \
taskset -c "$cpu_set" \
python3 "$engine" --branch delta52 --stage "$stage" \
  --emit-singular "$attempt/stage${stage}.sing" \
  >"$attempt/stage${stage}.json" 2>"$attempt/stage${stage}.err"
status=$?
set -e

echo "stage=$stage status=$status cpu_set=$cpu_set attempt=$attempt"
exit "$status"
