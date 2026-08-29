#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only local membership runner refused host" >&2
  exit 125
fi
if [[ $# -ne 7 ]]; then
  echo "usage: run_local_membership_aws.sh AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS FREEZE MODE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
freeze=$6
mode=$7
if [[ "$mode" != "exact_q" ]]; then
  echo "unsupported local membership mode" >&2
  exit 125
fi
rel=cases/max12_812_order2_u2_62_k00_local_membership_v11_20260827
v1rel=cases/max12_812_order2_u2_62_k00_closure_incidence_v1_20260827
mkdir -p "$aws_job/run/artifacts"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'mode=%s\n' "$mode"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
python3 "$rel/compile_local_membership.py" "$aws_job/compiled" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input="$aws_job/compiled/k00_local_membership_q.sing"
sha256sum "$input" "$aws_job/compiled/compiler_result.json" > "$aws_job/compiled.sha256"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_job/run" "$lane_tag" timeout "$timeout_seconds" \
  bash "$aws_root/$v1rel/run_singular_in_dir.sh" "$aws_job/run/artifacts" "$input"
rc=$?
set -e
printf 'engine_rc=%s\n' "$rc" > "$aws_job/run/FINAL.validation"
if [[ "$rc" -ne 0 ]]; then
  exit "$rc"
fi
python3 "$rel/validate_local_membership.py" \
  "$aws_job/run/$lane_tag.stdout" "$aws_job/run/artifacts" \
  "$aws_job/compiled/compiler_result.json" "$aws_job/run/RESULT.json" \
  > "$aws_job/run/validator.stdout" 2> "$aws_job/run/validator.stderr"
printf 'validator=PASS_LOCAL_MEMBERSHIP\n' >> "$aws_job/run/FINAL.validation"
sha256sum "$aws_job/run/RESULT.json" "$aws_job/run/artifacts/LOCAL_STANDARD_BASIS.txt" \
  "$aws_job/run/artifacts/LOCAL_BASIS_TRANSFORM.txt" > "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
if [[ -f "$aws_job/run/artifacts/LOCAL_MEMBERSHIP_UNIT.txt" ]]; then
  sha256sum "$aws_job/run/artifacts/LOCAL_MEMBERSHIP_UNIT.txt" \
    "$aws_job/run/artifacts/LOCAL_MEMBERSHIP_MULTIPLIERS.txt" >> "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
else
  sha256sum "$aws_job/run/artifacts/LOCAL_NONMEMBERSHIP_RESIDUAL.txt" \
    "$aws_job/run/artifacts/LOCAL_LEADING_TRANSVERSE_CLASS.txt" >> "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
fi
