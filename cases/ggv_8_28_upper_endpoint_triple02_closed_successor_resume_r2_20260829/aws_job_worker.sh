#!/usr/bin/env bash
set -euo pipefail

: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${JOB_NONCE:?}"
: "${CPU_ID:?}"
: "${EXPECTED_INSTANCE_ID:?}"
: "${EXPECTED_HOSTNAME:?}"
: "${EXPECTED_SOURCE_ARCHIVE_SHA256:?}"
: "${CONTAINMENT_MODE:?}"
: "${SUPERVISOR_PID:?}"
: "${SUPERVISOR_STARTTIME:?}"
: "${LEASE_FILE:?}"
: "${WORKER_SCOPE_UNIT:?}"

[[ "$JOB_NONCE" =~ ^[a-z0-9]{8,32}$ ]]
[[ "$JOB_TAG" == *"_$JOB_NONCE" ]]

source_root="$JOB_ROOT/source/jc2"
case_rel="cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r2_20260829"
case_dir="$source_root/$case_rel"
expectations="$case_dir/runtime_expectations.env"
[[ -f "$expectations" ]]
# shellcheck disable=SC1090
source "$expectations"
: "${EXPECTED_PREREG_SHA256:?}"
: "${EXPECTED_WITNESS_REPLAY_SHA256:?}"
: "${EXPECTED_NODE2_REDUCE_SHA256:?}"
: "${EXPECTED_SINGULAR_NORMALIZED_VERSION_SHA256:?}"
: "${EXPECTED_ELIM_LIB_SHA256:?}"
r5_rel="cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r5_20260828"
r5_dir="$source_root/$r5_rel"
r3_rel="cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828"
frozen_archive="$source_root/$r3_rel/custody/terminals/ggv_endpoint_complement_triple02_r3_20260828T175423Z_i0f089.terminal.tar.gz"
po_rel="cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828"
settled_open_archive="$source_root/$po_rel/custody/terminals/ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d.terminal.tar.gz"
contract="$case_dir/containment_contract.py"
work="$JOB_ROOT/work"
custody="$JOB_ROOT/custody"
output="$JOB_ROOT/output"
source_archive="$JOB_ROOT/source_archive.tar.gz"
mkdir -p "$work" "$custody"
umask 077
exec > >(tee -a "$custody/worker.stdout.txt") \
     2> >(tee -a "$custody/worker.stderr.txt" >&2)

candidate_file="$custody/CANDIDATE_MATHEMATICAL_VERDICT.txt"
atomic_candidate() {
  local candidate=$1
  local temporary="$candidate_file.tmp.$$"
  printf '%s\n' "$candidate" > "$temporary"
  mv "$temporary" "$candidate_file"
}
watchdog_pid=0
finish_worker() {
  local finish_rc=$?
  if [[ "$watchdog_pid" -gt 1 ]]; then
    kill "$watchdog_pid" 2>/dev/null || true
  fi
  date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/WORKER_ENDED_UTC.txt" || true
  awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
    > "$custody/memory_worker_final.txt" || true
  ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
    > "$custody/processes_worker_final.txt" || true
  printf '%s\n' "$finish_rc" > "$custody/worker_exit_code.txt" || true
}
trap finish_worker EXIT

printf '%s\n' "$JOB_TAG" > "$custody/JOB_TAG.txt"
printf '%s\n' "$JOB_NONCE" > "$custody/JOB_NONCE.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$custody/WORKER_STARTED_UTC.txt"
worker_pid=$$
worker_pgid=$(ps -o pgid= -p $$ | tr -d ' ')
worker_sid=$(ps -o sid= -p $$ | tr -d ' ')
worker_start=$(awk '{print $22}' "/proc/$$/stat")
worker_uid=$(id -u)
worker_cgroup=$(tr '\n' ';' < "/proc/$$/cgroup")
printf '{"pid":%s,"pgid":%s,"sid":%s,"starttime":%s,"uid":%s,"mode":"%s","cgroup":"%s"}\n' \
  "$worker_pid" "$worker_pgid" "$worker_sid" "$worker_start" "$worker_uid" \
  "$CONTAINMENT_MODE" "$worker_cgroup" > "$custody/worker_identity.json"
