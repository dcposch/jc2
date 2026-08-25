#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?set JC2_ROOT}"
: "${MODEL_OUTPUT:?set MODEL_OUTPUT}"
: "${RESULT_DIR:?set RESULT_DIR}"

mkdir -p "$RESULT_DIR"
sha256sum "$MODEL_OUTPUT" > "$RESULT_DIR/MODEL.sha256"
sha256sum "$JC2_ROOT/cases/as_fonly_d7_global_q6_low_cartier_20260825/audit_low_cartier.py" \
  > "$RESULT_DIR/SOURCE.sha256"
date -u +%Y-%m-%dT%H:%M:%SZ > "$RESULT_DIR/start_utc"
hostname > "$RESULT_DIR/hostname"

set +e
/usr/bin/time -v env \
  JC2_ROOT="$JC2_ROOT" \
  MODEL_OUTPUT="$MODEL_OUTPUT" \
  RESULT_DIR="$RESULT_DIR" \
  OUTPUT_JSON="$RESULT_DIR/result.json" \
  python3 "$JC2_ROOT/cases/as_fonly_d7_global_q6_low_cartier_20260825/audit_low_cartier.py" \
  > "$RESULT_DIR/replay.stdout" 2> "$RESULT_DIR/replay.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$RESULT_DIR/replay.rc"
date -u +%Y-%m-%dT%H:%M:%SZ > "$RESULT_DIR/end_utc"
sha256sum "$RESULT_DIR"/result.json "$RESULT_DIR"/replay.stdout \
  "$RESULT_DIR"/replay.stderr > "$RESULT_DIR/OUTPUT.sha256" 2>/dev/null || true
test "$rc" -eq 0

