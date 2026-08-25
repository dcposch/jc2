#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: launch_saturation_remote.sh AWS_REPO_ROOT AWS_RUN_DIRECTORY REGISTERED_TAG STRICT_REES_SING" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
strict_rees=$4
mkdir -p "$aws_run"
{
  printf 'registered_tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'remote_job_dir=%s\n' "$(dirname "$aws_root")"
  printf 'launcher_pid=%s\n' "$$"
  printf 'timeout_seconds=%s\n' '14400'
  printf 'memory_cap_kib=%s\n' '268435456'
  printf 'strict_rees=%s\n' "$strict_rees"
  printf 'strict_rees_sha256=%s\n' "$(sha256sum "$strict_rees" | cut -d ' ' -f 1)"
  printf 'registered_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$(dirname "$aws_root")/launch_registration.txt"
printf '%s\n' "$$" > "$(dirname "$aws_root")/launcher.pid"

exec bash \
  "$aws_root/cases/max12_812_order2_u2_62_strict_rees_20260825/run_saturation_aws.sh" \
  "$aws_root" "$aws_run" "$lane_tag" "$strict_rees"
