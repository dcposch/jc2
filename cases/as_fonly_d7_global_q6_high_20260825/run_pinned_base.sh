#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${PIN_STRUCTURAL:?}"
: "${RESULT_DIR:?}"
mkdir -p "$RESULT_DIR"
SOURCE="$JC2_ROOT/cases/as_fonly_d7_global_q6_high_20260825"

/usr/bin/time -v env \
  JC2_ROOT="$JC2_ROOT" \
  PIN_STRUCTURAL="$PIN_STRUCTURAL" \
  SOLVER_TIMEOUT_MS=1 \
  SMT2_OUTPUT="$RESULT_DIR/formula.smt2" \
  OUTPUT_JSON="$RESULT_DIR/emitter.json" \
  python3 "$SOURCE/solve_global_q6_high.py" \
  >"$RESULT_DIR/emitter.stdout" 2>"$RESULT_DIR/emitter.stderr"

set +e
/usr/bin/time -v boolector -m -d "$RESULT_DIR/formula.smt2" \
  >"$RESULT_DIR/boolector.stdout" 2>"$RESULT_DIR/boolector.stderr"
rc=$?
set -e
printf '%s\n' "$rc" >"$RESULT_DIR/boolector.rc"
if [[ "$rc" == 10 ]]; then
  /usr/bin/time -v env \
    JC2_ROOT="$JC2_ROOT" \
    MODEL_OUTPUT="$RESULT_DIR/boolector.stdout" \
    OUTPUT_JSON="$RESULT_DIR/direct_replay.json" \
    python3 "$SOURCE/replay_global_q6_high.py" \
    >"$RESULT_DIR/direct_replay.stdout" 2>"$RESULT_DIR/direct_replay.stderr"
  printf '%s\n' SAT-DIRECT-REPLAY-PASS >"$RESULT_DIR/VERDICT.txt"
elif [[ "$rc" == 20 ]]; then
  printf '%s\n' UNSAT-SOLVER-EVIDENCE-ONLY >"$RESULT_DIR/VERDICT.txt"
else
  printf '%s\n' "NONTERMINAL-SOLVER-RC-$rc" >"$RESULT_DIR/VERDICT.txt"
fi
(
  cd "$RESULT_DIR"
  find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 -print0 \
    | sort -z | xargs -0 sha256sum >OUTPUTS.sha256
)
cat "$RESULT_DIR/VERDICT.txt"
