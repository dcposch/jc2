#!/bin/bash
# ROOT one-shot highest fixed89/0 deployment. No science edits/retries.
set -euo pipefail
# Metadata-only template: refusing unresolved fields before any deployment.
if LC_ALL=C grep -q 'JC2_[A-Z][A-Z_]*_PLACEHOLDER' "$0"; then exit 2; fi
test "$(id -u)" = 0
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-05b82c8e457c586ce
test "$(hostname)" = ip-172-30-0-164
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 6e13db88-d1a2-45cd-aa1b-028d8e070589
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 17:32:00 UTC' +%s)"
test ! -e /opt/jc2-r2-highest-ready-20260910T1720
test ! -e /run/jc2-r2-highest-ready-20260910T1720
test ! -e /var/lib/jc2-r2-highest-ready-20260910T1720
test ! -e /usr/lib/python312.zip
test ! -L /usr/lib/python312.zip
cd /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage
if LC_ALL=C grep -q 'JC2_[A-Z][A-Z_]*_PLACEHOLDER' ROOT-REGISTRATION.json; then exit 2; fi
sha256sum -c <<'JC2_STAGE_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  check.py
396dc3b42f082ffbc08516a3dd41528516e2e69e3994fc005b22b79b3a605927  dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  probe.py
3d68ec187f77dc1906f177d8f487f1d037dd0a1aa4b46329632ee6f27f315225  mutate.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  artifact.json
36876aac2d52c61591d833b8c473583f0296829034f5a84eef64b56a7dc7c007  native-manifest.json
bb647ddf5f3eb1a36e759cbbab58869c52d60cebf9edc2c8a8016faf4f35b11d  ROOT-EXECUTION-CARD.md
f0bfb025d5445f5cb16b48c29ff0d9aef909616216482c52973bd5c8f37f4318  CONTRACT.md
476ebfff4ec5ddb46e656d87e4509d5e61f731704a0a5a5ae2d63acd5b1ba887  ROOT-REGISTRATION.json
8afc9b158483183e1afefef65c5aad54a8a46615b0f3b3d4682812c8dd8d74b2  highest-entry.py
6f094c4b468afe7e9f09d8b0d4ee4f33faa3017afb9809eaa312ff2f70904913  highest-produce.py
1e685c413484f90d68db77bba844cb220f0d1b86c33c1d82ac9f587ad76c15f5  highest-check.py
85ce5e9ab2067ae07033fca52e0c4d0c8853032133f9799d388d8d0745c24698  f10-r2-highest-status-fix-gate-fable5-20260910.md
8358693287a2874f05b431ab0081c98db9461bdc6eaf06be33f40a2f83c72ca8  f10-r2-highest-modular-runtime-gate-fable5-20260910.md
82ad9bec15b2d8f3465dce7a0cbcc46d92b7f85dda0d6e3c014720081cc2143e  native.stdout
e1a625094c5213fe29c247aadd2f27232c18889289957e0311fba7ca62b5be7a  native.sha256
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
install -d -o 0 -g 0 -m 0755 /opt/jc2-r2-highest-ready-20260910T1720 /opt/jc2-r2-highest-ready-20260910T1720/science /opt/jc2-r2-highest-ready-20260910T1720/wrapper /opt/jc2-r2-highest-ready-20260910T1720/highest /opt/jc2-r2-highest-ready-20260910T1720/metadata
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/authority.py /opt/jc2-r2-highest-ready-20260910T1720/science/authority.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/arithmetic.py /opt/jc2-r2-highest-ready-20260910T1720/science/arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/produce.py /opt/jc2-r2-highest-ready-20260910T1720/science/produce.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/check_arithmetic.py /opt/jc2-r2-highest-ready-20260910T1720/science/check_arithmetic.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/check.py /opt/jc2-r2-highest-ready-20260910T1720/science/check.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/dispatch.py /opt/jc2-r2-highest-ready-20260910T1720/wrapper/dispatch.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/probe.py /opt/jc2-r2-highest-ready-20260910T1720/wrapper/probe.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/mutate.py /opt/jc2-r2-highest-ready-20260910T1720/wrapper/mutate.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/run_capped.py /opt/jc2-r2-highest-ready-20260910T1720/metadata/run_capped.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/artifact.json /opt/jc2-r2-highest-ready-20260910T1720/metadata/artifact.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/native-manifest.json /opt/jc2-r2-highest-ready-20260910T1720/metadata/native-manifest.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/ROOT-EXECUTION-CARD.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/ROOT-EXECUTION-CARD.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/CONTRACT.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/CONTRACT.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/ROOT-REGISTRATION.json /opt/jc2-r2-highest-ready-20260910T1720/metadata/ROOT-REGISTRATION.json
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/highest-entry.py /opt/jc2-r2-highest-ready-20260910T1720/highest/entry.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/highest-produce.py /opt/jc2-r2-highest-ready-20260910T1720/highest/produce.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/highest-check.py /opt/jc2-r2-highest-ready-20260910T1720/highest/check.py
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/f10-r2-highest-status-fix-gate-fable5-20260910.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/f10-r2-highest-status-fix-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/f10-r2-highest-modular-runtime-gate-fable5-20260910.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/f10-r2-highest-modular-runtime-gate-fable5-20260910.md
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/native.stdout /opt/jc2-r2-highest-ready-20260910T1720/metadata/native.stdout
install -o 0 -g 0 -m 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage/native.sha256 /opt/jc2-r2-highest-ready-20260910T1720/metadata/native.sha256
sha256sum -c <<'JC2_INSTALLED_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  /opt/jc2-r2-highest-ready-20260910T1720/science/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  /opt/jc2-r2-highest-ready-20260910T1720/science/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  /opt/jc2-r2-highest-ready-20260910T1720/science/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  /opt/jc2-r2-highest-ready-20260910T1720/science/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  /opt/jc2-r2-highest-ready-20260910T1720/science/check.py
396dc3b42f082ffbc08516a3dd41528516e2e69e3994fc005b22b79b3a605927  /opt/jc2-r2-highest-ready-20260910T1720/wrapper/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  /opt/jc2-r2-highest-ready-20260910T1720/wrapper/probe.py
3d68ec187f77dc1906f177d8f487f1d037dd0a1aa4b46329632ee6f27f315225  /opt/jc2-r2-highest-ready-20260910T1720/wrapper/mutate.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-r2-highest-ready-20260910T1720/metadata/run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  /opt/jc2-r2-highest-ready-20260910T1720/metadata/artifact.json
36876aac2d52c61591d833b8c473583f0296829034f5a84eef64b56a7dc7c007  /opt/jc2-r2-highest-ready-20260910T1720/metadata/native-manifest.json
bb647ddf5f3eb1a36e759cbbab58869c52d60cebf9edc2c8a8016faf4f35b11d  /opt/jc2-r2-highest-ready-20260910T1720/metadata/ROOT-EXECUTION-CARD.md
f0bfb025d5445f5cb16b48c29ff0d9aef909616216482c52973bd5c8f37f4318  /opt/jc2-r2-highest-ready-20260910T1720/metadata/CONTRACT.md
476ebfff4ec5ddb46e656d87e4509d5e61f731704a0a5a5ae2d63acd5b1ba887  /opt/jc2-r2-highest-ready-20260910T1720/metadata/ROOT-REGISTRATION.json
8afc9b158483183e1afefef65c5aad54a8a46615b0f3b3d4682812c8dd8d74b2  /opt/jc2-r2-highest-ready-20260910T1720/highest/entry.py
6f094c4b468afe7e9f09d8b0d4ee4f33faa3017afb9809eaa312ff2f70904913  /opt/jc2-r2-highest-ready-20260910T1720/highest/produce.py
1e685c413484f90d68db77bba844cb220f0d1b86c33c1d82ac9f587ad76c15f5  /opt/jc2-r2-highest-ready-20260910T1720/highest/check.py
85ce5e9ab2067ae07033fca52e0c4d0c8853032133f9799d388d8d0745c24698  /opt/jc2-r2-highest-ready-20260910T1720/metadata/f10-r2-highest-status-fix-gate-fable5-20260910.md
8358693287a2874f05b431ab0081c98db9461bdc6eaf06be33f40a2f83c72ca8  /opt/jc2-r2-highest-ready-20260910T1720/metadata/f10-r2-highest-modular-runtime-gate-fable5-20260910.md
82ad9bec15b2d8f3465dce7a0cbcc46d92b7f85dda0d6e3c014720081cc2143e  /opt/jc2-r2-highest-ready-20260910T1720/metadata/native.stdout
e1a625094c5213fe29c247aadd2f27232c18889289957e0311fba7ca62b5be7a  /opt/jc2-r2-highest-ready-20260910T1720/metadata/native.sha256
JC2_INSTALLED_PINS
for jc2_file in /opt/jc2-r2-highest-ready-20260910T1720/science/authority.py /opt/jc2-r2-highest-ready-20260910T1720/science/arithmetic.py /opt/jc2-r2-highest-ready-20260910T1720/science/produce.py /opt/jc2-r2-highest-ready-20260910T1720/science/check_arithmetic.py /opt/jc2-r2-highest-ready-20260910T1720/science/check.py /opt/jc2-r2-highest-ready-20260910T1720/wrapper/dispatch.py /opt/jc2-r2-highest-ready-20260910T1720/wrapper/probe.py /opt/jc2-r2-highest-ready-20260910T1720/wrapper/mutate.py /opt/jc2-r2-highest-ready-20260910T1720/metadata/run_capped.py /opt/jc2-r2-highest-ready-20260910T1720/metadata/artifact.json /opt/jc2-r2-highest-ready-20260910T1720/metadata/native-manifest.json /opt/jc2-r2-highest-ready-20260910T1720/metadata/ROOT-EXECUTION-CARD.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/CONTRACT.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/ROOT-REGISTRATION.json /opt/jc2-r2-highest-ready-20260910T1720/highest/entry.py /opt/jc2-r2-highest-ready-20260910T1720/highest/produce.py /opt/jc2-r2-highest-ready-20260910T1720/highest/check.py /opt/jc2-r2-highest-ready-20260910T1720/metadata/f10-r2-highest-status-fix-gate-fable5-20260910.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/f10-r2-highest-modular-runtime-gate-fable5-20260910.md /opt/jc2-r2-highest-ready-20260910T1720/metadata/native.stdout /opt/jc2-r2-highest-ready-20260910T1720/metadata/native.sha256; do
 test "$(stat -c '%u %g %a' "$jc2_file")" = '0 0 444'
 /usr/bin/setpriv --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
