#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then
  echo "usage: $0 <repo> <out-root> <concurrency>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
concurrency=$3
case "$concurrency" in ''|*[!0-9]*) exit 2 ;; esac
if [ "$concurrency" -lt 1 ] || [ "$concurrency" -gt 90 ]; then
  echo "concurrency must lie in 1..90" >&2
  exit 2
fi
if [ -e "$out_root" ]; then
  echo "duplicate output root refused" >&2
  exit 3
fi
mkdir -p "$out_root"
case_dir=$repo_root/cases/max12_912_order3_nu_q8_singular_broad_scan_aws_20260825
fixed_case=$repo_root/cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825
values=$out_root/values.txt
for w_value in $(seq 1 126); do
  case "$w_value" in 1|2|63|71|95|126) continue ;; esac
  echo "$w_value"
done > "$values"
meta=$out_root/dispatch.meta
{
  echo "tag=q8_p127_pure_singular_exhaustive_nonduplicate_v1"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "prime=127"
  echo "excluded_previously_audited_w=1,2,63,71,95,126"
  echo "expected_lane_count=$(wc -l < "$values" | tr -d ' ')"
  echo "concurrency=$concurrency"
  sha256sum "$0" "$fixed_case/run_one.sh" "$fixed_case/generate.py" \
    | sed 's/^/source_sha256=/'
  echo "values_sha256=$(sha256sum "$values" | awk '{print $1}')"
} > "$meta"
set +e
xargs -P "$concurrency" -n 1 sh -c \
  '"$1/cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825/run_one.sh" "$1" "$2" "q8_singular_p127_w${3}_std_v2" 127 "$3" std' \
  worker "$repo_root" "$out_root" < "$values"
rc=$?
set -e
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "rc=$rc"
} >> "$meta"
exit "$rc"
