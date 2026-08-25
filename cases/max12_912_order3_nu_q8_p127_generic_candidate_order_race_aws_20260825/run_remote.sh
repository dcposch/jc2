#!/bin/sh
set -eu
if [ "$#" -ne 7 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <engine> <order> <permutation> <memory-GiB>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
engine=$4
order=$5
permutation=$6
memory_gib=$7
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$engine" in std|slimgb) ;; *) exit 2 ;; esac
case "$order" in dp|lp|block) ;; *) exit 2 ;; esac
case "$permutation" in canonical|reverse|inv-first|interleave) ;; *) exit 2 ;; esac
case "$memory_gib" in ''|*[!0-9]*) exit 2 ;; esac
if [ "$memory_gib" -lt 8 ] || [ "$memory_gib" -gt 96 ]; then exit 2; fi
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_generic_candidate_order_race_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
memory_kib=$((memory_gib * 1024 * 1024))
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=127"
  echo "engine=$engine"
  echo "order=$order"
  echo "permutation=$permutation"
  echo "route=unseeded original ideal generic candidate reduction"
  echo "virtual_memory_limit_kib=$memory_kib"
  echo "timeout_seconds=21600"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
} > "$meta"
set +e
python3 "$case_dir/generate.py" --engine "$engine" --order "$order" --permutation "$permutation" \
  > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "generator_rc=$generator_rc"
  echo "generator_stderr_sha256=$(sha256sum "$lane/generator.stderr" | awk '{print $1}')"
  echo "input_sha256=$(sha256sum "$lane/input.sing" | awk '{print $1}')"
  echo "input_bytes=$(wc -c < "$lane/input.sing" | tr -d ' ')"
} >> "$meta"
if [ "$generator_rc" -ne 0 ] || [ ! -s "$lane/input.sing" ]; then
  {
    echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    echo "rc=97"
    echo "failure=generator"
  } >> "$meta"
  exit 97
fi
set +e
(ulimit -v "$memory_kib"; timeout --signal=TERM --kill-after=120 21600 nice -n 10 \
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
