#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <engine>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
engine=$4
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$engine" in std|slimgb) ;; *) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
python3 "$case_dir/generate.py" --engine "$engine" \
  > "$lane/input.sing" 2> "$lane/generator.stderr"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "characteristic=127"
  echo "coefficient_field=F_127(w)"
  echo "engine=Singular-$engine-pure-DRL-candidate-reduction"
  echo "virtual_memory_limit_kib=134217728"
  echo "timeout_seconds=21600"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" "$case_dir/interpolation_candidate.json" \
    "$repo_root/cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
} > "$meta"
set +e
(ulimit -v 134217728; timeout --signal=TERM --kill-after=300 21600 nice -n 8 \
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
