#!/bin/bash
# ROOT terminal recovery/custody only; no scientific code or interpreter execution.
set -euo pipefail
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0de792cdaff6b0682
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = a051707c-61a9-407b-8921-f2a6f240a5cf
test "$(systemctl show jc2-r3-necessaryrows-20260911a.service -p MainPID --value)" = 0
test "$(systemctl show jc2-r3-necessaryrows-20260911a.service -p ControlPID --value)" = 0
test ! -e /sys/fs/cgroup/system.slice/jc2-r3-necessaryrows-20260911a.service
for jc2_recovery_pid in 8678 8738 8744; do test ! -e /proc/"$jc2_recovery_pid"; done
if pgrep -g 8678,8738; then exit 2; fi
if pgrep -af '^/usr/bin/python3.12 .*/opt/jc2-r3-necessaryrows-20260911a/'; then exit 2; fi
date -u '+ROOT_RECOVERY_BEGIN %Y-%m-%d %H:%M:%S.%N UTC'
jc2_recovery=/var/lib/jc2-r3-necessaryrows-20260911a/ROOT-RECOVERY
test ! -e "$jc2_recovery"
install -d -o 0 -g 0 -m 0700 "$jc2_recovery"
test "$(stat -c %d "$jc2_recovery")" = 66305
test ! -e /var/lib/jc2-r3-necessaryrows-20260911a/custody/CUSTODY.json
test ! -e /run/jc2-r3-necessaryrows-20260911a/produce.pre.json
test ! -e /run/jc2-r3-necessaryrows-20260911a/writer/produce.payload
test ! -e /run/jc2-r3-necessaryrows-20260911a/frozen/artifact.json
systemctl show jc2-r3-necessaryrows-20260911a.service > "$jc2_recovery/outer-terminal.show"
journalctl --no-pager -o json _SYSTEMD_INVOCATION_ID=d5c71b159ca94180ad520fc3f3e0e8e3 > "$jc2_recovery/outer-invocation.journal.jsonl"
journalctl --no-pager -o json -u jc2-r3-necessaryrows-20260911a.service > "$jc2_recovery/outer-unit.journal.jsonl"
cd /home/ubuntu/jc2-r3-necessaryrows-20260911a/stage
sha256sum -c installed.sha256 > "$jc2_recovery/installed-postcheck.log"
sha256sum -c native.sha256 > "$jc2_recovery/native-postcheck.log"
test "$(sha256sum /home/ubuntu/jc2-necessaryrows-native-metadata.sh | cut -d ' ' -f1)" = a62ba39d09d892faaa0d617d42a3ec8f543a12575679cb6a84a517031c4e369b
bash /home/ubuntu/jc2-necessaryrows-native-metadata.sh > "$jc2_recovery/native-post.stdout" 2> "$jc2_recovery/native-post.stderr"
test ! -s "$jc2_recovery/native-post.stderr"
diff -u <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' "$jc2_recovery/native-post.stdout")
systemctl stop jc2-r3-necessaryrows-20260911a-term.timer jc2-r3-necessaryrows-20260911a-kill.timer
date -u '+ROOT_ORIGINAL_SCIENCE_TIMERS_CLOSED_AFTER_QUIET %Y-%m-%d %H:%M:%S.%N UTC'
find /opt/jc2-r3-necessaryrows-20260911a /run/jc2-r3-necessaryrows-20260911a /home/ubuntu/jc2-r3-necessaryrows-20260911a/stage -type f -print0 | sort -z | xargs -0 sha256sum > "$jc2_recovery/TERMINAL.sha256"
sha256sum -c "$jc2_recovery/TERMINAL.sha256" > "$jc2_recovery/terminal-postcheck.log"
test -z "$(find /opt/jc2-r3-necessaryrows-20260911a /run/jc2-r3-necessaryrows-20260911a /var/lib/jc2-r3-necessaryrows-20260911a /home/ubuntu/jc2-r3-necessaryrows-20260911a/stage -type l -print -quit)"
test ! -e /home/ubuntu/jc2-r3-necessaryrows-20260911a/evidence.tar.gz
tar -czf /home/ubuntu/jc2-r3-necessaryrows-20260911a/evidence.tar.gz -C / opt/jc2-r3-necessaryrows-20260911a run/jc2-r3-necessaryrows-20260911a var/lib/jc2-r3-necessaryrows-20260911a home/ubuntu/jc2-r3-necessaryrows-20260911a/stage home/ubuntu/jc2-necessaryrows-physical-metadata.sh home/ubuntu/jc2-necessaryrows-native-metadata.sh home/ubuntu/jc2-necessaryrows-setup.sh home/ubuntu/jc2-necessaryrows-outer-launch.sh home/ubuntu/jc2-necessaryrows-recovery.sh
tar -df /home/ubuntu/jc2-r3-necessaryrows-20260911a/evidence.tar.gz -C /
sync /home/ubuntu/jc2-r3-necessaryrows-20260911a/evidence.tar.gz /home/ubuntu/jc2-r3-necessaryrows-20260911a "$jc2_recovery"
sha256sum /home/ubuntu/jc2-r3-necessaryrows-20260911a/evidence.tar.gz "$jc2_recovery/TERMINAL.sha256" "$jc2_recovery/native-post.stdout" "$jc2_recovery/outer-terminal.show"
stat -c '%s %n' /home/ubuntu/jc2-r3-necessaryrows-20260911a/evidence.tar.gz
wc -l "$jc2_recovery/TERMINAL.sha256" "$jc2_recovery/terminal-postcheck.log" "$jc2_recovery/native-postcheck.log"
date -u '+ROOT_RECOVERY_ARCHIVE_COMPARE_FSYNC_DONE %Y-%m-%d %H:%M:%S.%N UTC'
