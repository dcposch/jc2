#!/usr/bin/env bash
set -euo pipefail

printf 'UTC '
date -u +%Y-%m-%dT%H:%M:%SZ
printf 'HOST '
hostname
printf 'DMI_INSTANCE '
cat /sys/class/dmi/id/board_asset_tag
printf 'BOOT_ID '
cat /proc/sys/kernel/random/boot_id
printf 'UPTIME '
uptime
printf 'MEMORY\n'
free -b
printf 'USER_PROCESSES\n'
ps -U ubuntu -u ubuntu -o pid=,ppid=,pgid=,lstart=,etimes=,stat=,%cpu=,%mem=,rss=,comm= --sort=pid
printf 'ALL_PROCESSES\n'
ps -e -o pid=,ppid=,pgid=,user=,lstart=,etimes=,stat=,%cpu=,%mem=,rss=,comm= --sort=pid
printf 'COMPUTE_NAMES\n'
pgrep -a -x msolve || true
pgrep -a -x Singular || true
pgrep -a -x sage || true
pgrep -a -x magma || true
printf 'R400_NAMES\n'
pgrep -af 'r400_20260829|run_exact_packet|caprun.py' || true
printf 'SCREEN\n'
screen -ls 2>&1 || true
printf 'TMUX\n'
tmux list-sessions 2>&1 || true
printf 'CRONTAB\n'
crontab -l 2>&1 || true
printf 'ATQ\n'
atq 2>&1 || true
printf 'BLOCKS\n'
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,MODEL,SERIAL
printf 'INSTANCE_STORE_SIGNATURES\n'
for device in /dev/nvme1n1 /dev/nvme2n1; do
    if [[ -b "$device" ]]; then
        printf '%s\n' "$device"
        sudo -n wipefs --no-act "$device" || true
        findmnt -rn -S "$device" || true
    fi
done
printf 'SWAP\n'
swapon --show --bytes || true
printf 'R400_MOUNT\n'
findmnt -T /home/ubuntu/r400_20260829 -o SOURCE,TARGET,FSTYPE,OPTIONS
printf 'ROOT_MOUNT\n'
findmnt -T / -o SOURCE,TARGET,FSTYPE,OPTIONS
printf 'FILESYSTEMS\n'
df -B1 -T / /home/ubuntu/r400_20260829
printf 'KNOWN_CAMPAIGN_ROLES\n'
for role_path in /home/ubuntu/res32 /home/ubuntu/jc72108 /home/ubuntu/stuck7; do
    if [[ -d "$role_path" ]]; then
        printf 'ROLE_PATH %s\n' "$role_path"
        du -sb "$role_path"
        findmnt -T "$role_path" -o SOURCE,TARGET,FSTYPE,OPTIONS
    fi
done
