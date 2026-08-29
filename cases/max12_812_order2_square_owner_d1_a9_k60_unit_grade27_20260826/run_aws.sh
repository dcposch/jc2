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
sha256sum -c cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_20260826/compile_a9_k60_unit.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
if [[ "$characteristic" -eq 0 ]]; then label=q; else label="p${characteristic}"; fi
input="$aws_job/compiled/square_d1_a9_k60_unit_grade27_${label}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" "$aws_job/compiled/parent_v3_result.json" > "$aws_job/compiled.sha256"
for required in \
  'A9V3_LOAD_WEIGHT_DISTRIBUTIVITY_K10=190' \
  'A9V3_LOAD_WEIGHT_DISTRIBUTIVITY_K6=72' \
  'A9V3_LOAD_WEIGHT_DISTRIBUTIVITY_K2=27' \
  'D1A9_K60_LITERAL_TARGET_MU2_COUNT=1' \
  'D1A9_K60_LITERAL_TARGET_MU4_COUNT=1' \
  'D1A9_K60_LITERAL_TARGET_MU6_COUNT=1' \
  'D1A9_K60_LITERAL_TARGET_J_COUNT=1'; do
  if [[ "$(grep -Fxc "$required" "$aws_job/compiler.stdout" || true)" -ne 1 ]]; then exit 91; fi
done
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
for required in \
  'A9V2_SOURCE_HASHES=PASS' \
  'A9V2_RECURSIVE_QUOTIENT_IDENTITIES=1' \
  'A9V2_RECURSIVE_SOURCE_CENSUS_ENDPOINT=PASS_NAVIGATION_ONLY' \
  'D1A9_K60_PARENT_V3_REPLAY=1' \
  'D1A9_K60_GRADE27_IDENTITIES=1' \
  'D1A9_K60_MOVING_CONNECTION_AND_K6JET=1' \
  'D1A9_K60_DELAYED_K2_K10_K6=1' \
  'D1A9_K60_ALL_TARGETS_RETAINED=1' \
  'D1A9_K60_PARENT_COUNTS=1' \
  'D1A9_K60_FORCES_C_ZERO=1' \
  'D1A9_K60_EXACT_CONTACT_AUGMENTED_IDEAL_UNIT=1' \
  'D1A9_K60_CHEBYSHEV_PELL_CONTROL=1' \
  'D1A9_K60_UNIT_GRADE27_ENDPOINT=PASS_EMPTY_EXACT_CONTACT'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if [[ "$(grep -Ec '^A9V2_ROW_([0-9]|[12][0-9]|3[01])_[1-7]_NONZERO=[01]$' "$stdout" || true)" -ne 224 ]]; then
  printf 'validator=FAIL_ROW_STATUS_COUNT\n' >> "$validation"; exit 90
fi
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" \
   || grep -Fq '// **' "$stdout" || grep -Fq '// **' "$stderr" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_A9_K60_UNIT_GRADE27_EMPTY_EXACT_CONTACT\n' >> "$validation"

