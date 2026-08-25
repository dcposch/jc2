#!/bin/sh
# Evidence-aware AWS runner.  Run only on a provisioned Linux host.
set -eu

if [ "$#" -ne 4 ]; then
  echo "usage: $0 <repo-root> <output-root> <tag> <std|slimgb>" >&2
  exit 2
fi
repo_root=$1
output_root=$2
tag=$3
engine=$4
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case "$engine" in std|slimgb) ;; *) exit 2 ;; esac

case_dir=$repo_root/cases/max12_912_order3_nu_q8_absolute_component_grouping_aws_20260825
lane=$output_root/$tag
if [ -e "$lane" ]; then
  echo "duplicate lane refused: $lane" >&2
  exit 3
fi
mkdir -p "$lane"

meta=$lane/run.meta
input=$lane/input.sing
stdout=$lane/result.out
stderr=$lane/stderr.log
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "engine=$engine"
  echo "characteristic=0"
  echo "virtual_memory_limit_kib=268435456"
  echo "timeout_seconds=86400"
  echo "python=$(python3 --version 2>&1)"
  echo "singular=$(/usr/bin/Singular --version | head -1)"
  sha256sum "$0" "$case_dir/generate.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256" \
    "$repo_root/cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/FREEZE.txt" \
    | sed 's/^/source_sha256=/'
  free -b | sed 's/^/start_free=/'
} > "$meta"

python3 "$case_dir/generate.py" --engine "$engine" > "$input" 2> "$lane/generator.stderr"
echo "input_sha256=$(sha256sum "$input" | awk '{print $1}')" >> "$meta"

ulimit -v 268435456
set +e
timeout --signal=TERM --kill-after=300 86400 nice -n 10 \
  /usr/bin/time -v /usr/bin/Singular -q < "$input" > "$stdout" 2> "$stderr"
rc=$?
set -e

{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
  echo "stdout_sha256=$(sha256sum "$stdout" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$stderr" | awk '{print $1}')"
  free -b | sed 's/^/end_free=/'
} >> "$meta"
exit "$rc"
