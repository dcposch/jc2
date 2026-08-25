#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=7200}"
: "${MEMORY_KIB:=33554432}"
case_dir="$JC2_ROOT/cases/as_fonly_d7_q3_two_level_q2_q1_v2_20260825"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/diagnose_nonlinear.py" \
  "$0" "$MODEL_OUTPUT" > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=30s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$MODEL_OUTPUT" \
      PARENT_OUTPUT_JSON="$JOB_DIR/q3_parent.json" \
      OUTPUT_JSON="$JOB_DIR/nonlinear_checkpoint.json" \
  python3 "$case_dir/diagnose_nonlinear.py" \
  > "$JOB_DIR/replay.stdout" 2> "$JOB_DIR/replay.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/replay.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
