#!/usr/bin/env bash
set -euo pipefail

run_dir=${1:?usage: stop_aws.sh /absolute/path/to/exact/run/namespace}
if [[ "$run_dir" != /* || ! -d "$run_dir" || ! -f "$run_dir/runner.identity" ]]; then
  echo "STOP: pass an existing absolute tail3 run namespace" >&2
  exit 2
fi
if [[ "$(basename "$run_dir")" != tail3_* ]]; then
  echo "STOP: namespace basename is not tail3_*" >&2
  exit 2
fi
target_dir=$(cd "$(dirname "$0")" && pwd -P)
# shellcheck source=process_group_guard.sh
source "$target_dir/process_group_guard.sh"

declare -a pgids=()
if [[ -f "$run_dir/children.pgids" ]]; then
  while read -r pid pgid label job; do
    [[ "$pid" =~ ^[0-9]+$ && "$pgid" =~ ^[0-9]+$ && "$pid" == "$pgid" ]] || {
      echo "REFUSE: malformed child identity" >&2
      exit 3
    }
    [[ "$job" == "$run_dir/"* ]] || {
      echo "REFUSE: child job escapes namespace" >&2
      exit 3
    }
    pgids+=("$pgid")
  done < "$run_dir/children.pgids"
fi

for pgid in "${pgids[@]:-}"; do
  [[ -n "$pgid" ]] || continue
  echo "TERM validated PGID $pgid"
  tail3_signal_group "$run_dir" "$pgid" TERM || true
done
for _ in $(seq 1 60); do
  live=0
  for pgid in "${pgids[@]:-}"; do
    [[ -n "$pgid" ]] || continue
    if tail3_validate_group "$run_dir" "$pgid" 2>/dev/null; then live=1; fi
  done
  (( live == 0 )) && break
  sleep 1
done
for pgid in "${pgids[@]:-}"; do
  [[ -n "$pgid" ]] || continue
  if tail3_validate_group "$run_dir" "$pgid" 2>/dev/null; then
    echo "KILL validated PGID $pgid"
    tail3_signal_group "$run_dir" "$pgid" KILL
  fi
done

read -r runner_pid runner_starttime < "$run_dir/runner.identity"
if [[ "$runner_pid" =~ ^[0-9]+$ && "$runner_starttime" =~ ^[0-9]+$ \
      && -r "/proc/$runner_pid/stat" ]]; then
  observed_starttime=$(awk '{print $22}' "/proc/$runner_pid/stat")
  observed_args=$(ps -o args= -p "$runner_pid" || true)
  if [[ "$observed_starttime" == "$runner_starttime" \
        && "$observed_args" == *"run_aws.sh"* ]]; then
    echo "TERM validated runner $runner_pid"
    kill -TERM "$runner_pid" 2>/dev/null || true
  else
    echo "REFUSE: runner PID identity no longer matches" >&2
    exit 4
  fi
fi
touch "$run_dir/STOP_REQUESTED"

