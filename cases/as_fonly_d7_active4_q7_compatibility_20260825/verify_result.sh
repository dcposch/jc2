#!/bin/sh
set -eu

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TAG=as_active4_q7_compat_20260825T032738Z
RESULTS="$HERE/results_$TAG"

(cd "$RESULTS" && shasum -a 256 -c OUTPUTS.sha256)
grep -F 'PASS-ACTIVE4-Q7-COMPATIBILITY-CUBE' "$RESULTS/replay.stdout" >/dev/null
grep -F 'compatible_count 1' "$RESULTS/replay.stdout" >/dev/null
grep -F 'compatible_parameters [[0, 0, 0, 0]]' "$RESULTS/replay.stdout" >/dev/null
test ! -s "$RESULTS/replay.stderr"
echo PASS-ACTIVE4-Q7-COMPATIBILITY-RESULT-VERIFY
