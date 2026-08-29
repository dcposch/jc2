#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 5 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; timeout_seconds=$5
mkdir -p "$aws_job/run"
{
 printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_graph_relative_cone_a3_v2_q6_face_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 cases/max12_812_order2_affine_faber_a_graph_relative_cone_a3_v2_q6_face_20260826/analyze_graph_relative_cone_a3_v2.py "$aws_job/run/output" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En 'Traceback|RuntimeError|error occurred' "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_KGRAPH_A3V2_TERM_COUNT=365' 'A_KGRAPH_A3V2_THRESHOLD_Q=6' 'A_KGRAPH_A3V2_Q6_NONSTRICT_COUNT=2' 'A_KGRAPH_A3V2_CENTRAL_K10_LOW_TERMS=0' 'A_KGRAPH_A3V2_ENDPOINT=PASS_A3_QGT6_DIRECT_UNIT_AND_Q6_EQUALITY_FACE' 'A_KGRAPH_A3V2_DONE=1' 'A_KGRAPH_A3V2_SCOPE=GRAPH_RELATIVE_K_SUPPORT_SPLIT_ONLY_Q6_EQUALITY_REQUIRES_PREDECESSOR_REDUCTION_NO_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_GRAPH_RELATIVE_CONE_A3_V2\n' >> "$aws_job/run/$tag.validation"
