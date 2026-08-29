#!/usr/bin/env bash
set -euo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${LANE:?}"
: "${EXPECTED_INSTANCE_ID:?}"
: "${EXPECTED_HOSTNAME:?}"
: "${CPU_ID:?}"
: "${EXPECTED_PREREG_SHA:?}"

source_root="$JOB_ROOT/source/jc2"
task_rel="cases/sigray_rootaware_aws_recensus_r1_20260828"
task_root="$source_root/$task_rel"
custody="$JOB_ROOT/custody"
output="$JOB_ROOT/output"
mkdir -p "$custody"
umask 077

exec > >(tee -a "$custody/worker.stdout.txt") \
     2> >(tee -a "$custody/worker.stderr.txt" >&2)

printf '%s\n' "$JOB_TAG" > "$custody/JOB_TAG.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/STARTED_UTC.txt"
uname -a > "$custody/uname.txt"
hostname > "$custody/hostname.txt"
cat /sys/class/dmi/id/sys_vendor > "$custody/sys_vendor.txt"
[[ "$(uname -s)" == Linux ]]
[[ "$(cat /sys/class/dmi/id/sys_vendor)" == "Amazon EC2" ]]
[[ "$(hostname)" == "$EXPECTED_HOSTNAME" ]]
[[ "$(basename "$JOB_ROOT")" == "$JOB_TAG" ]]

