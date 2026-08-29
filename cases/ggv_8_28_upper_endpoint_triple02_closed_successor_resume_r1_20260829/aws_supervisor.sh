#!/usr/bin/env bash
set -uo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${CPU_ID:?}"
: "${EXPECTED_SOURCE_ARCHIVE_SHA256:?}"

case_rel="cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r1_20260829"
case_dir="$JOB_ROOT/source/jc2/$case_rel"
worker="$case_dir/aws_job_worker.sh"
contract="$case_dir/containment_contract.py"
custody="$JOB_ROOT/custody"
terminal_marker="$JOB_ROOT/TERMINAL.marker"
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

publish_emergency_no_verdict() {
  if [[ ! -e "$terminal_marker" ]]; then
    local temporary="$JOB_ROOT/.TERMINAL.marker.emergency.$$"
    printf '%s\n' CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT > "$temporary" || true
    mv "$temporary" "$terminal_marker" 2>/dev/null || true
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

supervisor_pid=$$
supervisor_pgid=$(ps -o pgid= -p $$ | tr -d ' ')
supervisor_sid=$(ps -o sid= -p $$ | tr -d ' ')
supervisor_start=$(awk '{print $22}' "/proc/$$/stat")
printf '{"pid":%s,"pgid":%s,"sid":%s,"starttime":%s,"cpu":%s}\n' \
  "$supervisor_pid" "$supervisor_pgid" "$supervisor_sid" \
  "$supervisor_start" "$CPU_ID" > "$custody/supervisor_identity.json"
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/SUPERVISOR_STARTED_UTC.txt"
start_epoch=$(date +%s)

swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
[[ "$swap_total" == 0 && "$swap_free" == 0 ]] || exit 73

# Prefer a verifiable transient user scope. The exact-PGID fallback is used
# only when the host has no usable delegated user systemd manager.
probe_unit="${scope_unit}-probe-$$"
if command -v systemd-run >/dev/null 2>&1 \
    && command -v systemctl >/dev/null 2>&1 \
    && [[ -r /sys/fs/cgroup/cgroup.controllers ]] \
    && systemctl --user show-environment >/dev/null 2>&1 \
    && timeout 10 systemd-run --user --scope --wait --collect --quiet \
         --unit "$probe_unit" --property=MemoryMax=274877906944 \
         --property=TasksMax=512 true >/dev/null 2>&1; then
  containment_mode=systemd_scope
fi
printf '%s\n' "$containment_mode" > "$custody/containment_mode.txt"
printf '%s\n' "$scope_unit" > "$custody/systemd_scope_unit.txt"
export CONTAINMENT_MODE="$containment_mode"

telemetry="$custody/telemetry.tsv"
printf 'utc\telapsed_s\tworker_pid\tworker_pgid\tcpu_pct\trss_kib\tmem_avail_kib\tswap_total_kib\tswap_free_kib\tdisk_avail_kib\n' \
  > "$telemetry"
swap_violation=0
whole_timeout=0
systemd_final_fault=0

if [[ "$containment_mode" == systemd_scope ]]; then
  systemd-run --user --scope --wait --collect --quiet --unit "$scope_unit" \
    --property=MemoryMax=274877906944 --property=TasksMax=512 \
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
if [[ -s "$identity" ]]; then
  worker_pid=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["pid"])' "$identity")
  worker_pgid=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["pgid"])' "$identity")
  worker_sid=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["sid"])' "$identity")
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
  mem_avail=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
  swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
  swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
  disk_avail=$(df -Pk "$JOB_ROOT" | awk 'NR==2 {print $4}')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$elapsed" "$worker_pid" \
    "$worker_pgid" "$cpu" "$rss" "$mem_avail" "$swap_total" \
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
      && "$systemd_final_fault" == 0 ]]; then
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

# The archive contains only the classifier candidate and finalization evidence,
# never a promoted mathematical terminal.  Freeze the exact regular-file set,
# independently replay both hashes and census, then replay a fresh extraction
# before the one atomic public terminal promotion.
manifest="$custody/TERMINAL_MANIFEST.sha256"
manifest_includes=(source source_archive.tar.gz work custody)
archive_members=(source source_archive.tar.gz work custody)
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
  --manifest "$manifest" "${manifest_cli[@]}" \
  > "$JOB_ROOT/.terminal_manifest_generator.stdout.txt" \
  2> "$JOB_ROOT/.terminal_manifest_generator.stderr.txt"
