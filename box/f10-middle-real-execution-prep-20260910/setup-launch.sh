#!/bin/bash
# ROOT one-shot setup and launch; no source edits, no retry, no package installs.
set -euo pipefail
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 1dd41ed9-bd96-41aa-b95a-671eb5d53ae9
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
test ! -e /opt/jc2-real-20260910T1022
test ! -e /run/jc2-real-20260910T1022
test ! -e /var/lib/jc2-real-20260910T1022
test ! -e /usr/lib/python312.zip
test ! -L /usr/lib/python312.zip
cd /home/ubuntu/jc2-real-native-20260910T1012/stage
sha256sum -c <<'JC2_STAGE_PINS'
364942819c8f80e1127ea7ccb0398adeec4aa22baa994161677d348d49c3d532  f10-middle-real-runtime-astra-20260910.md
f2db01a4aa9b982c1d379082c7d2a6d36f2575724660282d2ff5e3f8b53e5e6e  dispatch.py
d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4  probe.py
4587133176acc66842f9ded5c6b6a6e37683ff9ffe980bf9f46e42088359d73d  authority.py
44859af3084c3445522c8e73a88c0fc96a710375bcd9c9e50340fd4ce5de0dd2  producer.py
9369f0f311da9848f7d708a77413cda9115a4d8376aa626d7efaf017b4f8043c  checker.py
43643a6ee8546be56592237d62ac4b1a0ce16d47980c2ba895355f27ba015c4b  ROOT-CARD.md
819d5e70a33d826e53658b5d007305e985040adf5ac29e23c1c6e2110218c192  ROOT-STARTUP-DELTA.md
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  run_capped.py
c3111895d6d9c8ea217124aad44aefb351faf244ea13037935673f8f8fd785e9  f10-middle-real-code-astra-20260910.md
d3b8c09234d50b51b9dbcfaa7a9f341f34263540bd35e798c9f794137640c932  f10-middle-real-code-gate-fable5-20260910.md
3f79cabecdb2c0f480bde3db644eac91ea5c8d3d472a3477f575b356993347ea  f10-middle-real-domain-astra-20260910.md
f04c174e4b3111b2b9ee3e22e4ecceb619f0cfd2b9374e99a9ec9065cc52d21f  f10-middle-real-domain-gate-fable5-20260910.md
8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012  f10-middle-resonance-unit-astra-20260910.md
dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad  f10-middle-resonance-unit-gate-fable5-20260910.md
82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6  f10-middle-full-boundary-astra-20260910.md
8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491  f10-middle-full-boundary-gate-fable5-20260910.md
890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5  f10-middle-univariate-unit-astra-20260910.md
cff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62  f10-middle-septic-gate-fable5-20260910.md
0562b82afa2b6f6da1e2c488d261fc65f22f705629c12446bbfeaf85bdccbef2  f10-middle-real-runtime-gate-fable5-20260910.md
134e173289e4fb8e4f71e51e527b7dc5512075ca448512643e5bd942128692bf  native-manifest.json
2f86ce99b0cfbd6a6bfd4725fff91f37d9f56e331eb028530741974b3702a7a1  ROOT-REGISTRATION.json
7afb522325c3530eb7a99a6f29212f79c357f7871282cd56dd7dcfe24f036845  ROOT-EXECUTION-CARD.md
3c4a02de8ebba40bb34eecf7c4373a89c3eeebcdb5ecb1555f121ba2c159375b  native.stdout
JC2_STAGE_PINS
# Verify all collected aliases without reading scientific data.
awk '$1=="ALIAS" {print $2, $3}' native.stdout |
 while read -r jc2_alias jc2_canonical; do
  test "$(readlink -f "$jc2_alias")" = "$jc2_canonical"
 done