token=$(curl -fsS --connect-timeout 2 -X PUT \
  -H 'X-aws-ec2-metadata-token-ttl-seconds: 300' \
  http://169.254.169.254/latest/api/token)
instance_id=$(curl -fsS --connect-timeout 2 \
  -H "X-aws-ec2-metadata-token: $token" \
  http://169.254.169.254/latest/meta-data/instance-id)
instance_type=$(curl -fsS --connect-timeout 2 \
  -H "X-aws-ec2-metadata-token: $token" \
  http://169.254.169.254/latest/meta-data/instance-type)
[[ "$instance_id" == "$EXPECTED_INSTANCE_ID" ]]
printf '%s\n' "$instance_id" > "$custody/instance_id.txt"
printf '%s\n' "$instance_type" > "$custody/instance_type.txt"

awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  > "$custody/memory_preflight.txt"
swap_total=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
[[ "$swap_total" == 0 && "$swap_free" == 0 ]]
df -Pk "$JOB_ROOT" > "$custody/disk_preflight.txt"
ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/processes_preflight.txt"

actual_prereg=$(sha256sum "$task_root/PREREGISTRATION.md" | awk '{print $1}')
[[ "$actual_prereg" == "$EXPECTED_PREREG_SHA" ]]
(cd "$source_root" && sha256sum -c "$task_rel/SOURCE_MANIFEST.sha256") \
  > "$custody/source_manifest_check.txt"

export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export PYTHONPYCACHEPREFIX="$JOB_ROOT/work/pycache"
mkdir -p "$JOB_ROOT/work"
python3 -m py_compile \
  "$source_root/cases/sheet6_campaign.py" \
  "$source_root/cases/h3_check.py" \
  "$source_root/cases/hiii_compose.py" \
  "$source_root/cases/twopole_check.py" \
  "$source_root/cases/monodromy_td.py" \
  "$source_root/cases/sigray_rootaware_smoke.py" \
  "$task_root/run_lane.py" "$task_root/root_menu_probe.py" \
  "$task_root/invariant_inventory.py" "$task_root/invariant_compare.py"
python3 -u "$source_root/cases/sigray_rootaware_smoke.py" \
  > "$custody/smoke.stdout.txt" 2> "$custody/smoke.stderr.txt"
grep -F 'ROOT-AWARE SMOKE PASS: 8 checks' "$custody/smoke.stdout.txt" >/dev/null

supervisor_pid=$$
supervisor_pgid=$(ps -o pgid= -p $$ | tr -d ' ')
supervisor_sid=$(ps -o sid= -p $$ | tr -d ' ')
supervisor_start=$(awk '{print $22}' "/proc/$$/stat")
printf '{"pid":%s,"pgid":%s,"sid":%s,"starttime":%s}\n' \
  "$supervisor_pid" "$supervisor_pgid" "$supervisor_sid" "$supervisor_start" \
  > "$custody/supervisor_identity.json"

ulimit -f 16777216
ulimit -v 67108864
set +e
setsid /usr/bin/time -v -o "$custody/time.txt" \
  timeout --signal=TERM --kill-after=20s 7200s \
  taskset -c "$CPU_ID" python3 -u "$task_root/run_lane.py" \
    --lane "$LANE" --root "$source_root" --output "$output" \
  > "$custody/lane.stdout.txt" 2> "$custody/lane.stderr.txt" &
solver_pid=$!
set -e
solver_pgid=$(ps -o pgid= -p "$solver_pid" | tr -d ' ')
solver_sid=$(ps -o sid= -p "$solver_pid" | tr -d ' ')
solver_start=$(awk '{print $22}' "/proc/$solver_pid/stat")
printf '{"pid":%s,"pgid":%s,"sid":%s,"starttime":%s,"cpu":%s}\n' \
  "$solver_pid" "$solver_pgid" "$solver_sid" "$solver_start" "$CPU_ID" \
  > "$custody/solver_identity.json"

telemetry="$custody/telemetry.tsv"
printf 'utc\telapsed_s\tpid\tpgid\tcpu_pct\trss_kib\tmem_avail_kib\tswap_total_kib\tswap_free_kib\tdisk_avail_kib\n' > "$telemetry"
start_epoch=$(date +%s)
swap_violation=0
while kill -0 "$solver_pid" 2>/dev/null; do
  now=$(date +%s)
  cpu=$(ps -o pcpu= -g "$solver_pgid" | awk '{s+=$1} END {printf "%.1f", s+0}')
  rss=$(ps -o rss= -g "$solver_pgid" | awk '{s+=$1} END {print s+0}')
  mem_avail=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
  st=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
  sf=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
  disk=$(df -Pk "$JOB_ROOT" | awk 'NR==2 {print $4}')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$((now-start_epoch))" "$solver_pid" \
    "$solver_pgid" "$cpu" "$rss" "$mem_avail" "$st" "$sf" "$disk" \
    >> "$telemetry"
  if [[ "$st" != 0 || "$sf" != 0 ]]; then
    swap_violation=1
    kill -TERM -- "-$solver_pgid" 2>/dev/null || true
    break
  fi
  sleep 10
done

set +e
wait "$solver_pid"
lane_rc=$?
set -e
printf '%s\n' "$lane_rc" > "$custody/lane_returncode.txt"
printf '%s\n' "$swap_violation" > "$custody/swap_violation.txt"
awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  > "$custody/memory_final.txt"
ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/processes_final.txt"

if [[ "$swap_violation" != 0 ]]; then
  classification="INFRASTRUCTURE_FAILURE_SWAP_NO_VERDICT"
elif [[ "$lane_rc" == 0 ]]; then
  classification="RUN_COMPLETE_SCOPE_AS_OUTPUT_SUMMARY"
elif [[ "$lane_rc" == 124 || "$lane_rc" == 137 || "$lane_rc" == 143 ]]; then
  classification="TIMEOUT_NO_VERDICT"
else
  classification="ADAPTER_OR_STAGE_FAILURE_NO_VERDICT"
fi
printf '%s\n' "$classification" > "$custody/TERMINAL_CLASSIFICATION.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/ENDED_UTC.txt"
(cd "$JOB_ROOT" && find source output custody -type f \
  ! -name TERMINAL_MANIFEST.sha256 -print0 | sort -z | \
  xargs -0 sha256sum) > "$custody/TERMINAL_MANIFEST.sha256"
tar -czf "$JOB_ROOT/terminal_archive.tar.gz" -C "$JOB_ROOT" source output custody
sha256sum "$JOB_ROOT/terminal_archive.tar.gz" > "$JOB_ROOT/terminal_archive.sha256"
printf '%s\n' "$classification" > "$JOB_ROOT/TERMINAL.marker"
exit 0
