#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only seeded V3 launcher refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only seeded V3 launcher refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 4 ]]; then
  echo "usage: launch_remote_v3_rawgb.sh AWS_ROOT AWS_JOB TAG CAP_KIB" >&2
  exit 125
fi

aws_root=$1
aws_job=$2
lane_tag=$3
cap_kib=$4

mkdir -p "$aws_job/compiled" "$aws_job/run"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=3600\n'
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'mode=seeded-prime-v3-rawgb\n'
} > "$aws_job/launch_registration.txt"

cd "$aws_root"
sha256sum -c cases/max12_812_order4_seeded_projection_v2_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_v2_check.stdout"
sha256sum -c cases/max12_812_order4_seeded_projection_v3_rawgb_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_v3_check.stdout"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
python3 cases/max12_812_order4_seeded_projection_v2_20260826/compile_seeded_projection_v2.py \
  cases/max12_812_order4_mu4_nonzero_curve_20260825/aws_v2/max12_812_order4_mu4_nonzero_curve_v2_modsatQ_20260826T002334Z_box02/coefficient_curve_v2_modsatQ.sing \
  cases/max12_812_order4_mu4_nonzero_curve_20260825/aws_v2/max12_812_order4_mu4_nonzero_curve_v2_modsatQ_20260826T002334Z_box02/max12_812_order4_mu4_nonzero_curve_v2_modsatQ_20260826T002334Z_box02.stdout \
  "$aws_job/compiled/seeded_projection_v2.sing" --mode seeded-prime \
  > "$aws_job/compiler_v2.stdout" 2> "$aws_job/compiler_v2.stderr"
python3 cases/max12_812_order4_seeded_projection_v3_rawgb_20260826/compile_seeded_projection_v3_rawgb.py \
  "$aws_job/compiled/seeded_projection_v2.sing" \
  "$aws_job/compiled/seeded_projection_v3_rawgb.sing" \
  > "$aws_job/compiler_v3.stdout" 2> "$aws_job/compiler_v3.stderr"
sha256sum "$aws_job/compiled/seeded_projection_v2.sing" \
  "$aws_job/compiled/seeded_projection_v3_rawgb.sing" \
  > "$aws_job/compiled_inputs.sha256"
exec cases/max12_812_order4_seeded_projection_v3_rawgb_20260826/run_seeded_projection_aws_v3_rawgb.sh \
  "$aws_root" "$aws_job/run" "$lane_tag" \
  "$aws_job/compiled/seeded_projection_v3_rawgb.sing" "$cap_kib"
