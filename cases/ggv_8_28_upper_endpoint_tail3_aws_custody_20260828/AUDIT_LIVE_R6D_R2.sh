#!/usr/bin/env bash
# Read-only live topology/resource audit for the preregistered tail3 R2 lane.

set -euo pipefail

launch_root=/home/ubuntu/jobs/ggv_8_28_tail3_core_mod_r6d_r2_20260828T050159Z
source_root=/home/ubuntu/jobs/ggv_8_28_tail3_source_r1_20260828T050159Z
case_dir=$source_root/cases/ggv_8_28_upper_endpoint_tail3_desk_20260828
expected_launcher=383943
memory_floor_kib=$((150 * 1024 * 1024))
disk_floor_bytes=$((50 * 1024 * 1024 * 1024))

mapfile -t run_dirs < <(find "$launch_root/runs" -mindepth 1 -maxdepth 1 \
  -type d -name 'tail3_*' -print)
[[ "${#run_dirs[@]}" == 1 ]]
run_dir=${run_dirs[0]}
[[ "$run_dir" == \
  "$launch_root/runs/tail3_core_mod_r6d_call_20260828T051902Z_383943_cutoff3_core_mod_r6d_r2" ]]

read -r launcher_pid launcher_start launcher_sid launcher_pgid \
  < "$launch_root/launcher.identity"
read -r runner_pid runner_start < "$run_dir/runner.identity"
[[ "$launcher_pid" == "$expected_launcher" \
   && "$runner_pid" == "$expected_launcher" \
   && "$runner_start" == "$launcher_start" \
   && "$launcher_sid" == "$expected_launcher" \
   && "$launcher_pgid" == "$expected_launcher" ]]
observed_start=$(awk '{print $22}' "/proc/$runner_pid/stat")
read -r _ runner_sid runner_pgid runner_state runner_args \
  < <(ps -o pid=,sid=,pgid=,state=,args= -p "$runner_pid")
[[ "$observed_start" == "$runner_start" \
   && "$runner_sid" == "$runner_pid" \
   && "$runner_pgid" == "$runner_pid" \
   && "$runner_state" != Z* \
   && "$runner_args" == *"$case_dir/TARGETS/run_aws.sh"* ]]

mapfile -t children < "$run_dir/children.pgids"
[[ "${#children[@]}" == 6 ]]
declare -a singular_pids=()
aggregate_group_rss=0
for chart in 0 1 2 3 4 5; do
  read -r pid pgid label job <<< "${children[$chart]}"
  [[ "$pid" =~ ^[0-9]+$ && "$pid" == "$pgid" \
     && "$label" == "chart$chart" \
     && "$job" == "$run_dir/chart$chart.sing" ]]
  members=0
  singulars=0
  group_rss=0
  while read -r member _ppid sid observed_pgid state comm rss args; do
    [[ "$observed_pgid" == "$pgid" ]] || continue
    members=$((members + 1))
    [[ "$sid" == "$pgid" && "$state" != Z* \
       && "$args" == *"$run_dir/"* ]]
    group_rss=$((group_rss + rss))
    if [[ "$comm" == Singular ]]; then
      singulars=$((singulars + 1))
      singular_pids+=("$member")
      [[ "$args" == "Singular -q $job" ]]
    fi
  done < <(ps -eo pid=,ppid=,sid=,pgid=,state=,comm=,rss=,args=)
  [[ "$members" -ge 4 && "$singulars" == 1 && "$group_rss" -gt 0 ]]
  aggregate_group_rss=$((aggregate_group_rss + group_rss))
  echo "CHART=$chart WORKER_PID_PGID_SID=$pid SINGULAR_PID=${singular_pids[-1]} GROUP_RSS_KIB=$group_rss"
done
[[ "${#singular_pids[@]}" == 6 ]]

mapfile -t global_singular < <(ps -C Singular -o pid=,sid=,pgid=,args=)
[[ "${#global_singular[@]}" == 6 ]]
for row in "${global_singular[@]}"; do
  [[ "$row" == *"$run_dir/"* ]]
done

available_kib=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
swap_total_kib=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free_kib=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
swap_used_kib=$((swap_total_kib - swap_free_kib))
disk_available_bytes=$(df -PB1 "$run_dir" | awk 'NR==2 {print $4}')
(( available_kib >= memory_floor_kib ))
(( disk_available_bytes >= disk_floor_bytes ))
(( swap_total_kib == 0 && swap_used_kib == 0 ))

telemetry=$(tail -n 1 "$run_dir/TELEMETRY.tsv")
IFS=$'\t' read -r telemetry_utc telemetry_mem telemetry_swap \
  telemetry_disk telemetry_groups <<< "$telemetry"
[[ "$telemetry_utc" != utc && "$telemetry_groups" != none ]]
(( telemetry_mem >= memory_floor_kib \
   && telemetry_disk >= disk_floor_bytes \
   && telemetry_swap == 0 ))
for pgid in 384230 384248 384266 384284 384302 384320; do
  [[ "$telemetry_groups" == *"$pgid:"* ]]
done

grep -q '^PREFLIGHT=PASS$' "$launch_root/launcher.stdout"
grep -q '^PROCESS_GROUP_REGRESSION_RSS_INCLUDED=PASS$' \
  "$launch_root/launcher.stdout"
grep -q '^PROCESS_GROUP_REGRESSION_TERM_CLEARED=PASS$' \
  "$launch_root/launcher.stdout"
if find "$run_dir" -maxdepth 1 -type f \
    \( -name 'RUN_*' -o -name 'WORKERS_*' -o \
       -name 'RESOURCE_GUARD_STOP' \) -print | grep .; then
  echo 'STOP: unexpected terminal/resource marker during live audit' >&2
  exit 50
fi

echo "AUDIT_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "RUN_DIR=$run_dir"
echo "SINGULAR_COUNT=${#singular_pids[@]}"
echo "AGGREGATE_VALIDATED_GROUP_RSS_KIB=$aggregate_group_rss"
echo "MEM_AVAILABLE_KIB=$available_kib"
echo "DISK_AVAILABLE_BYTES=$disk_available_bytes"
echo "SWAP_TOTAL_KIB=$swap_total_kib"
echo "SWAP_USED_KIB=$swap_used_kib"
echo "LAST_TELEMETRY=$telemetry"
echo 'R2_LIVE_TOPOLOGY_RESOURCE_AUDIT=PASS'
