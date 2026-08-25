#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${OUTPUT_JSON:?}"
: "${PARENT_REPLAY_JSON:?}"
date -u +%Y-%m-%dT%H:%M:%SZ > start_utc
set +e
/usr/bin/time -v timeout 3600 env JC2_ROOT="${JC2_ROOT}" \
  OUTPUT_JSON="${OUTPUT_JSON}" PARENT_REPLAY_JSON="${PARENT_REPLAY_JSON}" \
  python3 "${JC2_ROOT}/cases/as_b9_9_12_full_fibre_linear_window_20260825/solve_linear_window_9_12.py" \
  > solver.stdout 2> solver.stderr
rc=$?
set -e
printf '%s\n' "${rc}" > solver.rc
date -u +%Y-%m-%dT%H:%M:%SZ > end_utc
sha256sum start_utc end_utc solver.rc solver.stdout solver.stderr \
  "${OUTPUT_JSON}" "${PARENT_REPLAY_JSON}" > OUTPUT.sha256 2>/dev/null || true
exit "${rc}"
