#!/bin/bash
# ROOT one-shot fullunit fixed89/0 deployment. No science edits/retries.
set -euo pipefail
# Metadata-only template: refusing unresolved fields before any deployment.
if LC_ALL=C grep -q 'JC2_[A-Z][A-Z_]*_PLACEHOLDER' "$0"; then exit 2; fi
test "$(id -u)" = 0
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0941baf1a7ff9131b
test "$(hostname)" = ip-172-30-0-40
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 460f23fc-3966-4d65-a2ac-3aeecc56c542
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 18:16:00 UTC' +%s)"
test ! -e /opt/jc2-r2-fullunit-ready-20260910T1800-typefix
test ! -e /run/jc2-r2-fullunit-ready-20260910T1800-typefix
test ! -e /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix
test ! -e /usr/lib/python312.zip
test ! -L /usr/lib/python312.zip
cd /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage
if LC_ALL=C grep -q 'JC2_[A-Z][A-Z_]*_PLACEHOLDER' ROOT-REGISTRATION.json; then exit 2; fi
sha256sum -c <<'JC2_STAGE_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  check.py
b6998cae2d38e962777dc1064f39a841cfee3e5bb0fc3905599a5378aa78ff69  dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  probe.py
4548656af387b7e08df5bd5c56504f97c2d11d2b5375cbfbadde5304465c4c97  mutate.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  artifact.json
6ac39ea21b716938ae0c375e0dc6e7447a1aaba83fb71e96be1bd5bf7f349ffb  native-manifest.json
d5f147d3c816a2439ee34aec49928d07981fd571e5cc043a05c404ff4ca71c03  ROOT-EXECUTION-CARD.md
cb0da8dcfe19a033f9daad1de7de4e602a330f15a90c383824550522b8d847eb  CONTRACT.md
ed4173cff602b016951e178818bdfd3bef1fe7be5f8bfcdafce7ef1e6aa277ea  ROOT-REGISTRATION.json
c49b7dfabe6dc8cc5b7aaea485171a6b709fc6158f180ae1157afd90b3cf4b1f  fullunit-entry.py
60a290aee2ed5def7ed4242743f187dea755659f287707fa79c6c1e05f2d1f10  fullunit-produce.py
ccc3d2ddfca98f7faaed9df323fb90ec183b437b3c6b0bfcde0820186e667023  fullunit-check.py
eca8d1e56b4d119c346e56be9730281169097c747468cc195df26c961213e317  f10-r2-fullunit-runtime-gate-fable5-20260910.md
d6ff5b7ad5248b0ef2a57fb2dbda042a5f4f92237d78c4b12e651288b4de28f5  native.stdout
13ea6cfb00cc6be26967f50909214b7d14dd93dea8537011365ef6d7204238b1  native.sha256
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
install -d -o 0 -g 0 -m 0755 /opt/jc2-r2-fullunit-ready-20260910T1800-typefix /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/authority.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/authority.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/arithmetic.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/produce.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/produce.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/check_arithmetic.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check_arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/check.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/dispatch.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/dispatch.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/probe.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/probe.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/mutate.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/mutate.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/run_capped.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/run_capped.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/artifact.json /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/artifact.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native-manifest.json /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native-manifest.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/ROOT-EXECUTION-CARD.md /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-EXECUTION-CARD.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/CONTRACT.md /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/CONTRACT.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/ROOT-REGISTRATION.json /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-REGISTRATION.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/fullunit-entry.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/entry.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/fullunit-produce.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/produce.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/fullunit-check.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/check.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/f10-r2-fullunit-runtime-gate-fable5-20260910.md /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/f10-r2-fullunit-runtime-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native.stdout /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.stdout
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native.sha256 /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.sha256
sha256sum -c <<'JC2_INSTALLED_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check.py
b6998cae2d38e962777dc1064f39a841cfee3e5bb0fc3905599a5378aa78ff69  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/probe.py
4548656af387b7e08df5bd5c56504f97c2d11d2b5375cbfbadde5304465c4c97  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/mutate.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/artifact.json
6ac39ea21b716938ae0c375e0dc6e7447a1aaba83fb71e96be1bd5bf7f349ffb  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native-manifest.json
d5f147d3c816a2439ee34aec49928d07981fd571e5cc043a05c404ff4ca71c03  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-EXECUTION-CARD.md
cb0da8dcfe19a033f9daad1de7de4e602a330f15a90c383824550522b8d847eb  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/CONTRACT.md
ed4173cff602b016951e178818bdfd3bef1fe7be5f8bfcdafce7ef1e6aa277ea  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-REGISTRATION.json
c49b7dfabe6dc8cc5b7aaea485171a6b709fc6158f180ae1157afd90b3cf4b1f  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/entry.py
60a290aee2ed5def7ed4242743f187dea755659f287707fa79c6c1e05f2d1f10  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/produce.py
ccc3d2ddfca98f7faaed9df323fb90ec183b437b3c6b0bfcde0820186e667023  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/check.py
eca8d1e56b4d119c346e56be9730281169097c747468cc195df26c961213e317  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/f10-r2-fullunit-runtime-gate-fable5-20260910.md
d6ff5b7ad5248b0ef2a57fb2dbda042a5f4f92237d78c4b12e651288b4de28f5  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.stdout
13ea6cfb00cc6be26967f50909214b7d14dd93dea8537011365ef6d7204238b1  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.sha256
JC2_INSTALLED_PINS
for jc2_file in /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/authority.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/arithmetic.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/produce.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check_arithmetic.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/dispatch.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/probe.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/mutate.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/run_capped.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/artifact.json /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native-manifest.json /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-EXECUTION-CARD.md /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/CONTRACT.md /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-REGISTRATION.json /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/entry.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/produce.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/check.py /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/f10-r2-fullunit-runtime-gate-fable5-20260910.md /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.stdout /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.sha256; do
 test "$(stat -c '%u %g %a' "$jc2_file")" = '0 0 444'
 /usr/bin/setpriv --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
