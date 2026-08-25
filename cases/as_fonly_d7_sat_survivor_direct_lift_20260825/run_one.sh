#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${SURVIVOR_JSON:?}"
: "${LAYER_COUNT:?}"
: "${RESULT_DIR:?}"
mkdir -p "$RESULT_DIR"

SOURCE="$JC2_ROOT/cases/as_fonly_d7_sat_survivor_direct_lift_20260825"
SMT="$RESULT_DIR/formula.smt2"

/usr/bin/time -v env \
  JC2_ROOT="$JC2_ROOT" \
  SURVIVOR_JSON="$SURVIVOR_JSON" \
  LAYER_COUNT="$LAYER_COUNT" \
  SMT2_OUTPUT="$SMT" \
  OUTPUT_JSON="$RESULT_DIR/emitter.json" \
  SOLVER_TIMEOUT_MS=1 \
  python3 "$SOURCE/emit_direct_lift.py" \
  >"$RESULT_DIR/emitter.stdout" 2>"$RESULT_DIR/emitter.stderr"

set +e
/usr/bin/time -v boolector -m -d "$SMT" \
  >"$RESULT_DIR/boolector.stdout" 2>"$RESULT_DIR/boolector.stderr"
solver_rc=$?
set -e
printf '%s\n' "$solver_rc" >"$RESULT_DIR/boolector.rc"

if [[ "$solver_rc" == 10 ]]; then
  /usr/bin/time -v env \
    JC2_ROOT="$JC2_ROOT" \
    SURVIVOR_JSON="$SURVIVOR_JSON" \
    LAYER_COUNT="$LAYER_COUNT" \
    MODEL_OUTPUT="$RESULT_DIR/boolector.stdout" \
    OUTPUT_JSON="$RESULT_DIR/direct_replay.json" \
    python3 "$SOURCE/replay_direct_lift.py" \
    >"$RESULT_DIR/direct_replay.stdout" 2>"$RESULT_DIR/direct_replay.stderr"
  printf '%s\n' SAT-DIRECT-REPLAY-PASS >"$RESULT_DIR/VERDICT.txt"
elif [[ "$solver_rc" == 20 ]]; then
  printf '%s\n' UNSAT-SOLVER-EVIDENCE-ONLY >"$RESULT_DIR/VERDICT.txt"
else
  printf '%s\n' "NONTERMINAL-SOLVER-RC-$solver_rc" >"$RESULT_DIR/VERDICT.txt"
fi

(
  cd "$RESULT_DIR"
  find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 -print0 \
    | sort -z | xargs -0 sha256sum >OUTPUTS.sha256
)
cat "$RESULT_DIR/VERDICT.txt"
