#!/bin/bash
# ROOT one-shot r2 deployment; immutable source copies, no science edits/retry.
set -euo pipefail
test "$(id -u)" = 0
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test "$(hostname)" = ip-172-30-0-72
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 7ed95cce-3312-4f55-bc76-4e7f37c4cf7e
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 12:49:00 UTC' +%s)"
test ! -e /opt/jc2-r2-20260910T1230
test ! -e /run/jc2-r2-20260910T1230
test ! -e /var/lib/jc2-r2-20260910T1230
test ! -e /usr/lib/python312.zip
test ! -L /usr/lib/python312.zip
cd /home/ubuntu/jc2-r2-native-20260910T1230/stage
sha256sum -c <<'JC2_STAGE_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  check.py
4838e40051bd19d19c35095eac2ee50de7d11d905b2da403a459c25d91f3a749  dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  probe.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  run_capped.py
947bb434fd80ce8cbe2df01c8f877715aa3e8e82afbf90aa0e1212f5ac73f9e7  f10-r2-reconstruction-code-astra-20260910.md
3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b  f10-r2-reconstruction-code-gate-fable5-20260910.md
002ff55c5d60e843011f988562d2e38a3cc36e1f497c5dd7e18e540e7fc7f8e7  f10-r2-runtime-astra-20260910.md
558fa2f1ef15b8477148fc014df4dcbcf783b61bcddae9889213b995bcb86e16  f10-r2-runtime-gate-fable5-20260910.md
2c06f0580356172c05ec5e860051d8a31bb6f3dc01a0b0d48075c4680c5180b5  CONTRACT.md
1e08bbddcf816b09344a0ec5bd7c1913515a93438810fa9b95240a0102d23edb  native-manifest.json
90b4d8a0a41b6a29bab30b3724db75a52ae3a5f5f209e46eceb1da8e5e541476  ROOT-EXECUTION-CARD.md
526edd84cd1457f8f2fc9cac0ca9d9aa24e71cf8e9fa5168c94344ab7832fd94  ROOT-REGISTRATION.json
2a7757ffd38d2ede1e47e48a1e9e52ccacc4c3bc4617e0a6efdec9938db6e1df  native-v2.stdout
7e101b69792fb2095da590f24657496e97cb0bf8037ad7c4d525d2ac00033bd7  native.sha256
JC2_STAGE_PINS
sha256sum -c native.sha256
while read -r jc2_alias jc2_target; do
 test "$(readlink -e "$jc2_alias")" = "$jc2_target"
done < <(awk '$1=="ALIAS" {print $2, $3}' native-v2.stdout)
while read -r jc2_dir; do
 jc2_expected=$(awk -v d="$jc2_dir" '$1=="ENTRY" && $2==d {print $3}' native-v2.stdout)
 jc2_actual=$(find "$jc2_dir" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)
 test "$jc2_expected" = "$jc2_actual"
