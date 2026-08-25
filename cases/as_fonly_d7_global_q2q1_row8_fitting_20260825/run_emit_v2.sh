#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=7200}"
: "${MEMORY_KIB:=67108864}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_global_q2q1_row8_fitting_20260825"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/solve_global_row8_v2.py" \
  "$case_dir/run_emit_v2.sh" > "$JOB_DIR/SOURCE.sha256"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" SOLVER_TIMEOUT_MS=1 \
      SMT2_OUTPUT="$JOB_DIR/global_row8.smt2" \
      OUTPUT_JSON="$JOB_DIR/emitter.json" \
      ROW8_EXPR_OUTPUT="$JOB_DIR/row8_expression.smt2expr" \
      OMIT_GLOBAL_ROW8="${OMIT_GLOBAL_ROW8:-0}" \
  python3 "$case_dir/solve_global_row8_v2.py" \
  > "$JOB_DIR/emitter.stdout" 2> "$JOB_DIR/emitter.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/emitter.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
