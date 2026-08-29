#!/usr/bin/env bash
set -Eeuo pipefail

job_dir=$1
worker_pid=""
registered_pid=""

cleanup() {
  cleanup_rc=$?
  if [[ -n "$worker_pid" && -f "$job_dir/records/GROUP.tsv" ]]; then
    python3 "$job_dir/source/runner/process_group_guard.py" stop \
      --registry "$job_dir/records/GROUP.tsv" --grace-seconds 30 \
      >>"$job_dir/records/TRAP_STOP.jsonl" 2>&1 || true
  fi
  return "$cleanup_rc"
}
trap cleanup EXIT HUP INT TERM

mkdir -p "$job_dir/output" "$job_dir/records"
find "$job_dir/source" -type f -print0 | sort -z | xargs -0 sha256sum \
  >"$job_dir/records/FROZEN_SOURCE.sha256"
source_manifest_sha=$(sha256sum "$job_dir/records/FROZEN_SOURCE.sha256" | awk '{print $1}')
chmod -R a-w "$job_dir/source"

setsid timeout --foreground --signal=TERM --kill-after=40s 7300s \
  env AWS_RUN_TAG="$(basename "$job_dir")" \
  "$job_dir/source/runner/job_worker.sh" "$job_dir" \
  >"$job_dir/records/launcher.stdout" \
  2>"$job_dir/records/launcher.stderr" &
worker_pid=$!
registered_pid=$worker_pid
sleep 0.2

read -r observed_pgid observed_sid observed_starttime < <(
  python3 - "$worker_pid" <<'PY'
import sys
from pathlib import Path
pid = int(sys.argv[1])
raw = Path(f"/proc/{pid}/stat").read_text()
tail = raw[raw.rfind(")") + 2:].split()
print(tail[2], tail[3], tail[19])
PY
)
[[ "$worker_pid" == "$observed_pgid" && "$worker_pid" == "$observed_sid" ]]
printf 'SECOND_ORDER\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "$worker_pid" "$observed_pgid" "$observed_sid" "$observed_starttime" \
  "$job_dir" "$source_manifest_sha" >"$job_dir/records/GROUP.tsv"
touch "$job_dir/records/REGISTERED"

set +e
python3 "$job_dir/source/runner/process_group_guard.py" monitor \
  --registry "$job_dir/records/GROUP.tsv" --grace-seconds 30 \
  >"$job_dir/records/MONITOR.jsonl" 2>"$job_dir/records/MONITOR.stderr"
monitor_rc=$?
wait "$worker_pid"
worker_rc=$?
set -e

printf '%s\n' "$monitor_rc" >"$job_dir/records/MONITOR_RC"
printf '%s\n' "$worker_rc" >"$job_dir/records/WORKER_RC"
python3 "$job_dir/source/runner/process_group_guard.py" snapshot \
  --registry "$job_dir/records/GROUP.tsv" \
  >"$job_dir/records/FINAL_CENSUS.json"
worker_pid=""
trap - EXIT HUP INT TERM

if [[ "$monitor_rc" -ne 0 && ! -f "$job_dir/output/TERMINAL" ]]; then
  printf '%s\n' NO_VERDICT_GUARD >"$job_dir/output/TERMINAL"
fi
if [[ ! -f "$job_dir/output/TERMINAL" ]]; then
  printf '%s\n' NO_VERDICT_NO_MARKER >"$job_dir/output/TERMINAL"
fi

find "$job_dir/output" -type f -print0 | sort -z | xargs -0 sha256sum \
  >"$job_dir/records/OUTPUTS.sha256"
find "$job_dir/output" "$job_dir/records" -type f \
  ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum \
  >"$job_dir/EVIDENCE.sha256"
chmod -R a-w "$job_dir/source" "$job_dir/output" "$job_dir/records" \
  "$job_dir/EVIDENCE.sha256"

printf 'JOB_DIR=%s\n' "$job_dir"
printf 'WORKER_PID=%s\n' "$registered_pid"
printf 'WORKER_RC=%s\n' "$worker_rc"
printf 'MONITOR_RC=%s\n' "$monitor_rc"
printf 'TERMINAL=%s\n' "$(tr -d '\n' <"$job_dir/output/TERMINAL")"
sha256sum "$job_dir/output/probe.stdout" "$job_dir/output/probe.stderr" \
  "$job_dir/output/probe.time" "$job_dir/output/SECOND_ORDER_CERTIFICATE.json" \
  "$job_dir/output/POSTCHECK.json" "$job_dir/output/TERMINAL" \
  "$job_dir/EVIDENCE.sha256" 2>/dev/null || true

