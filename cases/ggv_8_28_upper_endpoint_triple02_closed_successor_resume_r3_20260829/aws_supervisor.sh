#!/usr/bin/env bash
set -uo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${JOB_NONCE:?}"
: "${CPU_ID:?}"
: "${EXPECTED_SOURCE_ARCHIVE_SHA256:?}"

[[ "$JOB_NONCE" =~ ^[a-z0-9]{8,32}$ ]] || exit 70
[[ "$JOB_TAG" == *"_$JOB_NONCE" ]] || exit 70

case_rel="cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r3_20260829"
case_dir="$JOB_ROOT/source/jc2/$case_rel"
worker="$case_dir/aws_job_worker.sh"
contract="$case_dir/containment_contract.py"
custody="$JOB_ROOT/custody"
terminal_marker="$JOB_ROOT/TERMINAL.marker"
lease_file="$JOB_ROOT/LEASE.json"
mkdir -p "$custody"
umask 077
launcher_pid=0
launcher_start=0
launcher_identity_gate=0
launcher_reap_failure=1
worker_pgid=0
containment_mode=pgid
scope_unit="codex-${JOB_TAG//[^A-Za-z0-9_.-]/-}"
scope_unit=${scope_unit:0:180}

emergency_cleanup() {
  if [[ "$containment_mode" == systemd_scope ]]; then
    systemctl --user kill --kill-whom=all --signal=KILL \
      "$scope_unit.scope" >/dev/null 2>&1 || true
  elif [[ "$worker_pgid" -gt 1 && "$worker_pgid" != "$(ps -o pgid= -p $$ | tr -d ' ')" ]]; then
    kill -KILL -- "-$worker_pgid" 2>/dev/null || true
  fi
  if [[ "$launcher_pid" -gt 1 && "$launcher_start" -gt 0 \
        && -f "$contract" ]]; then
    python3 "$contract" signal-pid --pid "$launcher_pid" \
      --starttime "$launcher_start" --signal KILL >/dev/null 2>&1 || true
  fi
  if [[ -f "$contract" ]]; then
    local emergency_pgid=$worker_pgid
    [[ "$containment_mode" == systemd_scope ]] && emergency_pgid=0
    python3 "$contract" cleanup --pgid "$emergency_pgid" \
      --job-tag "$JOB_TAG" --exclude-pid $$ \
      --pgid-output "$custody/emergency_pgid_census.json" \
      --tag-output "$custody/emergency_job_tag_census.json" \
      > "$custody/emergency_cleanup.stdout.txt" \
      2> "$custody/emergency_cleanup.stderr.txt" || true
  fi
}

publish_no_replace() {
  # ln(2) is atomic and never replaces an existing target.
  local content_file=$1
  ln "$content_file" "$terminal_marker" 2>/dev/null
}

publish_emergency_no_verdict() {
  if [[ ! -e "$terminal_marker" ]]; then
    local temporary="$JOB_ROOT/.TERMINAL.marker.emergency.$$"
    printf '%s\nTERMINAL_ARCHIVE_SHA256=NONE\nDECISION_RECORD_SHA256=NONE\n' \
      CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT > "$temporary" || true
    publish_no_replace "$temporary" || true
    rm -f "$temporary"
  fi
}
on_exit() {
  local rc=$?
  trap - EXIT
  if [[ ! -e "$terminal_marker" ]]; then
    emergency_cleanup
    publish_emergency_no_verdict
  fi
  exit "$rc"
}
trap on_exit EXIT
trap 'exit 143' TERM
trap 'exit 130' INT
trap 'exit 129' HUP

