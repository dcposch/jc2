#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?}"
: "${RESULT_ROOT:?}"
if [[ "$#" -ne 4 ]]; then
  echo "usage: $0 base_index seven_trits predecessor_count completion_count" >&2
  exit 2
fi
base_index=$1
digits=$2
predecessor_count=$3
completion_count=$4
[[ "$base_index" =~ ^[0-9]+$ ]]
[[ "$digits" =~ ^[012]{7}$ ]]
[[ "$predecessor_count" =~ ^[0-9]+$ ]]
[[ "$completion_count" =~ ^[0-9]+$ ]]

pin="${digits:0:1},${digits:1:1},${digits:2:1},${digits:3:1},${digits:4:1},${digits:5:1},${digits:6:1}"
out="$RESULT_ROOT/base_$(printf '%04d' "$base_index")_${digits}"
mkdir -p "$out"
printf 'base_index=%s\nstructural_digits=%s\npredecessor_count=%s\ncompletion_count=%s\nhost=%s\n' \
  "$base_index" "$digits" "$predecessor_count" "$completion_count" \
  "$(hostname)" > "$out/base.meta"

env JC2_ROOT="$JC2_ROOT" PIN_STRUCTURAL="$pin" SOLVER_TIMEOUT_MS=1 \
  SMT2_OUTPUT="$out/formula.smt2" OUTPUT_JSON="$out/emitter.json" \
  timeout --signal=TERM --kill-after=60s 7200 /usr/bin/time -v \
  python3 "$JC2_ROOT/cases/as_fonly_d7_global_predecessor_rawq7_20260825/solve_global_predecessor.py" \
  > "$out/emitter.stdout" 2> "$out/emitter.stderr"
grep -q '^PASS-AS-GLOBAL-PREDECESSOR-RAWQ7-EMITTER$' "$out/emitter.stdout"

set +e
timeout --signal=TERM --kill-after=60s 43200 /usr/bin/time -v \
  boolector -m -d "$out/formula.smt2" \
  > "$out/boolector.stdout" 2> "$out/boolector.stderr"
solver_rc=$?
set -e
printf '%s\n' "$solver_rc" > "$out/boolector.rc"
case "$solver_rc" in
  10)
    env JC2_ROOT="$JC2_ROOT" MODEL_OUTPUT="$out/boolector.stdout" \
      OUTPUT_JSON="$out/direct_replay.json" EXPECT_TERMINAL_ZERO=1 \
      timeout --signal=TERM --kill-after=60s 7200 /usr/bin/time -v \
      python3 "$JC2_ROOT/cases/as_fonly_d7_global_predecessor_rawq7_20260825/replay_model.py" \
      > "$out/direct_replay.stdout" 2> "$out/direct_replay.stderr"
    grep -q '^PASS-DIRECT-INTEGER-SOURCE-REPLAY$' "$out/direct_replay.stdout"
    verdict=SAT-DIRECT-REPLAY-PASS
    ;;
  20)
    grep -q '^unsat$' "$out/boolector.stdout"
    verdict=UNSAT-SOLVER-EVIDENCE-ONLY
    ;;
  *)
    echo "FAIL-BOOLECTOR-RC-$solver_rc" >&2
    exit 1
    ;;
esac

printf '%s\n' "$verdict" > "$out/VERDICT.txt"
(
  cd "$out"
  find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 -print0 \
    | sort -z | xargs -0 sha256sum
) > "$out/OUTPUTS.sha256"
echo "PASS-STRUCTURAL-BASE-$base_index-$digits-$verdict"
