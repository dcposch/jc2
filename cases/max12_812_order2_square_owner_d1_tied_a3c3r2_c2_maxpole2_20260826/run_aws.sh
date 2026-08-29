#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; evidence=$2; tag=$3; characteristic=$4; timeout_seconds=$5; cap_kib=$6; source_sha=$7
case "$tag" in max12_812_order2_square_d1_tied_a3c3r2_c2_maxpole2_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65519|65521) ;; *) exit 125 ;; esac
if [[ -e "$evidence" ]]; then exit 125; fi
mkdir -p "$evidence/run"
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$evidence"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"; printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"; printf 'source_archive_sha256=%s\n' "$source_sha"
} > "$evidence/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_owner_d1_tied_a3c3r2_c2_maxpole2_20260826/FREEZE.sha256 > "$evidence/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$evidence/run" "$tag" timeout "$timeout_seconds" \
  bash -lc 'python3 cases/max12_812_order2_square_owner_d1_tied_a3c3r2_c2_maxpole2_20260826/compile_tied_c2_maxpole2.py "$1" --characteristic "$2" > "$3" 2> "$4" && for f in "$1"/*.sing; do Singular -q "$f" || exit $?; done' _ \
  "$evidence/compiled" "$characteristic" "$evidence/compiler.stdout" "$evidence/compiler.stderr"
engine_rc=$?
set -e
stdout="$evidence/run/${tag}.stdout"; stderr="$evidence/run/${tag}.stderr"; validation="$evidence/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$evidence/compiled"/* > "$evidence/compiled.sha256"
for required in \
  'F433_SOURCE_HASHES=PASS' \
  'F433_SCOPE=A3_C3_R2_UNIT_LOAD_G16_ONLY' \
  'F433_PRIMITIVE_COUNT=4' \
  'F433_UNIQUE_MAX_POLE=C2_POLE2' \
  'F433_PADDED_CUTOFF_IDENTICAL=1' \
  'F433_SOURCE_DIVISIBLE=1' \
  'F433_SOURCE_QUOTIENT_IDENTITIES=1' \
  'F433_SOURCE_FORBIDDEN=1' \
  'F433_ANALYTIC_DIVISIBLE=1' \
  'F433_ROW_IDENTITIES_16=1' \
  'F433_ALL_SEVEN_ROWS_BRIDGED=1' \
  'F433_ALL_SOURCE_QUOTIENTS_EXACT=1' \
  'F433_TARGETFREE_ALL_SEVEN=1' \
  'F433_COMMON_N2=1' \
  'F433_ORDINARY_PART_QUOTIENT_RETAINED=1' \
  'F433_L2_RECURRENCE=1' \
  'F433_BOTH_ROOT_FABER_IDENTITIES=1' \
  'F433_MAXPOLE_ROOTS_C2_SQUARES=1' \
  'F433_BOTH_EXACT_C_CHARTS_UNIT=1' \
  'F433_EVALUATION_DETERMINANT_UNIT=1' \
  'F433_NEGCTRL_OMIT_C2_ZERO_ROOTS=1' \
  'F433_ENDPOINT=PASS_EMPTY_A3_C3_R2_ON_D_P_K0'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" || grep -Fq '=FAIL' "$evidence/compiler.stderr" \
   || grep -Fq '// **' "$stdout" || grep -Fq '// **' "$stderr" || grep -Fq '// **' "$evidence/compiler.stderr" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
if grep -Eq '^[[:space:]]*Swaps: [1-9]' "$stderr"; then
  printf 'validator=FAIL_NONZERO_SWAP\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_TIED_A3C3R2_C2_MAXPOLE2_EMPTY\n' >> "$validation"
