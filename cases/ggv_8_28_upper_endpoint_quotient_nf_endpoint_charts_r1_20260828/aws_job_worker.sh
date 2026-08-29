#!/usr/bin/env bash
set -euo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${EXPECTED_INSTANCE_ID:?}"
: "${EXPECTED_HOSTNAME:?}"
: "${EXPECTED_PREREG_SHA:?}"
: "${CPU_ID:?}"

source_root="$JOB_ROOT/source/jc2"
case_rel="cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_charts_r1_20260828"
case_dir="$source_root/$case_rel"
work="$JOB_ROOT/work"
output="$JOB_ROOT/output"
custody="$JOB_ROOT/custody"
mkdir -p "$work" "$output" "$custody"
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
python3 -m py_compile "$case_dir/prepare_inputs.py" "$case_dir/build_endpoint_chart.py"
set +e
/usr/bin/time -v -o "$custody/adapter_selfcheck.time" \
  timeout --signal=TERM --kill-after=5s 60s \
  taskset -c "$CPU_ID" Singular -q "$case_dir/adapter_selfcheck.sing" \
  > "$custody/adapter_selfcheck.stdout.txt" \
  2> "$custody/adapter_selfcheck.stderr.txt"
selfcheck_rc=$?
set -e
printf '%s\n' "$selfcheck_rc" > "$custody/adapter_selfcheck.rc"
[[ "$selfcheck_rc" == 0 ]]
grep -Fx 'SELFTEST_ZERO_NF=1' "$custody/adapter_selfcheck.stdout.txt" >/dev/null
grep -Fx 'SELFTEST_NONZERO_NF=1' "$custody/adapter_selfcheck.stdout.txt" >/dev/null
grep -Fx 'SELFTEST_CRAMER_IDENTITY=1' "$custody/adapter_selfcheck.stdout.txt" >/dev/null
grep -Fx 'ENDPOINT_CHART_ADAPTER_SELFCHECK_PASS=1' "$custody/adapter_selfcheck.stdout.txt" >/dev/null
python3 -u "$case_dir/prepare_inputs.py" --payload-dir "$source_root" \
  --work-dir "$work/prepared" > "$custody/prepare.stdout.txt" \
  2> "$custody/prepare.stderr.txt"
grep -F 'IMMUTABLE_BANKED_INPUT_PREPARATION_PASS' "$custody/prepare.stdout.txt" >/dev/null

