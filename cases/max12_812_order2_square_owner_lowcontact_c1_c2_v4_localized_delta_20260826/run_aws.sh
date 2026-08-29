#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true); if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; compile_timeout=$5; engine_timeout=$6
mkdir -p "$aws_job/run"
{
 printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"; printf 'job_dir=%s\n' "$aws_job"
 printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"; printf 'characteristic=0\n'
 printf 'compile_timeout_seconds=%s\n' "$compile_timeout"; printf 'engine_timeout_seconds=%s\n' "$engine_timeout"; printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"
} > "$aws_job/launch_registration.txt"; printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"; sha256sum -c cases/max12_812_order2_square_owner_lowcontact_c1_c2_v4_localized_delta_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_owner_lowcontact_c1_c2_v4_localized_delta_20260826/compile_delta_v4.py "$aws_job/compiled" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"; if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
input="$aws_job/compiled/square_lowcontact_c2_localized_delta_v4_q.sing"; sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/$tag.stdout"; validation="$aws_job/run/$tag.validation"; printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit "$engine_rc"; fi
for required in 'SQUARE_ROOTWISE_C1_ENDPOINT=PASS_LEADING_C1_KILLED' 'SQUARE_ROOTWISE_C2_RAW_MEMBERSHIP=0' 'SQUARE_ROOTWISE_C2_LOCALIZED_IDEAL_PROPER=1' 'SQUARE_ROOTWISE_C2_RAW_DELTA_BEGIN' 'SQUARE_ROOTWISE_C2_RAW_DELTA_END' 'SQUARE_ROOTWISE_C2_LOCALIZED_DELTA_BEGIN' 'SQUARE_ROOTWISE_C2_LOCALIZED_DELTA_END'; do
 if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90; fi
done
if grep -Eq '^\? ' "$stdout"; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$validation"; exit 90; fi
if grep -Fqx 'SQUARE_ROOTWISE_C2_G14_AT_A_ROOT_EQUALS_THREE_EIGHTHS_C2_SQUARED=1' "$stdout"; then printf 'validator=PASS_LOCALIZED_MEMBERSHIP\n' >> "$validation"; else printf 'validator=PASS_DIAGNOSTIC_LOCALIZED_NONMEMBERSHIP\n' >> "$validation"; fi

