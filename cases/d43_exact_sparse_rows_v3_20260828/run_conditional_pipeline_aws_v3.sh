#!/usr/bin/env bash
# Supervisor for the D43 v3 exact a00pp conditional pipeline.
#
# The external hash-pinned launcher starts this script INSIDE the whole-job
# containment boundary (systemd user scope with MemoryMax/MemorySwapMax=0/
# TasksMax, or a setsid session in the pgid fallback), holding the exclusive
# kernel run lease.  Everything below - supervisor, sticky monitor, both side
# workers, pair assembly, the conditional emitter, and finalization - runs in
# that one boundary under one JOB_TAG.
#
# The mathematical flow is revision 2 unchanged: independent f and g side
# builds under per-side caps, matched-pair custody with same-host distinct-PID
# overlap, the literal collapsed-D21 band-20 gate, and one-process emission of
# all 19 shards plus the 184-row merge.  Emission only; solve=false.
#
# Exactly one authoritative terminal object, TERMINAL.json, is published by
# atomic rename as the last successful action after every payload, custody,
# and archive gate.  No positive VERDICT, COMPLETE stage, receipt, or marker
# exists earlier; every failure path leaves a single NO_VERDICT authority.
set -uo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${RUN_NONCE:?}"
: "${AWS_RUN_TAG:?}"
: "${AWS_EXPECTED_HOSTNAME:?}"
: "${CONTAINMENT_MODE:?}"

source_root="$JOB_ROOT/source/jc2"
case_dir="$source_root/cases/d43_exact_sparse_rows_v3_20260828"
manifest="$case_dir/PIPELINE_MANIFEST_V3.json"
contract="$case_dir/job_contract_v3.py"
producer="$case_dir/selected_rows_v3.py"
preflight_py="$case_dir/aws_preflight_v3.py"
lease="$JOB_ROOT/RUN_LEASE.json"
records="$JOB_ROOT/records"
output="$JOB_ROOT/output"
custody="$JOB_ROOT/custody"
sides="$output/sides"
violations="$custody/violations"
terminal="$JOB_ROOT/TERMINAL.json"
terminal_archive="$JOB_ROOT/${JOB_TAG}.terminal.tar.gz"
umask 077

py() { python3 -B "$@"; }

# --- mandatory terminal inputs, fail-closed defaults -----------------------
preflight_rc=125
source_check_rc=125
f_rc=125
g_rc=125
pair_rc=125
emit_rc=125
candidate_rc=125
containment_identity_gate=0
monitor_started=0
monitor_stop_clean=0
swap_violation=1
whole_timeout=0
peer_cancelled=0
oom_kill_count=125
cleanup_gate=0
cgroup_final_gate=0
manifest_generator_rc=125
manifest_replay_rc=125
archive_replay_rc=125
archive_ready=0
swap_total=1
swap_free=1
monitor_pid=0
monitor_start=0
stage_pid_f=0
stage_start_f=0
stage_pid_g=0
stage_start_g=0
stage_pid_one=0
stage_start_one=0
cgroup_dir=""
start_epoch=$(date +%s)

atomic_marker() {
  local path=$1 value=$2 temporary
  temporary="${path}.tmp.$$"
  printf '%s\n' "$value" >"$temporary"
  mv "$temporary" "$path"
}

read_swap() {
  swap_total=$(awk '/^SwapTotal:/{print $2}' /proc/meminfo)
  swap_free=$(awk '/^SwapFree:/{print $2}' /proc/meminfo)
}

zero_swap() {
  read_swap
  [[ "$swap_total" == 0 && "$swap_free" == 0 ]]
}

kill_stage_tree() {
  local pid=$1 starttime=$2 label=$3
  [[ "$pid" -gt 1 && "$starttime" -gt 0 ]] || return 0
  py "$contract" kill-tree --pid "$pid" --starttime "$starttime" \
    --census-output "$custody/kill_tree_${label}.json" \
    >>"$custody/kill_tree.log" 2>&1 || true
}

