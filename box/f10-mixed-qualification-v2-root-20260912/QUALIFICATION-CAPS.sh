#!/bin/bash
set -euo pipefail
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0e074c341fc759521
systemd-run --quiet --unit=jc2-mixed-v2-qual-term --on-calendar='2026-09-12 23:24:55 UTC' --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-mixed-v2-native-20260912.service jc2-mixed-v2-assembly-20260912.service jc2-mixed-v2-inspect-20260912.service jc2-mixed-v2-imports-20260912.service
systemd-run --quiet --unit=jc2-mixed-v2-qual-kill --on-calendar='2026-09-12 23:25:00 UTC' --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-mixed-v2-native-20260912.service jc2-mixed-v2-assembly-20260912.service jc2-mixed-v2-inspect-20260912.service jc2-mixed-v2-imports-20260912.service
systemctl show jc2-mixed-v2-qual-term.timer jc2-mixed-v2-qual-kill.timer -p Id -p ActiveState -p NextElapseUSecRealtime > /opt/jc2-mixed-20260912/prep/qualification-caps.properties
test "$(systemctl show jc2-mixed-v2-qual-term.timer -P ActiveState)" = active
test "$(systemctl show jc2-mixed-v2-qual-kill.timer -P ActiveState)" = active
cat /opt/jc2-mixed-20260912/prep/qualification-caps.properties
