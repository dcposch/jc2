#!/usr/bin/env bash
set -euo pipefail

: "${JOB_DIR:?}"
: "${SOURCE_ROOT:?}"
: "${LIST_COMPILER:?}"
: "${SHARD_INDEX:?}"
: "${SHARD_COUNT:=27}"

mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$LIST_COMPILER" > "$JOB_DIR/source.sha256"
ulimit -v 8388608
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=30s 43200 \
  env JC2_ROOT="$SOURCE_ROOT" SHARD_INDEX="$SHARD_INDEX" \
      SHARD_COUNT="$SHARD_COUNT" python3 "$LIST_COMPILER" \
  > "$JOB_DIR/shard.stdout" 2> "$JOB_DIR/shard.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/shard.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
sha256sum "$JOB_DIR"/shard.* > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
