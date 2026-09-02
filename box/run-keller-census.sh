#!/usr/bin/env bash
set -euo pipefail

repo=${1:?usage: run-keller-census /absolute/path/to/jc2}
source_py="$repo/box/keller_cluster_census.py"
census_root="$HOME/cluster_census"
mkdir -p "$census_root"
census_out=$(mktemp -d "$census_root/run-20260902.XXXXXX")
rows_dir="$census_out/rows"
mkdir -p "$rows_dir"
job_deadline=$(( $(date +%s) + 43200 ))
printf '%s\n' "$census_out" > "$census_out/RUN_DIRECTORY"
census_py="$census_out/keller_cluster_census.py"
install -m 0755 "$source_py" "$census_py"
sha256sum "$census_py" > "$census_out/ENGINE_SHA256"

python3.12 "$census_py" self-test > "$census_out/self-test.json"
python3.12 "$census_py" plan \
  --n-min 2 --n-max 8 --d-min 2 --d-max 200 \
  --window legacy-inclusive --f-cap unbounded > "$census_out/plan.json"

: > "$census_out/cells.txt"
for N in $(seq 2 8); do
  for D in $(seq 2 200); do
    printf '%s %s\n' "$N" "$D" >> "$census_out/cells.txt"
  done
done

export census_py rows_dir
run_cell() {
  N=$1
  D=$2
  set +e
  python3.12 "$census_py" census \
    --N "$N" --D "$D" --window legacy-inclusive --f-cap unbounded \
    --max-states 250000 --deadline-seconds 39600 \
    --output "$rows_dir/$(printf 'N%03d-D%03d.jsonl' "$N" "$D")"
  cell_rc=$?
  set -e
  case "$cell_rc" in
    0|2) return 0 ;;
    *) return "$cell_rc" ;;
  esac
}
export -f run_cell

set +e
parallel_budget=$(( job_deadline - $(date +%s) - 1800 ))
if (( parallel_budget <= 0 )); then
  printf '%s\n' 'no worker budget remained after preflight' >&2
  exit 75
fi
timeout --signal=TERM --kill-after=180 "${parallel_budget}s" \
  parallel --jobs 48 --colsep ' ' --joblog "$census_out/joblog.tsv" \
  run_cell {1} {2} :::: "$census_out/cells.txt"
parallel_rc=$?
set -e
printf '%s\n' "$parallel_rc" > "$census_out/parallel.rc"

set +e
merge_budget=$(( job_deadline - $(date +%s) ))
if (( merge_budget > 0 )); then
  timeout --signal=TERM --kill-after=30 "${merge_budget}s" \
    python3.12 "$census_py" merge \
      --n-min 2 --n-max 8 --d-min 2 --d-max 200 \
      --expected-window legacy-inclusive --expected-f-cap unbounded \
      --expected-profile-mode H2-common-n \
      "$rows_dir" --output "$census_out/all.jsonl"
  merge_rc=$?
else
  merge_rc=124
fi
set -e
printf '%s\n' "$merge_rc" > "$census_out/merge.rc"
hash_budget=$(( job_deadline - $(date +%s) ))
if (( hash_budget > 0 )); then
  timeout "${hash_budget}s" bash -c '
    find "$1" -type f \( -name "*.json" -o -name "*.jsonl" -o -name "*.py" \) -print0 \
      | sort -z | xargs -0 sha256sum > "$1/SHA256SUMS"
  ' _ "$census_out"
fi
printf 'run directory: %s\n' "$census_out"
```

Interpretation of return codes is deliberate: `0` means complete, `2` means
well-formed but incomplete, `64` means invalid input or data, `70` means an
internal/resource failure with no complete result emitted, and `124` is the
outer timeout.  Missing worker files and return code 2 must not be converted to
zero counts.  When `all.jsonl` exists, its last record is the only box-wide
“smallest D” table.