if [[ "$CONTAINMENT_MODE" == pgid ]]; then
  [[ "$worker_pid" == "$worker_pgid" && "$worker_pid" == "$worker_sid" ]]
elif [[ "$CONTAINMENT_MODE" != systemd_scope ]]; then
  exit 71
fi
export JOB_CONTAINMENT_PGID="$worker_pgid"
export JOB_CONTAINMENT_SID="$worker_sid"
export WORKER_PID="$worker_pid"
export WORKER_STARTTIME="$worker_start"
export SOURCE_ARCHIVE_PATH="$source_archive"
uname -a > "$custody/uname.txt"
hostname > "$custody/hostname.txt"
cat /sys/class/dmi/id/sys_vendor > "$custody/sys_vendor.txt"
[[ "$(uname -s)" == Linux ]]
[[ "$(cat /sys/class/dmi/id/sys_vendor)" == "Amazon EC2" ]]
[[ "$(hostname)" == "$EXPECTED_HOSTNAME" ]]
[[ "$(basename "$JOB_ROOT")" == "$JOB_TAG" ]]
[[ "$CPU_ID" =~ ^[0-9]+$ ]]
[[ "$CPU_ID" -lt "$(nproc)" ]]

# Lease: the worker verifies the same atomic lease the launcher built, and the
# installed launcher copy must hash to the value recorded in that lease.
python3 "$contract" lease-verify --lease "$LEASE_FILE" \
  --sidecar "$JOB_ROOT/LEASE.sha256" --job-tag "$JOB_TAG" \
  --job-nonce "$JOB_NONCE" \
  --source-archive-sha256 "$EXPECTED_SOURCE_ARCHIVE_SHA256" \
  > "$custody/worker_lease_verify.txt"
launcher_copy="$JOB_ROOT/launch_preflight_copy.sh"
[[ -f "$launcher_copy" ]]
recorded_launcher_sha=$(python3 -c \
  'import json,sys; print(json.load(open(sys.argv[1]))["launcher_sha256"])' \
  "$LEASE_FILE")
actual_launcher_copy_sha=$(sha256sum "$launcher_copy" | awk '{print $1}')
[[ "$actual_launcher_copy_sha" == "$recorded_launcher_sha" ]]
printf '%s  %s\n' "$actual_launcher_copy_sha" "$launcher_copy" \
  > "$custody/launcher_copy.sha256"

