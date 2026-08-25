#!/usr/bin/env bash
set -euo pipefail

: "${AUDIT_DIR:?}"
cd "${AUDIT_DIR}"
sha256sum independent_common_core.py > independent_source.sha256
date -u +%Y-%m-%dT%H:%M:%SZ > independent.start_utc
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s 7200 env \
  JC2_ROOT="${AUDIT_DIR}/source" \
  OUTPUT_JSON="${AUDIT_DIR}/independent_result.json" \
  LINEAR_REPLAY_JSON="${AUDIT_DIR}/independent_linear_replay.json" \
  PARENT_REPLAY_JSON="${AUDIT_DIR}/independent_nested_replay.json" \
  ANF_OUTPUT="${AUDIT_DIR}/independent.anf.json" \
  WITNESS_OUTPUT="${AUDIT_DIR}/independent_witness.json" \
  python3 "${AUDIT_DIR}/independent_common_core.py" \
  > independent.stdout 2> independent.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > independent.rc
date -u +%Y-%m-%dT%H:%M:%SZ > independent.end_utc
exit "${rc}"
