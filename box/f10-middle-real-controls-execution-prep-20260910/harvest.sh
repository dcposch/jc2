#!/bin/bash
set -euo pipefail
test "$(id -u)" = 0
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 5ef9c85d-97e1-46ae-b551-18039ef4db2d
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(systemctl show jc2-f10-real-controls-20260910T1204.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-real-controls-20260910T1204.service -p ControlPID --value)" = 0
test ! -e /proc/8439/stat
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-real-controls-20260910T1204.service/cgroup.procs
sha256sum -c /home/ubuntu/jc2-real-controls-native-20260910T1204/stage/terminal.sha256
sha256sum -c /home/ubuntu/jc2-real-controls-native-20260910T1204/stage/native.sha256
sync -f /var/lib/jc2-real-controls-20260910T1204
date -u '+ROOT_TERMINAL_HASHES_SYNC %Y-%m-%d %H:%M:%S.%N UTC'
test ! -e /home/ubuntu/jc2-real-controls-native-20260910T1204/stage/terminal-artifacts.tar.gz
tar -czf /home/ubuntu/jc2-real-controls-native-20260910T1204/stage/terminal-artifacts.tar.gz -C / run/jc2-real-controls-20260910T1204 var/lib/jc2-real-controls-20260910T1204 opt/jc2-real-controls-20260910T1204
chmod 0444 /home/ubuntu/jc2-real-controls-native-20260910T1204/stage/terminal-artifacts.tar.gz
sha256sum /home/ubuntu/jc2-real-controls-native-20260910T1204/stage/terminal-artifacts.tar.gz
systemctl stop jc2-real-controls-outer-term-20260910T1204.timer jc2-real-controls-outer-kill-20260910T1204.timer
systemctl show jc2-real-controls-outer-term-20260910T1204.timer jc2-real-controls-outer-kill-20260910T1204.timer -p ActiveState -p NextElapseUSecRealtime
date -u '+ROOT_TERMINAL_SYSTEM_TIMERS_CLOSED %Y-%m-%d %H:%M:%S.%N UTC'
