#!/bin/bash
# ROOT metadata-only terminal custody; no scientific execution or payload parsing.
set -euo pipefail
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0d991a2cfbf613ac6
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = efdbfc83-f361-4cdf-ac88-ab294e6c7d84
test "$(systemctl show jc2-contact-gram-20260910T2110.service -p MainPID --value)" = 0
test "$(systemctl show jc2-contact-gram-20260910T2110.service -p ControlPID --value)" = 0
test ! -e /sys/fs/cgroup/system.slice/jc2-contact-gram-20260910T2110.service
for jc2_pid in 8499 8587 8588; do test ! -e /proc/"$jc2_pid"; done
date -u '+ROOT_CONTACT_TERMINAL_HARVEST_BEGIN %Y-%m-%d %H:%M:%S.%N UTC'
cd /home/ubuntu/jc2-contact-gram-20260910T2110/stage
test ! -e terminal-pin-recheck-final.log
sha256sum -c terminal.sha256 >terminal-pin-recheck-final.log
test "$(wc -l < terminal-pin-recheck-final.log)" = 309
sha256sum -c native.sha256 >native-postcheck-final.log
test "$(sha256sum native-metadata.sh | cut -d ' ' -f1)" = dc62ae8d993ff2797a0200a05e98a0477e74c8efd6e32a9728aff44c680edb56
bash native-metadata.sh >native-post.stdout 2>native-post.stderr
test ! -s native-post.stderr
diff -u <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' native-post.stdout)
for jc2_fixture in certificate.json uphi.json bernstein.json positive.receipt.json; do
 test "$(stat -c '%u %g %a' /run/jc2-contact-gram-20260910T2110/frozen/$jc2_fixture)" = '0 0 444'
done
test ! -s /run/jc2-contact-gram-20260910T2110/dispatcher.stdout
test ! -s /run/jc2-contact-gram-20260910T2110/dispatcher.stderr
test "$(stat -c %d /var/lib/jc2-contact-gram-20260910T2110/custody)" = 66305
sync /var/lib/jc2-contact-gram-20260910T2110/custody /var/lib/jc2-contact-gram-20260910T2110
systemctl stop jc2-contact-gram-20260910T2110-term.timer jc2-contact-gram-20260910T2110-kill.timer
date -u '+ROOT_ORIGINAL_SYSTEM_TIMERS_CLOSED_AFTER_TERMINAL %Y-%m-%d %H:%M:%S.%N UTC'
test -z "$(find /opt/jc2-contact-gram-20260910T2110 /run/jc2-contact-gram-20260910T2110 /var/lib/jc2-contact-gram-20260910T2110 /home/ubuntu/jc2-contact-gram-20260910T2110/stage -type l -print -quit)"
test ! -e /home/ubuntu/jc2-contact-gram-20260910T2110/evidence.tar.gz
tar -czf /home/ubuntu/jc2-contact-gram-20260910T2110/evidence.tar.gz -C / opt/jc2-contact-gram-20260910T2110 run/jc2-contact-gram-20260910T2110 var/lib/jc2-contact-gram-20260910T2110 home/ubuntu/jc2-contact-gram-20260910T2110/stage
tar -df /home/ubuntu/jc2-contact-gram-20260910T2110/evidence.tar.gz -C /
sync /home/ubuntu/jc2-contact-gram-20260910T2110/evidence.tar.gz /home/ubuntu/jc2-contact-gram-20260910T2110
sha256sum /home/ubuntu/jc2-contact-gram-20260910T2110/evidence.tar.gz /var/lib/jc2-contact-gram-20260910T2110/custody/CUSTODY.json terminal-pin-recheck-final.log native-postcheck-final.log native-post.stdout native-post.stderr
stat -c '%n %s' /home/ubuntu/jc2-contact-gram-20260910T2110/evidence.tar.gz
date -u '+ROOT_CONTACT_ARCHIVE_COMPARE_SYNC_DONE %Y-%m-%d %H:%M:%S.%N UTC'
