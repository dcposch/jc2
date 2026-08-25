#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}" "${INPUT_ANF:?}" "${OUTPUT_JSON:?}" \
  "${REDUCED_ANF_OUTPUT:?}" "${GEOMETRY_SING:?}" "${FINITE_SING:?}"
case_dir="${JC2_ROOT}/cases/as_b8_max12_affine_kuranishi_aws_20260825"
test "$(sha256sum "${case_dir}/compile_affine_kuranishi.py" | cut -d' ' -f1)" = \
  "a3f1b0356198f2acc9a967e2f99967f78ff74828318ef4ff12630cc60c594861"
test "$(sha256sum "${INPUT_ANF}" | cut -d' ' -f1)" = \
  "9121d7cb4ee5aa5f38f31312077c084dc98fbc1b4175c73cef4a95dadaad45a4"
hostname > reduce.host.txt
uname -a > reduce.uname.txt
python3 --version > reduce.python-version.txt 2>&1
sha256sum "${case_dir}/QUADRATIC_SOLVE_PREREGISTRATION.md" \
  "${case_dir}/reduce_quadratic.py" "${case_dir}/run_reduce_aws.sh" \
  "${case_dir}/compile_affine_kuranishi.py" "${INPUT_ANF}" > reduce.INPUT.sha256
date -u +%Y-%m-%dT%H:%M:%SZ > reduce.start.utc
set +e
/usr/bin/time -v timeout 7200 env JC2_ROOT="${JC2_ROOT}" INPUT_ANF="${INPUT_ANF}" \
  OUTPUT_JSON="${OUTPUT_JSON}" REDUCED_ANF_OUTPUT="${REDUCED_ANF_OUTPUT}" \
  GEOMETRY_SING="${GEOMETRY_SING}" FINITE_SING="${FINITE_SING}" \
  REPLAY_RESULT="$(dirname "${OUTPUT_JSON}")/replayed_parent_result.json" \
  REPLAY_ANF="$(dirname "${OUTPUT_JSON}")/replayed_parent_anf.json" \
  python3 "${case_dir}/reduce_quadratic.py" > reduce.stdout 2> reduce.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > reduce.rc
date -u +%Y-%m-%dT%H:%M:%SZ > reduce.end.utc
sha256sum reduce.host.txt reduce.uname.txt reduce.python-version.txt \
  reduce.INPUT.sha256 reduce.start.utc reduce.end.utc reduce.rc \
  reduce.stdout reduce.stderr "${OUTPUT_JSON}" "${REDUCED_ANF_OUTPUT}" \
  "${GEOMETRY_SING}" "${FINITE_SING}" > reduce.OUTPUT.sha256 2>/dev/null || true
exit "${rc}"
