#!/bin/bash
# DISABLED/UNBOUND fixed preholder-installed late-DATA consumer. Never bash -s.
set -euo pipefail
grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0" && exit 2
test "$#" = 3
test "$(id -u)" = 0
jc2_pid=$1; jc2_start=$2; jc2_inv=$3
[[ "$jc2_pid" =~ ^[1-9][0-9]{0,9}$ && "$jc2_start" =~ ^[1-9][0-9]{0,14}$ && "$jc2_inv" =~ ^[0-9a-f]{32}$ ]]
jc2_unit='JC2_REMOTE_UNIT_PLACEHOLDER'
jc2_cgroup='JC2_REMOTE_CGROUP_PLACEHOLDER'
jc2_base='JC2_REMOTE_BASE_PLACEHOLDER'
jc2_stop='JC2_EARLIEST_ORIGINAL_STOP_EPOCH_PLACEHOLDER'
jc2_fifo='JC2_REMOTE_FIFO_PLACEHOLDER'
jc2_names='refuse-status refuse-caps refuse-inventory refuse-source refuse-hash valid startup-produce startup-check dummy'
test "$(date -u +%s)" -lt "$((jc2_stop - 5))"
test "$(tr -d '\n' </sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' </sys/class/dmi/id/board_asset_tag)" = 'JC2_INSTANCE_ID_PLACEHOLDER'
test "$(hostname)" = 'JC2_HOSTNAME_PLACEHOLDER'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'JC2_BOOT_ID_PLACEHOLDER'
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p ActiveState --value)" = active
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_pid"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p InvocationID --value)" = "$jc2_inv"
test "$(sed 's/^.*) //' /proc/"$jc2_pid"/stat | awk '{print $20}')" = "$jc2_start"
test "$(tr '\0' '\n' </proc/"$jc2_pid"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\nJC2_REMOTE_HOLDER_PATH_PLACEHOLDER'
test "$(readlink /proc/"$jc2_pid"/exe)" = /usr/bin/python3.12
for jc2_ns in pid mnt cgroup user; do
 test "$(readlink /proc/$$/ns/$jc2_ns)" = "$(readlink /proc/1/ns/$jc2_ns)"
 test "$(readlink /proc/$$/ns/$jc2_ns)" = "$(readlink /proc/$jc2_pid/ns/$jc2_ns)"
done
test "$(readlink /proc/$jc2_pid/ns/pid)" = 'JC2_PID_NAMESPACE_PLACEHOLDER'
test "$(sed -n '1p' /proc/$jc2_pid/cgroup)" = "0::${jc2_cgroup#/sys/fs/cgroup}"
test "$(sed -n '1,4p' "$jc2_cgroup/cgroup.procs")" = "$jc2_pid"
test -z "$(</proc/$jc2_pid/task/$jc2_pid/children)"
test "$(sed -n '1p' "$jc2_cgroup/cpu.max")" = '6900 10000'
test "$(sed -n '1p' "$jc2_cgroup/cpu.max.burst")" = 0
test "$(sed -n '1p' "$jc2_cgroup/memory.max")" = 8589934592
test "$(sed -n '1p' "$jc2_cgroup/memory.swap.max")" = 0
test "$(sed -n '1p' "$jc2_cgroup/pids.max")" = 32
test "$(sed -n '1p' "$jc2_cgroup/cgroup.type")" = domain
test -z "$(<"$jc2_cgroup/cgroup.subtree_control")"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p Delegate --value)" = no
for jc2_iface in cgroup.procs cgroup.threads cgroup.subtree_control; do
 test "$(stat -c '%u:%g:%A' "$jc2_cgroup/$jc2_iface")" = "0:0:-rw-r--r--"
