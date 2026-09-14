#!/bin/sh
set -eu
test "$(uname -s)" = Linux
test "$(sed -n '1p' /sys/devices/virtual/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(sed -n '1p' /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(hostname)" = ip-172-30-0-72
date -u +%Y-%m-%dT%H:%M:%S.%NUTC
hostname
sed -n '1p' /proc/sys/kernel/random/boot_id
readlink /proc/self/ns/pid
test -f /usr/bin/Singular
readlink -f /usr/bin/Singular
file /usr/bin/Singular
dpkg-query -W -f='${Package} ${Version} ${Status}\n' singular-ui singular-data
/usr/bin/ldd /usr/bin/Singular
sha256sum /usr/bin/Singular /usr/bin/python3 /usr/bin/ldd
/usr/bin/ldd /usr/bin/Singular | /usr/bin/awk '/=> \/|^[[:space:]]*\// {for(i=1;i<=NF;i++) if($i ~ /^\//) print $i}' | LC_ALL=C /usr/bin/sort -u | while IFS= read -r jc2_native_path; do
  test -f "$jc2_native_path"
  sha256sum "$jc2_native_path"
done
date -u +%Y-%m-%dT%H:%M:%S.%NUTC

