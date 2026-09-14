#!/usr/bin/env bash
set -u
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=8"
echo "POLL utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
declare -A JOBS=(
  [172.30.0.183]=m12_union.msolve.log
  [172.30.0.202]=v38.msolve.log
  [172.30.0.108]=m15.msolve.log
  [172.30.0.190]=v18.msolve.log
  [172.30.0.121]=m12_union.guided.log
  [172.30.0.55]=v38.guided.log
  [172.30.0.45]=m15.guided.log
  [172.30.0.125]=v18.guided.log
)
for ip in 172.30.0.183 172.30.0.202 172.30.0.108 172.30.0.190 \
          172.30.0.121 172.30.0.55 172.30.0.45 172.30.0.125; do
  log=${JOBS[$ip]}
  echo "----- $ip $log -----"
  ssh $SSHO ubuntu@$ip "echo -n 'load: '; uptime | sed 's/.*load/load/'; echo -n 'mem: '; awk '/MemAvailable/{printf \"avail_GiB=%.1f\\n\", \$2/1024/1024}' /proc/meminfo; echo -n 'msolve: '; pgrep -c -x msolve || echo 0; echo -n 'Singular: '; pgrep -c Singular || echo 0; echo '--- tail ---'; tail -8 \$HOME/$log 2>/dev/null || echo NO_LOG; echo -n 'VERDICT: '; grep -aoE 'UNIT_IDEAL_CHAR0|NONUNIT_POSDIM|NONUNIT_DIM0|UNIT_MODULAR_ONLY|TIMEOUT_NO_VERDICT|PARSED_STATUS.*|GUIDED_FINAL.*|PIPELINE_.*PARSED=.*|NATIVE_DONE|ALLOCAT|Killed|EMIT_FAIL' \$HOME/$log 2>/dev/null | tail -3"
done
