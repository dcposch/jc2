#!/bin/bash
# DISABLED final metadata installation. NO token, dispatcher, source or cleanup.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then exit 2; fi
test 'ROOT_FREEZE_EXACT_PREFLIGHT9_REGISTRATION_ONLY' = ROOT_FREEZE_EXACT_PREFLIGHT9_REGISTRATION_ONLY
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'i-033947c617e8ad0e5'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'c682c214-afd7-4839-898d-e81fae3ccf27'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11T16:14:00+00:00' +%s)"
jc2_base=/opt/jc2-closedchild-preflight9-20260911c
jc2_stage=/home/ubuntu/jc2-closedchild-preflight9-20260911c/stage
jc2_unit=jc2-closedchild-preflight9-20260911c.service
jc2_cgroup=/sys/fs/cgroup/system.slice/$jc2_unit
jc2_holder=32315
jc2_start=81252
jc2_invocation=5fa4785de938458e8cc6125550a25385
jc2_final="$jc2_base/metadata/ROOT-REGISTRATION.json"
[[ "$jc2_holder" =~ ^[1-9][0-9]*$ ]]
cd "$jc2_stage"
test "$(sha256sum FINAL-INSTALL-INPUTS.sha256 | cut -d ' ' -f 1)" = '57b15603df94eff3b04be1b288f80a879558be0cdf86724007070999f4a2abfa'
sha256sum --strict -c FINAL-INSTALL-INPUTS.sha256
test "$(sha256sum ROOT-REGISTRATION.json | cut -d ' ' -f 1)" = '257de6c1815389d99887a9fcd941d7c6e15fa5b1298e0e60cb30044bbd40f46b'
test "$(sha256sum ROOT-EXECUTION-CARD.md | cut -d ' ' -f 1)" = '1a2c09813ebf7a179908f18b882a1f5f345864064e528ce45a275d58338b2797'
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' ROOT-REGISTRATION.json ROOT-EXECUTION-CARD.md; then exit 2; fi
test ! -e "$jc2_final"
test ! -L "$jc2_final"
test ! -e "$jc2_base/metadata/ROOT-EXECUTION-CARD.md"
test ! -L "$jc2_base/metadata/ROOT-EXECUTION-CARD.md"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_holder"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p ActiveState --value)" = active
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p InvocationID --value)" = "$jc2_invocation"
test "$(sed 's/^.*) //' /proc/"$jc2_holder"/stat | awk '{print $20}')" = "$jc2_start"
test "$(tr '\0' '\n' < /proc/"$jc2_holder"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\n/opt/jc2-closedchild-preflight9-20260911c/admin/holder.py'
for jc2_ns in pid mnt cgroup user; do
 test "$(readlink "/proc/$$/ns/$jc2_ns")" = "$(readlink "/proc/1/ns/$jc2_ns")"
 test "$(readlink "/proc/$$/ns/$jc2_ns")" = "$(readlink "/proc/$jc2_holder/ns/$jc2_ns")"
