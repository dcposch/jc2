#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 9 ]]; then
  exit 125
fi
root=$1
job=$2
tag=$3
order=$4
memory_cap_kib=$5
total_wall_seconds=$6
archive_sha256=$7
source_label=$8
method=$9
package=cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827
case "$order" in dp|lp) ;; *) exit 126 ;; esac
case "$method" in separate|tracked) ;; *) exit 126 ;; esac
if [[ "$memory_cap_kib" -ne 201326592 || "$total_wall_seconds" -ne 21600 ]]; then exit 127; fi

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\norder=%s\nmethod=%s\nmemory_cap_kib=%s\ntotal_wall_seconds=%s\nsource_archive_sha256=%s\nsource_label=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$order" \
  "$method" "$memory_cap_kib" "$total_wall_seconds" "$archive_sha256" "$source_label" \
  > "$job/launch_registration.txt"
cd "$root"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$memory_cap_kib"
started=$SECONDS
remaining() {
  local left=$((total_wall_seconds - (SECONDS - started)))
  if (( left <= 0 )); then exit 124; fi
  printf '%s\n' "$left"
}

compiler_lane="${tag}_compiler"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$compiler_lane" timeout "$(remaining)" \
  python3 "$package/compile_cascade_dehom_v43.py" "$job/compiled" --order "$order" --method "$method"
script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["singular_script"])' \
  "$job/compiled/compiler_result.json")
singular_lane="${tag}_singular"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$singular_lane" timeout "$(remaining)" \
  Singular -q "$script"
grep -Fx 'V43_DEHOM_OUTCOME=unit' "$job/run/${singular_lane}.stdout" >/dev/null
homogenize_lane="${tag}_homogenize"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$homogenize_lane" timeout "$(remaining)" \
  python3 "$package/homogenize_cascade_lift_v43.py" \
  --compiler-result "$job/compiled/compiler_result.json" \
  --singular-stdout "$job/run/${singular_lane}.stdout" \
  --singular-stderr "$job/run/${singular_lane}.stderr" \
  --order "$order" --output "$job/homogenized"
grep -Fx 'PASS-A1-TOTAL-DVR-W30-V43-DEHOM-HOMOGENIZED' \
  "$job/run/${homogenize_lane}.stdout" >/dev/null
cp "$job/homogenized/result.json" "$job/RESULT.json"
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then exit 91; fi
printf 'end_utc=%s\nelapsed_seconds=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$((SECONDS - started))" > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