[[ "$(basename "$JOB_ROOT")" == "$JOB_TAG" ]] || exit 70
[[ ! -e "$JOB_ROOT/${JOB_TAG}.terminal.tar.gz" ]] || exit 70
[[ ! -e "$terminal_marker" ]] || exit 70
[[ -f "$worker" && -f "$contract" ]] || exit 70
# Direct-supervisor entry must verify the same atomic lease the launcher
# built, and must itself take an atomic supervisor sub-lease so a second
# supervisor in the same namespace fails closed.
[[ -f "$lease_file" && -f "$JOB_ROOT/LEASE.sha256" ]] || exit 70
[[ -f "$JOB_ROOT/launch_preflight_copy.sh" ]] || exit 70
python3 "$contract" lease-verify --lease "$lease_file" \
  --sidecar "$JOB_ROOT/LEASE.sha256" --job-tag "$JOB_TAG" \
  --job-nonce "$JOB_NONCE" \
  --source-archive-sha256 "$EXPECTED_SOURCE_ARCHIVE_SHA256" \
  > "$custody/supervisor_lease_verify.txt" 2>&1 || exit 70
mkdir "$JOB_ROOT/.supervisor_lease" 2>/dev/null || exit 70

supervisor_pid=$$
supervisor_pgid=$(ps -o pgid= -p $$ | tr -d ' ')
supervisor_sid=$(ps -o sid= -p $$ | tr -d ' ')
supervisor_start=$(awk '{print $22}' "/proc/$$/stat")
printf '{"pid":%s,"pgid":%s,"sid":%s,"starttime":%s,"cpu":%s}\n' \
  "$supervisor_pid" "$supervisor_pgid" "$supervisor_sid" \
  "$supervisor_start" "$CPU_ID" > "$custody/supervisor_identity.json"
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/SUPERVISOR_STARTED_UTC.txt"
start_epoch=$(date +%s)
export SUPERVISOR_PID="$supervisor_pid"
export SUPERVISOR_STARTTIME="$supervisor_start"
export LEASE_FILE="$lease_file"

swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
[[ "$swap_total" == 0 && "$swap_free" == 0 ]] || exit 73

# C3: only a transient user scope with an independent runtime deadline,
# control-group kill mode, zero swap, and aggregate memory/task limits is
# eligible for a mathematical terminal.  The probe requires every property;
# a host that rejects any of them falls back to exact-PGID containment, in
# which the worker refuses production and the decision layer refuses
# promotion (NO_VERDICT-only).
probe_unit="${scope_unit}-probe-$$"
if command -v systemd-run >/dev/null 2>&1 \
    && command -v systemctl >/dev/null 2>&1 \
    && [[ -r /sys/fs/cgroup/cgroup.controllers ]] \
    && systemctl --user show-environment >/dev/null 2>&1 \
    && timeout 10 systemd-run --user --scope --wait --collect --quiet \
         --unit "$probe_unit" --property=MemoryMax=274877906944 \
         --property=TasksMax=512 --property=RuntimeMaxSec=30 \
         --property=KillMode=control-group --property=MemorySwapMax=0 \
         true >/dev/null 2>&1; then
  containment_mode=systemd_scope
fi
printf '%s\n' "$containment_mode" > "$custody/containment_mode.txt"
printf '%s\n' "$scope_unit" > "$custody/systemd_scope_unit.txt"
export CONTAINMENT_MODE="$containment_mode"
export WORKER_SCOPE_UNIT="$scope_unit"

telemetry="$custody/telemetry.tsv"
printf 'utc\telapsed_s\tworker_pid\tworker_pgid\tcpu_pct\trss_kib\tcgroup_mem_bytes\tmem_avail_kib\tswap_total_kib\tswap_free_kib\tdisk_avail_kib\n' \
  > "$telemetry"
swap_violation=0
whole_timeout=0
systemd_final_fault=0
systemd_runtime_fault=0

if [[ "$containment_mode" == systemd_scope ]]; then
  systemd-run --user --scope --wait --collect --quiet --unit "$scope_unit" \
    --property=MemoryMax=274877906944 --property=TasksMax=512 \
    --property=RuntimeMaxSec=21600 --property=KillMode=control-group \
    --property=MemorySwapMax=0 \
    taskset -c "$CPU_ID" bash "$worker" \
    > "$custody/supervised_worker.stdout.txt" \
    2> "$custody/supervised_worker.stderr.txt" &
else
  setsid --wait taskset -c "$CPU_ID" bash "$worker" \
    > "$custody/supervised_worker.stdout.txt" \
    2> "$custody/supervised_worker.stderr.txt" &
