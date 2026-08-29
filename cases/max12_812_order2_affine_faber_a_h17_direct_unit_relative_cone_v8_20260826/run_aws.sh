#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 5 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; timeout_seconds=$5
mkdir -p "$aws_job/run"; cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v8_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v8_20260826/analyze_h17_cone_v8.py "$aws_job/output" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
for required in 'A_H17_CONE_SUPPORT=630' 'A_H17_CONE_UNIQUE=17/4<q<7' 'A_H17_CONE_LOWER_BLOCK=5' 'A_H17_CONE_UPPER_BLOCK=3' 'A_H17_CONE_ENDPOINT=PASS_EXACT_RELATIVE_CONE_V8' 'A_H17_CONE_DONE=1' 'A_H17_CONE_SCOPE=INTERNAL_NORMALIZED_GRAPH_SUPPORT_H17_EQUALITY_VALUATION_ONLY_NO_RATIONAL_REGRADING_TOTAL_REES_SOURCE_COVER_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_H17_DIRECT_UNIT_RELATIVE_CONE_V8\n' >> "$aws_job/run/$tag.validation"
