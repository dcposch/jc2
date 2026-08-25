#!/bin/sh
set -eu
if [ "$#" -ne 5 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <prime> <root>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
prime=$4
root=$5
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$prime:$root" in *[!0-9:]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_wv_support_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=$prime"
  echo "root=$root"
  echo "order=192"
  echo "holdout=16"
  echo "max_degrees=24,16"
  echo "max_columns=176"
  echo "route=targeted exact modular w-v/theta-v support"
  sha256sum "$0" "$case_dir/wv_support.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_invariant_support_20260824/modular_support.py" \
    | sed 's/^/source_sha256=/'
  free -b | sed 's/^/start_free=/'
} > "$meta"
set +e
timeout --signal=TERM --kill-after=30 1800 nice -n 7 \
  python3 "$case_dir/wv_support.py" --prime "$prime" --root "$root" \
  --order 192 --max-left 24 --max-right 16 --max-columns 176 --holdout 16 \
  > "$lane/result.json" 2> "$lane/stderr.log"
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$lane/result.json" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$lane/stderr.log" | awk '{print $1}')"
  free -b | sed 's/^/end_free=/'
} >> "$meta"
exit "$rc"
