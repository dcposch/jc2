#!/usr/bin/env bash
set -euo pipefail
: "${JOB_ROOT:?}"
: "${SOURCE_ROOT:?}"
: "${OLD_JOB_ROOT:?}"
: "${BASE_NAME:?}"
: "${PYTHON:=python3}"

out="${JOB_ROOT}/${BASE_NAME}"
mkdir -p "${out}"
date -u +%Y-%m-%dT%H:%M:%SZ > "${out}/start_utc"
set +e
/usr/bin/time -v timeout 3600 env \
  JC2_ROOT="${SOURCE_ROOT}" \
  MODEL_OUTPUT="${OLD_JOB_ROOT}/inputs/model_${BASE_NAME#base_}.stdout" \
  PARENT_OUTPUT_JSON="${OLD_JOB_ROOT}/${BASE_NAME}/q3_parent.json" \
  PREVIOUS_Z9_RESULT_JSON="${OLD_JOB_ROOT}/${BASE_NAME}/result.json" \
  OUTPUT_JSON="${out}/result.json" \
  "${PYTHON}" \
  "${SOURCE_ROOT}/cases/as_fonly_d7_q3_full_output_cone_z27_20260825/solve_full_output_cone_z27.py" \
  > "${out}/solver.stdout" 2> "${out}/solver.stderr"
rc=$?
set -e
printf '%s\n' "${rc}" > "${out}/solver.rc"
date -u +%Y-%m-%dT%H:%M:%SZ > "${out}/end_utc"
find "${out}" -maxdepth 1 -type f ! -name OUTPUT.sha256 -print0 \
  | sort -z | xargs -0 sha256sum > "${out}/OUTPUT.sha256"
exit "${rc}"
