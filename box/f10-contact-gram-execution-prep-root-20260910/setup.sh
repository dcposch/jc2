#!/bin/bash
# DISABLED OFFLINE TEMPLATE; NOT a launcher or a supervision instrument.
# ROOT must finalize, review, hash and separately authorize a future metadata setup.
# This file has never been executed. Scientific sources are only copied unchanged.
set -euo pipefail
command -v rg >/dev/null || exit 2
if rg -q 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
  printf '%s\n' 'DISABLED: unresolved ROOT placeholders' >&2
  exit 2
fi
jc2_release='ROOT_SEPARATELY_AUTHORIZED_METADATA_SETUP'
test "$jc2_release" = ROOT_SEPARATELY_AUTHORIZED_METADATA_SETUP
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'i-0d991a2cfbf613ac6'
test "$(hostname)" = 'ip-172-30-0-241'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'efdbfc83-f361-4cdf-ac88-ab294e6c7d84'
test "$(readlink /proc/self/ns/pid)" = 'pid:[4026531836]'
jc2_python='/usr/bin/python3.12'
jc2_setpriv='/usr/bin/setpriv'
test "$(readlink -f "$jc2_python")" = "$jc2_python"
test "$(readlink -f "$jc2_setpriv")" = "$jc2_setpriv"
jc2_base='/opt/jc2-contact-gram-20260910T2110'
jc2_mount='/run/jc2-contact-gram-20260910T2110'
jc2_durable_parent='/var/lib/jc2-contact-gram-20260910T2110'
test ! -e "$jc2_base"
test ! -L "$jc2_base"
test ! -e "$jc2_mount"
test ! -L "$jc2_mount"
test ! -e "$jc2_durable_parent"
test ! -L "$jc2_durable_parent"
cd '/home/ubuntu/jc2-contact-gram-20260910T2110/stage'
# ROOT validates the finalized JSON types/schema, enabled authority, literal
# vectors and whole native observations OFFLINE; no Python/source import here.
if rg -q 'JC2_[A-Z0-9_]+_PLACEHOLDER' ROOT-REGISTRATION.json ROOT-EXECUTION-CARD.md native-manifest.json; then
  printf '%s\n' 'DISABLED: unresolved staged metadata' >&2
  exit 2