manifest_generator_rc=$?
if [[ "$manifest_generator_rc" == 0 ]]; then
  python3 "$contract" manifest-verify --root "$JOB_ROOT" \
    --manifest "$manifest" "${manifest_cli[@]}" \
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
      "${manifest_cli[@]}" \
      > "$JOB_ROOT/.terminal_archive_replay.stdout.txt" \
      2> "$JOB_ROOT/.terminal_archive_replay.stderr.txt" \
    && (cd "$archive_replay_dir" && sha256sum -c \
      custody/TERMINAL_MANIFEST.sha256) \
      > "$JOB_ROOT/.terminal_archive_sha256sum.stdout.txt" \
      2> "$JOB_ROOT/.terminal_archive_sha256sum.stderr.txt"; then
  archive_replay_rc=0
  if mv "$archive_tmp" "$terminal_archive" \
      && sha256sum "$terminal_archive" > "$terminal_archive.sha256" \
      && (cd "$JOB_ROOT" && sha256sum -c \
        "$(basename "$terminal_archive.sha256")") \
        > "$JOB_ROOT/.terminal_outer_sha256sum.stdout.txt" \
        2> "$JOB_ROOT/.terminal_outer_sha256sum.stderr.txt"; then
    archive_ready=1
  fi
fi
rm -f "$archive_tmp"
case "$archive_replay_dir" in
  "$JOB_ROOT"/.terminal_archive_replay.*)
    rm -rf -- "$archive_replay_dir"
    ;;
  *) archive_ready=0 ;;
esac
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
printf 'swap_violation=%s\nwhole_timeout=%s\ncontainment_preflight_failure=%s\nlauncher_reap_failure=%s\nsystemd_final_fault=%s\nmanifest_generator_rc=%s\nmanifest_replay_rc=%s\narchive_replay_rc=%s\narchive_ready=%s\n' \
  "$swap_violation" "$whole_timeout" "$containment_preflight_failure" \
  "$launcher_reap_failure" "$systemd_final_fault" \
  "$manifest_generator_rc" "$manifest_replay_rc" "$archive_replay_rc" \
  "$archive_ready" > "$JOB_ROOT/FINALIZATION_LATCHES.txt"

decision_tmp="$JOB_ROOT/.TERMINAL.marker.decision.$$"
python3 "$contract" terminal \
  --candidate "$custody/CANDIDATE_MATHEMATICAL_VERDICT.txt" \
  --worker-rc "$worker_rc" --swap-total "$swap_total" --swap-free "$swap_free" \
  --swap-violation "$swap_violation" --whole-timeout "$whole_timeout" \
  --containment-preflight-failure "$containment_preflight_failure" \
  --launcher-reap-failure "$launcher_reap_failure" \
  --systemd-final-fault "$systemd_final_fault" \
  --scope-marker "$custody/SCOPE_FIREWALL.marker" \
  --worker-gate "$custody/WORKER_FINAL_GATE.marker" \
  --containment-marker "$custody/CONTAINMENT_EMPTY.marker" \
  --pgid-census "$custody/no_orphan_pgid_census.json" \
  --tag-census "$custody/no_orphan_job_tag_census.json" \
  --archive-ready "$archive_ready" \
  --manifest-generator-rc "$manifest_generator_rc" \
  --manifest-replay-rc "$manifest_replay_rc" \
  --archive-replay-rc "$archive_replay_rc" --output "$decision_tmp" \
  > "$JOB_ROOT/terminal_decision.stdout.txt" \
  2> "$JOB_ROOT/terminal_decision.stderr.txt"
decision_rc=$?
if [[ "$decision_rc" != 0 && "$decision_rc" != 3 ]]; then
  printf '%s\n' CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT > "$decision_tmp"
fi
if ! mv "$decision_tmp" "$terminal_marker"; then
  exit 74
fi
exit 0
