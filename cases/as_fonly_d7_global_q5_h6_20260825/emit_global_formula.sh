#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${RESULT_DIR:?}"
SOURCE="$JC2_ROOT/cases/as_fonly_d7_global_q5_h6_20260825"
mkdir -p "$RESULT_DIR"

date -u +%Y-%m-%dT%H:%M:%SZ >"$RESULT_DIR/start_utc"
hostname >"$RESULT_DIR/hostname"
/usr/bin/time -v env \
  JC2_ROOT="$JC2_ROOT" \
  SOLVER_TIMEOUT_MS=1 \
  SMT2_OUTPUT="$RESULT_DIR/formula.smt2" \
  OUTPUT_JSON="$RESULT_DIR/emitter.json" \
  python3 "$SOURCE/solve_global_q5_h6.py" \
  >"$RESULT_DIR/emitter.stdout" 2>"$RESULT_DIR/emitter.stderr"
date -u +%Y-%m-%dT%H:%M:%SZ >"$RESULT_DIR/end_utc"
sha256sum "$RESULT_DIR"/formula.smt2 "$RESULT_DIR"/emitter.json \
  "$RESULT_DIR"/emitter.stdout "$RESULT_DIR"/emitter.stderr \
  >"$RESULT_DIR/OUTPUT.sha256"

