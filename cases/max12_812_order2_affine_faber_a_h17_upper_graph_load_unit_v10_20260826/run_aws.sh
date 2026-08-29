#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 5 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; timeout_seconds=$5
mkdir -p "$aws_job/run"; cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/analyze_upper_graph_v10.py "$aws_job/output" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
for required in 'A_H17_UPPER_GRAPH_LOAD=5/4*K10*a^3*E^7' 'A_H17_UPPER_GRAPH_UNIQUE=7<q<17/2' 'A_H17_UPPER_GRAPH_Q7_TIES=2' 'A_H17_UPPER_GRAPH_ENDPOINT=PASS_EXACT_GRAPH_LOAD_UNIT' 'A_H17_UPPER_GRAPH_DONE=1' 'A_H17_UPPER_GRAPH_SCOPE=INTERNAL_AFFINE_GRAPH_SPECIAL_FIBRE_H17_UPPER_CONE_ONLY_NO_POSITIVE_DEVIATION_COMPOSITION_BOUNDARY_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
  if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_H17_UPPER_GRAPH_LOAD_UNIT_V10\n' >> "$aws_job/run/$tag.validation"
