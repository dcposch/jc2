#!/bin/bash
set -euo pipefail
test "$(id -u)" = 0
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 14ae48f0-89c1-4c56-b7f7-a1bb130ab768
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-09de82a596b4a6023
test "$(systemctl show jc2-f10-r2-controls-20260910T1400.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-controls-20260910T1400.service -p ControlPID --value)" = 0
test ! -e /proc/8395/stat
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-controls-20260910T1400.service/cgroup.procs
sha256sum -c /home/ubuntu/jc2-r2-controls-20260910T1400/stage/terminal.sha256
sha256sum -c /home/ubuntu/jc2-r2-controls-20260910T1400/stage/native.sha256 > /home/ubuntu/jc2-r2-controls-20260910T1400/stage/native-postcheck.log
while read -r jc2_alias jc2_target; do
 test "$(readlink -e "$jc2_alias")" = "$jc2_target"
done < <(awk '$1=="ALIAS" {print $2, $3}' /home/ubuntu/jc2-r2-controls-20260910T1400/stage/native.stdout)
while read -r jc2_dir; do
 jc2_expected=$(awk -v d="$jc2_dir" '$1=="ENTRY" && $2==d {print $3}' /home/ubuntu/jc2-r2-controls-20260910T1400/stage/native.stdout)
 jc2_actual=$(find "$jc2_dir" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)
 test "$jc2_expected" = "$jc2_actual"
done < <(awk '$1=="DIRECTORY" {print $5}' /home/ubuntu/jc2-r2-controls-20260910T1400/stage/native.stdout)
sync -f /var/lib/jc2-r2-controls-20260910T1400
date -u '+ROOT_TERMINAL_HASHES_SYNC %Y-%m-%d %H:%M:%S.%N UTC'
test ! -e /home/ubuntu/jc2-r2-controls-20260910T1400/stage/terminal-artifacts.tar.gz
tar -czf /home/ubuntu/jc2-r2-controls-20260910T1400/stage/terminal-artifacts.tar.gz -C / run/jc2-r2-controls-20260910T1400 var/lib/jc2-r2-controls-20260910T1400 opt/jc2-r2-controls-20260910T1400
tar --compare -zf /home/ubuntu/jc2-r2-controls-20260910T1400/stage/terminal-artifacts.tar.gz -C /
chmod 0444 /home/ubuntu/jc2-r2-controls-20260910T1400/stage/terminal-artifacts.tar.gz
sync -f /home/ubuntu/jc2-r2-controls-20260910T1400/stage/terminal-artifacts.tar.gz
sha256sum /home/ubuntu/jc2-r2-controls-20260910T1400/stage/terminal-artifacts.tar.gz
systemctl stop jc2-r2-controls-outer-term-20260910T1400.timer jc2-r2-controls-outer-kill-20260910T1400.timer
systemctl show jc2-r2-controls-outer-term-20260910T1400.timer jc2-r2-controls-outer-kill-20260910T1400.timer -p ActiveState -p NextElapseUSecRealtime
date -u '+ROOT_TERMINAL_SYSTEM_TIMERS_CLOSED %Y-%m-%d %H:%M:%S.%N UTC'
