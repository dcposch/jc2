#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${OUTPUT_JSON:?}"
: "${PARENT_REPLAY_JSON:?}"
: "${ANF_OUTPUT:?}"
: "${SMT2_OUTPUT:?}"
date -u +%Y-%m-%dT%H:%M:%SZ > start_utc
set +e
/usr/bin/time -v timeout 7200 env JC2_ROOT="${JC2_ROOT}" \
  OUTPUT_JSON="${OUTPUT_JSON}" PARENT_REPLAY_JSON="${PARENT_REPLAY_JSON}" \
  ANF_OUTPUT="${ANF_OUTPUT}" SMT2_OUTPUT="${SMT2_OUTPUT}" \
  python3 "${JC2_ROOT}/cases/as_b9_max12_full_fibre_quadratic_3p11_20260825/compile_quadratic_3p11.py" \
  > compiler.stdout 2> compiler.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > compiler.rc
date -u +%Y-%m-%dT%H:%M:%SZ > end_utc
sha256sum start_utc end_utc compiler.rc compiler.stdout compiler.stderr \
  "${OUTPUT_JSON}" "${PARENT_REPLAY_JSON}" "${ANF_OUTPUT}" \
  "${SMT2_OUTPUT}" > OUTPUT.sha256 2>/dev/null || true
exit "${rc}"
