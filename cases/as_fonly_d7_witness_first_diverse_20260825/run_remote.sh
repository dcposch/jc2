#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${JOB_DIR:?}"
: "${SAMPLE_COUNT:?}"
case_dir="$JC2_ROOT/cases/as_fonly_d7_witness_first_diverse_20260825"
results="$JOB_DIR/results"
mkdir -p "$results"
pids=()
for ((index=0; index<SAMPLE_COUNT; index++)); do
  suffix=$(printf '%03d' "$index")
  (
    ulimit -v 4194304
    /usr/bin/time -v env \
      JC2_ROOT="$JC2_ROOT" SAMPLE_INDEX="$index" SAMPLE_COUNT="$SAMPLE_COUNT" \
      OUTPUT_JSON="$results/sample_$suffix.json" \
      python3 "$case_dir/compile_sample.py" \
      >"$results/sample_$suffix.stdout" 2>"$results/sample_$suffix.stderr"
    printf '%s\n' "$?" >"$results/sample_$suffix.rc"
  ) &
  pids+=("$!")
  printf '%s\n' "$!" >"$results/sample_$suffix.pid"
done
failed=0
for pid in "${pids[@]}"; do
  if ! wait "$pid"; then failed=1; fi
done
if [[ "$failed" -ne 0 ]]; then
  printf 'FAIL-AS-WITNESS-FIRST-SAMPLE\n' >&2
  exit 1
fi
ulimit -v 4194304
/usr/bin/time -v env RESULTS_DIR="$results" SAMPLE_COUNT="$SAMPLE_COUNT" \
  python3 "$case_dir/aggregate.py" \
  >"$results/aggregate.stdout" 2>"$results/aggregate.stderr"
printf '%s\n' "$?" >"$results/aggregate.rc"
find "$results" -type f -print0 | sort -z | xargs -0 sha256sum \
  >"$results/OUTPUTS.sha256"
printf 'PASS-AS-WITNESS-FIRST-DIVERSE-REMOTE\n'

