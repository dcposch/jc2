#!/bin/bash
# INERT / UNBOUND. ROOT substitutes every token from one fresh registration.
set -eu
TASK_INSTANCE='__FRESH_INSTANCE_ID__'
TASK_BOOT='__FRESH_BOOT_ID__'
TASK_HOST='__FRESH_HOSTNAME__'
TASK_PID_NS='__FRESH_PID_NAMESPACE__'
TASK_CGROUP_NS='__FRESH_CGROUP_NAMESPACE__'
TASK_UID='__POSITIVE_SCIENCE_UID__'
TASK_GID='__POSITIVE_SCIENCE_GID__'
TASK_ADMISSION='__ORIGINAL_ADMISSION_UTC__'
TASK_TERM_AT='__ORIGINAL_DEADLINE_MINUS_5S_UTC__'
TASK_DEADLINE='__ORIGINAL_DEADLINE_UTC__'
TASK_UNIT='__SCIENCE_UNIT__'
TASK_TERM_JOB='__SCIENCE_TERM_TIMER_UNIT__'
TASK_KILL_JOB='__SCIENCE_KILL_TIMER_UNIT__'
TASK_REGISTRATION='/opt/jc2-mixed-20260912/meta/REGISTRATION.json'
TASK_REGISTRATION_SHA='__ENABLED_REGISTRATION_SHA256__'
TASK_PYTHON='/usr/bin/python3.12'
TASK_PYTHON_SHA='__PINNED_PYTHON_SHA256__'
TASK_DISPATCH='/opt/jc2-mixed-20260912/runtime/dispatch.py'
TASK_DISPATCH_SHA='__PINNED_CAPTURE_DISPATCH_SHA256__'
TASK_MOUNT='/opt/jc2-mixed-20260912/science-tmpfs'
TASK_OUTPUT="$TASK_MOUNT/output"
TASK_ADMIN="$TASK_MOUNT/admin"
TASK_EXPECTED_CGROUP="/system.slice/$TASK_UNIT.service"
TASK_EXPECTED_CGROUP_FS="/sys/fs/cgroup$TASK_EXPECTED_CGROUP"

case "$TASK_UID:$TASK_GID" in *[!0-9:]*|0:*|*:0|'':*|*:) exit 2;; esac
test "$(tr -d '\n' </sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' </sys/class/dmi/id/board_asset_tag)" = "$TASK_INSTANCE"
test "$(cat /proc/sys/kernel/random/boot_id)" = "$TASK_BOOT"
test "$(hostname)" = "$TASK_HOST"
test "$(readlink /proc/self/ns/pid)" = "$TASK_PID_NS"
test "$(readlink /proc/self/ns/cgroup)" = "$TASK_CGROUP_NS"
test "$(sha256sum "$TASK_PYTHON" | cut -d' ' -f1)" = "$TASK_PYTHON_SHA"
test "$(sha256sum "$TASK_DISPATCH" | cut -d' ' -f1)" = "$TASK_DISPATCH_SHA"
test "$(sha256sum "$TASK_REGISTRATION" | cut -d' ' -f1)" = "$TASK_REGISTRATION_SHA"
test ! -e "$TASK_MOUNT"
install -d -o root -g root -m 0755 "$TASK_MOUNT"
mount -t tmpfs -o size=268435456,mode=0755,nodev,nosuid,noexec tmpfs "$TASK_MOUNT"
install -d -o root -g root -m 0755 "$TASK_ADMIN"
install -d -o "$TASK_UID" -g "$TASK_GID" -m 0700 "$TASK_OUTPUT"
test "$(find "$TASK_MOUNT" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf 'admin\noutput')"
test -z "$(find "$TASK_ADMIN" "$TASK_OUTPUT" -mindepth 1 -print -quit)"

TASK_TERM_CALENDAR="$(date -u -d "$TASK_TERM_AT" '+%Y-%m-%d %H:%M:%S UTC')"
TASK_KILL_CALENDAR="$(date -u -d "$TASK_DEADLINE" '+%Y-%m-%d %H:%M:%S UTC')"
test "$(date -u -d "$TASK_TERM_CALENDAR" +%s)" = "$(date -u -d "$TASK_TERM_AT" +%s)"
test "$(date -u -d "$TASK_KILL_CALENDAR" +%s)" = "$(date -u -d "$TASK_DEADLINE" +%s)"
systemd-run --quiet --unit="$TASK_TERM_JOB" --on-calendar="$TASK_TERM_CALENDAR" \
  --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=TERM "$TASK_UNIT.service"
systemd-run --quiet --unit="$TASK_KILL_JOB" --on-calendar="$TASK_KILL_CALENDAR" \
  --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=KILL "$TASK_UNIT.service"
TASK_TIMERS_ARMED="$(systemctl show "$TASK_TERM_JOB.timer" "$TASK_KILL_JOB.timer" \
  -p Id -p LoadState -p ActiveState -p NextElapseUSecRealtime)"
test "${#TASK_TIMERS_ARMED}" -le 8192
test "$(systemctl show "$TASK_TERM_JOB.timer" -P ActiveState)" = active
test "$(systemctl show "$TASK_KILL_JOB.timer" -P ActiveState)" = active
TASK_LAUNCH_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
test ! "$TASK_LAUNCH_UTC" \< "$TASK_ADMISSION"
test "$TASK_LAUNCH_UTC" \< "$TASK_DEADLINE"

