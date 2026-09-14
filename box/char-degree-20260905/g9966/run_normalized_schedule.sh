#!/bin/bash
set -eu
cd /home/ubuntu/jc2
for stage in $(seq 0 8); do
  for branch in delta2 delta52; do
    printf '%s %s\n' "$branch" "$stage"
  done
done | xargs -n2 -P2 bash -c '
set -eu
branch=$1
stage=$2
ulimit -v 25165824
input=box/char-degree-20260905/g9966/normalized-inputs/${branch}_stage${stage}.json
out=box/char-degree-20260905/g9966/normalized-runs/${branch}_stage${stage}
mkdir -p "$out"
while [ ! -s "$input" ]; do sleep 2; done
python3 -u box/char-degree-20260905/g9966/run_normalized.py --input "$input" --out "$out" --timeout 1200 > "$out/driver.log" 2>&1
' lane99
