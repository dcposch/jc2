#!/bin/bash
# ROOT-authorized metadata only on the exact future r3 worker (DISABLED template).
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
 exit 2
fi
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = JC2_INSTANCE_PLACEHOLDER
test -f /var/lib/jc2-stdlib-ready
for jc2_update_unit in apt-daily.timer apt-daily-upgrade.timer unattended-upgrades.service; do
 if systemctl is-active --quiet "$jc2_update_unit"; then exit 2; fi
done
date -u '+PHYSICAL_START %Y-%m-%d %H:%M:%S.%N UTC'
hostname
uname -r
systemctl --version
sed -n '1p' /proc/sys/kernel/random/boot_id
readlink /proc/self/ns/pid
stat -c '%d %F %u %g %a %n' /var/lib /usr/bin/python3.12 /usr/bin/setpriv
findmnt -n -o SOURCE,FSTYPE,OPTIONS --target /var/lib
readlink -e /usr/bin/python3.12 /usr/bin/setpriv /usr/bin/chrt
sha256sum /usr/bin/python3.12 /usr/bin/setpriv
getent passwd 65534
test ! -e /usr/lib/python312.zip
test ! -L /usr/lib/python312.zip
stat -fc '%T' /sys/fs/cgroup
sed -n '1,5p' /sys/fs/cgroup/cgroup.controllers
sed -n '1p' /proc/sys/kernel/sched_cfs_bandwidth_slice_us
test ! -e /opt/jc2-r3-necessaryrows-20260911a
test ! -e /run/jc2-r3-necessaryrows-20260911a
test ! -e /var/lib/jc2-r3-necessaryrows-20260911a
test ! -e /home/ubuntu/jc2-r3-necessaryrows-20260911a
install -d -m 0755 /home/ubuntu/jc2-r3-necessaryrows-20260911a /home/ubuntu/jc2-r3-necessaryrows-20260911a/stage
date -u '+PHYSICAL_END %Y-%m-%d %H:%M:%S.%N UTC'
