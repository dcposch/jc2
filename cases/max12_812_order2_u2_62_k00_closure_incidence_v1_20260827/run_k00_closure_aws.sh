#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only K00 closure runner refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only K00 closure runner refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: run_k00_closure_aws.sh AWS_ROOT AWS_RUN TAG INPUT CAP_KIB TIMEOUT_SECONDS" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
input=$4
cap_kib=$5
timeout_seconds=$6
case_rel=cases/max12_812_order2_u2_62_k00_closure_incidence_v1_20260827
artifact_dir="$aws_run/artifacts"

mkdir -p "$aws_run" "$artifact_dir"
sha256sum "$input" > "$aws_run/SINGULAR_INPUT.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" \
  timeout "$timeout_seconds" \
  bash "$aws_root/$case_rel/run_singular_in_dir.sh" "$artifact_dir" "$input"
engine_rc=$?
set -e

stdout="$aws_run/$lane_tag.stdout"
validation="$aws_run/$lane_tag.validation"
{
  printf 'engine_rc=%s\n' "$engine_rc"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"
  find "$aws_run" -maxdepth 2 -type f ! -name TIMEOUT_EVIDENCE.sha256 -print0 \
    | sort -z | xargs -0 sha256sum \
    > "$aws_run/TIMEOUT_EVIDENCE.sha256"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi

python3 "$aws_root/$case_rel/validate_closure.py" \
  "$stdout" "$artifact_dir" "$aws_run/../compiled/compiler_result.json" \
  "$aws_run/RESULT.json" --tag "$lane_tag" \
  --characteristic "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["characteristic"])' "$aws_run/../compiled/compiler_result.json")" \
  > "$aws_run/validator.stdout" 2> "$aws_run/validator.stderr"
printf 'validator=PASS\n' >> "$validation"
sha256sum "$aws_run/RESULT.json" "$artifact_dir/H_BASIS.txt" \
  > "$aws_run/ENDPOINT_EVIDENCE.sha256"
if [[ -f "$artifact_dir/H_UNIT_LIFT.txt" ]]; then
  sha256sum "$artifact_dir/H_UNIT_LIFT.txt" >> "$aws_run/ENDPOINT_EVIDENCE.sha256"
fi