emergency_containment() {
  kill_stage_tree "$stage_pid_f" "$stage_start_f" emergency_f
  kill_stage_tree "$stage_pid_g" "$stage_start_g" emergency_g
  kill_stage_tree "$stage_pid_one" "$stage_start_one" emergency_one
  kill_stage_tree "$monitor_pid" "$monitor_start" emergency_monitor
  local cleanup_pgid=0
  [[ "$CONTAINMENT_MODE" == setsid_pgid ]] && cleanup_pgid=$$
  py "$contract" cleanup --pgid "$cleanup_pgid" --job-tag "$JOB_TAG" \
    --exclude-pid $$ \
    --pgid-output "$custody/emergency_pgid_census.json" \
    --tag-output "$custody/emergency_tag_census.json" \
    >"$custody/emergency_cleanup.stdout.txt" \
    2>"$custody/emergency_cleanup.stderr.txt" || true
}

publish_emergency_no_verdict() {
  local reason=$1
  [[ -e "$terminal" ]] && return 0
  local temporary="$JOB_ROOT/.TERMINAL.json.emergency.$$"
  printf '{\n "schema": "jc2.d43.a00pp-exact-source-rows.v3.terminal",\n "status": "NO_VERDICT_%s",\n "terminal_authority": true,\n "positive": false,\n "job_tag": "%s",\n "utc": "%s"\n}\n' \
    "$reason" "$JOB_TAG" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >"$temporary" || return 0
  mv "$temporary" "$terminal" 2>/dev/null || true
}

on_exit() {
  local rc=$?
  trap - EXIT
  if [[ ! -e "$terminal" ]]; then
    emergency_containment
    publish_emergency_no_verdict SUPERVISOR_EMERGENCY_EXIT
  fi
  exit "$rc"
}
trap on_exit EXIT
trap 'exit 143' TERM
trap 'exit 130' INT
trap 'exit 129' HUP

# --- guards before any output mutation -------------------------------------
[[ "$(uname -s)" == Linux ]] || exit 90
[[ "$JOB_TAG" == "$(basename "$JOB_ROOT")" ]] || exit 91
[[ "$JOB_TAG" == "$AWS_RUN_TAG" ]] || exit 92
[[ -f "$contract" && -f "$producer" && -f "$preflight_py" ]] || exit 93
[[ -s "$records/REGISTERED.json" ]] || exit 94
py "$contract" verify-fresh-namespace --job-root "$JOB_ROOT" \
  >"$records/launch_fresh_namespace.txt" 2>&1 || exit 95
py "$contract" verify-lease --lease "$lease" --job-root "$JOB_ROOT" \
  --job-tag "$JOB_TAG" --expect-nonce "$RUN_NONCE" \
  >"$records/launch_lease_verify.txt" 2>&1 || exit 96
zero_swap || exit 97

mkdir -p "$records" "$output" "$sides" "$custody" "$violations"
atomic_marker "$output/CURRENT_STAGE" RUNNING_CONTAINMENT_IDENTITY

read_contract() {
  py - "$manifest" "$1" <<'EOF'
import json, sys
print(json.load(open(sys.argv[1]))["resource_contract"][sys.argv[2]])
EOF
}
whole_job_timeout=$(read_contract whole_job_timeout_seconds) || exit 98
whole_job_memory_max=$(read_contract whole_job_memory_max_bytes) || exit 98
whole_job_pids_max=$(read_contract whole_job_pids_max) || exit 98
monitor_interval=$(read_contract monitor_interval_seconds) || exit 98
cpu_f=$(read_contract cpu_f) || exit 98
cpu_g=$(read_contract cpu_g) || exit 98
side_as=$(read_contract side_address_space_bytes) || exit 98
emit_as=$(read_contract conditional_emitter_address_space_bytes) || exit 98
fsize=$(read_contract file_size_bytes) || exit 98
stage_timeout=$(read_contract timeout_seconds) || exit 98
deadline_epoch=$((start_epoch + whole_job_timeout))

