#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "usage: run_compile_aws.sh AWS_REPO_ROOT AWS_RUN_DIRECTORY REGISTERED_TAG" >&2
  exit 125
fi
if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only runner refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only runner refused vendor=${vendor:-unknown}" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
if [[ -z "$aws_root" || -z "$aws_run" || -z "$lane_tag" ]]; then
  echo "root, run directory, and registered tag are mandatory" >&2
  exit 125
fi

mkdir -p "$aws_run" "$aws_run/output"
export JC2_REGISTERED_AWS_LANE=$lane_tag
ulimit -v 134217728
exec "$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" \
  timeout 7200 python3 \
  "$aws_root/cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees.py" \
  "$aws_run/output/compiled"
