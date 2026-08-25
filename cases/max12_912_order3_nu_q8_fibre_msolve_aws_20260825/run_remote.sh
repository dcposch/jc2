#!/bin/sh
set -eu
if [ "$#" -ne 7 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <prime> <w-value> <elim|param> <threads>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
prime=$4
w_value=$5
mode=$6
threads=$7
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$prime:$w_value:$threads" in *[!0-9:]*) exit 2 ;; esac
case "$mode" in elim|param) ;; *) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_fibre_msolve_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
python3 "$case_dir/generate.py" --prime "$prime" --w-value "$w_value" \
  > "$lane/input.ms" 2> "$lane/generator.stderr"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=$prime"
  echo "w_value=$w_value"
  echo "mode=$mode"
  echo "threads=$threads"
  echo "route=fixed-w msolve elimination/parametrization discriminator"
  echo "virtual_memory_limit_kib=67108864"
  echo "timeout_seconds=14400"
  msolve -h 2>&1 | head -1 | sed 's/^/msolve=/'
  sha256sum "$0" "$case_dir/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825/generate.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.ms" | awk '{print $1}')"
} > "$meta"
if [ "$mode" = elim ]; then
  mode_args="-e 7 -g 2"
else
  mode_args=""
fi
set +e
(ulimit -v 67108864; timeout --signal=TERM --kill-after=120 14400 nice -n 6 \
  /usr/bin/time -v msolve -v 2 -t "$threads" $mode_args \
  -f "$lane/input.ms" -o "$lane/result.out" \
  > "$lane/console.out" 2> "$lane/stderr.log")
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "result_sha256=$(sha256sum "$lane/result.out" | awk '{print $1}')"
  echo "console_sha256=$(sha256sum "$lane/console.out" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
} >> "$meta"
exit "$rc"

