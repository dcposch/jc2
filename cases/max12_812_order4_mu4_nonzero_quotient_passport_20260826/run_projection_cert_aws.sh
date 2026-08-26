#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only projection certificate refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only projection certificate refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 5 ]]; then
  echo "usage: run_projection_cert_aws.sh AWS_ROOT AWS_RUN TAG INPUT CAP_KIB" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
input=$4
cap_kib=$5
mkdir -p "$aws_run"
sha256sum "$input" > "$aws_run/SINGULAR_INPUT.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
ulimit -v "$cap_kib"
exec "$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" timeout 7200 Singular -q "$input"
