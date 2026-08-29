#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 8 ]]; then exit 125; fi
root=$1; job=$2; tag=$3; characteristic=$4; cap=$5; compile_wall=$6; engine_wall=$7; archive_sha=$8
package=cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827
mkdir -p "$job/run"; printf 'tag=%s\nhost=%s\nstart_utc=%s\ncharacteristic=%s\nsource_archive_sha256=%s\n' "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$characteristic" "$archive_sha" > "$job/launch_registration.txt"
cd "$root"; sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"; export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_compiler" timeout "$compile_wall" python3 "$package/prolong_boundary_g18_v33.py" "$job/compiled" --characteristic "$characteristic"
script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["control_script"])' "$job/compiled/result.json")
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_singular" timeout "$engine_wall" Singular -q "$script"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" python3 "$package/validate_boundary_g18_v33.py" --result "$job/compiled/result.json" --stdout "$job/run/${tag}_singular.stdout" --stderr "$job/run/${tag}_singular.stderr" --characteristic "$characteristic" --output "$job/RESULT.json"
grep -Fx 'PASS-A1-BOUNDARY-PROLONG-G18-V33-VALIDATOR' "$job/run/${tag}_validator.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory' "$job/run"; then exit 91; fi
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$job/EVIDENCE.sha256"