token=$(curl -fsS --connect-timeout 2 -X PUT \
  -H 'X-aws-ec2-metadata-token-ttl-seconds: 300' \
  http://169.254.169.254/latest/api/token)
instance_id=$(curl -fsS --connect-timeout 2 \
  -H "X-aws-ec2-metadata-token: $token" \
  http://169.254.169.254/latest/meta-data/instance-id)
instance_type=$(curl -fsS --connect-timeout 2 \
  -H "X-aws-ec2-metadata-token: $token" \
  http://169.254.169.254/latest/meta-data/instance-type)
instance_job_tag=$(curl -fsS --connect-timeout 2 \
  -H "X-aws-ec2-metadata-token: $token" \
  http://169.254.169.254/latest/meta-data/tags/instance/CodexJob)
[[ "$instance_id" == "$EXPECTED_INSTANCE_ID" ]]
[[ "$instance_job_tag" == "$JOB_TAG" ]]
printf '%s\n' "$instance_id" > "$custody/instance_id.txt"
printf '%s\n' "$instance_type" > "$custody/instance_type.txt"
printf '%s\n' "$instance_job_tag" > "$custody/instance_CodexJob_tag.txt"

awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  > "$custody/memory_preflight.txt"
mem_total_kib=$(awk '/^MemTotal:/ {print $2}' /proc/meminfo)
swap_total_kib=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free_kib=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
[[ "$mem_total_kib" -le 1073741824 ]]
[[ "$swap_total_kib" == 0 ]]
[[ "$swap_free_kib" == 0 ]]
df -Pk "$JOB_ROOT" > "$custody/disk_preflight.txt"
ps -eo pid,ppid,pgid,sid,etimes,pcpu,rss,args --sort=-rss \
  > "$custody/processes_preflight.txt"

actual_source_archive_sha=$(sha256sum "$source_archive" | awk '{print $1}')
[[ "$actual_source_archive_sha" == "$EXPECTED_SOURCE_ARCHIVE_SHA256" ]]
printf '%s  %s\n' "$actual_source_archive_sha" "$source_archive" \
  > "$custody/source_archive.sha256"
actual_prereg_sha=$(sha256sum "$case_dir/AWS_PREREGISTRATION.md" | awk '{print $1}')
[[ "$actual_prereg_sha" == "$EXPECTED_PREREG_SHA256" ]]
(cd "$source_root" && sha256sum -c "$case_rel/SOURCE_MANIFEST.sha256") \
  > "$custody/source_manifest_check.txt"

singular_path=$(command -v Singular)
printf '%s\n' "$singular_path" > "$custody/Singular.path"
Singular --version > "$custody/Singular.version"
sed -E 's/random=[0-9]+/random=<normalized>/' "$custody/Singular.version" \
  > "$custody/Singular.version.normalized"
actual_singular_version_sha=$(sha256sum \
  "$custody/Singular.version.normalized" | awk '{print $1}')
[[ "$actual_singular_version_sha" == "$EXPECTED_SINGULAR_NORMALIZED_VERSION_SHA256" ]]
# The exact Singular binary digest becomes part of the one-job binding of
# every stage identity/result record and of the decision record.
singular_binary_sha=$(sha256sum "$singular_path" | awk '{print $1}')
printf '%s  %s\n' "$singular_binary_sha" "$singular_path" \
  > "$custody/singular_binary.sha256"
export EXPECTED_SINGULAR_SHA256="$singular_binary_sha"
mapfile -t elim_candidates < <(find /usr/share/singular /usr/local/share/singular \
  -type f -name elim.lib 2>/dev/null | sort -u)
[[ "${#elim_candidates[@]}" == 1 ]]
printf '%s\n' "${elim_candidates[0]}" > "$custody/elim.lib.path"
actual_elim_sha=$(sha256sum "${elim_candidates[0]}" | awk '{print $1}')
[[ "$actual_elim_sha" == "$EXPECTED_ELIM_LIB_SHA256" ]]
printf '%s  %s\n' "$actual_elim_sha" "${elim_candidates[0]}" \
  > "$custody/elim.lib.sha256"

export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export PYTHONPYCACHEPREFIX="$work/pycache"
python3 -m py_compile \
  "$case_dir/prepare_resume.py" "$case_dir/build_resume.py" \
  "$case_dir/resume_recursor.py" "$case_dir/classify_resume.py" \
  "$case_dir/generator_selfcheck.py" "$case_dir/run_singular_stage.py" \
  "$case_dir/containment_contract.py" "$case_dir/containment_selfcheck.py" \
  "$r5_dir/recurse_component.py" "$r5_dir/transcript_gate.py"

python3 "$case_dir/containment_selfcheck.py" \
  --contract "$contract" \
  --stage-runner "$case_dir/run_singular_stage.py" \
  --worker "$case_dir/aws_job_worker.sh" \
  --supervisor "$case_dir/aws_supervisor.sh" \
  --output "$custody/containment_selfcheck.json" \
  > "$custody/containment_selfcheck.stdout.txt" \
  2> "$custody/containment_selfcheck.stderr.txt"
grep -Fx 'CONTAINMENT_AND_TERMINAL_SELFCHECK_PASS=1' \
  "$custody/containment_selfcheck.stdout.txt" >/dev/null

# C3: the exact-PGID fallback is NO_VERDICT-only.  Without an independently
# bounded systemd scope the worker refuses to run any Singular stage or
# production and banks nothing; the supervisor's decision layer cannot
# promote in this mode either.
if [[ "$CONTAINMENT_MODE" != systemd_scope ]]; then
  printf '%s\n' PGID_FALLBACK_PRODUCTION_SKIPPED=1 \
    > "$custody/PGID_FALLBACK_PRODUCTION_SKIPPED.marker"
  exit 0
fi

# C3: supervisor-death containment.  A watchdog inside the worker scope
# checks the exact supervisor PID start time and kills the entire scope
# cgroup when the supervisor is gone; the scope's independent RuntimeMaxSec
# bounds the tree even if this watchdog dies with it.
supervisor_death_watchdog() {
  while true; do
    sleep 5
    local current
    current=$(awk '{print $22}' "/proc/$SUPERVISOR_PID/stat" 2>/dev/null \
      || printf 'GONE')
    if [[ "$current" != "$SUPERVISOR_STARTTIME" ]]; then
      date -u +%Y-%m-%dT%H:%M:%SZ \
        > "$custody/SUPERVISOR_DEATH_DETECTED_UTC.txt" 2>/dev/null || true
      systemctl --user kill --kill-whom=all --signal=KILL \
        "$WORKER_SCOPE_UNIT.scope" >/dev/null 2>&1 || true
      exit 0
    fi
  done
}
supervisor_death_watchdog &
watchdog_pid=$!
printf '%s\n' "$watchdog_pid" > "$custody/supervisor_death_watchdog.pid"

ulimit -f 67108864
ulimit -v 268435456

run_stage() {
  local label=$1
  local script=$2
  local stage_cwd=$3
  local cap=$4
  local restore_errexit=0
  if [[ $- == *e* ]]; then
    restore_errexit=1
  fi
  set +e
  /usr/bin/time -v -o "$custody/${label}.time" \
    taskset -c "$CPU_ID" python3 "$case_dir/run_singular_stage.py" \
      --singular "$singular_path" --script "$script" --cwd "$stage_cwd" \
      --stdout "$custody/${label}.stdout.txt" \
      --stderr "$custody/${label}.stderr.txt" \
      --result "$custody/${label}.result.json" \
      --identity "$custody/${label}.identity.json" \
      --cap-seconds "$cap" --expected-pgid "$JOB_CONTAINMENT_PGID" \
      --expected-sid "$JOB_CONTAINMENT_SID" --job-tag "$JOB_TAG" \
      --job-nonce "$JOB_NONCE" --stage-label "$label" \
      --lease "$LEASE_FILE" --source-archive "$source_archive" \
      --source-archive-sha256 "$EXPECTED_SOURCE_ARCHIVE_SHA256" \
      --singular-sha256 "$EXPECTED_SINGULAR_SHA256" \
      --supervisor-pid "$SUPERVISOR_PID" \
      --supervisor-starttime "$SUPERVISOR_STARTTIME" \
      --worker-pid "$WORKER_PID" --worker-starttime "$WORKER_STARTTIME" \
      > "$custody/${label}.runner.stdout.txt" \
      2> "$custody/${label}.runner.stderr.txt"
  local stage_rc=$?
  if [[ "$restore_errexit" == 1 ]]; then
    set -e
  else
    set +e
  fi
  printf '%s\n' "$stage_rc" > "$custody/${label}.rc"
  return "$stage_rc"
}

control_work="$work/controls"
mkdir -p "$control_work/hostile" "$control_work/selfcheck"
run_stage diagnostic_hostile "$case_dir/diagnostic_hostile.sing" \
  "$control_work/hostile" 60
python3 "$r5_dir/transcript_gate.py" \
  --stdout "$custody/diagnostic_hostile.stdout.txt" \
  --stderr "$custody/diagnostic_hostile.stderr.txt" --expect diagnostic \
  --evidence "$custody/diagnostic_hostile.gate.json" \
  > "$custody/diagnostic_hostile.gate.stdout.txt" \
  2> "$custody/diagnostic_hostile.gate.stderr.txt"
grep -Fx 'TRANSCRIPT_EXPECTED_DIAGNOSTIC_PASS=1' \
  "$custody/diagnostic_hostile.gate.stdout.txt" >/dev/null
grep -Fx 'HOSTILE_SAT_TYPE=list' "$custody/diagnostic_hostile.stdout.txt" >/dev/null
grep -Fx 'HOSTILE_SAT_SIZE=1' "$custody/diagnostic_hostile.stdout.txt" >/dev/null
grep -Fx 'HOSTILE_END_MARKER=1' "$custody/diagnostic_hostile.stdout.txt" >/dev/null

run_stage adapter_selfcheck "$case_dir/adapter_selfcheck.sing" \
  "$control_work/selfcheck" 60
python3 "$r5_dir/transcript_gate.py" \
  --stdout "$custody/adapter_selfcheck.stdout.txt" \
  --stderr "$custody/adapter_selfcheck.stderr.txt" --expect clean \
  --evidence "$custody/adapter_selfcheck.gate.json" \
  > "$custody/adapter_selfcheck.gate.stdout.txt" \
  2> "$custody/adapter_selfcheck.gate.stderr.txt"
for marker in \
  SELFTEST_SUCCESSOR_CONTAINS_PARENT_DELTA=1 \
  SELFTEST_SUCCESSOR_PROPER=1 \
  SELFTEST_SUCCESSOR_PARENT_OPEN_EMPTY=1 \
  SELFTEST_PROPER_STABILITY_FAILURES=0 \
  SELFTEST_PROPER_NODE_INCLUSION_FAILURES=0 \
  SELFTEST_PROPER_PURE_POWER_REDUCTION_COUNT=0 \
  SELFTEST_PROPER_REVERSE_REDUCTION_COUNT=2 \
  SELFTEST_STRICT_OVERIDEAL_WEAK_PREDICATES_PASS=1 \
  SELFTEST_STRICT_OVERIDEAL_REVERSE_REJECTED=1 \
  SELFTEST_EMPTY_POWER_FOUND=1 \
  SELFTEST_EMPTY_POWER_EXPONENT=3 \
  SELFTEST_EMPTY_POWER_REDUCTION_COUNT=4 \
  SELFTEST_EMPTY_PRIOR_NONMEMBERSHIP_COUNT=3 \
  SELFTEST_REDUCER_DISPLAYED_Q2_FACTOR_NF_ZERO=1 \
  SELFTEST_REDUCER_KNOWN_NONZERO_NF=1 \
  SELFTEST_ENDPOINT_PLUS_ONE_AFFINE_REPLAY=1 \
  SELFTEST_ENDPOINT_PLUS_TWO_AFFINE_REPLAY=1 \
  SELFTEST_ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=1 \
  SELFTEST_INNOCENT_PLUS_ONE_ZERO_PLUS_TWO_NONZERO=1 \
  SELFTEST_BORDERED_PLANT_EQUALS_DELTA=1 \
  TRIPLE02_CLOSED_SUCCESSOR_ADAPTER_SELFCHECK_PASS=1
do
  grep -Fx "$marker" "$custody/adapter_selfcheck.stdout.txt" >/dev/null
done

python3 -u "$case_dir/prepare_resume.py" --r3-archive "$frozen_archive" \
  --proper-open-archive "$settled_open_archive" \
  --destination "$work/prepared" > "$custody/prepare_resume.stdout.txt" \
  2> "$custody/prepare_resume.stderr.txt"
grep -Fx 'TRIPLE02_CLOSED_SUCCESSOR_PREPARATION_PASS=1' \
  "$custody/prepare_resume.stdout.txt" >/dev/null
python3 -u "$case_dir/build_resume.py" --prepared "$work/prepared" \
  --frozen-r5-source "$r5_dir/recurse_component.py" \
  --output-dir "$work/generated" > "$custody/build_resume.stdout.txt" \
  2> "$custody/build_resume.stderr.txt"
grep -Fx 'TRIPLE02_CLOSED_SUCCESSOR_BUILD_PASS=1' \
  "$custody/build_resume.stdout.txt" >/dev/null
actual_witness_sha=$(sha256sum \
  "$work/generated/TRIPLE02_NODE1_WITNESS_REPLAY.sing" | awk '{print $1}')
[[ "$actual_witness_sha" == "$EXPECTED_WITNESS_REPLAY_SHA256" ]]
actual_node2_sha=$(sha256sum \
  "$work/generated/NODE_002_REDUCE_EXPECTED.sing" | awk '{print $1}')
[[ "$actual_node2_sha" == "$EXPECTED_NODE2_REDUCE_SHA256" ]]
expected_witness_file_sha=$(awk 'NR==1 {print $1}' \
  "$case_dir/EXPECTED_GENERATED_SCRIPTS.sha256")
expected_node2_file_sha=$(awk 'NR==2 {print $1}' \
  "$case_dir/EXPECTED_GENERATED_SCRIPTS.sha256")
[[ "$expected_witness_file_sha" == "$EXPECTED_WITNESS_REPLAY_SHA256" ]]
[[ "$expected_node2_file_sha" == "$EXPECTED_NODE2_REDUCE_SHA256" ]]

python3 -u "$case_dir/generator_selfcheck.py" \
  --preparer "$case_dir/prepare_resume.py" \
  --builder "$case_dir/build_resume.py" \
  --recursor "$case_dir/resume_recursor.py" \
  --classifier "$case_dir/classify_resume.py" \
  --adapter-selfcheck "$case_dir/adapter_selfcheck.sing" \
  --frozen-archive "$frozen_archive" \
  --frozen-r5-source "$r5_dir/recurse_component.py" \
  --prepared "$work/prepared" --build "$work/generated" \
  --fixture-root "$work/generator_fixtures" \
  > "$custody/generator_selfcheck.stdout.txt" \
  2> "$custody/generator_selfcheck.stderr.txt"
grep -Fx 'TRIPLE02_CLOSED_SUCCESSOR_GENERATOR_SELFCHECK_PASS=1' \
  "$custody/generator_selfcheck.stdout.txt" >/dev/null

production="$work/production"
set +e
/usr/bin/time -v -o "$custody/production.time" \
  taskset -c "$CPU_ID" python3 -u "$case_dir/resume_recursor.py" \
    --prepared "$work/prepared" --build "$work/generated" \
    --frozen-r5-source "$r5_dir/recurse_component.py" \
    --case-dir "$case_dir" --output "$production" \
    --singular "$singular_path" --start-node 2 --max-nodes 6 \
    --fast-cap 900 --slow-cap 3600 \
    > "$custody/production.stdout.txt" \
    2> "$custody/production.stderr.txt"
production_rc=$?
set -e
printf '%s\n' "$production_rc" > "$custody/production.rc"
if [[ "$production_rc" != 0 ]]; then
  atomic_candidate ADAPTER_FAILURE_NO_VERDICT
  exit 0
fi
python3 -u "$case_dir/classify_resume.py" \
  --production "$production" --prepared "$work/prepared" \
  --build "$work/generated" \
  --frozen-r5-source "$r5_dir/recurse_component.py" \
  --case-dir "$case_dir" --output "$output" \
  --job-tag "$JOB_TAG" --job-nonce "$JOB_NONCE" \
  --source-archive-sha256 "$EXPECTED_SOURCE_ARCHIVE_SHA256" \
  --singular-sha256 "$EXPECTED_SINGULAR_SHA256" \
  --singular-path "$singular_path" --lease "$LEASE_FILE" \
  --worker-identity "$custody/worker_identity.json" \
  --supervisor-identity "$custody/supervisor_identity.json" \
  --fast-cap 900 --slow-cap 3600 \
  > "$custody/classifier.stdout.txt" \
  2> "$custody/classifier.stderr.txt"
grep -Fx 'TRIPLE02_CLOSED_SUCCESSOR_CLASSIFIER_PASS=1' \
  "$custody/classifier.stdout.txt" >/dev/null
candidate=$(tr -d '\r\n' < "$output/VERDICT.txt")
case "$candidate" in
  EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER|\
  RING_LEVEL_ENDPOINT_SURVIVOR_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_CHART_PENDING_NILPOTENCE_RADICAL|\
  NO_VERDICT_OPEN_REMAINDER_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR|\
  REVERSE_CONTAINMENT_SEARCH_EXHAUSTED_NO_VERDICT_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR) ;;
  *) exit 72 ;;
esac
(cd "$JOB_ROOT" && find work/production work/generated output -type f -print0 | \
  sort -z | xargs -0 sha256sum) > "$custody/WORKER_ARTIFACT_MANIFEST.sha256"
(cd "$JOB_ROOT" && sha256sum -c custody/WORKER_ARTIFACT_MANIFEST.sha256) \
  > "$custody/worker_artifact_manifest_check.txt"
printf '%s\n' CLOSED_SUCCESSOR_RESULT_BANKED_WITHOUT_WHOLE_STRATUM_OR_JC2_PROMOTION \
  > "$custody/SCOPE_FIREWALL.marker"
awk '/MemTotal|MemAvailable|SwapTotal|SwapFree/ {print}' /proc/meminfo \
  > "$custody/memory_worker_prepromotion.txt"
[[ "$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)" == 0 ]]
[[ "$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)" == 0 ]]
# C1: bank the one content-addressed decision record.  It derives the
# candidate from the production and classifier verdicts (never from an
# argument), requires them equal and allowlisted, and binds the job tag,
# nonce, source archive, lease, launcher, Singular binary, worker/supervisor
# identities, both summary/verdict hashes, and the complete artifact
# manifest hash.  The late authority replays every equality from the frozen
# terminal archive.
python3 "$contract" decision-build \
  --output-record "$custody/DECISION_RECORD.json" \
  --output-sidecar "$custody/DECISION_RECORD.sha256" \
  --job-tag "$JOB_TAG" --job-nonce "$JOB_NONCE" \
  --source-archive-sha256 "$EXPECTED_SOURCE_ARCHIVE_SHA256" \
  --singular-sha256 "$EXPECTED_SINGULAR_SHA256" \
  --containment-mode-file "$custody/containment_mode.txt" \
  --lease "$LEASE_FILE" \
  --worker-identity "$custody/worker_identity.json" \
  --supervisor-identity "$custody/supervisor_identity.json" \
  --production "$production" --classifier-output "$output" \
  --artifact-manifest "$custody/WORKER_ARTIFACT_MANIFEST.sha256" \
  > "$custody/decision_build.stdout.txt" \
  2> "$custody/decision_build.stderr.txt"
grep -E '^DECISION_RECORD_SHA256=[0-9a-f]{64}$' \
  "$custody/decision_build.stdout.txt" >/dev/null
printf '%s\n' WORKER_ARTIFACT_AND_RESOURCE_GATES_PASS=1 \
  > "$custody/WORKER_FINAL_GATE.marker"
atomic_candidate "$candidate"
exit 0
