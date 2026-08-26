#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only compiler refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only compiler refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 5 ]]; then
  echo "usage: run_compile_aws.sh AWS_ROOT AWS_RUN TAG SOURCE_INPUT OUTPUT_INPUT" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
source_input=$4
output_input=$5
mkdir -p "$aws_run" "$(dirname "$output_input")"
export JC2_REGISTERED_AWS_LANE=$lane_tag
sha256sum "$source_input" > "$aws_run/source_input.sha256"
python3 "$aws_root/cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/compile_invariant_graph_v1.py" \
  "$source_input" "$output_input" > "$aws_run/compiler.stdout" 2> "$aws_run/compiler.stderr"
sha256sum "$output_input" > "$aws_run/compiled_input.sha256"

