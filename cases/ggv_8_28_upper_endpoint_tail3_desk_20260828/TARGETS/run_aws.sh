#!/usr/bin/env bash
set -euo pipefail

mode=${1:?usage: run_aws.sh mod|exact root|core|full [tag] [all|0,1,...]}
scope=${2:?usage: run_aws.sh mod|exact root|core|full [tag] [all|0,1,...]}
user_tag=${3:-run}
chart_selection=${4-}
case "$mode" in mod|exact) ;; *) echo "invalid mode" >&2; exit 2;; esac
case "$scope" in root|core|full) ;; *) echo "invalid scope" >&2; exit 2;; esac
if [[ ! "$user_tag" =~ ^[A-Za-z0-9._-]+$ ]]; then
  echo "tag must contain only A-Za-z0-9._-" >&2
  exit 2
fi

declare -a selected_charts=()
if [[ "$scope" == root ]]; then
  if [[ -z "$chart_selection" ]]; then chart_selection=none; fi
  if [[ "$chart_selection" != none ]]; then
    echo "chart subsets are forbidden for the root diagnostic" >&2
    exit 2
  fi
else
  if [[ -z "$chart_selection" ]]; then
    echo "core/full runs require an explicit chart selection" >&2
    exit 2
  fi
  if [[ "$mode" == exact && "$chart_selection" == all ]]; then
    echo "exact core/full forbids all; use the host-pinned ordered pair" >&2
    exit 2
  fi
  if [[ "$chart_selection" == all ]]; then
    selected_charts=(0 1 2 3 4 5)
  elif [[ "$chart_selection" =~ ^[0-5](,[0-5])*$ ]]; then
    IFS=, read -r -a selected_charts <<< "$chart_selection"
    declare -A seen_charts=()
    for chart in "${selected_charts[@]}"; do
      if [[ -n "${seen_charts[$chart]:-}" ]]; then
        echo "duplicate chart in selection" >&2
        exit 2
      fi
      seen_charts[$chart]=1
    done
  else
    echo "chart selection must be all or a comma-separated subset of 0..5" >&2
    exit 2
  fi
fi

if [[ "$scope" == root ]]; then
  expected_host=r6d
  expected_instance_id=i-07eeaf8ba6f0bc419
elif [[ "$mode" == mod ]]; then
  if [[ "$chart_selection" != all ]]; then
    echo "modular endpoint recon requires explicit all on r6d" >&2
    exit 2
  fi
  expected_host=r6d
  expected_instance_id=i-07eeaf8ba6f0bc419
else
  case "$chart_selection" in
    0,1) expected_host=r6a; expected_instance_id=i-02cb2b4a379ffcc64 ;;
    2,3) expected_host=r6c; expected_instance_id=i-040b7a1c2ed72d4cc ;;
    4,5) expected_host=r6d; expected_instance_id=i-07eeaf8ba6f0bc419 ;;
    *)
      echo "exact endpoint run requires one frozen ordered pair: 0,1 / 2,3 / 4,5" >&2
      exit 2
      ;;
  esac
fi

