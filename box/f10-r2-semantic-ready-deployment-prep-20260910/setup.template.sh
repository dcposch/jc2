#!/bin/bash
# ROOT one-shot semantic6/10 deployment. No science edits/retries.
set -euo pipefail
# Metadata-only template: refusing unresolved fields before any deployment.
if LC_ALL=C grep -q 'JC2_[A-Z][A-Z_]*_PLACEHOLDER' "$0"; then exit 2; fi
test "$(id -u)" = 0
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = JC2_INSTANCE_ID_PLACEHOLDER
test "$(hostname)" = JC2_HOSTNAME_PLACEHOLDER
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = JC2_BOOT_ID_PLACEHOLDER
test "$(readlink /proc/self/ns/pid)" = 'JC2_PID_NAMESPACE_PLACEHOLDER'
test "$(date -u +%s)" -lt "$(date -ud 'JC2_SETUP_ADMISSION_PLACEHOLDER' +%s)"
test ! -e /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER
test ! -e /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER
test ! -e /var/lib/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER
test ! -e /usr/lib/python312.zip
test ! -L /usr/lib/python312.zip
cd /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage
sha256sum -c <<'JC2_STAGE_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  check.py
6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b  dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  probe.py
a896a8094be9b38f7ffa3a82cab15d340add0d7ab5f513340b2b7f916e489540  mutate_controls.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  artifact.json
JC2_NATIVE_MANIFEST_SHA_PLACEHOLDER  native-manifest.json
JC2_ROOT_CARD_SHA_PLACEHOLDER  ROOT-EXECUTION-CARD.md
469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b  f10-r2-semantic-code-gate-fable5-20260910.md
3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b  f10-r2-reconstruction-code-gate-fable5-20260910.md
3bce51215a7c746acb4bd5bc833f2644e5f2b1ac89e8681cdea2c65dfba00b0c  f10-r2-actual-result-gate-fable5-20260910.md
edd4c71e86d0d5cac2ee277de69199522a2a5bca9381833f19dc078e9759ea19  CONTRACT.md
JC2_ROOT_REGISTRATION_SHA_PLACEHOLDER  ROOT-REGISTRATION.json
JC2_NATIVE_RAW_SHA_PLACEHOLDER  native.stdout
JC2_NATIVE_HASHLIST_SHA_PLACEHOLDER  native.sha256
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
install -d -o 0 -g 0 -m 0755 /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/authority.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/authority.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/arithmetic.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/produce.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/produce.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/check_arithmetic.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/check_arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/check.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/check.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/dispatch.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/dispatch.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/probe.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/probe.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/mutate_controls.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/mutate_controls.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/run_capped.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/run_capped.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/artifact.json /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/artifact.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/native-manifest.json /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native-manifest.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/ROOT-EXECUTION-CARD.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-EXECUTION-CARD.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/f10-r2-semantic-code-gate-fable5-20260910.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-semantic-code-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/f10-r2-reconstruction-code-gate-fable5-20260910.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-reconstruction-code-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/f10-r2-actual-result-gate-fable5-20260910.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-actual-result-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/CONTRACT.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/CONTRACT.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/stage/ROOT-REGISTRATION.json /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-REGISTRATION.json
sha256sum -c <<'JC2_INSTALLED_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/check.py
6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/probe.py
a896a8094be9b38f7ffa3a82cab15d340add0d7ab5f513340b2b7f916e489540  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/mutate_controls.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/artifact.json
JC2_NATIVE_MANIFEST_SHA_PLACEHOLDER  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native-manifest.json
JC2_ROOT_CARD_SHA_PLACEHOLDER  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-EXECUTION-CARD.md
469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-semantic-code-gate-fable5-20260910.md
3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-reconstruction-code-gate-fable5-20260910.md
3bce51215a7c746acb4bd5bc833f2644e5f2b1ac89e8681cdea2c65dfba00b0c  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-actual-result-gate-fable5-20260910.md
edd4c71e86d0d5cac2ee277de69199522a2a5bca9381833f19dc078e9759ea19  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/CONTRACT.md
JC2_ROOT_REGISTRATION_SHA_PLACEHOLDER  /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-REGISTRATION.json
JC2_INSTALLED_PINS
for jc2_file in /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/authority.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/arithmetic.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/produce.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/check_arithmetic.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science/check.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/dispatch.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/probe.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/mutate_controls.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/run_capped.py /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/artifact.json /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native-manifest.json /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-EXECUTION-CARD.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-semantic-code-gate-fable5-20260910.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-reconstruction-code-gate-fable5-20260910.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-r2-actual-result-gate-fable5-20260910.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/CONTRACT.md /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-REGISTRATION.json; do
 test "$(stat -c '%u %g %a' "$jc2_file")" = '0 0 444'
 /usr/bin/setpriv --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
test "$(find /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' arithmetic.py authority.py check.py check_arithmetic.py produce.py)"
test "$(find /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' dispatch.py mutate_controls.py probe.py)"
test "$(stat -c %d /var/lib)" = JC2_DURABLE_DEVICE_PLACEHOLDER
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER
mount -t tmpfs -o size=16777216,mode=0755,nodev,nosuid tmpfs /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/authority /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/frozen
install -d -o 65534 -g 65534 -m 0700 /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/writer
stat -c '%d %u %g %a %n' /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/science /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/authority /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/frozen /run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/writer
systemd-run --unit=jc2-r2-controls-ready-outer-term-JC2_BATCH_SUFFIX_PLACEHOLDER --on-calendar='JC2_SYSTEM_TERM_PLACEHOLDER' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-f10-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER.service
systemd-run --unit=jc2-r2-controls-ready-outer-kill-JC2_BATCH_SUFFIX_PLACEHOLDER --on-calendar='JC2_SYSTEM_KILL_PLACEHOLDER' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-f10-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER.service
systemctl is-active jc2-r2-controls-ready-outer-term-JC2_BATCH_SUFFIX_PLACEHOLDER.timer jc2-r2-controls-ready-outer-kill-JC2_BATCH_SUFFIX_PLACEHOLDER.timer
date -u '+R2_SEMANTIC_SYSTEM_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --unit=jc2-f10-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER.service --property=WorkingDirectory=/opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper --property=RuntimeMaxSec=660 --property=TimeoutStopSec=5 --property=KillMode=control-group --property=MemoryMax=2147483648 --property=OOMPolicy=kill --property=TasksMax=32 --property=LimitCPU=infinity --property=StandardOutput=file:/run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/outer.stdout --property=StandardError=file:/run/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/outer.stderr /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC /usr/bin/python3.12 -I -S -B /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/wrapper/dispatch.py --registration /opt/jc2-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-REGISTRATION.json
for jc2_try in $(seq 1 100); do
 jc2_main=$(systemctl show jc2-f10-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER.service -p MainPID --value)
 if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
  systemctl show jc2-f10-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER.service -p MainPID -p InvocationID -p ActiveState -p ControlGroup -p ExecMainStartTimestamp -p MemoryMax -p TasksMax -p RuntimeMaxUSec -p KillMode -p LimitCPU
  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  readlink /proc/"$jc2_main"/ns/pid
  sed -n '1p' /sys/fs/cgroup/system.slice/jc2-f10-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER.service/memory.max
  date -u '+R2_SEMANTIC_SAME_CALL_MAIN_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  exit 0
 fi
 sleep 0.1
done
systemctl show jc2-f10-r2-controls-ready-JC2_BATCH_SUFFIX_PLACEHOLDER.service -p MainPID -p ActiveState -p ExecMainStatus
exit 1
