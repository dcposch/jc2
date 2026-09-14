#!/bin/bash
# ROOT terminal custody/hash/archive only; no scientific execution.
set -euo pipefail
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0f5058733b2e2b130
test "$(tr -d '\n' < /proc/sys/kernel/random/boot_id)" = 17eb5153-cb6f-49c5-ab7b-a65e183f0293
test "$(systemctl show jc2-f10-r2-controls-ready-20260910T1620.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-controls-ready-20260910T1620.service -p ControlPID --value)" = 0
test ! -e /proc/8424
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-controls-ready-20260910T1620.service
date -u '+HARVEST_EXACT_GROUP_QUIET %FT%T.%NZ'
cd /home/ubuntu/jc2-r2-controls-ready-20260910T1620/stage
printf '%s\n' 'da4d484397e3896c74a073a8ab4f2317513ea11fca5ac374a89a2324ba004fee  /var/lib/jc2-r2-controls-ready-20260910T1620/CUSTODY.json' | sha256sum -c
sha256sum -c terminal-files.sha256 > terminal-files-recheck.log
sha256sum -c <<'JC2_INSTALLED_PINS' > installed-postcheck.log
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  /opt/jc2-r2-controls-ready-20260910T1620/science/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  /opt/jc2-r2-controls-ready-20260910T1620/science/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  /opt/jc2-r2-controls-ready-20260910T1620/science/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  /opt/jc2-r2-controls-ready-20260910T1620/science/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  /opt/jc2-r2-controls-ready-20260910T1620/science/check.py
6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b  /opt/jc2-r2-controls-ready-20260910T1620/wrapper/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  /opt/jc2-r2-controls-ready-20260910T1620/wrapper/probe.py
a896a8094be9b38f7ffa3a82cab15d340add0d7ab5f513340b2b7f916e489540  /opt/jc2-r2-controls-ready-20260910T1620/wrapper/mutate_controls.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-r2-controls-ready-20260910T1620/metadata/run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  /opt/jc2-r2-controls-ready-20260910T1620/metadata/artifact.json
acbf656e441249cacab8b0a002c39b048f4755004e35e70b112f2e704086c722  /opt/jc2-r2-controls-ready-20260910T1620/metadata/native-manifest.json
1b2f206401fd9d17271e20179d5e67ce4b408d85c98d9e3febcc454fefa81c48  /opt/jc2-r2-controls-ready-20260910T1620/metadata/ROOT-EXECUTION-CARD.md
469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b  /opt/jc2-r2-controls-ready-20260910T1620/metadata/f10-r2-semantic-code-gate-fable5-20260910.md
3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b  /opt/jc2-r2-controls-ready-20260910T1620/metadata/f10-r2-reconstruction-code-gate-fable5-20260910.md
3bce51215a7c746acb4bd5bc833f2644e5f2b1ac89e8681cdea2c65dfba00b0c  /opt/jc2-r2-controls-ready-20260910T1620/metadata/f10-r2-actual-result-gate-fable5-20260910.md
edd4c71e86d0d5cac2ee277de69199522a2a5bca9381833f19dc078e9759ea19  /opt/jc2-r2-controls-ready-20260910T1620/metadata/CONTRACT.md
0d0b00638cb42de7b7a59e1661ff0ae21668ff9ce0175e50a8b575d1d4ee3605  /opt/jc2-r2-controls-ready-20260910T1620/metadata/ROOT-REGISTRATION.json
JC2_INSTALLED_PINS
printf '%s\n' 'bd679559b8422b6b7516f26e8aaf15179022c4d9a872dc54cff27966ba87627d  native-metadata.sh' '06c6634683d4888ee252dd352208534467d22484d7e12b8a0b951c048afa6911  native.stdout' '94c31f95eaf02dec6a70fd085a2737516b9ca8d5774157cb66ebbb9899d2f257  native.sha256' | sha256sum -c
sha256sum -c native.sha256 > native-postcheck.log
timeout --signal=TERM --kill-after=5s 180s /bin/bash native-metadata.sh > native-post.stdout 2> native-post.stderr
test ! -s native-post.stderr
cmp <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native-post.stdout)
printf '%s\n' NATIVE_FILES_ALIASES_DIRECTORIES_STATS_COUNTS_IDENTICAL
date -u '+POSTCHECK_COMPLETE %FT%T.%NZ'
systemctl stop jc2-r2-controls-ready-outer-term-20260910T1620.timer jc2-r2-controls-ready-outer-kill-20260910T1620.timer
systemctl show jc2-r2-controls-ready-outer-term-20260910T1620.timer jc2-r2-controls-ready-outer-kill-20260910T1620.timer -p Id -p ActiveState -p SubState
sync -f /var/lib/jc2-r2-controls-ready-20260910T1620
tar -czpf /home/ubuntu/jc2-r2-controls-ready-20260910T1620/evidence.tar.gz -C / opt/jc2-r2-controls-ready-20260910T1620 run/jc2-r2-controls-ready-20260910T1620 var/lib/jc2-r2-controls-ready-20260910T1620 home/ubuntu/jc2-r2-controls-ready-20260910T1620/stage
tar -dzf /home/ubuntu/jc2-r2-controls-ready-20260910T1620/evidence.tar.gz -C /
chmod 0444 /home/ubuntu/jc2-r2-controls-ready-20260910T1620/evidence.tar.gz
sync -f /home/ubuntu/jc2-r2-controls-ready-20260910T1620/evidence.tar.gz
sha256sum /home/ubuntu/jc2-r2-controls-ready-20260910T1620/evidence.tar.gz
stat --printf='ARCHIVE_BYTES %s\n' /home/ubuntu/jc2-r2-controls-ready-20260910T1620/evidence.tar.gz
date -u '+HARVEST_ARCHIVE_SYNCED %FT%T.%NZ'
