#!/usr/bin/env bash
# Hardened AWS-only runner for the `(mu,r,D)=(2,2,8)` reconnaissance.
set -euo pipefail

if (( $# != 11 )); then
  echo "usage: $0 JOB_ROOT LANE_TAG EXPECTED_INSTANCE_ID CHARACTERISTIC PROFILE ENGINE MEMORY_KIB TIMEOUT_SECONDS EXPECTED_RUNNER_SHA256 EXPECTED_GENERATOR_SHA256 EXPECTED_GIT_BASIS" >&2
  exit 125
fi

readonly JOB_ROOT=$1
readonly LANE_TAG=$2
readonly EXPECTED_INSTANCE_ID=$3
readonly CHARACTERISTIC=$4
readonly PROFILE=$5
readonly ENGINE=$6
readonly MEMORY_KIB=$7
readonly TIMEOUT_SECONDS=$8
readonly EXPECTED_RUNNER_SHA=$9
readonly EXPECTED_GENERATOR_SHA=${10}
readonly EXPECTED_GIT_BASIS=${11}

if [[ ! "$LANE_TAG" =~ ^quartic_inv_mu2_d8_[A-Za-z0-9][A-Za-z0-9_-]{0,95}$ ]]; then
  echo "refusing malformed or unregistered lane tag: $LANE_TAG" >&2
  exit 125
fi
readonly LANE_SUFFIX=${LANE_TAG#quartic_inv_mu2_d8_}
readonly CANONICAL_JOB_ROOT=/home/ubuntu/jobs/quartic_inv_mu2_d8_$LANE_SUFFIX
[[ "$JOB_ROOT" == "$CANONICAL_JOB_ROOT" ]] || { echo "refusing noncanonical job root: $JOB_ROOT" >&2; exit 125; }
[[ "$EXPECTED_INSTANCE_ID" =~ ^i-[0-9a-f]+$ ]] || { echo "invalid expected EC2 instance id" >&2; exit 125; }
[[ "$CHARACTERISTIC" =~ ^(0|[1-9][0-9]{0,9})$ ]] || { echo "invalid characteristic" >&2; exit 125; }
case "$PROFILE" in actual|target3|drop_last) ;; *) echo "invalid profile" >&2; exit 125 ;; esac
case "$ENGINE" in std|slimgb) ;; *) echo "invalid engine" >&2; exit 125 ;; esac
if [[ ! "$MEMORY_KIB" =~ ^[1-9][0-9]{6,9}$ ]] || (( MEMORY_KIB < 4194304 || MEMORY_KIB > 1000000000 )); then
  echo "memory cap must lie between 4 GiB and 1 TB in KiB units" >&2
  exit 125
fi
if [[ ! "$TIMEOUT_SECONDS" =~ ^[1-9][0-9]{1,5}$ ]] || (( TIMEOUT_SECONDS < 60 || TIMEOUT_SECONDS > 43200 )); then
  echo "timeout must lie between 60 and 43200 seconds" >&2
  exit 125
fi
for digest in "$EXPECTED_RUNNER_SHA" "$EXPECTED_GENERATOR_SHA"; do
  [[ "$digest" =~ ^[0-9a-f]{64}$ ]] || { echo "invalid expected SHA-256" >&2; exit 125; }
done
[[ "$EXPECTED_GIT_BASIS" =~ ^[0-9a-f]{40}$ ]] || { echo "invalid expected git basis" >&2; exit 125; }

[[ "$(uname -s)" == Linux ]] || { echo "refusing heavy lane outside Linux" >&2; exit 125; }
readonly AWS_VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
readonly INSTANCE_ID=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag 2>/dev/null || true)
if [[ "$AWS_VENDOR" != "Amazon EC2" || "$INSTANCE_ID" != "$EXPECTED_INSTANCE_ID" ]]; then
  echo "AWS identity mismatch: vendor=${AWS_VENDOR:-unknown} instance=${INSTANCE_ID:-unknown}" >&2
  exit 125
fi

MEMTOTAL_KIB=
while read -r key value unit; do
  if [[ "$key" == "MemTotal:" ]]; then MEMTOTAL_KIB=$value; break; fi
done < /proc/meminfo
readonly MEMTOTAL_KIB
if [[ ! "$MEMTOTAL_KIB" =~ ^[1-9][0-9]+$ ]] || (( MEMORY_KIB > MEMTOTAL_KIB * 80 / 100 )); then
  echo "memory cap unavailable or exceeds 80 percent of host RAM" >&2
  exit 125
fi

readonly SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
readonly SOURCE_GENERATOR=$SCRIPT_DIR/generate_mu2_d8.py
[[ -f "$SOURCE_GENERATOR" && ! -L "$SOURCE_GENERATOR" ]] || { echo "missing regular generator" >&2; exit 125; }
readonly OBSERVED_RUNNER_SHA=$(sha256sum "$0" | cut -d ' ' -f 1)
readonly OBSERVED_GENERATOR_SHA=$(sha256sum "$SOURCE_GENERATOR" | cut -d ' ' -f 1)
if [[ "$OBSERVED_RUNNER_SHA" != "$EXPECTED_RUNNER_SHA" || "$OBSERVED_GENERATOR_SHA" != "$EXPECTED_GENERATOR_SHA" ]]; then
  echo "runner or generator hash mismatch" >&2
  exit 125