fi
launcher_pid=$!
printf '%s\n' "$launcher_pid" > "$custody/containment_launcher.pid"
if launcher_start=$(python3 "$contract" pid-start --pid "$launcher_pid" \
    2> "$custody/containment_launcher_identity.stderr.txt"); then
  launcher_identity_gate=1
  printf '%s\n' "$launcher_start" \
    > "$custody/containment_launcher.starttime"
else
  launcher_start=0
fi

launcher_state_file="$custody/containment_launcher_state.json"
launcher_state_rc=2
poll_launcher_state() {
  if [[ "$launcher_identity_gate" != 1 ]]; then
    return 2
  fi
  python3 "$contract" wait-pid --pid "$launcher_pid" \
    --starttime "$launcher_start" --timeout 0 --output "$launcher_state_file" \
    > /dev/null 2>> "$custody/containment_launcher_identity.stderr.txt"
}

signal_launcher_exact() {
  local sig=$1
  [[ "$launcher_identity_gate" == 1 ]] || return 1
  python3 "$contract" signal-pid --pid "$launcher_pid" \
    --starttime "$launcher_start" --signal "$sig" \
    >> "$custody/containment_launcher_signals.txt" \
    2>> "$custody/containment_launcher_identity.stderr.txt"
}

identity="$custody/worker_identity.json"
for _ in $(seq 1 200); do
  [[ -s "$identity" ]] && break
  poll_launcher_state
  launcher_state_rc=$?
  [[ "$launcher_state_rc" == 1 ]] || break
  sleep 0.1
done
identity_gate=0
worker_pid=0
worker_pgid=0
worker_sid=0
worker_starttime=0
if [[ -s "$identity" ]]; then
  worker_pid=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["pid"])' "$identity")
  worker_pgid=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["pgid"])' "$identity")
  worker_sid=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["sid"])' "$identity")
  worker_starttime=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["starttime"])' "$identity")
  if python3 "$contract" validate-worker --identity "$identity" \
      --mode "$containment_mode" > "$custody/worker_identity_gate.txt" 2>&1; then
    identity_gate=1
  fi
fi

scope_cgroup=""
scope_membership_gate=0
if [[ "$containment_mode" == systemd_scope && "$identity_gate" == 1 ]]; then
  scope_cgroup=$(systemctl --user show --property=ControlGroup --value \
    "$scope_unit.scope" 2>/dev/null || true)
  printf '%s\n' "$scope_cgroup" > "$custody/systemd_scope_cgroup.txt"
  if [[ -n "$scope_cgroup" ]] \
      && grep -Fxq "0::$scope_cgroup" "/proc/$worker_pid/cgroup"; then
    scope_membership_gate=1
  fi
elif [[ "$containment_mode" == pgid && "$identity_gate" == 1 ]]; then
  scope_membership_gate=1
fi
printf '%s\n' "$scope_membership_gate" > "$custody/scope_membership_gate.txt"

# R3 (O-N3): verify ALL FIVE charged worker-scope properties by exact value
# (KillMode=control-group, RuntimeMaxUSec exactly 21600 s, MemoryMax,
# TasksMax, MemorySwapMax=0) through the one contract predicate the late
# decision authority replays; record the exact shown values for the archive.
if [[ "$containment_mode" == systemd_scope ]]; then
  systemd_runtime_fault=1
  if [[ "$identity_gate" == 1 ]] \
      && systemctl --user show "$scope_unit.scope" \
        --property=KillMode --property=RuntimeMaxUSec \
        --property=MemoryMax --property=TasksMax --property=MemorySwapMax \
        > "$custody/systemd_runtime_limits.txt" 2>&1 \
      && python3 "$contract" runtime-limits-record \
        --show-file "$custody/systemd_runtime_limits.txt" \
        --output "$custody/systemd_runtime_limits.json" \
        > "$custody/systemd_runtime_limits_record.stdout.txt" \
        2> "$custody/systemd_runtime_limits_record.stderr.txt"; then
    systemd_runtime_fault=0
  fi
