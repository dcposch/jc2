#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only launcher refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only launcher refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 5 ]]; then
  echo "usage: launch_projection_cert_remote.sh AWS_ROOT AWS_JOB TAG MODE CAP_KIB" >&2
  exit 125
fi

aws_root=$1
aws_job=$2
lane_tag=$3
mode=$4
cap_kib=$5
case "$mode" in
  a6|prime-lift) ;;
  *) echo "invalid mode: $mode" >&2; exit 125 ;;
esac

mkdir -p "$aws_job/compiled" "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=7200\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'mode=%s\n' "$mode"
} > "$aws_job/launch_registration.txt"

cd "$aws_root"
sha256sum -c cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/FREEZE_PROJECTION_CERT_V1.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
python3 cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/compile_projection_cert_v1.py \
  cases/max12_812_order4_mu4_nonzero_curve_20260825/aws_compile_v2_box02_20260826T002224Z/compiled/coefficient_curve.sing \
  "$aws_job/compiled/projection_cert_v1.sing" --mode "$mode" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
sha256sum "$aws_job/compiled/projection_cert_v1.sing" > "$aws_job/compiled_input.sha256"

exec cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/run_projection_cert_aws.sh \
  "$aws_root" "$aws_job/run" "$lane_tag" \
  "$aws_job/compiled/projection_cert_v1.sing" "$cap_kib"
