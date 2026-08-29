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
sha256sum -c cases/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
compiled="$aws_job/compiled"
python3 cases/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826/compile_graph_relative_multisupport.py "$compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
input=$(find "$compiled" -maxdepth 1 -name '*.sing' -type f -print -quit)
set +e
/usr/bin/time -v timeout "$timeout_seconds" "$singular_bin" -q "$input" > "$aws_job/run/$tag.stdout" 2> "$aws_job/run/$tag.stderr"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/run/$tag.validation"
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE_OR_TIMEOUT\n' >> "$aws_job/run/$tag.validation"; exit "$engine_rc"; fi
if grep -En '\?|// \*\*|error occurred' "$aws_job/compiler.stdout" "$aws_job/compiler.stderr" "$aws_job/run/$tag.stdout" "$aws_job/run/$tag.stderr" >/dev/null 2>&1; then printf 'validator=FAIL_DIAGNOSTIC\n' >> "$aws_job/run/$tag.validation"; exit 91; fi
for required in 'A_KGRAPH_TARGET_MU6_ZERO=1' 'A_KGRAPH_TARGET_J_ZERO=1' 'A_KGRAPH_TARGET_D4=1' 'A_KGRAPH_TARGET_DM=1' 'A_KGRAPH_CENTRAL_CUBIC=1' 'A_KGRAPH_TRANSVERSE_LAMBDA=1' 'A_KGRAPH_TRANSVERSE_CENTER=1' 'A_KGRAPH_MUTATION_DETECTED=1' 'A_KGRAPH_RAW_COORDINATES_GONE=1' 'A_KGRAPH_TERMS_BEGIN' 'A_KGRAPH_TERMS_END' 'A_KGRAPH_ENDPOINT=PASS_GRAPH_RELATIVE_MULTISUPPORT' 'A_KGRAPH_DONE=1' 'A_KGRAPH_SCOPE=GRAPH_RELATIVE_NORMALIZED_K_SUPPORT_ONLY_NO_PREDECESSOR_REDUCTION_NEWTON_FAN_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT'; do
 if [[ "$(grep -Fxc "$required" "$aws_job/run/$tag.stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$aws_job/run/$tag.validation"; exit 92; fi
done
term_count=$(sed -n 's/^A_KGRAPH_TERM_COUNT=//p' "$aws_job/run/$tag.stdout")
if [[ ! "$term_count" =~ ^[1-9][0-9]*$ ]]; then printf 'validator=FAIL_TERM_COUNT\n' >> "$aws_job/run/$tag.validation"; exit 93; fi
exp_count=$(grep -c '^A_KGRAPH_TERM_EXP=' "$aws_job/run/$tag.stdout" || true)
term_lines=$(grep -c '^A_KGRAPH_TERM=' "$aws_job/run/$tag.stdout" || true)
if [[ "$exp_count" -ne "$term_count" || "$term_lines" -ne "$term_count" ]]; then printf 'validator=FAIL_SUPPORT_CARDINALITY\n' >> "$aws_job/run/$tag.validation"; exit 94; fi
printf 'validator=PASS_A_GRAPH_RELATIVE_MULTISUPPORT\n' >> "$aws_job/run/$tag.validation"
