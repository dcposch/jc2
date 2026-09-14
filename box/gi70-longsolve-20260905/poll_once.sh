#!/usr/bin/env bash
set -u
ROOT=/home/ubuntu/jc2
OUT=$ROOT/box/gi70-longsolve-20260905
IP=${1:?worker IP required}
{
  echo "POLL_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  for stem in gi70_a_exact_std gi70_b_guided_hilbert gi70_c_c1_msolve gi70_d_c1_slimgb; do
    timeout 20 bash "$ROOT/ops/fleet/dispatch.sh" poll "$IP" "$stem" || true
  done
  bash "$ROOT/ops/fleet/fleet.sh" run "$IP" \
    'free -b; ps -eo pid,ppid,pgid,etimes,rss,vsz,%mem,comm,args | awk '\''NR==1 || /Singular|msolve|run_guided.py|guided_gb.py/'\''; for f in /home/ubuntu/jc2/box/gi70-longsolve-20260905/results/*/returncode.txt; do test -e "$f" && echo "RCFILE $f=$(cat "$f")"; done'
} | tee -a "$OUT/logs/polls.log"
