#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then
  echo "usage: $0 REPO OUTROOT SHAPE_SAMPLES BASE_W" >&2
  exit 64
fi
repo=$1
outroot=$2
samples=$3
base_w=$4
case "$base_w" in *[!0-9]*|'') exit 64 ;; esac
if [ "$base_w" -lt 1 ] || [ "$base_w" -gt 126 ] || [ "$base_w" -eq 39 ] || [ "$base_w" -eq 56 ] || [ "$base_w" -eq 125 ]; then
  echo "not a preregistered good fibre: $base_w" >&2
  exit 64
fi
case_dir=$repo/cases/max12_912_order3_nu_q8_p127_breadth_order8_aws_20260825
tag=$(printf 'q8_p127_breadth_w%03d_order8_v1' "$base_w")
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused: $lane" >&2; exit 65; fi
mkdir -p "$lane"
set +e
python3 "$case_dir/generate_breadth.py" --samples "$samples" --base-w "$base_w" \
  > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "characteristic=127"
  echo "base_w=$base_w"
  echo "hensel_order=8"
  echo "method=coefficient-wise-moving-v-breadth-contact"
  echo "generator_rc=$generator_rc"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate_breadth.py" \
    "$repo/cases/max12_912_order3_nu_q8_p127_hensel_coordinate_lift_aws_20260825/generate.py" \
    "$samples" \
    "$repo/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json" \
    "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
  echo "input_bytes=$(wc -c < "$lane/input.sing" | tr -d ' ')"
} > "$lane/run.meta"
if [ "$generator_rc" -ne 0 ] || [ ! -s "$lane/input.sing" ] || [ -s "$lane/generator.stderr" ]; then
  {
    date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
    echo "rc=90"
    echo "endpoint=GENERATOR_FAIL"
  } >> "$lane/run.meta"
  exit 90
fi
set +e
(
  ulimit -v 8388608
  timeout --signal=TERM --kill-after=60 3600 /usr/bin/time -v \
    Singular -q < "$lane/input.sing"
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
endpoint=FAIL
coeff_count=$(grep -c '^coefficient_order=' "$lane/result.out" || true)
if [ "$rc" -eq 0 ] \
  && grep -qx "base_w=$base_w" "$lane/result.out" \
  && grep -qx 'base_fail=0' "$lane/result.out" \
  && grep -qx 'H0_degree=190' "$lane/result.out" \
  && grep -qx 'gcd_detJ_H0_degree=0' "$lane/result.out" \
  && grep -qx 'gcd_Hv_H0_degree=0' "$lane/result.out" \
  && grep -qx 'moving_dimension=0' "$lane/result.out" \
  && grep -qx 'moving_vdim=1520' "$lane/result.out" \
  && [ "$coeff_count" -eq 7 ] \
  && grep -qx 'coefficient_order=7' "$lane/result.out" \
  && grep -qx 'order=8' "$lane/result.out" \
  && grep -qx 'final_fail=0' "$lane/result.out" \
  && ! grep -q '^   ?' "$lane/result.out"; then
  endpoint=PASS
else
  [ "$rc" -ne 0 ] || rc=91
fi
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
  echo "rc=$rc"
  echo "endpoint=$endpoint"
  echo "coefficient_marker_count=$coeff_count"
  sha256sum "$lane/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$lane/stderr.log" | sed 's/^/stderr_sha256=/'
} >> "$lane/run.meta"
exit "$rc"
