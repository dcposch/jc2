#!/bin/bash
# Administrative copy/mount only; no source program or library import.
set -euo pipefail
test "$#" -eq 1
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = "$1"
test "$(date -u +%s)" -lt "$(date -u -d '2026-09-12 23:25:00 UTC' +%s)"
task_stage=/home/ubuntu/jc2-mixed-v2-stage-20260912
task_base=/opt/jc2-mixed-20260912
test ! -e "$task_base"
test -d /usr/lib/python3/dist-packages/sympy
test -d /usr/lib/python3/dist-packages/mpmath
test -x /usr/bin/jq
install -d -o root -g root -m 0755 "$task_base" "$task_base/science" "$task_base/runtime" "$task_base/lib" "$task_base/meta" "$task_base/prep"
for task_name in authority.py produce.py check.py; do
    install -o root -g root -m 0444 "$task_stage/$task_name" "$task_base/science/$task_name"
done
for task_name in dispatch.py run_capped.py probe.py; do
    install -o root -g root -m 0444 "$task_stage/$task_name" "$task_base/runtime/$task_name"
done
cp -a /usr/lib/python3/dist-packages/sympy /usr/lib/python3/dist-packages/mpmath "$task_base/lib/"
for task_name in native-metadata.actual.sh native_records.py inspect_native.py inspect_imports.py REGISTRATION.md; do
    install -o root -g root -m 0444 "$task_stage/$task_name" "$task_base/meta/$task_name"
done
mount -t tmpfs -o size=268435456,mode=0755,nodev,nosuid,noexec tmpfs "$task_base/prep"
date -u '+INSTALL_END %Y-%m-%d %H:%M:%S.%N UTC'
hostname
readlink /proc/self/ns/pid
readlink /proc/self/ns/cgroup
sed -n '1p' /proc/sys/kernel/random/boot_id
uname -srmo
systemd --version
dpkg-query -W -f='${Package} ${Version}\n' python3.12 python3.12-minimal libpython3.12-stdlib util-linux procps
find "$task_base/science" "$task_base/runtime" "$task_base/meta" -type f -exec sha256sum '{}' +
