#!/bin/sh
set -eu
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TAG=as_canonical_q8_zero_next_high_20260825T042300Z_v3
RESULTS="$HERE/results_$TAG"
(cd "$RESULTS" && sha256sum -c OUTPUTS.sha256)
grep -F 'PASS-CANONICAL-Q8-ZERO-NEXT-HIGH-AGGREGATE' \
  "$RESULTS/aggregate.stdout" >/dev/null
grep -F 'sample_count 64' "$RESULTS/aggregate.stdout" >/dev/null
grep -F 'q7_compatible_count 64' "$RESULTS/aggregate.stdout" >/dev/null
grep -F 'high_zero_count_histogram {"0": 64}' \
  "$RESULTS/aggregate.stdout" >/dev/null
test ! -s "$RESULTS/aggregate.stderr"
i=0
while [ "$i" -lt 64 ]; do
  stem="sample_$(printf '%02d' "$i")"
  grep -F 'PASS-Q8STATE-NEXT-HIGH-SAMPLE' "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'q8_rank_pair_compatible [13, 13] True' \
    "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'q7_rank_pair_compatible [9, 9] True' \
    "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'q7_fiber_dimension_states 9 19683' \
    "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'high_zero_count 0' "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'quadratic_exact_nonzero_count True' \
    "$RESULTS/$stem.stdout" >/dev/null
  test ! -s "$RESULTS/$stem.stderr"
  i=$((i + 1))
done
echo PASS-CANONICAL-Q8-ZERO-NEXT-HIGH-RESULT-VERIFY
