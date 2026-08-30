#!/usr/bin/env bash
# Hardened AWS-only screening runner (v2) for the D3 clean-infinity HB jet packet.
set -euo pipefail

if (( $# != 10 )); then
  echo "usage: $0 JOB_ROOT LANE_TAG EXPECTED_INSTANCE_ID PRIME JET_ORDER ENGINE MEMORY_KIB TIMEOUT_SECONDS EXPECTED_RUNNER_SHA256 EXPECTED_GENERATOR_SHA256" >&2
  exit 125
fi

readonly D3_JOB_ROOT=$1
readonly D3_LANE_TAG=$2
readonly D3_EXPECTED_INSTANCE_ID=$3
readonly D3_PRIME=$4
readonly D3_JET_ORDER=$5
readonly D3_ENGINE=$6
readonly D3_MEMORY_KIB=$7
readonly D3_TIMEOUT_SECONDS=$8
readonly D3_EXPECTED_RUNNER_SHA=$9
readonly D3_EXPECTED_GENERATOR_SHA=${10}
readonly D3_EXPECTED_SELFTEST_STDOUT_SHA=fc80bb406ce8755af035adf86bd7100e14c74f541db27764aaa924ef01412061
readonly D3_MEMORY_FRACTION_PERCENT=85

if [[ ! "$D3_LANE_TAG" =~ ^d3_clean_hb_[A-Za-z0-9][A-Za-z0-9_-]{0,95}$ ]]; then
  echo "refusing malformed or unregistered lane tag: $D3_LANE_TAG" >&2
  exit 125
fi
readonly D3_LANE_SUFFIX=${D3_LANE_TAG#d3_clean_hb_}
readonly D3_CANONICAL_JOB_ROOT=/home/ubuntu/jobs/d3_one_support_clean_hb_$D3_LANE_SUFFIX
if [[ "$D3_JOB_ROOT" != "$D3_CANONICAL_JOB_ROOT" ]]; then
  echo "refusing noncanonical job root: $D3_JOB_ROOT" >&2
  exit 125
fi
if [[ ! "$D3_EXPECTED_INSTANCE_ID" =~ ^i-[0-9a-f]+$ ]]; then
  echo "invalid expected EC2 instance id" >&2
  exit 125
fi
if [[ ! "$D3_PRIME" =~ ^(0|[1-9][0-9]{0,9})$ ]]; then
  echo "invalid characteristic" >&2
  exit 125
fi
if [[ ! "$D3_JET_ORDER" =~ ^[1-9][0-9]?$ ]]; then
  echo "invalid jet order" >&2
  exit 125
fi
case "$D3_ENGINE" in std|slimgb) ;; *) echo "invalid engine" >&2; exit 125 ;; esac
if [[ ! "$D3_MEMORY_KIB" =~ ^[1-9][0-9]{0,9}$ ]]; then
  echo "invalid memory limit" >&2
  exit 125
fi
if [[ ! "$D3_TIMEOUT_SECONDS" =~ ^[1-9][0-9]{0,5}$ ]]; then
  echo "invalid timeout" >&2
  exit 125
fi
if [[ ! "$D3_EXPECTED_RUNNER_SHA" =~ ^[0-9a-f]{64}$ ]]; then
  echo "invalid expected runner SHA-256" >&2
  exit 125
fi
if [[ ! "$D3_EXPECTED_GENERATOR_SHA" =~ ^[0-9a-f]{64}$ ]]; then
  echo "invalid expected generator SHA-256" >&2
  exit 125
fi
if (( D3_JET_ORDER < 2 || D3_JET_ORDER > 27 )); then
  echo "jet order must lie in [2,27]" >&2
  exit 125
fi
if (( D3_MEMORY_KIB < 4194304 || D3_MEMORY_KIB > 1000000000 )); then
  echo "memory cap must lie between 4 GiB and 1 TB in KiB units" >&2
  exit 125
fi
if (( D3_TIMEOUT_SECONDS < 60 || D3_TIMEOUT_SECONDS > 43200 )); then
  echo "timeout must lie between 60 and 43200 seconds" >&2
  exit 125
fi

if [[ "$(uname -s)" != Linux ]]; then
  echo "refusing heavy lane outside Linux" >&2
  exit 125
fi
readonly D3_AWS_VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
readonly D3_INSTANCE_ID=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag 2>/dev/null || true)
if [[ "$D3_AWS_VENDOR" != "Amazon EC2" || "$D3_INSTANCE_ID" != "$D3_EXPECTED_INSTANCE_ID" ]]; then
  echo "AWS identity mismatch: vendor=${D3_AWS_VENDOR:-unknown} instance=${D3_INSTANCE_ID:-unknown}" >&2
  exit 125
