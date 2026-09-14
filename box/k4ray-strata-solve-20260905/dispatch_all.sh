#!/bin/bash
# Parallel detached dispatch; each ssh is capped (the remote job survives via setsid).
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
LIST=${1:?}
while read ip K b pin gv; do
  ( timeout 25 bash $D/dispatch_k4.sh run $ip $K $b $pin 9000 1 2>&1 | head -1 ) &
  sleep 0.4
done < "$LIST"
wait
echo ALL_DISPATCH_ATTEMPTED
