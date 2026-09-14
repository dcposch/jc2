#!/bin/sh
set -eu
cd /home/ubuntu/f10-r1-exact-decision-run-20260909
test "$(hostname)" = ip-172-30-0-72
test "$(/usr/bin/tr -d '\n' < /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
printf '%s\n' 'c5e4e4a94ef1bb568992d7c31222a79cae26f262dde2d0272bdd421963d69437  ROOT-REGISTRATION.json' '203dd96e7c7137faf76645c6e05bea0123749b58a150d751e2bd1346baefe04a  INPUT.sha256' | sha256sum --check
sha256sum --check INPUT.sha256
test ! -e batch.outer.stdout
test ! -e batch.outer.stderr
test "$(systemctl --user show jc2-f10-r1-exact-decision-run-20260909.service --property=LoadState --value)" = not-found
date -u +%Y-%m-%dT%H:%M:%SZ
systemd-run --user --unit=jc2-f10-r1-exact-decision-run-20260909 --property=WorkingDirectory=/home/ubuntu/f10-r1-exact-decision-run-20260909 --property=RuntimeMaxSec=180s --property=KillMode=control-group --property=TimeoutStopSec=2s --property=StandardOutput=file:/home/ubuntu/f10-r1-exact-decision-run-20260909/batch.outer.stdout --property=StandardError=file:/home/ubuntu/f10-r1-exact-decision-run-20260909/batch.outer.stderr /usr/bin/python3 -I -B /home/ubuntu/f10-r1-exact-decision-run-20260909/caller.py /home/ubuntu/f10-r1-exact-decision-run-20260909/ROOT-REGISTRATION.json
systemctl --user show jc2-f10-r1-exact-decision-run-20260909.service --property=LoadState,ActiveState,SubState,MainPID,Result,ExecMainStatus,ExecMainStartTimestamp,ExecMainExitTimestamp,ControlGroup
