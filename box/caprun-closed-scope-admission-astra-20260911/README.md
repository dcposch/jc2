# Disabled admission materialization

STATIC/UNEXECUTED. Neither file was run, imported, syntax checked, compiled, AST parsed or tested. Both require focused review and actual host qualification. No active registration or authority is included.

## Fixed interfaces

The proposed installation is `/opt/jc2-closedchild-preflight9-20260911a/admin/holder.py`, outside both the exact five-file science directory and exact three-file wrapper directory. The root0700 channel is the separate `/run/jc2-closedchild-preflight9-20260911a-admission`, outside the batch output mount; its one precreated root0600 FIFO is `release.fifo`. These are literal prospective layout choices, not observed paths. ROOT authenticates ancestors, ownership, ACLs, no concurrent replacement, interpreter/admin helper identities and native startup behavior. No installer is supplied.

ROOT must finalize a separate immutable holder copy with ENABLED=True, RELEASE=ROOT_HOLDER_ADMISSION_ONLY, one unique64-lowercase-hex TOKEN, exact host/boot/PID namespace, and two fixed UTC+00:00 timestamps. CUTOFF is strictly before the unchanged admission deadline. No actual values are selected here. The holder's120-second monotonic ceiling is an UNMEASURED planning ceiling inside the original deadlines, not extra time. CPython initialization precedes its local timer; original systemd lifetime and independent absolute stop timers enclose startup too.

The holder requires `/usr/bin/python3.12 -I -S -B` with only its literal script argument. It reads no input commands, environment or registration JSON. After ROOT final freeze/review, the unique authorized writer sends exactly the73-byte frame `RELEASE ` followed by64 lowercase hexadecimal token bytes and newline, then closes its write descriptor. No writer script or token is supplied. ROOT must not send anything until the outer template has returned ADMITTED_NOT_RELEASED and ROOT has authenticated the actual unit, all nine leaves and final frozen registration.

No-writer/empty-before-first-data EOF waits until the fixed cutoff; it cannot release. Reads are nonblocking and at most74 bytes total; poll intervals are at most100ms. Prefix mismatch, extra/duplicate bytes in that stream, partial frame followed by EOF, error or cutoff stops. Exact full frame without writer close still waits and times out. After one completed frame, the reader closes; a later separate writer is outside the trusted ROOT-exclusive-one-writer/no-restart contract. This is not authentication against malicious ROOT or an assertion that a FIFO can prove no future writer.

The fixed stdout line HOLDER_WAITING_FOR_ROOT_RELEASE is emitted after the absent-registration check and successful FIFO identity/open checks. The outer template requires that bounded sentinel, live literal holder argv, no holder child, sole direct membership, PID namespace/executable and kernel controls. It records unit/InvocationID/start/PGID/scheduler/settings/counters and accepts only before its60-second capture bound. All setup/collector shell children remain outside the holder unit. The outer template never creates leaves, final registration or release bytes. Admission is not final physical qualification: ROOT must inspect all recorded systemd settings, actual mount/cgroup/user namespaces and effective ownership/interfaces before release.

## Exec and accounting boundary

Holder creates no child, thread, subprocess, shell or helper. Before waiting it closes inherited descriptors above2, replaces stdin by /dev/null and retains only regular stdout/stderr; the FIFO is CLOEXEC and explicitly closed. Before exec it again closes all extra descriptors, resets signal dispositions to defaults and clears blocked signals, cancels its private wait timer, sets cwd/umask, rechecks cutoff and uses os.execve with the exact seven-element registered outer_argv and only PATH/LANG/LC_ALL/TZ. No eval, arbitrary argv or environment arrives through the FIFO. Uncaught termination may produce a signal exit; ordinary handled errors report HOLDER_STOP_NO_DISPATCH and exit2. Failed exec never retries.

PID/start/cgroup and systemd RuntimeMaxSec3000 persist; timers are not rearmed. aggregate_cpu_start_usec remains0, so holder CPU is included. All old memory/swap/CPU/quota/Tasks/kill/restart properties remain literal. Source900/600 and batch3000/2100/8GiB/128MiB are unchanged; PREFLIGHT_ONLY_9 remains the sole later mode. No FULL13, successful producer/checker, probe or dummy is launched by this preparation.

ROOT still owes split installation/manifests excluding the absent final registration, final registration serialization/installation0444/fsync/readback, native qualification including administrative helpers, no-migration/one-writer exclusivity, actual nine leaf identities and empty topology, actual same-process namespace view, terminal quiet and durable custody. The holder's final registration mode/path check is not independent SHA authentication: external ROOT must bind that SHA and all physical pins to its one-time release record. Tiny check-to-exec scheduling intervals are not atomic clock or adversarial-root proofs. Existing stale-positive false-STOP risk is unchanged.

