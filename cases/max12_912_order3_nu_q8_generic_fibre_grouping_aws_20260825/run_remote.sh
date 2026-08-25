#!/bin/sh
set -eu
if [ "$#" -ne 6 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <characteristic> <engine> <absolute:0|1>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
characteristic=$4
engine=$5
absolute=$6
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$characteristic" in *[!0-9]*) exit 2 ;; esac
case "$engine" in std|slimgb) ;; *) exit 2 ;; esac
case "$absolute" in 0|1) ;; *) exit 2 ;; esac
if [ "$absolute" = 1 ] && [ "$characteristic" -ne 0 ]; then exit 2; fi
case_dir=$repo_root/cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
args="--characteristic $characteristic --engine $engine"
if [ "$absolute" = 1 ]; then args="$args --absolute"; fi
python3 "$case_dir/generate.py" $args > "$lane/input.sing" 2> "$lane/generator.stderr"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "characteristic=$characteristic"
  echo "engine=$engine"
  echo "absolute=$absolute"
  echo "route=generic Q8 quotient fibre over coefficient field w"
  echo "virtual_memory_limit_kib=268435456"
  echo "timeout_seconds=86400"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" "$case_dir/scan_primes.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_galois_primitivity_aws_20260825/FREEZE.txt" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
  free -b | sed 's/^/start_free=/'
} > "$meta"
set +e
(ulimit -v 268435456; timeout --signal=TERM --kill-after=300 86400 nice -n 8 \
  /usr/bin/time -v Singular -q < "$lane/input.sing" \
  > "$lane/result.out" 2> "$lane/stderr.log")
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
  free -b | sed 's/^/end_free=/'
} >> "$meta"
exit "$rc"