done < <(awk '$1=="DIRECTORY" {print $5}' native-v2.stdout)
install -d -o 0 -g 0 -m 0755 /opt/jc2-r2-20260910T1230 /opt/jc2-r2-20260910T1230/science /opt/jc2-r2-20260910T1230/wrapper /opt/jc2-r2-20260910T1230/metadata
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/authority.py /opt/jc2-r2-20260910T1230/science/authority.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/arithmetic.py /opt/jc2-r2-20260910T1230/science/arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/produce.py /opt/jc2-r2-20260910T1230/science/produce.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/check_arithmetic.py /opt/jc2-r2-20260910T1230/science/check_arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/check.py /opt/jc2-r2-20260910T1230/science/check.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/dispatch.py /opt/jc2-r2-20260910T1230/wrapper/dispatch.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/probe.py /opt/jc2-r2-20260910T1230/wrapper/probe.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/run_capped.py /opt/jc2-r2-20260910T1230/metadata/run_capped.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/f10-r2-reconstruction-code-astra-20260910.md /opt/jc2-r2-20260910T1230/metadata/f10-r2-reconstruction-code-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/f10-r2-reconstruction-code-gate-fable5-20260910.md /opt/jc2-r2-20260910T1230/metadata/f10-r2-reconstruction-code-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/f10-r2-runtime-astra-20260910.md /opt/jc2-r2-20260910T1230/metadata/f10-r2-runtime-astra-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/f10-r2-runtime-gate-fable5-20260910.md /opt/jc2-r2-20260910T1230/metadata/f10-r2-runtime-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/CONTRACT.md /opt/jc2-r2-20260910T1230/metadata/CONTRACT.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/native-manifest.json /opt/jc2-r2-20260910T1230/metadata/native-manifest.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/ROOT-EXECUTION-CARD.md /opt/jc2-r2-20260910T1230/metadata/ROOT-EXECUTION-CARD.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-native-20260910T1230/stage/ROOT-REGISTRATION.json /opt/jc2-r2-20260910T1230/metadata/ROOT-REGISTRATION.json
sha256sum -c <<'JC2_INSTALLED_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  /opt/jc2-r2-20260910T1230/science/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  /opt/jc2-r2-20260910T1230/science/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  /opt/jc2-r2-20260910T1230/science/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  /opt/jc2-r2-20260910T1230/science/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  /opt/jc2-r2-20260910T1230/science/check.py
4838e40051bd19d19c35095eac2ee50de7d11d905b2da403a459c25d91f3a749  /opt/jc2-r2-20260910T1230/wrapper/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  /opt/jc2-r2-20260910T1230/wrapper/probe.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-r2-20260910T1230/metadata/run_capped.py
947bb434fd80ce8cbe2df01c8f877715aa3e8e82afbf90aa0e1212f5ac73f9e7  /opt/jc2-r2-20260910T1230/metadata/f10-r2-reconstruction-code-astra-20260910.md
3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b  /opt/jc2-r2-20260910T1230/metadata/f10-r2-reconstruction-code-gate-fable5-20260910.md
002ff55c5d60e843011f988562d2e38a3cc36e1f497c5dd7e18e540e7fc7f8e7  /opt/jc2-r2-20260910T1230/metadata/f10-r2-runtime-astra-20260910.md
558fa2f1ef15b8477148fc014df4dcbcf783b61bcddae9889213b995bcb86e16  /opt/jc2-r2-20260910T1230/metadata/f10-r2-runtime-gate-fable5-20260910.md
2c06f0580356172c05ec5e860051d8a31bb6f3dc01a0b0d48075c4680c5180b5  /opt/jc2-r2-20260910T1230/metadata/CONTRACT.md
1e08bbddcf816b09344a0ec5bd7c1913515a93438810fa9b95240a0102d23edb  /opt/jc2-r2-20260910T1230/metadata/native-manifest.json
90b4d8a0a41b6a29bab30b3724db75a52ae3a5f5f209e46eceb1da8e5e541476  /opt/jc2-r2-20260910T1230/metadata/ROOT-EXECUTION-CARD.md
526edd84cd1457f8f2fc9cac0ca9d9aa24e71cf8e9fa5168c94344ab7832fd94  /opt/jc2-r2-20260910T1230/metadata/ROOT-REGISTRATION.json
JC2_INSTALLED_PINS
for jc2_file in /opt/jc2-r2-20260910T1230/science/authority.py /opt/jc2-r2-20260910T1230/science/arithmetic.py /opt/jc2-r2-20260910T1230/science/produce.py /opt/jc2-r2-20260910T1230/science/check_arithmetic.py /opt/jc2-r2-20260910T1230/science/check.py /opt/jc2-r2-20260910T1230/wrapper/dispatch.py /opt/jc2-r2-20260910T1230/wrapper/probe.py /opt/jc2-r2-20260910T1230/metadata/run_capped.py /opt/jc2-r2-20260910T1230/metadata/f10-r2-reconstruction-code-astra-20260910.md /opt/jc2-r2-20260910T1230/metadata/f10-r2-reconstruction-code-gate-fable5-20260910.md /opt/jc2-r2-20260910T1230/metadata/f10-r2-runtime-astra-20260910.md /opt/jc2-r2-20260910T1230/metadata/f10-r2-runtime-gate-fable5-20260910.md /opt/jc2-r2-20260910T1230/metadata/CONTRACT.md /opt/jc2-r2-20260910T1230/metadata/native-manifest.json /opt/jc2-r2-20260910T1230/metadata/ROOT-EXECUTION-CARD.md /opt/jc2-r2-20260910T1230/metadata/ROOT-REGISTRATION.json; do
 test "$(stat -c '%u %g %a' "$jc2_file")" = '0 0 444'
 /usr/bin/setpriv --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
