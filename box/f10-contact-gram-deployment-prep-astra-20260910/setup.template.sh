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
jc2_release='JC2_METADATA_SETUP_RELEASE_PLACEHOLDER'
test "$jc2_release" = ROOT_SEPARATELY_AUTHORIZED_METADATA_SETUP
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'JC2_INSTANCE_ID_PLACEHOLDER'
test "$(hostname)" = 'JC2_HOSTNAME_PLACEHOLDER'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'JC2_BOOT_ID_PLACEHOLDER'
test "$(readlink /proc/self/ns/pid)" = 'JC2_PID_NAMESPACE_PLACEHOLDER'
jc2_python='/JC2_PYTHON_CANONICAL_PATH_PLACEHOLDER'
jc2_setpriv='/JC2_SETPRIV_CANONICAL_PATH_PLACEHOLDER'
test "$(readlink -f "$jc2_python")" = "$jc2_python"
test "$(readlink -f "$jc2_setpriv")" = "$jc2_setpriv"
jc2_base='/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER'
jc2_mount='/run/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER'
jc2_durable_parent='/var/lib/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER'
test ! -e "$jc2_base"
test ! -L "$jc2_base"
test ! -e "$jc2_mount"
test ! -L "$jc2_mount"
test ! -e "$jc2_durable_parent"
test ! -L "$jc2_durable_parent"
cd '/JC2_STAGE_DIRECTORY_PLACEHOLDER'
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
JC2_NATIVE_MANIFEST_SHA256_PLACEHOLDER  native-manifest.json
JC2_NATIVE_STDOUT_SHA256_PLACEHOLDER  native.stdout
JC2_NATIVE_SHA256_SHA256_PLACEHOLDER  native.sha256
JC2_ROOT_REGISTRATION_JSON_SHA256_PLACEHOLDER  ROOT-REGISTRATION.json
JC2_ROOT_EXECUTION_CARD_MD_SHA256_PLACEHOLDER  ROOT-EXECUTION-CARD.md
JC2_STAGE_PINS
sha256sum -c <<'JC2_EXECUTABLE_PINS'
JC2_PYTHON_SHA256_PLACEHOLDER  /JC2_PYTHON_CANONICAL_PATH_PLACEHOLDER
JC2_SETPRIV_SHA256_PLACEHOLDER  /JC2_SETPRIV_CANONICAL_PATH_PLACEHOLDER
JC2_EXECUTABLE_PINS
# FILES-only manifest is consumed by dispatcher. ROOT separately authenticates
# collector directory/alias/absence/python_path/cache records; no R2 schema import.
sha256sum -c native.sha256
install -d -o 0 -g 0 -m 0755 "$jc2_base" "$jc2_base/source" "$jc2_base/metadata"
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/run_capped.py'
install -o 0 -g 0 -m 0444 'run_capped.py' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/run_capped.py'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/producer.py'
install -o 0 -g 0 -m 0444 'producer.py' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/producer.py'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/checker.py'
install -o 0 -g 0 -m 0444 'checker.py' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/checker.py'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/authority.py'
install -o 0 -g 0 -m 0444 'authority.py' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/authority.py'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/probe.py'
install -o 0 -g 0 -m 0444 'probe.py' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/probe.py'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/mutate.py'
install -o 0 -g 0 -m 0444 'mutate.py' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/mutate.py'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/dispatch.py'
install -o 0 -g 0 -m 0444 'dispatch.py' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/dispatch.py'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-real-window-astra-20260910.md'
install -o 0 -g 0 -m 0444 'f10-contact-real-window-astra-20260910.md' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-real-window-astra-20260910.md'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-quartic-gram-gate-fable5-20260910.md'
install -o 0 -g 0 -m 0444 'f10-contact-quartic-gram-gate-fable5-20260910.md' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-quartic-gram-gate-fable5-20260910.md'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-symmetric-remainder-astra-20260910.md'
install -o 0 -g 0 -m 0444 'f10-contact-symmetric-remainder-astra-20260910.md' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-symmetric-remainder-astra-20260910.md'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native-manifest.json'
install -o 0 -g 0 -m 0444 'native-manifest.json' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native-manifest.json'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native.stdout'
install -o 0 -g 0 -m 0444 'native.stdout' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native.stdout'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native.sha256'
install -o 0 -g 0 -m 0444 'native.sha256' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native.sha256'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-REGISTRATION.json'
install -o 0 -g 0 -m 0444 'ROOT-REGISTRATION.json' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-REGISTRATION.json'
test ! -e '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-EXECUTION-CARD.md'
install -o 0 -g 0 -m 0444 'ROOT-EXECUTION-CARD.md' '/opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-EXECUTION-CARD.md'
sha256sum -c <<'JC2_INSTALLED_PINS'
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/run_capped.py
afc617ae797661df8cbb1ca1d8a00825a6c607e1fb854754c0230376965f74ee  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/producer.py
ceca0a07f1b2f6433de87bb7327280cb1165703ea9196f6d7e37b953a8631b06  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/checker.py
96ca421fe8d82f7035161d35c325db2e1433346db0101ab6bfffe9da6984a141  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/authority.py
d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/probe.py
70857a11be5e21d63d8bb476663dd3587332d1968f5f26912e6851aa51d5d77c  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/mutate.py
61f21a2c5912cd53a46f8881783994e104a511cee1261713df53936aced9c126  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/source/dispatch.py
f87a2189ceacbca0d58e84aa5e32838b89c47ff249ea9acb5d757ae184e6a2d2  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-real-window-astra-20260910.md
ce14c6a789086419f88a601faf10bfd388639697cd693a1deb12160c955f5068  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-quartic-gram-gate-fable5-20260910.md
96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/f10-contact-symmetric-remainder-astra-20260910.md
JC2_NATIVE_MANIFEST_SHA256_PLACEHOLDER  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native-manifest.json
JC2_NATIVE_STDOUT_SHA256_PLACEHOLDER  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native.stdout
JC2_NATIVE_SHA256_SHA256_PLACEHOLDER  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/native.sha256
JC2_ROOT_REGISTRATION_JSON_SHA256_PLACEHOLDER  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-REGISTRATION.json
JC2_ROOT_EXECUTION_CARD_MD_SHA256_PLACEHOLDER  /opt/jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER/metadata/ROOT-EXECUTION-CARD.md
JC2_INSTALLED_PINS
install -d -o 0 -g 0 -m 0755 "$jc2_durable_parent"
test "$(stat -c %d "$jc2_durable_parent")" = 'JC2_DURABLE_DEVICE_INTEGER_PLACEHOLDER'
test "$(findmnt -n -o FSTYPE --target "$jc2_durable_parent")" = 'JC2_DURABLE_EXT4_OR_XFS_PLACEHOLDER'
test ! -e "$jc2_durable_parent/custody"
install -d -o 0 -g 0 -m 0755 "$jc2_mount"
mount -t tmpfs -o size=16777216,mode=0755,nosuid,nodev tmpfs "$jc2_mount"
install -d -o 0 -g 0 -m 0755 "$jc2_mount/authority" "$jc2_mount/frozen"
install -d -o JC2_SCIENCE_UID_INTEGER_PLACEHOLDER -g JC2_SCIENCE_GID_INTEGER_PLACEHOLDER -m 0700 "$jc2_mount/writer"
# Fixed sources and all ancestry must be readable by this future science UID.
for jc2_file in "$jc2_base"/source/* "$jc2_base"/metadata/*; do
  "$jc2_setpriv" --reuid JC2_SCIENCE_UID_INTEGER_PLACEHOLDER --regid JC2_SCIENCE_GID_INTEGER_PLACEHOLDER --clear-groups --no-new-privs -- /usr/bin/test -r "$jc2_file"
done
printf '%s\n' 'METADATA_SETUP_ONLY_NO_LAUNCH: ROOT must separately verify full-cgroup supervision, native/startup/argv and active independent timers.'
# Deliberately NO systemd-run, worker action, scientific child, cleanup/unmount,
# supervisor implementation or claimed full-budget enforcement in this template.
