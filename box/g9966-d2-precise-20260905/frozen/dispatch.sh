#!/bin/bash
# jc2 fleet job dispatch: run a chart job DETACHED on a worker (survives SSH
# disconnect via setsid), then poll for the guided_gb verdict.
#   dispatch.sh run  <IP> <CLASS> <STEM> [timeout]   # detached launch
#   dispatch.sh poll <IP> <STEM>                      # tail + verdict
#   dispatch.sh kill <IP>                             # kill all worker jobs
set -uo pipefail
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
D=/home/ubuntu/jc2/box/moh14-charts-20260905
cmd=${1:?}; IP=${2:?}
case "$cmd" in
  run)  CLASS=$3; STEM=$4; TO=${5:-6000}
        ssh $SSHO ubuntu@$IP "cd $D && setsid bash -c 'timeout $TO stdbuf -oL bash classes/$CLASS/jobs/${STEM}_fleet.sh > \$HOME/${STEM}.log 2>&1' </dev/null >/dev/null 2>&1 & echo LAUNCHED ${STEM} pid=\$!"
        ;;
  poll) STEM=$3
        ssh $SSHO ubuntu@$IP "echo '--- ${STEM} tail:'; tail -3 \$HOME/${STEM}.log 2>/dev/null; echo -n 'VERDICT: '; grep -aoE 'GG__[A-Z_]+|dimension *[=:] *[-0-9]+|reduce\\(1\\)=0|Killed|error:|Error' \$HOME/${STEM}.log 2>/dev/null | tail -1; echo -n 'RUNNING: '; pgrep -c Singular"
        ;;
  kill) ssh $SSHO ubuntu@$IP 'pkill -9 -f fleet.sh; pkill -9 Singular; echo killed' ;;
esac
