#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6
mkdir -p "$aws_job/run"; cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_odd_null_controls_v5_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
python3 cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_odd_null_controls_v5_20260826/compile_odd_null_v5.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
label=q; if [[ "$characteristic" != 0 ]]; then label=p${characteristic}; fi
for chart in x y; do
 set +e
 /usr/bin/time -v timeout "$timeout_seconds" Singular -q "$aws_job/compiled/affine_faber_a_g48n_${chart}_${label}.sing" > "$aws_job/run/${tag}_${chart}.stdout" 2> "$aws_job/run/${tag}_${chart}.stderr"
 engine_rc=$?
 set -e
 printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/${tag}_${chart}.validation"
 if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/${tag}_${chart}.validation"; exit "$engine_rc"; fi
 upper=$(printf '%s' "$chart" | tr '[:lower:]' '[:upper:]')
 for required in "A_G48N_${upper}_TCOEFF_CONTROL=1" "A_G48N_${upper}_LOWER_ZERO=1" "A_G48N_${upper}_DONE=1" "A_G48N_${upper}_SCOPE=FIXED_RATIONAL_${upper}_CHART_GRADE48_ODD_NULL_CONTROL_ONLY_NO_FULL_FAN_REES_ORDER2_MAX12_OR_JC2_VERDICT"; do
  if [[ "$(grep -Fxc "$required" "$aws_job/run/${tag}_${chart}.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/${tag}_${chart}.validation"; exit 92; fi
 done
 for prefix in "A_G48N_${upper}_C1=" "A_G48N_${upper}_C7=" "A_G48N_${upper}_GB=" "A_G48N_${upper}_UNIT="; do
  if [[ "$(grep -Fc "$prefix" "$aws_job/run/${tag}_${chart}.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE_PREFIX:%s\n' "$prefix" >> "$aws_job/run/${tag}_${chart}.validation"; exit 93; fi
 done
 printf 'validator=PASS_A_G48_ODD_NULL_%s\n' "$upper" >> "$aws_job/run/${tag}_${chart}.validation"
done

