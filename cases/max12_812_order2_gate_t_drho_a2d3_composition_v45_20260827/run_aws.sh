#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 6 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
cap=$4
compile_wall=$5
archive_sha=$6
package=cases/max12_812_order2_gate_t_drho_a2d3_composition_v45_20260827
mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nsource_archive_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$archive_sha" > "$job/launch_registration.txt"
cd "$root"
sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_compiler" \
  timeout "$compile_wall" python3 "$package/verify_drho_a2d3_v45.py" "$job/compiled"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" \
  python3 "$package/validate_drho_a2d3_v45.py" \
  --result "$job/compiled/result.json" \
  --compiler-stdout "$job/run/${tag}_compiler.stdout" \
  --compiler-stderr "$job/run/${tag}_compiler.stderr" --output "$job/RESULT.json"
grep -Fx 'PASS-KGT-DRHO-UAC-A2D3-V45-VALIDATOR' "$job/run/${tag}_validator.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$job/EVIDENCE.sha256"

