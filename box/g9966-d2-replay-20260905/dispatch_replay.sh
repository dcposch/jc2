#!/bin/bash
# Detached fleet dispatch for the D2-floor replay (same protocol as
# ops/fleet/dispatch.sh: setsid + timeout + poll).  The charged dispatch.sh
# is hardcoded to box/moh14-charts-20260905; this clone points at this box.
#   dispatch_replay.sh run  <IP> <STEM> [timeout]
#   dispatch_replay.sh poll <IP> <STEM>
#   dispatch_replay.sh kill <IP>
set -uo pipefail
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
D=/home/ubuntu/g9966-d2-replay
cmd=${1:?}; IP=${2:?}
case "$cmd" in
  run)  STEM=$3; TO=${4:-12000}
        ssh $SSHO ubuntu@$IP "cd $D && setsid bash -c 'timeout $TO stdbuf -oL bash jobs/${STEM}_fleet.sh > \$HOME/${STEM}.log 2>&1' </dev/null >/dev/null 2>&1 & echo LAUNCHED ${STEM} pid=\$!"
        ;;
  poll) STEM=$3
        ssh $SSHO ubuntu@$IP "echo '--- ${STEM} tail:'; tail -8 \$HOME/${STEM}.log 2>/dev/null; echo -n 'VERDICT: '; grep -aoE 'GG_UNIT|GG_NONUNIT|DEAD|COUNTING-BOUND|dimension *= *[-0-9]+|Killed|error:|Error|PROGRESS [^ ]+' \$HOME/${STEM}.log 2>/dev/null | tail -3 | tr '\n' '|'; echo; echo -n 'RUNNING: '; pgrep -c -f replay_engine.py || true"
        ;;
  kill) ssh $SSHO ubuntu@$IP 'pkill -9 -f replay_engine.py; pkill -9 Singular; echo killed' ;;
esac
