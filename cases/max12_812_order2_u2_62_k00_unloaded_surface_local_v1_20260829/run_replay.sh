#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing exact replay outside Linux" >&2
  exit 125
fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" != "Amazon EC2" ]]; then
  echo "refusing exact replay outside Amazon EC2" >&2
  exit 125
fi

case_dir=$(cd "$(dirname "$0")" && pwd)
cert_dir=$case_dir/aws_r6b_global_power_v4
cd "$cert_dir"
sha256sum -c CUSTODY.sha256
cd "$case_dir"
exec Singular -q replay_global_power.sing
