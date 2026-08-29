#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 7 ]]; then exit 125; fi
root=$1; job=$2; tag=$3; prime=$4; cap=$5; wall=$6; archive_sha=$7
package=cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827
mkdir -p "$job/run"; printf 'tag=%s\nhost=%s\nstart_utc=%s\nselector_prime=%s\nsource_archive_sha256=%s\n' "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$prime" "$archive_sha" > "$job/launch_registration.txt"
cd "$root"; sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"; export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap"
python=/home/ubuntu/venvs/td6/bin/python; "$python" -c 'import flint; assert flint.__version__ == "0.9.0"'
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_compiler" timeout "$wall" "$python" "$package/solve_graded_ladder_v37.py" "$job/compiled" --selector-prime "$prime"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" "$python" "$package/validate_graded_ladder_v37.py" --result "$job/compiled/result.json" --compiler-stdout "$job/run/${tag}_compiler.stdout" --compiler-stderr "$job/run/${tag}_compiler.stderr" --selector-prime "$prime" --output "$job/RESULT.json"
grep -Fx 'PASS-A1-GRADED-LADDER-V37-VALIDATOR' "$job/run/${tag}_validator.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory' "$job/run"; then exit 91; fi
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$job/EVIDENCE.sha256"
