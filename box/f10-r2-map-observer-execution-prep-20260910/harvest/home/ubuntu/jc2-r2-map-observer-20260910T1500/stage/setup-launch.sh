#!/bin/bash
# ROOT one-shot metadata-only two-refusal diagnostic, no semantic payload.
set -euo pipefail
test "$(id -u)" = 0
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0a30e221e2d8b2d29
test "$(hostname)" = ip-172-30-0-111
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 602d4427-0f4a-4df3-ac6e-4594036882cb
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 15:15:00 UTC' +%s)"
test ! -e /opt/jc2-r2-map-observer-20260910T1500
test ! -e /run/jc2-r2-map-observer-20260910T1500
test ! -e /var/lib/jc2-r2-map-observer-20260910T1500
test ! -e /usr/lib/python312.zip
test ! -L /usr/lib/python312.zip
cd /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage
sha256sum -c <<'JC2_STAGE_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  check.py
b4cea19b474a3238caf0871369baa5fc8497e1d1ac5cc6e107815372297640e2  dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  probe.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  run_capped.py
5003b730e59c1c6e246a093c1531128ca869698c89bc061f0074eb45d8b8324c  native-manifest.json
cfe844a45859fae74ce606d5781b8c26d28765c2e0ed3e85efec5cea8db7b4ad  ROOT-EXECUTION-CARD.md
1944f1d87853b35e0efcca72c8097cc35f70947a81a78d7b87b7025832f2c9ae  f10-r2-map-observer-gate-fable5-20260910.md
f62f7480201d89cf7a6bcd6419a8d239f661f3dc8fd30be3000248d7c86a5496  CONTRACT.md
f2aa0a04ac0231ba8892aef7e0c1dc6b8450d92e77868e53364c66f878b94d92  ROOT-REGISTRATION.json
f0cd3a7356e30beca2e7af93fa9587e64358dac3be2e3e5104288bf3c495856e  native.stdout
1744bef0855296b26f391bf079c636a0ef6304220d113dd679683532a56e4dad  native.sha256
JC2_STAGE_PINS
sha256sum -c native.sha256 > native-precheck.log
while read -r jc2_alias jc2_target; do
 test "$(readlink -e "$jc2_alias")" = "$jc2_target"
done < <(awk '$1=="ALIAS" {print $2, $3}' native.stdout)
while read -r jc2_dir; do
 jc2_expected=$(awk -v d="$jc2_dir" '$1=="ENTRY" && $2==d {print $3}' native.stdout)
 jc2_actual=$(find "$jc2_dir" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)
 test "$jc2_expected" = "$jc2_actual"
done < <(awk '$1=="DIRECTORY" {print $5}' native.stdout)
install -d -o 0 -g 0 -m 0755 /opt/jc2-r2-map-observer-20260910T1500 /opt/jc2-r2-map-observer-20260910T1500/science /opt/jc2-r2-map-observer-20260910T1500/wrapper /opt/jc2-r2-map-observer-20260910T1500/metadata
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/authority.py /opt/jc2-r2-map-observer-20260910T1500/science/authority.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/arithmetic.py /opt/jc2-r2-map-observer-20260910T1500/science/arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/produce.py /opt/jc2-r2-map-observer-20260910T1500/science/produce.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/check_arithmetic.py /opt/jc2-r2-map-observer-20260910T1500/science/check_arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/check.py /opt/jc2-r2-map-observer-20260910T1500/science/check.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/dispatch.py /opt/jc2-r2-map-observer-20260910T1500/wrapper/dispatch.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/probe.py /opt/jc2-r2-map-observer-20260910T1500/wrapper/probe.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/run_capped.py /opt/jc2-r2-map-observer-20260910T1500/metadata/run_capped.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/native-manifest.json /opt/jc2-r2-map-observer-20260910T1500/metadata/native-manifest.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/ROOT-EXECUTION-CARD.md /opt/jc2-r2-map-observer-20260910T1500/metadata/ROOT-EXECUTION-CARD.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/f10-r2-map-observer-gate-fable5-20260910.md /opt/jc2-r2-map-observer-20260910T1500/metadata/f10-r2-map-observer-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/CONTRACT.md /opt/jc2-r2-map-observer-20260910T1500/metadata/CONTRACT.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage/ROOT-REGISTRATION.json /opt/jc2-r2-map-observer-20260910T1500/metadata/ROOT-REGISTRATION.json
sha256sum -c <<'JC2_INSTALLED_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  /opt/jc2-r2-map-observer-20260910T1500/science/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  /opt/jc2-r2-map-observer-20260910T1500/science/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  /opt/jc2-r2-map-observer-20260910T1500/science/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  /opt/jc2-r2-map-observer-20260910T1500/science/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  /opt/jc2-r2-map-observer-20260910T1500/science/check.py
b4cea19b474a3238caf0871369baa5fc8497e1d1ac5cc6e107815372297640e2  /opt/jc2-r2-map-observer-20260910T1500/wrapper/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  /opt/jc2-r2-map-observer-20260910T1500/wrapper/probe.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-r2-map-observer-20260910T1500/metadata/run_capped.py
5003b730e59c1c6e246a093c1531128ca869698c89bc061f0074eb45d8b8324c  /opt/jc2-r2-map-observer-20260910T1500/metadata/native-manifest.json
cfe844a45859fae74ce606d5781b8c26d28765c2e0ed3e85efec5cea8db7b4ad  /opt/jc2-r2-map-observer-20260910T1500/metadata/ROOT-EXECUTION-CARD.md
1944f1d87853b35e0efcca72c8097cc35f70947a81a78d7b87b7025832f2c9ae  /opt/jc2-r2-map-observer-20260910T1500/metadata/f10-r2-map-observer-gate-fable5-20260910.md
f62f7480201d89cf7a6bcd6419a8d239f661f3dc8fd30be3000248d7c86a5496  /opt/jc2-r2-map-observer-20260910T1500/metadata/CONTRACT.md
f2aa0a04ac0231ba8892aef7e0c1dc6b8450d92e77868e53364c66f878b94d92  /opt/jc2-r2-map-observer-20260910T1500/metadata/ROOT-REGISTRATION.json
JC2_INSTALLED_PINS
for jc2_file in /opt/jc2-r2-map-observer-20260910T1500/science/authority.py /opt/jc2-r2-map-observer-20260910T1500/science/arithmetic.py /opt/jc2-r2-map-observer-20260910T1500/science/produce.py /opt/jc2-r2-map-observer-20260910T1500/science/check_arithmetic.py /opt/jc2-r2-map-observer-20260910T1500/science/check.py /opt/jc2-r2-map-observer-20260910T1500/wrapper/dispatch.py /opt/jc2-r2-map-observer-20260910T1500/wrapper/probe.py /opt/jc2-r2-map-observer-20260910T1500/metadata/run_capped.py /opt/jc2-r2-map-observer-20260910T1500/metadata/native-manifest.json /opt/jc2-r2-map-observer-20260910T1500/metadata/ROOT-EXECUTION-CARD.md /opt/jc2-r2-map-observer-20260910T1500/metadata/f10-r2-map-observer-gate-fable5-20260910.md /opt/jc2-r2-map-observer-20260910T1500/metadata/CONTRACT.md /opt/jc2-r2-map-observer-20260910T1500/metadata/ROOT-REGISTRATION.json; do
 test "$(stat -c '%u %g %a' "$jc2_file")" = '0 0 444'
 /usr/bin/setpriv --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