set +e
systemd-run --quiet --wait --unit="$TASK_UNIT" --service-type=exec \
  -p Slice=system.slice -p User=root -p Group=root -p Restart=no -p KillMode=control-group \
  -p Delegate=no -p NoNewPrivileges=yes \
  -p 'CapabilityBoundingSet=CAP_DAC_OVERRIDE CAP_KILL CAP_SETUID CAP_SETGID' -p AmbientCapabilities= \
  -p RestrictRealtime=yes -p RestrictNamespaces=yes -p ProtectControlGroups=yes \
  -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms -p MemoryMax=34359738368 \
  -p MemorySwapMax=0 -p TasksMax=64 -p LimitCPU=3300 \
  -p LimitAS=34359738368 -p LimitFSIZE=268435456 \
  -p RuntimeMaxSec=3535s -p TimeoutStopSec=5s \
  -p StandardOutput=journal -p StandardError=journal \
  -E TMPDIR="$TASK_OUTPUT" -E TMP="$TASK_OUTPUT" -E TEMP="$TASK_OUTPUT" \
  -E XDG_CACHE_HOME="$TASK_OUTPUT" -E PYTHONPYCACHEPREFIX="$TASK_OUTPUT/pycache" \
  "$TASK_PYTHON" -E -s -S -B "$TASK_DISPATCH" \
    --registration "$TASK_REGISTRATION" --sha256 "$TASK_REGISTRATION_SHA"
TASK_WAIT_RC=$?
set -e
printf '%s\n' "$TASK_TIMERS_ARMED" >"$TASK_ADMIN/timers-armed.properties"
printf '%s\n' "$TASK_WAIT_RC" >"$TASK_ADMIN/systemd-run.exit"
set +e
systemctl show "$TASK_UNIT.service" -p Id -p LoadState -p ActiveState -p SubState \
  -p Result -p ExecMainCode -p ExecMainStatus >"$TASK_ADMIN/unit-terminal.properties" \
  2>"$TASK_ADMIN/unit-show.stderr"
TASK_SHOW_RC=$?
set -e
systemctl status "$TASK_UNIT.service" --no-pager --lines=256 | \
  head -c 65536 >"$TASK_ADMIN/pre-admission-or-unit.journal"
test "$(stat -c %s "$TASK_ADMIN/unit-show.stderr")" -le 4096

test "$TASK_SHOW_RC" -eq 0
TASK_UNIT_LOAD="$(sed -n 's/^LoadState=//p' "$TASK_ADMIN/unit-terminal.properties")"
if test "$TASK_UNIT_LOAD" = loaded; then
  if test -e "$TASK_EXPECTED_CGROUP_FS"; then
    test -r "$TASK_EXPECTED_CGROUP_FS/cgroup.procs"
    head -c 1 "$TASK_EXPECTED_CGROUP_FS/cgroup.procs" >"$TASK_ADMIN/cgroup.procs.first-byte"
    test ! -s "$TASK_ADMIN/cgroup.procs.first-byte"
    test "$(find "$TASK_EXPECTED_CGROUP_FS" -mindepth 1 -type d -print -quit)" = ''
  fi
  if ! systemctl reset-failed "$TASK_UNIT.service"; then
    test "$(systemctl show "$TASK_UNIT.service" -P LoadState)" = not-found
  fi
  test ! -e "$TASK_EXPECTED_CGROUP_FS"
else
  test "$TASK_UNIT_LOAD" = not-found
  test "$TASK_WAIT_RC" -eq 0
  systemctl show --property=Version --value >/dev/null
  test -z "$(systemctl list-units --all --full --plain --no-legend "$TASK_UNIT.service")"
  test ! -e "$TASK_EXPECTED_CGROUP_FS"
  printf '%s\n' UNIT_ALREADY_UNLOADED_AFTER_WAIT >"$TASK_ADMIN/unit-unloaded.status"
fi
systemctl stop "$TASK_TERM_JOB.timer" "$TASK_KILL_JOB.timer"
test "$(systemctl is-active "$TASK_TERM_JOB.timer" || true)" = inactive
test "$(systemctl is-active "$TASK_KILL_JOB.timer" || true)" = inactive
test "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \< "$TASK_DEADLINE"
test -z "$(find "$TASK_MOUNT" -xdev -type f -size +268435456c -print -quit)"
find "$TASK_MOUNT" -xdev -printf '%P\n' | LC_ALL=C sort >"$TASK_ADMIN/final-census"
find "$TASK_MOUNT" -xdev -type f ! -path "$TASK_ADMIN/terminal.sha256" -print0 | \
  LC_ALL=C sort -z | xargs -0 sha256sum >"$TASK_ADMIN/terminal.sha256"
test "$TASK_WAIT_RC" -eq 0

# ROOT must authenticate the admission/deadline/timer relation and live unit/cgroup
# controls, fsync files and parents, whole-read/hash the exact census, durably
# transfer it, and retire the exact unit/worker. Any failure is STOP; no retry.
