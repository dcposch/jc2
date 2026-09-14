#!/usr/bin/env bash
# Lane-local detached dispatcher derived from the charged dispatch protocol.
set -uo pipefail
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=12"
D=/home/ubuntu/jc2/box/g9966-d2-precise-20260905
CMD=${1:?run, poll, or kill}; IP=${2:?private IP}
case "$CMD" in
  run)
    STEM=${3:?job stem}; OUTER_TIMEOUT=${4:-9300}
    ssh -n -f $SSHO ubuntu@"$IP" "cd $D; setsid bash -c 'timeout --signal=TERM --kill-after=30s $OUTER_TIMEOUT stdbuf -oL bash jobs/${STEM}_fleet.sh > \$HOME/${STEM}.log 2>&1; printf \"%s\\n\" \$? > \$HOME/${STEM}.rc' </dev/null >/dev/null 2>&1 & printf \"%s\\n\" \$! > \$HOME/${STEM}.launch.pid"
    sleep 1
    ssh $SSHO ubuntu@"$IP" "cat \$HOME/${STEM}.launch.pid" ;;
  poll)
    STEM=${3:?job stem}
    ssh $SSHO ubuntu@"$IP" "date -u +%Y-%m-%dT%H:%M:%SZ; echo LOG; tail -20 \$HOME/${STEM}.log 2>/dev/null || true; echo RC; cat \$HOME/${STEM}.rc 2>/dev/null || echo RUNNING; echo PROCESSES; ps -eo pid,ppid,etime,etimes,rss,vsz,%cpu,stat,cmd --sort=-rss | grep -E 'band_engine.py|${STEM}_fleet|Singular' | grep -v grep | head -30 || true" ;;
  kill)
    STEM=${3:?job stem}
    ssh $SSHO ubuntu@"$IP" "pkill -TERM -f '${STEM}_fleet.sh|band_engine.py' || true; sleep 5; pkill -KILL -f '${STEM}_fleet.sh|band_engine.py' || true" ;;
  *) echo "unknown command: $CMD" >&2; exit 2 ;;
esac
