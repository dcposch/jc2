#!/bin/bash
# INERT AWS-only read-only observer. Bind every placeholder and review the
# resulting bytes before use. It never starts, stops, signals, or writes target state.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
  printf '%s\n' 'DISABLED: unresolved native-live observation binding' >&2
  exit 2
fi

task_instance=JC2_INSTANCE_PLACEHOLDER
task_boot=JC2_BOOT_PLACEHOLDER
task_host=JC2_HOST_PLACEHOLDER
task_pid_ns=JC2_PID_NS_PLACEHOLDER
task_cgroup_ns=JC2_CGROUP_NS_PLACEHOLDER
task_cutoff='JC2_ORIGINAL_CUTOFF_PLACEHOLDER'
task_unit=jc2-mixed-v3-native-20260913.service
task_control_group=/system.slice/jc2-mixed-v3-native-20260913.service
task_cgroup_fs=/sys/fs/cgroup/system.slice/jc2-mixed-v3-native-20260913.service
task_script=/opt/jc2-mixed-20260912/meta/native-metadata.actual.sh

task_read_bounded() {
  test "$#" -eq 1
  local task_value
  task_value="$(/usr/bin/head -c 4097 -- "$1"; printf x)"
  test "${#task_value}" -le 4097
  task_value="${task_value%x}"
  printf '%s' "$task_value"
}

task_property() {
  test "$#" -eq 2
  local task_key="$1" task_blob="$2" task_rows
  task_rows="$(printf '%s\n' "$task_blob" | /usr/bin/sed -n "s/^${task_key}=//p")"
  test "$(printf '%s\n' "$task_blob" | /usr/bin/sed -n "/^${task_key}=/p" | /usr/bin/wc -l)" -eq 1
  printf '%s' "$task_rows"
}

test "$(id -u)" -eq 0
test "$(task_read_bounded /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(task_read_bounded /sys/class/dmi/id/board_asset_tag)" = "$task_instance"
test "$(task_read_bounded /proc/sys/kernel/random/boot_id)" = "$task_boot"
test "$(hostname)" = "$task_host"
test "$(readlink /proc/self/ns/pid)" = "$task_pid_ns"
test "$(readlink /proc/self/ns/cgroup)" = "$task_cgroup_ns"
task_cutoff_epoch="$(date -u -d "$task_cutoff" +%s)"
test "$(date -u +%s)" -lt "$task_cutoff_epoch"
test "$(readlink -f -- "$task_cgroup_fs")" = "$task_cgroup_fs"

task_started=0
task_properties=''
task_pid=''
for ((task_poll=0; task_poll<60; task_poll++)); do
  test "$(date -u +%s)" -lt "$task_cutoff_epoch"
  task_probe="$(systemctl show "$task_unit" \
    -p Id -p LoadState -p ActiveState -p SubState -p MainPID -p ControlGroup \
    -p ExecStart -p Restart -p KillMode -p CPUQuotaPerSecUSec \
    -p CPUQuotaPeriodUSec -p MemoryMax -p MemorySwapMax -p TasksMax \
    -p LimitAS -p LimitFSIZE -p RuntimeMaxUSec -p TimeoutStopUSec -p InvocationID)"
  test "${#task_probe}" -le 8192
  task_probe_load="$(task_property LoadState "$task_probe")"
  task_probe_active="$(task_property ActiveState "$task_probe")"
  task_probe_pid="$(task_property MainPID "$task_probe")"
  if test "$task_probe_load" = loaded && test "$task_probe_active" = active \
      && [[ "$task_probe_pid" =~ ^[1-9][0-9]*$ ]]; then
    task_properties="$task_probe"
    task_pid="$task_probe_pid"
    task_started=1
    break
  fi
  sleep 1
done
test "$task_started" -eq 1

