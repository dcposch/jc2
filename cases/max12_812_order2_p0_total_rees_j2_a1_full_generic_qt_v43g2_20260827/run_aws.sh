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
package=cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g2_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g2_*_exact_decision_* ]]; then
  exit 126
fi
if [[ "$memory_cap_kib" -ne 671088640 || "$wall_seconds" -ne 21600 ]]; then
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
started=$SECONDS
remaining() {
  local left=$((wall_seconds - (SECONDS - started)))
  if (( left <= 0 )); then exit 124; fi
  printf '%s\n' "$left"
}

compiler_lane="${tag}_compiler"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$compiler_lane" timeout "$(remaining)" \
  python3 "$package/compile_generic_only_qt_v43g2.py" "$job/compiled"
script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["singular_script"])' \
  "$job/compiled/compiler_result.json")
singular_lane="${tag}_singular"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$singular_lane" timeout "$(remaining)" \
  Singular -q "$script"
stdout="$job/run/${singular_lane}.stdout"
if grep -q 'SPECIAL_FIBRE_UNIT' "$stdout"; then
  exit 89
fi
if grep -Fx 'V43G2_GENERIC_OUTCOME=nonunit' "$stdout" >/dev/null; then
  outcome=exact-full-generic-nonunit
elif grep -Fx 'V43G2_GENERIC_OUTCOME=unit' "$stdout" >/dev/null; then
  grep -Fx 'V43G2_UNIT_STATUS=requires-tracked-lift' "$stdout" >/dev/null
  outcome=exact-full-generic-unit-requires-tracked-lift
else
  exit 90
fi
grep -Fx 'PASS_A1_GENERIC_ONLY_QT_V43G2' "$stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
cp "$job/compiled/compiler_result.json" "$job/COMPILER_RESULT.json"
printf 'end_utc=%s\nelapsed_seconds=%s\noutcome=%s\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$((SECONDS - started))" "$outcome" \
  > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
