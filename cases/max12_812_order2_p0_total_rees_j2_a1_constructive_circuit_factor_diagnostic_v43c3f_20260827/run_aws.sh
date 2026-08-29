#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 6 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
memory_cap_kib=$4
wall_seconds=$5
source_manifest_sha256=$6
package=cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_factor_diagnostic_v43c3f_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_v43c3_factor_v43c3f_* ]]; then exit 126; fi
if [[ "$memory_cap_kib" -ne 4194304 || "$wall_seconds" -ne 600 ]]; then exit 127; fi
actual=$(sha256sum "$root/AWS_SOURCE_MANIFEST.sha256" | awk '{print $1}')
if [[ "$actual" != "$source_manifest_sha256" ]]; then exit 128; fi
(cd "$root" && sha256sum -c AWS_SOURCE_MANIFEST.sha256 >/dev/null)

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib=%s\nwall_seconds=%s\nsource_manifest_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$memory_cap_kib" \
  "$wall_seconds" "$source_manifest_sha256" > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"
lane="${tag}_exact_factor_diagnostic"
(
  ulimit -v "$memory_cap_kib"
  bash ops/aws_exact_lane.sh "$root" "$job/run" "$lane" timeout "$wall_seconds" \
    python3 "$package/diagnose_factors_v43c3f.py" "$job/output"
)
stdout="$job/run/${lane}.stdout"
grep -Fx 'PASS-V43C3F-EXACT-TOP-LEVEL-FACTOR-DIAGNOSTIC-ONLY' "$stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
printf 'end_utc=%s\noutcome=exact-factor-diagnostic-only\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$job/finish_registration.txt"
(cd "$job" && find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256)
