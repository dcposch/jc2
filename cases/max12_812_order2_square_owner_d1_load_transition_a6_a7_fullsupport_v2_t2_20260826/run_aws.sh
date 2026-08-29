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
sha256sum -c cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/compile_v2_t2.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
if [[ "$characteristic" -eq 0 ]]; then label=q; else label="p${characteristic}"; fi
input="$aws_job/compiled/square_d1_load_transition_a6_a7_v2_${label}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
for a in 6 7; do
  if [[ "$a" -eq 6 ]]; then g=23; gp=24; else g=25; gp=26; fi
  for required in \
    "A${a}_SOURCE_HASHES=PASS" "A${a}_FIXED_CONTACT=${a}" "A${a}_GRADE_PAIR=${g},${gp}" \
    "A${a}_SOURCE_DIVISIBLE=1" "A${a}_SOURCE_QUOTIENT_IDENTITIES=1" "A${a}_SOURCE_SUPPORT_FILTER=1" \
    "A${a}_ANALYTIC_DIVISIBLE=1" "A${a}_ROW_IDENTITIES_${g}=1" "A${a}_ROW_IDENTITIES_${gp}=1" \
    "A${a}_NEGCTRL_DELETE_T1_FAILS=1" "A${a}_NEGCTRL_DELETE_K6C_FAILS=1" "A${a}_NEGCTRL_DELETE_KRC_FAILS=1" \
    "A${a}_DENOMINATOR_RECURRENCE_FIRST=1" "A${a}_DENOMINATOR_RECURRENCE_NEXT=1" \
    "A${a}_COMPLETE_SOURCE_BRIDGE=1" "A${a}_BOTH_ROOT_ALLOCATIONS=1" "A${a}_UNMATCHED_C2_RESIDUE=1" \
    "A${a}_ENDPOINT=PASS_D1_K6_TRANSITION_A${a}"; do
    if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
      printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
    fi
  done
done
if [[ "$(grep -Fxc 'D1_LOAD_TRANSITION_A6_A7_ENDPOINT=PASS' "$stdout" || true)" -ne 1 ]]; then
  printf 'validator=FAIL_MISSING_OR_NONUNIQUE:PACKAGE_ENDPOINT\n' >> "$validation"; exit 90
fi
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" \
   || grep -Fq '// **' "$stdout" || grep -Fq '// **' "$stderr" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Eq '^[[:space:]]*\? ' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_LOAD_TRANSITION_A6_A7_V2_T2\n' >> "$validation"

