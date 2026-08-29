#!/usr/bin/env bash
set -euo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${COMPONENT:?}"
: "${EXPECTED_INSTANCE_ID:?}"
: "${EXPECTED_HOSTNAME:?}"
: "${EXPECTED_PREREG_SHA:?}"
: "${CPU_ID:?}"

source_root="$JOB_ROOT/source/jc2"
case_rel="cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r2_20260828"
case_dir="$source_root/$case_rel"
work="$JOB_ROOT/work"
output="$JOB_ROOT/output"
custody="$JOB_ROOT/custody"
mkdir -p "$work" "$custody"
umask 077
exec > >(tee -a "$custody/worker.stdout.txt") \
     2> >(tee -a "$custody/worker.stderr.txt" >&2)

printf '%s\n' "$JOB_TAG" > "$custody/JOB_TAG.txt"
printf '%s\n' "$COMPONENT" > "$custody/COMPONENT.txt"
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
[[ "$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)" == 0 ]]
[[ "$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)" == 0 ]]
df -Pk "$JOB_ROOT" > "$custody/disk_preflight.txt"
ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/processes_preflight.txt"
command -v Singular > "$custody/Singular.path"
Singular --version > "$custody/Singular.version"

actual_prereg=$(sha256sum "$case_dir/PREREGISTRATION.md" | awk '{print $1}')
[[ "$actual_prereg" == "$EXPECTED_PREREG_SHA" ]]
(cd "$source_root" && sha256sum -c "$case_rel/SOURCE_MANIFEST.sha256") \
  > "$custody/source_manifest_check.txt"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export PYTHONPYCACHEPREFIX="$work/pycache"
python3 -m py_compile "$case_dir/prepare_base.py" "$case_dir/recurse_component.py" \
  "$case_dir/generator_selfcheck.py"

set +e
/usr/bin/time -v -o "$custody/adapter_selfcheck.time" \
  timeout --signal=TERM --kill-after=5s 60s taskset -c "$CPU_ID" \
  Singular -q "$case_dir/adapter_selfcheck.sing" \
  > "$custody/adapter_selfcheck.stdout.txt" \
  2> "$custody/adapter_selfcheck.stderr.txt"
selfcheck_rc=$?
set -e
printf '%s\n' "$selfcheck_rc" > "$custody/adapter_selfcheck.rc"
[[ "$selfcheck_rc" == 0 ]]
for marker in \
  SELFTEST_NILPOTENT_OPEN_EMPTY=1 \
  SELFTEST_PROPER_OPEN_SATURATION=1 \
  SELFTEST_CLOSED_SUCCESSOR_PROPER=1 \
  SELFTEST_MINOR_NF_NONZERO=1 \
  ENDPOINT_COMPLEMENT_ADAPTER_SELFCHECK_PASS=1
do
  grep -Fx "$marker" "$custody/adapter_selfcheck.stdout.txt" >/dev/null
done

base_archive="$source_root/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_charts_r1_20260828/custody/ggv_quotient_nf_endpoint_charts_r1_20260828T170400Z_i0f089_r2.terminal.tar.gz"
python3 -u "$case_dir/prepare_base.py" --archive "$base_archive" \
  --output "$work/base" > "$custody/prepare_base.stdout.txt" \
  2> "$custody/prepare_base.stderr.txt"
grep -F ENDPOINT_COMPLEMENT_BASE_PREPARATION_PASS \
  "$custody/prepare_base.stdout.txt" >/dev/null
python3 -u "$case_dir/generator_selfcheck.py" --base "$work/base" \
  --recursor "$case_dir/recurse_component.py" \
  --output "$custody/generated_q1p03_reduce.sing" \
  > "$custody/generator_selfcheck.stdout.txt" \
  2> "$custody/generator_selfcheck.stderr.txt"
for marker in \
  GENERATED_PLACEHOLDER_CENSUS=0 \
  PLACEHOLDER_MUTATION_REJECTED=1 \
  PIVOT_CERTIFICATE_MARKER_REQUIRED=1 \
  ENDPOINT_COMPLEMENT_GENERATOR_SELFCHECK_PASS=1
do
  grep -Fx "$marker" "$custody/generator_selfcheck.stdout.txt" >/dev/null
done

ulimit -f 67108864
ulimit -v 100663296
set +e
/usr/bin/time -v -o "$custody/component.time" \
  taskset -c "$CPU_ID" python3 -u "$case_dir/recurse_component.py" \
    --base "$work/base" --component "$COMPONENT" --output "$output" \
    --max-nodes 12 --stage-cap 900 \
    > "$custody/component.stdout.txt" 2> "$custody/component.stderr.txt"
component_rc=$?
set -e
printf '%s\n' "$component_rc" > "$custody/component.rc"

if [[ -f "$output/VERDICT.txt" ]]; then
  verdict=$(cat "$output/VERDICT.txt")
else
  verdict=ADAPTER_FAILURE_NO_VERDICT
fi
case "$verdict" in
  EXACT_ENDPOINT_DEAD_ON_FINITE_GEOMETRIC_CHART_COVER|\
  RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL|\
  NO_VERDICT_OPEN_REMAINDER)
    [[ "$component_rc" == 0 ]]
    ;;
  ADAPTER_FAILURE_NO_VERDICT)
    ;;
  *)
    verdict=ADAPTER_FAILURE_NO_VERDICT
    ;;
esac
printf '%s\n' "$verdict" > "$custody/TERMINAL_CLASSIFICATION.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/ENDED_UTC.txt"
awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  > "$custody/memory_final.txt"
[[ "$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)" == 0 ]]
[[ "$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)" == 0 ]]
ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/processes_final.txt"
(cd "$JOB_ROOT" && find source work output custody -type f \
  ! -name TERMINAL_MANIFEST.sha256 -print0 | sort -z | xargs -0 sha256sum) \
  > "$custody/TERMINAL_MANIFEST.sha256"
tar -czf "$JOB_ROOT/terminal_archive.tar.gz" -C "$JOB_ROOT" source work output custody
sha256sum "$JOB_ROOT/terminal_archive.tar.gz" > "$JOB_ROOT/terminal_archive.sha256"
printf '%s\n' "$verdict" > "$JOB_ROOT/TERMINAL.marker"
exit 0
