set -eu
TASK_INSTANCE='i-052458938409563d3'; TASK_BOOT='7fe794ce-6d60-4b81-b78f-995dc1ac182f'; TASK_HOST='ip-172-30-0-113'
TASK_PID_NS='pid:[4026531836]'; TASK_CGROUP_NS='cgroup:[4026531835]'
TASK_UID='65534'; TASK_GID='65534'; TASK_UNIT='jc2-mixed-v3-dummy-20260913'
TASK_TERM_JOB='jc2-mixed-v3-dummy-term-20260913'; TASK_KILL_JOB='jc2-mixed-v3-dummy-kill-20260913'
TASK_TERM_AT='2026-09-13 01:53:20 UTC'; TASK_KILL_AT='2026-09-13 01:53:25 UTC'
TASK_MOUNT='/opt/jc2-mixed-dummy-v3-20260913'; TASK_ADMIN="$TASK_MOUNT/admin"; TASK_OUTPUT="$TASK_MOUNT/output"
TASK_PYTHON='/usr/bin/python3.12'; TASK_SETPRIV='/usr/bin/setpriv'
TASK_CAPRUN='/opt/jc2-mixed-20260912/runtime/run_capped.py'; TASK_PROBE='/opt/jc2-mixed-20260912/runtime/probe.py'; TASK_JQ='/usr/bin/jq'
TASK_EXPECTED_CGROUP="/system.slice/$TASK_UNIT.service"
TASK_EXPECTED_CGROUP_FS="/sys/fs/cgroup$TASK_EXPECTED_CGROUP"
TASK_ARGV_SHA='e585a9fa1c85c2a84ccec59c96df6857cf3514822edb2c435ce1db01cb0eb8d5'; TASK_ARGV_COUNT='12'

test "$(sha256sum "$TASK_CAPRUN" | cut -d' ' -f1)" = 4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2
test "$(sha256sum "$TASK_PROBE" | cut -d' ' -f1)" = 16d723b7fbe6dc218351274e4078df1959add5c2914174079d707fdc14e17158
test "$(cat /proc/sys/kernel/random/boot_id)" = "$TASK_BOOT"
test "$(hostname)" = "$TASK_HOST"; test "$(readlink /proc/self/ns/pid)" = "$TASK_PID_NS"
test "$(readlink /proc/self/ns/cgroup)" = "$TASK_CGROUP_NS"

install -d -o root -g root -m 0755 "$TASK_MOUNT"
mount -t tmpfs -o size=268435456,mode=0755,nodev,nosuid,noexec tmpfs "$TASK_MOUNT"
install -d -o root -g root -m 0755 "$TASK_ADMIN"
install -d -o "$TASK_UID" -g "$TASK_GID" -m 0700 "$TASK_OUTPUT"
test "$(find "$TASK_MOUNT" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = "$(printf 'admin\noutput')"

systemd-run --quiet --unit="$TASK_TERM_JOB" --on-calendar="$TASK_TERM_AT" \
  --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=TERM "$TASK_UNIT.service"
systemd-run --quiet --unit="$TASK_KILL_JOB" --on-calendar="$TASK_KILL_AT" \
  --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=KILL "$TASK_UNIT.service"
systemctl show "$TASK_TERM_JOB.timer" "$TASK_KILL_JOB.timer" \
  -p Id -p LoadState -p ActiveState -p NextElapseUSecRealtime \
  >"$TASK_ADMIN/timers-armed.properties"
test "$(systemctl show "$TASK_TERM_JOB.timer" -P ActiveState)" = active
test "$(systemctl show "$TASK_KILL_JOB.timer" -P ActiveState)" = active