Specific untested OS interfaces: Linux FIFO POLLIN/POLLHUP/EOF behavior, CPython3.12 valid-signal reset and descriptor inheritance across exec, systemd Type=exec identity/accounting, shell procfs/timeout capture, installed native/namespace closure. No host observations are fabricated. Unexpected behavior is STOP, not retry or a cap increase.

QUANTITY: can this exact admission holder yield one captured live identity, one authenticated registration freeze and one same-PID release under the unchanged clocks? Unknown. CHEAPEST TEST: focused static review of these two exact files, then separately ROOT-authorized administrative qualification. Planning wall10 minutes UNMEASURED for review;120 seconds is only the proposed bounded admission allowance, not measured execution. No new foundation review or scientific experiment is requested.

## Literal outer-template delta

The following documentary unified diff is generated from the one pinned old outer file and this owned new template. It is not executed.

```diff
--- accepted-outer-launch.template.sh
+++ proposed-outer-admission.template.sh
@@ -1,72 +1,95 @@
 #!/bin/bash
-# DISABLED ROOT outer launch template. Existing OS controls; no science changes.
+# DISABLED ROOT admission only. STATIC/UNTESTED; never writes a release token.
 set -euo pipefail
 test "$(id -u)" = 0
 if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
- printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
+ printf '%s\n' 'DISABLED: unresolved ROOT admission metadata' >&2
  exit 2
 fi
-test 'JC2_OUTER_RELEASE_PLACEHOLDER' = ROOT_RELEASED_EXACT_NECESSARY_ROWS_BATCH
+test 'JC2_OUTER_RELEASE_PLACEHOLDER' = ROOT_ADMIT_HOLDER_ONLY
 test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = 'JC2_INSTANCE_PLACEHOLDER'
 test "$(sed -n '1p' /proc/sys/kernel/random/boot_id)" = 'JC2_BOOT_ID_PLACEHOLDER'
-test "$(date -u +%s)" -lt "$(date -ud 'JC2_LATEST_DISPATCH_LAUNCH_UTC_PLACEHOLDER' +%s)"
-jc2_unit=jc2-r3-necessaryrows-20260911a.service
+test "$(date -u +%s)" -lt "$(date -ud 'JC2_LATEST_HOLDER_LAUNCH_UTC_PLACEHOLDER' +%s)"
+jc2_unit=jc2-closedchild-preflight9-20260911a.service
 jc2_cgroup=/sys/fs/cgroup/system.slice/$jc2_unit
+jc2_base=/opt/jc2-closedchild-preflight9-20260911a
+jc2_channel=/run/jc2-closedchild-preflight9-20260911a-admission
 test ! -e "$jc2_cgroup"
-cd '/home/ubuntu/jc2-r3-necessaryrows-20260911a/stage'
-sha256sum -c installed.sha256
-sha256sum -c native.sha256
-# Both independent absolute stop timers are armed BEFORE any dispatcher process.
-systemd-run --unit=jc2-r3-necessaryrows-20260911a-term \
+test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
+test ! -L "$jc2_base/metadata/ROOT-REGISTRATION.json"
+test -p "$jc2_channel/release.fifo"
+test ! -L "$jc2_channel/release.fifo"
+test "$(stat -c '%u:%a' "$jc2_channel")" = 0:700
+test "$(stat -c '%u:%a' "$jc2_channel/release.fifo")" = 0:600
+cd 'JC2_ADMISSION_STAGE_PATH_PLACEHOLDER'
+# ROOT's split-stage manifest excludes the still-absent final registration.
+sha256sum -c 'JC2_ADMISSION_INPUTS_MANIFEST_PLACEHOLDER'
+sha256sum -c 'JC2_NATIVE_MANIFEST_PATH_PLACEHOLDER'
+test "$(sha256sum "$jc2_base/admin/holder.py" | cut -d' ' -f1)" = 'JC2_FINAL_HOLDER_SHA_PLACEHOLDER'
+test "$(stat -c '%u:%a' "$jc2_base/admin/holder.py")" = 0:444
+# Existing independent absolute TERM/KILL and externally armed worker stop.
+systemctl is-active 'JC2_WORKER_STOP_TIMER_PLACEHOLDER'
+systemd-run --unit=jc2-closedchild-preflight9-20260911a-term \
  --on-calendar='JC2_MATH_TERM_UTC_PLACEHOLDER' --timer-property=AccuracySec=1s \
  /usr/bin/systemctl kill --kill-whom=all --signal=TERM "$jc2_unit"
-systemd-run --unit=jc2-r3-necessaryrows-20260911a-kill \
+systemd-run --unit=jc2-closedchild-preflight9-20260911a-kill \
  --on-calendar='JC2_MATH_KILL_UTC_PLACEHOLDER' --timer-property=AccuracySec=1s \
  /usr/bin/systemctl kill --kill-whom=all --signal=KILL "$jc2_unit"
-systemctl is-active jc2-r3-necessaryrows-20260911a-term.timer jc2-r3-necessaryrows-20260911a-kill.timer
-date -u '+ROOT_OUTER_TIMERS_ARMED_BEFORE_LAUNCH %Y-%m-%d %H:%M:%S.%N UTC'
-systemd-run --unit="$jc2_unit" --property=Type=exec \
- --property=WorkingDirectory=/opt/jc2-r3-necessaryrows-20260911a/wrapper \
+systemctl is-active jc2-closedchild-preflight9-20260911a-term.timer jc2-closedchild-preflight9-20260911a-kill.timer
+date -u '+ROOT_OUTER_TIMERS_ARMED_BEFORE_HOLDER %Y-%m-%d %H:%M:%S.%N UTC'
+jc2_capture_end=$((SECONDS + 60))
+jc2_admitted=false
+trap 'if test "$jc2_admitted" != true; then /usr/bin/timeout 5 /usr/bin/systemctl kill --kill-whom=all --signal=TERM "$jc2_unit" || true; fi' EXIT
+/usr/bin/timeout 10 systemd-run --unit="$jc2_unit" --property=Type=exec \
+ --property=WorkingDirectory=/opt/jc2-closedchild-preflight9-20260911a/wrapper \
  --property=RuntimeMaxSec=3000 --property=RuntimeRandomizedExtraSec=0 \
  --property=TimeoutStopSec=5 --property=KillMode=control-group \
  --property=MemoryMax=8589934592 --property=MemorySwapMax=0 --property=OOMPolicy=kill \
  --property=TasksMax=32 --property=CPUAccounting=yes --property=CPUQuota=69% \
  --property=CPUQuotaPeriodSec=10ms --property=CPUSchedulingPolicy=other \
  --property=RestrictRealtime=yes --property=Delegate=no --property=Restart=no \
- --property=StandardOutput=file:/run/jc2-r3-necessaryrows-20260911a/outer.stdout \
- --property=StandardError=file:/run/jc2-r3-necessaryrows-20260911a/outer.stderr \
+ --property=StandardInput=null \
+ --property=StandardOutput=file:/run/jc2-closedchild-preflight9-20260911a/outer.stdout \
+ --property=StandardError=file:/run/jc2-closedchild-preflight9-20260911a/outer.stderr \
  /usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC \
  /usr/bin/python3.12 -I -S -B \
- /opt/jc2-r3-necessaryrows-20260911a/wrapper/dispatch.py \
- --registration /opt/jc2-r3-necessaryrows-20260911a/metadata/ROOT-REGISTRATION.json
-for jc2_try in $(seq 1 100); do
- jc2_main=$(systemctl show "$jc2_unit" -p MainPID --value)
- if test "$jc2_main" != 0 && test -r /proc/"$jc2_main"/cmdline; then
-  systemctl show "$jc2_unit" -p MainPID -p InvocationID -p ControlGroup -p ActiveState -p ExecMainStartTimestamp -p Type -p RuntimeMaxUSec -p RuntimeRandomizedExtraUSec -p TimeoutStopUSec -p KillMode -p MemoryMax -p MemorySwapMax -p TasksMax -p CPUQuotaPerSecUSec -p CPUQuotaPeriodUSec -p CPUSchedulingPolicy -p RestrictRealtime -p Delegate -p Restart
-  ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
+ /opt/jc2-closedchild-preflight9-20260911a/admin/holder.py
+while test "$SECONDS" -lt "$jc2_capture_end"; do
+ jc2_main=$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)
+ if [[ "$jc2_main" =~ ^[1-9][0-9]*$ ]] && test -r /proc/"$jc2_main"/cmdline &&
+    test "$(head -c 129 /run/jc2-closedchild-preflight9-20260911a/outer.stdout)" = HOLDER_WAITING_FOR_ROOT_RELEASE; then
+  test "$(tr '\0' '\n' < /proc/"$jc2_main"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\n/opt/jc2-closedchild-preflight9-20260911a/admin/holder.py'
+  test "$(sed -n '1p' /proc/"$jc2_main"/cgroup)" = "0::/system.slice/$jc2_unit"
+  test "$(readlink /proc/"$jc2_main"/ns/pid)" = 'JC2_PID_NAMESPACE_PLACEHOLDER'
+  test "$(readlink /proc/"$jc2_main"/exe)" = /usr/bin/python3.12
+  test "$(sed -n '1,4p' "$jc2_cgroup/cgroup.procs")" = "$jc2_main"
+  test -z "$(< /proc/"$jc2_main"/task/"$jc2_main"/children)"
+  test "$(sed -n '1p' "$jc2_cgroup/cpu.max")" = '6900 10000'
+  test "$(sed -n '1p' "$jc2_cgroup/cpu.max.burst")" = 0
+  test "$(sed -n '1p' "$jc2_cgroup/memory.max")" = 8589934592
+  test "$(sed -n '1p' "$jc2_cgroup/memory.swap.max")" = 0
+  test "$(sed -n '1p' "$jc2_cgroup/pids.max")" = 32
+  test "$(sed -n '1p' "$jc2_cgroup/cgroup.type")" = domain
+  test -z "$(< "$jc2_cgroup/cgroup.subtree_control")"
+  /usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID -p ControlPID -p InvocationID -p ControlGroup -p ActiveState -p ExecMainStartTimestamp -p Type -p RuntimeMaxUSec -p RuntimeRandomizedExtraUSec -p TimeoutStopUSec -p KillMode -p MemoryMax -p MemorySwapMax -p TasksMax -p CPUQuotaPerSecUSec -p CPUQuotaPeriodUSec -p CPUSchedulingPolicy -p RestrictRealtime -p Delegate -p Restart
+  /usr/bin/timeout 3 ps -p "$jc2_main" -o pid=,ppid=,pgid=,lstart=,args=
   sed -n '1p' /proc/"$jc2_main"/stat
-  readlink /proc/"$jc2_main"/ns/pid
-  /usr/bin/chrt -p "$jc2_main"
+  /usr/bin/timeout 3 /usr/bin/chrt -p "$jc2_main"
   for jc2_control in cpu.max cpu.max.burst cpu.stat memory.max memory.swap.max memory.current pids.max cgroup.procs; do
    printf 'ROOT_CONTROL %s\n' "$jc2_control"
    sed -n '1,30p' "$jc2_cgroup/$jc2_control"
   done
-  if test "$(sed -n '1p' "$jc2_cgroup/cpu.max")" != '6900 10000' ||
-     test "$(sed -n '1p' "$jc2_cgroup/cpu.max.burst")" != 0 ||
-     test "$(sed -n '1p' "$jc2_cgroup/memory.max")" != 8589934592 ||
-     test "$(sed -n '1p' "$jc2_cgroup/memory.swap.max")" != 0 ||
-     test "$(sed -n '1p' "$jc2_cgroup/pids.max")" != 32; then
-    systemctl kill --kill-whom=all --signal=TERM "$jc2_unit"
-    exit 2
-  fi
-  for jc2_child in $(sed -n '1p' /proc/"$jc2_main"/task/"$jc2_main"/children); do
-   ps -p "$jc2_child" -o pid=,ppid=,pgid=,lstart=,args=
-  done
-  date -u '+ROOT_SAME_LAUNCH_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
+  test "$SECONDS" -lt "$jc2_capture_end"
+  test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_main"
+  test "$(tr '\0' '\n' < /proc/"$jc2_main"/cmdline)" = $'/usr/bin/python3.12\n-I\n-S\n-B\n/opt/jc2-closedchild-preflight9-20260911a/admin/holder.py'
+  test ! -e "$jc2_base/metadata/ROOT-REGISTRATION.json"
+  test "$SECONDS" -lt "$jc2_capture_end"
+  date -u '+ROOT_HOLDER_CAPTURE %Y-%m-%d %H:%M:%S.%N UTC'
+  jc2_admitted=true
+  printf '%s\n' ADMITTED_NOT_RELEASED
   exit 0
  fi
  sleep 0.1
 done
-systemctl show "$jc2_unit" -p MainPID -p ControlPID -p ActiveState -p SubState -p ExecMainStatus -p CPUUsageNSec
-date -u '+ROOT_NO_LIVE_CAPTURE_TERMINAL_CHECK_REQUIRED %Y-%m-%d %H:%M:%S.%N UTC'
+printf '%s\n' 'STOP: no holder admission within 60 seconds' >&2
 exit 2
```
