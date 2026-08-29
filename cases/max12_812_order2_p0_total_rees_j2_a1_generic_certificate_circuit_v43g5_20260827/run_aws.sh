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
package=cases/max12_812_order2_p0_total_rees_j2_a1_generic_certificate_circuit_v43g5_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_generic_certificate_circuit_v43g5_*_exact_circuit_* ]]; then
  exit 126
fi
if [[ "$memory_cap_kib" -ne 134217728 || "$wall_seconds" -ne 21600 ]]; then
  exit 127
fi
actual_manifest_sha256=$(sha256sum "$root/AWS_SOURCE_MANIFEST.sha256" | awk '{print $1}')
if [[ "$actual_manifest_sha256" != "$source_manifest_sha256" ]]; then
  exit 128
fi
(cd "$root" && sha256sum -c AWS_SOURCE_MANIFEST.sha256 >/dev/null)

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib_per_lane=%s\nwall_seconds=%s\nsource_manifest_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$memory_cap_kib" "$wall_seconds" "$source_manifest_sha256" \
  > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"

compiler_lane="${tag}_compiler"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$compiler_lane" timeout 1800 \
  python3 "$package/compile_certificate_circuit_v43g5.py" "$job/compiled" --phase compile
grep -Fx 'V43G5_SUPPORT_ROWS=11' "$job/run/${compiler_lane}.stdout" >/dev/null
grep -Fx 'V43G5_ACTIVE_VARIABLES=30' "$job/run/${compiler_lane}.stdout" >/dev/null
grep -Fx 'V43G5_SUBSETS=2048' "$job/run/${compiler_lane}.stdout" >/dev/null
grep -Fx 'PASS-A1-GENERIC-CIRCUIT-V43G5-COMPILER' "$job/run/${compiler_lane}.stdout" >/dev/null

qfield_lane="${tag}_qfield_subsets"
pole_lane="${tag}_full_pole"
(
  ulimit -v "$memory_cap_kib"
  bash ops/aws_exact_lane.sh "$root" "$job/run" "$qfield_lane" timeout "$wall_seconds" \
    Singular -q "$job/compiled/qfield_all_subsets.sing"
) &
qfield_pid=$!
(
  ulimit -v "$memory_cap_kib"
  bash ops/aws_exact_lane.sh "$root" "$job/run" "$pole_lane" timeout "$wall_seconds" \
    Singular -q "$job/compiled/full_support_pole.sing"
) &
pole_pid=$!
printf 'qfield_pid=%s\npole_pid=%s\n' "$qfield_pid" "$pole_pid" > "$job/worker_pids.txt"
qfield_rc=0
pole_rc=0
wait "$qfield_pid" || qfield_rc=$?
wait "$pole_pid" || pole_rc=$?
printf 'qfield_rc=%s\npole_rc=%s\n' "$qfield_rc" "$pole_rc" > "$job/worker_rcs.txt"
if [[ "$qfield_rc" -ne 0 || "$pole_rc" -ne 0 ]]; then
  exit 90
fi
qfield_stdout="$job/run/${qfield_lane}.stdout"
pole_stdout="$job/run/${pole_lane}.stdout"
grep -Fx 'V43G5_QT_SUBSETS=2048' "$qfield_stdout" >/dev/null
grep -Fx 'PASS_A1_GENERIC_CIRCUIT_QT_V43G5' "$qfield_stdout" >/dev/null
grep -Fx 'PASS_A1_GENERIC_FULL_POLE_V43G5' "$pole_stdout" >/dev/null

analyze_lane="${tag}_analyze"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$analyze_lane" timeout 1800 \
  python3 "$package/compile_certificate_circuit_v43g5.py" "$job/compiled" \
    --phase analyze --qfield-stdout "$qfield_stdout" --pole-stdout "$pole_stdout"
grep -Fx 'PASS-A1-GENERIC-CIRCUIT-V43G5-ANALYSIS' "$job/run/${analyze_lane}.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
cp "$job/compiled/compiler_result.json" "$job/COMPILER_RESULT.json"
cp "$job/compiled/analysis.json" "$job/ANALYSIS.json"
printf 'end_utc=%s\noutcome=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  'exact-full-subset-table-and-full-support-pole-scan-replayed' \
  > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
