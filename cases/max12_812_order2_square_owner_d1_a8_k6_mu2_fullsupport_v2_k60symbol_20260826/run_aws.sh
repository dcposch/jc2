#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; characteristic=$5; compile_timeout=$6; engine_timeout=$7
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"; printf 'compile_timeout_seconds=%s\n' "$compile_timeout"
  printf 'engine_timeout_seconds=%s\n' "$engine_timeout"; printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_v2_k60symbol_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_v2_k60symbol_20260826/compile_v2_k60symbol.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
if [[ "$characteristic" -eq 0 ]]; then label=q; else label="p${characteristic}"; fi
input="$aws_job/compiled/square_d1_a8_k6_mu2_v2_${label}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
for required in \
  'A8Q0_SOURCE_HASHES=PASS' 'A8Q0_SOURCE_DIVISIBLE=1' 'A8Q0_SOURCE_QUOTIENT_IDENTITIES=1' \
  'A8Q0_SOURCE_SUPPORT_FILTER=1' 'A8Q0_ANALYTIC_DIVISIBLE=1' 'A8Q0_ROW_IDENTITIES_26=1' \
  'A8Q0_ROW_IDENTITY=1' 'A8Q0_DENOMINATOR_RECURRENCE=1' 'A8Q0_NUMERATOR_COEFFICIENTS=1' \
  'A8Q0_DK60_FORCES_C_ZERO=1' 'A8Q0_ENDPOINT=PASS_A8_Q6_ZERO_SIMPLE_POLE' \
  'A8QP_SOURCE_HASHES=PASS' 'A8QP_SOURCE_DIVISIBLE=1' 'A8QP_SOURCE_QUOTIENT_IDENTITIES=1' \
  'A8QP_SOURCE_SUPPORT_FILTER=1' 'A8QP_ANALYTIC_DIVISIBLE=1' 'A8QP_ROW_IDENTITIES_27=1' \
  'A8QP_ROW_IDENTITIES_28=1' 'A8QP_NEGCTRL_DELETE_T1_FAILS=1' \
  'A8QP_NEGCTRL_DELETE_K6C_FAILS=1' 'A8QP_NEGCTRL_DELETE_MU2_FAILS=1' \
  'A8QP_DENOMINATOR_RECURRENCE_FIRST=1' 'A8QP_DENOMINATOR_RECURRENCE_NEXT=1' \
  'A8QP_COMPLETE_SOURCE_BRIDGE=1' 'A8QP_BOTH_SHIFTED_ROOT_ALLOCATIONS=1' \
  'A8QP_MU2_L_MULTIPLE_C2_RESIDUE=1' 'A8QP_ENDPOINT=PASS_A8_POSITIVE_Q6_OR_ZERO_K6' \
  'D1_A8_K6_MU2_ENDPOINT=PASS'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" \
   || grep -Fq '// **' "$stdout" || grep -Fq '// **' "$stderr" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_A8_K6_MU2_V2_K60SYMBOL\n' >> "$validation"

