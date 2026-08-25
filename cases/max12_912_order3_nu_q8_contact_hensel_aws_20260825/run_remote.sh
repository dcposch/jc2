#!/bin/sh
set -eu
if [ "$#" -ne 6 ]; then echo "usage: $0 REPO OUTROOT TAG FACTOR ORDER TIMEOUT" >&2; exit 64; fi
repo=$1; outroot=$2; tag=$3; factor=$4; order=$5; timecap=$6
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 64 ;; esac
case "$factor" in linear67|linear58|linear26|quintic) ;; *) exit 64 ;; esac
case "$order" in 64|256|1024|2048|4096|8192) ;; *) exit 64 ;; esac
case "$timecap" in *[!0-9]*|'') exit 64 ;; esac
case_dir=$repo/cases/max12_912_order3_nu_q8_contact_hensel_aws_20260825
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$lane"
set +e
python3 "$case_dir/generate.py" --factor "$factor" --order "$order" > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"; hostname | sed 's/^/host=/'; date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "factor=$factor"; echo "order=$order"; echo "generator_rc=$generator_rc"
  echo "method=full-8x8-Newton-doubling-corrected-Q8-contact"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" \
    "$repo/cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/aws_box02_v1/result.json" \
    "$repo/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json" \
    "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
} > "$lane/run.meta"
if [ "$generator_rc" -ne 0 ] || [ ! -s "$lane/input.sing" ] || [ -s "$lane/generator.stderr" ]; then
  echo "rc=90" >> "$lane/run.meta"; echo "endpoint=GENERATOR_FAIL" >> "$lane/run.meta"; exit 90
fi
set +e
(
  ulimit -v 67108864
  timeout --signal=TERM --kill-after=120 "$timecap" /usr/bin/time -v Singular -q < "$lane/input.sing"
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
endpoint=FAIL
if [ "$rc" -eq 0 ] \
  && grep -qx "factor=$factor" "$lane/result.out" \
  && grep -qx 'base_fail=0' "$lane/result.out" \
  && grep -qx 'gcd_detJ_factor_degree=0' "$lane/result.out" \
  && grep -qx "order=$order" "$lane/result.out" \
  && grep -qx 'final_fail=0' "$lane/result.out" \
  && grep -q '^h_contact_order=' "$lane/result.out" \
  && ! grep -q '^   ?' "$lane/result.out"; then endpoint=PASS; else [ "$rc" -ne 0 ] || rc=91; fi
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ; echo "rc=$rc"; echo "endpoint=$endpoint"
  sha256sum "$lane/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$lane/stderr.log" | sed 's/^/stderr_sha256=/'
} >> "$lane/run.meta"
exit "$rc"
