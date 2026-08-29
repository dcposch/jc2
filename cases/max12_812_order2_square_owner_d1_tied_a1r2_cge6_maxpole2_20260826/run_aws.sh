#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; timeout_seconds=$5; cap_kib=$6; source_sha=$7
case "$tag" in max12_812_order2_square_d1_tied_a1r2_cge6_maxpole2_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65519|65521) ;; *) exit 125 ;; esac
if [[ -e "$aws_job" ]]; then exit 125; fi
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"; printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"; printf 'source_archive_sha256=%s\n' "$source_sha"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_owner_d1_tied_a1r2_cge6_maxpole2_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$timeout_seconds" \
  bash -lc 'python3 cases/max12_812_order2_square_owner_d1_tied_a1r2_cge6_maxpole2_20260826/compile_tied_cge6_maxpole2.py "$1" --characteristic "$2" > "$3" 2> "$4" && for f in "$1"/*.sing; do Singular -q "$f" || exit $?; done' _ \
  "$aws_job/compiled" "$characteristic" "$aws_job/compiler.stdout" "$aws_job/compiler.stderr"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$aws_job/compiled"/* > "$aws_job/compiled.sha256"
for required in \
  'TC6_SOURCE_HASHES=PASS' \
  'TC6_COMPILER_VERSION=V2_ORDINARY_PART_REMAINDER' \
  'TC6_SCOPE=A1_R2_CGE6_UNIT_LOAD_G16_ONLY' \
  'TC6_PRIMITIVE_COUNT=3' \
  'TC6_UNIQUE_MAX_POLE=RA2_POLE2' \
  'TC6_PADDED_CUTOFF_IDENTICAL=1' \
  'TC6_SOURCE_DIVISIBLE=1' \
  'TC6_SOURCE_QUOTIENT_IDENTITIES=1' \
  'TC6_SOURCE_FORBIDDEN=1' \
  'TC6_ANALYTIC_DIVISIBLE=1' \
  'TC6_ROW_IDENTITIES_16=1' \
  'TC6_ALL_SEVEN_ROWS_BRIDGED=1' \
  'TC6_ALL_SOURCE_QUOTIENTS_EXACT=1' \
  'TC6_TARGETFREE_ALL_SEVEN=1' \
  'TC6_COMMON_N2=1' \
  'TC6_ORDINARY_PART_QUOTIENT_RETAINED=1' \
  'TC6_L2_RECURRENCE=1' \
  'TC6_BOTH_ROOT_FABER_IDENTITIES=1' \
  'TC6_DERIVATIVE_ROW_SYZYGY=1' \
  'TC6_C_DELAYED_BEYOND_G16=1' \
  'TC6_FOUR_ROOT_VALUE_CHARTS_COVERED=1' \
  'TC6_BOTH_EXACT_L_QUOTIENTS=1' \
  'TC6_QUOTIENT_TERMINALS=PLUS_MINUS_5_OVER_2_K0_LAM3_BU3' \
  'TC6_DERIVATIVE_TERMINALS=5_K0_LAM4_BU3' \
  'TC6_EXACT_TERMINAL_UNITS=1' \
  'TC6_NEGCTRL_OMIT_R3_ZERO_TERMINAL=1' \
  'TC6_FIRST_POLE_ONLY=ALLOCATION_NOT_ENDPOINT' \
  'TC6_ENDPOINT=PASS_EMPTY_A1_R2_CGE6_ON_D_P_K0'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" || grep -Fq '=FAIL' "$aws_job/compiler.stderr" \
   || grep -Fq '// **' "$stdout" || grep -Fq '// **' "$stderr" || grep -Fq '// **' "$aws_job/compiler.stderr" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr" || grep -Fq 'error occurred' "$aws_job/compiler.stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
if grep -Eq '^[[:space:]]*Swaps: [1-9]' "$stderr"; then
  printf 'validator=FAIL_NONZERO_SWAP\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_TIED_A1R2_CGE6_MAXPOLE2_EMPTY\n' >> "$validation"

