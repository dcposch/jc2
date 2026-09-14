#!/bin/bash
# DISABLED one-time creation of exact nine empty leaves beneath the LIVE holder.
# Administrative setup only: no source/dummy/registration/release/cleanup.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then exit 2; fi
test 'JC2_LEAF_SETUP_RELEASE_PLACEHOLDER' = ROOT_CREATE_EXACT_NINE_EMPTY_LEAVES
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'JC2_INSTANCE_PLACEHOLDER'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'JC2_BOOT_ID_PLACEHOLDER'
test "$(date -u +%s)" -lt "$(date -ud 'JC2_HOLDER_CUTOFF_UTC_PLACEHOLDER' +%s)"
jc2_unit=jc2-closedchild-preflight9-20260911b.service
jc2_cgroup=/sys/fs/cgroup/system.slice/$jc2_unit
jc2_holder=JC2_CAPTURED_HOLDER_PID_PLACEHOLDER
jc2_start=JC2_CAPTURED_HOLDER_START_TICKS_PLACEHOLDER
jc2_invocation=JC2_CAPTURED_INVOCATION_ID_PLACEHOLDER
jc2_base=/opt/jc2-closedchild-preflight9-20260911b
[[ "$jc2_holder" =~ ^[1-9][0-9]*$ ]]
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p ActiveState --value)" = active
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_holder"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p InvocationID --value)" = "$jc2_invocation"
test "$(sed 's/^.*) //' /proc/"$jc2_holder"/stat | awk '{print $20}')" = "$jc2_start"
test "$(tr '\0' '\n' < /proc/"$jc2_holder"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\n/opt/jc2-closedchild-preflight9-20260911b/admin/holder.py'
test "$(readlink /proc/"$jc2_holder"/exe)" = /usr/bin/python3.12
for jc2_ns in pid mnt cgroup user; do
 jc2_root_ns=$(readlink "/proc/$$/ns/$jc2_ns")
 test "$jc2_root_ns" = "$(readlink "/proc/1/ns/$jc2_ns")"
 test "$jc2_root_ns" = "$(readlink "/proc/$jc2_holder/ns/$jc2_ns")"
 printf 'ROOT_HOLDER_NAMESPACE %s %s\n' "$jc2_ns" "$jc2_root_ns"
done
test "$(findmnt -rn -o TARGET --target /sys/fs/cgroup)" = /sys/fs/cgroup
test "$(findmnt -rn -o FSTYPE --target /sys/fs/cgroup)" = cgroup2
test "$(findmnt -rn -o FSROOT --target /sys/fs/cgroup)" = /
test "$(readlink -e "$jc2_cgroup")" = "$jc2_cgroup"
test "$(sed -n '1p' /proc/"$jc2_holder"/cgroup)" = "0::/system.slice/$jc2_unit"
test "$(sed -n '1,4p' "$jc2_cgroup/cgroup.procs")" = "$jc2_holder"
test -z "$(< /proc/"$jc2_holder"/task/"$jc2_holder"/children)"
test "$(sed -n '1p' "$jc2_cgroup/cgroup.type")" = domain
test -z "$(< "$jc2_cgroup/cgroup.subtree_control")"
test -z "$(find "$jc2_cgroup" -mindepth 1 -maxdepth 1 -type d -print)"
test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
test ! -L "$jc2_base/metadata/ROOT-REGISTRATION.json"
# ROOT separately authenticates effective ACLs/ancestry/migration interfaces and
# no concurrent ROOT/systemd writer; these are not proved by a mode-bit snapshot.
test 'JC2_ROOT_EXCLUSIVITY_APPROVAL_PLACEHOLDER' = ROOT_NO_DELEGATION_MIGRATION_OR_CONCURRENT_WRITER
stat -c 'ROOT_OUTER %d %i %u %g %a %n' "$jc2_cgroup"
for jc2_label in refuse-status refuse-caps refuse-inventory refuse-source refuse-hash valid startup-produce startup-check dummy; do
 jc2_leaf="$jc2_cgroup/$jc2_label"
 test ! -e "$jc2_leaf"
 test ! -L "$jc2_leaf"
 mkdir -m 0755 "$jc2_leaf"
 test "$(readlink -e "$jc2_leaf")" = "$jc2_leaf"
 test "$(stat -c '%u:%g:%a' "$jc2_leaf")" = 0:0:755
 test "$(sed -n '1p' "$jc2_leaf/cgroup.type")" = domain
 test -z "$(< "$jc2_leaf/cgroup.subtree_control")"
 test -z "$(< "$jc2_leaf/cgroup.procs")"
 test -z "$(find "$jc2_leaf" -mindepth 1 -maxdepth 1 -type d -print)"
 test "$(awk '$1 == "populated" {print $2}' "$jc2_leaf/cgroup.events")" = 0
 stat -c 'ROOT_LEAF %d %i %u %g %a %n' "$jc2_leaf"
 # Raw ownership/interface metadata, not an ACL attestation.
 stat -c 'ROOT_MIGRATION_INTERFACE %d %i %u %g %a %n' "$jc2_leaf/cgroup.procs" "$jc2_leaf/cgroup.threads" "$jc2_leaf/cgroup.subtree_control"
done
test "$(find "$jc2_cgroup" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | LC_ALL=C sort)" = $'dummy\nrefuse-caps\nrefuse-hash\nrefuse-inventory\nrefuse-source\nrefuse-status\nstartup-check\nstartup-produce\nvalid'
test "$(date -u +%s)" -lt "$(date -ud 'JC2_HOLDER_CUTOFF_UTC_PLACEHOLDER' +%s)"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_holder"
test "$(sed 's/^.*) //' /proc/"$jc2_holder"/stat | awk '{print $20}')" = "$jc2_start"
date -u '+ROOT_NINE_LEAVES_CREATED_NO_FREEZE_NO_RELEASE %Y-%m-%d %H:%M:%S.%N UTC'
# Any failure leaves evidence for original outer TERM/KILL and worker retirement.
# No rmdir, re-creation, migration, retry, clock rebase or token write.
