#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=43200}"
: "${MEMORY_KIB:=67108864}"
source_case="$JC2_ROOT/cases/as_fonly_d7_q3_state_complete_bv_20260825"
runner_case="$JC2_ROOT/cases/as_fonly_d7_q3_state_complete_bv_v2_20260825"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$runner_case/PREREGISTRATION.md" "$0" \
  "$source_case/emit_formula.py" "$source_case/replay_model.py" \
  "$MODEL_OUTPUT" > "$JOB_DIR/INPUT.sha256"
ulimit -v "$MEMORY_KIB"
env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$MODEL_OUTPUT" \
  PARENT_OUTPUT_JSON="$JOB_DIR/q3_parent_emitter.json" \
  SMT2_OUTPUT="$JOB_DIR/formula.smt2" OUTPUT_JSON="$JOB_DIR/emitter.json" \
  OMIT_HIGH="${OMIT_HIGH:-0}" EMITTER_TIMEOUT_MS=1 \
  python3 "$source_case/emit_formula.py" \
  > "$JOB_DIR/emitter.stdout" 2> "$JOB_DIR/emitter.stderr"
grep -q '^PASS-AS-Q3-STATE-COMPLETE-BV-EMITTER$' "$JOB_DIR/emitter.stdout"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  boolector -m -d "$JOB_DIR/formula.smt2" \
  > "$JOB_DIR/boolector.stdout" 2> "$JOB_DIR/boolector.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$JOB_DIR/boolector.rc"
case "$rc" in
  10)
    env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$MODEL_OUTPUT" \
      SOLVER_MODEL="$JOB_DIR/boolector.stdout" \
      PARENT_OUTPUT_JSON="$JOB_DIR/q3_parent_replay.json" \
      OUTPUT_JSON="$JOB_DIR/direct_replay.json" \
      python3 "$source_case/replay_model.py" \
      > "$JOB_DIR/direct_replay.stdout" 2> "$JOB_DIR/direct_replay.stderr"
    grep -q '^PASS-AS-Q3-STATE-COMPLETE-DIRECT-INTEGER-REPLAY$' \
      "$JOB_DIR/direct_replay.stdout"
    verdict=SAT-DIRECT-REPLAY-PASS
    ;;
  20)
    grep -q '^unsat$' "$JOB_DIR/boolector.stdout"
    verdict=UNSAT-SOLVER-EVIDENCE-ONLY
    ;;
  *)
    verdict=FAIL-BOOLECTOR-RC-$rc
    ;;
esac
printf '%s\n' "$verdict" > "$JOB_DIR/VERDICT.txt"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
test "$verdict" != "FAIL-BOOLECTOR-RC-$rc"
echo "PASS-$verdict"
