#!/bin/sh
set -eu
test "$(hostname)" = ip-172-30-0-72
test "$(tr -d '\n' < /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
systemctl --user show jc2-f10-r1-exact-decision-extended-run-20260909.service --property=LoadState,ActiveState,MainPID,ExecMainStatus,ExecMainStartTimestamp,ExecMainExitTimestamp
test "$(systemctl --user show jc2-f10-r1-exact-decision-extended-run-20260909.service --property=ActiveState --value)" = active
test "$(systemctl --user show jc2-f10-r1-exact-decision-extended-run-20260909.service --property=MainPID --value)" = 1312
walk_owned() {
  ps -p "$1" -o pid=,ppid=,pgid=,lstart=,etime=,time=,rss=,args=
  for child in $(pgrep -P "$1" || true); do walk_owned "$child"; done
}
walk_owned 1312
date -u +%Y-%m-%dT%H:%M:%SZ