done
test "$(sed -n '1,4p' "$jc2_cgroup/cgroup.procs")" = "$jc2_holder"
test -z "$(< /proc/"$jc2_holder"/task/"$jc2_holder"/children)"
test "$(sed -n '1p' "$jc2_cgroup/cgroup.type")" = domain
test -z "$(< "$jc2_cgroup/cgroup.subtree_control")"
jq -e '.schema=="f10-necessary-rows-runtime/closed-child-v1" and .enabled==true and .exclusive_no_concurrent_writer==true and .execution_mode=="PREFLIGHT_ONLY_9" and .phase_policy==null and .typed_slot_policy=={} and .aggregate_cpu_start_usec=="0" and .closed_child_guard.root_no_migration==true' ROOT-REGISTRATION.json >/dev/null
test "$(jq -r '.cgroup_path' ROOT-REGISTRATION.json)" = "$jc2_cgroup"
test "$(jq -r '.instance_id' ROOT-REGISTRATION.json)" = 'i-033947c617e8ad0e5'
test "$(jq -r '.boot_id' ROOT-REGISTRATION.json)" = 'c682c214-afd7-4839-898d-e81fae3ccf27'
test "$(jq -r '.pid_namespace' ROOT-REGISTRATION.json)" = "$(readlink /proc/"$jc2_holder"/ns/pid)"
test "$(jq -r '.closed_child_guard.outer_device' ROOT-REGISTRATION.json)" = "$(stat -c %d "$jc2_cgroup")"
test "$(jq -r '.closed_child_guard.outer_inode' ROOT-REGISTRATION.json)" = "$(stat -c %i "$jc2_cgroup")"
test "$(jq -r '.allowed_phases[]' ROOT-REGISTRATION.json)" = $'refuse-status\nrefuse-caps\nrefuse-inventory\nrefuse-source\nrefuse-hash\nvalid\nstartup-produce\nstartup-check\ndummy'
test "$(jq -r '.closed_child_guard.leaves | keys[]' ROOT-REGISTRATION.json)" = $'dummy\nrefuse-caps\nrefuse-hash\nrefuse-inventory\nrefuse-source\nrefuse-status\nstartup-check\nstartup-produce\nvalid'
test "$(find "$jc2_cgroup" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | LC_ALL=C sort)" = $'dummy\nrefuse-caps\nrefuse-hash\nrefuse-inventory\nrefuse-source\nrefuse-status\nstartup-check\nstartup-produce\nvalid'
for jc2_label in refuse-status refuse-caps refuse-inventory refuse-source refuse-hash valid startup-produce startup-check dummy; do
 jc2_leaf="$jc2_cgroup/$jc2_label"
 test "$(jq -r --arg label "$jc2_label" '.closed_child_guard.leaves[$label].path' ROOT-REGISTRATION.json)" = "$jc2_leaf"
 test "$(readlink -e "$jc2_leaf")" = "$jc2_leaf"
 test "$(jq -r --arg label "$jc2_label" '.closed_child_guard.leaves[$label].device' ROOT-REGISTRATION.json)" = "$(stat -c %d "$jc2_leaf")"
 test "$(jq -r --arg label "$jc2_label" '.closed_child_guard.leaves[$label].inode' ROOT-REGISTRATION.json)" = "$(stat -c %i "$jc2_leaf")"
 test "$(sed -n '1p' "$jc2_leaf/cgroup.type")" = domain
 test -z "$(< "$jc2_leaf/cgroup.subtree_control")"
 test -z "$(< "$jc2_leaf/cgroup.procs")"
 test -z "$(find "$jc2_leaf" -mindepth 1 -maxdepth 1 -type d -print)"
 test "$(awk '$1 == "populated" {print $2}' "$jc2_leaf/cgroup.events")" = 0
done
# ROOT previously reconstructed all9 full argv and exact per-phase canonical
# JSON digests, qualified native/ACL/namespace facts, and checked coordinator
# retirement timer on the COORDINATOR. These lines do not invent those facts.
jq -r '.pins | to_entries[] | "\(.value)  \(.key)"' ROOT-REGISTRATION.json | sha256sum --strict -c
sha256sum --strict -c native.sha256
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11T16:14:00+00:00' +%s)"
install -o 0 -g 0 -m 0444 ROOT-REGISTRATION.json "$jc2_final"
install -o 0 -g 0 -m 0444 ROOT-EXECUTION-CARD.md "$jc2_base/metadata/ROOT-EXECUTION-CARD.md"
sync -f "$jc2_base/metadata"
cmp ROOT-REGISTRATION.json "$jc2_final"
cmp ROOT-EXECUTION-CARD.md "$jc2_base/metadata/ROOT-EXECUTION-CARD.md"
test "$(sha256sum "$jc2_final" | cut -d ' ' -f 1)" = '257de6c1815389d99887a9fcd941d7c6e15fa5b1298e0e60cb30044bbd40f46b'
test "$(stat -c '%u:%g:%a' "$jc2_final")" = 0:0:444
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_holder"
test "$(sed 's/^.*) //' /proc/"$jc2_holder"/stat | awk '{print $20}')" = "$jc2_start"
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11T16:14:00+00:00' +%s)"
date -u '+ROOT_FINAL_REGISTRATION_FROZEN_NO_RELEASE %Y-%m-%d %H:%M:%S.%N UTC'
# External ROOT must independently authorize the ONE bounded token write.
# Any failure preserves partial evidence; no overwrite/retry/restart/deletion.
