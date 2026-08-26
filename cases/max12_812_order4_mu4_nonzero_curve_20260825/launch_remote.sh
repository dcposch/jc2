#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 5 ]]; then
  echo "usage: launch_remote.sh MODE AWS_REPO_ROOT AWS_RUN_DIRECTORY REGISTERED_TAG INPUT_OR_DASH" >&2
  exit 125
fi

mode=$1
aws_root=$2
aws_run=$3
lane_tag=$4
input=$5
mkdir -p "$aws_run"
case "$mode" in
  compile)
    timeout_seconds=7200
    memory_cap_kib=134217728
    runner="$aws_root/cases/max12_812_order4_mu4_nonzero_curve_20260825/run_compile_aws.sh"
    ;;
  geometry)
    timeout_seconds=21600
    memory_cap_kib=402653184
    runner="$aws_root/cases/max12_812_order4_mu4_nonzero_curve_20260825/run_geometry_aws.sh"
    ;;
  *)
    echo "unknown mode: $mode" >&2
    exit 125
    ;;
esac

{
  printf 'registered_tag=%s\n' "$lane_tag"
  printf 'mode=%s\n' "$mode"
  printf 'host=%s\n' "$(hostname)"
  printf 'remote_repo_root=%s\n' "$aws_root"
  printf 'remote_job_dir=%s\n' "$aws_run"
  printf 'launcher_pid=%s\n' "$$"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'memory_cap_kib=%s\n' "$memory_cap_kib"
  printf 'input=%s\n' "$input"
  if [[ "$input" != "-" ]]; then
    printf 'input_sha256=%s\n' "$(sha256sum "$input" | cut -d ' ' -f 1)"
  fi
  printf 'registered_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$aws_run/launch_registration.txt"
printf '%s\n' "$$" > "$aws_run/launcher.pid"

if [[ "$mode" == "compile" ]]; then
  exec bash "$runner" "$aws_root" "$aws_run" "$lane_tag"
fi
exec bash "$runner" "$aws_root" "$aws_run" "$lane_tag" "$input"
