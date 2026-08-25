#!/bin/sh
set -eu
if [ "$#" -ne 8 ]; then echo "usage: $0 REPO OUTROOT TAG ORDER ALGORITHM VARIABLES TIMEOUT VM_KIB" >&2; exit 64; fi
repo=$1
outroot=$2
tag=$3
order=$4
algorithm=$5
variables=$6
timecap=$7
vmcap=$8
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 64 ;; esac
case "$order" in dp|lp|Dp) ;; *) exit 64 ;; esac
case "$algorithm" in std|slimgb) ;; *) exit 64 ;; esac
case "$variables" in original|vfirst|ulast) ;; *) exit 64 ;; esac
case "$timecap:$vmcap" in *[!0-9:]*) exit 64 ;; esac
case_dir=$repo/cases/max12_912_order3_nu_q8_generic_vertical_length_orders_aws_20260825
base_dir=$repo/cases/max12_912_order3_nu_q8_generic_vertical_length_aws_20260825
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$lane"
set +e
python3 "$case_dir/generate_variant.py" --order "$order" --algorithm "$algorithm" --variables "$variables" > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "term_order=$order"
  echo "algorithm=$algorithm"
  echo "variable_order=$variables"
  echo "generator_rc=$generator_rc"
  echo "timeout_seconds=$timecap"
  echo "virtual_memory_limit_kib=$vmcap"
  echo "method=pure-Singular-generic-coefficient-field-localized-source-length"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate_variant.py" "$base_dir/generate.py" \
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
  ulimit -v "$vmcap"
  timeout --signal=TERM --kill-after=300 "$timecap" /usr/bin/time -v Singular -q < "$lane/input.sing"
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
endpoint=FAIL
if [ "$rc" -eq 0 ] \
  && grep -qx 'Q8-GENERIC-VERTICAL-LENGTH' "$lane/result.out" \
  && grep -qx "term_order=$order" "$lane/result.out" \
  && grep -qx "algorithm=$algorithm" "$lane/result.out" \
  && grep -qx "variable_order=$variables" "$lane/result.out" \
  && grep -qx 'source_fail=0' "$lane/result.out" \
  && ! grep -q '^   ?' "$lane/result.out"; then
  endpoint=PASS
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
