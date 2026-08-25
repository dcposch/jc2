#!/bin/sh
set -eu

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TAG=as_canonical_q8q7_samples_20260825T041000Z
RESULTS="$HERE/results_$TAG"
(cd "$RESULTS" && sha256sum -c OUTPUTS.sha256)
grep -F 'PASS-CANONICAL-Q8Q7-FIBRE-SAMPLE-AGGREGATE' \
  "$RESULTS/aggregate.stdout" >/dev/null
grep -F 'sample_count 64' "$RESULTS/aggregate.stdout" >/dev/null
grep -F 'survivor_sample_count 64' "$RESULTS/aggregate.stdout" >/dev/null
test ! -s "$RESULTS/aggregate.stderr"
i=0
while [ "$i" -lt 64 ]; do
  stem="sample_$(printf '%02d' "$i")"
  grep -F 'PASS-CANONICAL-Q8Q7-FIBRE-SAMPLE' \
    "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'q9_rows_zero True' "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'q8_rank_pair [13, 13]' "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'q7_rank_cokernel 9 10' "$RESULTS/$stem.stdout" >/dev/null
  grep -F 'zero_count 129140163' "$RESULTS/$stem.stdout" >/dev/null
  test ! -s "$RESULTS/$stem.stderr"
  i=$((i + 1))
done
echo PASS-CANONICAL-Q8Q7-FIBRE-SAMPLES-RESULT-VERIFY
