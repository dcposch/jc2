#!/bin/bash
# ROOT terminal metadata and byte custody only. No scientific code execution.
set -euo pipefail
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-031b57c489417e1d1
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 56714315-f924-4dee-bf5d-95bf5c700dfa
test "$(systemctl show jc2-r3-directrows-20260911a.service -p MainPID --value)" = 0
test "$(systemctl show jc2-r3-directrows-20260911a.service -p ControlPID --value)" = 0
test "$(systemctl show jc2-r3-directrows-20260911a.service -p ActiveState --value)" = failed
test ! -e /sys/fs/cgroup/system.slice/jc2-r3-directrows-20260911a.service
for jc2_pid in 8570 8663 8664; do test ! -e /proc/"$jc2_pid"; done
date -u '+ROOT_R3_TERMINAL_HARVEST_BEGIN %Y-%m-%d %H:%M:%S.%N UTC'
cd /home/ubuntu/jc2-r3-directrows-20260911a/stage
test ! -e terminal-pin-recheck.log
sha256sum -c terminal.sha256 >terminal-pin-recheck.log
test "$(wc -l < terminal-pin-recheck.log)" = 224
sha256sum -c native.sha256 >native-postcheck.log
test "$(sha256sum native-metadata.sh | cut -d ' ' -f1)" = baf2f2762fe338eeb9a8f0444e6864cba2b2dc796af58920d0fb32ec26a6d582
bash native-metadata.sh >native-post.stdout 2>native-post.stderr
test ! -s native-post.stderr
diff -u <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native-post.stdout)
systemctl show jc2-r3-directrows-20260911a.service >outer-terminal.show
journalctl --no-pager -o json _SYSTEMD_INVOCATION_ID=2c97ab475b254ff8ae8b2b091118c53b >outer-invocation.journal.jsonl
journalctl --no-pager -o json -u jc2-r3-directrows-20260911a.service >outer-unit.journal.jsonl
test "$(stat -c %d /var/lib/jc2-r3-directrows-20260911a/custody)" = 66305
test ! -e /run/jc2-r3-directrows-20260911a/writer/produce.payload
sync /var/lib/jc2-r3-directrows-20260911a/custody /var/lib/jc2-r3-directrows-20260911a
systemctl stop jc2-r3-directrows-20260911a-term.timer jc2-r3-directrows-20260911a-kill.timer
date -u '+ROOT_ORIGINAL_SYSTEM_TIMERS_CLOSED_AFTER_TERMINAL %Y-%m-%d %H:%M:%S.%N UTC'
test -z "$(find /opt/jc2-r3-directrows-20260911a /run/jc2-r3-directrows-20260911a /var/lib/jc2-r3-directrows-20260911a /home/ubuntu/jc2-r3-directrows-20260911a/stage -type l -print -quit)"
test ! -e /home/ubuntu/jc2-r3-directrows-20260911a/evidence.tar.gz
tar -czf /home/ubuntu/jc2-r3-directrows-20260911a/evidence.tar.gz -C / opt/jc2-r3-directrows-20260911a run/jc2-r3-directrows-20260911a var/lib/jc2-r3-directrows-20260911a home/ubuntu/jc2-r3-directrows-20260911a/stage home/ubuntu/jc2-r3-directrows-20260911a/native.stdout home/ubuntu/jc2-r3-directrows-20260911a/native.stderr home/ubuntu/jc2-r3-directrows-20260911a/setup.stdout home/ubuntu/jc2-r3-directrows-20260911a/setup.stderr home/ubuntu/jc2-r3-directrows-20260911a/outer-launch.stdout home/ubuntu/jc2-r3-directrows-20260911a/outer-launch.stderr home/ubuntu/physical-metadata.sh home/ubuntu/physical.stdout home/ubuntu/physical.stderr home/ubuntu/native-metadata.sh
tar -df /home/ubuntu/jc2-r3-directrows-20260911a/evidence.tar.gz -C /
sync /home/ubuntu/jc2-r3-directrows-20260911a/evidence.tar.gz /home/ubuntu/jc2-r3-directrows-20260911a
sha256sum /home/ubuntu/jc2-r3-directrows-20260911a/evidence.tar.gz /var/lib/jc2-r3-directrows-20260911a/custody/CUSTODY.json terminal-pin-recheck.log native-postcheck.log native-post.stdout native-post.stderr outer-terminal.show outer-invocation.journal.jsonl outer-unit.journal.jsonl
stat -c '%n %s' /home/ubuntu/jc2-r3-directrows-20260911a/evidence.tar.gz
date -u '+ROOT_R3_ARCHIVE_COMPARE_SYNC_DONE %Y-%m-%d %H:%M:%S.%N UTC'