else
  printf '{"verified": false, "killmode": "", "runtime_max_usec": "", "memory_max": "", "tasks_max": "", "memory_swap_max": ""}\n' \
    > "$custody/systemd_runtime_limits.json"
fi

terminate_primary() {
  local sig=$1
  if [[ "$containment_mode" == systemd_scope ]]; then
    systemctl --user kill --kill-whom=all --signal="$sig" \
      "$scope_unit.scope" >/dev/null 2>&1 || true
  elif [[ "$worker_pgid" -gt 1 && "$worker_pgid" != "$supervisor_pgid" ]]; then
    kill -"$sig" -- "-$worker_pgid" 2>/dev/null || true
  fi
}

terminate_tagged_early() {
  local early_pgid=$worker_pgid
  [[ "$containment_mode" == systemd_scope ]] && early_pgid=0
  python3 "$contract" cleanup --pgid "$early_pgid" --job-tag "$JOB_TAG" \
    --exclude-pid "$supervisor_pid" \
    --pgid-output "$custody/early_cleanup_pgid_census.json" \
    --tag-output "$custody/early_cleanup_job_tag_census.json" \
    > "$custody/early_cleanup.stdout.txt" \
    2> "$custody/early_cleanup.stderr.txt" || true
}

containment_preflight_failure=0
if [[ "$identity_gate" != 1 || "$scope_membership_gate" != 1 \
      || "$launcher_identity_gate" != 1 ]]; then
  containment_preflight_failure=1
  terminate_primary TERM
  sleep 1
  terminate_primary KILL
  terminate_tagged_early
fi
if [[ "$containment_mode" == systemd_scope \
      && "$systemd_runtime_fault" != 0 ]]; then
  containment_preflight_failure=1
  terminate_primary TERM
  sleep 1
  terminate_primary KILL
  terminate_tagged_early
fi

while true; do
  poll_launcher_state
  launcher_state_rc=$?
  if [[ "$launcher_state_rc" == 0 ]]; then
    break
  elif [[ "$launcher_state_rc" != 1 ]]; then
    containment_preflight_failure=1
    break
  fi
  now=$(date +%s)
  elapsed=$((now-start_epoch))
  cpu=$(ps -o pcpu= -g "$worker_pgid" 2>/dev/null | awk '{s+=$1} END {printf "%.1f",s+0}')
  rss=$(ps -o rss= -g "$worker_pgid" 2>/dev/null | awk '{s+=$1} END {print s+0}')
  cgroup_mem=NA
  if [[ "$containment_mode" == systemd_scope && -n "$scope_cgroup" \
        && -r "/sys/fs/cgroup$scope_cgroup/memory.current" ]]; then
    cgroup_mem=$(cat "/sys/fs/cgroup$scope_cgroup/memory.current" \
      2>/dev/null || printf 'NA')
  fi
  mem_avail=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
  swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
  swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
  disk_avail=$(df -Pk "$JOB_ROOT" | awk 'NR==2 {print $4}')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$elapsed" "$worker_pid" \
    "$worker_pgid" "$cpu" "$rss" "$cgroup_mem" "$mem_avail" "$swap_total" \
    "$swap_free" "$disk_avail" >> "$telemetry"
  if [[ "$swap_total" != 0 || "$swap_free" != 0 ]]; then
    swap_violation=1
    terminate_primary TERM
    terminate_tagged_early
    break
  fi
  if [[ "$elapsed" -ge 21600 ]]; then
    whole_timeout=1
    terminate_primary TERM
    terminate_tagged_early
    break
  fi
  sleep 10
done
if [[ "$swap_violation" != 0 || "$whole_timeout" != 0 \
      || "$containment_preflight_failure" != 0 ]]; then
  sleep 5
  terminate_primary KILL
  signal_launcher_exact KILL || true