target_dir=$(cd "$(dirname "$0")" && pwd -P)
case_dir=$(cd "$target_dir/.." && pwd -P)
# shellcheck source=process_group_guard.sh
source "$target_dir/process_group_guard.sh"
run_root=${TAIL3_RUN_ROOT:-$case_dir/AWS_RUNS}
utc=$(date -u +%Y%m%dT%H%M%SZ)
selection_slug=${chart_selection//,/}
namespace="tail3_${scope}_${mode}_${expected_host}_c${selection_slug}_${utc}_$$_${user_tag}"
run_dir="$run_root/$namespace"
mkdir -p "$run_root"
if ! mkdir "$run_dir"; then
  echo "STOP: namespace already exists: $run_dir" >&2
  exit 3
fi

if [[ "$mode" == mod ]]; then
  workers=6
  mem_gib=40
  file_gib=6
  wall_seconds=21600
  field=mod
  certify=()
else
  workers=2
  mem_gib=120
  file_gib=6
  wall_seconds=43200
  field=q
  certify=(--certify)
fi
if [[ "$scope" == root && "$workers" -gt 3 ]]; then workers=3; fi
if [[ "$scope" == root ]]; then
  total_jobs=3
  coverage_status=ROOT_DIAGNOSTIC_NO_ENDPOINT
  selected_chart_text=none
else
  total_jobs=${#selected_charts[@]}
  selected_chart_text=$(IFS=,; echo "${selected_charts[*]}")
  if (( total_jobs == 6 )); then
    coverage_status=COMPLETE_SIX_CHART_COVER
  else
    coverage_status=PARTIAL_NONPROMOTABLE_ALONE
  fi
fi
if (( workers > total_jobs )); then workers=$total_jobs; fi
batches=$(((total_jobs + workers - 1) / workers))
campaign_wall_seconds=$((batches * wall_seconds))
aggregate_mem_gib=$((workers * mem_gib))
aggregate_file_gib=$((total_jobs * file_gib))
memory_floor_gib=150
disk_floor_gib=50
required_mem_gib=$((aggregate_mem_gib + memory_floor_gib))
required_disk_gib=$((aggregate_file_gib + disk_floor_gib))

"$target_dir/preflight_aws.sh" "$required_mem_gib" "$required_disk_gib" \
  "$mode" "$scope" "$selected_chart_text" \
  | tee "$run_dir/PREFLIGHT.txt"
instance_id=$(awk -F= '$1=="INSTANCE_ID" {print $2}' "$run_dir/PREFLIGHT.txt")
if [[ "$instance_id" != "$expected_instance_id" ]]; then
  echo "STOP: preflight instance does not match registered runner host" >&2
  exit 38
fi
runner_starttime=$(awk '{print $22}' "/proc/$$/stat")
printf '%s %s\n' "$$" "$runner_starttime" > "$run_dir/runner.identity"
printf '%s\n' \
  "NAMESPACE=$namespace" "MODE=$mode" "SCOPE=$scope" \
  "HOST_ALIAS=$expected_host" "INSTANCE_ID=$instance_id" \
  "SELECTED_CHARTS=$selected_chart_text" \
  "COVERAGE_STATUS=$coverage_status" \
  "WORKERS=$workers" "TOTAL_JOBS=$total_jobs" "BATCHES=$batches" \
  "MEM_GIB_PER_WORKER=$mem_gib" "FILE_GIB_PER_WORKER=$file_gib" \
  "JOB_WALL_SECONDS=$wall_seconds" \
  "CAMPAIGN_WALL_SECONDS=$campaign_wall_seconds" \
  "AGGREGATE_MEM_GIB=$aggregate_mem_gib" \
  "MEMORY_FLOOR_GIB=$memory_floor_gib" \
  "CUMULATIVE_OUTPUT_RESERVATION_GIB=$aggregate_file_gib" \
  "DISK_FLOOR_GIB=$disk_floor_gib" > "$run_dir/METADATA.txt"
printf '%s\n' \
  "SOURCE_MANIFEST_SHA256=$(sha256sum "$case_dir/SOURCE.sha256" | awk '{print $1}')" \
  "EVIDENCE_MANIFEST_SHA256=$(sha256sum "$case_dir/EVIDENCE.sha256" | awk '{print $1}')" \
  "TARGET_JSON_SHA256=$(sha256sum "$target_dir/tail3_v_nonzero_d22_target.json" | awk '{print $1}')" \
  >> "$run_dir/METADATA.txt"

declare -a child_pids=()
declare -a child_pgids=()
disk_floor_bytes=$((disk_floor_gib * 1024 * 1024 * 1024))
memory_floor_kib=$((memory_floor_gib * 1024 * 1024))
jobs_launched=0
guard_pid=""
campaign_started=$(date +%s)
printf '%s\n' $'utc\tmem_available_kib\tswap_used_kib\tdisk_available_bytes\tpgid_rss_kib' \
  > "$run_dir/TELEMETRY.tsv"

terminate_children() {
  local pgid
  for pgid in "${child_pgids[@]:-}"; do
    [[ -n "$pgid" ]] || continue
    tail3_signal_group "$run_dir" "$pgid" TERM || true
  done
  for _ in $(seq 1 30); do
    local live=0
    for pgid in "${child_pgids[@]:-}"; do
      [[ -n "$pgid" ]] || continue
      if tail3_validate_group "$run_dir" "$pgid" 2>/dev/null; then live=1; fi
    done
    (( live == 0 )) && return
    sleep 1
  done
  for pgid in "${child_pgids[@]:-}"; do
    [[ -n "$pgid" ]] || continue
    tail3_signal_group "$run_dir" "$pgid" KILL || true
  done
}

stop_all() {
  if [[ "$guard_pid" =~ ^[0-9]+$ ]]; then
    kill -TERM "$guard_pid" 2>/dev/null || true
  fi
  terminate_children
}
trap 'stop_all; trap - EXIT; exit 130' INT TERM
trap stop_all EXIT

resource_guard() {
  while true; do
    local available_bytes available_kib swap_total swap_free swap_used now utc
    local pgid rss pgid_rss=none
    available_bytes=$(df -PB1 "$run_dir" | awk 'NR==2 {print $4}')
    available_kib=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
    swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
    swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
    swap_used=$((swap_total - swap_free))
    now=$(date +%s)
    utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    if [[ -f "$run_dir/children.pgids" ]]; then
      pgid_rss=""
      while read -r _pid pgid _label _job; do
        if tail3_validate_group "$run_dir" "$pgid" 2>/dev/null; then
          rss=$(ps -eo pgid=,rss= | awk -v wanted="$pgid" \
            '$1==wanted {sum+=$2} END {print sum+0}')
          pgid_rss+="${pgid}:${rss},"
        fi
      done < "$run_dir/children.pgids"
      [[ -n "$pgid_rss" ]] || pgid_rss=none
    fi
    printf '%s\t%s\t%s\t%s\t%s\n' "$utc" "$available_kib" \
      "$swap_used" "$available_bytes" "$pgid_rss" >> "$run_dir/TELEMETRY.tsv"
    if (( available_bytes < disk_floor_bytes )); then
      echo "STOP: live disk guard crossed ${disk_floor_gib}GiB floor" \
        | tee "$run_dir/RESOURCE_GUARD_STOP"
      kill -TERM "$$" 2>/dev/null || true
      return 30
    fi
    if (( available_kib < memory_floor_kib )); then
      echo "STOP: live memory guard crossed ${memory_floor_gib}GiB floor" \
        | tee "$run_dir/RESOURCE_GUARD_STOP"
      kill -TERM "$$" 2>/dev/null || true
      return 31
    fi
    if (( swap_total != 0 || swap_used != 0 )); then
      echo "STOP: swap configured/used during run" \
        | tee "$run_dir/RESOURCE_GUARD_STOP"
      kill -TERM "$$" 2>/dev/null || true
      return 32
    fi
    if (( now - campaign_started >= campaign_wall_seconds )); then
      echo "STOP: global campaign wall ${campaign_wall_seconds}s reached" \
        | tee "$run_dir/RESOURCE_GUARD_STOP"
      kill -TERM "$$" 2>/dev/null || true
      return 33
    fi
    sleep 30
  done
}
resource_guard &
guard_pid=$!

check_remaining_resources() {
  local remaining=$((total_jobs - jobs_launched))
  local available_bytes required_bytes available_kib swap_total swap_free
  local active slots required_next_kib
  available_bytes=$(df -PB1 "$run_dir" | awk 'NR==2 {print $4}')
  required_bytes=$(((disk_floor_gib + remaining * file_gib) * 1024 * 1024 * 1024))
  if (( available_bytes < required_bytes )); then
    echo "STOP: disk ${available_bytes}B cannot preserve ${remaining} remaining " \
         "outputs plus ${disk_floor_gib}GiB floor" >&2
    return 34
  fi
  available_kib=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
  active=${#child_pids[@]}
  slots=$((workers - active))
  required_next_kib=$(((memory_floor_gib + slots * mem_gib) * 1024 * 1024))
  if (( available_kib < required_next_kib )); then
    echo "STOP: insufficient memory before next batch" >&2
    return 35
  fi
  swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
  swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
  if (( swap_total != 0 || swap_total - swap_free != 0 )); then
    echo "STOP: swap gate failed before next launch" >&2
    return 36
  fi
}

launch_one() {
  local label=$1
  shift
  check_remaining_resources
  local job="$run_dir/$label.sing"
  python3 "$target_dir/render_singular.py" \
    --target "$target_dir/tail3_v_nonzero_d22_target.json" \
    --output "$job" --scope "$scope" --field "$field" "$@" "${certify[@]}"
  (cd "$run_dir"; sha256sum "$label.sing" > "$label.sing.sha256")
  jobs_launched=$((jobs_launched + 1))

  setsid bash "$target_dir/job_worker.sh" "$run_dir" "$label" "$job" \
    "$mem_gib" "$file_gib" "$wall_seconds" &
  local pid=$! pgid=""
  for _ in $(seq 1 20); do
    pgid=$(ps -o pgid= -p "$pid" 2>/dev/null | tr -d ' ' || true)
    [[ "$pgid" == "$pid" ]] && break
    if ! kill -0 "$pid" 2>/dev/null; then break; fi
    sleep 0.05
  done
  if [[ "$pgid" != "$pid" ]] || ! tail3_validate_group "$run_dir" "$pgid"; then
    kill -TERM "$pid" 2>/dev/null || true
    wait "$pid" 2>/dev/null || true
    echo "STOP: failed to establish validated session PGID for $label" >&2
    return 37
  fi
  child_pids+=("$pid")
  child_pgids+=("$pgid")
  printf '%s %s %s %s\n' "$pid" "$pgid" "$label" "$job" \
    >> "$run_dir/children.pgids"
}

run_batch() {
  local status=0 pid
  for pid in "${child_pids[@]}"; do wait "$pid" || status=1; done
  child_pids=()
  child_pgids=()
  return "$status"
}

status=0
if [[ "$scope" == root ]]; then
  branches=(q0_l0 q0_4b_minus_l qnonzero_simplified)
  batch_count=0
  for branch in "${branches[@]}"; do
    launch_one "root_${branch}" --branch "$branch" --order lp
    batch_count=$((batch_count + 1))
    if (( batch_count == workers )); then
      run_batch || status=1
      batch_count=0
    fi
  done
  if (( batch_count )); then run_batch || status=1; fi
else
  batch_count=0
  for chart in "${selected_charts[@]}"; do
    launch_one "chart${chart}" --chart "$chart" --order dp
    batch_count=$((batch_count + 1))
    if (( batch_count == workers )); then
      run_batch || status=1
      batch_count=0
    fi
  done
  if (( batch_count )); then run_batch || status=1; fi
fi

if [[ "$guard_pid" =~ ^[0-9]+$ ]]; then
  kill -TERM "$guard_pid" 2>/dev/null || true
  wait "$guard_pid" 2>/dev/null || true
fi
guard_pid=""
trap - INT TERM EXIT

write_evidence() {
  (
    cd "$run_dir"
    find . -maxdepth 1 -type f ! -name 'RUN_EVIDENCE.sha256*' -print0 \
      | sort -z | xargs -0 sha256sum
  ) > "$run_dir/RUN_EVIDENCE.sha256.tmp"
  mv "$run_dir/RUN_EVIDENCE.sha256.tmp" "$run_dir/RUN_EVIDENCE.sha256"
}

if (( status )); then
  touch "$run_dir/RUN_INCOMPLETE_OR_FAILED"
else
  touch "$run_dir/WORKERS_COMPLETED"
fi
write_evidence

if (( status == 0 )) && [[ "$mode" == exact && "$scope" != root ]]; then
  validation_out=$(mktemp /tmp/tail3-validation-out.XXXXXX)
  validation_err=$(mktemp /tmp/tail3-validation-err.XXXXXX)
  if python3 "$target_dir/validate_results.py" run "$run_dir" \
      --expected-charts "$selected_chart_text" --allow-precompletion \
      > "$validation_out" 2> "$validation_err"; then
    mv "$validation_out" "$run_dir/VALIDATION.json"
    mv "$validation_err" "$run_dir/VALIDATION.stderr"
    touch "$run_dir/RUN_COMPLETED"
  else
    mv "$validation_out" "$run_dir/VALIDATION_FAILED.stdout"
    mv "$validation_err" "$run_dir/VALIDATION_FAILED.stderr"
    touch "$run_dir/RUN_INCOMPLETE_OR_FAILED"
    status=1
  fi
elif (( status == 0 )); then
  touch "$run_dir/RUN_COMPLETED"
fi
write_evidence
echo "RUN_DIR=$run_dir"
exit "$status"
