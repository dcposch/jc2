#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 6 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
memory_cap_kib=$4
wall_seconds=$5
source_manifest_sha256=$6
package=cases/max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_v2_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_v2_* ]]; then exit 126; fi
if [[ "$memory_cap_kib" -ne 8388608 || "$wall_seconds" -ne 1200 ]]; then exit 127; fi
actual=$(sha256sum "$root/AWS_SOURCE_MANIFEST.sha256" | awk '{print $1}')
if [[ "$actual" != "$source_manifest_sha256" ]]; then exit 128; fi
(cd "$root" && sha256sum -c AWS_SOURCE_MANIFEST.sha256 >/dev/null)

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib=%s\nwall_seconds=%s\nsource_manifest_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$memory_cap_kib" \
  "$wall_seconds" "$source_manifest_sha256" > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"
lane="${tag}_exact_total_converter_v2"
(
  ulimit -v "$memory_cap_kib"
  bash ops/aws_exact_lane.sh "$root" "$job/run" "$lane" timeout "$wall_seconds" \
    python3 "$package/replay_total_converter_v43c5_v2.py" "$job/output"
)
stdout="$job/run/${lane}.stdout"
grep -Fx 'PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5-V2' "$stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
cp "$job/output/result.json" "$job/RESULT.json"
printf 'end_utc=%s\noutcome=exact-total-a1-628-circuit-certificate-v2-replayed\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$job/finish_registration.txt"
(cd "$job" && find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256)