fi
worker_rc=125
if [[ "$launcher_identity_gate" == 1 ]] \
    && python3 "$contract" wait-pid --pid "$launcher_pid" \
      --starttime "$launcher_start" --timeout 10 \
      --output "$custody/containment_launcher_reap.json" \
      > "$custody/containment_launcher_reap.stdout.txt" \
      2> "$custody/containment_launcher_reap.stderr.txt"; then
  # The exact PID is absent or a same-start-time zombie, so this shell-builtin
  # wait is provably immediate and only collects the already-terminated child.
  wait "$launcher_pid"
  worker_rc=$?
  launcher_reap_failure=0
else
  launcher_reap_failure=1
fi
printf '%s\n' "$worker_rc" > "$custody/supervisor_worker_returncode.txt"
printf '%s\n' "$swap_violation" > "$custody/supervisor_swap_violation.txt"
printf '%s\n' "$whole_timeout" > "$custody/supervisor_whole_timeout.txt"
printf '%s\n' "$containment_preflight_failure" \
  > "$custody/supervisor_containment_preflight_failure.txt"
printf '%s\n' "$launcher_reap_failure" \
  > "$custody/supervisor_launcher_reap_failure.txt"
printf '%s\n' "$systemd_runtime_fault" \
  > "$custody/supervisor_systemd_runtime_fault.txt"

# Kill the complete primary boundary on every exit, then remove any exact
# JOB_TAG descendant that somehow escaped it. PID start times and uid are
# revalidated by containment_contract.py before each signal.
terminate_primary TERM
sleep 1
terminate_primary KILL
cleanup_pgid=$worker_pgid
[[ "$containment_mode" == systemd_scope ]] && cleanup_pgid=0
cleanup_gate=0
if python3 "$contract" cleanup --pgid "$cleanup_pgid" --job-tag "$JOB_TAG" \
    --exclude-pid "$supervisor_pid" \
    --pgid-output "$custody/no_orphan_pgid_census.json" \
    --tag-output "$custody/no_orphan_job_tag_census.json" \
    > "$custody/containment_cleanup.stdout.txt" \
    2> "$custody/containment_cleanup.stderr.txt"; then
  cleanup_gate=1
fi

systemd_empty_gate=1
if [[ "$containment_mode" == systemd_scope ]]; then
  systemd_empty_gate=0
  systemd_show_rc=0
  systemctl --user show "$scope_unit.scope" \
    --property=LoadState --property=ActiveState --property=SubState \
    --property=Result > "$custody/systemd_scope_final_state.txt" 2>&1 \
    || systemd_show_rc=$?
  printf '%s\n' "$systemd_show_rc" \
    > "$custody/systemd_scope_final_state.rc"
  systemd_collected_gate=0
  if [[ "$systemd_show_rc" != 0 ]] \
      || grep -Fxq 'LoadState=not-found' \
        "$custody/systemd_scope_final_state.txt"; then
    systemd_collected_gate=1
  fi
  if [[ -n "$scope_cgroup" ]]; then
    cgroup_path="/sys/fs/cgroup$scope_cgroup"
    cgroup_procs="$cgroup_path/cgroup.procs"
    if [[ -r "$cgroup_procs" ]]; then
      cgroup_rc=0
      python3 "$contract" cgroup-census --path "$cgroup_procs" \
        --output "$custody/systemd_cgroup_procs_final.json" \
        > "$custody/systemd_cgroup_census.stdout.txt" \
        2> "$custody/systemd_cgroup_census.stderr.txt" || cgroup_rc=$?
      if [[ "$cgroup_rc" == 0 && "$systemd_show_rc" == 0 ]] \
          && grep -Fxq 'ActiveState=inactive' \
            "$custody/systemd_scope_final_state.txt" \
          && grep -Fxq 'Result=success' \
            "$custody/systemd_scope_final_state.txt"; then
        systemd_empty_gate=1
      else
        systemd_final_fault=1
      fi
    elif [[ ! -e "$cgroup_path" && "$launcher_reap_failure" == 0 \
            && "$scope_membership_gate" == 1 \
            && "$systemd_collected_gate" == 1 ]]; then
      # A cgroup directory cannot be removed while populated.  Together with
      # prior exact membership and bounded launcher reap, failed lookup records
      # the explicit --collect path rather than treating a missing file as
      # silently empty.
      printf '[]\n' > "$custody/systemd_cgroup_procs_final.json"
      printf '%s\n' SYSTEMD_SCOPE_COLLECTED_AFTER_BOUND_LAUNCHER_REAP=1 \
        > "$custody/systemd_scope_collected.marker"
      systemd_empty_gate=1
    else
      systemd_final_fault=1
    fi
  else
    systemd_final_fault=1
  fi
