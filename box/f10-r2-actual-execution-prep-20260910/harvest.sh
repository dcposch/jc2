#!/bin/bash
set -euo pipefail
test "$(id -u)" = 0
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 7ed95cce-3312-4f55-bc76-4e7f37c4cf7e
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(systemctl show jc2-f10-r2-20260910T1230.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-20260910T1230.service -p ControlPID --value)" = 0
test ! -e /proc/10121/stat
test ! -e /proc/10369/stat
test ! -e /proc/10370/stat
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-20260910T1230.service/cgroup.procs
sha256sum -c /home/ubuntu/jc2-r2-native-20260910T1230/stage/terminal.sha256
sha256sum -c /home/ubuntu/jc2-r2-native-20260910T1230/stage/native.sha256
sync -f /var/lib/jc2-r2-20260910T1230
date -u '+ROOT_TERMINAL_HASHES_SYNC %Y-%m-%d %H:%M:%S.%N UTC'
test ! -e /home/ubuntu/jc2-r2-native-20260910T1230/stage/terminal-artifacts.tar.gz
tar -czf /home/ubuntu/jc2-r2-native-20260910T1230/stage/terminal-artifacts.tar.gz -C / run/jc2-r2-20260910T1230 var/lib/jc2-r2-20260910T1230 opt/jc2-r2-20260910T1230
chmod 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/terminal-artifacts.tar.gz
sha256sum /home/ubuntu/jc2-r2-native-20260910T1230/stage/terminal-artifacts.tar.gz
systemctl stop jc2-r2-outer-term-20260910T1230.timer jc2-r2-outer-kill-20260910T1230.timer
systemctl show jc2-r2-outer-term-20260910T1230.timer jc2-r2-outer-kill-20260910T1230.timer -p ActiveState -p NextElapseUSecRealtime
date -u '+ROOT_TERMINAL_SYSTEM_TIMERS_CLOSED %Y-%m-%d %H:%M:%S.%N UTC'