set +e
systemd-run --quiet --wait --unit="$TASK_UNIT" --service-type=exec \
  -p Slice=system.slice -p User=root -p Group=root -p Restart=no -p KillMode=control-group \
  -p Delegate=no -p NoNewPrivileges=yes \
  -p 'CapabilityBoundingSet=CAP_DAC_OVERRIDE CAP_KILL CAP_SETUID CAP_SETGID' -p AmbientCapabilities= \
  -p RestrictRealtime=yes -p RestrictNamespaces=yes -p ProtectControlGroups=yes \
  -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms -p MemoryMax=34359738368 \
  -p MemorySwapMax=0 -p TasksMax=64 -p LimitCPU=4 \
  -p LimitAS=34359738368 -p LimitFSIZE=268435456 \
  -p RuntimeMaxSec=20s -p TimeoutStopSec=5s \
  -p StandardOutput=file:"$TASK_OUTPUT/runner.stdout" \
  -p StandardError=file:"$TASK_OUTPUT/runner.stderr" \
  -E TMPDIR="$TASK_OUTPUT" -E TMP="$TASK_OUTPUT" -E TEMP="$TASK_OUTPUT" \
  -E XDG_CACHE_HOME="$TASK_OUTPUT" -E PYTHONPYCACHEPREFIX="$TASK_OUTPUT/pycache" \
  "$TASK_PYTHON" -E -s -S -B "$TASK_CAPRUN" \
    --wall-seconds 5 --cpu-seconds 3 --rss-bytes 33554432 \
    --stdout-file "$TASK_OUTPUT/dummy.stdout" --stderr-file "$TASK_OUTPUT/dummy.stderr" \
    --telemetry-file "$TASK_OUTPUT/dummy.telemetry.json" --cwd "$TASK_OUTPUT" -- \
    "$TASK_SETPRIV" --reuid="$TASK_UID" --regid="$TASK_GID" --clear-groups --no-new-privs \
    "$TASK_PYTHON" -E -s -S -B "$TASK_PROBE" --descendant-rss-term-kill
TASK_WAIT_RC=$?
set -e
printf '%s\n' "$TASK_WAIT_RC" >"$TASK_ADMIN/systemd-run.exit"
systemctl show "$TASK_UNIT.service" -p Id -p LoadState -p ActiveState -p SubState \
  -p Result -p ExecMainCode -p ExecMainStatus >"$TASK_ADMIN/unit-terminal.properties"
test "$TASK_WAIT_RC" -eq 125
test "$(systemctl show "$TASK_UNIT.service" -P ExecMainStatus)" = 125

task_size_le() { test "$(stat -c %s "$1")" -le "$2"; }
task_size_le "$TASK_OUTPUT/dummy.stdout" 4096
task_size_le "$TASK_OUTPUT/dummy.stderr" 4096
task_size_le "$TASK_OUTPUT/dummy.telemetry.json" 65536
task_size_le "$TASK_OUTPUT/runner.stdout" 4096
task_size_le "$TASK_OUTPUT/runner.stderr" 4096
test ! -s "$TASK_OUTPUT/dummy.stderr"; test ! -s "$TASK_OUTPUT/runner.stderr"
test "$(tail -c 1 "$TASK_OUTPUT/dummy.stdout" | od -An -tuC | tr -d ' ')" = 10
test "$(wc -l <"$TASK_OUTPUT/dummy.stdout")" -eq 2
test "$(sed -n '1p' "$TASK_OUTPUT/dummy.stdout")" = DESCENDANT_READY
TASK_JSON="$(sed -n '2p' "$TASK_OUTPUT/dummy.stdout")"
test "$(printf '%s\n' "$TASK_JSON" | "$TASK_JQ" -cS .)" = "$TASK_JSON"

printf '%s\n' "$TASK_JSON" | "$TASK_JQ" -e \
  --arg boot "$TASK_BOOT" --arg pns "$TASK_PID_NS" --arg cns "$TASK_CGROUP_NS" \
  --arg cg "$TASK_EXPECTED_CGROUP" --arg cgf "$TASK_EXPECTED_CGROUP_FS" \
  --arg uid "$TASK_UID" --arg gid "$TASK_GID" '
  keys==["boot_id","cap_eff","cgroup","cgroup_controls","cgroup_namespace","cgroup_path","cgroup_stat","gid","no_new_privs","payload_bytes","pgid","pid","pid_namespace","rlimits","schema","start_ticks","status","uid"] and
  .schema=="f10-mixed-dummy-identity/v2" and .status=="DESCENDANT_READY" and
  .boot_id==$boot and .pid_namespace==$pns and .cgroup_namespace==$cns and
  .cgroup==("0::"+$cg+"\n") and .cgroup_path==$cgf and .uid==$uid and .gid==$gid and
  .payload_bytes=="67108864" and .no_new_privs=="1" and .cap_eff=="0000000000000000" and
  (.pid|test("^[1-9][0-9]*$")) and (.pgid|test("^[1-9][0-9]*$")) and (.start_ticks|test("^[1-9][0-9]*$")) and
  .rlimits=={"as":["34359738368","34359738368"],"cpu":["3","4"],"fsize":["268435456","268435456"]} and
  (.cgroup_controls|keys)==["cgroup.controllers","cgroup.subtree_control","cgroup.type","cpu.max","cpu.max.burst","memory.max","memory.swap.max"] and
  .cgroup_controls["cpu.max"]=="80000 100000\n" and .cgroup_controls["cpu.max.burst"]=="0\n" and
  .cgroup_controls["memory.max"]=="34359738368\n" and .cgroup_controls["memory.swap.max"]=="0\n" and
  .cgroup_controls["cgroup.type"]=="domain\n" and .cgroup_controls["cgroup.subtree_control"]=="\n" and
  (.cgroup_stat|keys)==["device","gid","inode","mode","uid"]' >/dev/null

