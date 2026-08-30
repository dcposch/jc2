#!/usr/bin/env bash
set -euo pipefail

readonly EXPECTED_LANE='K00-REES-SANDWICH-TRIANGULAR-REPLAY-R6B-20260829'
readonly EXPECTED_INSTANCE='i-0f089e64c378f5da3'
readonly EXPECTED_MANIFEST='99203ca9612a6a398f52de9370ffbc269c622a292c020c2ae74e34d06b7c0d44'
readonly META='K00-REES-SANDWICH-TRIANGULAR-REPLAY.meta'

fail() {
  printf 'RUNNER_FAIL=%s\n' "$1" >&2
  exit 125
}

validate_caprun_normal() {
  python3 - "$1" <<'PY'
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
}

# Return 40 for endpoint failure, 41 for a generic Singular diagnostic, and
# 42 for an explicit payload failure.  The exact same validator is used for
# the planted negative control and both evidence processes.
validate_singular_output() {
  local output=$1
  local endpoint=$2
  local pass_count
  pass_count=$(grep -Fxc "$endpoint" "$output" || true)
  [[ "$pass_count" -eq 1 ]] || return 40
  if grep -Eq '^[[:space:]]*\?|error occurred in or before|`[^`]+` is not defined|expected .*expression' "$output"; then
    return 41
  fi
  if grep -q '^K00_REES_FAIL=' "$output"; then
    return 42
  fi
  return 0
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

readonly NEG='K00-REES-REPLAY-UNDEFINED-REGRESSION'
readonly SEARCH='K00-REES-TRIANGULAR-EXACT-REPLAY'
readonly INITIAL='K00-REES-REPLAY-INITIAL-STRICTNESS'
for output in \
  "$META" \
  "$NEG.stdout" "$NEG.stderr" "$NEG.caprun.json" \
  "$SEARCH.stdout" "$SEARCH.stderr" "$SEARCH.caprun.json" \
  "$INITIAL.stdout" "$INITIAL.stderr" "$INITIAL.caprun.json" \
  WITNESS_MONOMIAL.poly WITNESS_NORMAL_FORM.poly; do
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
  printf 'negative_caps=30_wall_30_cpu_268435456_rss\n'
  printf 'search_caps=1800_wall_1800_cpu_34359738368_rss\n'
  printf 'initial_caps=120_wall_120_cpu_1073741824_rss\n'
} >"$META"

# The planted script has a fake PASS and a generic Singular diagnostic.  A
# zero child status is expected; validator status 41 is the required result.
set +e
python3 run_capped.py \
  --wall-seconds 30 --cpu-seconds 30 --rss-bytes 268435456 \
  --rss-sample-seconds 0.10 --term-grace-seconds 5 \
  --stdout-file "$NEG.stdout" --stderr-file "$NEG.stderr" \
  --telemetry-file "$NEG.caprun.json" --cwd "$run_dir" \
  -- /usr/bin/Singular -q undefined_symbol_regression.sing
negative_caprun_rc=$?
set -e
[[ "$negative_caprun_rc" -eq 0 ]] || fail 'NEGATIVE_CAPRUN_NONZERO'
validate_caprun_normal "$NEG.caprun.json" || fail 'NEGATIVE_CAPRUN_TELEMETRY'
set +e
validate_singular_output "$NEG.stdout" 'PASS_K00_REES_PLANTED_UNDEFINED_SYMBOL'
negative_validation_rc=$?
set -e
[[ "$negative_validation_rc" -eq 41 ]] || fail "NEGATIVE_VALIDATOR_RC_${negative_validation_rc}"
{
  printf 'negative_control_caprun_rc=%s\n' "$negative_caprun_rc"
  printf 'negative_control_validation_rc=%s\n' "$negative_validation_rc"
  printf 'negative_control_rejected=1\n'
  printf 'negative_stdout_sha256=%s\n' "$(sha256sum "$NEG.stdout" | awk '{print $1}')"
  printf 'negative_stderr_sha256=%s\n' "$(sha256sum "$NEG.stderr" | awk '{print $1}')"
  printf 'negative_telemetry_sha256=%s\n' "$(sha256sum "$NEG.caprun.json" | awk '{print $1}')"
} >>"$META"

