#!/bin/bash
# DISABLED pre-admission installation only; final registration stays ABSENT.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
 exit 2
fi
test 'ROOT_SEPARATELY_AUTHORIZED_CLOSEDCHILD_PRE_ADMISSION' = ROOT_SEPARATELY_AUTHORIZED_CLOSEDCHILD_PRE_ADMISSION
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'i-00653baa8e5c32c75'
test "$(hostname)" = 'ip-172-30-0-120'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'd06102c6-210d-4161-9f85-a7327b96f44a'
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11T10:58:00+00:00' +%s)"
jc2_python='/usr/bin/python3.12'
jc2_setpriv='/usr/bin/setpriv'
test "$(readlink -f "$jc2_python")" = "$jc2_python"
test "$(readlink -f "$jc2_setpriv")" = "$jc2_setpriv"
jc2_base='/opt/jc2-closedchild-preflight9-20260911a'
jc2_mount='/run/jc2-closedchild-preflight9-20260911a'
jc2_channel='/run/jc2-closedchild-preflight9-20260911a-admission'
jc2_durable_parent='/var/lib/jc2-closedchild-preflight9-20260911a'
for jc2_target in "$jc2_base" "$jc2_mount" "$jc2_durable_parent" "$jc2_channel"; do
 test ! -e "$jc2_target"
 test ! -L "$jc2_target"
done
cd '/home/ubuntu/jc2-closedchild-preflight9-20260911a/stage'
test "$(sha256sum PRE-ADMISSION-STAGE.sha256 | cut -d ' ' -f 1)" = '3372218146cc991ff6e5debdfb82df9bc4e48c9de8271b9cda0d51ea5bd92978'
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' PRE-ADMISSION-STAGE.sha256 holder.py ROOT-SOURCE-CONTRACT.json preflight-policy.json native-manifest.json source-native-manifest.json; then
 exit 2
