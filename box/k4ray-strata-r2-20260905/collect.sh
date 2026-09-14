#!/bin/bash
# collect.sh <tag>  -- pull payloads from the three workers, build a status TSV
B=/home/ubuntu/jc2/box/k4ray-strata-r2-20260905
TAG=${1:-x}
for ip in 172.30.0.11 172.30.0.119 172.30.0.5; do
  mkdir -p $B/pull/$ip
  bash /home/ubuntu/jc2/ops/fleet/fleet.sh pull $ip '/home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve/*.json' $B/pull/$ip/ >/dev/null 2>&1
  bash /home/ubuntu/jc2/ops/fleet/fleet.sh run $ip "free -g|sed -n 2p; echo -n 'procs='; pgrep -c -f r2_solve.py; echo -n 'sing='; pgrep -c Singular; echo -n 'ms='; pgrep -c msolve" 2>/dev/null | tr '\n' ' ' >> $B/health-$TAG.txt
  echo " <- $ip" >> $B/health-$TAG.txt
done
python3 $B/status.py > $B/status-$TAG.tsv
for ip in 172.30.0.11 172.30.0.119 172.30.0.5; do
  bash /home/ubuntu/jc2/ops/fleet/fleet.sh pull $ip '/home/ubuntu/jc2/box/k4ray-strata-r2-20260905/msolve/*.ph2.json' /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/pull/$ip/ >/dev/null 2>&1
done
python3 /home/ubuntu/jc2/box/k4ray-strata-r2-20260905/merge.py > /dev/null 2>&1
