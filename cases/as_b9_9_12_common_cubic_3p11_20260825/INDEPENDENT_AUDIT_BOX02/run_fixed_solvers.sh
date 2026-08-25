#!/usr/bin/env bash
set -euo pipefail

: "${AUDIT_DIR:?}"
cd "${AUDIT_DIR}"
sha256sum common_fixed.smt2 common_fixed.boolector.smt2 > solver_inputs.sha256

run_one() {
  local tag="$1"
  shift
  date -u +%Y-%m-%dT%H:%M:%SZ > "${tag}.start_utc"
  set +e
  /usr/bin/time -v timeout --signal=TERM --kill-after=60s 7200 "$@" \
    > "${tag}.stdout" 2> "${tag}.stderr"
  local rc=$?
  set -e
  printf '%s\n' "${rc}" > "${tag}.rc"
  date -u +%Y-%m-%dT%H:%M:%SZ > "${tag}.end_utc"
}

run_one boolector_fixed /usr/bin/boolector -m common_fixed.boolector.smt2 &
boolector_pid=$!
run_one z3_fixed /home/ubuntu/jobs/as_fullfibre_qfbv_20260825T0602Z_v2/z3_4_16/bin/z3 \
  -smt2 common_fixed.smt2 &
z3_pid=$!
wait "${boolector_pid}"
wait "${z3_pid}"
sha256sum boolector_fixed.* z3_fixed.* > solver_outputs.sha256
