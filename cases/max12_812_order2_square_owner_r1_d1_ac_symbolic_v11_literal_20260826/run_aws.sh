#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true); if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; characteristic=$5; compile_timeout=$6; engine_timeout=$7
mkdir -p "$aws_job/run_r1" "$aws_job/run_d1"
{
 printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"; printf 'job_dir=%s\n' "$aws_job"
 printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"; printf 'characteristic=%s\n' "$characteristic"
 printf 'compile_timeout_seconds=%s\n' "$compile_timeout"; printf 'per_engine_timeout_seconds=%s\n' "$engine_timeout"; printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"; printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"; sha256sum -c cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v11_literal_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v11_literal_20260826/compile_v11_literal.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"; if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
if [[ "$characteristic" -eq 0 ]]; then label=q; else label="p${characteristic}"; fi
r1_input="$aws_job/compiled/square_r1_v11_${label}.sing"; d1_input="$aws_job/compiled/square_d1_ac_v11_${label}.sing"
sha256sum "$r1_input" "$d1_input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run_r1" "${tag}_r1" timeout "$engine_timeout" Singular -q "$r1_input"
r1_rc=$?
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run_d1" "${tag}_d1" timeout "$engine_timeout" Singular -q "$d1_input"
d1_rc=$?
set -e
r1_stdout="$aws_job/run_r1/${tag}_r1.stdout"; d1_stdout="$aws_job/run_d1/${tag}_d1.stdout"; validation="$aws_job/validation"
printf 'r1_engine_rc=%s\nd1_engine_rc=%s\n' "$r1_rc" "$d1_rc" > "$validation"
if [[ "$r1_rc" -eq 124 || "$d1_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$r1_rc" -ne 0 || "$d1_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
for required in 'R1_SOURCE_HASHES=PASS' 'R1_SOURCE_DIVISIBLE=1' 'R1_SOURCE_QUOTIENT_IDENTITIES=1' 'R1_SOURCE_FORBIDDEN=1' 'R1_ANALYTIC_DIVISIBLE=1' 'R1_ROW_IDENTITIES_13=1' 'R1_DENOMINATOR_RECURRENCE=1' 'R1_NUMERATOR_IDENTITY=1' 'R1_LOCALIZED_REDUCED_SUPPORT_ZERO=1' 'R1_ENDPOINT=PASS_R1_LEADING_SECTION_ZERO_ON_DPK'; do
 if [[ "$(grep -Fxc "$required" "$r1_stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_R1_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90; fi
done
for required in 'D1AC_SOURCE_HASHES=PASS' 'D1AC_SOURCE_DIVISIBLE=1' 'D1AC_SOURCE_QUOTIENT_IDENTITIES=1' 'D1AC_SOURCE_FORBIDDEN=1' 'D1AC_ANALYTIC_DIVISIBLE=1' 'D1AC_ROW_IDENTITIES_15=1' 'D1AC_ROW_IDENTITIES_16=1' 'D1AC_SYMBOLIC_SHIFT_G15=1' 'D1AC_SYMBOLIC_SHIFT_G16_THREE_MODULES=1' 'D1AC_DENOMINATOR_RECURRENCE_G15=1' 'D1AC_DENOMINATOR_RECURRENCE_G16=1' 'D1AC_BOTH_ROOT_ORIENTATIONS=1' 'D1AC_UNMATCHED_DOUBLE_POLE=1' 'D1AC_ENDPOINT=PASS_SYMBOLIC_D1_UNIQUE_AC_DOUBLE_POLE_GATE' 'R1_D1_AC_PACKAGE_ENDPOINT=PASS'; do
 if [[ "$(grep -Fxc "$required" "$d1_stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_D1_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90; fi
done
if grep -Fq '=FAIL' "$r1_stdout" || grep -Eq '^[[:space:]]*\? ' "$r1_stdout" || grep -Fq '=FAIL' "$d1_stdout" || grep -Eq '^[[:space:]]*\? ' "$d1_stdout"; then printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90; fi
printf 'validator=PASS_R1_D1_AC_SYMBOLIC_V11_LITERAL\n' >> "$validation"
