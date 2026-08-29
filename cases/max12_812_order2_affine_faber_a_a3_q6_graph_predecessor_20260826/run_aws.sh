#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; timeout_seconds=$6; singular_bin=$7
mkdir -p "$aws_job/run"
{
 printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
 printf 'characteristic=%s\ntimeout_seconds=%s\nvirtual_memory_cap_kib=%s\n' "$characteristic" "$timeout_seconds" "$cap_kib"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_affine_faber_a_a3_q6_graph_predecessor_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
compiled="$aws_job/compiled"
python3 cases/max12_812_order2_affine_faber_a_a3_q6_graph_predecessor_20260826/compile_a3_q6_graph_predecessor.py "$compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input=$(find "$compiled" -maxdepth 1 -name '*.sing' -type f -print -quit)
set +e
/usr/bin/time -v timeout "$timeout_seconds" "$singular_bin" -q "$input" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En '\?|// \*\*|error occurred' "$aws_job/compiler.stdout" "$aws_job/compiler.stderr" "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_A3Q6_TCOEFF_CONTROL=1' 'A_A3Q6_LOWER_ZERO=1' 'A_A3Q6_ROW_CONTROL=1' 'A_A3Q6_DEPENDENCY_CONTROL=1' 'A_A3Q6_HAND_CONTROL=1' 'A_A3Q6_SUCCESSOR_OMISSION_CONTROL=1' 'A_A3Q6_GRAPH_K10_CANCEL=1' 'A_A3Q6_MUTATION_DETECTED=1' 'A_A3Q6_UNIT_X=1' 'A_A3Q6_UNIT_Y=1' 'A_A3Q6_ENDPOINT=PASS_GRAPH_PREDECESSOR_BOTH_CHARTS_EMPTY' 'A_A3Q6_DONE=1' 'A_A3Q6_SCOPE=FIXED_DELAYED_H15_A3_Q6_GRADE42_GRAPH_PREDECESSOR_ONLY_NO_SOURCE_COVER_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
printf 'validator=PASS_A_A3_Q6_GRAPH_PREDECESSOR\n' >> "$aws_job/run/$tag.validation"
printf 'PASS\n' > "$aws_job/status.txt"