ulimit -f 67108864
ulimit -v 100663296
components=(p c8p02 q1p02 q1p03 triple02 triple03)
declare -A labels=( [p]=P [c8p02]=C8P02 [q1p02]=Q1P02 [q1p03]=Q1P03 [triple02]=TRIPLE02 [triple03]=TRIPLE03 )
overall_failure=0
for component in "${components[@]}"; do
  label=${labels[$component]}
  stage="$output/$component"
  mkdir "$stage"
  printf '%s\n' "$component" > "$output/CURRENT_COMPONENT"
  set +e
  /usr/bin/time -v -o "$stage/build.time" timeout --signal=TERM --kill-after=15s 120s \
    taskset -c "$CPU_ID" python3 -u "$case_dir/build_endpoint_chart.py" \
      --source-root "$work/prepared/upstream_source/jc2" \
      --packet "$work/prepared/banked/$component" --component "$component" \
      --output "$stage/chart.sing" > "$stage/build.stdout.txt" \
      2> "$stage/build.stderr.txt"
  build_rc=$?
  set -e
  printf '%s\n' "$build_rc" > "$stage/build.rc"
  if [[ "$build_rc" != 0 ]] || ! grep -F 'ENDPOINT_CHART_BUILD_PASS' "$stage/build.stdout.txt" >/dev/null; then
    printf '%s\n' ADAPTER_FAILURE_BUILD_NO_VERDICT > "$stage/CLASSIFICATION.txt"
    overall_failure=1
    continue
  fi
  cd "$stage"
  set +e
  /usr/bin/time -v -o "$stage/run.time" timeout --signal=TERM --kill-after=30s 900s \
    taskset -c "$CPU_ID" Singular -q "$stage/chart.sing" \
      > "$stage/run.stdout.txt" 2> "$stage/run.stderr.txt"
  run_rc=$?
  set -e
  printf '%s\n' "$run_rc" > "$stage/run.rc"
  if [[ "$run_rc" != 0 ]]; then
    printf '%s\n' ADAPTER_FAILURE_OR_TIMEOUT_NO_VERDICT > "$stage/CLASSIFICATION.txt"
    overall_failure=1
    continue
  fi
  cmp "$work/prepared/banked/$component/${label}_NF_RATIONAL_UNIT_PIVOTS.tsv" \
      "$stage/${label}_REPLAY_PIVOTS.tsv" > "$stage/pivot_cmp.stdout.txt" \
      2> "$stage/pivot_cmp.stderr.txt" || {
        printf '%s\n' ADAPTER_FAILURE_PIVOT_BYTE_DISAGREEMENT_NO_VERDICT > "$stage/CLASSIFICATION.txt"
        overall_failure=1
        continue
      }
  cmp "$work/prepared/banked/$component/${label}_NF_RESIDUAL_MATRIX.tsv" \
      "$stage/${label}_REPLAY_RESIDUAL.tsv" > "$stage/residual_cmp.stdout.txt" \
      2> "$stage/residual_cmp.stderr.txt" || {
        printf '%s\n' ADAPTER_FAILURE_RESIDUAL_BYTE_DISAGREEMENT_NO_VERDICT > "$stage/CLASSIFICATION.txt"
        overall_failure=1
        continue
      }
  for marker in \
    '^NF_RATIONAL_UNIT_PIVOT_COUNT=95$' \
    '^NF_PIVOT_INVARIANT_FAILURES=0$' \
    '^CHART_DELTA_NF_NONZERO=1$' \
    '^BANKED_DELTA_REPLAY_EQUAL=1$' \
    '^BORDERED_RPLUS1_IDENTITY_FAILURES=0$' \
    '^FULL_106_ROW_KERNEL_REPLAY_FAILURES=0$' \
    '^ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1$' \
    '^CHART_COMPLEMENT_IDEAL_ADDED=1$' \
    '^NO_RADICAL_NILPOTENCE_OR_GEOMETRIC_INFERENCE=1$' \
    '^REDUCER_SAFE_ENDPOINT_CHART_COMPLETE=1$'
  do
    if ! grep -q "$marker" "$stage/run.stdout.txt"; then
      printf '%s\n' ADAPTER_FAILURE_MARKER_NO_VERDICT > "$stage/CLASSIFICATION.txt"
      overall_failure=1
      break
    fi
  done
  if [[ -f "$stage/CLASSIFICATION.txt" ]]; then
    continue
  fi
  grep '^CHART_CLASSIFICATION=' "$stage/run.stdout.txt" | tail -1 | cut -d= -f2- \
    > "$stage/CLASSIFICATION.txt"
  grep '^COMPLEMENT_CLASSIFICATION=' "$stage/run.stdout.txt" | tail -1 \
    > "$stage/COMPLEMENT_CLASSIFICATION.txt"
  find "$stage" -type f ! -name ARTIFACTS.sha256 -print0 | sort -z | \
    xargs -0 sha256sum > "$stage/ARTIFACTS.sha256"
  [[ "$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)" == 0 ]]
  [[ "$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)" == 0 ]]
done

printf '%s\n' "$overall_failure" > "$output/overall_failure.txt"
if [[ "$overall_failure" == 0 ]]; then
  printf '%s\n' ROOT_CHARTS_COMPLETE_COMPLEMENTS_COMPONENTWISE > "$output/VERDICT.txt"
else
  printf '%s\n' COMPONENTWISE_ADAPTER_FAILURE_NO_VERDICT > "$output/VERDICT.txt"
fi
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/ENDED_UTC.txt"
awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  > "$custody/memory_final.txt"
ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/processes_final.txt"
(cd "$JOB_ROOT" && find source work output custody -type f \
  ! -name TERMINAL_MANIFEST.sha256 -print0 | sort -z | xargs -0 sha256sum) \
  > "$custody/TERMINAL_MANIFEST.sha256"
tar -czf "$JOB_ROOT/terminal_archive.tar.gz" -C "$JOB_ROOT" source work output custody
sha256sum "$JOB_ROOT/terminal_archive.tar.gz" > "$JOB_ROOT/terminal_archive.sha256"
printf '%s\n' "$(cat "$output/VERDICT.txt")" > "$JOB_ROOT/TERMINAL.marker"
exit 0
