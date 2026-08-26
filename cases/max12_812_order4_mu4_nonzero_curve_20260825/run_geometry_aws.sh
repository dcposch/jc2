#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: run_geometry_aws.sh AWS_REPO_ROOT AWS_RUN_DIRECTORY REGISTERED_TAG SINGULAR_INPUT" >&2
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
singular_input=$4
if [[ -z "$aws_root" || -z "$aws_run" || -z "$lane_tag" || -z "$singular_input" ]]; then
  echo "root, run directory, tag, and Singular input are mandatory" >&2
  exit 125
fi
if [[ ! -f "$singular_input" ]]; then
  echo "Singular input missing: $singular_input" >&2
  exit 125
fi

mkdir -p "$aws_run"
export JC2_REGISTERED_AWS_LANE=$lane_tag
Singular --version > "$aws_run/SINGULAR.version"
sha256sum "$singular_input" > "$aws_run/SINGULAR_INPUT.sha256"
ulimit -v 402653184
exec "$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" \
  timeout 21600 Singular -q "$singular_input"
