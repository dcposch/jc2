#!/bin/sh
set -eu
cd /home/ubuntu/f10-r1-exact-decision-extended-run-20260909
test "$(hostname)" = ip-172-30-0-72
test "$(/usr/bin/tr -d '\n' < /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
printf '%s\n' '845c1066ad2a85f21b9ead81dc1de926c47b6cc5fbb5e669f37a576e7fc834ff  ROOT-REGISTRATION.json' 'e65e934b48bba96e2263ef02cb8fec4aa2fed7c297c6df039954905ffa5ea221  INPUT.sha256' | sha256sum --check
sha256sum --check INPUT.sha256
test ! -e batch.outer.stdout
test ! -e batch.outer.stderr
test "$(systemctl --user show jc2-f10-r1-exact-decision-extended-run-20260909.service --property=LoadState --value)" = not-found
date -u +%Y-%m-%dT%H:%M:%SZ
systemd-run --user --unit=jc2-f10-r1-exact-decision-extended-run-20260909 --property=WorkingDirectory=/home/ubuntu/f10-r1-exact-decision-extended-run-20260909 --property=RuntimeMaxSec=780s --property=KillMode=control-group --property=TimeoutStopSec=2s --property=StandardOutput=file:/home/ubuntu/f10-r1-exact-decision-extended-run-20260909/batch.outer.stdout --property=StandardError=file:/home/ubuntu/f10-r1-exact-decision-extended-run-20260909/batch.outer.stderr /usr/bin/python3 -I -B /home/ubuntu/f10-r1-exact-decision-extended-run-20260909/caller.py /home/ubuntu/f10-r1-exact-decision-extended-run-20260909/ROOT-REGISTRATION.json
systemctl --user show jc2-f10-r1-exact-decision-extended-run-20260909.service --property=LoadState,ActiveState,SubState,MainPID,Result,ExecMainStatus,ExecMainStartTimestamp,ExecMainExitTimestamp,ControlGroup
