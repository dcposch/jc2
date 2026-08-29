#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V24 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: run_grade7_cokernel_v24_aws.sh AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
freeze=$6
rel=cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827

mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact_with_F65521_diagnostic\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'design=exact_grade7_two_cokernel_contraction_on_W_and_k10_unit_chart\n'
  printf 'scope=no_Wzero_no_grades8to19_no_full_jet_no_arc_no_closure_no_JC2\n'
} > "$aws_job/launch_registration.txt"

cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" \
  python3 "$rel/compile_grade7_cokernel_v24.py" "$aws_job/output" \
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
grep -Fqx 'K00_V24_PRODUCER=PASS' "$aws_job/run/compiler.stdout"
printf 'validator=PASS_EXACT_TWO_COMPATIBILITY_POLYNOMIALS\n' >> "$aws_job/run/FINAL.validation"
find "$aws_job/output" "$aws_job/run" -type f -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/EVIDENCE.sha256.tmp"
mv "$aws_job/EVIDENCE.sha256.tmp" "$aws_job/EVIDENCE.sha256"
