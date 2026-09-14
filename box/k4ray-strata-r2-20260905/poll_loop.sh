#!/bin/bash
B=/home/ubuntu/jc2/box/k4ray-strata-r2-20260905
for i in $(seq 2 13); do
  sleep 900
  n=$(printf '%02d' $i)
  bash $B/collect.sh $n >/dev/null 2>&1
  echo "$(date -u +%H:%M:%SZ) poll $n done: $(awk 'NR>1' $B/status-$n.tsv | wc -l) payloads" >> $B/poll.log
done
