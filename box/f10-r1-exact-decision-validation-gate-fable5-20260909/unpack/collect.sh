#!/bin/sh
set -eu
test "$(hostname)" = ip-172-30-0-72
test ! -e /proc/1312
test ! -e /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/jc2-f10-r1-exact-decision-validation-20260909.service
systemctl --user show jc2-f10-r1-exact-decision-validation-20260909.service --property=LoadState,ActiveState,SubState,MainPID,Result
journalctl --user -u jc2-f10-r1-exact-decision-validation-20260909.service --since '2026-09-09 14:49:00 UTC' --no-pager -n 20
cd /home/ubuntu/f10-r1-exact-decision-validation-20260909
sha256sum --check INPUT.sha256
set -C
find . -maxdepth 1 -type f ! -name TERMINAL.sha256 -print0 | sort -z | xargs -0 sha256sum > TERMINAL.sha256
sha256sum TERMINAL.sha256
date -u +%Y-%m-%dT%H:%M:%SZ
printf '%s\n' 'TERMINAL: original caller PID absent; exact service cgroup absent; all source pins unchanged'