fi

D3_MEMTOTAL_KIB=
while read -r D3_MEM_KEY D3_MEM_VALUE D3_MEM_UNIT; do
  if [[ "$D3_MEM_KEY" == "MemTotal:" ]]; then
    D3_MEMTOTAL_KIB=$D3_MEM_VALUE
    break
  fi
done < /proc/meminfo
readonly D3_MEMTOTAL_KIB
if [[ ! "$D3_MEMTOTAL_KIB" =~ ^[1-9][0-9]+$ ]]; then
  echo "cannot determine MemTotal from /proc/meminfo" >&2
  exit 125
fi
readonly D3_MAX_MEMORY_KIB=$((D3_MEMTOTAL_KIB * D3_MEMORY_FRACTION_PERCENT / 100))
if (( D3_MEMORY_KIB > D3_MAX_MEMORY_KIB )); then
  echo "memory cap exceeds ${D3_MEMORY_FRACTION_PERCENT}% of MemTotal: cap=$D3_MEMORY_KIB max=$D3_MAX_MEMORY_KIB total=$D3_MEMTOTAL_KIB" >&2
  exit 125
fi

readonly D3_SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
readonly D3_SOURCE_GENERATOR=$D3_SCRIPT_DIR/d3_one_support_clean_hb_generate.py
[[ -f "$D3_SOURCE_GENERATOR" ]] || { echo "missing generator: $D3_SOURCE_GENERATOR" >&2; exit 125; }
readonly D3_OBSERVED_RUNNER_SHA=$(sha256sum "$0" | cut -d ' ' -f 1)
if [[ "$D3_OBSERVED_RUNNER_SHA" != "$D3_EXPECTED_RUNNER_SHA" ]]; then
  echo "runner hash mismatch: expected=$D3_EXPECTED_RUNNER_SHA observed=$D3_OBSERVED_RUNNER_SHA" >&2
  exit 125
fi
readonly D3_OBSERVED_GENERATOR_SHA=$(sha256sum "$D3_SOURCE_GENERATOR" | cut -d ' ' -f 1)
if [[ "$D3_OBSERVED_GENERATOR_SHA" != "$D3_EXPECTED_GENERATOR_SHA" ]]; then
  echo "generator hash mismatch: expected=$D3_EXPECTED_GENERATOR_SHA observed=$D3_OBSERVED_GENERATOR_SHA" >&2
  exit 125
fi
command -v /usr/bin/python3 >/dev/null
command -v /usr/bin/Singular >/dev/null
command -v /usr/bin/timeout >/dev/null
command -v /usr/bin/time >/dev/null
/usr/bin/python3 -c 'import sympy' >/dev/null 2>&1 || {
  echo "SymPy import failed" >&2
  exit 125
}

umask 077
if ! mkdir -- "$D3_JOB_ROOT"; then
  echo "refusing reused or unavailable job root: $D3_JOB_ROOT" >&2
  exit 125
