#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=21600}"
: "${MEMORY_KIB:=33554432}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_q3_full_output_cone_z9_20260825"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$case_dir/PREREGISTRATION.md" \
  "$case_dir/solve_full_output_cone_z9.py" "$case_dir/run_remote.sh" \
  "$MODEL_OUTPUT" > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$MODEL_OUTPUT" \
      PARENT_OUTPUT_JSON="$JOB_DIR/q3_parent.json" \
      OUTPUT_JSON="$JOB_DIR/result.json" \
  python3 "$case_dir/solve_full_output_cone_z9.py" \
  > "$JOB_DIR/solver.stdout" 2> "$JOB_DIR/solver.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/solver.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
