#!/bin/bash
# Push frozen pipeline + 5 nunk<=100 classes; launch run-class detached (dispatch.sh pattern).
set -euo pipefail
ROOT=/home/ubuntu/jc2
DEST=$ROOT/box/operative-sweep-20260905
SSHK=$HOME/.ssh/jc2-fleet
SSHO="-i $SSHK -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
READY=$DEST/fleet-ready.txt
MAP=$DEST/job-map.txt
: > "$MAP"

IPS=()
while read -r id ip st; do
  IPS+=("$ip")
done < "$READY"
echo "workers: ${IPS[*]}"

push_one() {
  local ip=$1
  ssh $SSHO ubuntu@$ip "mkdir -p /home/ubuntu/jc2/box/lib /home/ubuntu/jc2/box/operative-sweep-20260905 /home/ubuntu/jc2/box/moh14-charts-20260905 /home/ubuntu/jc2/box/orderbasis-20260903"
  rsync -az -e "ssh $SSHO" \
    $ROOT/box/lib/census_sweep.py $ROOT/box/lib/guided_gb.py $ROOT/box/lib/split_window.py \
    ubuntu@$ip:/home/ubuntu/jc2/box/lib/
  rsync -az -e "ssh $SSHO" \
    $ROOT/box/moh14-charts-20260905/builder_fix.py \
    $ROOT/box/moh14-charts-20260905/sprime3_compiler.py \
    ubuntu@$ip:/home/ubuntu/jc2/box/moh14-charts-20260905/
  rsync -az -e "ssh $SSHO" \
    $ROOT/box/orderbasis-20260903/order_basis_full.py \
    ubuntu@$ip:/home/ubuntu/jc2/box/orderbasis-20260903/
  rsync -az -e "ssh $SSHO" \
    $ROOT/box/moh_skeleton_full.py \
    ubuntu@$ip:/home/ubuntu/jc2/box/moh_skeleton_full.py
  rsync -az -e "ssh $SSHO" \
    $DEST/run.py $DEST/inventory.json \
    ubuntu@$ip:/home/ubuntu/jc2/box/operative-sweep-20260905/
  rsync -az -e "ssh $SSHO" \
    $DEST/classes/ \
    ubuntu@$ip:/home/ubuntu/jc2/box/operative-sweep-20260905/classes/
  ssh $SSHO ubuntu@$ip 'python3 - <<"PY"
import sys
sys.path[:0]=["/home/ubuntu/jc2/box/lib","/home/ubuntu/jc2/box","/home/ubuntu/jc2/box/moh14-charts-20260905","/home/ubuntu/jc2/box/orderbasis-20260903"]
import census_sweep, builder_fix, moh_skeleton_full, sprime3_compiler, order_basis_full, guided_gb
print("imports_ok")
PY'
}

echo "PUSH"
for ip in "${IPS[@]}"; do
  echo "  push $ip"
  push_one "$ip"
done

CLASSES=(
  C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6
  C_n36m24_Mm18_3_5_ell1_s4_V5_18_9
  C_n36m24_Mm18_m4_5_ell1_s4_V5_18_6
  C_n36m24_Mm18_m4_5_ell1_s4_V7_18_6
  C_n36m24_Mm18_3_5_ell1_s4_V3_18_9
)

echo "LAUNCH"
i=0
for cid in "${CLASSES[@]}"; do
  ip="${IPS[$i]}"
  echo "$cid $ip" | tee -a "$MAP"
  # dispatch.sh pattern: setsid + timeout, survives SSH disconnect
  ssh $SSHO ubuntu@$ip "cd /home/ubuntu/jc2 && setsid bash -c 'timeout 1100 python3 -u box/operative-sweep-20260905/run.py run-class --class-id $cid --extract-timeout 300 --solve-timeout 300 --msolve > \$HOME/operative-sweep-${cid}.log 2>&1' </dev/null >/dev/null 2>&1 & echo LAUNCHED ${cid} pid=\$!"
  i=$((i+1))
done
echo "LAUNCHED_ALL"
cat "$MAP"
