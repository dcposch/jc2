#!/bin/bash
# Parallel I_light screens on the fleet worker. Each job is setsid-detached.
set -euo pipefail
cd /home/ubuntu/jc2
export PYTHONUNBUFFERED=1
D=box/k4ray-beta-strata-20260905
L=$D/fleet-logs
mkdir -p "$L" "$D/runs"
PY="python3 -u $D/strata_chart.py run"

launch() {
  local tag="$1"; shift
  echo "LAUNCH $tag $*"
  setsid bash -c "timeout 2400 stdbuf -oL $PY $tag $* > $L/${tag}.log 2>&1" </dev/null >/dev/null 2>&1 &
  echo "pid=$! tag=$tag"
}

# Four concurrent jobs (4 cores each). Exact Q for the first extra K=8 stratum
# (both covers); modular screens for the next K=8 and first extra K=9.
launch FLEET_K8_B7_Q0_Q      8 7 --pin-index 0 --chars 0     --timeout 1800 --count-timeout 180 --cores 4
launch FLEET_K8_B7_Q1_Q      8 7 --pin-index 1 --chars 0     --timeout 1800 --count-timeout 180 --cores 4
launch FLEET_K8_B8_Q0_P32003 8 8 --pin-index 0 --chars 32003 --timeout 1200 --count-timeout 240 --cores 4
launch FLEET_K9_B8_Q0_P32003 9 8 --pin-index 0 --chars 32003 --timeout 1200 --count-timeout 300 --cores 4

echo LAUNCHED
pgrep -af strata_chart || true
