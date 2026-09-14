set -eu
date -u '+INSPECTION_UTC %Y-%m-%d %H:%M:%S.%N UTC'
hostname
cat /sys/class/dmi/id/board_asset_tag
cat /proc/sys/kernel/random/boot_id
ps -e -o pid=,ppid=,pgid=,stat=,etimes=,comm=,args= | awk '$2 != 2'
findmnt -rn -o TARGET,SOURCE,FSTYPE
lsblk -o NAME,TYPE,SIZE,MODEL,MOUNTPOINTS
df -hT
systemctl list-timers --all --no-pager
systemctl --user list-timers --all --no-pager
