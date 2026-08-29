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
package=cases/max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_*_exact_rehom_* ]]; then
  exit 126
fi
if [[ "$memory_cap_kib" -ne 67108864 || "$wall_seconds" -ne 3600 ]]; then
  exit 127
fi
actual_manifest_sha256=$(sha256sum "$root/AWS_SOURCE_MANIFEST.sha256" | awk '{print $1}')
if [[ "$actual_manifest_sha256" != "$source_manifest_sha256" ]]; then
  exit 128
fi
(cd "$root" && sha256sum -c AWS_SOURCE_MANIFEST.sha256 >/dev/null)

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib=%s\nwall_seconds=%s\nsource_manifest_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$memory_cap_kib" "$wall_seconds" "$source_manifest_sha256" \
  > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$memory_cap_kib"
lane="${tag}_python"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$lane" timeout "$wall_seconds" \
  python3 "$package/rehomogenize_generic_qt_v43g4.py" "$job/output"
stdout="$job/run/${lane}.stdout"
grep -Fx 'V43G4_DENOMINATOR=5*t^6' "$stdout" >/dev/null
grep -Fx 'V43G4_CONTENT_REMOVED=1' "$stdout" >/dev/null
grep -Fx 'V43G4_PRODUCT_LEVELS=3,4' "$stdout" >/dev/null
grep -Fx 'V43G4_TOTAL_IDENTITY=5*t^6*a1^4' "$stdout" >/dev/null
grep -Fx 'V43G4_USED_ROWS=11' "$stdout" >/dev/null
grep -Fx 'PASS-A1-GENERIC-REHOM-V43G4' "$stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
cp "$job/output/result.json" "$job/RESULT.json"
printf 'end_utc=%s\noutcome=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  'exact-total-identity-5-t6-a1-4-replayed-requires-special-converter' \
  > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
