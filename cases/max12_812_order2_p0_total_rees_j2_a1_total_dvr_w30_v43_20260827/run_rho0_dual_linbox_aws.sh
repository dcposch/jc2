#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 7 ]]; then
  exit 125
fi
root=$1
job=$2
tag=$3
memory_cap_kib=$4
total_wall_seconds=$5
source_manifest_sha256=$6
source_label=$7
package=cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_rho0dual_exact_* ]]; then
  exit 126
fi
if [[ "$memory_cap_kib" -ne 201326592 || "$total_wall_seconds" -ne 21600 ]]; then
  exit 127
fi
for command in python3 g++ linbox-config sha256sum; do
  command -v "$command" >/dev/null || exit 128
done

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmemory_cap_kib=%s\ntotal_wall_seconds=%s\nsource_manifest_sha256=%s\nsource_label=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$memory_cap_kib" \
  "$total_wall_seconds" "$source_manifest_sha256" "$source_label" \
  > "$job/launch_registration.txt"
dpkg-query -W -f='${Package}=${Version}\n' liblinbox-dev liblinbox-1.7.0-0t64 \
  fflas-ffpack libgivaro-dev libntl-dev libflint-dev libiml-dev g++ \
  > "$job/toolchain_versions.txt"
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
  python3 "$package/compile_rho0_dual_linbox_v43.py" "$job/compiled"
grep -Fx 'PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER' \
  "$job/run/${compiler_lane}.stdout" >/dev/null

linbox_flags=()
while IFS= read -r line; do
  read -r -a line_flags <<< "$line"
  linbox_flags+=("${line_flags[@]}")
done < <(linbox-config --cflags --libs)
build_lane="${tag}_build"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$build_lane" timeout "$(remaining)" \
  g++ -O3 -DNDEBUG -fopenmp "$package/rho0_dual_linbox_v43.cpp" \
  -o "$job/rho0_dual_linbox_v43" "${linbox_flags[@]}"

matrix=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["matrix_path"])' \
  "$job/compiled/compiler_result.json")
rhs=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["rhs_path"])' \
  "$job/compiled/compiler_result.json")
solver_lane="${tag}_solver"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$solver_lane" timeout "$(remaining)" \
  "$job/rho0_dual_linbox_v43" "$matrix" "$rhs" "$job/rho0_dual_exact.solution"

validator_lane="${tag}_validator"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$validator_lane" timeout "$(remaining)" \
  python3 "$package/validate_rho0_dual_linbox_v43.py" \
  --compiler-result "$job/compiled/compiler_result.json" \
  --solution "$job/rho0_dual_exact.solution" --output "$job/validated"
grep -Fx 'PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-EXACT-REPLAY' \
  "$job/run/${validator_lane}.stdout" >/dev/null
cp "$job/validated/result.json" "$job/RESULT.json"
if grep -ERq 'Traceback|FAIL_|Killed|out of memory|error occurred' "$job/run"; then
  exit 91
fi
printf 'end_utc=%s\nelapsed_seconds=%s\noutcome=exact-Q-nonmembership\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$((SECONDS - started))" \
  > "$job/finish_registration.txt"
(
  cd "$job"
  find . -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
    > EVIDENCE.sha256
)
