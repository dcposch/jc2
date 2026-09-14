#!/bin/sh
set -eu
test "$(hostname)" = ip-172-30-0-72
test "$(sed -n '1p' /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(sed -n '1p' /sys/devices/virtual/dmi/id/sys_vendor)" = 'Amazon EC2'
printf '%s\n' '90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4  /usr/bin/Singular' 'a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223  /usr/bin/python3' | sha256sum --check
date -u '+%Y-%m-%dT%H:%M:%SZ'
printf '%s\n' 'print("CLI-METADATA-BEGIN");' 'option(nostdhilb,noprobabilistic);' 'print("CLI-METADATA-END");' 'quit;' | /usr/bin/timeout --foreground 5s /usr/bin/prlimit --cpu=3 --as=134217728 --fsize=1048576 /usr/bin/Singular --no-rc --no-stdlib --no-shell -q -t
