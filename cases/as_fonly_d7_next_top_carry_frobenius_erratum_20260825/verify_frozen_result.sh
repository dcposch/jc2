#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
remote_name=REMOTE_RESULTS_as_d7_top_frob_erratum_20260825T003321Z
(
  cd "$case_dir/$remote_name"
  shasum -a 256 -c ../REMOTE_RESULTS_MANIFEST.sha256
  test ! -s replay.err
  grep -q '^PASS-NEXT-TOP-CARRY-FROBENIUS-ERRATUM-SOURCE$' replay.out
)
(
  cd "$case_dir"
  shasum -a 256 -c RESULT_MANIFEST.sha256
)
printf '%s\n' 'PASS-AS-FONLY-D7-TOP-FROBENIUS-ERRATUM-FROZEN'
