#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=3600}"
: "${MEMORY_KIB:=16777216}"

source_dir="$JC2_ROOT/cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825"
program="$source_dir/solve_q3.py"
parent="$JC2_ROOT/cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/solve_full68.py"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$source_dir/PREREGISTRATION.md" "$program" "$0" "$parent" \
  "$MODEL_OUTPUT" > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=30s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$MODEL_OUTPUT" \
      PARENT_OUTPUT_JSON="$JOB_DIR/full68_parent.json" \
      OUTPUT_JSON="$JOB_DIR/q3.json" \
  python3 "$program" > "$JOB_DIR/replay.stdout" 2> "$JOB_DIR/replay.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/replay.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
