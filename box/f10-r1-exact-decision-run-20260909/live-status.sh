#!/bin/sh
set -eu
jc2_decision_unit=jc2-f10-r1-exact-decision-run-20260909.service
systemctl --user show "$jc2_decision_unit" --property=LoadState,ActiveState,SubState,MainPID,Result,ExecMainStatus,ExecMainStartTimestamp,ExecMainExitTimestamp
if test "$(systemctl --user show "$jc2_decision_unit" --property=ActiveState --value)" = active && test "$(systemctl --user show "$jc2_decision_unit" --property=MainPID --value)" = 1635; then
  ps -p 1635 -o pid=,ppid=,pgid=,stat=,args=
  for jc2_decision_child in $(pgrep -P 1635); do
    ps -p "$jc2_decision_child" -o pid=,ppid=,pgid=,stat=,args=
    for jc2_decision_grandchild in $(pgrep -P "$jc2_decision_child" || true); do
      ps -p "$jc2_decision_grandchild" -o pid=,ppid=,pgid=,stat=,args=
      for jc2_decision_engine in $(pgrep -P "$jc2_decision_grandchild" || true); do
        ps -p "$jc2_decision_engine" -o pid=,ppid=,pgid=,stat=,args=
      done
    done
  done
fi
date -u +%Y-%m-%dT%H:%M:%SZ
