#!/bin/sh
set -eu
cd /home/ubuntu/f10-r1-exact-decision-validation-20260909
test "$(hostname)" = ip-172-30-0-72
test "$(/usr/bin/tr -d '\n' < /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
printf '%s\n' '79f6aa3d478bd14a03c27bc88f24c16d021162315d0a68a9e1c68c5a1504fafd  ROOT-REGISTRATION.json' | sha256sum --check
sha256sum --check INPUT.sha256
test ! -e batch.outer.stdout
test ! -e batch.outer.stderr
test "$(systemctl --user show jc2-f10-r1-exact-decision-validation-20260909.service --property=LoadState --value)" = not-found
date -u +%Y-%m-%dT%H:%M:%SZ
systemd-run --user --unit=jc2-f10-r1-exact-decision-validation-20260909 --property=WorkingDirectory=/home/ubuntu/f10-r1-exact-decision-validation-20260909 --property=RuntimeMaxSec=180s --property=KillMode=control-group --property=TimeoutStopSec=2s --property=StandardOutput=file:/home/ubuntu/f10-r1-exact-decision-validation-20260909/batch.outer.stdout --property=StandardError=file:/home/ubuntu/f10-r1-exact-decision-validation-20260909/batch.outer.stderr /usr/bin/python3 -I -B /home/ubuntu/f10-r1-exact-decision-validation-20260909/caller.py /home/ubuntu/f10-r1-exact-decision-validation-20260909/ROOT-REGISTRATION.json
systemctl --user show jc2-f10-r1-exact-decision-validation-20260909.service --property=LoadState,ActiveState,SubState,MainPID,Result,ExecMainStatus,ExecMainStartTimestamp,ExecMainExitTimestamp,ControlGroup