# --- containment identity ---------------------------------------------------
if [[ "$CONTAINMENT_MODE" == systemd_scope ]]; then
  cgroup_rel=$(awk -F: '$1=="0"{print $3}' /proc/self/cgroup)
  cgroup_dir="/sys/fs/cgroup${cgroup_rel}"
  observed_swap_max=$(cat "$cgroup_dir/memory.swap.max" 2>/dev/null || echo MISSING)
  observed_memory_max=$(cat "$cgroup_dir/memory.max" 2>/dev/null || echo MISSING)
  observed_pids_max=$(cat "$cgroup_dir/pids.max" 2>/dev/null || echo MISSING)
  if [[ "$observed_swap_max" == 0 \
        && "$observed_memory_max" == "$whole_job_memory_max" \
        && "$observed_pids_max" == "$whole_job_pids_max" ]]; then
    containment_identity_gate=1
  fi
elif [[ "$CONTAINMENT_MODE" == setsid_pgid ]]; then
  observed_swap_max=NOT_APPLICABLE
  observed_memory_max=NOT_APPLICABLE
  observed_pids_max=NOT_APPLICABLE
  supervisor_sid=$(ps -o sid= -p $$ | tr -d ' ')
  supervisor_pgid=$(ps -o pgid= -p $$ | tr -d ' ')
  if [[ "$supervisor_sid" == "$$" && "$supervisor_pgid" == "$$" ]]; then
    containment_identity_gate=1
  fi
fi
printf '{"mode":"%s","cgroup_dir":"%s","memory_swap_max":"%s","memory_max":"%s","pids_max":"%s","gate":%s,"supervisor_pid":%s}\n' \
  "$CONTAINMENT_MODE" "$cgroup_dir" "$observed_swap_max" \
  "$observed_memory_max" "$observed_pids_max" \
  "$containment_identity_gate" "$$" \
  >"$custody/containment_identity.json"

# --- sticky continuous monitor ----------------------------------------------
if [[ "$containment_identity_gate" == 1 ]]; then
  monitor_args=(monitor --interval "$monitor_interval" \
    --deadline-epoch "$deadline_epoch" \
    --memory-max-bytes "$whole_job_memory_max" \
    --pids-max "$whole_job_pids_max" \
    --telemetry "$custody/telemetry.tsv" \
    --heartbeat "$custody/monitor.heartbeat.json" \
    --peak-output "$custody/monitor.peak.json" \
    --violations-dir "$violations" \
    --watch-ppid $$)
  if [[ "$CONTAINMENT_MODE" == systemd_scope ]]; then
    monitor_args+=(--cgroup-dir "$cgroup_dir" --kill-on-parent-death cgroup)
  else
    monitor_args+=(--pgid $$ --kill-on-parent-death pgid)
  fi
  py "$contract" "${monitor_args[@]}" \
    >"$custody/monitor.stdout.txt" 2>"$custody/monitor.stderr.txt" &
  monitor_pid=$!
  if monitor_start=$(py "$contract" pid-start --pid "$monitor_pid" \
      2>"$custody/monitor_identity.stderr.txt"); then
    monitor_started=1
    printf '{"pid":%s,"starttime":%s}\n' "$monitor_pid" "$monitor_start" \
      >"$custody/monitor_identity.json"
  else
    monitor_start=0
  fi
fi

violations_nonempty() {
  [[ -d "$violations" ]] && [[ -n "$(ls -A "$violations" 2>/dev/null)" ]]
}

heartbeat_fresh() {
  py - "$custody/monitor.heartbeat.json" "$monitor_interval" <<'EOF'
import json, sys, time
try:
    beat = json.load(open(sys.argv[1]))
    fresh = time.time() - float(beat["epoch"]) <= 3 * float(sys.argv[2]) + 10
except Exception:
    fresh = False
raise SystemExit(0 if fresh else 1)
EOF
}

