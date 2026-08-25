#!/bin/sh
set -eu

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TAG=as_global_q7_kuranishi_20260825T040000Z
RESULTS="$HERE/results_$TAG"
(cd "$RESULTS" && shasum -a 256 -c OUTPUTS.sha256)
grep -F 'PASS-GLOBAL-Q7-KURANISHI-QUADRATIC-PRESENTATION' \
  "$RESULTS/aggregate.stdout" >/dev/null
grep -F 'nonzero_coefficient_count 4' "$RESULTS/aggregate.stdout" >/dev/null
grep -F "support_names ['t6', 't8', 's15', 's17']" \
  "$RESULTS/aggregate.stdout" >/dev/null
test ! -s "$RESULTS/aggregate.stderr"
i=0
while [ "$i" -lt 36 ]; do
  grep -F 'PASS-GLOBAL-Q7-KURANISHI-DESIGN-SHARD' \
    "$RESULTS/shard_$(printf '%02d' "$i").stdout" >/dev/null
  test ! -s "$RESULTS/shard_$(printf '%02d' "$i").stderr"
  i=$((i + 1))
done
echo PASS-GLOBAL-Q7-KURANISHI-RESULT-VERIFY
