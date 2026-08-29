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
source_manifest_sha256=$8
source_label=$9
package=cases/max12_812_order2_p0_total_rees_j2_a1_rho0_w35_n7_extension_20260827
case "$mode:$prime" in
  modp:65519|exact:65521) ;;
  *) exit 126 ;;
esac
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_rho0_w35_n7_extension_${mode}_* ]]; then
  exit 127
fi
if [[ "$memory_cap_kib" -ne 201326592 || "$total_wall_seconds" -ne 21600 ]]; then
  exit 128
fi
for command in python3 g++ linbox-config sha256sum; do
  command -v "$command" >/dev/null || exit 129
done

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nmode=%s\nprime=%s\nmemory_cap_kib=%s\ntotal_wall_seconds=%s\nsource_manifest_sha256=%s\nsource_label=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$mode" "$prime" \
  "$memory_cap_kib" "$total_wall_seconds" "$source_manifest_sha256" "$source_label" \
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
  python3 "$package/compile_w35_n7_seed_extension.py" "$job/compiled" --phase compile
grep -Fx 'PASS-A1-RHO0-W35-N7-SEED-EXTENSION-COMPILER' \
  "$job/run/${compiler_lane}.stdout" >/dev/null
linbox_flags=()
while IFS= read -r line; do
  read -r -a line_flags <<< "$line"
  linbox_flags+=("${line_flags[@]}")
done < <(linbox-config --cflags --libs)
build_lane="${tag}_build"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$build_lane" timeout "$(remaining)" \
  g++ -O3 -DNDEBUG -fopenmp "$package/w35_n7_seed_extension_${mode}.cpp" \
  -o "$job/w35_n7_seed_extension_${mode}" "${linbox_flags[@]}"
matrix=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["matrix_path"])' \
  "$job/compiled/compiler_result.json")
rhs=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["rhs_path"])' \
  "$job/compiled/compiler_result.json")
solution="$job/w35_n7_seed_extension_${mode}.solution"
solver_lane="${tag}_solver"
if [[ "$mode" == modp ]]; then
  bash ops/aws_exact_lane.sh "$root" "$job/run" "$solver_lane" timeout "$(remaining)" \
    "$job/w35_n7_seed_extension_${mode}" "$matrix" "$rhs" "$prime" "$solution"
else
  bash ops/aws_exact_lane.sh "$root" "$job/run" "$solver_lane" timeout "$(remaining)" \
    "$job/w35_n7_seed_extension_${mode}" "$matrix" "$rhs" "$solution"
fi
validator_lane="${tag}_validator"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$validator_lane" timeout "$(remaining)" \
  python3 "$package/validate_w35_n7_seed_extension_${mode}.py" \
  --compiler-result "$job/compiled/compiler_result.json" --solution "$solution" \
  --output "$job/validated"
if [[ "$mode" == modp ]]; then
  token=PASS-A1-RHO0-W35-N7-SEED-EXTENSION-MODP-FULL-REPLAY
  outcome=finite-field-extension-screen-only
else
  token=PASS-A1-RHO0-W35-N7-SEED-EXTENSION-EXACT-FULL-REPLAY
  outcome=exact-Q-nonmembership
fi
grep -Fx "$token" "$job/run/${validator_lane}.stdout" >/dev/null
cp "$job/validated/result.json" "$job/RESULT.json"
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
