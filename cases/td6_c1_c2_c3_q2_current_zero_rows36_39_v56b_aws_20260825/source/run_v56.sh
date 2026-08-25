#!/usr/bin/env bash
set -euo pipefail

: "${TD6_OUTPUT_DIR:?set TD6_OUTPUT_DIR}"
: "${TD6_SHARD_INDEX:?set TD6_SHARD_INDEX}"
: "${TD6_SHARD_COUNT:?set TD6_SHARD_COUNT}"
mkdir -p "$TD6_OUTPUT_DIR"
export PYTHONHASHSEED=0 TD6_SHARD_MODE=current

exec systemd-run --user --scope -p MemoryMax=12G \
  /usr/bin/time -v timeout 7200 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_source_row_shards_v55_v56_20260825/replay.py
