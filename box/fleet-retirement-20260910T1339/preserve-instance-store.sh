set -eu
test "$(cat /sys/class/dmi/id/board_asset_tag)" = i-025410e620b1d65c9
test "$(cat /proc/sys/kernel/random/boot_id)" = 5f3e6300-ebd7-4eaf-9fce-223312588af4
test "$(findmnt -rn -T /home/ubuntu/t2t3-full -o SOURCE)" = /dev/md0
test "$(findmnt -rn -T /var/lib -o SOURCE)" = /dev/nvme0n1p1
test ! -e /var/lib/jc2-retired-instance-store-20260910T1340
test "$(du -sx --apparent-size -B1 /home/ubuntu/t2t3-full | cut -f1)" -lt 2147483648
test "$(df --output=avail -B1 /var/lib | tail -n1 | tr -d ' ')" -gt 4294967296
date -u '+INSTANCE_STORE_COPY_START %Y-%m-%d %H:%M:%S.%N UTC'
mkdir -m 0700 /var/lib/jc2-retired-instance-store-20260910T1340
tar --create --file /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar --sparse --one-file-system --numeric-owner --acls --xattrs --directory /home/ubuntu/t2t3-full .
tar --compare --file /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar --numeric-owner --acls --xattrs --directory /home/ubuntu/t2t3-full
chmod 0444 /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar
sync -f /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar
sha256sum /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar
stat -c '%n %s bytes mode=%a uid=%u gid=%g' /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar
tar --list --file /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar | wc -l
date -u '+INSTANCE_STORE_COPY_COMPARE_SYNC_DONE %Y-%m-%d %H:%M:%S.%N UTC'
