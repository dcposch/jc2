#!/usr/bin/env bash
set -euo pipefail

: "${FORMULA:?set FORMULA}"
: "${FORMULA_SHA256:?set FORMULA_SHA256}"
: "${RESULT_DIR:?set RESULT_DIR}"
: "${Z3_BIN:?set Z3_BIN}"
: "${SEED:?set SEED}"
: "${CAP_GIB:?set CAP_GIB}"
: "${TIMEOUT_SECONDS:?set TIMEOUT_SECONDS}"

mkdir -p "$RESULT_DIR"
actual=$(sha256sum "$FORMULA" | awk '{print $1}')
test "$actual" = "$FORMULA_SHA256"
test -x "$Z3_BIN"

date -u +%Y-%m-%dT%H:%M:%SZ > "$RESULT_DIR/start_utc"
hostname > "$RESULT_DIR/hostname"
printf '%s\n' "$actual  $FORMULA" > "$RESULT_DIR/INPUT.sha256"
"$Z3_BIN" --version > "$RESULT_DIR/solver.version"
sha256sum "$Z3_BIN" > "$RESULT_DIR/solver.binary.sha256"

set +e
(
  ulimit -v $((CAP_GIB * 1024 * 1024))
  exec /usr/bin/time -v timeout --signal=TERM --kill-after=60s \
    "$TIMEOUT_SECONDS" "$Z3_BIN" \
    smt.random_seed="$SEED" sat.random_seed="$SEED" "$FORMULA"
) > "$RESULT_DIR/solver.stdout" 2> "$RESULT_DIR/solver.stderr"
rc=$?
set -e

printf '%s\n' "$rc" > "$RESULT_DIR/solver.rc"
date -u +%Y-%m-%dT%H:%M:%SZ > "$RESULT_DIR/end_utc"
sha256sum "$RESULT_DIR"/solver.stdout "$RESULT_DIR"/solver.stderr \
  > "$RESULT_DIR/OUTPUT.sha256"
if test "$rc" -eq 0; then
  head -n 1 "$RESULT_DIR/solver.stdout" > "$RESULT_DIR/ENDPOINT"
else
  printf 'solver-rc-%s\n' "$rc" > "$RESULT_DIR/ENDPOINT"
fi

