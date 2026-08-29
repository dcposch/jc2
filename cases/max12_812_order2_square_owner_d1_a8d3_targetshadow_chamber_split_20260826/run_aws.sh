#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; evidence=$2; tag=$3; characteristic=$4; timeout_seconds=$5; cap_kib=$6; source_sha=$7
case "$tag" in max12_812_order2_square_d1_a8d3_targetshadow_*) ;; *) exit 125 ;; esac
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
sha256sum -c cases/max12_812_order2_square_owner_d1_a8d3_targetshadow_chamber_split_20260826/FREEZE.sha256 > "$evidence/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$evidence/run" "$tag" timeout "$timeout_seconds" \
  bash -lc 'python3 cases/max12_812_order2_square_owner_d1_a8d3_targetshadow_chamber_split_20260826/compile_chamber_split.py "$1" --characteristic "$2" > "$3" 2> "$4" && for f in "$1"/*.sing; do Singular -q "$f" || exit $?; done' _ \
  "$evidence/compiled" "$characteristic" "$evidence/compiler.stdout" "$evidence/compiler.stderr"
engine_rc=$?
set -e
stdout="$evidence/run/${tag}.stdout"; stderr="$evidence/run/${tag}.stderr"; validation="$evidence/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$evidence/compiled"/* > "$evidence/compiled.sha256"
for required in \
  'A8D3_SHADOW_SOURCE_HASHES=PASS' \
  'A8D3_SHADOW_LITERAL_ODD_ROWS_IMPORTED=4' \
  'A8D3_SHADOW_ROW1_G28_K60_C1=1' \
  'A8D3_SHADOW_SOURCE_RESIDUAL_MINUS3P_OVER32=1' \
  'A8D3_SHADOW_D_C1_BRANCH_SOURCE_ZERO=1' \
  'A8D3_SHADOW_V_C1_D_C0_BRANCH_SOURCE_ZERO=1' \
  'A8D3_SHADOW_TERMINAL_J_TARGET_EXACT=1' \
  'A8D3_SHADOW_D_C1_UNIT=1' \
  'A8D3_SHADOW_V_C1_D_C0_UNIT=1' \
  'A8D3_SHADOW_EXACT_C_CHART_COVER=1' \
  'A8D3_SHADOW_ENDPOINT=PASS_EMPTY_A8_D3_C11_RGE8_ON_D_PK0J'; do
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
printf 'validator=PASS_D1_A8D3_TARGETSHADOW_CHAMBER_EMPTY\n' >> "$validation"
