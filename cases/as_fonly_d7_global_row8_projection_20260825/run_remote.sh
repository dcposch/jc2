#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${JOB_DIR:?}"
: "${SHARD_INDEX:?}"
: "${SHARD_COUNT:=27}"
: "${TIMEOUT_SECONDS:=21600}"
: "${MEMORY_KIB:=4194304}"

case_dir="$JC2_ROOT/cases/as_fonly_d7_global_row8_projection_20260825"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$case_dir/PREREGISTRATION.md" \
  "$case_dir/project_row8_shard.py" "$case_dir/run_remote.sh" \
  "$JC2_ROOT/cases/as_fonly_d7_vertical_q9_state_gate_20260825/compile_shard.py" \
  > "$JOB_DIR/SOURCE.sha256"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  env JC2_ROOT="$JC2_ROOT" SHARD_INDEX="$SHARD_INDEX" \
      SHARD_COUNT="$SHARD_COUNT" OUTPUT_JSON="$JOB_DIR/result.json" \
  python3 "$case_dir/project_row8_shard.py" \
  > "$JOB_DIR/runner.stdout" 2> "$JOB_DIR/runner.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/runner.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