fi

command -v /usr/bin/python3 >/dev/null
command -v /usr/bin/Singular >/dev/null
command -v /usr/bin/timeout >/dev/null
command -v /usr/bin/time >/dev/null
/usr/bin/python3 -c 'import sympy' >/dev/null 2>&1 || { echo "SymPy import failed" >&2; exit 125; }

umask 077
mkdir -- "$JOB_ROOT"
readonly PAYLOAD=$JOB_ROOT/payload
readonly RUN=$JOB_ROOT/run
mkdir -- "$PAYLOAD" "$RUN"
cp "$0" "$PAYLOAD/aws_mu2_d8_run.sh"
cp "$SOURCE_GENERATOR" "$PAYLOAD/generate_mu2_d8.py"
readonly GENERATOR=$PAYLOAD/generate_mu2_d8.py
readonly INPUT=$RUN/input.sing
readonly GENERATOR_STDERR=$RUN/generator.stderr
readonly RESULT=$RUN/result.stdout
readonly STDERR=$RUN/singular.stderr
readonly META=$RUN/run.meta
readonly LANES=$RUN/lanes.log
readonly EVIDENCE=$JOB_ROOT/EVIDENCE.sha256
readonly START_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)

{
  printf 'schema=JC2_QUARTIC_INVARIANT_MU2_D8_AWS_RUN_V1\n'
  printf 'lane=%s\n' "$LANE_TAG"
  printf 'orchestrator_pid=%s\n' "$$"
  printf 'hostname=%s\n' "$(hostname)"
  printf 'aws_vendor=%s\n' "$AWS_VENDOR"
  printf 'instance_id=%s\n' "$INSTANCE_ID"
  printf 'instance_type=%s\n' "$(tr -d '\n' < /sys/class/dmi/id/product_name 2>/dev/null || echo UNKNOWN)"
  printf 'start_utc=%s\n' "$START_UTC"
  printf 'cpu_count=%s\n' "$(nproc)"
  printf 'memtotal_kib=%s\n' "$MEMTOTAL_KIB"
  printf 'memory_limit_kib=%s\n' "$MEMORY_KIB"
  printf 'timeout_seconds=%s\n' "$TIMEOUT_SECONDS"
  printf 'characteristic=%s\n' "$CHARACTERISTIC"
  printf 'profile=%s\n' "$PROFILE"
  printf 'engine=%s\n' "$ENGINE"
  printf 'runner_sha256=%s\n' "$OBSERVED_RUNNER_SHA"
  printf 'generator_sha256=%s\n' "$OBSERVED_GENERATOR_SHA"
  printf 'git_basis=%s\n' "$EXPECTED_GIT_BASIS"
  printf 'python=%s\n' "$(/usr/bin/python3 --version 2>&1)"
  printf 'sympy=%s\n' "$(/usr/bin/python3 -c 'import sympy; print(sympy.__version__)')"
  printf 'singular=%s\n' "$(/usr/bin/Singular --version | head -1)"
} > "$META"

ulimit -v "$MEMORY_KIB"
export PYTHONHASHSEED=0
export LC_ALL=C
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MALLOC_ARENA_MAX=4
export JC2_QUARTIC_INVARIANT_ROUTE_TOKEN=$LANE_TAG

set +e
/usr/bin/timeout --signal=TERM --kill-after=30 600 \
  /usr/bin/python3 "$GENERATOR" \
    --characteristic "$CHARACTERISTIC" --profile "$PROFILE" --engine "$ENGINE" \
    > "$INPUT" 2> "$GENERATOR_STDERR"
GENERATOR_RC=$?
set -e
if (( GENERATOR_RC != 0 )) || [[ -s "$GENERATOR_STDERR" ]] || [[ ! -s "$INPUT" ]]; then
  {
    printf 'generator_rc=%s\n' "$GENERATOR_RC"
    printf 'final_state=FAILED_CLOSED_GENERATOR\n'
    printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  } >> "$META"
  (cd "$JOB_ROOT" && find payload run -type f -print0 | sort -z | xargs -0 sha256sum) > "$EVIDENCE"
  exit 126
fi
printf 'input_sha256=%s\n' "$(sha256sum "$INPUT" | cut -d ' ' -f 1)" >> "$META"

set +e
/usr/bin/timeout --signal=TERM --kill-after=60 "$TIMEOUT_SECONDS" \
  /usr/bin/time -v nice -n 5 /usr/bin/Singular -q "$INPUT" \
  > "$RESULT" 2> "$STDERR"
RC=$?
set -e

{
  printf 'rc=%s\n' "$RC"
  printf 'result_sha256=%s\n' "$(sha256sum "$RESULT" | cut -d ' ' -f 1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$STDERR" | cut -d ' ' -f 1)"
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  if (( RC == 0 )); then
    printf 'final_state=DONE\n'
  elif (( RC == 124 || RC == 137 )); then
    printf 'final_state=TIMEOUT_OR_CAP\n'
  else
    printf 'final_state=FAILED\n'
  fi
} >> "$META"
printf '%s lane=%s rc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$LANE_TAG" "$RC" > "$LANES"
(cd "$JOB_ROOT" && find payload run -type f -print0 | sort -z | xargs -0 sha256sum) > "$EVIDENCE"
exit "$RC"
