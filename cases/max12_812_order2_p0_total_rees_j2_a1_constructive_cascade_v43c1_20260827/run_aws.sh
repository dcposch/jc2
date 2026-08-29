#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 6 ]]; then
  exit 125
fi
root=$1
job=$2
tag=$3
memory_cap_kib=$4
wall_seconds=$5
source_manifest_sha256=$6
package=cases/max12_812_order2_p0_total_rees_j2_a1_constructive_cascade_v43c1_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_constructive_cascade_v43c1_* ]]; then
  exit 126
fi
if [[ "$memory_cap_kib" -ne 268435456 || "$wall_seconds" -ne 14400 ]]; then
  exit 127
fi

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib=%s\nwall_seconds=%s\nsource_manifest_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$memory_cap_kib" "$wall_seconds" "$source_manifest_sha256" \
  > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$memory_cap_kib"
lane="${tag}_exact_replay"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$lane" timeout "$wall_seconds" \
  python3 "$package/replay_constructive_cascade_v43c1.py" "$job/output"
grep -Fx 'PASS-A1-RHO0-RAW-CONSTRUCTIVE-CASCADE-A1-104' \
  "$job/run/${lane}.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
cp "$job/output/result.json" "$job/RESULT.json"
printf 'end_utc=%s\noutcome=exact-unsplit-rho0-a1-power-certificate\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
