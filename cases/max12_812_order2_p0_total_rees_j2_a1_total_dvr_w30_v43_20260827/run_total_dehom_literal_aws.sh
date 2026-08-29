#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 10 ]]; then
  exit 125
fi
root=$1
job=$2
tag=$3
mode=$4
phase=$5
prime=$6
memory_cap_kib=$7
total_wall_seconds=$8
source_manifest_sha256=$9
source_label=${10}
package=cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827
case "$mode:$phase:$prime" in
  exact:lift:65521|modp:eliminate:65519) ;;
  *) exit 126 ;;
esac
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_totaldehom_${mode}_${phase}_literal_* ]]; then
  exit 127
fi
if [[ "$memory_cap_kib" -ne 201326592 || "$total_wall_seconds" -ne 21600 ]]; then
  exit 128
fi

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmode=%s\nphase=%s\nprime=%s\nmemory_cap_kib=%s\ntotal_wall_seconds=%s\nsource_manifest_sha256=%s\nsource_label=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$mode" "$phase" \
  "$prime" "$memory_cap_kib" "$total_wall_seconds" "$source_manifest_sha256" \
  "$source_label" > "$job/launch_registration.txt"
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
  python3 "$package/compile_total_dehom_literal_v43.py" "$job/compiled" \
  --mode "$mode" --prime "$prime" --phase "$phase"
grep -Fx 'PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-LITERAL-COMPILER' \
  "$job/run/${compiler_lane}.stdout" >/dev/null
script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["singular_script"])' \
  "$job/compiled/compiler_result.json")
singular_lane="${tag}_singular"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$singular_lane" timeout "$(remaining)" \
  Singular -q "$script"
stdout="$job/run/${singular_lane}.stdout"
grep -Fx 'V43_TOTAL_DEHOM_SPECIAL_UNIT=1' "$stdout" >/dev/null
if grep -Fx 'V43_TOTAL_DEHOM_OUTCOME=unit-eliminant' "$stdout" >/dev/null; then
  outcome=unit-eliminant
  grep -Fx 'PASS_A1_TOTAL_DVR_W30_V43_TOTAL_DEHOM' "$stdout" >/dev/null
  if [[ "$phase" == lift ]]; then
    grep -Fx 'V43_TOTAL_DEHOM_LIFT_REPLAY=1' "$stdout" >/dev/null
  fi
elif grep -Fx 'V43_TOTAL_DEHOM_OUTCOME=no-unit-eliminant' "$stdout" >/dev/null; then
  outcome=no-unit-eliminant
else
  exit 90
fi
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
printf 'end_utc=%s\nelapsed_seconds=%s\noutcome=%s\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$((SECONDS - started))" "$outcome" \
  > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
