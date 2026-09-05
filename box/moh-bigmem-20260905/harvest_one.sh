#!/usr/bin/env bash
# Pull compact solver artifacts from one worker into harvest/<stamp>/<ip>/.
set -euo pipefail
IP=${1:?ip}
STAMP=${2:-$(date -u +%H%M)}
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
DEST="/home/ubuntu/jc2/box/moh-bigmem-20260905/harvest/t${STAMP}/${IP}"
mkdir -p "$DEST"
rsync -az -e "ssh $SSHO" \
  --include='*/' \
  --include='*.stderr' --include='*.stdout' --include='*.log' --include='*.out' \
  --include='*.meta' --include='*.manifest.json' --include='*.status.json' \
  --include='*.emit.json' --include='*.rc' --include='*.rss.log' \
  --include='guided_gb_result.json' --include='*.err' --include='*.g2.out' \
  --exclude='*.ms' --exclude='*.sing' --exclude='*.tsv' --exclude='*.pyc' \
  --exclude='bin/' --exclude='circuit-src/' \
  ubuntu@${IP}:~/moh-bigmem-20260905/ "$DEST/tree/" || true
scp $SSHO ubuntu@${IP}:~/*.log "$DEST/" 2>/dev/null || true
ssh $SSHO ubuntu@${IP} "echo UTC=\$(date -u +%Y-%m-%dT%H:%M:%SZ); free -h | head -2; echo -n msolve=; pgrep -c -x msolve || echo 0; echo -n Singular=; pgrep -c Singular || echo 0; ps -eo pid,etime,rss,pcpu,cmd | awk 'NR==1||/msolve|Singular/' | head -20; echo '--- time ---'; grep -E 'Maximum resident|Elapsed \\(wall|Exit status|Command exited' ~/moh-bigmem-20260905/targets/*/*/*.g2.stderr ~/moh-bigmem-20260905/targets/*/guided/*.err 2>/dev/null | tail -20; echo '--- last F4/GG ---'; tail -3 ~/moh-bigmem-20260905/targets/*/*/*.g2.stderr 2>/dev/null; tail -8 ~/moh-bigmem-20260905/targets/*/guided/*.out 2>/dev/null" > "$DEST/poll.txt" || true
echo "HARVESTED $IP -> $DEST"
ls -la "$DEST" | head
