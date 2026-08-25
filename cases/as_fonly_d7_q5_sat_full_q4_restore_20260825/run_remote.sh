#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=1800}"
: "${MEMORY_KIB:=8388608}"

source_dir="$JC2_ROOT/cases/as_fonly_d7_q5_sat_full_q4_restore_20260825"
replay="$source_dir/replay_full_q4_restore.py"
parent="$JC2_ROOT/cases/as_fonly_d7_global_q5_h6_replay_erratum_20260825/replay_global_q5_h6_v2.py"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$source_dir/PREREGISTRATION.md" "$replay" "$0" "$parent" \
  "$MODEL_OUTPUT" > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=30s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$MODEL_OUTPUT" \
      PARENT_OUTPUT_JSON="$JOB_DIR/parent_replay.json" \
      OUTPUT_JSON="$JOB_DIR/full_q4_restore.json" \
  python3 "$replay" > "$JOB_DIR/replay.stdout" 2> "$JOB_DIR/replay.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/replay.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
