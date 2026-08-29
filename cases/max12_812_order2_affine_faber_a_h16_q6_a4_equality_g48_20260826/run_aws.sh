#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6; archive_sha=$7
mkdir -p "$aws_job/run"
{
 printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"; printf 'source_archive_sha256=%s\n' "$archive_sha"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_h16_q6_a4_equality_g48_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
python3 cases/max12_812_order2_affine_faber_a_h16_q6_a4_equality_g48_20260826/compile_h16_q6_a4_g48.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
label=q; if [[ "$characteristic" != 0 ]]; then label=p${characteristic}; fi
set +e
/usr/bin/time -v timeout "$timeout_seconds" Singular -q "$aws_job/compiled/affine_faber_a_h16_q6_a4_g48_${label}.sing" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En '\? error occurred|Traceback|RuntimeError' "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_H16Q6A4_TCOEFF_CONTROL=1' 'A_H16Q6A4_LOWER_ZERO=1' 'A_H16Q6A4_ENDPOINT=FIXED_REPRESENTATIVE_THROUGH_GRADE48_EMITTED' 'A_H16Q6A4_DONE=1' 'A_H16Q6A4_SCOPE=H16_Q6_A4_FIXED_REPRESENTATIVE_SOURCE_ROWS_G44_TO_G48_ONLY_NO_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
for required_prefix in 'A_H16Q6A4_C44_1=' 'A_H16Q6A4_C48_7=' 'A_H16Q6A4_K48=' 'A_H16Q6A4_K48_NF=' 'A_H16Q6A4_UNIT_X=' 'A_H16Q6A4_UNIT_Y='; do
 if [[ "$(grep -Fc "$required_prefix" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE_PREFIX:%s\n' "$required_prefix" >> "$aws_job/run/$tag.validation"; exit 93; fi
done
printf 'validator=PASS_A_H16_Q6_A4_G48_FIXED_PRODUCER\n' >> "$aws_job/run/$tag.validation"
