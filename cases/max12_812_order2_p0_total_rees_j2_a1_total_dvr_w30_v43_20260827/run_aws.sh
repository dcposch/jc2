#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 9 ]]; then
  exit 125
fi

root=$1
job=$2
tag=$3
mode=$4
prime=$5
memory_cap_kib=$6
total_wall_seconds=$7
archive_sha256=$8
python_executable=$9
package=cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827
v42=cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/replay_a1_cascade_closure_v42.py

case "$mode:$prime" in
  exact:65521|modp:65519) ;;
  *) exit 126 ;;
esac
if [[ "$memory_cap_kib" -ne 201326592 || "$total_wall_seconds" -ne 21600 ]]; then
  exit 127
fi

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmode=%s\nprime=%s\nmemory_cap_kib=%s\ntotal_wall_seconds=%s\nsource_archive_sha256=%s\npython=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$mode" "$prime" \
  "$memory_cap_kib" "$total_wall_seconds" "$archive_sha256" "$python_executable" \
  > "$job/launch_registration.txt"

cd "$root"
sha256sum -c "$package/FREEZE.sha256" > "$job/freeze_check.stdout"
if [[ "$mode" == exact ]]; then
  "$python_executable" -c 'import flint; assert flint.__version__ == "0.9.0"'
fi
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$memory_cap_kib"
started=$SECONDS

remaining() {
  local elapsed=$((SECONDS - started))
  local left=$((total_wall_seconds - elapsed))
  if (( left <= 0 )); then
    exit 124
  fi
  printf '%s\n' "$left"
}

cascade_lane="${tag}_v42_positive_and_corrupted_row_control"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$cascade_lane" \
  timeout "$(remaining)" python3 "$v42"

compiler_lane="${tag}_compiler"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$compiler_lane" \
  timeout "$(remaining)" "$python_executable" "$package/compile_total_dvr_w30_v43.py" \
  "$job/compiled" --mode "$mode" --selector-prime "$prime" --phase solve

rho0_outcome=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["rho0"]["outcome"])' \
  "$job/compiled/result.json")
validator_args=(
  --compiler-result "$job/compiled/result.json"
  --compiler-stdout "$job/run/${compiler_lane}.stdout"
  --compiler-stderr "$job/run/${compiler_lane}.stderr"
  --cascade-stdout "$job/run/${cascade_lane}.stdout"
  --cascade-stderr "$job/run/${cascade_lane}.stderr"
  --mode "$mode" --prime "$prime" --output "$job/RESULT.json"
)

if [[ "$rho0_outcome" == member ]]; then
  singular_script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["singular_script"])' \
    "$job/compiled/result.json")
  singular_lane="${tag}_singular_dvr"
  bash ops/aws_exact_lane.sh "$root" "$job/run" "$singular_lane" \
    timeout "$(remaining)" Singular -q "$singular_script"
  validator_args+=(
    --singular-stdout "$job/run/${singular_lane}.stdout"
    --singular-stderr "$job/run/${singular_lane}.stderr"
  )
elif [[ "$rho0_outcome" != nonmember ]]; then
  exit 92
fi

validator_lane="${tag}_validator"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$validator_lane" \
  timeout "$(remaining)" python3 "$package/validate_total_dvr_w30_v43.py" "${validator_args[@]}"
grep -Fx 'PASS-A1-TOTAL-DVR-W30-V43-VALIDATOR' \
  "$job/run/${validator_lane}.stdout" >/dev/null
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
printf 'end_utc=%s\nelapsed_seconds=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  "$((SECONDS - started))" > "$job/finish_registration.txt"
find "$job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum \
  > "$job/EVIDENCE.sha256"
