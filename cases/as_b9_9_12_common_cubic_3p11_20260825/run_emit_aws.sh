#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${OUTPUT_JSON:?}"
: "${PARENT_REPLAY_JSON:?}"
: "${GRANDPARENT_REPLAY_JSON:?}"
: "${PARENT_ANF_OUTPUT:?}"
: "${PARENT_SMT_OUTPUT:?}"
: "${SMT2_OUTPUT:?}"
: "${BOOLECTOR_SMT_OUTPUT:?}"
date -u +%Y-%m-%dT%H:%M:%SZ > start_utc
set +e
/usr/bin/time -v timeout 3600 env JC2_ROOT="${JC2_ROOT}" \
  OUTPUT_JSON="${OUTPUT_JSON}" PARENT_REPLAY_JSON="${PARENT_REPLAY_JSON}" \
  GRANDPARENT_REPLAY_JSON="${GRANDPARENT_REPLAY_JSON}" \
  PARENT_ANF_OUTPUT="${PARENT_ANF_OUTPUT}" PARENT_SMT_OUTPUT="${PARENT_SMT_OUTPUT}" \
  SMT2_OUTPUT="${SMT2_OUTPUT}" BOOLECTOR_SMT_OUTPUT="${BOOLECTOR_SMT_OUTPUT}" \
  python3 "${JC2_ROOT}/cases/as_b9_9_12_common_cubic_3p11_20260825/emit_common_cubic.py" \
  > emitter.stdout 2> emitter.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > emitter.rc
date -u +%Y-%m-%dT%H:%M:%SZ > end_utc
sha256sum start_utc end_utc emitter.rc emitter.stdout emitter.stderr \
  "${OUTPUT_JSON}" "${PARENT_REPLAY_JSON}" "${SMT2_OUTPUT}" \
  "${BOOLECTOR_SMT_OUTPUT}" > OUTPUT.sha256 2>/dev/null || true
exit "${rc}"
