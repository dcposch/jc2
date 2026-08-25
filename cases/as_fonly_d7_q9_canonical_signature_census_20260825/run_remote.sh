#!/usr/bin/env bash
set -euo pipefail

: "${JC2_ROOT:?set JC2_ROOT}"
: "${RESULTS_DIR:?set RESULTS_DIR}"
: "${SHARD_COUNT:?set SHARD_COUNT}"

mkdir -p "$RESULTS_DIR"
for shard_index in $(seq 0 $((SHARD_COUNT - 1))); do
  SHARD_INDEX="$shard_index" \
  python3 "$JC2_ROOT/cases/as_fonly_d7_q9_canonical_signature_census_20260825/compile_shard.py" \
    >"$RESULTS_DIR/shard_$(printf '%03d' "$shard_index").stdout" \
    2>"$RESULTS_DIR/shard_$(printf '%03d' "$shard_index").stderr" &
done
wait

for stderr in "$RESULTS_DIR"/shard_*.stderr; do
  test ! -s "$stderr"
done
pass_count=$(grep -l 'PASS-AS-Q9-CANONICAL-SIGNATURE-SHARD' \
  "$RESULTS_DIR"/shard_*.stdout | wc -l | tr -d ' ')
test "$pass_count" = "$SHARD_COUNT"

python3 "$JC2_ROOT/cases/as_fonly_d7_q9_canonical_signature_census_20260825/aggregate.py" \
  >"$RESULTS_DIR/aggregate.stdout" 2>"$RESULTS_DIR/aggregate.stderr"
test ! -s "$RESULTS_DIR/aggregate.stderr"
grep -q 'PASS-AS-Q9-CANONICAL-SIGNATURE-AGGREGATE' "$RESULTS_DIR/aggregate.stdout"

(
  cd "$RESULTS_DIR"
  find . -type f ! -name OUTPUTS.sha256 -print0 \
    | LC_ALL=C sort -z \
    | xargs -0 shasum -a 256 > OUTPUTS.sha256
)