fi
readonly D3_PAYLOAD=$D3_JOB_ROOT/payload
readonly D3_RUN=$D3_JOB_ROOT/run
mkdir -- "$D3_PAYLOAD" "$D3_RUN"
cp "$0" "$D3_PAYLOAD/aws_d3_one_support_clean_hb_run.sh"
cp "$D3_SOURCE_GENERATOR" "$D3_PAYLOAD/d3_one_support_clean_hb_generate.py"
readonly D3_GENERATOR=$D3_PAYLOAD/d3_one_support_clean_hb_generate.py
readonly D3_INPUT=$D3_RUN/input.sing
readonly D3_GENERATOR_STDERR=$D3_RUN/generator.stderr
readonly D3_SELFTEST_STDOUT=$D3_RUN/selftest.stdout
readonly D3_SELFTEST_STDERR=$D3_RUN/selftest.stderr
readonly D3_RESULT=$D3_RUN/result.stdout
readonly D3_STDERR=$D3_RUN/singular.stderr
readonly D3_META=$D3_RUN/run.meta
readonly D3_LANES=$D3_RUN/lanes.log
readonly D3_EVIDENCE=$D3_JOB_ROOT/EVIDENCE.sha256
readonly D3_ROUTE_TOKEN=$D3_LANE_TAG

: > "$D3_INPUT"
: > "$D3_GENERATOR_STDERR"
: > "$D3_SELFTEST_STDOUT"
: > "$D3_SELFTEST_STDERR"
: > "$D3_RESULT"
: > "$D3_STDERR"

readonly D3_RUNNER_SHA=$(sha256sum "$D3_PAYLOAD/aws_d3_one_support_clean_hb_run.sh" | cut -d ' ' -f 1)
if [[ "$D3_RUNNER_SHA" != "$D3_OBSERVED_RUNNER_SHA" ]]; then
  echo "runner copy hash drift: source=$D3_OBSERVED_RUNNER_SHA copy=$D3_RUNNER_SHA" >&2
  exit 125
fi
readonly D3_PYTHON_SHA=$(sha256sum /usr/bin/python3 | cut -d ' ' -f 1)
readonly D3_ROUTE_TOKEN_SHA=$(printf '%s' "$D3_ROUTE_TOKEN" | sha256sum | cut -d ' ' -f 1)
readonly D3_START_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)

{
  printf 'schema=D3_ONE_SUPPORT_CLEAN_HB_AWS_RUN_V2\n'
  printf 'lane=%s\n' "$D3_LANE_TAG"
  printf 'orchestrator_pid=%s\n' "$$"
  printf 'hostname=%s\n' "$(hostname)"
  printf 'aws_vendor=%s\n' "$D3_AWS_VENDOR"
  printf 'instance_id=%s\n' "$D3_INSTANCE_ID"
  printf 'instance_type=%s\n' "$(tr -d '\n' < /sys/class/dmi/id/product_name 2>/dev/null || echo UNKNOWN)"
  printf 'start_utc=%s\n' "$D3_START_UTC"
  printf 'cpu_count=%s\n' "$(nproc)"
  printf 'memtotal_kib=%s\n' "$D3_MEMTOTAL_KIB"
  printf 'memory_fraction_limit_percent=%s\n' "$D3_MEMORY_FRACTION_PERCENT"
  printf 'max_memory_kib=%s\n' "$D3_MAX_MEMORY_KIB"
  printf 'memory_limit_kib=%s\n' "$D3_MEMORY_KIB"
  printf 'timeout_seconds=%s\n' "$D3_TIMEOUT_SECONDS"
  printf 'generator_timeout_seconds=7200\n'
  printf 'prime=%s\n' "$D3_PRIME"
  printf 'jet_order=%s\n' "$D3_JET_ORDER"
  printf 'engine=%s\n' "$D3_ENGINE"
  printf 'expected_runner_sha256=%s\n' "$D3_EXPECTED_RUNNER_SHA"
  printf 'runner_sha256=%s\n' "$D3_RUNNER_SHA"
  printf 'expected_generator_sha256=%s\n' "$D3_EXPECTED_GENERATOR_SHA"
  printf 'generator_sha256=%s\n' "$D3_OBSERVED_GENERATOR_SHA"
  printf 'expected_selftest_stdout_sha256=%s\n' "$D3_EXPECTED_SELFTEST_STDOUT_SHA"
  printf 'route_token_sha256=%s\n' "$D3_ROUTE_TOKEN_SHA"
  printf 'python=%s\n' "$(/usr/bin/python3 --version 2>&1)"
  printf 'python_sha256=%s\n' "$D3_PYTHON_SHA"
  printf 'sympy=%s\n' "$(/usr/bin/python3 -c 'import sympy; print(sympy.__version__)')"
  printf 'singular=%s\n' "$(/usr/bin/Singular --version | head -1)"
} > "$D3_META"

