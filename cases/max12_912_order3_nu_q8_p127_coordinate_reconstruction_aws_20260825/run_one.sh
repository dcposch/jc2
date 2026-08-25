#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <w-value>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
w_value=$4
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$w_value" in ''|*[!0-9]*) exit 2 ;; esac
if [ "$w_value" -lt 1 ] || [ "$w_value" -gt 126 ]; then exit 2; fi
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_coordinate_reconstruction_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
python3 "$case_dir/generate.py" --w-value "$w_value" \
  > "$lane/input.sing" 2> "$lane/generator.stderr"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=127"
  echo "w_value=$w_value"
  echo "route=original-ideal fixed-fibre stdfglm lex shape"
  echo "virtual_memory_limit_kib=134217728"
  echo "timeout_seconds=7200"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
} > "$meta"
set +e
(ulimit -v 134217728; timeout --signal=TERM --kill-after=120 7200 nice -n 10 \
  /usr/bin/time -v Singular -q < "$lane/input.sing" \
  > "$lane/result.out" 2> "$lane/stderr.log")
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
} >> "$meta"
exit "$rc"
