#!/bin/bash
# Wake only on terminal states. Diagnostics go to watch.log, never stdout.
set -u
DEST=/home/ubuntu/jc2/box/operative-sweep-20260905
MAP=$DEST/job-map.txt
LOG=$DEST/watch.log
SSHK=$HOME/.ssh/jc2-fleet
SSHO="-i $SSHK -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=8"
: > "$LOG"

fail_now() { echo "FAILED: $*" | tee -a "$LOG"; exit 1; }

while :; do
  all_done=1
  any_dead=0
  dead_why=""
  n=0
  done_n=0
  while read -r cid ip; do
    [ -z "${cid:-}" ] && continue
    n=$((n+1))
    remote=$(ssh -n $SSHO ubuntu@$ip "python3 - <<'PY'
import os, glob
cid='$cid'
p=os.path.expanduser('/home/ubuntu/jc2/box/operative-sweep-20260905/classes/%s/certificate.json'%cid)
print('CERT', int(os.path.isfile(p)))
running=0
for line in os.popen(\"ps -eo pid,cmd\").read().splitlines():
    if 'run.py run-class' in line and cid in line and 'python3' in line:
        running=1
print('RUNNING', running)
log=os.path.expanduser('~/operative-sweep-%s.log'%cid)
print('LOGBYTES', os.path.getsize(log) if os.path.isfile(log) else -1)
PY" 2>>"$LOG") || { echo "$(date -u +%H:%M:%S) ssh_fail $cid $ip" >> "$LOG"; all_done=0; continue; }
    cert=$(echo "$remote" | awk '/^CERT /{print $2}')
    run=$(echo "$remote" | awk '/^RUNNING /{print $2}')
    echo "$(date -u +%H:%M:%S) $cid ip=$ip cert=$cert run=$run" >> "$LOG"
    if [ "$cert" = 1 ]; then
      done_n=$((done_n+1))
    else
      all_done=0
      if [ "$run" != 1 ]; then
        any_dead=1
        dead_why="$dead_why $cid@$ip"
      fi
    fi
  done < "$MAP"
  if [ "$n" -lt 5 ]; then
    echo "$(date -u +%H:%M:%S) map_incomplete n=$n" >> "$LOG"
    sleep 30
    continue
  fi
  if [ "$any_dead" = 1 ]; then
    fail_now "worker job vanished without certificate:$dead_why"
  fi
  if [ "$all_done" = 1 ]; then
    echo "DONE: $done_n/$n certificates"
    exit 0
  fi
  sleep 30
done