test "$(find /opt/jc2-r2-highest-ready-20260910T1720/science -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' arithmetic.py authority.py check.py check_arithmetic.py produce.py)"
test "$(find /opt/jc2-r2-highest-ready-20260910T1720/wrapper -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' dispatch.py mutate.py probe.py)"
test "$(find /opt/jc2-r2-highest-ready-20260910T1720/highest -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf '%s\n' check.py entry.py produce.py)"
test "$(stat -c %d /var/lib)" = 66305
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-highest-ready-20260910T1720
mount -t tmpfs -o size=16777216,mode=0755,nodev,nosuid tmpfs /run/jc2-r2-highest-ready-20260910T1720
install -d -o 0 -g 0 -m 0755 /run/jc2-r2-highest-ready-20260910T1720/authority /run/jc2-r2-highest-ready-20260910T1720/frozen
install -d -o 65534 -g 65534 -m 0700 /run/jc2-r2-highest-ready-20260910T1720/writer
stat -c '%d %u %g %a %n' /opt/jc2-r2-highest-ready-20260910T1720/science /opt/jc2-r2-highest-ready-20260910T1720/wrapper /opt/jc2-r2-highest-ready-20260910T1720/highest /opt/jc2-r2-highest-ready-20260910T1720/metadata /run/jc2-r2-highest-ready-20260910T1720 /run/jc2-r2-highest-ready-20260910T1720/authority /run/jc2-r2-highest-ready-20260910T1720/frozen /run/jc2-r2-highest-ready-20260910T1720/writer
systemd-run --unit=jc2-r2-highest-ready-outer-term-20260910T1720 --on-calendar='2026-09-10 17:43:15 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-f10-r2-highest-ready-20260910T1720.service
systemd-run --unit=jc2-r2-highest-ready-outer-kill-20260910T1720 --on-calendar='2026-09-10 17:43:20 UTC' --timer-property=AccuracySec=1s /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-f10-r2-highest-ready-20260910T1720.service
systemctl is-active jc2-r2-highest-ready-outer-term-20260910T1720.timer jc2-r2-highest-ready-outer-kill-20260910T1720.timer
date -u '+R2_HIGHEST_SYSTEM_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --unit=jc2-f10-r2-highest-ready-20260910T1720.service --property=WorkingDirectory=/opt/jc2-r2-highest-ready-20260910T1720/wrapper --property=RuntimeMaxSec=660 --property=TimeoutStopSec=5 --property=KillMode=control-group --property=MemoryMax=2147483648 --property=OOMPolicy=kill --property=TasksMax=32 --property=LimitCPU=infinity --property=StandardOutput=file:/run/jc2-r2-highest-ready-20260910T1720/outer.stdout --property=StandardError=file:/run/jc2-r2-highest-ready-20260910T1720/outer.stderr /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC /usr/bin/python3.12 -I -S -B /opt/jc2-r2-highest-ready-20260910T1720/wrapper/dispatch.py --registration /opt/jc2-r2-highest-ready-20260910T1720/metadata/ROOT-REGISTRATION.json
for jc2_try in $(seq 1 100); do
 jc2_main=$(systemctl show jc2-f10-r2-highest-ready-20260910T1720.service -p MainPID --value)
 if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
  systemctl show jc2-f10-r2-highest-ready-20260910T1720.service -p MainPID -p InvocationID -p ActiveState -p ControlGroup -p ExecMainStartTimestamp -p MemoryMax -p TasksMax -p RuntimeMaxUSec -p KillMode -p LimitCPU
  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  readlink /proc/"$jc2_main"/ns/pid
  sed -n '1p' /sys/fs/cgroup/system.slice/jc2-f10-r2-highest-ready-20260910T1720.service/memory.max
  date -u '+R2_HIGHEST_SAME_CALL_MAIN_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  exit 0
 fi
 sleep 0.1
done
systemctl show jc2-f10-r2-highest-ready-20260910T1720.service -p MainPID -p ActiveState -p ExecMainStatus
exit 1