monitor_healthy() {
  [[ "$monitor_started" == 1 ]] || return 1
  kill -0 "$monitor_pid" 2>/dev/null || return 1
  heartbeat_fresh || return 1
  return 0
}

run_capped() {
  local name=$1 cpu=$2 address_space=$3 timeout_seconds=$4
  shift 4
  /usr/bin/time -v -o "$output/${name}.time" \
    timeout --foreground --signal=TERM --kill-after=60s "$timeout_seconds" \
    prlimit --as="$address_space" --fsize="$fsize" \
    taskset --cpu-list "$cpu" nice -n 10 \
    env PYTHONDONTWRITEBYTECODE=1 PYTHONOPTIMIZE= \
    "$@" >"$output/${name}.stdout" 2>"$output/${name}.stderr"
  local rc=$?
  atomic_marker "$output/${name}.rc" "$rc"
  return "$rc"
}

# Poll a single backgrounded stage while enforcing sticky monitor latches.
# Sets poll_rc: the stage rc, or 98 on a latch-forced cancellation.
poll_stage() {
  local pid=$1 starttime=$2 label=$3
  while :; do
    if ! kill -0 "$pid" 2>/dev/null; then
      wait "$pid"
      poll_rc=$?
      return 0
    fi
    if violations_nonempty || ! monitor_healthy; then
      kill_stage_tree "$pid" "$starttime" "latch_${label}"
      wait "$pid" 2>/dev/null
      poll_rc=98
      return 0
    fi
    sleep 2
  done
}

stage_failed=0
fail_reason=NONE

