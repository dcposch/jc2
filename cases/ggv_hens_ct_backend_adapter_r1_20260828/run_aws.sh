#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "usage: run_aws.sh STAGING_SOURCE EXPECTED_INSTANCE_ID EXPECTED_INSTANCE_TYPE" >&2
  exit 64
fi

staging_source=$(realpath "$1")
expected_instance_id=$2
expected_instance_type=$3
job_tag=${AWS_RUN_TAG:-}
[[ -n "$job_tag" ]]
[[ "$job_tag" =~ ^ggv_hens_ct_backend_r1_[0-9]{8}T[0-9]{6}Z_[A-Za-z0-9_.-]+$ ]]
[[ "$expected_instance_id" == "i-040b7a1c2ed72d4cc" ]]
[[ "$expected_instance_type" == "r6i.16xlarge" ]]

run_dir="/home/ubuntu/jobs/$job_tag"
[[ ! -e "$run_dir" ]]
mkdir -p "$run_dir/source" "$run_dir/output" "$run_dir/records" "$run_dir/work"
cp -a "$staging_source/." "$run_dir/source/"
cd "$run_dir/source"
sha256sum -c SOURCE_MANIFEST.sha256
source_manifest_sha=$(sha256sum SOURCE_MANIFEST.sha256 | awk '{print $1}')
chmod -R a-w "$run_dir/source"

python3 "$run_dir/source/preflight.py" \
  --expected-instance-id "$expected_instance_id" \
  --expected-instance-type "$expected_instance_type" \
  --run-dir "$run_dir" --job-tag "$job_tag" \
  --output "$run_dir/records/PREFLIGHT.json"

registry="$run_dir/records/GROUP.tsv"
register_gate="$run_dir/records/REGISTERED"
/usr/bin/setsid "$run_dir/source/job_worker.sh" \
  "$run_dir" "$register_gate" "$source_manifest_sha" \
  > "$run_dir/records/worker.stdout" 2> "$run_dir/records/worker.stderr" &
worker_pid=$!
worker_pgid=$(ps -o pgid= -p "$worker_pid" | tr -d ' ')
worker_session=$(ps -o sid= -p "$worker_pid" | tr -d ' ')
[[ "$worker_pid" == "$worker_pgid" && "$worker_pid" == "$worker_session" ]]
worker_starttime=$(python3 - "$worker_pid" <<'PY'
from pathlib import Path
import sys
text = Path(f"/proc/{sys.argv[1]}/stat").read_text()
print(text[text.rfind(")") + 2:].split()[19])
PY
)
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "hens_ct_backend_r1" "$worker_pid" "$worker_pgid" "$worker_session" \
  "$worker_starttime" "$run_dir" "$source_manifest_sha" > "$registry"
touch "$register_gate"

python3 "$run_dir/source/process_group_guard.py" snapshot --registry "$registry" \
  > "$run_dir/records/FIRST_CENSUS.json"
python3 "$run_dir/source/process_group_guard.py" monitor --registry "$registry" \
  --grace-seconds 30 > "$run_dir/records/TELEMETRY.jsonl" 2>&1 &
monitor_pid=$!

set +e
wait "$worker_pid"
worker_rc=$?
wait "$monitor_pid"
monitor_rc=$?
set -e
printf '%s\n' "$worker_rc" > "$run_dir/records/worker.rc"
printf '%s\n' "$monitor_rc" > "$run_dir/records/monitor.rc"
if [[ "$monitor_rc" -ne 0 ]]; then
  python3 "$run_dir/source/process_group_guard.py" stop --registry "$registry" --grace-seconds 30 \
    > "$run_dir/records/GUARD_STOP.json" || true
  if [[ -w "$run_dir/output" ]]; then
    printf '%s\n' "RESOURCE_STOP" > "$run_dir/output/TERMINAL"
  fi
fi
python3 "$run_dir/source/process_group_guard.py" snapshot --registry "$registry" \
  > "$run_dir/records/FINAL_CENSUS.json"
python3 - "$run_dir/records/FINAL_CENSUS.json" <<'PY'
import json, sys
data = json.load(open(sys.argv[1], encoding="utf-8"))
assert data["member_count"] == 0, data
PY

chmod -R u+w "$run_dir/records"
find "$run_dir/source" "$run_dir/output" "$run_dir/records" \
  -type f ! -name EVIDENCE.sha256 -print0 | LC_ALL=C sort -z | xargs -0 sha256sum \
  > "$run_dir/records/EVIDENCE.sha256"
chmod -R a-w "$run_dir/source" "$run_dir/output" "$run_dir/records"
printf '%s\n' "RUN_DIR=$run_dir"
printf '%s\n' "WORKER_RC=$worker_rc"
printf '%s\n' "MONITOR_RC=$monitor_rc"
if [[ -s "$run_dir/output/TERMINAL" ]]; then
  printf '%s' "TERMINAL="
  cat "$run_dir/output/TERMINAL"
else
  printf '%s\n' "TERMINAL=MISSING"
fi
exit "$worker_rc"