set +e
python3 run_capped.py \
  --wall-seconds 1800 --cpu-seconds 1800 --rss-bytes 34359738368 \
  --rss-sample-seconds 0.10 --term-grace-seconds 5 \
  --stdout-file "$SEARCH.stdout" --stderr-file "$SEARCH.stderr" \
  --telemetry-file "$SEARCH.caprun.json" --cwd "$run_dir" \
  -- /usr/bin/Singular -q search_rees_sandwich.sing
search_caprun_rc=$?
set -e
[[ "$search_caprun_rc" -eq 0 ]] || fail 'SEARCH_CAPRUN_NONZERO'
validate_caprun_normal "$SEARCH.caprun.json" || fail 'SEARCH_CAPRUN_TELEMETRY'
validate_singular_output "$SEARCH.stdout" 'PASS_K00_REES_SANDWICH_EXACT_MINIMAL_N' || \
  fail 'SEARCH_OUTPUT_VALIDATION'
[[ -s WITNESS_MONOMIAL.poly ]] || fail 'WITNESS_MISSING'
[[ -s WITNESS_NORMAL_FORM.poly ]] || fail 'NORMAL_FORM_MISSING'
[[ "$(grep -Ec '^K00_REES_EXACT_SMALLEST_N=([5-9]|1[0-7])$' "$SEARCH.stdout")" -eq 1 ]] || \
  fail 'SMALLEST_N_ENDPOINT'
{
  printf 'search_caprun_rc=%s\n' "$search_caprun_rc"
  printf 'search_stdout_sha256=%s\n' "$(sha256sum "$SEARCH.stdout" | awk '{print $1}')"
  printf 'search_stderr_sha256=%s\n' "$(sha256sum "$SEARCH.stderr" | awk '{print $1}')"
  printf 'search_telemetry_sha256=%s\n' "$(sha256sum "$SEARCH.caprun.json" | awk '{print $1}')"
  printf 'witness_sha256=%s\n' "$(sha256sum WITNESS_MONOMIAL.poly | awk '{print $1}')"
  printf 'normal_form_sha256=%s\n' "$(sha256sum WITNESS_NORMAL_FORM.poly | awk '{print $1}')"
} >>"$META"

set +e
python3 run_capped.py \
  --wall-seconds 120 --cpu-seconds 120 --rss-bytes 1073741824 \
  --rss-sample-seconds 0.10 --term-grace-seconds 5 \
  --stdout-file "$INITIAL.stdout" --stderr-file "$INITIAL.stderr" \
  --telemetry-file "$INITIAL.caprun.json" --cwd "$run_dir" \
  -- /usr/bin/Singular -q initial_strictness.sing
initial_caprun_rc=$?
set -e
[[ "$initial_caprun_rc" -eq 0 ]] || fail 'INITIAL_CAPRUN_NONZERO'
validate_caprun_normal "$INITIAL.caprun.json" || fail 'INITIAL_CAPRUN_TELEMETRY'
validate_singular_output "$INITIAL.stdout" 'PASS_K00_REES_INITIAL_IDEAL_STRICTNESS' || \
  fail 'INITIAL_OUTPUT_VALIDATION'
{
  printf 'initial_caprun_rc=%s\n' "$initial_caprun_rc"
  printf 'initial_stdout_sha256=%s\n' "$(sha256sum "$INITIAL.stdout" | awk '{print $1}')"
  printf 'initial_stderr_sha256=%s\n' "$(sha256sum "$INITIAL.stderr" | awk '{print $1}')"
  printf 'initial_telemetry_sha256=%s\n' "$(sha256sum "$INITIAL.caprun.json" | awk '{print $1}')"
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'load_end=%s\n' "$(cut -d' ' -f1-3 /proc/loadavg)"
  printf 'memavailable_kib_end=%s\n' "$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)"
  printf 'lane_status=PASS\n'
} >>"$META"
printf 'PASS_%s\n' "$EXPECTED_LANE"
