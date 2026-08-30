#!/usr/bin/env bash
set -euo pipefail

readonly EXPECTED_LANE='K00-REES-SANDWICH-EXACT-N-R6B-20260829'
readonly EXPECTED_INSTANCE='i-0f089e64c378f5da3'
readonly EXPECTED_MANIFEST='d05d7c941441a4e6cffae8fb23f7910b0e958d03535bac097b218504deae8e82'
readonly RESULT_PREFIX='K00-REES-SANDWICH-EXACT-N-R6B'

fail() {
  printf 'RUNNER_FAIL=%s\n' "$1" >&2
  exit 125
}

[[ "$(uname -s)" == 'Linux' ]] || fail 'NON_LINUX'
[[ -r /sys/class/dmi/id/sys_vendor ]] || fail 'NO_DMI_VENDOR'
[[ "$(tr -d '\n' </sys/class/dmi/id/sys_vendor)" == 'Amazon EC2' ]] || fail 'NON_EC2'
[[ "${REGISTERED_LANE_TAG:-}" == "$EXPECTED_LANE" ]] || fail 'LANE_TAG_MISMATCH'
[[ $# -eq 1 ]] || fail 'USAGE_RUN_DIR'

run_dir=$1
[[ "$run_dir" == /* ]] || fail 'RUN_DIR_NOT_ABSOLUTE'
[[ -d "$run_dir" ]] || fail 'RUN_DIR_MISSING'
cd "$run_dir"

token=$(curl -fsS -X PUT \
  -H 'X-aws-ec2-metadata-token-ttl-seconds: 60' \
  http://169.254.169.254/latest/api/token) || fail 'IMDS_TOKEN'
instance_id=$(curl -fsS -H "X-aws-ec2-metadata-token: $token" \
  http://169.254.169.254/latest/meta-data/instance-id) || fail 'IMDS_INSTANCE'
[[ "$instance_id" == "$EXPECTED_INSTANCE" ]] || fail 'INSTANCE_MISMATCH'

[[ "$(sha256sum PAYLOAD.sha256 | awk '{print $1}')" == "$EXPECTED_MANIFEST" ]] || \
  fail 'MANIFEST_HASH'
sha256sum -c PAYLOAD.sha256 >/dev/null || fail 'PAYLOAD_HASH'

stdout_file="${RESULT_PREFIX}.stdout"
stderr_file="${RESULT_PREFIX}.stderr"
telemetry_file="${RESULT_PREFIX}.caprun.json"
meta_file="${RESULT_PREFIX}.meta"
witness_file='WITNESS_MONOMIAL.poly'
normal_file='WITNESS_NORMAL_FORM.poly'
for output in "$stdout_file" "$stderr_file" "$telemetry_file" "$meta_file" \
              "$witness_file" "$normal_file"; do
  [[ ! -e "$output" ]] || fail "OUTPUT_EXISTS_${output}"
done

{
  printf 'lane=%s\n' "$EXPECTED_LANE"
  printf 'instance_id=%s\n' "$instance_id"
  printf 'hostname=%s\n' "$(hostname)"
  printf 'boot_id=%s\n' "$(tr -d '\n' </proc/sys/kernel/random/boot_id)"
  printf 'vendor=%s\n' "$(tr -d '\n' </sys/class/dmi/id/sys_vendor)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'cwd=%s\n' "$run_dir"
  printf 'payload_manifest_sha256=%s\n' "$EXPECTED_MANIFEST"
  printf 'load_start=%s\n' "$(cut -d' ' -f1-3 /proc/loadavg)"
  printf 'memavailable_kib_start=%s\n' "$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)"
  printf 'singular_path=%s\n' "$(command -v Singular)"
  printf 'singular_version_begin\n'
  Singular -v
  printf 'singular_version_end\n'
  printf 'python_version=%s\n' "$(python3 --version 2>&1)"
  printf 'cap_wall_seconds=1800\n'
  printf 'cap_cpu_seconds=1800\n'
  printf 'cap_rss_bytes=34359738368\n'
  printf 'cap_rss_sample_seconds=0.10\n'
} >"$meta_file"

set +e
python3 run_capped.py \
  --wall-seconds 1800 \
  --cpu-seconds 1800 \
  --rss-bytes 34359738368 \
  --rss-sample-seconds 0.10 \
  --term-grace-seconds 5 \
  --stdout-file "$stdout_file" \
  --stderr-file "$stderr_file" \
  --telemetry-file "$telemetry_file" \
  --cwd "$run_dir" \
  -- /usr/bin/Singular -q run_rees_sandwich.sing
caprun_rc=$?
set -e

{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'caprun_rc=%s\n' "$caprun_rc"
  printf 'load_end=%s\n' "$(cut -d' ' -f1-3 /proc/loadavg)"
  printf 'memavailable_kib_end=%s\n' "$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)"
  printf 'stdout_sha256=%s\n' "$(sha256sum "$stdout_file" | awk '{print $1}')"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$stderr_file" | awk '{print $1}')"
  printf 'telemetry_sha256=%s\n' "$(sha256sum "$telemetry_file" | awk '{print $1}')"
} >>"$meta_file"

[[ "$caprun_rc" -eq 0 ]] || fail 'CAPRUN_NONZERO'
python3 - "$telemetry_file" <<'PY' || fail 'CAPRUN_TELEMETRY'
import json
import sys

with open(sys.argv[1], "r", encoding="utf-8") as stream:
    data = json.load(stream)
assert data["schema"] == "CAPRUN/v1"
assert data["status"] == "NORMAL_EXIT"
assert data["runner_exit_code"] == 0
assert data["child_returncode"] == 0
assert data["child_exit_code"] == 0
assert data["child_signal"] is None
assert data["termination"]["term_sent"] is False
assert data["termination"]["kill_sent"] is False
PY

[[ -s "$witness_file" ]] || fail 'WITNESS_MISSING'
[[ -s "$normal_file" ]] || fail 'NORMAL_FORM_MISSING'
[[ "$(grep -c '^PASS_K00_REES_SANDWICH_EXACT_MINIMAL_N$' "$stdout_file")" -eq 1 ]] || \
  fail 'PASS_ENDPOINT'
if grep -q '^K00_REES_FAIL=' "$stdout_file"; then
  fail 'PAYLOAD_FAIL_ENDPOINT'
fi
[[ "$(grep -Ec '^K00_REES_EXACT_SMALLEST_N=([5-9]|1[0-7])$' "$stdout_file")" -eq 1 ]] || \
  fail 'SMALLEST_N_ENDPOINT'

{
  printf 'witness_sha256=%s\n' "$(sha256sum "$witness_file" | awk '{print $1}')"
  printf 'normal_form_sha256=%s\n' "$(sha256sum "$normal_file" | awk '{print $1}')"
  printf 'lane_status=PASS\n'
} >>"$meta_file"
printf 'PASS_%s\n' "$EXPECTED_LANE"
