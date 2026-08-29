#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 4 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4
mkdir -p "$aws_job/run"
{
 printf 'tag=%s\nhost=%s\nlauncher_pid=%s\nstart_utc=%s\nvirtual_memory_cap_kib=%s\n' "$tag" "$(hostname)" "$$" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$cap_kib"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout 300 python3 cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/analyze_relative_cone.py "$aws_job/output" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En 'Traceback|RuntimeError|FAIL_' "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_KCONE_RAW_TERM_COUNT=371' 'A_KCONE_Q6_MINIMUM=45' 'A_KCONE_ENDPOINT=PASS_RAW_K_RELATIVE_CONE_V2' 'A_KCONE_DONE=1' 'A_KCONE_SCOPE=RAW_NORMALIZED_K_SUPPORT_GROUPING_AND_FIXED_DELAYED_Q_CONE_ONLY_NO_PREDECESSOR_REDUCTION_COEFFICIENT_FACTOR_SATURATION_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_FULL_K_RELATIVE_CONE_V2\n' >> "$aws_job/run/$tag.validation"
