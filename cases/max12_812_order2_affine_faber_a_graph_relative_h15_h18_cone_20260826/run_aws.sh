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
sha256sum -c cases/max12_812_order2_affine_faber_a_graph_relative_h15_h18_cone_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$timeout_seconds" python3 cases/max12_812_order2_affine_faber_a_graph_relative_h15_h18_cone_20260826/analyze_graph_relative_h15_h18.py "$aws_job/run/output" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En 'Traceback|RuntimeError|error occurred' "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_KGRAPH_H1518_TERM_COUNT=365' 'A_KGRAPH_H1518_UNSAFE_COUNT=0' 'A_KGRAPH_H1518_IDENTICAL_NONSTRICT_TIES=0' 'A_KGRAPH_H1518_H18_NONSTRICT_WALL=4*d4*a' 'A_KGRAPH_H1518_ENDPOINT=PASS_OPEN_15_H_18_DIRECT_UNIT_SUPPORT' 'A_KGRAPH_H1518_DONE=1' 'A_KGRAPH_H1518_SCOPE=GRAPH_RELATIVE_K_SUPPORT_AFTER_GRADE42_PREDECESSOR_QGT21MINUSH_ONLY_NO_PREDECESSOR_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_GRAPH_RELATIVE_H15_H18_CONE\n' >> "$aws_job/run/$tag.validation"
