#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 7 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
characteristic=$4
cap=$5
compile_wall=$6
archive_sha=$7
package=cases/max12_812_order2_gate_t_actual_total_g20_custody_v44_20260827
mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\ncharacteristic=%s\nsource_archive_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$characteristic" "$archive_sha" \
  > "$job/launch_registration.txt"
cd "$root"
sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_compiler" \
  timeout "$compile_wall" python3 "$package/compile_actual_total_g20_v44.py" \
  "$job/compiled" --characteristic "$characteristic"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" \
  python3 "$package/validate_actual_total_g20_v44.py" \
  --result "$job/compiled/result.json" \
  --compiler-stderr "$job/run/${tag}_compiler.stderr" \
  --characteristic "$characteristic" --output "$job/RESULT.json"
grep -Fx 'PASS-ACT-TOT-G20-CUSTODY-V44-VALIDATOR' "$job/run/${tag}_validator.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$job/EVIDENCE.sha256"