if [[ "$containment_identity_gate" == 1 && "$monitor_started" == 1 ]]; then
  # --- preflight ------------------------------------------------------------
  atomic_marker "$output/CURRENT_STAGE" RUNNING_PREFLIGHT
  run_capped PREFLIGHT "$cpu_f" 68719476736 3600 \
    python3 -B "$preflight_py" \
    --manifest "$manifest" --run-dir "$JOB_ROOT" --lease "$lease" \
    --output "$records/PREFLIGHT.json" &
  stage_pid_one=$!
  stage_start_one=$(py "$contract" pid-start --pid "$stage_pid_one" \
    2>/dev/null || echo 0)
  poll_stage "$stage_pid_one" "$stage_start_one" preflight
  preflight_rc=$poll_rc
  stage_pid_one=0
  if [[ "$preflight_rc" != 0 ]]; then
    stage_failed=1; fail_reason=PREFLIGHT
  fi

  # --- operational source drift check ---------------------------------------
  if [[ "$stage_failed" == 0 ]]; then
    atomic_marker "$output/CURRENT_STAGE" RUNNING_SOURCE_CHECK
    (cd "$source_root" && sha256sum -c \
      "cases/d43_exact_sparse_rows_v3_20260828/OPERATIONAL_SOURCE_V3.sha256") \
      >"$records/source_check.stdout" 2>"$records/source_check.stderr"
    source_check_rc=$?
    if [[ "$source_check_rc" != 0 ]]; then
      stage_failed=1; fail_reason=SOURCE_DRIFT
    fi
  fi

  # --- concurrent independent side builds with peer cancellation ------------
  if [[ "$stage_failed" == 0 ]]; then
    atomic_marker "$output/CURRENT_STAGE" RUNNING_BUILD_INDEPENDENT_F_G
    run_capped BUILD_F "$cpu_f" "$side_as" "$stage_timeout" \
      python3 -B "$producer" build-side \
      --manifest "$manifest" --preflight-receipt "$records/PREFLIGHT.json" \
      --lease "$lease" --side f --output "$sides/f.pkl" &
    stage_pid_f=$!
    stage_start_f=$(py "$contract" pid-start --pid "$stage_pid_f" \
      2>/dev/null || echo 0)
    run_capped BUILD_G "$cpu_g" "$side_as" "$stage_timeout" \
      python3 -B "$producer" build-side \
      --manifest "$manifest" --preflight-receipt "$records/PREFLIGHT.json" \
      --lease "$lease" --side g --output "$sides/g.pkl" &
    stage_pid_g=$!
    stage_start_g=$(py "$contract" pid-start --pid "$stage_pid_g" \
      2>/dev/null || echo 0)
    f_done=0; g_done=0
    while [[ "$f_done" == 0 || "$g_done" == 0 ]]; do
      if violations_nonempty || ! monitor_healthy; then
        [[ "$f_done" == 0 ]] && kill_stage_tree "$stage_pid_f" "$stage_start_f" latch_f
        [[ "$g_done" == 0 ]] && kill_stage_tree "$stage_pid_g" "$stage_start_g" latch_g
        [[ "$f_done" == 0 ]] && { wait "$stage_pid_f" 2>/dev/null; f_rc=98; f_done=1; }
        [[ "$g_done" == 0 ]] && { wait "$stage_pid_g" 2>/dev/null; g_rc=98; g_done=1; }
        break
      fi
      if [[ "$f_done" == 0 ]] && ! kill -0 "$stage_pid_f" 2>/dev/null; then
        wait "$stage_pid_f"; f_rc=$?; f_done=1
        if [[ "$f_rc" != 0 && "$g_done" == 0 ]]; then
          # First failure cancels and reaps the peer.
          peer_cancelled=1
          kill_stage_tree "$stage_pid_g" "$stage_start_g" peer_g
          wait "$stage_pid_g" 2>/dev/null; g_rc=99; g_done=1
        fi
      fi
      if [[ "$g_done" == 0 ]] && ! kill -0 "$stage_pid_g" 2>/dev/null; then
        wait "$stage_pid_g"; g_rc=$?; g_done=1
        if [[ "$g_rc" != 0 && "$f_done" == 0 ]]; then
          peer_cancelled=1
          kill_stage_tree "$stage_pid_f" "$stage_start_f" peer_f
          wait "$stage_pid_f" 2>/dev/null; f_rc=99; f_done=1
        fi
      fi
      sleep 2
    done
    stage_pid_f=0; stage_pid_g=0
    if [[ "$f_rc" != 0 || "$g_rc" != 0 ]]; then
      stage_failed=1; fail_reason=INDEPENDENT_SIDE_BUILD
    fi
  fi

  # --- matched pair ----------------------------------------------------------
  if [[ "$stage_failed" == 0 ]]; then
    atomic_marker "$output/CURRENT_STAGE" RUNNING_ASSEMBLE_MATCHED_PAIR
    run_capped ASSEMBLE_PAIR "$cpu_f" 274877906944 7200 \
      python3 -B "$producer" assemble-pair \
      --manifest "$manifest" --preflight-receipt "$records/PREFLIGHT.json" \
      --lease "$lease" \
      --f-receipt "$sides/f.pkl.receipt.json" \
      --g-receipt "$sides/g.pkl.receipt.json" \
      --output "$sides/PAIR.json" &
    stage_pid_one=$!
    stage_start_one=$(py "$contract" pid-start --pid "$stage_pid_one" \
      2>/dev/null || echo 0)
    poll_stage "$stage_pid_one" "$stage_start_one" pair
    pair_rc=$poll_rc
    stage_pid_one=0
    if [[ "$pair_rc" != 0 ]]; then
      stage_failed=1; fail_reason=PAIR_CUSTODY
    fi
  fi

  # --- conditional band-20 gate then all 184 rows in one process -------------
  if [[ "$stage_failed" == 0 ]]; then
    atomic_marker "$output/CURRENT_STAGE" RUNNING_CONDITIONAL_BAND20_THEN_ALL184
    run_capped CONDITIONAL_EMIT_ALL "$cpu_f" "$emit_as" "$stage_timeout" \
      python3 -B "$producer" conditional-emit-all \
      --manifest "$manifest" --preflight-receipt "$records/PREFLIGHT.json" \
      --lease "$lease" --pair "$sides/PAIR.json" --output-dir "$output" &
    stage_pid_one=$!
    stage_start_one=$(py "$contract" pid-start --pid "$stage_pid_one" \
      2>/dev/null || echo 0)
    poll_stage "$stage_pid_one" "$stage_start_one" emit
    emit_rc=$poll_rc
    stage_pid_one=0
    if [[ "$emit_rc" != 0 ]]; then
      stage_failed=1; fail_reason=COLLAPSED_D21_OR_ALL184
    fi
  fi

  # --- non-authoritative finalize candidate ----------------------------------
  if [[ "$stage_failed" == 0 ]]; then
    atomic_marker "$output/CURRENT_STAGE" RUNNING_FINALIZE_CANDIDATE
    run_capped FINALIZE_CANDIDATE "$cpu_f" 68719476736 3600 \
      python3 -B "$producer" finalize-candidate \
      --manifest "$manifest" --preflight-receipt "$records/PREFLIGHT.json" \
      --lease "$lease" --output-dir "$output" &
    stage_pid_one=$!
    stage_start_one=$(py "$contract" pid-start --pid "$stage_pid_one" \
      2>/dev/null || echo 0)
    poll_stage "$stage_pid_one" "$stage_start_one" candidate
    candidate_rc=$poll_rc
    stage_pid_one=0
    if [[ "$candidate_rc" != 0 ]]; then
      stage_failed=1; fail_reason=FINALIZE_CANDIDATE
    fi
  fi
