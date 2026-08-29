#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1
aws_job=$2
tag=$3
cap_kib=$4
characteristic=$5
compile_timeout=$6
engine_timeout=$7
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'compile_timeout_seconds=%s\n' "$compile_timeout"
  printf 'engine_timeout_seconds=%s\n' "$engine_timeout"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_disc_halfweight_k3_normalized_ray_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_disc_halfweight_k3_normalized_ray_20260826/compile_k3_normalized_ray.py \
  "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
input="$aws_job/compiled/disc_k3_normalized_ray_p${characteristic}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/$tag.stdout"
validation="$aws_job/run/$tag.validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit "$engine_rc"; fi
required=(
  'K3NR_SOURCE_HASHES=PASS'
  'K3NR_TRUNCATED_INVERSE=1'
  'K3NR_SIGMA12_DIVISIBLE=1'
  'K3NR_SIGMA12_BASE_ZERO=1'
  'K3NR_SIGMA13_KERNEL_ZERO=1'
  'K3NR_FORBIDDEN_LOW_GRADES=1'
  'K3NR_TANGENT_FREEZE_WEIGHT2=1'
  'K3NR_RAW_U1_MATCH=1'
  'K3NR_RAW_F1_ZERO=1'
  'K3NR_RAW_F2_MATCH=1'
  'K3NR_C17_RECURRENCE=1'
  'K3NR_LAST3_CERTIFICATE=1'
  'K3NR_ANALYTIC_BT_UNIT=1'
  'K3NR_SOURCE_BT_UNIT=1'
  'K3NR_ENDPOINT=PASS_NORMALIZED_RAY_SOURCE_UNIT'
)
for row in 1 2 3 4 5 6 7; do required+=("K3NR_ROW_COMPARE_${row}=1"); done
for marker in "${required[@]}"; do
  if [[ "$(grep -Fxc "$marker" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$marker" >> "$validation"
    exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Eq '^\? ' "$stdout"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"
  exit 90
fi
printf 'validator=PASS_K3_NORMALIZED_RAY_SOURCE_UNIT\n' >> "$validation"
