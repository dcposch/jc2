#!/bin/bash
set -euo pipefail
test "$(id -u)" = 0
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0941baf1a7ff9131b
test -e /var/lib/jc2-stdlib-ready
date -u '+PHYSICAL_BEGIN %Y-%m-%d %H:%M:%S.%N UTC'
hostname
sed -n '1p' /proc/sys/kernel/random/boot_id
readlink /proc/self/ns/pid
stat -c '%d %u %g %a %n' /var/lib
findmnt -T /var/lib -n -o FSTYPE,SOURCE
test ! -e /opt/jc2-r2-fullunit-ready-20260910T1800
test ! -e /run/jc2-r2-fullunit-ready-20260910T1800
test ! -e /var/lib/jc2-r2-fullunit-ready-20260910T1800
systemctl show apt-daily.timer apt-daily-upgrade.timer unattended-upgrades.service -p Id -p ActiveState
install -d -o 1000 -g 1000 -m 0755 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/stage
date -u '+PHYSICAL_END %Y-%m-%d %H:%M:%S.%N UTC'

