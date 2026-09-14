#!/bin/bash
# Pull every per-chart JSON payload, retry verdict and guided_gb summary from the fleet.
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=10"
mkdir -p $D/fleet-pull
for ip in 172.30.0.60 172.30.0.246 172.30.0.9 172.30.0.88; do
 ( mkdir -p $D/fleet-pull/$ip
   rsync -az --timeout=120 -e "ssh $SSHO" --include='*/' --include='*.json' --include='*.retry.log' \
     --include='*.msout' --include='summary.json' --exclude='*' \
     ubuntu@$ip:$D/ $D/fleet-pull/$ip/ 2>/dev/null
   timeout 60 ssh $SSHO ubuntu@$ip "grep -h -ao 'MSJOB__RESULT .*' $D/logs/*.mod.log $D/logs/*.exactq_ms.log 2>/dev/null" > $D/fleet-pull/$ip.msjob.jsonl 2>/dev/null
   timeout 60 ssh $SSHO ubuntu@$ip "cat /tmp/rt.out 2>/dev/null | grep -a '^RETRY '" > $D/fleet-pull/$ip.retry.txt 2>/dev/null
   timeout 60 ssh $SSHO ubuntu@$ip "for f in $D/logs/*.exactq.log; do s=\$(basename \$f .exactq.log); v=\$(grep -ao '\"verdict\": \"[A-Z_0-9]*\"' \$f | tail -1 | sed 's/.*: \"//;s/\"//'); m=\$(grep -aoE 'GG__[A-Z_]+ main [-0-9]+' \$f | tail -3 | tr '\n' ';'); r=\$(grep -ao 'EXACTQ_RC=[0-9]*' \$f|tail -1); echo \"\$s|\${v:-NONE}|\${m}|\${r}\"; done" > $D/fleet-pull/$ip.guidedgb.txt 2>/dev/null
 ) &
done
wait
echo FINAL_COLLECT_DONE
