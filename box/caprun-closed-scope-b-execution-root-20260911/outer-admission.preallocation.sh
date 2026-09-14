#!/bin/bash
# DISABLED ROOT admission only. STATIC/UNTESTED; never writes a release token.
set -euo pipefail
test "$(id -u)" = 0
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT admission metadata' >&2
 exit 2
fi
test 'JC2_OUTER_RELEASE_PLACEHOLDER' = ROOT_ADMIT_HOLDER_ONLY
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'JC2_INSTANCE_PLACEHOLDER'
test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'JC2_BOOT_ID_PLACEHOLDER'
test "$(date -u +%s)" -lt "$(date -ud '2026-09-11T12:25:45+00:00' +%s)"
jc2_unit=jc2-closedchild-preflight9-20260911b.service
jc2_cgroup=/sys/fs/cgroup/system.slice/$jc2_unit
jc2_base=/opt/jc2-closedchild-preflight9-20260911b
jc2_channel=/run/jc2-closedchild-preflight9-20260911b-admission
test ! -e "$jc2_cgroup"
test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
test ! -L "$jc2_base/metadata/ROOT-REGISTRATION.json"
test -p "$jc2_channel/release.fifo"
test ! -L "$jc2_channel/release.fifo"
test "$(stat -c '%u:%a' "$jc2_channel")" = 0:700
test "$(stat -c '%u:%a' "$jc2_channel/release.fifo")" = 0:600
cd '/home/ubuntu/jc2-closedchild-preflight9-20260911b/stage'
# ROOT's split-stage manifest excludes the still-absent final registration.
sha256sum -c 'PRE-ADMISSION-INSTALLED.sha256'
sha256sum -c 'native.sha256'
test "$(sha256sum "$jc2_base/admin/holder.py" | cut -d' ' -f1)" = 'JC2_FINAL_HOLDER_SHA_PLACEHOLDER'
test "$(stat -c '%u:%a' "$jc2_base/admin/holder.py")" = 0:444
# Existing independent absolute TERM/KILL and externally armed worker stop.
# Worker retirement is a COORDINATOR user-systemd duty, not a worker unit.
# ROOT verifies its exact instance/argv/original deadline and active timer on
# the coordinator immediately before remote admission, and freezes the receipt
# in the execution card. No dummy or unrelated worker-local timer substitutes.
systemd-run --unit=jc2-closedchild-preflight9-20260911b-term \
 --on-calendar='2026-09-11 12:35:00 UTC' --timer-property=AccuracySec=1s \
 /usr/bin/systemctl kill --kill-whom=all --signal=TERM "$jc2_unit"
systemd-run --unit=jc2-closedchild-preflight9-20260911b-kill \
 --on-calendar='2026-09-11 12:35:05 UTC' --timer-property=AccuracySec=1s \
 /usr/bin/systemctl kill --kill-whom=all --signal=KILL "$jc2_unit"
systemctl is-active jc2-closedchild-preflight9-20260911b-term.timer jc2-closedchild-preflight9-20260911b-kill.timer
date -u '+ROOT_OUTER_TIMERS_ARMED_BEFORE_HOLDER %Y-%m-%d %H:%M:%S.%N UTC'
jc2_capture_end=$((SECONDS + 60))
jc2_admitted=false
trap 'if test "$jc2_admitted" != true; then /usr/bin/timeout 5 /usr/bin/systemctl kill --kill-whom=all --signal=TERM "$jc2_unit" || true; fi' EXIT
/usr/bin/timeout 10 systemd-run --unit="$jc2_unit" --property=Type=exec \
 --property=WorkingDirectory=/opt/jc2-closedchild-preflight9-20260911b/wrapper \
 --property=RuntimeMaxSec=3000 --property=RuntimeRandomizedExtraSec=0 \
 --property=TimeoutStopSec=5 --property=KillMode=control-group \
 --property=MemoryMax=8589934592 --property=MemorySwapMax=0 --property=OOMPolicy=kill \
 --property=TasksMax=32 --property=CPUAccounting=yes --property=CPUQuota=69% \
 --property=CPUQuotaPeriodSec=10ms --property=CPUSchedulingPolicy=other \
 --property=RestrictRealtime=yes --property=Delegate=no --property=Restart=no \
 --property=StandardInput=null \
 --property=StandardOutput=file:/run/jc2-closedchild-preflight9-20260911b/outer.stdout \
 --property=StandardError=file:/run/jc2-closedchild-preflight9-20260911b/outer.stderr \
 /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC \
 /usr/bin/python3.12 -I -S -B \
 /opt/jc2-closedchild-preflight9-20260911b/admin/holder.py
