#!/usr/bin/env bash
set -euo pipefail

: "${JOB_DIR:?}"
: "${INPUT_RESULTS_DIR:?}"
: "${SHARD_COUNT:?}"
: "${JC2_ROOT:?}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_q9_canonical_signature_refinement_20260825"
shard_dir="$JOB_DIR/source_cross_shards"
aggregate_dir="$JOB_DIR/aggregate"
mkdir -p "$shard_dir" "$aggregate_dir"

(
  ulimit -v 4194304
  /usr/bin/time -v env \
    INPUT_RESULTS_DIR="$INPUT_RESULTS_DIR" \
    OUTPUT_DIR="$aggregate_dir" \
    SHARD_COUNT="$SHARD_COUNT" \
    python3 "$case_dir/aggregate_subsignatures.py" \
    >"$JOB_DIR/subsignatures.stdout" 2>"$JOB_DIR/subsignatures.stderr"
  printf '%s\n' "$?" >"$JOB_DIR/subsignatures.rc"
) &
metadata_pid=$!
printf '%s\n' "$metadata_pid" >"$JOB_DIR/subsignatures.pid"

pids=()
for ((index=0; index<SHARD_COUNT; index++)); do
  suffix=$(printf '%03d' "$index")
  (
    ulimit -v 4194304
    /usr/bin/time -v env \
      JC2_ROOT="$JC2_ROOT" \
      INPUT_RESULTS_DIR="$INPUT_RESULTS_DIR" \
      OUTPUT_DIR="$shard_dir" \
      SHARD_COUNT="$SHARD_COUNT" \
      CROSS_SHARD_COUNT="$SHARD_COUNT" \
      CROSS_SHARD_INDEX="$index" \
      python3 "$case_dir/source_cross_tab.py" \
      >"$shard_dir/stdout_$suffix.log" 2>"$shard_dir/stderr_$suffix.log"
    printf '%s\n' "$?" >"$shard_dir/rc_$suffix"
  ) &
  pids+=("$!")
  printf '%s\n' "$!" >"$shard_dir/pid_$suffix"
done

failed=0
for pid in "${pids[@]}"; do
  if ! wait "$pid"; then
    failed=1
  fi
done
if ! wait "$metadata_pid"; then
  failed=1
fi
if [[ "$failed" -ne 0 ]]; then
  printf 'FAIL-SHARD-OR-METADATA\n' >&2
  exit 1
fi

ulimit -v 4194304
/usr/bin/time -v env \
  INPUT_RESULTS_DIR="$INPUT_RESULTS_DIR" \
  CROSS_SHARD_RESULTS_DIR="$shard_dir" \
  OUTPUT_DIR="$aggregate_dir" \
  SHARD_COUNT="$SHARD_COUNT" \
  python3 "$case_dir/aggregate_source_cross_tab.py" \
  >"$JOB_DIR/source_cross_aggregate.stdout" \
  2>"$JOB_DIR/source_cross_aggregate.stderr"
printf '%s\n' "$?" >"$JOB_DIR/source_cross_aggregate.rc"

find "$shard_dir" "$aggregate_dir" -type f -print0 \
  | sort -z \
  | xargs -0 sha256sum >"$JOB_DIR/OUTPUTS.sha256"
printf 'PASS-AS-Q9-SIGNATURE-REFINEMENT-REMOTE\n'