test "$(find /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' arithmetic.py authority.py check.py check_arithmetic.py produce.py)"
test "$(find /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' dispatch.py mutate.py probe.py)"
test "$(find /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' check.py entry.py produce.py)"
test "$(stat -c %d /var/lib)" = 66305
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-fullunit-ready-20260910T1800-typefix
mount -t tmpfs -o size=16777216,mode=0755,nodev,nosuid tmpfs /run/jc2-r2-fullunit-ready-20260910T1800-typefix
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen
install -d -o 65534 -g 65534 -m 0700 /run/jc2-r2-fullunit-ready-20260910T1800-typefix/writer
stat -c '%d %u %g %a %n' /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata /run/jc2-r2-fullunit-ready-20260910T1800-typefix /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen /run/jc2-r2-fullunit-ready-20260910T1800-typefix/writer
systemd-run --unit=jc2-r2-fullunit-ready-outer-term-20260910T1800-typefix --on-calendar='2026-09-10 18:27:15 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service
systemd-run --unit=jc2-r2-fullunit-ready-outer-kill-20260910T1800-typefix --on-calendar='2026-09-10 18:27:20 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service
systemctl is-active jc2-r2-fullunit-ready-outer-term-20260910T1800-typefix.timer jc2-r2-fullunit-ready-outer-kill-20260910T1800-typefix.timer
date -u '+R2_FULLUNIT_SYSTEM_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --unit=jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service --property=WorkingDirectory=/opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper --property=RuntimeMaxSec=660 --property=TimeoutStopSec=5 --property=KillMode=control-group --property=MemoryMax=2147483648 --property=OOMPolicy=kill --property=TasksMax=32 --property=LimitCPU=infinity --property=StandardOutput=file:/run/jc2-r2-fullunit-ready-20260910T1800-typefix/outer.stdout --property=StandardError=file:/run/jc2-r2-fullunit-ready-20260910T1800-typefix/outer.stderr /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC /usr/bin/python3.12 -I -S -B /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/dispatch.py --registration /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-REGISTRATION.json
for jc2_try in $(seq 1 100); do
 jc2_main=$(systemctl show jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service -p MainPID --value)
 if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
  systemctl show jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service -p MainPID -p InvocationID -p ActiveState -p ControlGroup -p ExecMainStartTimestamp -p MemoryMax -p TasksMax -p RuntimeMaxUSec -p KillMode -p LimitCPU
  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  readlink /proc/"$jc2_main"/ns/pid
  sed -n '1p' /sys/fs/cgroup/system.slice/jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service/memory.max
  date -u '+R2_FULLUNIT_SAME_CALL_MAIN_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  exit 0
 fi
 sleep 0.1
done
systemctl show jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service -p MainPID -p ActiveState -p ExecMainStatus
exit 1
