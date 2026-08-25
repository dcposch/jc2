#!/bin/sh
set -eu
if [ "$#" -ne 9 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <prime> <w-value> <drl|fglm|elim> <threads> <seed> <timeout-seconds>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
prime=$4
w_value=$5
mode=$6
threads=$7
seed=$8
timeout_seconds=$9
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$prime:$w_value:$threads:$seed:$timeout_seconds" in *[!0-9:]*) exit 2 ;; esac
case "$mode" in drl|fglm|elim) ;; *) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_box02_drl_fglm_controls_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
python3 "$case_dir/generate.py" --prime "$prime" --w-value "$w_value" \
  > "$lane/input.ms" 2> "$lane/generator.stderr"
case "$mode" in
  drl) mode_args="-g 2" ;;
  fglm) mode_args="" ;;
  elim) mode_args="-e 7 -g 2" ;;
esac
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=$prime"
  echo "input_characteristic=$(sed -n '2p' "$lane/input.ms")"
  echo "w_value=$w_value"
  echo "mode=$mode"
  echo "threads=$threads"
  echo "random_seed=$seed"
  echo "route=independent fixed-w DRL/FGLM/elimination control"
  echo "virtual_memory_limit_kib=134217728"
  echo "timeout_seconds=$timeout_seconds"
  msolve --version 2>&1 | head -1 | sed 's/^/msolve=/'
  sha256sum "$0" "$case_dir/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_fibre_msolve_aws_20260825/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
  echo "input_sha256=$(sha256sum "$lane/input.ms" | awk '{print $1}')"
} > "$meta"
set +e
(ulimit -v 134217728; timeout --signal=TERM --kill-after=120 "$timeout_seconds" nice -n 5 \
  /usr/bin/time -v msolve -v 2 -t "$threads" --random-seed "$seed" $mode_args \
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

