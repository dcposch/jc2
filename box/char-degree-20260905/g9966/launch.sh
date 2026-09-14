#!/bin/bash
set -eu
cd /home/ubuntu/jc2
for branch in delta2 delta52; do
  mkdir -p box/char-degree-20260905/g9966/runs/${branch}_stage0
  nohup timeout 1800 python3 -u box/char-degree-20260905/g9966/run_characteristic.py --branch "$branch" --stage 0 --out box/char-degree-20260905/g9966/runs/${branch}_stage0 --gb-seconds 300 --term-cap 3000000 > box/char-degree-20260905/g9966/runs/${branch}_stage0/run.log 2>&1 &
  echo "$branch $!"
done
