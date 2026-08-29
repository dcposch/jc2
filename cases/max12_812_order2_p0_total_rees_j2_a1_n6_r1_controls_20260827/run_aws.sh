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
package=cases/max12_812_order2_p0_total_rees_j2_a1_n6_r1_controls_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_n6_r1_controls_* ]]; then exit 126; fi
if [[ "$memory_cap_kib" -ne 67108864 || "$wall_seconds" -ne 3600 ]]; then exit 127; fi
actual=$(sha256sum "$root/AWS_SOURCE_MANIFEST.sha256" | awk '{print $1}')
if [[ "$actual" != "$source_manifest_sha256" ]]; then exit 128; fi
(cd "$root" && sha256sum -c AWS_SOURCE_MANIFEST.sha256 >/dev/null)

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib=%s\nwall_seconds=%s\nsource_manifest_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$memory_cap_kib" \
  "$wall_seconds" "$source_manifest_sha256" > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$memory_cap_kib"
lane="${tag}_exact_replay"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$lane" timeout "$wall_seconds" \
  python3 "$package/replay_n6_r1_controls.py" "$job/output"
grep -Fx 'PASS-A1-N6-R1-ADDITIVE-CONTROLS' "$job/run/${lane}.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
cp "$job/output/result.json" "$job/RESULT.json"
printf 'end_utc=%s\noutcome=exact-additive-controls-pass\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)

