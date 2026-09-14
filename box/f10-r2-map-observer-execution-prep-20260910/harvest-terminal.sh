#!/bin/bash
# ROOT custody-only terminal harvest; no mathematical execution.
set -euo pipefail
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0a30e221e2d8b2d29
test "$(tr -d '\n' < /proc/sys/kernel/random/boot_id)" = 602d4427-0f4a-4df3-ac6e-4594036882cb
test "$(systemctl show jc2-f10-r2-map-observer-20260910T1500.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-map-observer-20260910T1500.service -p ControlPID --value)" = 0
test ! -e /proc/8389
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-map-observer-20260910T1500.service
date -u '+QUIET_VERIFIED %FT%T.%NZ'
sha256sum /var/lib/jc2-r2-map-observer-20260910T1500/CUSTODY.json
sed -n '1,300p' /var/lib/jc2-r2-map-observer-20260910T1500/CUSTODY.json
cd /home/ubuntu/jc2-r2-map-observer-20260910T1500/stage
sha256sum -c terminal-files.sha256 > terminal-files-recheck.log
sha256sum -c <<'JC2_INSTALLED_PINS' > installed-postcheck.log
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
printf '%s\n' '1c9e90633abdcb921e23bb505163a04b400ddc4bf859d1500b26913b503a1bd1  native-metadata.sh' '1744bef0855296b26f391bf079c636a0ef6304220d113dd679683532a56e4dad  native.sha256' 'f0cd3a7356e30beca2e7af93fa9587e64358dac3be2e3e5104288bf3c495856e  native.stdout' | sha256sum -c
sha256sum -c native.sha256 > native-postcheck.log
timeout --signal=TERM --kill-after=5s 180s /bin/bash native-metadata.sh > native-post.stdout 2> native-post.stderr
test ! -s native-post.stderr
cmp <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native-post.stdout)
printf '%s\n' 'NATIVE_FILES_ALIASES_DIRECTORIES_STAT_COUNTS_IDENTICAL'
printf '%s\n' 'abdf8ebc85486a018ad2f8f61d3f31ae829f99f29291d434958b679b7fce388d  /etc/ld.so.cache' | sha256sum -c
cp --preserve=mode,timestamps /etc/ld.so.cache ld.so.cache.post-observation
printf '%s\n' 'abdf8ebc85486a018ad2f8f61d3f31ae829f99f29291d434958b679b7fce388d  ld.so.cache.post-observation' | sha256sum -c
date -u '+POSTCHECK_COMPLETE %FT%T.%NZ'
systemctl stop jc2-r2-mapobserver-outer-term-20260910T1500.timer jc2-r2-mapobserver-outer-kill-20260910T1500.timer
systemctl show jc2-r2-mapobserver-outer-term-20260910T1500.timer jc2-r2-mapobserver-outer-kill-20260910T1500.timer -p Id -p ActiveState -p SubState
sync -f /var/lib/jc2-r2-map-observer-20260910T1500
tar -czpf /home/ubuntu/jc2-r2-map-observer-20260910T1500/evidence.tar.gz -C / opt/jc2-r2-map-observer-20260910T1500 run/jc2-r2-map-observer-20260910T1500 var/lib/jc2-r2-map-observer-20260910T1500 home/ubuntu/jc2-r2-map-observer-20260910T1500/stage
tar -dzf /home/ubuntu/jc2-r2-map-observer-20260910T1500/evidence.tar.gz -C /
chmod 0444 /home/ubuntu/jc2-r2-map-observer-20260910T1500/evidence.tar.gz
sync -f /home/ubuntu/jc2-r2-map-observer-20260910T1500/evidence.tar.gz
sha256sum /home/ubuntu/jc2-r2-map-observer-20260910T1500/evidence.tar.gz
stat --printf='ARCHIVE_BYTES %s\n' /home/ubuntu/jc2-r2-map-observer-20260910T1500/evidence.tar.gz
date -u '+CUSTODY_ARCHIVE_COMPLETE %FT%T.%NZ'