while test "$SECONDS" -lt "$jc2_capture_end"; do
 jc2_main=$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)
 if [[ "$jc2_main" =~ ^[1-9][0-9]*$ ]] && test -r /proc/"$jc2_main"/cmdline &&
    test "$(head -c 129 /run/jc2-closedchild-preflight9-20260911b/outer.stdout)" = HOLDER_WAITING_FOR_ROOT_RELEASE; then
  test "$(tr '\0' '\n' < /proc/"$jc2_main"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\n/opt/jc2-closedchild-preflight9-20260911b/admin/holder.py'
  test "$(sed -n '1p' /proc/"$jc2_main"/cgroup)" = "0::/system.slice/$jc2_unit"
  test "$(readlink /proc/"$jc2_main"/ns/pid)" = 'JC2_PID_NAMESPACE_PLACEHOLDER'
  test "$(readlink /proc/"$jc2_main"/exe)" = /usr/bin/python3.12
  test "$(sed -n '1,4p' "$jc2_cgroup/cgroup.procs")" = "$jc2_main"
  test -z "$(< /proc/"$jc2_main"/task/"$jc2_main"/children)"
  test "$(sed -n '1p' "$jc2_cgroup/cpu.max")" = '6900 10000'
  test "$(sed -n '1p' "$jc2_cgroup/cpu.max.burst")" = 0
  test "$(sed -n '1p' "$jc2_cgroup/memory.max")" = 8589934592
  test "$(sed -n '1p' "$jc2_cgroup/memory.swap.max")" = 0
  test "$(sed -n '1p' "$jc2_cgroup/pids.max")" = 32
  test "$(sed -n '1p' "$jc2_cgroup/cgroup.type")" = domain
  test -z "$(< "$jc2_cgroup/cgroup.subtree_control")"
  /usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID -p ControlPID -p InvocationID -p ControlGroup -p ActiveState -p ExecMainStartTimestamp -p Type -p RuntimeMaxUSec -p RuntimeRandomizedExtraUSec -p TimeoutStopUSec -p KillMode -p MemoryMax -p MemorySwapMax -p TasksMax -p CPUQuotaPerSecUSec -p CPUQuotaPeriodUSec -p CPUSchedulingPolicy -p RestrictRealtime -p Delegate -p Restart
  /usr/bin/timeout 3 ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
  sed -n '1p' /proc/"$jc2_main"/stat
  /usr/bin/timeout 3 /usr/bin/chrt -p "$jc2_main"
  for jc2_control in cpu.max cpu.max.burst cpu.stat memory.max memory.swap.max memory.current pids.max cgroup.procs; do
   printf 'ROOT_CONTROL %s\n' "$jc2_control"
   sed -n '1,30p' "$jc2_cgroup/$jc2_control"
  done
  test "$SECONDS" -lt "$jc2_capture_end"
  test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_main"
  test "$(tr '\0' '\n' < /proc/"$jc2_main"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\n/opt/jc2-closedchild-preflight9-20260911b/admin/holder.py'
  test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
  test "$SECONDS" -lt "$jc2_capture_end"
  date -u '+ROOT_HOLDER_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
  jc2_admitted=true
  printf '%s\n' ADMITTED_NOT_RELEASED
  exit 0
 fi
 sleep 0.1
done
printf '%s\n' 'STOP: no holder admission within 60 seconds' >&2
exit 2
