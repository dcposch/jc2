#!/usr/bin/env bash
set -euo pipefail

: "${JOB_DIR:?}"
: "${FORMULA:?}"
: "${BASE_INDEX:?}"
: "${BASE_DIGITS:?}"
: "${TIMEOUT_SECONDS:=21600}"
: "${MEMORY_KIB:=25165824}"
: "${BOOLECTOR_BIN:=/usr/bin/boolector}"

[[ "$BASE_DIGITS" =~ ^[012]{7}$ ]]
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
printf '%s\n' "$BASE_INDEX" > "$JOB_DIR/base_index"
printf '%s\n' "$BASE_DIGITS" > "$JOB_DIR/base_digits"
sha256sum "$FORMULA" > "$JOB_DIR/PARENT_FORMULA.sha256"
test "$(tail -n 1 "$FORMULA")" = "(check-sat)"

input="$JOB_DIR/pinned_formula.smt2"
sed '$d' "$FORMULA" > "$input"
names=(Pp Qq Rr Tt s w h)
for index in $(seq 0 6); do
  digit=${BASE_DIGITS:index:1}
  printf '(assert (= pred_%s (_ bv%s 32)))\n' \
    "${names[index]}" "$digit" >> "$input"
done
printf '(check-sat)\n' >> "$input"
sha256sum "$input" > "$JOB_DIR/INPUT.sha256"

ulimit -v "$MEMORY_KIB"
"$BOOLECTOR_BIN" --version > "$JOB_DIR/solver.version"
sha256sum "$BOOLECTOR_BIN" > "$JOB_DIR/solver.binary.sha256"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  "$BOOLECTOR_BIN" -m -d -rwl3 "$input" \
  > "$JOB_DIR/solver.stdout" 2> "$JOB_DIR/solver.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/solver.rc"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
sha256sum "$JOB_DIR"/solver.* > "$JOB_DIR/OUTPUT.sha256"
exit "$rc"