TASK_STDOUT_SHA="$(sha256sum "$TASK_OUTPUT/dummy.stdout" | cut -d' ' -f1)"
TASK_STDOUT_BYTES="$(stat -c %s "$TASK_OUTPUT/dummy.stdout")"
"$TASK_JQ" -e --arg boot "$TASK_BOOT" --arg out "$TASK_OUTPUT" --arg exe "$TASK_SETPRIV" \
  --arg sha "$TASK_STDOUT_SHA" --argjson bytes "$TASK_STDOUT_BYTES" \
  --argjson ac "$TASK_ARGV_COUNT" --arg ah "$TASK_ARGV_SHA" --argjson child "$TASK_JSON" '
  .schema=="CAPRUN/v1" and .status=="RESOURCE_CAP" and .resource=="rss" and
  .runner_exit_code==125 and .argv_count==$ac and .argv_sha256==$ah and
  .executable==$exe and .cwd==$out and .pid==.pgid and .pid!=($child.pid|tonumber) and
  .pgid==($child.pgid|tonumber) and .start_identity_source=="linux-proc-stat-field22" and
  (.start_identity|startswith("boot="+$boot+";start_ticks=")) and
  .max_observed_group_rss_bytes>33554432 and .caps.wall_seconds==5 and
  .caps.cpu_seconds==3 and .caps.rss_bytes==33554432 and
  .termination.reason=="rss_cap" and .termination.term_sent==true and
  .termination.kill_sent==true and .termination.leader_reaped==true and
  .termination.cleanup_complete==true and .termination.group_live_before_reap==[] and
  .stdout.sha256==$sha and .stdout.bytes==$bytes and .stderr.bytes==0' \
  "$TASK_OUTPUT/dummy.telemetry.json" >/dev/null
printf '%s\n' "CAPRUN/v1 status=RESOURCE_CAP telemetry=$TASK_OUTPUT/dummy.telemetry.json" >"$TASK_ADMIN/expected-runner.stdout"
cmp -s "$TASK_ADMIN/expected-runner.stdout" "$TASK_OUTPUT/runner.stdout"

if test -e "$TASK_EXPECTED_CGROUP_FS"; then
  test -r "$TASK_EXPECTED_CGROUP_FS/cgroup.procs"
  head -c 1 "$TASK_EXPECTED_CGROUP_FS/cgroup.procs" >"$TASK_ADMIN/cgroup.procs.first-byte"
  test ! -s "$TASK_ADMIN/cgroup.procs.first-byte"
  test "$(find "$TASK_EXPECTED_CGROUP_FS" -mindepth 1 -type d -print -quit)" = ''
fi
systemctl reset-failed "$TASK_UNIT.service"
test ! -e "$TASK_EXPECTED_CGROUP_FS"
systemctl stop "$TASK_TERM_JOB.timer" "$TASK_KILL_JOB.timer"
test "$(systemctl is-active "$TASK_TERM_JOB.timer" || true)" = inactive
test "$(systemctl is-active "$TASK_KILL_JOB.timer" || true)" = inactive

test -z "$(find "$TASK_MOUNT" -xdev -type f -size +268435456c -print -quit)"
find "$TASK_MOUNT" -xdev -printf '%P\n' | LC_ALL=C sort >"$TASK_ADMIN/final-census"
find "$TASK_MOUNT" -xdev -type f ! -path "$TASK_ADMIN/terminal.sha256" -print0 | \
  LC_ALL=C sort -z | xargs -0 sha256sum >"$TASK_ADMIN/terminal.sha256"