else
  stage_failed=1
  fail_reason=CONTAINMENT_OR_MONITOR_START
fi

# --- monitor stop (must be alive and fresh until now on the success path) ---
atomic_marker "$output/CURRENT_STAGE" RUNNING_FINAL_CUSTODY
if [[ "$monitor_started" == 1 ]]; then
  if monitor_healthy; then
    py "$contract" signal-pid --pid "$monitor_pid" \
      --starttime "$monitor_start" --signal TERM \
      >>"$custody/monitor_stop.log" 2>&1 || true
    if py "$contract" wait-pid --pid "$monitor_pid" \
        --starttime "$monitor_start" --timeout 30 \
        --output "$custody/monitor_reap.json" \
        >>"$custody/monitor_stop.log" 2>&1; then
      wait "$monitor_pid" 2>/dev/null
      monitor_exit_rc=$?
      if [[ "$monitor_exit_rc" == 0 ]]; then
        monitor_stop_clean=1
      fi
    else
      kill_stage_tree "$monitor_pid" "$monitor_start" monitor_force
      wait "$monitor_pid" 2>/dev/null
    fi
  else
    # Monitor death or staleness is itself a latched violation.
    kill_stage_tree "$monitor_pid" "$monitor_start" monitor_dead
    wait "$monitor_pid" 2>/dev/null
  fi
fi
monitor_pid=0

# --- sticky latch summary ---------------------------------------------------
py "$contract" violations-census --dir "$violations" \
  --output "$custody/violations_census.json" \
  >"$custody/violations_census.stdout.txt" 2>&1
violations_census_rc=$?
read_swap
final_elapsed=$(($(date +%s) - start_epoch))
swap_violation=0
if [[ -e "$violations/v_HOST_SWAP_NONZERO.json" \
      || -e "$violations/v_CGROUP_SWAP_NONZERO.json" \
      || "$swap_total" != 0 || "$swap_free" != 0 ]]; then
  swap_violation=1
fi
whole_timeout=0
if [[ -e "$violations/v_WHOLE_TIMEOUT.json" \
      || "$final_elapsed" -ge "$whole_job_timeout" ]]; then
  whole_timeout=1
