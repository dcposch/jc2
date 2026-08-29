#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; characteristic=$5; timeout_seconds=$6; source_sha=$7
case "$tag" in max12_812_order2_square_d1_a7_loadtie_dual_*) ;; *) exit 125 ;; esac
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
sha256sum -c cases/max12_812_order2_square_owner_d1_a7_loadtie_dual_functional_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$timeout_seconds" \
  bash -lc 'python3 cases/max12_812_order2_square_owner_d1_a7_loadtie_dual_functional_20260826/compile_a7_loadtie.py "$1" --characteristic "$2" > "$3" 2> "$4" && for f in "$1"/*.sing; do Singular -q "$f" || exit $?; done' _ \
  "$aws_job/compiled" "$characteristic" "$aws_job/compiler.stdout" "$aws_job/compiler.stderr"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$aws_job/compiled"/* > "$aws_job/compiled.sha256"
for required in \
  'A7D2_PRIMITIVE_COLUMNS=5' \
  'A7D3_PRIMITIVE_COLUMNS=7' \
  'A7D2_RANK2_OFF_DELTA=1' \
  'A7D3_RANK2_OFF_DELTA=1' \
  'A7D2_DUAL_LEFT_KERNEL_TARGET_PAIR=1' \
  'A7D3_DUAL_LEFT_KERNEL_TARGET_PAIR=1' \
  'A7D2_EXACT_CONTACT_CHART_UNITS=1' \
  'A7D3_EXACT_CONTACT_CHART_UNITS=1' \
  'A7D2_ROW2_TARGET_RETAINED=1' \
  'A7D3_ROW2_TARGET_RETAINED=1' \
  'A7D2_ENDPOINT=PASS_EMPTY_A7_D2_CLOSED_R_TAIL' \
  'A7D3_ENDPOINT=PASS_EMPTY_A7_D3_CLOSED_R_TAIL'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
if grep -Eq '^[[:space:]]*Swaps: [1-9]' "$stderr"; then
  printf 'validator=FAIL_NONZERO_SWAP\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_A7_LOADTIE_DUAL_FUNCTIONAL_D2_D3_EMPTY\n' >> "$validation"
