#!/usr/bin/env bash
set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
mode=""
branches_encoded=""
expected_instance_id=""
namespace=""
run_root="/home/ubuntu/jobs"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode) mode=$2; shift 2 ;;
    --branches) branches_encoded=$2; shift 2 ;;
    --expected-instance-id) expected_instance_id=$2; shift 2 ;;
    --namespace) namespace=$2; shift 2 ;;
    --run-root) run_root=$2; shift 2 ;;
    *) echo "unknown argument: $1" >&2; exit 64 ;;
  esac
done

[[ "$mode" == "modular" || "$mode" == "exact-unit" ]]
[[ -n "$branches_encoded" && -n "$expected_instance_id" && -n "$namespace" ]]
[[ "$namespace" =~ ^jc2-sign-[0-9]{8}T[0-9]{6}Z-[A-Za-z0-9_.-]+$ ]]
run_root=$(realpath "$run_root")
run_dir="$run_root/$namespace"
[[ ! -e "$run_dir" ]]
mkdir -p "$run_dir"

python3 "$here/preflight.py" --aws \
  --mode "$mode" --branches "$branches_encoded" \
  --expected-instance-id "$expected_instance_id" \
  --run-root "$run_root" --output "$run_dir/PREFLIGHT.json"

if [[ "$branches_encoded" == "all" ]]; then
  branches=("+---" "+--+" "+-+-" "+-++" "++--" "++-+" "+++-" "++++" "J0")
else
  IFS=',' read -r -a branches <<< "$branches_encoded"
fi

target="$here/sign_branch_elimination_target.json"
target_sha=$(sha256sum "$target" | awk '{print $1}')
[[ "$target_sha" == "3ba44de18e8ce15f9675734319d4dee2cee8cc795b796292a0d40838a6bda072" ]]

as_bytes=$((16 * 1024 * 1024 * 1024))
fsize_bytes=$((2 * 1024 * 1024 * 1024))
if [[ "$mode" == "modular" ]]; then
  wall_seconds=1800
  cpu_seconds=1800
  field="mod"
  certify=()
else
  wall_seconds=14400
  cpu_seconds=14400
  field="q"
  certify=(--certify)
fi

registry="$run_dir/groups.tsv"
: > "$registry"
printf '%s\n' "$target_sha  sign_branch_elimination_target.json" > "$run_dir/TARGET.sha256"

safe_label() {
  local value=$1
  value=${value//+/p}
  value=${value//-/m}
  printf '%s' "$value"
}

check_disk_batch() {
  local active_count=$1
  python3 - "$run_dir" "$active_count" <<'PY'
import shutil, sys
available = shutil.disk_usage(sys.argv[1]).free
required = (50 + 2 * int(sys.argv[2])) * 1024 ** 3
assert available >= required, (available, required)
print(f"DISK_BATCH_GATE=PASS available={available} required={required}")
PY
}

total=${#branches[@]}
batch_start=0
batch_index=0
while (( batch_start < total )); do
  remaining=$((total - batch_start))
  batch_count=$((remaining < 4 ? remaining : 4))
  check_disk_batch "$batch_count" | tee -a "$run_dir/BATCH_GATES.log"
  batch_registry="$run_dir/groups.batch${batch_index}.tsv"
  : > "$batch_registry"
  pids=()
  labels=()
  for ((offset=0; offset<batch_count; offset++)); do
    branch=${branches[$((batch_start + offset))]}
    safe=$(safe_label "$branch")
    label="${mode}.${safe}"
    job="$run_dir/$label.sing"
    log="$run_dir/$label.log"
    gate="$run_dir/$label.registered"
    python3 "$here/render_singular.py" --target "$target" \
      --branch "$branch" --field "$field" "${certify[@]}" --output "$job"
    (cd "$run_dir" && sha256sum "$label.sing" > "$label.sing.sha256")
    /usr/bin/setsid "$here/job_worker.sh" \
      "$run_dir" "$label" "$wall_seconds" "$as_bytes" "$fsize_bytes" \
      "$cpu_seconds" "$job" "$gate" > "$log" 2>&1 &
    pid=$!
    pgid=$(ps -o pgid= -p "$pid" | tr -d ' ')
    [[ "$pgid" == "$pid" ]]
    starttime=$(python3 - "$pid" <<'PY'
from pathlib import Path
import sys
text=Path(f"/proc/{sys.argv[1]}/stat").read_text()
parts=text[text.rfind(")")+2:].split()
print(parts[19])
PY
)
    job_sha=$(sha256sum "$job" | awk '{print $1}')
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$label" "$pid" "$pgid" "$starttime" "$run_dir" "$job_sha" \
      >> "$batch_registry"
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$label" "$pid" "$pgid" "$starttime" "$run_dir" "$job_sha" \
      >> "$registry"
    touch "$gate"
    pids+=("$pid")
    labels+=("$label")
  done

  python3 "$here/process_group_guard.py" snapshot --registry "$batch_registry" \
    >> "$run_dir/TELEMETRY.batch${batch_index}.jsonl"
  python3 "$here/process_group_guard.py" monitor --registry "$batch_registry" \
    --interval-seconds 30 --mem-floor-gib 150 --disk-floor-gib 50 \
    --grace-seconds 30 >> "$run_dir/TELEMETRY.batch${batch_index}.jsonl" 2>&1 &
  monitor_pid=$!

  batch_failed=0
  for index in "${!pids[@]}"; do
    pid=${pids[$index]}
    label=${labels[$index]}
    if wait "$pid"; then
      rc=0
    else
      rc=$?
      batch_failed=1
    fi
    printf '%s\n' "$rc" > "$run_dir/$label.rc"
    (cd "$run_dir" && sha256sum "$label.log" > "$label.log.sha256")
  done
  if wait "$monitor_pid"; then
    monitor_rc=0
  else
    monitor_rc=$?
    batch_failed=1
  fi
  printf '%s\n' "$monitor_rc" > "$run_dir/TELEMETRY.batch${batch_index}.rc"
  if (( batch_failed != 0 )); then
    python3 "$here/process_group_guard.py" stop --registry "$batch_registry" \
      --grace-seconds 30 || true
    echo "batch $batch_index failed; artifacts preserved at $run_dir" >&2
    exit 8
  fi
  batch_start=$((batch_start + batch_count))
  batch_index=$((batch_index + 1))
done

python3 "$here/validate_results.py" --run-dir "$run_dir" \
  --mode "$mode" --branches "$branches_encoded" \
  --expected-instance-id "$expected_instance_id" \
  --output "$run_dir/VALIDATION.json"
(cd "$run_dir" && sha256sum -- *.sha256 *.json *.jsonl *.log *.rc *.sing \
  > ARTIFACTS.sha256)
echo "RUN_COMPLETE=$run_dir"
