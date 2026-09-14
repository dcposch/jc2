#!/bin/bash
# ROOT terminal custody/hash/archive only; no scientific execution.
set -euo pipefail
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-05b82c8e457c586ce
test "$(tr -d '\n' < /proc/sys/kernel/random/boot_id)" = 6e13db88-d1a2-45cd-aa1b-028d8e070589
test "$(systemctl show jc2-f10-r2-highest-ready-20260910T1720.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-highest-ready-20260910T1720.service -p ControlPID --value)" = 0
test ! -e /proc/9533
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-highest-ready-20260910T1720.service
date -u '+HARVEST_EXACT_GROUP_QUIET %FT%T.%NZ'
cd /home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage
printf '%s\n' 'f8fc2182a7eb3ce888f639e6ce4030f18b8bed0532d46e0604042dada4f10f10  /var/lib/jc2-r2-highest-ready-20260910T1720/CUSTODY.json' | sha256sum -c
sha256sum -c terminal-files.sha256 > terminal-files-recheck.log
sha256sum -c <<'JC2_INSTALLED_PINS' > installed-postcheck.log
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
printf '%s\n' '68b1d3e40d8e63a44e7ccdf6ce76a6cc6ea824dabdbed6be395b894a6e1a4b3a  native-metadata.sh' '82ad9bec15b2d8f3465dce7a0cbcc46d92b7f85dda0d6e3c014720081cc2143e  native.stdout' 'e1a625094c5213fe29c247aadd2f27232c18889289957e0311fba7ca62b5be7a  native.sha256' | sha256sum -c
sha256sum -c native.sha256 > native-postcheck.log
timeout --foreground --signal=TERM --kill-after=5s 180s /bin/bash native-metadata.sh > native-post.stdout 2> native-post.stderr
test ! -s native-post.stderr
cmp <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native-post.stdout)
printf '%s\n' NATIVE_FILES_ALIASES_DIRECTORIES_STATS_COUNTS_IDENTICAL
date -u '+POSTCHECK_COMPLETE %FT%T.%NZ'
systemctl stop jc2-r2-highest-ready-outer-term-20260910T1620.timer jc2-r2-highest-ready-outer-kill-20260910T1620.timer
systemctl show jc2-r2-highest-ready-outer-term-20260910T1620.timer jc2-r2-highest-ready-outer-kill-20260910T1620.timer -p Id -p ActiveState -p SubState
sync -f /var/lib/jc2-r2-highest-ready-20260910T1720
test ! -e /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
tar -czpf /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz -C / opt/jc2-r2-highest-ready-20260910T1720 run/jc2-r2-highest-ready-20260910T1720 var/lib/jc2-r2-highest-ready-20260910T1720 home/ubuntu/jc2-r2-highest-ready-20260910T1720/stage
tar -dzf /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz -C /
chmod 0444 /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
sync -f /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
sha256sum /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
stat --printf='ARCHIVE_BYTES %s\n' /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
date -u '+HARVEST_ARCHIVE_SYNCED %FT%T.%NZ'
