#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only mod-32003 plane client refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only mod-32003 plane client refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 4 ]]; then
  echo "usage: run_plane_mod32003_aws.sh AWS_ROOT AWS_RUN TAG SOURCE_INPUT" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
source_input=$4
compiled=$aws_run/plane_mod32003_v1.sing
mkdir -p "$aws_run"
export JC2_REGISTERED_AWS_LANE=$lane_tag
python3 "$aws_root/cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/compile_plane_mod32003_v1.py" \
  "$source_input" "$compiled" > "$aws_run/compiler.stdout" 2> "$aws_run/compiler.stderr"
sha256sum "$source_input" "$compiled" > "$aws_run/inputs.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
ulimit -v 67108864
exec "$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" timeout 3600 Singular -q "$compiled"
