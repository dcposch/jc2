#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 7 ]; then
  echo "usage: $0 REPO OUTROOT PREFIX SHARD_COUNT TIMEOUT_SECONDS VMEM_KIB PYTHON_BIN" >&2
  exit 64
fi
repo=$1
outroot=$2
prefix=$3
shard_count=$4
timeout_seconds=$5
vmem_kib=$6
python_bin=$7
case_rel=cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825
ledger=$outroot/${prefix}_dispatch.meta
test ! -e "$ledger"
{
  printf 'prefix=%s\nhost=%s\nstart_utc=%s\n' \
    "$prefix" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field_order=16129\nshard_count=%s\n' "$shard_count"
  sha256sum "$repo/$case_rel/dispatch.sh" "$repo/$case_rel/run_shard.sh" \
    "$repo/$case_rel/count_shard.py"
} >"$ledger"
for ((index=0; index<shard_count; index++)); do
  start=$((index * 16129 / shard_count))
  stop=$(((index + 1) * 16129 / shard_count))
  tag=$(printf '%s_i%02d' "$prefix" "$index")
  launch_log=$outroot/${tag}.launch.log
  test ! -e "$outroot/$tag"
  PYTHON_BIN=$python_bin nohup bash "$repo/$case_rel/run_shard.sh" \
    "$repo" "$outroot" "$tag" "$start" "$stop" "$timeout_seconds" "$vmem_kib" \
    >"$launch_log" 2>&1 &
  pid=$!
  printf 'shard=%s start=%s stop=%s pid=%s\n' "$index" "$start" "$stop" "$pid" \
    >>"$ledger"
done
printf 'dispatch_end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >>"$ledger"
