#!/usr/bin/env bash
set -euo pipefail

root=/home/ubuntu/jc2
base="$root/box/g9966d52gate-20260903"
engine="$root/box/g9966band-20260903/band_engine.py"
attempt="$base/attempts/stage8"
expected_engine_sha=3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9

actual_engine_sha=$(sha256sum "$engine" | awk '{print $1}')
if [[ "$actual_engine_sha" != "$expected_engine_sha" ]]; then
  echo "pinned engine SHA-256 mismatch" >&2
  exit 3
fi

mkdir -p "$attempt"
for artifact in "$attempt/stage8.json" "$attempt/stage8.time" \
                "$attempt/stage8.sing" "$attempt/stage8.err"; do
  if [[ -e "$artifact" ]]; then
    echo "refusing to overwrite attempt artifact: $artifact" >&2
    exit 4
  fi
done

cpu_set=$(python3 -c 'import os; print(",".join(map(str, sorted(os.sched_getaffinity(0))[:4])))')
if [[ -z "$cpu_set" ]]; then
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
/usr/bin/time -v -o "$attempt/stage8.time" \
timeout --signal=TERM --kill-after=30s 3000s \
taskset -c "$cpu_set" \
python3 "$engine" --branch delta52 --stage 8 \
  --emit-singular "$attempt/stage8.sing" \
  >"$attempt/stage8.json" 2>"$attempt/stage8.err"
status=$?
set -e

echo "stage=8 status=$status cpu_set=$cpu_set attempt=$attempt"
exit "$status"
