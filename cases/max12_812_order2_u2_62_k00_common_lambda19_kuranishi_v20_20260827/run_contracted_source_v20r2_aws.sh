#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V20R2 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: run_contracted_source_v20r2_aws.sh AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
freeze=$6
rel=cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827

mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_with_F65521_fixture_control\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'design=V20R1_scalar_contraction_before_honest_weighted_specialization\n'
  printf 'dependency=V21R1_provisional_not_used_for_source_typing\n'
} > "$aws_job/launch_registration.txt"

cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" \
  python3 "$rel/compile_contracted_source_v20r2.py" "$aws_job/output" \
  > "$aws_job/run/compiler.stdout" 2> "$aws_job/run/compiler.stderr"
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
} >> "$aws_job/launch_registration.txt"
printf 'engine_rc=%s\n' "$rc" > "$aws_job/run/FINAL.validation"
if [[ "$rc" -ne 0 ]]; then
  exit "$rc"
fi
grep -Fqx 'K00_V20R2_ENDPOINT=PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE' \
  <(head -n 1 "$aws_job/run/compiler.stdout")
printf 'validator=PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE\n' \
  >> "$aws_job/run/FINAL.validation"
find "$aws_job/output" "$aws_job/run" -type f -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/run/ENDPOINT_EVIDENCE.sha256.tmp"
mv "$aws_job/run/ENDPOINT_EVIDENCE.sha256.tmp" "$aws_job/run/ENDPOINT_EVIDENCE.sha256"
