#!/bin/sh
set -eu
test "$(hostname)" = ip-172-30-0-72
test "$(/usr/bin/tr -d '\n' < /sys/devices/virtual/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(/usr/bin/tr -d '\n' < /sys/devices/virtual/dmi/id/sys_vendor)" = 'Amazon EC2'
printf '%s\n' 'a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223  /usr/bin/python3' '90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4  /usr/bin/Singular' | sha256sum --check
test ! -e /home/ubuntu/f10-r1-exact-decision-validation-20260909
test "$(systemctl --user show jc2-f10-r1-exact-decision-validation-20260909.service --property=LoadState --value)" = not-found
mkdir /home/ubuntu/f10-r1-exact-decision-validation-20260909
date -u +%Y-%m-%dT%H:%M:%SZ
printf '%s\n' 'PREPARE-PASS: exact owned worker, binary pins, exclusive directory; no caller executed'
