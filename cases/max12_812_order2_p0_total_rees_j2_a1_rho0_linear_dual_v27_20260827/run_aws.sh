#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux || $# -ne 6 ]]; then exit 125; fi
root=$1; job=$2; tag=$3; cap=$4; wall=$5; archive_sha=$6
package=cases/max12_812_order2_p0_total_rees_j2_a1_rho0_linear_dual_v27_20260827
mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nsource_archive_sha256=%s\n' "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$archive_sha" > "$job/launch_registration.txt"
cd "$root"
sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_producer" timeout "$wall" python3 "$package/produce_a1_rho0_linear_dual_v27.py" "$job/output"
bash ops/aws_exact_lane.sh "$root" "$job/run" "${tag}_validator" timeout "$wall" python3 "$package/validate_a1_rho0_linear_dual_v27.py" "$job/output"
grep -Fx 'PASS-A1-RHO0-LINEAR-DUAL-V27-PRODUCER' "$job/run/${tag}_producer.stdout" >/dev/null
grep -Fx 'PASS-A1-RHO0-LINEAR-DUAL-V27-VALIDATOR' "$job/run/${tag}_validator.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory' "$job/run"; then exit 91; fi
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$job/EVIDENCE.sha256"

