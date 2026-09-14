#!/bin/bash
# k4ray strata dispatch: detached per-stratum jobs on a fleet worker.
#   dispatch_k4.sh run  <IP> <K> <B> <PIN> [WATCHDOG] [CORES]
#   dispatch_k4.sh poll <IP> <K> <B> <PIN>
#   dispatch_k4.sh ps   <IP>
#   dispatch_k4.sh kill <IP>
set -uo pipefail
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
cmd=${1:?}; IP=${2:?}
case "$cmd" in
  run)  K=$3; B=$4; PIN=$5; WD=${6:-9000}; CO=${7:-2}; STEM="K${K}_B${B}_Q${PIN}"
        ssh $SSHO ubuntu@$IP "mkdir -p $D/logs && setsid bash -c 'stdbuf -oL bash $D/solve_stratum.sh $K $B $PIN $WD $CO > $D/logs/${STEM}.job.log 2>&1' </dev/null >/dev/null 2>&1 & echo LAUNCHED ${STEM} on $IP" ;;
  poll) K=$3; B=$4; PIN=$5; STEM="K${K}_B${B}_Q${PIN}"
        ssh $SSHO ubuntu@$IP "echo -n '${STEM} '; grep -ao 'MSJOB__RESULT.*' $D/logs/${STEM}.mod.log 2>/dev/null | tail -c 300; echo -n ' | Q:'; grep -aoE '\"verdict\": \"[A-Z_0-9]+\"|GG__[A-Z_]+|MemoryError|Killed' $D/logs/${STEM}.exactq.log 2>/dev/null | tail -1" ;;
  ps)   ssh $SSHO ubuntu@$IP 'echo -n "Singular="; pgrep -c Singular; echo -n "msolve="; pgrep -c msolve; free -g | sed -n 2p; uptime | sed "s/.*load/load/"' ;;
  kill) ssh $SSHO ubuntu@$IP "pkill -9 -f solve_stratum.sh; pkill -9 Singular; pkill -9 msolve; echo killed" ;;
esac
