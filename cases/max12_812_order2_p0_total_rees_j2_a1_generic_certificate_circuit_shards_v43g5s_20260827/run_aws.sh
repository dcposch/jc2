#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 6 ]]; then exit 125; fi
root=$1
job=$2
tag=$3
memory_cap_kib=$4
wall_seconds=$5
source_manifest_sha256=$6
package=cases/max12_812_order2_p0_total_rees_j2_a1_generic_certificate_circuit_shards_v43g5s_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_generic_certificate_circuit_shards_v43g5s_* ]]; then exit 126; fi
if [[ "$memory_cap_kib" -ne 4194304 || "$wall_seconds" -ne 3600 ]]; then exit 127; fi
actual=$(sha256sum "$root/AWS_SOURCE_MANIFEST.sha256" | awk '{print $1}')
if [[ "$actual" != "$source_manifest_sha256" ]]; then exit 128; fi
(cd "$root" && sha256sum -c AWS_SOURCE_MANIFEST.sha256 >/dev/null)

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nshards=32\nmemory_cap_kib_per_shard=%s\nwall_seconds=%s\nsource_manifest_sha256=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$memory_cap_kib" \
  "$wall_seconds" "$source_manifest_sha256" > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"

python3 "$package/shard_qfield_v43g5s.py" "$job/compiled" --phase compile \
  > "$job/run/compiler.stdout" 2> "$job/run/compiler.stderr"
grep -Fx 'PASS-V43G5S-COMPILER' "$job/run/compiler.stdout" >/dev/null

pids=()
for shard in $(seq -w 0 31); do
  script=$(find "$job/compiled" -maxdepth 1 -name "qfield_shard_${shard}_*.sing" -print -quit)
  (
    ulimit -v "$memory_cap_kib"
    timeout "$wall_seconds" Singular -q "$script" \
      > "$job/run/shard_${shard}.stdout" 2> "$job/run/shard_${shard}.stderr"
  ) &
  pids+=("$!")
done
printf '%s\n' "${pids[@]}" > "$job/worker_pids.txt"
failed=0
for pid in "${pids[@]}"; do wait "$pid" || failed=1; done
if [[ "$failed" -ne 0 ]]; then exit 90; fi

python3 "$package/shard_qfield_v43g5s.py" "$job/compiled" --phase aggregate \
  --run-dir "$job/run" > "$job/run/aggregate.stdout" 2> "$job/run/aggregate.stderr"
grep -Fx 'PASS-V43G5S-EXACT-QT-SUBSET-CENSUS' "$job/run/aggregate.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
cp "$job/compiled/compiler_result.json" "$job/COMPILER_RESULT.json"
cp "$job/compiled/aggregate_result.json" "$job/AGGREGATE_RESULT.json"
printf 'end_utc=%s\noutcome=exact-32-shard-Q(t)-subset-census\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$job/finish_registration.txt"
(cd "$job" && find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256)
