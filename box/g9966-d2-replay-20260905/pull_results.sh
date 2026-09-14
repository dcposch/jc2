#!/usr/bin/env bash
set -euo pipefail
IP=172.30.0.163
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$HERE/runs/delta2" "$HERE/runs/delta52" "$HERE/fleet-logs"
bash /home/ubuntu/jc2/ops/fleet/fleet.sh pull "$IP" \
  /home/ubuntu/g9966-d2-replay/runs/delta2/ "$HERE/runs/delta2/"
bash /home/ubuntu/jc2/ops/fleet/fleet.sh pull "$IP" \
  /home/ubuntu/g9966-d2-replay/runs/delta52/ "$HERE/runs/delta52/"
bash /home/ubuntu/jc2/ops/fleet/fleet.sh pull "$IP" \
  /home/ubuntu/d2s4.log "$HERE/fleet-logs/d2s4.log" || true
bash /home/ubuntu/jc2/ops/fleet/fleet.sh pull "$IP" \
  /home/ubuntu/d52s8.log "$HERE/fleet-logs/d52s8.log" || true
echo PULLED
ls -la "$HERE/runs/delta2" "$HERE/runs/delta52" "$HERE/fleet-logs"
