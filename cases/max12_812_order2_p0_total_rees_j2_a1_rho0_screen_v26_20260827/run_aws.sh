#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 6 ]]; then exit 125; fi
root=$1; job=$2; tag=$3; cap=$4; wall=$5; archive_sha=$6
package=cases/max12_812_order2_p0_total_rees_j2_a1_rho0_screen_v26_20260827
mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nsource_archive_sha256=%s\n' "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$archive_sha" > "$job/launch_registration.txt"
cd "$root"; sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap"
/usr/bin/time -v timeout 300 python3 "$package/compile_a1_rho0_v26.py" "$job/compiled" > "$job/compiler.stdout" 2> "$job/compiler.stderr"
script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["script"])' "$job/compiled/compile_result.json")
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_singular" timeout "$wall" Singular -q "$script"
stdout="$job/run/${tag}_singular.stdout"; stderr="$job/run/${tag}_singular.stderr"
if grep -Eq 'FAIL_|\?|error occurred|Killed|out of memory' "$stdout" "$stderr"; then exit 91; fi
grep -Fx 'V26_CONTROLS=1' "$stdout" >/dev/null
grep -Fx 'PASS_A1_RHO0_SCREEN_V26' "$stdout" >/dev/null
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$job/EVIDENCE.sha256"
