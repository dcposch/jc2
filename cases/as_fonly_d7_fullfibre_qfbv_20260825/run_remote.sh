#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${JOB_DIR:?}"
: "${SOLVER_TIMEOUT_MS:?}"
case_dir="$JC2_ROOT/cases/as_fonly_d7_fullfibre_qfbv_20260825"
representatives="$case_dir/STATE_REPRESENTATIVES.tsv"
results="$JOB_DIR/results"
mkdir -p "$results"
pids=()
while IFS=$'\t' read -r state label signature; do
  if [[ "$state" == "state_index" ]]; then continue; fi
  suffix=$(printf '%07d' "$state")
  (
    # Eight GiB per solver lane, expressed in KiB for `ulimit -v`.
    ulimit -v 8388608
    /usr/bin/time -v env JC2_ROOT="$JC2_ROOT" STATE_INDEX="$state" \
      CANONICAL_LABEL="$label" PRESENTATION_SIGNATURE="$signature" \
      SOLVER_TIMEOUT_MS="$SOLVER_TIMEOUT_MS" \
      SMT2_OUTPUT="$results/state_$suffix.smt2" \
      OUTPUT_JSON="$results/state_$suffix.json" \
      python3 "$case_dir/solve_state.py" \
      >"$results/state_$suffix.stdout" 2>"$results/state_$suffix.stderr"
    printf '%s\n' "$?" >"$results/state_$suffix.rc"
  ) &
  pids+=("$!")
  printf '%s\n' "$!" >"$results/state_$suffix.pid"
done <"$representatives"
failed=0
for pid in "${pids[@]}"; do
  if ! wait "$pid"; then failed=1; fi
done
if [[ "$failed" -ne 0 ]]; then
  printf 'FAIL-AS-FULLFIBRE-QFBV-STATE\n' >&2
  exit 1
fi
/usr/bin/time -v env RESULTS_DIR="$results" \
  REPRESENTATIVES_FILE="$representatives" python3 "$case_dir/aggregate.py" \
  >"$results/aggregate.stdout" 2>"$results/aggregate.stderr"
printf '%s\n' "$?" >"$results/aggregate.rc"
find "$results" -type f -print0 | sort -z | xargs -0 sha256sum \
  >"$results/OUTPUTS.sha256"
printf 'PASS-AS-FULLFIBRE-QFBV-REMOTE\n'