fi
oom_kill_count=0
if [[ "$CONTAINMENT_MODE" == systemd_scope && -n "$cgroup_dir" ]]; then
  cat "$cgroup_dir/memory.events" >"$custody/memory.events.final.txt" 2>/dev/null
  cat "$cgroup_dir/memory.peak" >"$custody/memory.peak.final.txt" 2>/dev/null
  cat "$cgroup_dir/pids.events" >"$custody/pids.events.final.txt" 2>/dev/null
  oom_kill_count=$(awk '$1=="oom_kill"{print $2}' \
    "$custody/memory.events.final.txt" 2>/dev/null || echo 125)
  [[ -n "$oom_kill_count" ]] || oom_kill_count=125
fi
if [[ -e "$violations/v_OOM_KILL_OBSERVED.json" && "$oom_kill_count" == 0 ]]; then
  oom_kill_count=125
fi
awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  >"$custody/meminfo.final.txt"
printf 'final_elapsed_s=%s\nstage_failed=%s\nfail_reason=%s\npeer_cancelled=%s\nviolations_census_rc=%s\n' \
  "$final_elapsed" "$stage_failed" "$fail_reason" "$peer_cancelled" \
  "$violations_census_rc" >"$custody/final_latches.txt"

# --- whole-boundary cleanup and orphan proof --------------------------------
cleanup_pgid=0
[[ "$CONTAINMENT_MODE" == setsid_pgid ]] && cleanup_pgid=$$
if py "$contract" cleanup --pgid "$cleanup_pgid" --job-tag "$JOB_TAG" \
    --exclude-pid $$ \
    --pgid-output "$custody/no_orphan_pgid_census.json" \
    --tag-output "$custody/no_orphan_tag_census.json" \
    >"$custody/final_cleanup.stdout.txt" \
    2>"$custody/final_cleanup.stderr.txt"; then
  cleanup_gate=1
fi
if [[ "$CONTAINMENT_MODE" == systemd_scope && -n "$cgroup_dir" ]]; then
  if py "$contract" cgroup-census --path "$cgroup_dir/cgroup.procs" \
      --allow-pid $$ --output "$custody/cgroup_final_census.json" \
      >"$custody/cgroup_final_census.stdout.txt" 2>&1; then
    cgroup_final_gate=1
  fi
else
  # In the pgid fallback the exact-PGID census above is the equivalent
  # fail-closed terminal input; there is no cgroup to read.
  printf '[]\n' >"$custody/cgroup_final_census.json"
  cgroup_final_gate=$cleanup_gate
fi

# --- deterministic immutable terminal archive with full replay --------------
terminal_manifest="$custody/TERMINAL_MANIFEST.sha256"
manifest_includes=(--include records --include output --include custody \
  --include RUN_LEASE.json)
py "$contract" manifest-build --root "$JOB_ROOT" \
  --manifest "$terminal_manifest" "${manifest_includes[@]}" \
  >"$JOB_ROOT/.finalize_manifest_build.txt" 2>&1
manifest_generator_rc=$?
if [[ "$manifest_generator_rc" == 0 ]]; then
  py "$contract" manifest-verify --root "$JOB_ROOT" \
    --manifest "$terminal_manifest" "${manifest_includes[@]}" \
    >"$JOB_ROOT/.finalize_manifest_verify.txt" 2>&1
  manifest_replay_rc=$?
  if [[ "$manifest_replay_rc" == 0 ]]; then
    (cd "$JOB_ROOT" && sha256sum -c custody/TERMINAL_MANIFEST.sha256) \
      >"$JOB_ROOT/.finalize_manifest_sha256sum.txt" 2>&1
    manifest_replay_rc=$?
  fi
