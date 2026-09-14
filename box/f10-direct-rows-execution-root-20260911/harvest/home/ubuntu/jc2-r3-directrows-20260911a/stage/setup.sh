#!/bin/bash
# DISABLED metadata installation only; no scientific imports/launch/cleanup.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
 exit 2
fi
test 'ROOT_SEPARATELY_AUTHORIZED_DIRECT_ROWS_METADATA_SETUP' = ROOT_SEPARATELY_AUTHORIZED_DIRECT_ROWS_METADATA_SETUP
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'i-031b57c489417e1d1'
test "$(hostname)" = 'ip-172-30-0-218'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = '56714315-f924-4dee-bf5d-95bf5c700dfa'
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11 05:08:00 UTC' +%s)"
jc2_python='/usr/bin/python3.12'
jc2_setpriv='/usr/bin/setpriv'
test "$(readlink -f "$jc2_python")" = "$jc2_python"
test "$(readlink -f "$jc2_setpriv")" = "$jc2_setpriv"
jc2_base='/opt/jc2-r3-directrows-20260911a'
jc2_mount='/run/jc2-r3-directrows-20260911a'
jc2_durable_parent='/var/lib/jc2-r3-directrows-20260911a'
for jc2_target in "$jc2_base" "$jc2_mount" "$jc2_durable_parent"; do
 test ! -e "$jc2_target"
 test ! -L "$jc2_target"
done
cd '/home/ubuntu/jc2-r3-directrows-20260911a/stage'
test "$(sha256sum STAGE-INPUTS.sha256 | cut -d ' ' -f 1)" = '424125e2089921041418eec8f4910df961699f703db51d104097b2c22f707e96'
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' STAGE-INPUTS.sha256 ROOT-REGISTRATION.json ROOT-EXECUTION-CARD.md ROOT-SOURCE-CONTRACT.json preflight-policy.json native-manifest.json source-native-manifest.json; then
 exit 2
fi
sha256sum -c STAGE-INPUTS.sha256
sha256sum -c <<'JC2_EXECUTABLE_PINS'
a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223  /usr/bin/python3.12
62ec0120791f3afcfb689fed52384ec2b0accc6e118a6b9a1d6fcfa7450aaf37  /usr/bin/setpriv
JC2_EXECUTABLE_PINS
# Full six-field closure AND source's bounded matched subset are distinct.
sha256sum -c native.sha256
install -d -o 0 -g 0 -m 0755 "$jc2_base" "$jc2_base/science" "$jc2_base/wrapper" "$jc2_base/runtime" "$jc2_base/metadata"
test ! -e '/opt/jc2-r3-directrows-20260911a/science/authority.py'
install -o 0 -g 0 -m 0444 'authority.py' '/opt/jc2-r3-directrows-20260911a/science/authority.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/science/arithmetic.py'
install -o 0 -g 0 -m 0444 'arithmetic.py' '/opt/jc2-r3-directrows-20260911a/science/arithmetic.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/science/produce.py'
install -o 0 -g 0 -m 0444 'produce.py' '/opt/jc2-r3-directrows-20260911a/science/produce.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/science/check_arithmetic.py'
install -o 0 -g 0 -m 0444 'check_arithmetic.py' '/opt/jc2-r3-directrows-20260911a/science/check_arithmetic.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/science/check.py'
install -o 0 -g 0 -m 0444 'check.py' '/opt/jc2-r3-directrows-20260911a/science/check.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/wrapper/dispatch.py'
install -o 0 -g 0 -m 0444 'dispatch.py' '/opt/jc2-r3-directrows-20260911a/wrapper/dispatch.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/wrapper/probe.py'
install -o 0 -g 0 -m 0444 'probe.py' '/opt/jc2-r3-directrows-20260911a/wrapper/probe.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/wrapper/mutate.py'
install -o 0 -g 0 -m 0444 'mutate.py' '/opt/jc2-r3-directrows-20260911a/wrapper/mutate.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/runtime/run_capped.py'
install -o 0 -g 0 -m 0444 'run_capped.py' '/opt/jc2-r3-directrows-20260911a/runtime/run_capped.py'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/native-manifest.json'
install -o 0 -g 0 -m 0444 'native-manifest.json' '/opt/jc2-r3-directrows-20260911a/metadata/native-manifest.json'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/source-native-manifest.json'
install -o 0 -g 0 -m 0444 'source-native-manifest.json' '/opt/jc2-r3-directrows-20260911a/metadata/source-native-manifest.json'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/native.stdout'
install -o 0 -g 0 -m 0444 'native.stdout' '/opt/jc2-r3-directrows-20260911a/metadata/native.stdout'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/native.sha256'
install -o 0 -g 0 -m 0444 'native.sha256' '/opt/jc2-r3-directrows-20260911a/metadata/native.sha256'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/ROOT-REGISTRATION.json'
install -o 0 -g 0 -m 0444 'ROOT-REGISTRATION.json' '/opt/jc2-r3-directrows-20260911a/metadata/ROOT-REGISTRATION.json'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/ROOT-EXECUTION-CARD.md'
install -o 0 -g 0 -m 0444 'ROOT-EXECUTION-CARD.md' '/opt/jc2-r3-directrows-20260911a/metadata/ROOT-EXECUTION-CARD.md'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/ROOT-SOURCE-CONTRACT.json'
install -o 0 -g 0 -m 0444 'ROOT-SOURCE-CONTRACT.json' '/opt/jc2-r3-directrows-20260911a/metadata/ROOT-SOURCE-CONTRACT.json'
test ! -e '/opt/jc2-r3-directrows-20260911a/metadata/preflight-policy.json'
install -o 0 -g 0 -m 0444 'preflight-policy.json' '/opt/jc2-r3-directrows-20260911a/metadata/preflight-policy.json'
test "$(sha256sum installed.sha256 | cut -d ' ' -f 1)" = '70021be4165ed52552d2da0bf66da7a9117c0dbec7aadb20814ac98b5b6b6a32'
sha256sum -c installed.sha256
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
printf '%s\n' 'DIRECT_ROWS_METADATA_SETUP_ONLY_NO_LAUNCH: ROOT still owns independent control/registration/timer admission.'
# No systemd-run, science/dummy/import, automatic cleanup/unmount or worker action.
