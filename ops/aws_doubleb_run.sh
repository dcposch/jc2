#!/bin/sh
# Evidence-aware remote runner for the max12 normalized double-B race.
# Usage: aws_doubleb_run.sh TAG BACKEND CHARACTERISTIC TIMEOUT_SECONDS
set -eu

if [ "$#" -ne 4 ]; then
  echo "usage: $0 TAG BACKEND CHARACTERISTIC TIMEOUT_SECONDS" >&2
  exit 2
fi

tag=$1
backend=$2
characteristic=$3
cap=$4

case "$tag" in
  ''|*[!A-Za-z0-9._-]*) echo "invalid tag" >&2; exit 2 ;;
esac
case "$characteristic" in
  ''|*[!0-9]*) echo "invalid characteristic" >&2; exit 2 ;;
esac
case "$cap" in
  ''|*[!0-9]*) echo "invalid timeout" >&2; exit 2 ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)
case_dir=$repo_root/cases/max12_912_order3_nu1_probe_20260824
out_root=${JC2_DOUBLEB_OUT:-$repo_root/aws-doubleb-out}
lane=$out_root/$tag

if [ -e "$lane" ]; then
  echo "duplicate lane refused: $lane" >&2
  exit 3
fi
mkdir -p "$lane"

meta=$lane/metadata.txt
input=$lane/input
result=$lane/result.out
stderr=$lane/stderr.log

{
  echo "tag=$tag"
  echo "backend=$backend"
  echo "characteristic=$characteristic"
  echo "timeout_seconds=$cap"
  echo "host=$(hostname)"
  echo "nproc=$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo UNKNOWN)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "python=$(python3 --version 2>&1)"
  echo "singular=$(Singular --version 2>/dev/null | head -n 1 || echo MISSING)"
  echo "msolve=$(msolve --version 2>&1 | head -n 1 || echo MISSING)"
  sha256sum "$script_dir/aws_doubleb_run.sh" | sed 's/^/runner_sha256=/'
  for source in \
    "$case_dir/generate_double_b_p_projection.py" \
    "$case_dir/generate_double_b_projection.py" \
    "$case_dir/generate_weighted_projection.py" \
    "$case_dir/generate_double_b_msolve.py" \
    "$repo_root/cases/max12_912_order3_fibre_20260824/order3_fibre.py" \
    "$repo_root/cases/max12_high_row_probe_20260824/shared_faber_probe.py"
  do
    if [ -f "$source" ]; then
      sha256sum "$source" | sed 's/^/source_sha256=/'
    fi
  done
  free -b | sed 's/^/start_free=/'
} > "$meta"

case "$backend" in
  singular-p-sat-slimgb)
    python3 "$case_dir/generate_double_b_p_projection.py" \
      --characteristic "$characteristic" --engine slimgb --saturate-p > "$input.sing"
    input=$input.sing
    command_label="Singular -q < input.sing"
    set +e
    timeout --signal=TERM --kill-after=300 "$cap" \
      nice -n 5 Singular -q < "$input" > "$result" 2> "$stderr"
    rc=$?
    set -e
    ;;
  singular-p-sat-modstd)
    python3 "$case_dir/generate_double_b_p_projection.py" \
      --characteristic "$characteristic" --engine modstd --saturate-p > "$input.sing"
    input=$input.sing
    command_label="Singular modStd p-saturated projection"
    set +e
    timeout --signal=TERM --kill-after=300 "$cap" \
      nice -n 5 Singular -q < "$input" > "$result" 2> "$stderr"
    rc=$?
    set -e
    ;;
  singular-pq-slimgb)
    python3 "$case_dir/generate_double_b_projection.py" \
      --characteristic "$characteristic" --engine slimgb > "$input.sing"
    input=$input.sing
    command_label="Singular p,q projection"
    set +e
    timeout --signal=TERM --kill-after=300 "$cap" \
      nice -n 5 Singular -q < "$input" > "$result" 2> "$stderr"
    rc=$?
    set -e
    ;;
  singular-weighted-doubleb-slimgb)
    python3 "$case_dir/generate_weighted_projection.py" \
      --characteristic "$characteristic" --engine slimgb --double-b > "$input.sing"
    input=$input.sing
    command_label="Singular weighted double-B projection"
    set +e
    timeout --signal=TERM --kill-after=300 "$cap" \
      nice -n 5 Singular -q < "$input" > "$result" 2> "$stderr"
    rc=$?
    set -e
    ;;
  singular-weighted-doubleb-modstd)
    python3 "$case_dir/generate_weighted_projection.py" \
      --characteristic "$characteristic" --engine modstd --double-b > "$input.sing"
    input=$input.sing
    command_label="Singular modStd weighted double-B projection"
    set +e
    timeout --signal=TERM --kill-after=300 "$cap" \
      nice -n 5 Singular -q < "$input" > "$result" 2> "$stderr"
    rc=$?
    set -e
    ;;
  msolve-sat-elim-p-last|msolve-sat-elim-p-first)
    order=p-last
    # The saturated system has nine declared variables.  Eliminate the first
    # eight in p-last order so that the retained coordinate is exactly p.
    elim=8
    if [ "$backend" = "msolve-sat-elim-p-first" ]; then
      order=p-first
      elim=0
    fi
    python3 "$case_dir/generate_double_b_msolve.py" \
      --characteristic "$characteristic" --mode saturated --order "$order" > "$input.ms"
    input=$input.ms
    if [ "$elim" -eq 0 ]; then
      command_label="msolve saturated full solve order=$order"
    else
      command_label="msolve saturated elimination order=$order block=$elim"
    fi
    set +e
    if [ "$elim" -eq 0 ]; then
      timeout --signal=TERM --kill-after=300 "$cap" \
        nice -n 5 msolve -f "$input" -o "$result" -t 32 -v 2 -g 2 \
          -P 1 --random-seed 0 2> "$stderr"
    else
      timeout --signal=TERM --kill-after=300 "$cap" \
        nice -n 5 msolve -f "$input" -o "$result" -t 32 -v 2 -g 2 \
          -e "$elim" --random-seed 0 2> "$stderr"
    fi
    rc=$?
    set -e
    ;;
  *)
    echo "unknown backend: $backend" >&2
    exit 2
    ;;
esac

{
  echo "command=$command_label"
  echo "input_sha256=$(sha256sum "$input" | awk '{print $1}')"
  echo "input_bytes=$(wc -c < "$input" | tr -d ' ')"
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "exit_code=$rc"
  echo "result_bytes=$(wc -c < "$result" | tr -d ' ')"
  echo "stderr_bytes=$(wc -c < "$stderr" | tr -d ' ')"
  echo "result_sha256=$(sha256sum "$result" | awk '{print $1}')"
  echo "stderr_sha256=$(sha256sum "$stderr" | awk '{print $1}')"
  free -b | sed 's/^/end_free=/'
  if [ "$rc" -eq 0 ]; then echo "final_status=DONE"; else echo "final_status=FAILED"; fi
} >> "$meta"

exit "$rc"
