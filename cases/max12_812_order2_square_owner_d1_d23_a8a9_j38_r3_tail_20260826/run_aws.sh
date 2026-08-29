#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 9 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; characteristic=$5; a=$6; d=$7; timeout_seconds=$8; source_sha=$9
case "$tag" in max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65519|65521) ;; *) exit 125 ;; esac
case "$a:$d" in
  8:3) count=17; pole4=41; source_jets=100 ;;
  9:2) count=13; pole4=42; source_jets=94 ;;
  9:3) count=13; pole4=43; source_jets=87 ;;
  *) exit 125 ;;
esac
if [[ -e "$aws_job" ]]; then exit 125; fi
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"; printf 'cell=a%s_d%s\n' "$a" "$d"
  printf 'timeout_seconds=%s\n' "$timeout_seconds"; printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'source_archive_sha256=%s\n' "$source_sha"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$timeout_seconds" \
  bash -lc 'python3 cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/compile_tail_r3.py "$1" --characteristic "$2" --a "$3" --d "$4" > "$5" 2> "$6" && for f in "$1"/*.sing; do Singular -q "$f" || exit $?; done' _ \
  "$aws_job/compiled" "$characteristic" "$a" "$d" "$aws_job/compiler.stdout" "$aws_job/compiler.stderr"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$aws_job/compiled"/* > "$aws_job/compiled.sha256"
prefix="D1A${a}D${d}J38R3"
for required in \
  "${prefix}_SOURCE_HASHES=PASS" \
  "${prefix}_PRIMITIVE_FAMILY_COUNT=${count}" \
  "${prefix}_MAX_POLE_THROUGH_G38=3" \
  "${prefix}_FIRST_POLE4_GRADE=${pole4}" \
  "${prefix}_ALL_LICENSED_SOURCE_JETS_IN_INVENTORY=1" \
  "${prefix}_LICENSED_SOURCE_JET_COUNT=${source_jets}" \
  "${prefix}_LICENSED_TARGET_JET_COUNT=22" \
  "${prefix}_ALL_SEVEN_SOURCE_ROWS_BRIDGED=1" \
  "${prefix}_ALL_LICENSED_TARGET_JETS_RETAINED=1" \
  "${prefix}_ALL_MECHANICAL_JET_MAXIMA_ENTER_G38=1" \
  "${prefix}_SOURCE_R3_MOD_G39=1" \
  "${prefix}_ETA_RTAIL_SAFE=1" \
  "${prefix}_GRADE38_COEFFICIENT_MINUS_J_OVER_4=1" \
  "${prefix}_FULL_R3_MOD_G39=1" \
  "${prefix}_EXACT_DJ_UNIT=1" \
  "${prefix}_ENDPOINT=PASS_EMPTY_A${a}_D${d}_RGE${a}_ON_DJ"; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if [[ "$(grep -Ec "^${prefix}_INVENTORY_SHA256=[0-9a-f]{64}$" "$stdout" || true)" -ne 1 ]] \
   || [[ "$(grep -Ec "^${prefix}_ANALYTIC_MONOMIAL_COUNT=[1-9][0-9]*$" "$stdout" || true)" -ne 1 ]] \
   || [[ "$(grep -Ec "^${prefix}_LITERAL_MONOMIAL_COUNT=[1-9][0-9]*$" "$stdout" || true)" -ne 1 ]]; then
  printf 'validator=FAIL_INVENTORY_MARKER\n' >> "$validation"; exit 90
fi
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" || grep -Fq '=FAIL' "$aws_job/compiler.stderr" \
   || grep -Fq '// **' "$stdout" || grep -Fq '// **' "$stderr" || grep -Fq '// **' "$aws_job/compiler.stderr" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr" || grep -Fq 'error occurred' "$aws_job/compiler.stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
if grep -Eq '^[[:space:]]*Swaps: [1-9]' "$stderr"; then
  printf 'validator=FAIL_NONZERO_SWAP\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_A%s_D%s_J38_R3_TAIL_EMPTY\n' "$a" "$d" >> "$validation"
