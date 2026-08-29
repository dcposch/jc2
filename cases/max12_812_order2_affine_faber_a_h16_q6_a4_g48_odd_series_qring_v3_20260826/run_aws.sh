#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6
mkdir -p "$aws_job/run"; cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_odd_series_qring_v3_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
python3 cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_odd_series_qring_v3_20260826/compile_odd_series_qring_v3.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
label=q; if [[ "$characteristic" != 0 ]]; then label=p${characteristic}; fi
set +e
/usr/bin/time -v timeout "$timeout_seconds" Singular -q "$aws_job/compiled/affine_faber_a_h16_q6_a4_g48_odd_series_qring_v3_${label}.sing" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En '\? error occurred|Traceback|RuntimeError' "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_H16Q6A4_ODD_QRING_V3_TCOEFF_CONTROL=1' 'A_H16Q6A4_ODD_QRING_V3_TRUNCATION=s^49' 'A_H16Q6A4_ODD_QRING_V3_ENDPOINT=GRADE48_EMITTED' 'A_H16Q6A4_ODD_QRING_V3_DONE=1' 'A_H16Q6A4_ODD_QRING_V3_SCOPE=ROWS1_3_7_COMPLETE_SOURCE_MOD_S49_EXACT_THROUGH_G48_NO_PREDECESSOR_REDUCTION_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
if [[ "$(grep -Fc 'A_H16Q6A4_ODD_QRING_V3_48=' "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_GRADE48\n' >> "$aws_job/run/$tag.validation"; exit 93; fi
printf 'validator=PASS_A_H16_Q6_A4_G48_ODD_SERIES_QRING_V3\n' >> "$aws_job/run/$tag.validation"
