#!/usr/bin/env bash
set -euo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${CPU_ID:?}"

custody="$JOB_ROOT/custody"
mkdir -p "$custody"
umask 077
supervisor_pid=$$
supervisor_pgid=$(ps -o pgid= -p $$ | tr -d ' ')
supervisor_sid=$(ps -o sid= -p $$ | tr -d ' ')
supervisor_start=$(awk '{print $22}' "/proc/$$/stat")
printf '{"pid":%s,"pgid":%s,"sid":%s,"starttime":%s,"cpu":%s}\n' \
  "$supervisor_pid" "$supervisor_pgid" "$supervisor_sid" \
  "$supervisor_start" "$CPU_ID" > "$custody/supervisor_identity.json"

telemetry="$custody/telemetry.tsv"
printf 'utc\telapsed_s\tpgid\tcpu_pct\trss_kib\tmem_avail_kib\tswap_total_kib\tswap_free_kib\tdisk_avail_kib\n' > "$telemetry"
start_epoch=$(date +%s)
swap_violation=0
set +e
/usr/bin/time -v -o "$custody/overall.time" \
  timeout --signal=TERM --kill-after=30s 7200s \
  bash "$JOB_ROOT/source/jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/aws_job_worker.sh" &
worker_pid=$!
set -e
worker_start=$(awk '{print $22}' "/proc/$worker_pid/stat")
printf '{"pid":%s,"pgid":%s,"sid":%s,"starttime":%s}\n' \
  "$worker_pid" "$supervisor_pgid" "$supervisor_sid" "$worker_start" \
  > "$custody/worker_identity.json"
while kill -0 "$worker_pid" 2>/dev/null; do
  now=$(date +%s)
  cpu=$(ps -o pcpu= -g "$supervisor_pgid" | awk '{s+=$1} END {printf "%.1f",s+0}')
  rss=$(ps -o rss= -g "$supervisor_pgid" | awk '{s+=$1} END {print s+0}')
  mem_avail=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
  st=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
  sf=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
  disk=$(df -Pk "$JOB_ROOT" | awk 'NR==2 {print $4}')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$((now-start_epoch))" \
    "$supervisor_pgid" "$cpu" "$rss" "$mem_avail" "$st" "$sf" "$disk" \
    >> "$telemetry"
  if [[ "$st" != 0 || "$sf" != 0 ]]; then
    swap_violation=1
    kill -TERM "$worker_pid" 2>/dev/null || true
    break
  fi
  sleep 10
done
set +e
wait "$worker_pid"
worker_rc=$?
set -e
printf '%s\n' "$worker_rc" > "$custody/supervisor_worker_returncode.txt"
printf '%s\n' "$swap_violation" > "$custody/supervisor_swap_violation.txt"
ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/supervisor_processes_final.txt"
if [[ "$swap_violation" != 0 ]]; then
  printf '%s\n' INFRASTRUCTURE_FAILURE_SWAP_NO_VERDICT > "$JOB_ROOT/TERMINAL.marker"
elif [[ "$worker_rc" != 0 && ! -f "$JOB_ROOT/TERMINAL.marker" ]]; then
  if [[ "$worker_rc" == 124 || "$worker_rc" == 137 || "$worker_rc" == 143 ]]; then
    printf '%s\n' TIMEOUT_NO_VERDICT > "$JOB_ROOT/TERMINAL.marker"
  else
    printf '%s\n' ADAPTER_OR_SUPERVISOR_FAILURE_NO_VERDICT > "$JOB_ROOT/TERMINAL.marker"
  fi
fi
printf '%s\n' "$JOB_TAG" > "$custody/no_orphan_job_tag.txt"
pgrep -af "$JOB_TAG" > "$custody/no_orphan_census.txt" || true
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/SUPERVISOR_ENDED_UTC.txt"
(cd "$JOB_ROOT" && find source work output custody -type f \
  ! -name TERMINAL_MANIFEST.sha256 -print0 | sort -z | xargs -0 sha256sum) \
  > "$custody/TERMINAL_MANIFEST.sha256"
tar -czf "$JOB_ROOT/terminal_archive.tar.gz" -C "$JOB_ROOT" source work output custody
sha256sum "$JOB_ROOT/terminal_archive.tar.gz" > "$JOB_ROOT/terminal_archive.sha256"
exit 0
