#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=21600}"
: "${MEMORY_KIB:=134217728}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_global_q5_q4_cartier_fitting_v5_symbolic_20260825"
mkdir -p "$JOB_DIR/result"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$case_dir/PREREGISTRATION_V6.md" \
  "$case_dir/analyze_cartier_fitting_v6.py" "$case_dir/run_remote_v6.sh" \
  > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" OUTPUT_DIR="$JOB_DIR/result" \
  python3 "$case_dir/analyze_cartier_fitting_v6.py" \
  > "$JOB_DIR/runner.stdout" 2> "$JOB_DIR/runner.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/runner.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
