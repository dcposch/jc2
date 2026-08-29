#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 5 ]]; then exit 125; fi

aws_root=$1
aws_job=$2
tag=$3
cap_kib=$4
timeout_seconds=$5
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_pade_coeff_verify_20260826/FREEZE.sha256 \
  > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 \
  cases/max12_812_order2_pade_coeff_verify_20260826/verify_pade_coefficients.py \
  > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"
  exit "$engine_rc"
fi
for required in \
  'PADE_T15_FACTOR=PASS' \
  'PADE_T16_FACTOR=PASS' \
  'PADE_T17_FACTOR=PASS' \
  'PADE_B_PLUS_P_A=PASS' \
  'PADE_C_REDUCTION_76=PASS' \
  'PADE_EXACT_COEFFICIENT_VERIFIER=PASS' \
  'PADE_SCOPE=COEFFICIENT_IDENTITIES_ONLY_NO_SCHEME_OR_ORDER2_VERDICT'
do
  if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"
    exit 90
  fi
done
printf 'validator=PASS_EXACT_IDENTITIES\n' >> "$aws_job/run/$tag.validation"
