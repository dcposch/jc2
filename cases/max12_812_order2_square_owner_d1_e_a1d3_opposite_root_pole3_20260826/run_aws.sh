#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; timeout_seconds=$5; cap_kib=$6; source_sha=$7
case "$tag" in max12_812_order2_square_d1_e_a1d3_opposite_root_pole3_*) ;; *) exit 125 ;; esac
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
sha256sum -c cases/max12_812_order2_square_owner_d1_e_a1d3_opposite_root_pole3_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$timeout_seconds" \
  bash -lc 'python3 cases/max12_812_order2_square_owner_d1_e_a1d3_opposite_root_pole3_20260826/compile_e_pole3.py "$1" --characteristic "$2" > "$3" 2> "$4" && for f in "$1"/*.sing; do Singular -q "$f" || exit $?; done' _ \
  "$aws_job/compiled" "$characteristic" "$aws_job/compiler.stdout" "$aws_job/compiler.stderr"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$aws_job/compiled"/* > "$aws_job/compiled.sha256"
for required in \
  'B13_BASELINE=A1_D3_S1_G15_T18' \
  'B13_PRIMITIVE_COUNT=8' \
  'B13_GLOBAL_POLE_CEILING=3' \
  'B13_NEGCTRL_C2_AND_RA2_LOCAL_DOUBLE=1' \
  'B13_NEGCTRL_RA2_SECOND_CORRECTION=1' \
  'B13_ENDPOINT=PASS_ROUTE_DEDICATED_E_SUCCESSOR_NO_EMPTY_VERDICT' \
  'E_POLE3_SOURCE_HASHES=PASS' \
  'E_POLE3_COMPLETE_PRIMITIVE_COUNT=8' \
  'E_POLE3_SOLE_POLE3=MINUS_ONE_SIXTEENTH_A3_OVER_L3_AT_G18' \
  'E_POLE3_ALL_SEVEN_ROWS_BRIDGED=1' \
  'E_POLE3_RA2_SECOND_CORRECTION_RETAINED=1' \
  'E_POLE3_L3_RECURRENCE=1' \
  'E_POLE3_BOTH_FABER_ROOT_IDENTITIES=1' \
  'E_POLE3_BOTH_OPPOSITE_ROOT_TERMINALS=1' \
  'E_POLE3_TARGETFREE_ROWS_1356=1' \
  'E_POLE3_EXACT_UNIT_IDEALS=1' \
  'E_POLE3_ENDPOINT=PASS_EMPTY_E_A1_D3_RGE2_ON_D_P_K0'; do
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
printf 'validator=PASS_D1_E_A1D3_OPPOSITE_ROOT_POLE3_EMPTY\n' >> "$validation"
