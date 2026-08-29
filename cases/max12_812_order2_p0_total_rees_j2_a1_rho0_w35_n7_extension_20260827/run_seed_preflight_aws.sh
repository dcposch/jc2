#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 7 ]]; then
  exit 125
fi
root=$1
job=$2
tag=$3
memory_cap_kib=$4
total_wall_seconds=$5
source_manifest_sha256=$6
source_label=$7
package=cases/max12_812_order2_p0_total_rees_j2_a1_rho0_w35_n7_extension_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_rho0_w35_n7_preflight_* ]]; then
  exit 126
fi
if [[ "$memory_cap_kib" -ne 201326592 || "$total_wall_seconds" -ne 3600 ]]; then
  exit 127
fi

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib=%s\ntotal_wall_seconds=%s\nsource_manifest_sha256=%s\nsource_label=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$memory_cap_kib" \
  "$total_wall_seconds" "$source_manifest_sha256" "$source_label" \
  > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$memory_cap_kib"
lane="${tag}_compiler"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$lane" timeout "$total_wall_seconds" \
  python3 "$package/compile_w35_n7_seed_extension.py" "$job/preflight" \
  --phase preflight
grep -Fx 'PASS-A1-RHO0-W35-N7-SEED-EXTENSION-PREFLIGHT' \
  "$job/run/${lane}.stdout" >/dev/null
cp "$job/preflight/result.json" "$job/RESULT.json"
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
printf 'end_utc=%s\noutcome=preflight-only-no-math-verdict\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