# Capture begins here. Every later failure is terminal; there is no return to polling.
test "$(task_property Id "$task_properties")" = "$task_unit"
test "$(task_property LoadState "$task_properties")" = loaded
test "$(task_property ActiveState "$task_properties")" = active
test "$(task_property ControlGroup "$task_properties")" = "$task_control_group"
test "$(task_property Restart "$task_properties")" = no
test "$(task_property KillMode "$task_properties")" = control-group
test "$(task_property CPUQuotaPerSecUSec "$task_properties")" = 800ms
test "$(task_property CPUQuotaPeriodUSec "$task_properties")" = 100ms
test "$(task_property MemoryMax "$task_properties")" = 1073741824
test "$(task_property MemorySwapMax "$task_properties")" = 0
test "$(task_property TasksMax "$task_properties")" = 64
test "$(task_property LimitAS "$task_properties")" = 1073741824
test "$(task_property LimitFSIZE "$task_properties")" = 4194304
test "$(task_property RuntimeMaxUSec "$task_properties")" = '9min 55s'
test "$(task_property TimeoutStopUSec "$task_properties")" = 5s
task_invocation="$(task_property InvocationID "$task_properties")"
[[ "$task_invocation" =~ ^[0-9a-f]{32}$ ]]
task_exec="$(task_property ExecStart "$task_properties")"
[[ "$task_exec" == *"path=/usr/bin/bash ; argv[]=/usr/bin/bash $task_script ; ignore_errors=no"* ]]
[[ "$task_exec" == *"; pid=$task_pid ;"* ]]

task_stat="$(task_read_bounded "/proc/$task_pid/stat")"
task_stat_tail="${task_stat##*) }"
set -- $task_stat_tail
test "$#" -ge 20
task_ppid="$2"
task_pgid="$3"
task_start_ticks="${20}"
[[ "$task_ppid" =~ ^[0-9]+$ && "$task_pgid" =~ ^[0-9]+$ && "$task_start_ticks" =~ ^[1-9][0-9]*$ ]]
task_exe="$(readlink -f -- "/proc/$task_pid/exe")"
test "$task_exe" = /usr/bin/bash
task_proc_pid_ns="$(readlink "/proc/$task_pid/ns/pid")"
task_proc_cgroup_ns="$(readlink "/proc/$task_pid/ns/cgroup")"
test "$task_proc_pid_ns" = "$task_pid_ns"
test "$task_proc_cgroup_ns" = "$task_cgroup_ns"
task_proc_cgroup="$(task_read_bounded "/proc/$task_pid/cgroup")"
test "$task_proc_cgroup" = "0::$task_control_group"
task_status="$(task_read_bounded "/proc/$task_pid/status")"
printf '%s\n' "$task_status" | grep -Eq '^Uid:[[:space:]]+0[[:space:]]+0[[:space:]]+0[[:space:]]+0$'
printf '%s\n' "$task_status" | grep -Eq '^Gid:[[:space:]]+0[[:space:]]+0[[:space:]]+0[[:space:]]+0$'
task_limits="$(task_read_bounded "/proc/$task_pid/limits")"
printf '%s\n' "$task_limits" | grep -Eq '^Max file size[[:space:]]+4194304[[:space:]]+4194304[[:space:]]+bytes$'
printf '%s\n' "$task_limits" | grep -Eq '^Max address space[[:space:]]+1073741824[[:space:]]+1073741824[[:space:]]+bytes$'

