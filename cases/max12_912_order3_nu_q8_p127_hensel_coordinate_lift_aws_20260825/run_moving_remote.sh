#!/bin/sh
set -eu
if [ "$#" -ne 5 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <shape-samples.json> <order>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
samples=$4
order=$5
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$order" in 8|16|32|64|128) ;; *) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_hensel_coordinate_lift_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
meta=$lane/run.meta
set +e
python3 "$case_dir/generate_moving.py" --samples "$samples" --order "$order" \
  > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "characteristic=127"
  echo "base_w=25"
  echo "hensel_order=$order"
  echo "method=coefficient-wise-moving-v-basis"
  echo "generator_rc=$generator_rc"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate_moving.py" "$case_dir/generate.py" "$samples" \
    "$repo_root/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
  echo "input_bytes=$(wc -c < "$lane/input.sing" | tr -d ' ')"
} > "$meta"
if [ "$generator_rc" -ne 0 ] || [ ! -s "$lane/input.sing" ] || [ -s "$lane/generator.stderr" ]; then
  {
    echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    echo "rc=90"
    echo "endpoint=GENERATOR_FAIL"
  } >> "$meta"
  exit 90
fi
set +e
(ulimit -v 33554432; timeout --signal=TERM --kill-after=180 7200 nice -n 5 \
  /usr/bin/time -v Singular -q < "$lane/input.sing" \
  > "$lane/result.out" 2> "$lane/stderr.log")
rc=$?
set -e
endpoint=FAIL
expected_vdim=$((190 * order))
if [ "$rc" -eq 0 ] \
  && grep -qx 'base_fail=0' "$lane/result.out" \
  && grep -qx "moving_vdim=$expected_vdim" "$lane/result.out" \
  && grep -qx 'final_fail=0' "$lane/result.out" \
  && ! grep -q '^   ?' "$lane/result.out"; then
  endpoint=PASS
else
  [ "$rc" -ne 0 ] || rc=91
fi
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "endpoint=$endpoint"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