test "$(find /opt/jc2-r2-map-observer-20260910T1500/science -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' arithmetic.py authority.py check.py check_arithmetic.py produce.py)"
test "$(find /opt/jc2-r2-map-observer-20260910T1500/wrapper -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' dispatch.py probe.py)"
test "$(stat -c %d /var/lib)" = 66305
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-map-observer-20260910T1500
mount -t tmpfs -o size=16777216,mode=0755,nodev,nosuid tmpfs /run/jc2-r2-map-observer-20260910T1500
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-map-observer-20260910T1500/authority /run/jc2-r2-map-observer-20260910T1500/frozen
install -d -o 65534 -g 65534 -m 0700 /run/jc2-r2-map-observer-20260910T1500/writer
stat -c '%d %u %g %a %n' /opt/jc2-r2-map-observer-20260910T1500/science /opt/jc2-r2-map-observer-20260910T1500/wrapper /opt/jc2-r2-map-observer-20260910T1500/metadata /run/jc2-r2-map-observer-20260910T1500 /run/jc2-r2-map-observer-20260910T1500/authority /run/jc2-r2-map-observer-20260910T1500/frozen /run/jc2-r2-map-observer-20260910T1500/writer
systemd-run --unit=jc2-r2-mapobserver-outer-term-20260910T1500 --on-calendar='2026-09-10 15:27:15 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-f10-r2-map-observer-20260910T1500.service
systemd-run --unit=jc2-r2-mapobserver-outer-kill-20260910T1500 --on-calendar='2026-09-10 15:27:20 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-f10-r2-map-observer-20260910T1500.service
systemctl is-active jc2-r2-mapobserver-outer-term-20260910T1500.timer jc2-r2-mapobserver-outer-kill-20260910T1500.timer
date -u '+OBSERVER_SYSTEM_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --unit=jc2-f10-r2-map-observer-20260910T1500.service --property=WorkingDirectory=/opt/jc2-r2-map-observer-20260910T1500/wrapper --property=RuntimeMaxSec=660 --property=TimeoutStopSec=5 --property=KillMode=control-group --property=MemoryMax=2147483648 --property=OOMPolicy=kill --property=TasksMax=32 --property=LimitCPU=infinity --property=StandardOutput=file:/run/jc2-r2-map-observer-20260910T1500/outer.stdout --property=StandardError=file:/run/jc2-r2-map-observer-20260910T1500/outer.stderr /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC /usr/bin/python3.12 -I -S -B /opt/jc2-r2-map-observer-20260910T1500/wrapper/dispatch.py --registration /opt/jc2-r2-map-observer-20260910T1500/metadata/ROOT-REGISTRATION.json
for jc2_try in $(seq 1 100); do
 jc2_main=$(systemctl show jc2-f10-r2-map-observer-20260910T1500.service -p MainPID --value)
 if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
  systemctl show jc2-f10-r2-map-observer-20260910T1500.service -p MainPID -p InvocationID -p ActiveState -p ControlGroup -p ExecMainStartTimestamp -p MemoryMax -p TasksMax -p RuntimeMaxUSec -p KillMode -p LimitCPU
  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  readlink /proc/"$jc2_main"/ns/pid
  sed -n '1p' /sys/fs/cgroup/system.slice/jc2-f10-r2-map-observer-20260910T1500.service/memory.max
  date -u '+OBSERVER_SAME_CALL_MAIN_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  exit 0
 fi
 sleep 0.1
done
systemctl show jc2-f10-r2-map-observer-20260910T1500.service -p MainPID -p ExecMainPID -p ActiveState -p ExecMainStatus
exit 1

