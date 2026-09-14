#!/bin/bash
# DISABLED ROOT physical metadata for the future closed-child worker.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
 exit 2
fi
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-033947c617e8ad0e5
test -f /var/lib/jc2-stdlib-ready
for jc2_update_unit in apt-daily.timer apt-daily-upgrade.timer unattended-upgrades.service; do
 if systemctl is-active --quiet "$jc2_update_unit"; then exit 2; fi
done
date -u '+PHYSICAL_START %Y-%m-%d %H:%M:%S.%N UTC'
hostname
uname -r
systemctl --version
sed -n '1p' /proc/sys/kernel/random/boot_id
test "$(id -u)" = 0
for jc2_ns in pid mnt cgroup user; do
 jc2_current=$(readlink "/proc/$$/ns/$jc2_ns")
 jc2_init=$(readlink "/proc/1/ns/$jc2_ns")
 test "$jc2_current" = "$jc2_init"
 printf 'ROOT_INIT_NAMESPACE %s %s\n' "$jc2_ns" "$jc2_current"
done
readlink /proc/self/ns/pid
findmnt -n -o TARGET,FSTYPE,FSROOT,OPTIONS --target /sys/fs/cgroup
test "$(findmnt -rn -o TARGET --target /sys/fs/cgroup)" = /sys/fs/cgroup
test "$(findmnt -rn -o FSTYPE --target /sys/fs/cgroup)" = cgroup2
test "$(findmnt -rn -o FSROOT --target /sys/fs/cgroup)" = /
sed -n '1,8p' /proc/1/cgroup
# Equality with PID1 and the root mount is evidence, not an adversarial ROOT proof.
# ROOT separately checks ancestry, effective ACLs, delegation and no migration.
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
test ! -e /opt/jc2-closedchild-preflight9-20260911c
test ! -e /run/jc2-closedchild-preflight9-20260911c
test ! -e /var/lib/jc2-closedchild-preflight9-20260911c
test ! -e /home/ubuntu/jc2-closedchild-preflight9-20260911c
install -d -m 0755 /home/ubuntu/jc2-closedchild-preflight9-20260911c /home/ubuntu/jc2-closedchild-preflight9-20260911c/stage
test ! -e /run/jc2-closedchild-preflight9-20260911c-admission
test ! -L /run/jc2-closedchild-preflight9-20260911c-admission
date -u '+PHYSICAL_END %Y-%m-%d %H:%M:%S.%N UTC'
