#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only unloaded V8 launcher refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: launch_remote_unloaded_membership_v8.sh AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS MODE FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
mode=$6
freeze=$7
rel=cases/max12_812_order2_u2_62_k00_unloaded_membership_v8_20260827
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'mode=%s\n' "$mode"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
python3 "$rel/compile_unloaded_membership_v8.py" "$aws_job/compiled" --mode "$mode" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input="$aws_job/compiled/k00_unloaded_v8_${mode}_q.sing"
sha256sum "$input" "$aws_job/compiled/compiler_result.json" > "$aws_job/compiled.sha256"
exec bash "$rel/run_unloaded_membership_v8_aws.sh" \
  "$aws_root" "$aws_job/run" "$lane_tag" "$input" "$cap_kib" "$timeout_seconds" "$mode"