ulimit -v "$D3_MEMORY_KIB"
export PYTHONHASHSEED=0
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MALLOC_ARENA_MAX=4
unset PYTHONOPTIMIZE

set +e
/usr/bin/timeout --signal=TERM --kill-after=60 120 \
  /usr/bin/python3 "$D3_GENERATOR" --self-test \
  > "$D3_SELFTEST_STDOUT" 2> "$D3_SELFTEST_STDERR"
D3_SELFTEST_RC=$?
set -e
readonly D3_SELFTEST_STDOUT_SHA=$(sha256sum "$D3_SELFTEST_STDOUT" | cut -d ' ' -f 1)
readonly D3_SELFTEST_STDERR_SHA=$(sha256sum "$D3_SELFTEST_STDERR" | cut -d ' ' -f 1)
if [[ "$D3_SELFTEST_RC" != 0 ]] || \
   [[ "$D3_SELFTEST_STDOUT_SHA" != "$D3_EXPECTED_SELFTEST_STDOUT_SHA" ]] || \
   [[ -s "$D3_SELFTEST_STDERR" ]]; then
  {
    printf 'selftest_rc=%s\n' "$D3_SELFTEST_RC"
    printf 'selftest_stdout_sha256=%s\n' "$D3_SELFTEST_STDOUT_SHA"
    printf 'selftest_stderr_sha256=%s\n' "$D3_SELFTEST_STDERR_SHA"
    printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'final_state=FAILED_CLOSED_SELFTEST\n'
  } >> "$D3_META"
  printf '%s lane=%s rc=126 state=FAILED_CLOSED_SELFTEST\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$D3_LANE_TAG" > "$D3_LANES"
  (cd "$D3_JOB_ROOT" && find payload run -type f -print0 | sort -z | xargs -0 sha256sum) > "$D3_EVIDENCE"
  exit 126
fi

set +e
export D3_ONE_SUPPORT_CLEAN_HB_ROUTE_TOKEN=$D3_ROUTE_TOKEN
/usr/bin/timeout --signal=TERM --kill-after=60 7200 \
  /usr/bin/python3 "$D3_GENERATOR" \
    --prime "$D3_PRIME" --jet-order "$D3_JET_ORDER" --engine "$D3_ENGINE" \
  > "$D3_INPUT" 2> "$D3_GENERATOR_STDERR"
D3_GENERATOR_RC=$?
unset D3_ONE_SUPPORT_CLEAN_HB_ROUTE_TOKEN
set -e
{
  printf 'selftest_rc=%s\n' "$D3_SELFTEST_RC"
  printf 'selftest_stdout_sha256=%s\n' "$D3_SELFTEST_STDOUT_SHA"
  printf 'selftest_stderr_sha256=%s\n' "$D3_SELFTEST_STDERR_SHA"
  printf 'generator_rc=%s\n' "$D3_GENERATOR_RC"
  printf 'generator_stderr_sha256=%s\n' "$(sha256sum "$D3_GENERATOR_STDERR" | cut -d ' ' -f 1)"
  printf 'input_sha256=%s\n' "$(sha256sum "$D3_INPUT" | cut -d ' ' -f 1)"
  printf 'input_bytes=%s\n' "$(wc -c < "$D3_INPUT" | tr -d ' ')"
} >> "$D3_META"
if [[ "$D3_GENERATOR_RC" != 0 ]] || [[ ! -s "$D3_INPUT" ]]; then
  {
    printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'final_state=FAILED_CLOSED_GENERATOR\n'
  } >> "$D3_META"
  printf '%s lane=%s rc=126 state=FAILED_CLOSED_GENERATOR\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$D3_LANE_TAG" > "$D3_LANES"
  (cd "$D3_JOB_ROOT" && find payload run -type f -print0 | sort -z | xargs -0 sha256sum) > "$D3_EVIDENCE"
  exit 126
