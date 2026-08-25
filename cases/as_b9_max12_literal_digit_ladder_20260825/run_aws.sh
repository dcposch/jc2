#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${INPUT_JSON:?}"
: "${EXPECTED_INPUT_SHA256:?}"
: "${INPUT_MODULUS:?}"
: "${OUTPUT_JSON:?}"
date -u +%Y-%m-%dT%H:%M:%SZ > start_utc
set +e
/usr/bin/time -v timeout 1800 env \
  JC2_ROOT="${JC2_ROOT}" INPUT_JSON="${INPUT_JSON}" \
  EXPECTED_INPUT_SHA256="${EXPECTED_INPUT_SHA256}" \
  INPUT_MODULUS="${INPUT_MODULUS}" OUTPUT_JSON="${OUTPUT_JSON}" \
  python3 "${JC2_ROOT}/cases/as_b9_max12_literal_digit_ladder_20260825/advance_literal.py" \
  > solver.stdout 2> solver.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > solver.rc
date -u +%Y-%m-%dT%H:%M:%SZ > end_utc
sha256sum start_utc end_utc solver.rc solver.stdout solver.stderr \
  "${OUTPUT_JSON}" > OUTPUT.sha256 2>/dev/null || true
exit "${rc}"
