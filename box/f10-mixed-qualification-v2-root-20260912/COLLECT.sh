#!/bin/bash
set -euo pipefail
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0e074c341fc759521
test "$(date -u +%s)" -lt "$(date -u -d '2026-09-12 23:25:00 UTC' +%s)"
task_prep=/opt/jc2-mixed-20260912/prep
test ! -e "$task_prep/native.stdout"
set +e
systemd-run --quiet --wait --unit=jc2-mixed-v2-native-20260912 --service-type=exec -p Restart=no -p KillMode=control-group -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms -p MemoryMax=1073741824 -p MemorySwapMax=0 -p TasksMax=64 -p LimitAS=1073741824 -p LimitFSIZE=4194304 -p RuntimeMaxSec=595s -p TimeoutStopSec=5s -p StandardOutput=file:"$task_prep/native.stdout" -p StandardError=file:"$task_prep/native.stderr" /usr/bin/bash /opt/jc2-mixed-20260912/meta/native-metadata.actual.sh
task_rc=$?
set -e
printf '%s\n' "$task_rc" > "$task_prep/native.wait-exit"
systemctl show jc2-mixed-v2-native-20260912.service -p Id -p ActiveState -p SubState -p Result -p MainPID -p ControlGroup -p ExecMainCode -p ExecMainStatus > "$task_prep/native.terminal.properties"
date -u '+COLLECT_WAIT_END %Y-%m-%d %H:%M:%S.%N UTC'
printf 'COLLECT_ACTUAL_WAIT_EXIT %s\n' "$task_rc"
exit "$task_rc"
