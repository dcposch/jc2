#!/bin/sh
set -eu
if [ "$#" -ne 6 ]; then
  echo "usage: $0 <repo> <out-root> <tag> <completed-elim-lane> <timeout-seconds> <memory-kib>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
upstream=$4
timeout_seconds=$5
memory_kib=$6
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$timeout_seconds:$memory_kib" in *[!0-9:]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_box02_drl_fglm_controls_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
for file in "$upstream/input.ms" "$upstream/result.out" "$upstream/run.meta"; do
  [ -f "$file" ] || { echo "missing upstream file: $file" >&2; exit 4; }
done
grep -q '^rc=0$' "$upstream/run.meta" || { echo "upstream did not exit zero" >&2; exit 4; }
mkdir -p "$lane"
python3 "$case_dir/prepare_verify.py" --input "$upstream/input.ms" --basis "$upstream/result.out" \
  > "$lane/verify.sing" 2> "$lane/generator.stderr"
meta=$lane/run.meta
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "upstream=$upstream"
  echo "route=standardize candidate elimination ideal and reduce original rows"
  echo "virtual_memory_limit_kib=$memory_kib"
  echo "timeout_seconds=$timeout_seconds"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/prepare_verify.py" \
    "$upstream/input.ms" "$upstream/result.out" "$upstream/run.meta" \
    | sed 's/^/source_sha256=/'
  echo "verify_input_sha256=$(sha256sum "$lane/verify.sing" | awk '{print $1}')"
} > "$meta"
set +e
(ulimit -v "$memory_kib"; timeout --signal=TERM --kill-after=60 "$timeout_seconds" nice -n 7 \
  /usr/bin/time -v Singular -q < "$lane/verify.sing" \
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