test "$(find /opt/jc2-r2-20260910T1230/science -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' arithmetic.py authority.py check.py check_arithmetic.py produce.py)"
test "$(find /opt/jc2-r2-20260910T1230/wrapper -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' dispatch.py probe.py)"
test "$(stat -c %d /var/lib)" = 66305
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-20260910T1230
mount -t tmpfs -o size=16777216,mode=0755,nodev,nosuid tmpfs /run/jc2-r2-20260910T1230
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-20260910T1230/authority /run/jc2-r2-20260910T1230/frozen
install -d -o 65534 -g 65534 -m 0700 /run/jc2-r2-20260910T1230/writer
stat -c '%d %u %g %a %n' /opt/jc2-r2-20260910T1230/science /opt/jc2-r2-20260910T1230/wrapper /opt/jc2-r2-20260910T1230/metadata /run/jc2-r2-20260910T1230 /run/jc2-r2-20260910T1230/authority /run/jc2-r2-20260910T1230/frozen /run/jc2-r2-20260910T1230/writer
systemd-run --unit=jc2-r2-outer-term-20260910T1230 --on-calendar='2026-09-10 13:03:15 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-f10-r2-20260910T1230.service
systemd-run --unit=jc2-r2-outer-kill-20260910T1230 --on-calendar='2026-09-10 13:03:20 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-f10-r2-20260910T1230.service
systemctl is-active jc2-r2-outer-term-20260910T1230.timer jc2-r2-outer-kill-20260910T1230.timer
date -u '+R2_SYSTEM_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --unit=jc2-f10-r2-20260910T1230.service --property=WorkingDirectory=/opt/jc2-r2-20260910T1230/wrapper --property=RuntimeMaxSec=660 --property=TimeoutStopSec=5 --property=KillMode=control-group --property=MemoryMax=2147483648 --property=OOMPolicy=kill --property=TasksMax=32 --property=LimitCPU=infinity --property=StandardOutput=file:/run/jc2-r2-20260910T1230/outer.stdout --property=StandardError=file:/run/jc2-r2-20260910T1230/outer.stderr /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC /usr/bin/python3.12 -I -S -B /opt/jc2-r2-20260910T1230/wrapper/dispatch.py --registration /opt/jc2-r2-20260910T1230/metadata/ROOT-REGISTRATION.json
for jc2_try in $(seq 1 100); do
 jc2_main=$(systemctl show jc2-f10-r2-20260910T1230.service -p MainPID --value)
 if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
  systemctl show jc2-f10-r2-20260910T1230.service -p MainPID -p InvocationID -p ActiveState -p ControlGroup -p ExecMainStartTimestamp -p MemoryMax -p TasksMax -p RuntimeMaxUSec -p KillMode -p LimitCPU
  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  readlink /proc/"$jc2_main"/ns/pid
  sed -n '1p' /sys/fs/cgroup/system.slice/jc2-f10-r2-20260910T1230.service/memory.max
  date -u '+R2_SAME_CALL_MAIN_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  exit 0
 fi
 sleep 0.1
done
systemctl show jc2-f10-r2-20260910T1230.service -p MainPID -p ActiveState -p ExecMainStatus
exit 1
