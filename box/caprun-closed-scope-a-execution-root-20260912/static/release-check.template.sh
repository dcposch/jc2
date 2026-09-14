#!/bin/bash
# DISABLED/UNBOUND; separately invoked fixed late-DATA release guard.
set -euo pipefail
grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0" && exit 2
test "$#" = 5
test "$1" = ROOT_RELEASE_EXACT_PREFLIGHT9_ONLY
test "$(id -u)" = 0
jc2_pid=$2; jc2_start=$3; jc2_inv=$4; jc2_regsha=$5
[[ "$jc2_pid" =~ ^[1-9][0-9]{0,9}$ && "$jc2_start" =~ ^[1-9][0-9]{0,14}$ && "$jc2_inv" =~ ^[0-9a-f]{32}$ && "$jc2_regsha" =~ ^[0-9a-f]{64}$ ]]
jc2_unit='jc2-closedchild-preflight9-20260912a.service'; jc2_cgroup='/sys/fs/cgroup/system.slice/jc2-closedchild-preflight9-20260912a.service'; jc2_base='/opt/jc2-closedchild-preflight9-20260912a'; jc2_stage='/opt/jc2-closedchild-preflight9-20260912a-final-stage'; jc2_stop='1789203720'; jc2_fifo='/run/jc2-closedchild-preflight9-20260912a-admission/release.fifo'
test "$(date -u +%s)" -lt "$((jc2_stop - 5))"
test "$(tr -d '\n' </sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' </sys/class/dmi/id/board_asset_tag)" = 'JC2_INSTANCE_ID_PLACEHOLDER'
test "$(hostname)" = 'JC2_HOSTNAME_PLACEHOLDER'; test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'JC2_BOOT_ID_PLACEHOLDER'
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p ActiveState --value)" = active
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_pid"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p InvocationID --value)" = "$jc2_inv"
test "$(sed 's/^.*) //' /proc/"$jc2_pid"/stat | awk '{print $20}')" = "$jc2_start"
test "$(readlink /proc/$jc2_pid/ns/pid)" = 'JC2_PID_NAMESPACE_PLACEHOLDER'
for jc2_ns in pid mnt cgroup user; do
 test "$(readlink /proc/$$/ns/$jc2_ns)" = "$(readlink /proc/1/ns/$jc2_ns)"
 test "$(readlink /proc/$$/ns/$jc2_ns)" = "$(readlink /proc/$jc2_pid/ns/$jc2_ns)"
done
test "$(tr '\0' '\n' </proc/"$jc2_pid"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\n/opt/jc2-closedchild-preflight9-20260912a/admin/holder.py'
test "$(readlink /proc/"$jc2_pid"/exe)" = /usr/bin/python3.12
test "$(findmnt -rn -o TARGET --target /sys/fs/cgroup)" = /sys/fs/cgroup
test "$(findmnt -rn -o FSTYPE --target /sys/fs/cgroup)" = cgroup2
test "$(findmnt -rn -o FSROOT --target /sys/fs/cgroup)" = /
test "$(readlink -e "$jc2_cgroup")" = "$jc2_cgroup"
test "$(stat -c '%u:%g:%a' "$jc2_cgroup")" = 0:0:755
test "$(sed -n '1p' "$jc2_cgroup/cpu.max.burst")" = 0
test "$(sed -n '1p' "$jc2_cgroup/memory.swap.max")" = 0
test "$(sed -n '1p' "$jc2_cgroup/cgroup.type")" = domain
test -z "$(<"$jc2_cgroup/cgroup.subtree_control")"
for jc2_iface in cgroup.procs cgroup.threads cgroup.subtree_control; do
 test "$(stat -c '%u:%g:%A' "$jc2_cgroup/$jc2_iface")" = "0:0:-rw-r--r--"
