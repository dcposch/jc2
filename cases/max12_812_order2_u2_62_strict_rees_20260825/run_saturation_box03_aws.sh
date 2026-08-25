#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: run_saturation_box03_aws.sh AWS_REPO_ROOT AWS_RUN_DIRECTORY REGISTERED_TAG STRICT_REES_SING" >&2
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
strict_rees=$4
if [[ -z "$aws_root" || -z "$aws_run" || -z "$lane_tag" || -z "$strict_rees" ]]; then
  echo "root, run directory, registered tag, and strict-Rees input are mandatory" >&2
  exit 125
fi
if [[ ! -f "$strict_rees" ]]; then
  echo "strict-Rees input not found: $strict_rees" >&2
  exit 125
fi

mkdir -p "$aws_run"
export JC2_REGISTERED_AWS_LANE=$lane_tag
Singular --version > "$aws_run/SINGULAR.version"
sha256sum "$strict_rees" > "$aws_run/STRICT_REES_INPUT.sha256"
# Box03 had about 262 GiB available at preregistration.  Keep this lane at
# 192 GiB so the seven pre-existing Singular processes retain headroom.
ulimit -v 201326592
exec "$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" \
  timeout 14400 Singular "$strict_rees"