fi

set +e
/usr/bin/timeout --signal=TERM --kill-after=300 "$D3_TIMEOUT_SECONDS" \
  /usr/bin/time -v /usr/bin/nice -n 5 /usr/bin/Singular -q \
  < "$D3_INPUT" > "$D3_RESULT" 2> "$D3_STDERR"
D3_SINGULAR_RC=$?
set -e

D3_VALIDATED_RC=$D3_SINGULAR_RC
D3_VERDICT=NONE
if [[ "$D3_SINGULAR_RC" == 0 ]]; then
  if ! grep -Fqx 'D3_CLEAN_HB_CONTROL_UNIT=PASS' "$D3_RESULT" || \
     ! grep -Fqx 'D3_CLEAN_HB_CONTROL_PROPER=PASS' "$D3_RESULT" || \
     ! grep -Eq '^D3_CLEAN_HB_BASIS_SIZE=[0-9]+$' "$D3_RESULT" || \
     ! grep -Eq '^D3_CLEAN_HB_BASIS_DIM=-?[0-9]+$' "$D3_RESULT"; then
    D3_VALIDATED_RC=126
  elif [[ "$(grep -Ec '^D3_CLEAN_HB_SCREEN=(UNIT|NONUNIT)$' "$D3_RESULT")" != 1 ]]; then
    D3_VALIDATED_RC=126
  else
    D3_VERDICT=$(grep -E '^D3_CLEAN_HB_SCREEN=(UNIT|NONUNIT)$' "$D3_RESULT" | cut -d= -f2)
  fi
fi

if [[ "$D3_VALIDATED_RC" == 0 ]]; then
  if [[ "$D3_PRIME" == 0 && "$D3_VERDICT" == UNIT ]]; then
    D3_FINAL_STATE=EXACT_SCREEN_UNIT_CERTIFICATE_REQUIRED
  elif [[ "$D3_PRIME" == 0 && "$D3_VERDICT" == NONUNIT ]]; then
    D3_FINAL_STATE=EXACT_SCREEN_NONUNIT
  elif [[ "$D3_VERDICT" == UNIT ]]; then
    D3_FINAL_STATE=MODULAR_SCREEN_UNIT
  else
    D3_FINAL_STATE=MODULAR_SCREEN_NONUNIT
  fi
else
  D3_FINAL_STATE=FAILED_CLOSED_OR_INCONCLUSIVE
fi

{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'singular_rc=%s\n' "$D3_SINGULAR_RC"
  printf 'validated_rc=%s\n' "$D3_VALIDATED_RC"
  printf 'screen_verdict=%s\n' "$D3_VERDICT"
  printf 'result_sha256=%s\n' "$(sha256sum "$D3_RESULT" | cut -d ' ' -f 1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$D3_STDERR" | cut -d ' ' -f 1)"
  printf 'final_state=%s\n' "$D3_FINAL_STATE"
} >> "$D3_META"
printf '%s lane=%s rc=%s state=%s\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$D3_LANE_TAG" "$D3_VALIDATED_RC" "$D3_FINAL_STATE" \
  > "$D3_LANES"
(
  cd "$D3_JOB_ROOT"
  find payload run -type f -print0 | sort -z | xargs -0 sha256sum
) > "$D3_EVIDENCE"
exit "$D3_VALIDATED_RC"
