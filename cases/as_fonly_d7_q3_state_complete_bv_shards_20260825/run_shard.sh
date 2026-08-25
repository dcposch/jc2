#!/usr/bin/env bash
set -euo pipefail
: "${JC2_ROOT:?}"
: "${MODEL_OUTPUT:?}"
: "${FORMULA_INPUT:?}"
: "${ASSIGNMENTS_JSON:?}"
: "${BRANCH_INDEX:?}"
: "${JOB_DIR:?}"
: "${TIMEOUT_SECONDS:=43200}"
: "${MEMORY_KIB:=8388608}"
case_dir="$JC2_ROOT/cases/as_fonly_d7_q3_state_complete_bv_shards_20260825"
source_case="$JC2_ROOT/cases/as_fonly_d7_q3_state_complete_bv_20260825"
mkdir -p "$JOB_DIR"
hostname > "$JOB_DIR/hostname"
date -u +%FT%TZ > "$JOB_DIR/start_utc"
sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/pin_formula.py" \
  "$case_dir/run_shard.sh" "$source_case/replay_model.py" \
  "$FORMULA_INPUT" "$ASSIGNMENTS_JSON" "$MODEL_OUTPUT" \
  > "$JOB_DIR/INPUT.sha256"
env FORMULA_INPUT="$FORMULA_INPUT" ASSIGNMENTS_JSON="$ASSIGNMENTS_JSON" \
  BRANCH_INDEX="$BRANCH_INDEX" SMT2_OUTPUT="$JOB_DIR/formula.pinned.smt2" \
  OUTPUT_JSON="$JOB_DIR/pin.json" python3 "$case_dir/pin_formula.py" \
  > "$JOB_DIR/pin.stdout" 2> "$JOB_DIR/pin.stderr"
grep -q '^PASS-AS-Q3-FIRST-CARRY-PIN$' "$JOB_DIR/pin.stdout"
ulimit -v "$MEMORY_KIB"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60s "$TIMEOUT_SECONDS" \
  boolector -m -d "$JOB_DIR/formula.pinned.smt2" \
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
  *) verdict=FAIL-BOOLECTOR-RC-$rc ;;
esac
printf '%s\n' "$verdict" > "$JOB_DIR/VERDICT.txt"
date -u +%FT%TZ > "$JOB_DIR/end_utc"
find "$JOB_DIR" -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$JOB_DIR/OUTPUT.sha256"
test "$verdict" != "FAIL-BOOLECTOR-RC-$rc"
echo "PASS-$verdict"