fi
printf '%s\n' "$systemd_final_fault" \
  > "$custody/supervisor_systemd_final_fault.txt"
if [[ "$cleanup_gate" == 1 && "$systemd_empty_gate" == 1 \
      && "$scope_membership_gate" == 1 && "$launcher_reap_failure" == 0 \
      && "$containment_preflight_failure" == 0 \
      && "$systemd_final_fault" == 0 \
      && "$systemd_runtime_fault" == 0 ]]; then
  printf '%s\n' CONTAINMENT_EMPTY_PASS=1 \
    > "$custody/CONTAINMENT_EMPTY.marker"
fi

ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/supervisor_processes_final.txt"
awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  > "$custody/memory_supervisor_final.txt"
swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/SUPERVISOR_ENDED_UTC.txt"

# R3 (O-N4): bank the sticky fault-latch state INSIDE the archive before the
# freeze.  The late decision authority requires this record from the archive
# bytes and refuses any fault regression against the live flags, so the
# archived latch state is load-bearing, not merely present.  Post-freeze
# sticky re-checks can only worsen the live flags (downgrade-only).
printf '{"schema":"triple02_closed_successor_r3_fault_latches_v1","job_tag":"%s","job_nonce":"%s","containment_mode":"%s","worker_rc":%s,"swap_violation":%s,"whole_timeout":%s,"containment_preflight_failure":%s,"launcher_reap_failure":%s,"systemd_final_fault":%s,"systemd_runtime_fault":%s}\n' \
  "$JOB_TAG" "$JOB_NONCE" "$containment_mode" "$worker_rc" \
  "$swap_violation" "$whole_timeout" "$containment_preflight_failure" \
  "$launcher_reap_failure" "$systemd_final_fault" "$systemd_runtime_fault" \
  > "$custody/FAULT_LATCHES_PRE_ARCHIVE.json"

# The archive contains only the classifier candidate, the decision record,
# and finalization evidence, never a promoted mathematical terminal.  Freeze
# the exact regular-file AND directory sets, independently replay hashes and
# censuses, then replay a fresh extraction that the late decision authority
# will read; the live tree is never the decision source.
manifest="$custody/TERMINAL_MANIFEST.sha256"
dirs_relative="custody/TERMINAL_DIRS.list"
manifest_includes=(source source_archive.tar.gz LEASE.json LEASE.sha256
                   launch_preflight_copy.sh work custody)
archive_members=(source source_archive.tar.gz LEASE.json LEASE.sha256
                 launch_preflight_copy.sh work custody)
if [[ -d "$JOB_ROOT/output" ]]; then
  manifest_includes+=(output)
  archive_members+=(output)
fi
manifest_cli=()
for include in "${manifest_includes[@]}"; do
  manifest_cli+=(--include "$include")
done
manifest_generator_rc=125
manifest_replay_rc=125
archive_replay_rc=125
python3 "$contract" manifest-build --root "$JOB_ROOT" \
  --manifest "$manifest" --dirs-relative "$dirs_relative" \
  "${manifest_cli[@]}" \
  > "$JOB_ROOT/.terminal_manifest_generator.stdout.txt" \
  2> "$JOB_ROOT/.terminal_manifest_generator.stderr.txt"
