#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then
  echo "usage: $0 <repo> <out-root> <tag>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_generic_fglm_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
python3 "$case_dir/generate_drl.py" > "$lane/input.sing" 2> "$lane/generator.stderr"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "characteristic=127"
  echo "coefficient_field=F_127(w)"
  echo "engine=Singular-std-pure-DRL"
  echo "virtual_memory_limit_kib=67108864"
  echo "timeout_seconds=7200"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate_drl.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
} > "$meta"
set +e
(ulimit -v 67108864; timeout --signal=TERM --kill-after=120 7200 nice -n 8 \
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
