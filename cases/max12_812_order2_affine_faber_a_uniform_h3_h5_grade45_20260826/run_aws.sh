#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6; singular_bin=$7
mkdir -p "$aws_job/run"
{
 printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
 printf 'characteristic=%s\ntimeout_seconds=%s\nvirtual_memory_cap_kib=%s\n' "$characteristic" "$timeout_seconds" "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_uniform_h3_h5_grade45_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
compiled="$aws_job/compiled"
python3 cases/max12_812_order2_affine_faber_a_uniform_h3_h5_grade45_20260826/compile_uniform_h3_h5.py "$compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input=$(find "$compiled" -maxdepth 1 -name '*.sing' -type f -print -quit)
set +e
/usr/bin/time -v timeout "$timeout_seconds" "$singular_bin" -q "$input" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En '\?|// \*\*|error occurred' "$aws_job/compiler.stdout" "$aws_job/compiler.stderr" "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_LK45_TCOEFF_CONTROL=1' 'A_LK45_LOWER_ZERO=1' 'A_UH35_RAW_H3_MOD_S46=1' 'A_UH35_RAW_H5_MOD_S46=1' 'A_UH35_K_LOWER_ZERO=1' 'A_UH35_K45_CERTIFICATE=1' 'A_UH35_UNIT=1' 'A_UH35_ENDPOINT=PASS_RAW_UNIVERSAL_H3_H5_AND_LOCALIZED_UNIT' 'A_UH35_DONE=1' 'A_UH35_SCOPE=EXACT_MOVING_DISCRIMINANT_FORMAL_CHART_ORD_XY_GE6_DELAYED_LOAD_D_P_M_KK_NO_Q_LT6_COVERAGE_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
if [[ "$(grep -Fxc 'A_UH35_K45=-1/16*m^3*p' "$aws_job/run/$tag.stdout" || true)" -ne 1 && "$(grep -Fxc 'A_UH35_K45=-1/16*p*m^3' "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_K45_PRINT\n' >> "$aws_job/run/$tag.validation"; exit 93; fi
printf 'validator=PASS_A_UNIFORM_H3_H5_RAW_CERTIFICATE\n' >> "$aws_job/run/$tag.validation"
