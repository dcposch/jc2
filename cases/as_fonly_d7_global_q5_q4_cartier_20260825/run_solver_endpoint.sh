#!/usr/bin/env bash
set -euo pipefail

: "${JOB_DIR:?}"
: "${FORMULA:?}"
: "${ENGINE:?}"
: "${TIMEOUT_SECONDS:=43200}"
: "${MEMORY_KIB:=134217728}"

mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$FORMULA" > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"

case "$ENGINE" in
  boolector_rwl3)
    solver=(/usr/bin/boolector -m -d -rwl3 "$FORMULA")
    /usr/bin/boolector --version > "$JOB_DIR/solver.version"
    ;;
  boolector_rwl0)
    solver=(/usr/bin/boolector -m -d -rwl0 "$FORMULA")
    /usr/bin/boolector --version > "$JOB_DIR/solver.version"
    ;;
  boolector_rwl2)
    solver=(/usr/bin/boolector -m -d -rwl2 "$FORMULA")
    /usr/bin/boolector --version > "$JOB_DIR/solver.version"
    ;;
  z3_416_seed23)
    solver=(/home/ubuntu/jobs/as_fullfibre_qfbv_20260825T0602Z_v2/z3_4_16/bin/z3
            smt.random_seed=23 sat.random_seed=23 "$FORMULA")
    "${solver[0]}" -version > "$JOB_DIR/solver.version"
    ;;
  z3_48_seed61)
    solver=(/usr/bin/z3 smt.random_seed=61 sat.random_seed=61 "$FORMULA")
    "${solver[0]}" -version > "$JOB_DIR/solver.version"
    ;;
  *)
    echo "unknown ENGINE=$ENGINE" >&2
    exit 64
    ;;
esac

sha256sum "${solver[0]}" > "$JOB_DIR/solver.binary.sha256"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  "${solver[@]}" > "$JOB_DIR/solver.stdout" 2> "$JOB_DIR/solver.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/solver.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
sha256sum "$JOB_DIR"/solver.* > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
