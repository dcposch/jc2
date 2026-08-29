#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only weighted-block runner refused host" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: run_weighted_block_aws.sh AWS_ROOT AWS_RUN TAG INPUT CAP_KIB TIMEOUT_SECONDS" >&2
  exit 125
fi
aws_root=$1
aws_run=$2
lane_tag=$3
input=$4
cap_kib=$5
timeout_seconds=$6
v1_rel=cases/max12_812_order2_u2_62_k00_closure_incidence_v1_20260827
v2_rel=cases/max12_812_order2_u2_62_k00_closure_gopen_v2_20260827
v4_rel=cases/max12_812_order2_u2_62_k00_closure_weighted_v4_20260827
artifact_dir="$aws_run/artifacts"
mkdir -p "$aws_run" "$artifact_dir"
sha256sum "$input" > "$aws_run/SINGULAR_INPUT.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" timeout "$timeout_seconds" \
  bash "$aws_root/$v1_rel/run_singular_in_dir.sh" "$artifact_dir" "$input"
engine_rc=$?
set -e
stdout="$aws_run/$lane_tag.stdout"
validation="$aws_run/$lane_tag.validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi
python3 "$aws_root/$v2_rel/validate_gopen.py" \
  "$stdout" "$artifact_dir" "$aws_run/../compiled/compiler_result.json" \
  "$aws_run/BASE_RESULT.json" --tag "$lane_tag" \
  > "$aws_run/base_validator.stdout" 2> "$aws_run/base_validator.stderr"
python3 "$aws_root/$v4_rel/validate_weighted_block.py" \
  "$stdout" "$aws_run/BASE_RESULT.json" "$aws_run/../compiled/compiler_result.json" \
  "$aws_run/RESULT.json" > "$aws_run/validator.stdout" 2> "$aws_run/validator.stderr"
printf 'validator=PASS\n' >> "$validation"
sha256sum "$aws_run/RESULT.json" "$artifact_dir/H_BASIS.txt" \
  > "$aws_run/ENDPOINT_EVIDENCE.sha256"
if [[ -f "$artifact_dir/H_UNIT_LIFT.txt" ]]; then
  sha256sum "$artifact_dir/H_UNIT_LIFT.txt" >> "$aws_run/ENDPOINT_EVIDENCE.sha256"
fi
