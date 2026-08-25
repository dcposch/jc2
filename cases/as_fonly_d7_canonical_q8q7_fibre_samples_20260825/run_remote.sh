#!/bin/sh
set -eu
TAG=${1:?tag required}
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/../.." && pwd)
RESULTS="$HERE/results_$TAG"
mkdir -p "$RESULTS"
START=$(date -u +%Y-%m-%dT%H:%M:%SZ)
i=0
while [ "$i" -lt 64 ]; do
  (
    BOOTSTRAP_JSON="$RESULTS/bootstrap_$(printf '%02d' "$i").json" \
    SAMPLE_INDEX_CANONICAL="$i" \
    OUTPUT_JSON="$RESULTS/sample_$(printf '%02d' "$i").json" \
    JC2_ROOT="$ROOT" timeout 43200 python3 "$HERE/compile_sample.py" \
      >"$RESULTS/sample_$(printf '%02d' "$i").stdout" \
      2>"$RESULTS/sample_$(printf '%02d' "$i").stderr"
  ) &
  i=$((i + 1))
done
wait
RESULTS_DIR="$RESULTS" AGGREGATE_JSON="$RESULTS/aggregate.json" \
  python3 "$HERE/aggregate.py" >"$RESULTS/aggregate.stdout" \
  2>"$RESULTS/aggregate.stderr"
END=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  echo "tag=$TAG"
  echo "host=$(hostname)"
  echo "start_utc=$START"
  echo "end_utc=$END"
  echo "python=$(python3 --version 2>&1)"
  echo "sample_count=64"
  echo "per_sample_timeout_seconds=43200"
  echo "rc=0"
} >"$RESULTS/run.meta"
(cd "$RESULTS" && find . -maxdepth 1 -type f ! -name OUTPUTS.sha256 -print0 \
  | sort -z | xargs -0 sha256sum) >"$RESULTS/OUTPUTS.sha256"

