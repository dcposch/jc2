#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || $# -ne 8 ]]; then
  exit 125
fi
root=$1
compiled_job=$2
job=$3
tag=$4
memory_cap_kib=$5
total_wall_seconds=$6
source_manifest_sha256=$7
source_label=$8
package=cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827
if [[ "$tag" != max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_rho0dual_exact_resume_* ]]; then
  exit 126
fi
if [[ "$memory_cap_kib" -ne 201326592 || "$total_wall_seconds" -ne 21600 ]]; then
  exit 127
fi
for command in python3 g++ linbox-config sha256sum; do
  command -v "$command" >/dev/null || exit 128
done
compiler_result="$compiled_job/compiled/compiler_result.json"
test -f "$compiler_result" || exit 129

mkdir -p "$job/run"
printf 'tag=%s\nhost=%s\nstart_utc=%s\nresumed_compiled_job=%s\nmemory_cap_kib=%s\ntotal_wall_seconds=%s\nsource_manifest_sha256=%s\nsource_label=%s\n' \
  "$tag" "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$compiled_job" \
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

python3 - "$compiler_result" <<'PY'
from hashlib import sha256
import json, pathlib, sys
p=pathlib.Path(sys.argv[1]); d=json.loads(p.read_text())
assert d["status"] == "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER"
for key in ("matrix", "rhs", "coordinate"):
    q=pathlib.Path(d[f"{key}_path"])
    assert sha256(q.read_bytes()).hexdigest() == d[f"{key}_sha256"]
PY
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
  "$compiler_result")
rhs=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["rhs_path"])' \
  "$compiler_result")
solver_lane="${tag}_solver"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$solver_lane" timeout "$(remaining)" \
  "$job/rho0_dual_linbox_v43" "$matrix" "$rhs" "$job/rho0_dual_exact.solution"
validator_lane="${tag}_validator"
bash ops/aws_exact_lane.sh "$root" "$job/run" "$validator_lane" timeout "$(remaining)" \
  python3 "$package/validate_rho0_dual_linbox_v43.py" \
  --compiler-result "$compiler_result" --solution "$job/rho0_dual_exact.solution" \
  --output "$job/validated"
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