manifest_generator_rc=$?
if [[ "$manifest_generator_rc" == 0 ]]; then
  python3 "$contract" manifest-verify --root "$JOB_ROOT" \
    --manifest "$manifest" --dirs-relative "$dirs_relative" \
    "${manifest_cli[@]}" \
    > "$JOB_ROOT/.terminal_manifest_replay.stdout.txt" \
    2> "$JOB_ROOT/.terminal_manifest_replay.stderr.txt"
  manifest_replay_rc=$?
  if [[ "$manifest_replay_rc" == 0 ]]; then
    (cd "$JOB_ROOT" && sha256sum -c \
      custody/TERMINAL_MANIFEST.sha256) \
      > "$JOB_ROOT/.terminal_manifest_sha256sum.stdout.txt" \
      2> "$JOB_ROOT/.terminal_manifest_sha256sum.stderr.txt"
    manifest_replay_rc=$?
  fi
fi
archive_ready=0
outer_archive_sha=""
terminal_archive="$JOB_ROOT/${JOB_TAG}.terminal.tar.gz"
archive_tmp="$terminal_archive.tmp.$$"
archive_replay_dir="$JOB_ROOT/.terminal_archive_replay.$$"
if [[ "$manifest_generator_rc" == 0 && "$manifest_replay_rc" == 0 ]] \
    && tar -czf "$archive_tmp" -C "$JOB_ROOT" "${archive_members[@]}" \
    && tar -tzf "$archive_tmp" \
      > "$JOB_ROOT/.terminal_archive_listing.txt" \
    && python3 "$contract" archive-extract-verify \
      --archive "$archive_tmp" --destination "$archive_replay_dir" \
      --manifest-relative custody/TERMINAL_MANIFEST.sha256 \
      --dirs-relative "$dirs_relative" \
      "${manifest_cli[@]}" \
      > "$JOB_ROOT/.terminal_archive_replay.stdout.txt" \
      2> "$JOB_ROOT/.terminal_archive_replay.stderr.txt" \
    && (cd "$archive_replay_dir" && sha256sum -c \
      custody/TERMINAL_MANIFEST.sha256) \
      > "$JOB_ROOT/.terminal_archive_sha256sum.stdout.txt" \
      2> "$JOB_ROOT/.terminal_archive_sha256sum.stderr.txt"; then
  archive_replay_rc=0
  # No-replace atomic installation: hard-link, then remove the temporary.
  if ln "$archive_tmp" "$terminal_archive" 2>/dev/null \
      && sha256sum "$terminal_archive" > "$terminal_archive.sha256" \
      && (cd "$JOB_ROOT" && sha256sum -c \
        "$(basename "$terminal_archive.sha256")") \
        > "$JOB_ROOT/.terminal_outer_sha256sum.stdout.txt" \
        2> "$JOB_ROOT/.terminal_outer_sha256sum.stderr.txt"; then
    archive_ready=1
    outer_archive_sha=$(awk '{print $1}' "$terminal_archive.sha256")
  fi
fi
rm -f "$archive_tmp"
if [[ "$archive_ready" != 1 ]]; then
  rm -f "$terminal_archive" "$terminal_archive.sha256"
fi

# Finalization itself is inside the whole-job and zero-swap contract.  These
# are sticky updates: a clean last reading can never erase an earlier fault.
final_elapsed=$(($(date +%s)-start_epoch))
if [[ "$final_elapsed" -ge 21600 ]]; then
  whole_timeout=1
fi
swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
if [[ "$swap_total" != 0 || "$swap_free" != 0 ]]; then
  swap_violation=1
fi
# R3 (O-N4): the post-freeze latch file binds the job tag and the charged
# archive digest and carries a content-address sidecar, so an auditor can
# authenticate it against the marker chain (marker -> archive digest ->
# these latches); the pre-freeze latch state is inside the archive itself.
printf 'job_tag=%s\nswap_violation=%s\nwhole_timeout=%s\ncontainment_preflight_failure=%s\nlauncher_reap_failure=%s\nsystemd_final_fault=%s\nsystemd_runtime_fault=%s\nmanifest_generator_rc=%s\nmanifest_replay_rc=%s\narchive_replay_rc=%s\narchive_ready=%s\ncontainment_mode=%s\nterminal_archive_sha256=%s\n' \
  "$JOB_TAG" \
  "$swap_violation" "$whole_timeout" "$containment_preflight_failure" \
  "$launcher_reap_failure" "$systemd_final_fault" "$systemd_runtime_fault" \
  "$manifest_generator_rc" "$manifest_replay_rc" "$archive_replay_rc" \
  "$archive_ready" "$containment_mode" "${outer_archive_sha:-NONE}" \
  > "$JOB_ROOT/FINALIZATION_LATCHES.txt"
