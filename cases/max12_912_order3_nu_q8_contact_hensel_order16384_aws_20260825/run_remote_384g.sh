#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then echo "usage: $0 REPO OUTROOT TAG FACTOR" >&2; exit 64; fi
repo=$1
outroot=$2
tag=$3
factor=$4
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 64 ;; esac
case "$factor" in linear67|linear58|linear26) ;; *) exit 64 ;; esac
case_dir=$repo/cases/max12_912_order3_nu_q8_contact_hensel_order16384_aws_20260825
base_dir=$repo/cases/max12_912_order3_nu_q8_contact_hensel_aws_20260825
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$lane"
set +e
python3 "$case_dir/generate_order16384.py" --factor "$factor" --order 16384 > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "factor=$factor"
  echo "order=16384"
  echo "generator_rc=$generator_rc"
  echo "virtual_memory_limit_kib=402653184"
  echo "method=full-8x8-Newton-doubling-corrected-Q8-contact"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate_order16384.py" "$base_dir/generate.py" \
    "$repo/cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/aws_box02_v1/result.json" \
    "$repo/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json" \
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
  ulimit -v 402653184
  timeout --signal=TERM --kill-after=120 21600 /usr/bin/time -v Singular -q < "$lane/input.sing"
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
endpoint=FAIL
if [ "$rc" -eq 0 ] \
  && grep -qx "factor=$factor" "$lane/result.out" \
  && grep -qx 'base_fail=0' "$lane/result.out" \
  && grep -qx 'gcd_detJ_factor_degree=0' "$lane/result.out" \
  && grep -qx 'order=16384' "$lane/result.out" \
  && grep -qx 'moving_vdim=16384' "$lane/result.out" \
  && grep -qx 'final_fail=0' "$lane/result.out" \
  && grep -qx 'h_contact_order=-1' "$lane/result.out" \
  && grep -qx 'h_lead_coefficient=0' "$lane/result.out" \
  && grep -qx 'h_contact_at_least=16384' "$lane/result.out" \
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
