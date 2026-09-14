#!/usr/bin/env bash
# Wake only on terminal events for local I_light and fleet I_light jobs.
set -euo pipefail
LOGDIR=/tmp/k4ray-beta-strata-watch
mkdir -p "$LOGDIR"
diag=$LOGDIR/watch.diag
IP=172.30.0.127
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
LOCAL_ROOT=/home/ubuntu/jc2/box/k4ray-beta-strata-20260905
FLEET_TAGS="FLEET_K8_B7_Q0_Q FLEET_K8_B7_Q1_Q FLEET_K8_B8_Q0_P32003 FLEET_K9_B8_Q0_P32003"
LOCAL_TAGS="K7_B6_Q0_LIGHT_c0 K7_B6_Q1_LIGHT_c0"

emit() { echo "$1"; }

instance_alive() {
  aws ec2 describe-instances --region us-east-1 --instance-ids i-01de3f3912cb345f7 \
    --query 'Reservations[].Instances[].State.Name' --output text 2>>"$diag" | grep -q running
}

fleet_running() {
  ssh $SSHO ubuntu@$IP 'pgrep -c -f "strata_chart.py run FLEET_"' 2>>"$diag" || echo 0
}

local_done() {
  local tag=$1
  local f=$LOCAL_ROOT/runs/$tag/summary.json
  [[ -f $f ]] || return 1
  python3 - "$f" <<'PY'
import json,sys
s=json.load(open(sys.argv[1]))
print(s.get("verdict","UNKNOWN"))
PY
}

fleet_verdict() {
  local tag=$1
  ssh $SSHO ubuntu@$IP "python3 -c 'import json,os,sys
p=\"/home/ubuntu/jc2/box/k4ray-beta-strata-20260905/runs/$tag/summary.json\"
print(\"NONE\" if not os.path.exists(p) else json.load(open(p)).get(\"verdict\",\"UNKNOWN\"))'" 2>>"$diag"
}

# First pass: wait until every local K7 B6 job has a summary, or 20 more minutes.
deadline=$((SECONDS + 900))
local_pending=1
while (( SECONDS < deadline )); do
  all_local=1
  for t in $LOCAL_TAGS; do
    if ! local_done "$t" >/dev/null; then all_local=0; fi
  done
  if (( all_local )); then
    emit "ACTION_REQUIRED: local K7_B6 summaries ready"
    local_pending=0
    break
  fi
  sleep 30
done

# Fleet: wake when any job writes a summary, when all fleet python jobs exit, or instance dies.
prev_count=$(fleet_running | tail -1)
seen=""
while :; do
  instance_alive || { emit "FAILED: fleet instance i-01de3f3912cb345f7 not running"; exit 1; }
  count=$(fleet_running | tail -1)
  count=${count:-0}
  for t in $FLEET_TAGS; do
    v=$(fleet_verdict "$t" | tail -1)
    if [[ "$v" != "NONE" && "$v" != "" && "$seen" != *"|$t|"* ]]; then
      seen="$seen|$t|"
      emit "ACTION_REQUIRED: fleet $t verdict=$v"
    fi
  done
  if [[ "$count" == "0" ]]; then
    emit "DONE: fleet strata_chart processes exited"
    exit 0
  fi
  sleep 30
done
