#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only launcher refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only launcher refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 3 ]]; then
  echo "usage: launch_remote.sh AWS_ROOT AWS_JOB TAG" >&2
  exit 125
fi

aws_root=$1
aws_job=$2
lane_tag=$3
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=7200\n'
  printf 'virtual_memory_cap_kib=134217728\n'
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order4_lemniscatic_target_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
exec cases/max12_812_order4_lemniscatic_target_20260826/run_lemniscatic_param_aws.sh \
  "$aws_root" "$aws_job/run" "$lane_tag" \
  "$aws_root/cases/max12_812_order4_lemniscatic_target_20260826/lemniscatic_param_v1.sing"
