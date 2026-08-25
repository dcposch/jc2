#!/bin/sh
set -eu
if [ "$#" -ne 5 ]; then echo "usage: $0 REPO OUTROOT TAG CHART W_VALUE" >&2; exit 64; fi
repo=$1
outroot=$2
tag=$3
chart=$4
wvalue=$5
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 64 ;; esac
case "$chart" in u|c|d2|d4|x1|x5|v) ;; *) exit 64 ;; esac
case "$wvalue" in *[!0-9]*) exit 64 ;; esac
case_dir=$repo/cases/max12_912_order3_nu_q8_projective_fibre_boundary_aws_20260825
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$lane"
set +e
python3 "$case_dir/generate.py" --chart "$chart" --w-value "$wvalue" > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "chart=$chart"
  echo "w_value=$wvalue"
  echo "generator_rc=$generator_rc"
  echo "timeout_seconds=3600"
  echo "virtual_memory_limit_kib=67108864"
  echo "method=pure-Singular-global-family-raw-projective-boundary-chart"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" \
    "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
} > "$lane/run.meta"
if [ "$generator_rc" -ne 0 ] || [ ! -s "$lane/input.sing" ] || [ -s "$lane/generator.stderr" ]; then
  echo "rc=90" >> "$lane/run.meta"
  echo "endpoint=GENERATOR_FAIL" >> "$lane/run.meta"
  exit 90
fi
set +e
(
  ulimit -v 67108864
  timeout --signal=TERM --kill-after=120 3600 /usr/bin/time -v Singular -q < "$lane/input.sing"
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
endpoint=FAIL
if [ "$rc" -eq 0 ] \
  && grep -qx 'Q8-PROJECTIVE-FIBRE-RAW-BOUNDARY' "$lane/result.out" \
  && grep -qx "w_value=$wvalue" "$lane/result.out" \
  && grep -qx "chart=$chart" "$lane/result.out" \
  && grep -qx 'homogenization_fail=0' "$lane/result.out" \
  && ! grep -q '^   ?' "$lane/result.out"; then
  if grep -qx 'boundary_empty=1' "$lane/result.out"; then endpoint=EMPTY; else endpoint=RAW_BOUNDARY_PRESENT; fi
else
  [ "$rc" -ne 0 ] || rc=91
fi
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
  echo "rc=$rc"
  echo "endpoint=$endpoint"
  sha256sum "$lane/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$lane/stderr.log" | sed 's/^/stderr_sha256=/'
} >> "$lane/run.meta"
exit "$rc"
