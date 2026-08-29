#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V25 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: $0 AWS_ROOT AWS_JOB TAG CAP_KIB TIMEOUT_SECONDS FREEZE" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
freeze=$6
rel=cases/max12_812_order2_u2_62_k00_grade8_newest_block_v25_20260827

mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact_with_F65521_literal_fixtures\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'design=grade8_newest_fitting_block_with_allowed_k6_1\n'
  printf 'scope=no_augmented_relation_no_prefix_existence_no_later_grades_no_arc_no_closure_no_JC2\n'
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c "$freeze" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" \
  python3 "$rel/compile_grade8_newest_block_v25.py" "$aws_job/output" \
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
grep -Fqx 'K00_V25_PRODUCER=PASS' "$aws_job/run/compiler.stdout"
printf 'validator=PASS_EXACT_GRADE8_NEWEST_BLOCK\n' >> "$aws_job/run/FINAL.validation"
find "$aws_job/output" "$aws_job/run" "$aws_job/freeze_check.stdout" \
  "$aws_job/launch_registration.txt" -type f -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/EVIDENCE.sha256.tmp"
mv "$aws_job/EVIDENCE.sha256.tmp" "$aws_job/EVIDENCE.sha256"