fi
sha256sum --strict -c PRE-ADMISSION-STAGE.sha256
sha256sum --strict -c <<'JC2_EXECUTABLE_PINS'
a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223  /usr/bin/python3.12
62ec0120791f3afcfb689fed52384ec2b0accc6e118a6b9a1d6fcfa7450aaf37  /usr/bin/setpriv
JC2_EXECUTABLE_PINS
# Full six-field closure AND source's bounded matched subset are distinct.
sha256sum --strict -c native.sha256
install -d -o 0 -g 0 -m 0755 "$jc2_base" "$jc2_base/science" "$jc2_base/wrapper" "$jc2_base/runtime" "$jc2_base/metadata" "$jc2_base/admin"
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/science/authority.py'
install -o 0 -g 0 -m 0444 'authority.py' '/opt/jc2-closedchild-preflight9-20260911a/science/authority.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/science/arithmetic.py'
install -o 0 -g 0 -m 0444 'arithmetic.py' '/opt/jc2-closedchild-preflight9-20260911a/science/arithmetic.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/science/produce.py'
install -o 0 -g 0 -m 0444 'produce.py' '/opt/jc2-closedchild-preflight9-20260911a/science/produce.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/science/check_arithmetic.py'
install -o 0 -g 0 -m 0444 'check_arithmetic.py' '/opt/jc2-closedchild-preflight9-20260911a/science/check_arithmetic.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/science/check.py'
install -o 0 -g 0 -m 0444 'check.py' '/opt/jc2-closedchild-preflight9-20260911a/science/check.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/wrapper/dispatch.py'
install -o 0 -g 0 -m 0444 'dispatch.py' '/opt/jc2-closedchild-preflight9-20260911a/wrapper/dispatch.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/wrapper/probe.py'
install -o 0 -g 0 -m 0444 'probe.py' '/opt/jc2-closedchild-preflight9-20260911a/wrapper/probe.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/wrapper/mutate.py'
install -o 0 -g 0 -m 0444 'mutate.py' '/opt/jc2-closedchild-preflight9-20260911a/wrapper/mutate.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/runtime/run_capped.py'
install -o 0 -g 0 -m 0444 'run_capped.py' '/opt/jc2-closedchild-preflight9-20260911a/runtime/run_capped.py'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/metadata/native-manifest.json'
install -o 0 -g 0 -m 0444 'native-manifest.json' '/opt/jc2-closedchild-preflight9-20260911a/metadata/native-manifest.json'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/metadata/source-native-manifest.json'
install -o 0 -g 0 -m 0444 'source-native-manifest.json' '/opt/jc2-closedchild-preflight9-20260911a/metadata/source-native-manifest.json'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/metadata/native.stdout'
install -o 0 -g 0 -m 0444 'native.stdout' '/opt/jc2-closedchild-preflight9-20260911a/metadata/native.stdout'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/metadata/native.sha256'
install -o 0 -g 0 -m 0444 'native.sha256' '/opt/jc2-closedchild-preflight9-20260911a/metadata/native.sha256'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/metadata/ROOT-SOURCE-CONTRACT.json'
install -o 0 -g 0 -m 0444 'ROOT-SOURCE-CONTRACT.json' '/opt/jc2-closedchild-preflight9-20260911a/metadata/ROOT-SOURCE-CONTRACT.json'
test ! -e '/opt/jc2-closedchild-preflight9-20260911a/metadata/preflight-policy.json'
install -o 0 -g 0 -m 0444 'preflight-policy.json' '/opt/jc2-closedchild-preflight9-20260911a/metadata/preflight-policy.json'
test ! -e "$jc2_base/admin/holder.py"
install -o 0 -g 0 -m 0444 holder.py "$jc2_base/admin/holder.py"
test "$(sha256sum "$jc2_base/admin/holder.py" | cut -d ' ' -f 1)" = '188223110628c3af953cc551920c31cbb9ccfd5a3842e707556f73640c56d010'
test "$(sha256sum PRE-ADMISSION-INSTALLED.sha256 | cut -d ' ' -f 1)" = '2430b36be4212a8ec605d970687987deeaa943491725e9a8e1eeb9bef1ac1e62'
sha256sum --strict -c PRE-ADMISSION-INSTALLED.sha256
test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
test ! -L "$jc2_base/metadata/ROOT-REGISTRATION.json"
install -d -o 0 -g 0 -m 0700 "$jc2_channel"
/usr/bin/mkfifo -m 0600 "$jc2_channel/release.fifo"
test "$(stat -c '%u:%g:%a' "$jc2_channel/release.fifo")" = 0:0:600
install -d -o 0 -g 0 -m 0755 "$jc2_durable_parent"
test "$(stat -c %d "$jc2_durable_parent")" = '66305'
test "$(findmnt -n -o FSTYPE --target "$jc2_durable_parent")" = 'ext4'
test ! -e "$jc2_durable_parent/custody"
install -d -o 0 -g 0 -m 0755 "$jc2_mount"
mount -t tmpfs -o size=134217728,mode=0755,nosuid,nodev tmpfs "$jc2_mount"
install -d -o 0 -g 0 -m 0755 "$jc2_mount/authority" "$jc2_mount/frozen"
install -d -o 65534 -g 65534 -m 0700 "$jc2_mount/writer"
for jc2_file in "$jc2_base"/science/* "$jc2_base"/wrapper/* "$jc2_base"/runtime/* "$jc2_base"/metadata/*; do
 "$jc2_setpriv" --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
sync -f "$jc2_base"
sync -f "$jc2_durable_parent"
sync -f "$jc2_channel"
printf '%s\n' 'CLOSED_CHILD_PRE_ADMISSION_INSTALLED_NO_REGISTRATION_NO_LAUNCH: ROOT owns all later release duties.'
# No systemd-run, science/dummy/import, automatic cleanup/unmount or worker action.
