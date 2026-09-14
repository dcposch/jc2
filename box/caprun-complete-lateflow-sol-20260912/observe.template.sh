#!/bin/bash
# DISABLED/UNBOUND ROOT observation only. Bind, hash, and independently review before use.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then exit 2; fi
test "$(id -u)" = 0
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_HOLDER_CUTOFF_PLACEHOLDER' +%s)"
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_ADMISSION_STOP_PLACEHOLDER' +%s)"
jc2_unit='JC2_UNIT_PLACEHOLDER'
jc2_cgroup='JC2_CGROUP_PLACEHOLDER'
jc2_mount='JC2_MOUNT_PLACEHOLDER'
jc2_holder=$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)
jc2_invocation=$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p InvocationID --value)
[[ "$jc2_holder" =~ ^[1-9][0-9]*$ ]]
[[ "$jc2_invocation" =~ ^[0-9a-f]{32}$ ]]
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p ActiveState --value)" = active
jc2_start=$(sed 's/^.*) //' /proc/"$jc2_holder"/stat | awk '{print $20}')
[[ "$jc2_start" =~ ^[1-9][0-9]*$ ]]
jc2_hz=$(getconf CLK_TCK)
jc2_uptime=$(awk '{print $1}' /proc/uptime)
awk -v up="$jc2_uptime" -v start="$jc2_start" -v hz="$jc2_hz" 'BEGIN { exit !((up-start/hz) >= 0 && (up-start/hz) < 120) }'
test "$(tr '\0' '\n' < /proc/"$jc2_holder"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\nJC2_HOLDER_PATH_PLACEHOLDER'
test "$(sed -n '1p' /proc/"$jc2_holder"/cgroup)" = "0::/system.slice/$jc2_unit"
test "$(sed -n '1,4p' "$jc2_cgroup/cgroup.procs")" = "$jc2_holder"
test -z "$(< /proc/"$jc2_holder"/task/"$jc2_holder"/children)"
test "$(sed -n '1p' "$jc2_cgroup/cgroup.type")" = domain
test -z "$(< "$jc2_cgroup/cgroup.subtree_control")"
test -z "$(find "$jc2_mount/authority" -mindepth 1 -maxdepth 1 -print)"
test -z "$(find "$jc2_mount/frozen" -mindepth 1 -maxdepth 1 -print)"
test -z "$(find "$jc2_mount/writer" -mindepth 1 -maxdepth 1 -print)"
jc2_outer_device=$(stat -c %d "$jc2_cgroup")
jc2_outer_inode=$(stat -c %i "$jc2_cgroup")
jc2_leaves='[]'
for jc2_label in refuse-status refuse-caps refuse-inventory refuse-source refuse-hash valid startup-produce startup-check dummy; do
 jc2_leaf="$jc2_cgroup/$jc2_label"
 test "$(readlink -e "$jc2_leaf")" = "$jc2_leaf"
 test "$(sed -n '1p' "$jc2_leaf/cgroup.type")" = domain
 test -z "$(< "$jc2_leaf/cgroup.subtree_control")"
 test -z "$(< "$jc2_leaf/cgroup.procs")"
 test -z "$(find "$jc2_leaf" -mindepth 1 -maxdepth 1 -type d -print)"
 test "$(awk '$1 == "populated" {print $2}' "$jc2_leaf/cgroup.events")" = 0
 jc2_leaves=$(jq -c --arg n "$jc2_label" --arg p "$jc2_leaf" --argjson d "$(stat -c %d "$jc2_leaf")" --argjson i "$(stat -c %i "$jc2_leaf")" '. + [{name:$n,path:$p,device:$d,inode:$i}]' <<<"$jc2_leaves")
done
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_HOLDER_CUTOFF_PLACEHOLDER' +%s)"
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_ADMISSION_STOP_PLACEHOLDER' +%s)"
jq -cn --arg context ROOT_ATTESTED_CANDIDATE --arg instance_id 'JC2_INSTANCE_PLACEHOLDER' --arg hostname 'JC2_HOSTNAME_PLACEHOLDER' --arg boot_id 'JC2_BOOT_ID_PLACEHOLDER' --arg pid_namespace "$(readlink /proc/"$jc2_holder"/ns/pid)" --arg cgroup_path "$jc2_cgroup" --argjson holder_pid "$jc2_holder" --argjson start_ticks "$jc2_start" --arg invocation_id "$jc2_invocation" --argjson outer_device "$jc2_outer_device" --argjson outer_inode "$jc2_outer_inode" --argjson leaves "$jc2_leaves" --arg coordinator_receipt_sha256 'JC2_COORDINATOR_RECEIPT_SHA256_PLACEHOLDER' --arg native_manifest_sha256 'JC2_NATIVE_MANIFEST_SHA256_PLACEHOLDER' --arg native_list_sha256 'JC2_NATIVE_LIST_SHA256_PLACEHOLDER' '{schema:"caprun-late-observation/v1",context:$context,instance_id:$instance_id,hostname:$hostname,boot_id:$boot_id,pid_namespace:$pid_namespace,cgroup_path:$cgroup_path,holder_pid:$holder_pid,start_ticks:$start_ticks,invocation_id:$invocation_id,outer_device:$outer_device,outer_inode:$outer_inode,leaves:$leaves,coordinator_receipt_sha256:$coordinator_receipt_sha256,native_manifest_sha256:$native_manifest_sha256,native_list_sha256:$native_list_sha256}'
