#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${FORMULA:?}"
: "${FORMULA_SHA256:?}"
: "${RESULT_DIR:?}"
: "${BOOLECTOR_BIN:?}"
: "${REWRITE_LEVEL:?}"
: "${CAP_GIB:?}"
: "${TIMEOUT_SECONDS:?}"
SOURCE="$JC2_ROOT/cases/as_fonly_d7_global_q5_h6_20260825"
mkdir -p "$RESULT_DIR"

actual=$(sha256sum "$FORMULA" | awk '{print $1}')
test "$actual" = "$FORMULA_SHA256"
test -x "$BOOLECTOR_BIN"
date -u +%Y-%m-%dT%H:%M:%SZ >"$RESULT_DIR/start_utc"
hostname >"$RESULT_DIR/hostname"
printf '%s  %s\n' "$actual" "$FORMULA" >"$RESULT_DIR/INPUT.sha256"
"$BOOLECTOR_BIN" --version >"$RESULT_DIR/solver.version"
sha256sum "$BOOLECTOR_BIN" >"$RESULT_DIR/solver.binary.sha256"

set +e
(
  ulimit -v $((CAP_GIB * 1024 * 1024))
  exec /usr/bin/time -v timeout --signal=TERM --kill-after=60s \
    "$TIMEOUT_SECONDS" "$BOOLECTOR_BIN" -m -d \
    -rwl"$REWRITE_LEVEL" "$FORMULA"
) >"$RESULT_DIR/solver.stdout" 2>"$RESULT_DIR/solver.stderr"
rc=$?
set -e
printf '%s\n' "$rc" >"$RESULT_DIR/solver.rc"

if [[ "$rc" == 10 ]]; then
  /usr/bin/time -v env \
    JC2_ROOT="$JC2_ROOT" \
    MODEL_OUTPUT="$RESULT_DIR/solver.stdout" \
    OUTPUT_JSON="$RESULT_DIR/direct_replay.json" \
    python3 "$SOURCE/replay_global_q5_h6.py" \
    >"$RESULT_DIR/direct_replay.stdout" 2>"$RESULT_DIR/direct_replay.stderr"
  printf '%s\n' SAT-DIRECT-REPLAY-PASS >"$RESULT_DIR/VERDICT.txt"
elif [[ "$rc" == 20 ]]; then
  printf '%s\n' UNSAT-SOLVER-EVIDENCE-ONLY >"$RESULT_DIR/VERDICT.txt"
else
  printf 'NONTERMINAL-SOLVER-RC-%s\n' "$rc" >"$RESULT_DIR/VERDICT.txt"
fi

date -u +%Y-%m-%dT%H:%M:%SZ >"$RESULT_DIR/end_utc"
(
  cd "$RESULT_DIR"
  find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 -print0 \
    | sort -z | xargs -0 sha256sum >OUTPUTS.sha256
)
cat "$RESULT_DIR/VERDICT.txt"