fi
archive_tmp="$terminal_archive.tmp.$$"
archive_replay_dir="$JOB_ROOT/.terminal_archive_replay.$$"
if [[ "$manifest_generator_rc" == 0 && "$manifest_replay_rc" == 0 ]] \
    && py "$contract" archive-build --root "$JOB_ROOT" \
      --member-manifest "$terminal_manifest" \
      --manifest-member custody/TERMINAL_MANIFEST.sha256 \
      --output "$archive_tmp" \
      >"$JOB_ROOT/.finalize_archive_build.txt" 2>&1 \
    && py "$contract" archive-extract-verify --archive "$archive_tmp" \
      --destination "$archive_replay_dir" \
      --manifest-relative custody/TERMINAL_MANIFEST.sha256 \
      --include records --include output --include custody \
      --include RUN_LEASE.json \
      >"$JOB_ROOT/.finalize_archive_replay.txt" 2>&1 \
    && (cd "$archive_replay_dir" && sha256sum -c \
      custody/TERMINAL_MANIFEST.sha256) \
      >"$JOB_ROOT/.finalize_archive_sha256sum.txt" 2>&1; then
  archive_replay_rc=0
  if mv "$archive_tmp" "$terminal_archive" \
      && (cd "$JOB_ROOT" && sha256sum "$(basename "$terminal_archive")" \
        >"$terminal_archive.sha256") \
      && (cd "$JOB_ROOT" && sha256sum -c \
        "$(basename "$terminal_archive").sha256") \
        >"$JOB_ROOT/.finalize_outer_sha256sum.txt" 2>&1; then
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

# Sticky refresh: finalization itself is inside the swap/timeout contract.
read_swap
if [[ "$swap_total" != 0 || "$swap_free" != 0 ]]; then
  swap_violation=1
fi
final_elapsed=$(($(date +%s) - start_epoch))
if [[ "$final_elapsed" -ge "$whole_job_timeout" ]]; then
  whole_timeout=1
fi

# --- single authoritative terminal decision, atomic rename, exit ------------
decision_tmp="$JOB_ROOT/.TERMINAL.json.decision.$$"
py "$contract" terminal \
  --candidate "$output/FINALIZE_CANDIDATE.json" \
  --lease "$lease" --job-root "$JOB_ROOT" --job-tag "$JOB_TAG" \
  --preflight-rc "$preflight_rc" --source-check-rc "$source_check_rc" \
  --f-rc "$f_rc" --g-rc "$g_rc" --pair-rc "$pair_rc" --emit-rc "$emit_rc" \
  --candidate-rc "$candidate_rc" \
  --containment-identity-gate "$containment_identity_gate" \
  --monitor-started "$monitor_started" \
  --monitor-stop-clean "$monitor_stop_clean" \
  --monitor-violations "$custody/violations_census.json" \
  --swap-violation "$swap_violation" \
  --swap-total "$swap_total" --swap-free "$swap_free" \
  --whole-timeout "$whole_timeout" --peer-cancelled "$peer_cancelled" \
  --oom-kill-count "$oom_kill_count" --cleanup-gate "$cleanup_gate" \
  --pgid-census "$custody/no_orphan_pgid_census.json" \
  --tag-census "$custody/no_orphan_tag_census.json" \
  --cgroup-final-gate "$cgroup_final_gate" \
  --manifest-generator-rc "$manifest_generator_rc" \
  --manifest-replay-rc "$manifest_replay_rc" \
  --archive-replay-rc "$archive_replay_rc" \
  --archive-ready "$archive_ready" \
  --archive-sha-sidecar "$terminal_archive.sha256" \
  --output "$decision_tmp" \
  >"$JOB_ROOT/.terminal_decision.stdout.txt" \
  2>"$JOB_ROOT/.terminal_decision.stderr.txt"
decision_rc=$?
if [[ "$decision_rc" != 0 && "$decision_rc" != 3 ]]; then
  printf '{\n "schema": "jc2.d43.a00pp-exact-source-rows.v3.terminal",\n "status": "NO_VERDICT_TERMINAL_DECISION_FAILURE",\n "terminal_authority": true,\n "positive": false,\n "job_tag": "%s",\n "utc": "%s"\n}\n' \
    "$JOB_TAG" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >"$decision_tmp"
fi
[[ ! -e "$terminal" ]] || exit 75
mv "$decision_tmp" "$terminal" || exit 74
exit 0