done
test "$(sed -n '1p' /proc/$jc2_pid/cgroup)" = "0::${jc2_cgroup#/sys/fs/cgroup}"
test "$(sed -n '1,4p' "$jc2_cgroup/cgroup.procs")" = "$jc2_pid"; test -z "$(</proc/$jc2_pid/task/$jc2_pid/children)"
test "$(sed -n '1p' "$jc2_cgroup/cpu.max")" = '6900 10000'; test "$(sed -n '1p' "$jc2_cgroup/memory.max")" = 8589934592; test "$(sed -n '1p' "$jc2_cgroup/pids.max")" = 32
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p Delegate --value)" = no
jc2_hz=$(getconf CLK_TCK); read -r jc2_up _ </proc/uptime; jc2_up=${jc2_up%%.*}
[[ "$jc2_hz" =~ ^[1-9][0-9]*$ && "$jc2_up" =~ ^[0-9]+$ ]]
test "$((jc2_up - jc2_start / jc2_hz))" -ge 0; test "$((jc2_up - jc2_start / jc2_hz))" -lt 120
test "$(sha256sum "$jc2_base/metadata/ROOT-REGISTRATION.json" | cut -d' ' -f1)" = "$jc2_regsha"
test "$(stat -c '%u:%g:%a' "$jc2_base/metadata/ROOT-REGISTRATION.json")" = 0:0:444
cd "$jc2_stage"
sha256sum --strict -c FINAL-INSTALL-INPUTS.sha256
sha256sum --strict -c native.sha256
test "$(sha256sum ROOT-REGISTRATION.json | cut -d' ' -f1)" = "$jc2_regsha"
cmp ROOT-REGISTRATION.json "$jc2_base/metadata/ROOT-REGISTRATION.json"
cmp ROOT-EXECUTION-CARD.md "$jc2_base/metadata/ROOT-EXECUTION-CARD.md"
test "$(stat -c '%u:%g:%a' "$jc2_base/metadata/ROOT-EXECUTION-CARD.md")" = 0:0:444
jq -r '.pins | to_entries[] | "\(.value)  \(.key)"' ROOT-REGISTRATION.json | sha256sum --strict -c -
test -z "$(find /run/jc2-closedchild-preflight9-20260912a/authority /run/jc2-closedchild-preflight9-20260912a/frozen /run/jc2-closedchild-preflight9-20260912a/writer -mindepth 1 -maxdepth 1 -print -quit)"
test "$(find "$jc2_cgroup" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | LC_ALL=C sort)" = $'dummy\nrefuse-caps\nrefuse-hash\nrefuse-inventory\nrefuse-source\nrefuse-status\nstartup-check\nstartup-produce\nvalid'
for jc2_name in refuse-status refuse-caps refuse-inventory refuse-source refuse-hash valid startup-produce startup-check dummy; do
 jc2_leaf="$jc2_cgroup/$jc2_name"
 test "$(readlink -e "$jc2_leaf")" = "$jc2_leaf"
 test "$(stat -c '%u:%g:%a' "$jc2_leaf")" = 0:0:755
 test "$(sed -n '1p' "$jc2_leaf/cgroup.type")" = domain
 test -z "$(<"$jc2_leaf/cgroup.subtree_control")"
 test -z "$(find "$jc2_leaf" -mindepth 1 -maxdepth 1 -type d -print -quit)"
 test "$(jq -r --arg n "$jc2_name" '.closed_child_guard.leaves[$n].path' "$jc2_base/metadata/ROOT-REGISTRATION.json")" = "$jc2_leaf"
 for jc2_iface in cgroup.procs cgroup.threads cgroup.subtree_control; do
  test "$(stat -c '%u:%g:%A' "$jc2_leaf/$jc2_iface")" = "0:0:-rw-r--r--"
 done
 test -z "$(<"$jc2_cgroup/$jc2_name/cgroup.procs")"; test "$(awk '$1=="populated"{print $2}' "$jc2_cgroup/$jc2_name/cgroup.events")" = 0
 test "$(jq -r --arg n "$jc2_name" '.closed_child_guard.leaves[$n].device' "$jc2_base/metadata/ROOT-REGISTRATION.json")" = "$(stat -c %d "$jc2_cgroup/$jc2_name")"
 test "$(jq -r --arg n "$jc2_name" '.closed_child_guard.leaves[$n].inode' "$jc2_base/metadata/ROOT-REGISTRATION.json")" = "$(stat -c %i "$jc2_cgroup/$jc2_name")"
done
test "$(jq -r '.closed_child_guard.outer_device' "$jc2_base/metadata/ROOT-REGISTRATION.json")" = "$(stat -c %d "$jc2_cgroup")"
test "$(jq -r '.closed_child_guard.outer_inode' "$jc2_base/metadata/ROOT-REGISTRATION.json")" = "$(stat -c %i "$jc2_cgroup")"
test -p "$jc2_fifo"; test ! -L "$jc2_fifo"; test "$(stat -c '%u:%g:%a' "$jc2_fifo")" = 0:0:600
test "$(date -u +%s)" -lt "$((jc2_stop - 3))"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_pid"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p InvocationID --value)" = "$jc2_inv"
test "$(sed 's/^.*) //' /proc/"$jc2_pid"/stat | awk '{print $20}')" = "$jc2_start"
exec '/opt/jc2-closedchild-preflight9-20260912a-admin/fifo-write.sh' ROOT_RELEASE_EXACT_PREFLIGHT9_ONLY
