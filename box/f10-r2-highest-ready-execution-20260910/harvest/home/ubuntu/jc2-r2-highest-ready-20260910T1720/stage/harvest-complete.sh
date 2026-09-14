#!/bin/bash
# ROOT completion after harvest's wrong historical timer suffix; no science rerun.
set -euo pipefail
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-05b82c8e457c586ce
test "$(tr -d '\n' < /proc/sys/kernel/random/boot_id)" = 6e13db88-d1a2-45cd-aa1b-028d8e070589
test ! -e /proc/9533
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-highest-ready-20260910T1720.service
cd /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage
test "$(wc -l < terminal-files-recheck.log)" = 281
test "$(wc -l < installed-postcheck.log)" = 21
test "$(wc -l < native-postcheck.log)" = 1226
test ! -s native-post.stderr
cmp <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native-post.stdout)
systemctl stop jc2-r2-highest-ready-outer-term-20260910T1720.timer jc2-r2-highest-ready-outer-kill-20260910T1720.timer
systemctl show jc2-r2-highest-ready-outer-term-20260910T1720.timer jc2-r2-highest-ready-outer-kill-20260910T1720.timer -p Id -p ActiveState -p SubState
date -u '+ORIGINAL_SYSTEM_TIMERS_CLOSED %FT%T.%NZ'
sync -f /var/lib/jc2-r2-highest-ready-20260910T1720
test ! -e /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
tar -czpf /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz -C / opt/jc2-r2-highest-ready-20260910T1720 run/jc2-r2-highest-ready-20260910T1720 var/lib/jc2-r2-highest-ready-20260910T1720 home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage
tar -dzf /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz -C /
chmod 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
sync -f /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
sha256sum /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
stat --printf='ARCHIVE_BYTES %s\n' /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
date -u '+HARVEST_ARCHIVE_SYNCED %FT%T.%NZ'