done
test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
test ! -L "$jc2_base/metadata/ROOT-REGISTRATION.json"
test -p "$jc2_fifo"; test ! -L "$jc2_fifo"; test "$(stat -c '%u:%g:%a' "$jc2_fifo")" = 0:0:600
test -z "$(find 'JC2_REMOTE_AUTHORITY_DIR_PLACEHOLDER' 'JC2_REMOTE_FROZEN_DIR_PLACEHOLDER' 'JC2_REMOTE_WRITER_DIR_PLACEHOLDER' -mindepth 1 -maxdepth 1 -print -quit)"
test -z "$(find "$jc2_cgroup" -mindepth 1 -maxdepth 1 -type d -print -quit)"
for jc2_name in $jc2_names; do
 jc2_leaf="$jc2_cgroup/$jc2_name"
 test ! -e "$jc2_leaf"; test ! -L "$jc2_leaf"
 mkdir -m 0755 "$jc2_leaf"
done
test "$(find "$jc2_cgroup" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | LC_ALL=C sort)" = $'dummy\nrefuse-caps\nrefuse-hash\nrefuse-inventory\nrefuse-source\nrefuse-status\nstartup-check\nstartup-produce\nvalid'
jc2_hz=$(getconf CLK_TCK); read -r jc2_up _ </proc/uptime; jc2_up=${jc2_up%%.*}
[[ "$jc2_hz" =~ ^[1-9][0-9]*$ && "$jc2_up" =~ ^[0-9]+$ ]]
test "$((jc2_up - jc2_start / jc2_hz))" -ge 0
test "$((jc2_up - jc2_start / jc2_hz))" -lt 120
jc2_outer=$(stat -c '%d %i' "$jc2_cgroup")
printf '{"schema":"caprun-late-observation/v1","context":"ROOT_ATTESTED_CANDIDATE","instance_id":"%s","hostname":"%s","boot_id":"%s","pid_namespace":"%s","cgroup_path":"%s","holder_pid":%s,"start_ticks":%s,"invocation_id":"%s","outer_device":%s,"outer_inode":%s,"leaves":[' 'JC2_INSTANCE_ID_PLACEHOLDER' 'JC2_HOSTNAME_PLACEHOLDER' 'JC2_BOOT_ID_PLACEHOLDER' 'JC2_PID_NAMESPACE_PLACEHOLDER' "$jc2_cgroup" "$jc2_pid" "$jc2_start" "$jc2_inv" ${jc2_outer% *} ${jc2_outer#* }
jc2_sep=
for jc2_name in $jc2_names; do
 jc2_leaf="$jc2_cgroup/$jc2_name"
 test "$(readlink -e "$jc2_leaf")" = "$jc2_leaf"
 test "$(stat -c '%u:%g:%a' "$jc2_leaf")" = 0:0:755
 test "$(sed -n '1p' "$jc2_leaf/cgroup.type")" = domain
 test -z "$(<"$jc2_leaf/cgroup.subtree_control")"; test -z "$(<"$jc2_leaf/cgroup.procs")"
 test "$(awk '$1=="populated"{print $2}' "$jc2_leaf/cgroup.events")" = 0
 test -z "$(find "$jc2_leaf" -mindepth 1 -maxdepth 1 -type d -print -quit)"
 for jc2_iface in cgroup.procs cgroup.threads cgroup.subtree_control; do
  test "$(stat -c '%u:%g:%A' "$jc2_leaf/$jc2_iface")" = "0:0:-rw-r--r--"
 done
 jc2_id=$(stat -c '%d %i' "$jc2_leaf")
 printf '%s{"name":"%s","path":"%s","device":%s,"inode":%s}' "$jc2_sep" "$jc2_name" "$jc2_leaf" ${jc2_id% *} ${jc2_id#* }
 jc2_sep=,
done
test "$(date -u +%s)" -lt "$((jc2_stop - 3))"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_pid"
test "$(sed 's/^.*) //' /proc/"$jc2_pid"/stat | awk '{print $20}')" = "$jc2_start"
printf '],"coordinator_receipt_sha256":"%s","native_manifest_sha256":"%s","native_list_sha256":"%s"}\n' 'JC2_RECEIPT_SHA256_PLACEHOLDER' 'JC2_REMOTE_NATIVE_MANIFEST_SHA256_PLACEHOLDER' 'JC2_NATIVE_LIST_SHA256_PLACEHOLDER'