printf '%s  FINALIZATION_LATCHES.txt\n' \
  "$(sha256sum "$JOB_ROOT/FINALIZATION_LATCHES.txt" | awk '{print $1}')" \
  > "$JOB_ROOT/FINALIZATION_LATCHES.sha256"

# C1 + R3 (O-B1): the late terminal authority authenticates the FROZEN
# ARCHIVE BYTES at decision time — it re-hashes $terminal_archive against
# the charged digest, re-runs the complete member/manifest/directory
# censuses from the archive bytes, requires the fresh extraction in
# $archive_replay_dir to be byte-identical member-for-member, and reads
# every decision input from the archive bytes in memory.  A same-uid edit,
# deletion, replacement, symlink, or archive/extraction mix-and-match after
# the freeze fails closed.  The live candidate file is never read here.
decision_tmp="$JOB_ROOT/.TERMINAL.marker.decision.$$"
terminal_args=(
  --live-lease "$lease_file"
  --job-tag "$JOB_TAG" --job-nonce "$JOB_NONCE"
  --source-archive-sha256 "$EXPECTED_SOURCE_ARCHIVE_SHA256"
  --containment-mode-file "$custody/containment_mode.txt"
  --worker-pid "$worker_pid" --worker-starttime "$worker_starttime"
  --supervisor-pid "$supervisor_pid"
  --supervisor-starttime "$supervisor_start"
  --worker-rc "$worker_rc" --swap-total "$swap_total"
  --swap-free "$swap_free"
  --swap-violation "$swap_violation" --whole-timeout "$whole_timeout"
  --containment-preflight-failure "$containment_preflight_failure"
  --launcher-reap-failure "$launcher_reap_failure"
  --systemd-final-fault "$systemd_final_fault"
  --systemd-runtime-fault "$systemd_runtime_fault"
  --scope-marker "$custody/SCOPE_FIREWALL.marker"
  --worker-gate "$custody/WORKER_FINAL_GATE.marker"
  --containment-marker "$custody/CONTAINMENT_EMPTY.marker"
  --pgid-census "$custody/no_orphan_pgid_census.json"
  --tag-census "$custody/no_orphan_job_tag_census.json"
  --archive-ready "$archive_ready"
  --manifest-generator-rc "$manifest_generator_rc"
  --manifest-replay-rc "$manifest_replay_rc"
  --archive-replay-rc "$archive_replay_rc" --output "$decision_tmp"
)
if [[ "$archive_ready" == 1 ]]; then
  terminal_args+=(--fresh-root "$archive_replay_dir"
                  --archive-sha256 "$outer_archive_sha"
                  --terminal-archive "$terminal_archive"
                  --manifest-relative custody/TERMINAL_MANIFEST.sha256
                  --dirs-relative "$dirs_relative"
                  "${manifest_cli[@]}")
fi
python3 "$contract" terminal "${terminal_args[@]}" \
  > "$JOB_ROOT/terminal_decision.stdout.txt" \
  2> "$JOB_ROOT/terminal_decision.stderr.txt"
decision_rc=$?
if [[ "$decision_rc" != 0 && "$decision_rc" != 3 ]]; then
  printf '%s\nTERMINAL_ARCHIVE_SHA256=NONE\nDECISION_RECORD_SHA256=NONE\n' \
    CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT > "$decision_tmp"
fi
if ! publish_no_replace "$decision_tmp"; then
  rm -f "$decision_tmp"
  exit 74
fi
rm -f "$decision_tmp"
case "$archive_replay_dir" in
  "$JOB_ROOT"/.terminal_archive_replay.*)
    rm -rf -- "$archive_replay_dir"
    ;;
esac
exit 0
