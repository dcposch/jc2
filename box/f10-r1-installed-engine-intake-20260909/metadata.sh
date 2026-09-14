#!/bin/sh
set -eu
test "$(hostname)" = ip-172-30-0-72
test "$(sed -n '1p' /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(sed -n '1p' /sys/devices/virtual/dmi/id/sys_vendor)" = 'Amazon EC2'
date -u '+%Y-%m-%dT%H:%M:%SZ'
hostname
readlink -f /usr/bin/Singular
sha256sum /usr/bin/Singular /usr/bin/python3
dpkg-query -W singular singular-data
/usr/bin/python3 -I -B --version
/usr/bin/timeout --foreground 5s /usr/bin/prlimit --cpu=3 --as=134217728 --fsize=1048576 /usr/bin/Singular --no-rc --no-stdlib --no-shell --version
/usr/bin/timeout --foreground 5s /usr/bin/prlimit --cpu=3 --as=134217728 --fsize=1048576 /usr/bin/Singular --no-rc --no-stdlib --no-shell --help
