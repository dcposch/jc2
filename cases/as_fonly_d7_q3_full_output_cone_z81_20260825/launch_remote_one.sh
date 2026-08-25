#!/usr/bin/env bash
set -euo pipefail
: "${JOB_ROOT:?}"
: "${SOURCE_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${Q3_PARENT_OUTPUT:?}"
: "${PREVIOUS_Z9_RESULT:?}"
: "${BASE_NAME:?}"
: "${PYTHON:=python3}"

out="${JOB_ROOT}/${BASE_NAME}"
mkdir -p "${out}"
date -u +%Y-%m-%dT%H:%M:%SZ > "${out}/start_utc"
set +e
/usr/bin/time -v timeout 7200 env \
  JC2_ROOT="${SOURCE_ROOT}" \
  MODEL_OUTPUT="${MODEL_OUTPUT}" \
  PARENT_OUTPUT_JSON="${Q3_PARENT_OUTPUT}" \
  PREVIOUS_Z9_RESULT_JSON="${PREVIOUS_Z9_RESULT}" \
  PARENT_REPLAY_JSON="${out}/parent_z27_replay.json" \
  OUTPUT_JSON="${out}/result.json" \
  ANF_OUTPUT="${out}/obstruction.anf.json" \
  SMT2_OUTPUT="${out}/obstruction.smt2" \
  "${PYTHON}" \
  "${SOURCE_ROOT}/cases/as_fonly_d7_q3_full_output_cone_z81_20260825/compile_full_output_z81.py" \
  > "${out}/compiler.stdout" 2> "${out}/compiler.stderr"
rc=$?
set -e
printf '%s\n' "${rc}" > "${out}/compiler.rc"
date -u +%Y-%m-%dT%H:%M:%SZ > "${out}/end_utc"
find "${out}" -maxdepth 1 -type f ! -name OUTPUT.sha256 -print0 \
  | sort -z | xargs -0 sha256sum > "${out}/OUTPUT.sha256"
exit "${rc}"
