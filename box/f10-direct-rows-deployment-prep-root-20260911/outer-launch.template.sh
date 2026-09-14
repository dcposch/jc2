#!/bin/bash
# DISABLED ROOT outer launch template. Existing OS controls; no science changes.
set -euo pipefail
test "$(id -u)" = 0
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
 exit 2
fi
test 'JC2_OUTER_RELEASE_PLACEHOLDER' = ROOT_RELEASED_EXACT_DIRECT_ROWS_BATCH
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'JC2_INSTANCE_PLACEHOLDER'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'JC2_BOOT_ID_PLACEHOLDER'
test "$(date -u +%s)" -lt "$(date -ud 'JC2_LATEST_DISPATCH_LAUNCH_UTC_PLACEHOLDER' +%s)"
jc2_unit=jc2-r3-directrows-20260911a.service
jc2_cgroup=/sys/fs/cgroup/system.slice/$jc2_unit
test ! -e "$jc2_cgroup"
cd '/home/ubuntu/jc2-r3-directrows-20260911a/stage'
sha256sum -c installed.sha256
sha256sum -c native.sha256
# Both independent absolute stop timers are armed BEFORE any dispatcher process.
systemd-run --unit=jc2-r3-directrows-20260911a-term \
 --on-calendar='JC2_MATH_TERM_UTC_PLACEHOLDER' --timer-property=AccuracySec=1s \
 /usr/bin/systemctl kill --kill-whom=all --signal=TERM "$jc2_unit"
systemd-run --unit=jc2-r3-directrows-20260911a-kill \
 --on-calendar='JC2_MATH_KILL_UTC_PLACEHOLDER' --timer-property=AccuracySec=1s \
 /usr/bin/systemctl kill --kill-whom=all --signal=KILL "$jc2_unit"
systemctl is-active jc2-r3-directrows-20260911a-term.timer jc2-r3-directrows-20260911a-kill.timer
date -u '+ROOT_OUTER_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
systemd-run --unit="$jc2_unit" --property=Type=exec \
 --property=WorkingDirectory=/opt/jc2-r3-directrows-20260911a/wrapper \
 --property=RuntimeMaxSec=3000 --property=RuntimeRandomizedExtraSec=0 \
 --property=TimeoutStopSec=5 --property=KillMode=control-group \
 --property=MemoryMax=8589934592 --property=MemorySwapMax=0 --property=OOMPolicy=kill \
 --property=TasksMax=32 --property=CPUAccounting=yes --property=CPUQuota=69% \
 --property=CPUQuotaPeriodSec=10ms --property=CPUSchedulingPolicy=other \
 --property=RestrictRealtime=yes --property=Delegate=no --property=Restart=no \
 --property=StandardOutput=file:/run/jc2-r3-directrows-20260911a/outer.stdout \
 --property=StandardError=file:/run/jc2-r3-directrows-20260911a/outer.stderr \
 /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC \
 /usr/bin/python3.12 -I -S -B \
 /opt/jc2-r3-directrows-20260911a/wrapper/dispatch.py \
 --registration /opt/jc2-r3-directrows-20260911a/metadata/ROOT-REGISTRATION.json
for jc2_try in $(seq 1 100); do
 jc2_main=$(systemctl show "$jc2_unit" -p MainPID --value)
 if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
  systemctl show "$jc2_unit" -p MainPID -p InvocationID -p ControlGroup -p ActiveState -p ExecMainStartTimestamp -p Type -p RuntimeMaxUSec -p RuntimeRandomizedExtraUSec -p TimeoutStopUSec -p KillMode -p MemoryMax -p MemorySwapMax -p TasksMax -p CPUQuotaPerSecUSec -p CPUQuotaPeriodUSec -p CPUSchedulingPolicy -p RestrictRealtime -p Delegate -p Restart
  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  readlink /proc/"$jc2_main"/ns/pid
  /usr/bin/chrt -p "$jc2_main"
  for jc2_control in cpu.max cpu.max.burst cpu.stat memory.max memory.swap.max memory.current pids.max cgroup.procs; do
   printf 'ROOT_CONTROL %s\n' "$jc2_control"
   sed -n '1,30p' "$jc2_cgroup/$jc2_control"
  done
  if test "$(sed -n '1p' "$jc2_cgroup/cpu.max")" != '6900 10000' ||
     test "$(sed -n '1p' "$jc2_cgroup/cpu.max.burst")" != 0 ||
     test "$(sed -n '1p' "$jc2_cgroup/memory.max")" != 8589934592 ||
     test "$(sed -n '1p' "$jc2_cgroup/memory.swap.max")" != 0 ||
     test "$(sed -n '1p' "$jc2_cgroup/pids.max")" != 32; then
    systemctl kill --kill-whom=all --signal=TERM "$jc2_unit"
    exit 2
  fi
  for jc2_child in $(sed -n '1p' /proc/"$jc2_main"/task/"$jc2_main"/children); do
   ps -p "$jc2_child" -o pid=,ppid=,pgid=,lstart=,args=
  done
  date -u '+ROOT_SAME_LAUNCH_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  exit 0
 fi
 sleep 0.1
done
systemctl show "$jc2_unit" -p MainPID -p ControlPID -p ActiveState -p SubState -p ExecMainStatus -p CPUUsageNSec
date -u '+ROOT_NO_LIVE_CAPTURE_TERMINAL_CHECK_REQUIRED %Y-%m-%d %H:%M:%S.%N UTC'
exit 2