sha256sum -c native.sha256
install -d -o 0 -g 0 -m 0755 /opt/jc2-real-20260910T1022
test ! -e /opt/jc2-real-20260910T1022/f10-middle-real-runtime-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-real-runtime-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-runtime-astra-20260910.md
test ! -e /opt/jc2-real-20260910T1022/dispatch.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/dispatch.py /opt/jc2-real-20260910T1022/dispatch.py
test ! -e /opt/jc2-real-20260910T1022/probe.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/probe.py /opt/jc2-real-20260910T1022/probe.py
test ! -e /opt/jc2-real-20260910T1022/authority.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/authority.py /opt/jc2-real-20260910T1022/authority.py
test ! -e /opt/jc2-real-20260910T1022/producer.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/producer.py /opt/jc2-real-20260910T1022/producer.py
test ! -e /opt/jc2-real-20260910T1022/checker.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/checker.py /opt/jc2-real-20260910T1022/checker.py
test ! -e /opt/jc2-real-20260910T1022/ROOT-CARD.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/ROOT-CARD.md /opt/jc2-real-20260910T1022/ROOT-CARD.md
test ! -e /opt/jc2-real-20260910T1022/ROOT-STARTUP-DELTA.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/ROOT-STARTUP-DELTA.md /opt/jc2-real-20260910T1022/ROOT-STARTUP-DELTA.md
test ! -e /opt/jc2-real-20260910T1022/run_capped.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/run_capped.py /opt/jc2-real-20260910T1022/run_capped.py
test ! -e /opt/jc2-real-20260910T1022/f10-middle-real-code-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-real-code-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-code-astra-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-real-code-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-real-code-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-code-gate-fable5-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-real-domain-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-real-domain-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-domain-astra-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-real-domain-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-real-domain-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-domain-gate-fable5-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-resonance-unit-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-astra-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-resonance-unit-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-gate-fable5-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-full-boundary-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-full-boundary-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-full-boundary-astra-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-full-boundary-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-full-boundary-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-full-boundary-gate-fable5-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-univariate-unit-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-univariate-unit-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-univariate-unit-astra-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-septic-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-septic-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-septic-gate-fable5-20260910.md
test ! -e /opt/jc2-real-20260910T1022/f10-middle-real-runtime-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/f10-middle-real-runtime-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-runtime-gate-fable5-20260910.md
test ! -e /opt/jc2-real-20260910T1022/native-manifest.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/native-manifest.json /opt/jc2-real-20260910T1022/native-manifest.json
test ! -e /opt/jc2-real-20260910T1022/ROOT-REGISTRATION.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/ROOT-REGISTRATION.json /opt/jc2-real-20260910T1022/ROOT-REGISTRATION.json
test ! -e /opt/jc2-real-20260910T1022/ROOT-EXECUTION-CARD.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-real-native-20260910T1012/stage/ROOT-EXECUTION-CARD.md /opt/jc2-real-20260910T1022/ROOT-EXECUTION-CARD.md
sha256sum -c <<'JC2_INSTALLED_PINS'
364942819c8f80e1127ea7ccb0398adeec4aa22baa994161677d348d49c3d532  /opt/jc2-real-20260910T1022/f10-middle-real-runtime-astra-20260910.md
f2db01a4aa9b982c1d379082c7d2a6d36f2575724660282d2ff5e3f8b53e5e6e  /opt/jc2-real-20260910T1022/dispatch.py
d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4  /opt/jc2-real-20260910T1022/probe.py
4587133176acc66842f9ded5c6b6a6e37683ff9ffe980bf9f46e42088359d73d  /opt/jc2-real-20260910T1022/authority.py
44859af3084c3445522c8e73a88c0fc96a710375bcd9c9e50340fd4ce5de0dd2  /opt/jc2-real-20260910T1022/producer.py
9369f0f311da9848f7d708a77413cda9115a4d8376aa626d7efaf017b4f8043c  /opt/jc2-real-20260910T1022/checker.py
43643a6ee8546be56592237d62ac4b1a0ce16d47980c2ba895355f27ba015c4b  /opt/jc2-real-20260910T1022/ROOT-CARD.md
819d5e70a33d826e53658b5d007305e985040adf5ac29e23c1c6e2110218c192  /opt/jc2-real-20260910T1022/ROOT-STARTUP-DELTA.md
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-real-20260910T1022/run_capped.py
c3111895d6d9c8ea217124aad44aefb351faf244ea13037935673f8f8fd785e9  /opt/jc2-real-20260910T1022/f10-middle-real-code-astra-20260910.md
d3b8c09234d50b51b9dbcfaa7a9f341f34263540bd35e798c9f794137640c932  /opt/jc2-real-20260910T1022/f10-middle-real-code-gate-fable5-20260910.md
3f79cabecdb2c0f480bde3db644eac91ea5c8d3d472a3477f575b356993347ea  /opt/jc2-real-20260910T1022/f10-middle-real-domain-astra-20260910.md
f04c174e4b3111b2b9ee3e22e4ecceb619f0cfd2b9374e99a9ec9065cc52d21f  /opt/jc2-real-20260910T1022/f10-middle-real-domain-gate-fable5-20260910.md
8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012  /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-astra-20260910.md
dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad  /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-gate-fable5-20260910.md
82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6  /opt/jc2-real-20260910T1022/f10-middle-full-boundary-astra-20260910.md
8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491  /opt/jc2-real-20260910T1022/f10-middle-full-boundary-gate-fable5-20260910.md
890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5  /opt/jc2-real-20260910T1022/f10-middle-univariate-unit-astra-20260910.md
cff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62  /opt/jc2-real-20260910T1022/f10-middle-septic-gate-fable5-20260910.md
0562b82afa2b6f6da1e2c488d261fc65f22f705629c12446bbfeaf85bdccbef2  /opt/jc2-real-20260910T1022/f10-middle-real-runtime-gate-fable5-20260910.md
134e173289e4fb8e4f71e51e527b7dc5512075ca448512643e5bd942128692bf  /opt/jc2-real-20260910T1022/native-manifest.json
2f86ce99b0cfbd6a6bfd4725fff91f37d9f56e331eb028530741974b3702a7a1  /opt/jc2-real-20260910T1022/ROOT-REGISTRATION.json
7afb522325c3530eb7a99a6f29212f79c357f7871282cd56dd7dcfe24f036845  /opt/jc2-real-20260910T1022/ROOT-EXECUTION-CARD.md
JC2_INSTALLED_PINS
for jc2_file in /opt/jc2-real-20260910T1022/f10-middle-real-runtime-astra-20260910.md /opt/jc2-real-20260910T1022/dispatch.py /opt/jc2-real-20260910T1022/probe.py /opt/jc2-real-20260910T1022/authority.py /opt/jc2-real-20260910T1022/producer.py /opt/jc2-real-20260910T1022/checker.py /opt/jc2-real-20260910T1022/ROOT-CARD.md /opt/jc2-real-20260910T1022/ROOT-STARTUP-DELTA.md /opt/jc2-real-20260910T1022/run_capped.py /opt/jc2-real-20260910T1022/f10-middle-real-code-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-code-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-domain-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-domain-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-resonance-unit-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-full-boundary-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-full-boundary-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-univariate-unit-astra-20260910.md /opt/jc2-real-20260910T1022/f10-middle-septic-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/f10-middle-real-runtime-gate-fable5-20260910.md /opt/jc2-real-20260910T1022/native-manifest.json /opt/jc2-real-20260910T1022/ROOT-REGISTRATION.json /opt/jc2-real-20260910T1022/ROOT-EXECUTION-CARD.md; do
 /usr/bin/setpriv --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
