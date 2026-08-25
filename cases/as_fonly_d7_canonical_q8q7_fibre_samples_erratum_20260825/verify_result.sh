#!/bin/sh
set -eu
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
RESULTS="$HERE/results_as_q8_particular_erratum_20260825T0425Z"
(cd "$RESULTS" && sha256sum -c OUTPUTS.sha256)
grep -F 'sample_count 64' "$RESULTS/audit.stdout" >/dev/null
grep -F 'zero_particular_count 13' "$RESULTS/audit.stdout" >/dev/null
grep -F 'nonzero_particular_count 51' "$RESULTS/audit.stdout" >/dev/null
grep -F 'PASS-Q8-PARTICULAR-ERRATUM-AUDIT' "$RESULTS/audit.stdout" >/dev/null
test ! -s "$RESULTS/audit.stderr"
echo PASS-Q8-PARTICULAR-ERRATUM-RESULT-VERIFY
