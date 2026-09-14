#!/usr/bin/env bash
set -euo pipefail
ROOT=/home/ubuntu/jc2
OUT=$ROOT/box/gi70-longsolve-20260905
FLEET=$ROOT/ops/fleet/fleet.sh
IP=172.30.0.111
ID=i-0b29f3356aaf6ef81

mkdir -p "$OUT/dispatch-logs"
bash "$FLEET" pull "$IP" /home/ubuntu/jc2/box/gi70-longsolve-20260905/results/ "$OUT/results/"
for stem in gi70_a_exact_std gi70_b_guided_hilbert gi70_c_c1_msolve gi70_d_c1_slimgb; do
  bash "$FLEET" pull "$IP" "/home/ubuntu/${stem}.log" "$OUT/dispatch-logs/${stem}.log"
done
bash "$FLEET" run "$IP" \
  'date -u; free -b; ps -eo pid,ppid,pgid,etimes,rss,vsz,%mem,comm,args | awk '\''NR==1 || /Singular|msolve|run_guided.py|guided_gb.py/'\''' \
  > "$OUT/custody/remote-final-processes.log"
sha256sum "$OUT"/dispatch-logs/* "$OUT"/results/*/* 2>/dev/null \
  > "$OUT/custody/collected-top-level.sha256" || true

echo "COLLECTED_ONLY id=$ID ip=$IP utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