task_argv=()
task_argv_bytes=0
while IFS= read -r -d '' task_arg; do
  task_argv_bytes=$((task_argv_bytes + ${#task_arg} + 1))
  test "$task_argv_bytes" -le 4096
  task_argv+=("$task_arg")
done < "/proc/$task_pid/cmdline"
test "${#task_argv[@]}" -eq 2
test "${task_argv[0]}" = /usr/bin/bash
test "${task_argv[1]}" = "$task_script"

test -d "$task_cgroup_fs"
task_cpu_max="$(task_read_bounded "$task_cgroup_fs/cpu.max")"
task_cpu_burst="$(task_read_bounded "$task_cgroup_fs/cpu.max.burst")"
task_memory_max="$(task_read_bounded "$task_cgroup_fs/memory.max")"
task_swap_max="$(task_read_bounded "$task_cgroup_fs/memory.swap.max")"
task_pids_max="$(task_read_bounded "$task_cgroup_fs/pids.max")"
task_cgroup_type="$(task_read_bounded "$task_cgroup_fs/cgroup.type")"
task_cgroup_procs="$(task_read_bounded "$task_cgroup_fs/cgroup.procs")"
test "$task_cpu_max" = '80000 100000'
test "$task_cpu_burst" = 0
test "$task_memory_max" = 1073741824
test "$task_swap_max" = 0
test "$task_pids_max" = 64
test "$task_cgroup_type" = domain
printf '%s\n' "$task_cgroup_procs" | grep -Fx "$task_pid" >/dev/null

task_stat_after="$(task_read_bounded "/proc/$task_pid/stat")"
task_stat_after_tail="${task_stat_after##*) }"
set -- $task_stat_after_tail
test "$#" -ge 20
test "$2" = "$task_ppid"
test "$3" = "$task_pgid"
test "${20}" = "$task_start_ticks"
task_properties_after="$(systemctl show "$task_unit" \
  -p Id -p LoadState -p ActiveState -p MainPID -p ControlGroup -p InvocationID)"
test "${#task_properties_after}" -le 4096
test "$(task_property Id "$task_properties_after")" = "$task_unit"
test "$(task_property LoadState "$task_properties_after")" = loaded
test "$(task_property ActiveState "$task_properties_after")" = active
test "$(task_property MainPID "$task_properties_after")" = "$task_pid"
test "$(task_property ControlGroup "$task_properties_after")" = "$task_control_group"
test "$(task_property InvocationID "$task_properties_after")" = "$task_invocation"
test "$(readlink -f -- "/proc/$task_pid/exe")" = "$task_exe"
test "$(date -u +%s)" -lt "$task_cutoff_epoch"

task_total=$(( ${#task_properties} + ${#task_properties_after} + ${#task_stat} + \
  ${#task_status} + ${#task_limits} + ${#task_proc_cgroup} + \
  ${#task_cgroup_procs} + 8192 ))
test "$task_total" -lt 65536
printf '%s\n' 'NATIVE_LIVE_CAPTURE_V1'
printf 'capture_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%S.%NZ)"
printf 'instance=%s\nboot=%s\nhost=%s\nunit=%s\ninvocation=%s\n' \
  "$task_instance" "$task_boot" "$task_host" "$task_unit" "$task_invocation"
printf 'pid=%s\nppid=%s\npgid=%s\nstart_ticks=%s\nexe=%s\npid_ns=%s\ncgroup_ns=%s\n' \
  "$task_pid" "$task_ppid" "$task_pgid" "$task_start_ticks" "$task_exe" \
  "$task_proc_pid_ns" "$task_proc_cgroup_ns"
printf 'argv0=%q\nargv1=%q\n' "${task_argv[0]}" "${task_argv[1]}"
printf '%s\n%s\n' '--- systemd-initial ---' "$task_properties"
printf '%s\n%s\n' '--- systemd-final ---' "$task_properties_after"
printf '%s\n%s\n' '--- proc-stat ---' "$task_stat"
printf '%s\n%s\n' '--- proc-status ---' "$task_status"
printf '%s\n%s\n' '--- proc-limits ---' "$task_limits"
printf '%s\n%s\n' '--- proc-cgroup ---' "$task_proc_cgroup"
printf 'cpu.max=%s\ncpu.max.burst=%s\nmemory.max=%s\nmemory.swap.max=%s\npids.max=%s\ncgroup.type=%s\n' \
  "$task_cpu_max" "$task_cpu_burst" "$task_memory_max" "$task_swap_max" \
  "$task_pids_max" "$task_cgroup_type"
printf '%s\n%s\n' '--- cgroup.procs ---' "$task_cgroup_procs"
printf '%s\n' 'NATIVE_LIVE_CAPTURE_COMPLETE'
