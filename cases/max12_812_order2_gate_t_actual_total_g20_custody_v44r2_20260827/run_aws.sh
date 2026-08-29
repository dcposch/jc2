#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 7 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
mode=$4
cap=$5
wall=$6
archive_sha=$7
package=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r2_20260827
mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmode=%s\nsource_archive_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$mode" "$archive_sha" \
  > "$job/launch_registration.txt"
cd "$root"
sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap"
lane=$mode
if [[ "$mode" == qcross ]]; then lane=q; fi
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_${lane}_validator" \
  timeout "$wall" python3 "$package/validate_frozen_v44r1_v44r2.py" \
  --lane "$lane" --output "$job/RESULT_${lane}.json"
grep -Fx "PASS-ACT-TOT-G20-CUSTODY-V44R2-${lane^^}" "$job/run/${tag}_${lane}_validator.stdout" >/dev/null
if [[ "$mode" == qcross ]]; then
  export JC2_V44R2_CROSS_OUTPUT="$job/RESULT_CROSS.json"
  bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_cross_validator" \
    timeout "$wall" python3 "$package/validate_crosslane_v44r2.py"
  grep -Fx 'PASS-ACT-TOT-G20-CUSTODY-V44R2-CROSSLANE' "$job/run/${tag}_cross_validator.stdout" >/dev/null
fi
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$job/EVIDENCE.sha256"

