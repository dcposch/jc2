#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only weighted-block launcher refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: launch_remote_weighted_block.sh AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS CHARACTERISTIC FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
characteristic=$6
freeze=$7
v4_rel=cases/max12_812_order2_u2_62_k00_closure_weighted_v4_20260827
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'characteristic=%s\n' "$characteristic"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
python3 "$v4_rel/compile_weighted_block.py" \
  "$aws_job/compiled" --characteristic "$characteristic" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input="$aws_job/compiled/k00_weighted_block_char${characteristic}.sing"
sha256sum "$input" "$aws_job/compiled/compiler_result.json" > "$aws_job/compiled.sha256"
exec bash "$v4_rel/run_weighted_block_aws.sh" \
  "$aws_root" "$aws_job/run" "$lane_tag" "$input" "$cap_kib" "$timeout_seconds"
