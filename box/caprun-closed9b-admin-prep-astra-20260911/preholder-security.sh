#!/bin/bash
set -euo pipefail
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = JC2_INSTANCE_PLACEHOLDER
date -u '+PREHOLDER_SECURITY_START %Y-%m-%d %H:%M:%S.%N UTC'
jc2_base=/opt/jc2-closedchild-preflight9-20260911b
jc2_mount=/run/jc2-closedchild-preflight9-20260911b
jc2_channel=/run/jc2-closedchild-preflight9-20260911b-admission
test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
test ! -e /sys/fs/cgroup/system.slice/jc2-closedchild-preflight9-20260911b.service
for jc2_path in / /opt /run /var /var/lib /var/lib/jc2-closedchild-preflight9-20260911b /sys /sys/fs /sys/fs/cgroup /sys/fs/cgroup/system.slice /sys/fs/cgroup/cgroup.procs /sys/fs/cgroup/cgroup.threads /sys/fs/cgroup/cgroup.subtree_control /sys/fs/cgroup/system.slice/cgroup.procs /sys/fs/cgroup/system.slice/cgroup.threads /sys/fs/cgroup/system.slice/cgroup.subtree_control "$jc2_base" "$jc2_mount" "$jc2_mount/authority" "$jc2_mount/frozen" "$jc2_channel" "$jc2_channel/release.fifo"; do
 test "$(readlink -e "$jc2_path")" = "$jc2_path"
 test "$(stat -c %u "$jc2_path")" = 0
 jc2_mode=$(stat -c %a "$jc2_path")
 test "$((8#$jc2_mode & 8#022))" = 0
 stat -c 'PROTECTED_ACTUAL %d %i %u %g %a %n' "$jc2_path"
done
while IFS= read -r jc2_path; do
 test "$(stat -c '%u:%g:%a' "$jc2_path")" = 0:0:755
 stat -c 'INSTALLED_DIRECTORY %d %i %u %g %a %n' "$jc2_path"
done < <(find "$jc2_base" -type d -print)
while IFS= read -r jc2_path; do
 test "$(stat -c '%u:%g:%a' "$jc2_path")" = 0:0:444
 stat -c 'INSTALLED_FILE %d %i %u %g %a %n' "$jc2_path"
done < <(find "$jc2_base" -type f -print)
test -z "$(find "$jc2_base" -type l -print)"
test "$(stat -c '%u:%g:%a' "$jc2_mount/writer")" = 65534:65534:700
test "$(stat -c '%u:%g:%a' "$jc2_channel")" = 0:0:700
test "$(stat -c '%u:%g:%a' "$jc2_channel/release.fifo")" = 0:0:600
test -z "$(find "$jc2_mount" -type f -print)"
findmnt -rn -o TARGET,FSTYPE,FSROOT,OPTIONS --target "$jc2_mount"
findmnt -rn -o TARGET,FSTYPE,FSROOT,OPTIONS --target /sys/fs/cgroup
for jc2_ns in pid mnt cgroup user; do
 test "$(readlink "/proc/$$/ns/$jc2_ns")" = "$(readlink "/proc/1/ns/$jc2_ns")"
 printf 'ROOT_PID1_NAMESPACE %s %s\n' "$jc2_ns" "$(readlink "/proc/$$/ns/$jc2_ns")"
done
dpkg-query -W -f='ADMIN_EXTRA_PACKAGE ${Package} ${Version}\n' gawk diffutils libmagic1t64 libc-bin
date -u '+PREHOLDER_SECURITY_END %Y-%m-%d %H:%M:%S.%N UTC'
