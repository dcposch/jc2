#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true); if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; characteristic=$5; compile_timeout=$6; engine_timeout=$7
mkdir -p "$aws_job/run"
{
 printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"; printf 'job_dir=%s\n' "$aws_job"
 printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"; printf 'characteristic=%s\n' "$characteristic"
 printf 'compile_timeout_seconds=%s\n' "$compile_timeout"; printf 'engine_timeout_seconds=%s\n' "$engine_timeout"; printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"; printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"; sha256sum -c cases/max12_812_order2_square_owner_lowcontact_c1_c2_v3_namespaced_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_owner_lowcontact_c1_c2_v3_namespaced_20260826/compile_rootwise_v3.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"; if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
if [[ "$characteristic" -eq 0 ]]; then label=q; else label="p${characteristic}"; fi
input="$aws_job/compiled/square_lowcontact_rootwise_v3_${label}.sing"; sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/$tag.stdout"; validation="$aws_job/run/$tag.validation"; printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit "$engine_rc"; fi
for required in 'SQUARE_LOW_C1_DIVISIBLE=1' 'SQUARE_LOW_C1_IDENTITIES=1' 'SQUARE_LOW_C1_FORBIDDEN=1' 'SQUARE_ROOTWISE_C1_ANALYTIC_DIVISIBLE=1' 'SQUARE_ROOTWISE_C1_ROW_IDENTITIES=1' 'SQUARE_ROOTWISE_C1_DIVISION_RECURRENCE=1' 'SQUARE_ROOTWISE_C1_REMAINDER_DEGREE=1' 'SQUARE_ROOTWISE_C1_G12_MOD_LOWER_EQUALS_THREE_EIGHTHS_C1_SQUARED=1' 'SQUARE_ROOTWISE_C1_ENDPOINT=PASS_LEADING_C1_KILLED' 'SQUARE_LOW_C2_DIVISIBLE=1' 'SQUARE_LOW_C2_IDENTITIES=1' 'SQUARE_LOW_C2_FORBIDDEN=1' 'SQUARE_ROOTWISE_C2_ANALYTIC_DIVISIBLE=1' 'SQUARE_ROOTWISE_C2_ROW_IDENTITIES=1' 'SQUARE_ROOTWISE_C2_DIVISION_RECURRENCE=1' 'SQUARE_ROOTWISE_C2_REMAINDER_DEGREE=1' 'SQUARE_ROOTWISE_C2_G14_AT_A_ROOT_EQUALS_THREE_EIGHTHS_C2_SQUARED=1' 'SQUARE_ROOTWISE_C2_ENDPOINT=PASS_LEADING_C2_KILLED' 'SQUARE_ROOTWISE_ENDPOINT=PASS_C1_C2_KILLED'; do
 if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90; fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Eq '^\? ' "$stdout"; then printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90; fi
printf 'validator=PASS_SQUARE_LOWCONTACT_ROOTWISE_V3\n' >> "$validation"