fi
sha256sum -c <<'JC2_STAGE_PINS'
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  run_capped.py
afc617ae797661df8cbb1ca1d8a00825a6c607e1fb854754c0230376965f74ee  producer.py
ceca0a07f1b2f6433de87bb7327280cb1165703ea9196f6d7e37b953a8631b06  checker.py
96ca421fe8d82f7035161d35c325db2e1433346db0101ab6bfffe9da6984a141  authority.py
d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4  probe.py
70857a11be5e21d63d8bb476663dd3587332d1968f5f26912e6851aa51d5d77c  mutate.py
61f21a2c5912cd53a46f8881783994e104a511cee1261713df53936aced9c126  dispatch.py
f87a2189ceacbca0d58e84aa5e32838b89c47ff249ea9acb5d757ae184e6a2d2  f10-contact-real-window-astra-20260910.md
ce14c6a789086419f88a601faf10bfd388639697cd693a1deb12160c955f5068  f10-contact-quartic-gram-gate-fable5-20260910.md
96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13  f10-contact-symmetric-remainder-astra-20260910.md
3a02fdb4133f1edefa512d5f6d8b7b106e6cb325cd6b8af679569e51eee22160  native-manifest.json
afd077c5530b8a44b565c19923a1ff13850c9b474aa72f4b41007034f4244950  native.stdout
e1a625094c5213fe29c247aadd2f27232c18889289957e0311fba7ca62b5be7a  native.sha256
18b7adba04c17b74b7454733de53b7070159e6d0a607a457f8db4b8aee9ee869  ROOT-REGISTRATION.json
e5db321d06c7659069e553146433515109f774d32ad1d8886361d2363400bcf6  ROOT-EXECUTION-CARD.md
JC2_STAGE_PINS
sha256sum -c <<'JC2_EXECUTABLE_PINS'
a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223  /usr/bin/python3.12
62ec0120791f3afcfb689fed52384ec2b0accc6e118a6b9a1d6fcfa7450aaf37  /usr/bin/setpriv
JC2_EXECUTABLE_PINS
# FILES-only manifest is consumed by dispatcher. ROOT separately authenticates
# collector directory/alias/absence/python_path/cache records; no R2 schema import.
sha256sum -c native.sha256
install -d -o 0 -g 0 -m 0755 "$jc2_base" "$jc2_base/source" "$jc2_base/metadata"
test ! -e '/opt/jc2-contact-gram-20260910T2110/source/run_capped.py'
install -o 0 -g 0 -m 0444 'run_capped.py' '/opt/jc2-contact-gram-20260910T2110/source/run_capped.py'
test ! -e '/opt/jc2-contact-gram-20260910T2110/source/producer.py'
install -o 0 -g 0 -m 0444 'producer.py' '/opt/jc2-contact-gram-20260910T2110/source/producer.py'
test ! -e '/opt/jc2-contact-gram-20260910T2110/source/checker.py'
install -o 0 -g 0 -m 0444 'checker.py' '/opt/jc2-contact-gram-20260910T2110/source/checker.py'
test ! -e '/opt/jc2-contact-gram-20260910T2110/source/authority.py'
install -o 0 -g 0 -m 0444 'authority.py' '/opt/jc2-contact-gram-20260910T2110/source/authority.py'
test ! -e '/opt/jc2-contact-gram-20260910T2110/source/probe.py'
install -o 0 -g 0 -m 0444 'probe.py' '/opt/jc2-contact-gram-20260910T2110/source/probe.py'
test ! -e '/opt/jc2-contact-gram-20260910T2110/source/mutate.py'
install -o 0 -g 0 -m 0444 'mutate.py' '/opt/jc2-contact-gram-20260910T2110/source/mutate.py'
test ! -e '/opt/jc2-contact-gram-20260910T2110/source/dispatch.py'
install -o 0 -g 0 -m 0444 'dispatch.py' '/opt/jc2-contact-gram-20260910T2110/source/dispatch.py'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-real-window-astra-20260910.md'
install -o 0 -g 0 -m 0444 'f10-contact-real-window-astra-20260910.md' '/opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-real-window-astra-20260910.md'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-quartic-gram-gate-fable5-20260910.md'
install -o 0 -g 0 -m 0444 'f10-contact-quartic-gram-gate-fable5-20260910.md' '/opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-quartic-gram-gate-fable5-20260910.md'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-symmetric-remainder-astra-20260910.md'
install -o 0 -g 0 -m 0444 'f10-contact-symmetric-remainder-astra-20260910.md' '/opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-symmetric-remainder-astra-20260910.md'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/native-manifest.json'
install -o 0 -g 0 -m 0444 'native-manifest.json' '/opt/jc2-contact-gram-20260910T2110/metadata/native-manifest.json'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/native.stdout'
install -o 0 -g 0 -m 0444 'native.stdout' '/opt/jc2-contact-gram-20260910T2110/metadata/native.stdout'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/native.sha256'
install -o 0 -g 0 -m 0444 'native.sha256' '/opt/jc2-contact-gram-20260910T2110/metadata/native.sha256'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/ROOT-REGISTRATION.json'
install -o 0 -g 0 -m 0444 'ROOT-REGISTRATION.json' '/opt/jc2-contact-gram-20260910T2110/metadata/ROOT-REGISTRATION.json'
test ! -e '/opt/jc2-contact-gram-20260910T2110/metadata/ROOT-EXECUTION-CARD.md'
install -o 0 -g 0 -m 0444 'ROOT-EXECUTION-CARD.md' '/opt/jc2-contact-gram-20260910T2110/metadata/ROOT-EXECUTION-CARD.md'
sha256sum -c <<'JC2_INSTALLED_PINS'
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-contact-gram-20260910T2110/source/run_capped.py
afc617ae797661df8cbb1ca1d8a00825a6c607e1fb854754c0230376965f74ee  /opt/jc2-contact-gram-20260910T2110/source/producer.py
ceca0a07f1b2f6433de87bb7327280cb1165703ea9196f6d7e37b953a8631b06  /opt/jc2-contact-gram-20260910T2110/source/checker.py
96ca421fe8d82f7035161d35c325db2e1433346db0101ab6bfffe9da6984a141  /opt/jc2-contact-gram-20260910T2110/source/authority.py
d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4  /opt/jc2-contact-gram-20260910T2110/source/probe.py
70857a11be5e21d63d8bb476663dd3587332d1968f5f26912e6851aa51d5d77c  /opt/jc2-contact-gram-20260910T2110/source/mutate.py
61f21a2c5912cd53a46f8881783994e104a511cee1261713df53936aced9c126  /opt/jc2-contact-gram-20260910T2110/source/dispatch.py
f87a2189ceacbca0d58e84aa5e32838b89c47ff249ea9acb5d757ae184e6a2d2  /opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-real-window-astra-20260910.md
ce14c6a789086419f88a601faf10bfd388639697cd693a1deb12160c955f5068  /opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-quartic-gram-gate-fable5-20260910.md
96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13  /opt/jc2-contact-gram-20260910T2110/metadata/f10-contact-symmetric-remainder-astra-20260910.md
3a02fdb4133f1edefa512d5f6d8b7b106e6cb325cd6b8af679569e51eee22160  /opt/jc2-contact-gram-20260910T2110/metadata/native-manifest.json
afd077c5530b8a44b565c19923a1ff13850c9b474aa72f4b41007034f4244950  /opt/jc2-contact-gram-20260910T2110/metadata/native.stdout
e1a625094c5213fe29c247aadd2f27232c18889289957e0311fba7ca62b5be7a  /opt/jc2-contact-gram-20260910T2110/metadata/native.sha256
18b7adba04c17b74b7454733de53b7070159e6d0a607a457f8db4b8aee9ee869  /opt/jc2-contact-gram-20260910T2110/metadata/ROOT-REGISTRATION.json
e5db321d06c7659069e553146433515109f774d32ad1d8886361d2363400bcf6  /opt/jc2-contact-gram-20260910T2110/metadata/ROOT-EXECUTION-CARD.md
JC2_INSTALLED_PINS
install -d -o 0 -g 0 -m 0755 "$jc2_durable_parent"
test "$(stat -c %d "$jc2_durable_parent")" = '66305'
test "$(findmnt -n -o FSTYPE --target "$jc2_durable_parent")" = 'ext4'
test ! -e "$jc2_durable_parent/custody"
install -d -o 0 -g 0 -m 0755 "$jc2_mount"
mount -t tmpfs -o size=16777216,mode=0755,nosuid,nodev tmpfs "$jc2_mount"
install -d -o 0 -g 0 -m 0755 "$jc2_mount/authority" "$jc2_mount/frozen"
install -d -o 65534 -g 65534 -m 0700 "$jc2_mount/writer"
# Fixed sources and all ancestry must be readable by this future science UID.
for jc2_file in "$jc2_base"/source/* "$jc2_base"/metadata/*; do
  "$jc2_setpriv" --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
printf '%s\n' 'METADATA_SETUP_ONLY_NO_LAUNCH: ROOT must separately verify full-cgroup supervision, native/startup/argv and active independent timers.'
# Deliberately NO systemd-run, worker action, scientific child, cleanup/unmount,
# supervisor implementation or claimed full-budget enforcement in this template.