test "$(stat -c %d /var/lib)" = 66305
install -d -o 0 -g 0 -m 0755 /run/jc2-real-20260910T1022
mount -t tmpfs -o size=16777216,mode=0755,nodev,nosuid tmpfs /run/jc2-real-20260910T1022
install -d -o 0 -g 0 -m 0755 /run/jc2-real-20260910T1022/authority /run/jc2-real-20260910T1022/frozen
install -d -o 65534 -g 65534 -m 0700 /run/jc2-real-20260910T1022/writer
stat -c '%d %u %g %a %n' /opt/jc2-real-20260910T1022 /run/jc2-real-20260910T1022 /run/jc2-real-20260910T1022/authority /run/jc2-real-20260910T1022/frozen /run/jc2-real-20260910T1022/writer
find /opt/jc2-real-20260910T1022 -maxdepth 1 -type f -printf '%f\n' | sort
systemd-run --unit=jc2-real-outer-term-20260910T1022 --on-calendar='2026-09-10 10:36:30 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-f10-middle-real-20260910T1022.service
systemd-run --unit=jc2-real-outer-kill-20260910T1022 --on-calendar='2026-09-10 10:36:35 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-f10-middle-real-20260910T1022.service
systemctl is-active jc2-real-outer-term-20260910T1022.timer jc2-real-outer-kill-20260910T1022.timer
date -u '+ROOT_OUTER_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --unit=jc2-f10-middle-real-20260910T1022.service --property=WorkingDirectory=/opt/jc2-real-20260910T1022 --property=RuntimeMaxSec=720 --property=TimeoutStopSec=5 --property=KillMode=control-group --property=MemoryMax=2300M --property=OOMPolicy=kill --property=TasksMax=32 --property=StandardOutput=file:/run/jc2-real-20260910T1022/dispatcher.stdout --property=StandardError=file:/run/jc2-real-20260910T1022/dispatcher.stderr /usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3.12 -I -S -B /opt/jc2-real-20260910T1022/dispatch.py --registration /opt/jc2-real-20260910T1022/ROOT-REGISTRATION.json
for jc2_try in $(seq 1 100); do
 jc2_main=$(systemctl show jc2-f10-middle-real-20260910T1022.service -p MainPID --value)
 if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
  systemctl show jc2-f10-middle-real-20260910T1022.service -p MainPID -p InvocationID -p ActiveState -p ControlGroup -p ExecMainStartTimestamp -p MemoryMax -p TasksMax -p RuntimeMaxUSec -p KillMode
  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  readlink /proc/"$jc2_main"/ns/pid
  for jc2_child in $(sed -n '1p' /proc/"$jc2_main"/task/"$jc2_main"/children); do
   ps -p "$jc2_child" -o pid=,ppid=,pgid=,lstart=,args=
  done
  date -u '+ROOT_SAME_LAUNCH_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  exit 0
 fi
 sleep 0.1
done
systemctl show jc2-f10-middle-real-20260910T1022.service -p MainPID -p ActiveState -p ExecMainStatus
exit 1
