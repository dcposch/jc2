#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only one-parameter launcher refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only one-parameter launcher refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: launch_remote_oneparam.sh AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS CHARACTERISTIC FREEZE" >&2
  exit 125
fi

aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
characteristic=$6
freeze=$7

mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'characteristic=%s\n' "$characteristic"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"

cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
python3 cases/max12_812_order2_u2_62_oneparam_rees_20260826/compile_oneparam_rees.py \
  "$aws_job/compiled" --characteristic "$characteristic" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input="$aws_job/compiled/oneparam_rees_char${characteristic}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
exec bash cases/max12_812_order2_u2_62_oneparam_rees_20260826/run_oneparam_aws.sh \
  "$aws_root" "$aws_job/run" "$lane_tag" "$input" "$cap_kib" "$timeout_seconds"
