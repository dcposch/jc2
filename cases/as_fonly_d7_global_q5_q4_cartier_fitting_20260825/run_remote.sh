#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=43200}"
: "${MEMORY_KIB:=134217728}"

mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum \
  "$JC2_ROOT/cases/as_fonly_d7_global_q5_q4_cartier_fitting_20260825/"{PREREGISTRATION.md,analyze_cartier_fitting.py,run_remote.sh} \
  "$JC2_ROOT/cases/as_fonly_d7_global_q5_q4_cartier_20260825/"{solve_global_q5_q4_cartier.py,compatible_bases.tsv} \
  > "$JOB_DIR/SOURCE.sha256"

ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" OUTPUT_DIR="$JOB_DIR/result" \
      AFFINE_TIMEOUT_MS=3600000 \
  python3 "$JC2_ROOT/cases/as_fonly_d7_global_q5_q4_cartier_fitting_20260825/analyze_cartier_fitting.py" \
  > "$JOB_DIR/analyzer.stdout" 2> "$JOB_DIR/analyzer.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/analyzer.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"

