#!/bin/bash
set -euo pipefail
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0941baf1a7ff9131b
test "$(systemctl show jc2-f10-r2-fullunit-ready-20260910T1800.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-fullunit-ready-20260910T1800.service -p ControlPID --value)" = 0
test ! -e /proc/15158
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-fullunit-ready-20260910T1800.service
test ! -e /var/lib/jc2-r2-fullunit-ready-20260910T1800
test "$(find /run/jc2-r2-fullunit-ready-20260910T1800 -mindepth 1 -type f | wc -l)" = 2
test "$(sha256sum /run/jc2-r2-fullunit-ready-20260910T1800/outer.stdout | cut -d ' ' -f 1)" = 861eefb9232989a93447381f59aaa148750818927addd5a3e5a3a27caf880572
test ! -s /run/jc2-r2-fullunit-ready-20260910T1800/outer.stderr
sha256sum -c /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/stage/native.sha256 > /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/stage/refusal-native-postcheck.log
systemctl stop jc2-r2-fullunit-ready-outer-term-20260910T1800.timer jc2-r2-fullunit-ready-outer-kill-20260910T1800.timer
date -u '+FAILED_INITIALIZATION_ORIGINAL_SYSTEM_TIMERS_CLOSED %Y-%m-%d %H:%M:%S.%N UTC'
tar -czf /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/refusal-evidence.tar.gz -C / opt/jc2-r2-fullunit-ready-20260910T1800 run/jc2-r2-fullunit-ready-20260910T1800 home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/stage
tar -df /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/refusal-evidence.tar.gz -C /
sync /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/refusal-evidence.tar.gz
sha256sum /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/refusal-evidence.tar.gz
stat -c '%s' /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/refusal-evidence.tar.gz
date -u '+FAILED_INITIALIZATION_ARCHIVE_SYNCED %Y-%m-%d %H:%M:%S.%N UTC'
