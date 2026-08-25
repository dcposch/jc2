#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then echo "usage: $0 REPO OUTROOT TAG W_VALUE" >&2; exit 64; fi
repo=$1
outroot=$2
tag=$3
wvalue=$4
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 64 ;; esac
case "$wvalue" in *[!0-9]*) exit 64 ;; esac
case_dir=$repo/cases/max12_912_order3_nu_q8_projective_fibre_boundary_saturated_aws_20260825
base_dir=$repo/cases/max12_912_order3_nu_q8_projective_fibre_boundary_aws_20260825
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$lane"
set +e
python3 "$case_dir/generate.py" --w-value "$wvalue" > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "w_value=$wvalue"
  echo "generator_rc=$generator_rc"
  echo "timeout_seconds=7200"
  echo "virtual_memory_limit_kib=134217728"
  echo "method=pure-Singular-global-family-t-saturation-projective-boundary"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" "$base_dir/generate.py" \
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
  ulimit -v 134217728
  timeout --signal=TERM --kill-after=120 7200 /usr/bin/time -v Singular -q < "$lane/input.sing"
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
endpoint=FAIL
if [ "$rc" -eq 0 ] \
  && grep -qx 'Q8-PROJECTIVE-FIBRE-SATURATED-BOUNDARY' "$lane/result.out" \
  && grep -qx "w_value=$wvalue" "$lane/result.out" \
  && grep -qx 'homogenization_fail=0' "$lane/result.out" \
  && grep -qx 'empty_count=7' "$lane/result.out" \
  && ! grep -q '^   ?' "$lane/result.out"; then
  endpoint=EMPTY_ALL
elif [ "$rc" -eq 0 ] \
  && grep -qx 'Q8-PROJECTIVE-FIBRE-SATURATED-BOUNDARY' "$lane/result.out" \
  && grep -qx 'homogenization_fail=0' "$lane/result.out" \
  && grep -q '^empty_count=' "$lane/result.out" \
  && ! grep -q '^   ?' "$lane/result.out"; then
  endpoint=SATURATED_BOUNDARY_PRESENT
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
