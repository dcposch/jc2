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
sha256sum -c cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/compile_age10_j38_r3.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
if [[ "$characteristic" -eq 0 ]]; then label=q; else label="p${characteristic}"; fi
input="$aws_job/compiled/square_d1_age10_j38_odd_recurrence3_${label}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" "$aws_job/compiled/source_inventory.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
for required in \
  'D1J38R3_SOURCE_HASHES=PASS' \
  'D1J38R3_PRIMITIVE_FAMILY_COUNT=11' \
  'D1J38R3_POLE_GE4_MIN_GRADE=43' \
  'D1J38R3_MECHANICAL_JET_MAXIMA=A7_C10_R6_K106_K610_K26_P10' \
  'D1J38R3_ALL_SEVEN_SOURCE_ROWS_BRIDGED=1' \
  'D1J38R3_REQUIRED_A7_ENTERS_G38=1' \
  'D1J38R3_REQUIRED_K10_6_ENTERS_G38=1' \
  'D1J38R3_SOURCE_RECURRENCE_MOD_G39=1' \
  'D1J38R3_DIVISIBLE_G38=1' \
  'D1J38R3_GRADE38_COEFFICIENT_MINUS_J_OVER_4=1' \
  'D1J38R3_RECURRENCE_MOD_G39=1' \
  'D1J38R3_SYMBOLIC_THETA_ETA_SAFE=1' \
  'D1J38R3_EXACT_J_CONTACT_UNIT=1' \
  'D1J38R3_CHEBYSHEV_PELL_CONTROL=1' \
  'D1J38R3_ENDPOINT=PASS_EMPTY_UNIFORM_A_GE_10'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if [[ "$(grep -Ec '^D1J38R3_INVENTORY_SHA256=[0-9a-f]{64}$' "$stdout" || true)" -ne 1 ]] \
   || [[ "$(grep -Ec '^D1J38R3_ANALYTIC_MONOMIAL_COUNT=[1-9][0-9]*$' "$stdout" || true)" -ne 1 ]] \
   || [[ "$(grep -Ec '^D1J38R3_LITERAL_MONOMIAL_COUNT=[1-9][0-9]*$' "$stdout" || true)" -ne 1 ]]; then
  printf 'validator=FAIL_INVENTORY_MARKER\n' >> "$validation"; exit 90
fi
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" \
   || grep -Fq '// **' "$stdout" || grep -Fq '// **' "$stderr" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_AGE10_J38_ODD_RECURRENCE3\n' >> "$validation"
