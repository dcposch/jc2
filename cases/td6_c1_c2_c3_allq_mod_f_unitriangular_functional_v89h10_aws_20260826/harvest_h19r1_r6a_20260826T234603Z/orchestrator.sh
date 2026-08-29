#!/usr/bin/env bash
set -euo pipefail

if (( $# != 4 )); then
  echo "usage: $0 JOB_ROOT HOST_LABEL PYTHON_BIN EXPECTED_INSTANCE_ID" >&2
  exit 125
fi

JOB_ROOT=$1
HOST_LABEL=$2
PYTHON_BIN=$3
EXPECTED_INSTANCE_ID=$4
PAYLOAD="$JOB_ROOT/payload"

case "$JOB_ROOT" in
  /home/ubuntu/jobs/td6_coordinate12_h19_*) ;;
  *) echo "refusing unregistered job root: $JOB_ROOT" >&2; exit 125 ;;
esac
case "$HOST_LABEL" in
  r6a|r6b) ;;
  *) echo "refusing unknown host label: $HOST_LABEL" >&2; exit 125 ;;
esac

if [[ "$(uname -s)" != Linux ]]; then
  echo "refusing non-Linux host" >&2
  exit 125
fi
AWS_VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
INSTANCE_ID=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag 2>/dev/null || true)
if [[ "$AWS_VENDOR" != "Amazon EC2" || "$INSTANCE_ID" != "$EXPECTED_INSTANCE_ID" ]]; then
  echo "AWS identity mismatch: vendor=$AWS_VENDOR instance=$INSTANCE_ID" >&2
  exit 125
fi
if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "missing Python executable: $PYTHON_BIN" >&2
  exit 125
fi
FLINT_VERSION=$(
  "$PYTHON_BIN" -c 'import flint; print(flint.__version__)' 2>/dev/null
) || { echo "python-flint import failed" >&2; exit 125; }
if [[ "$FLINT_VERSION" != 0.9.0 ]]; then
  echo "python-flint version mismatch: $FLINT_VERSION" >&2
  exit 125
fi
FLINT_MODULE=$("$PYTHON_BIN" -c 'import flint.pyflint as p; print(p.__file__)')
FLINT_MODULE_SHA=$(sha256sum "$FLINT_MODULE" | cut -d ' ' -f 1)
EXPECTED_FLINT_MODULE_SHA=1f7ef1f52024937f542772ff9190e2f74449228cd69a6746b6608fbbd449d138
if [[ "$FLINT_MODULE_SHA" != "$EXPECTED_FLINT_MODULE_SHA" ]]; then
  echo "python-flint module hash mismatch: $FLINT_MODULE_SHA" >&2
  exit 125
fi

H15_ARCHIVE_SHA=2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81
H19_PREREG_SHA=c578f6124f41fe69fa94be4b9cb02c56353b294f57d37a0c862d39405b1d836e
H19_REPLAY_SHA=7919aa9d3a769e456abadd54eea12008b0a9121760b8382bbf8bdc72b3ec1784
H19_RUNNER_SHA=11d3c15d39e6a0155b74f46eb7e8abcfe9d4e4fc84bac6954e2206e34eb0e9f4
H19_ERRATUM_SHA=27d8289d7215d16806d1f1197b137acc7d49b0d75a05c766833eaaa38db44418
H19_MANIFEST_SHA=a60d6fdb1e503caad7861cf1acd7ebc22a39eaac3ae53f1e1499514937f9c7d5

verify_file() {
  local expected=$1
  local path=$2
  local observed
  [[ -f "$path" ]] || { echo "missing payload: $path" >&2; exit 125; }
  observed=$(sha256sum "$path" | cut -d ' ' -f 1)
  if [[ "$observed" != "$expected" ]]; then
    echo "payload hash mismatch: $path expected=$expected observed=$observed" >&2
    exit 125
  fi
}

verify_file "$H15_ARCHIVE_SHA" "$PAYLOAD/source_p13_full_normal_form.tar.gz"
verify_file "$H19_PREREG_SHA" "$PAYLOAD/h19/PREREGISTRATION_RAW_P13_COORDINATE12_AUDIT_R1.md"
verify_file "$H19_REPLAY_SHA" "$PAYLOAD/h19/replay_v89h19r1_raw_p13_coordinate12_audit.py"
verify_file "$H19_RUNNER_SHA" "$PAYLOAD/h19/run_v89h19r1_raw_p13_coordinate12_audit.sh"
verify_file "$H19_ERRATUM_SHA" "$PAYLOAD/h19/P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md"
verify_file "$H19_MANIFEST_SHA" "$PAYLOAD/h19/SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256"

SOURCE_ROOT="$JOB_ROOT/source_root"
SOURCE="$SOURCE_ROOT/source"
RUN="$JOB_ROOT/run"
OUTPUT="$JOB_ROOT/output"
if [[ -e "$SOURCE_ROOT" || -e "$RUN" || -e "$OUTPUT" ]]; then
  echo "refusing reused job root: $JOB_ROOT" >&2
  exit 125
fi
mkdir -p "$SOURCE_ROOT" "$RUN" "$OUTPUT"
tar -xzf "$PAYLOAD/source_p13_full_normal_form.tar.gz" -C "$SOURCE_ROOT"
cp "$PAYLOAD/h19/PREREGISTRATION_RAW_P13_COORDINATE12_AUDIT_R1.md" "$SOURCE/"
cp "$PAYLOAD/h19/replay_v89h19r1_raw_p13_coordinate12_audit.py" "$SOURCE/"
cp "$PAYLOAD/h19/run_v89h19r1_raw_p13_coordinate12_audit.sh" "$SOURCE/"
cp "$PAYLOAD/h19/P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md" "$SOURCE/"
cp "$PAYLOAD/h19/SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256" "$SOURCE/"

(cd "$SOURCE" && sha256sum -c SOURCE_P13_FULL_NORMAL_FORM.sha256) \
  > "$RUN/h15_source_check.stdout" 2> "$RUN/h15_source_check.stderr"
(cd "$SOURCE" && sha256sum -c SOURCE_P12_FULL_NORMAL_FORM.sha256) \
  > "$RUN/h12_source_check.stdout" 2> "$RUN/h12_source_check.stderr"
(cd "$SOURCE" && sha256sum -c SOURCE_P12_FLAG.sha256) \
  > "$RUN/h11_source_check.stdout" 2> "$RUN/h11_source_check.stderr"
(cd "$SOURCE" && sha256sum -c PAYLOAD_CLOSURE.sha256) \
  > "$RUN/payload_closure_check.stdout" 2> "$RUN/payload_closure_check.stderr"
(cd "$SOURCE" && sha256sum -c SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256) \
  > "$RUN/h19_source_check.stdout" 2> "$RUN/h19_source_check.stderr"

STAMP=$(date -u +%Y%m%dT%H%M%SZ)
TAG="td6_v89h19r1_raw_p13_c12_${STAMP}_${HOST_LABEL}"
META="$RUN/$TAG.meta"
STDOUT="$RUN/$TAG.stdout"
STDERR="$RUN/$TAG.stderr"
unset PYTHONOPTIMIZE
PYTHON_OPTIMIZE=$("$PYTHON_BIN" -c 'import sys; print(sys.flags.optimize)')
if [[ "$PYTHON_OPTIMIZE" != 0 ]]; then
  echo "Python assertions are disabled: optimize=$PYTHON_OPTIMIZE" >&2
  exit 125
fi

{
  printf 'lane=%s\n' "$TAG"
  printf 'orchestrator_pid=%s\n' "$$"
  printf 'host_label=%s\n' "$HOST_LABEL"
  printf 'hostname=%s\n' "$(hostname)"
  printf 'instance_id=%s\n' "$INSTANCE_ID"
  printf 'instance_type=%s\n' "$(tr -d '\n' < /sys/class/dmi/id/product_name)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'cpu_count=%s\n' "$(nproc)"
  printf 'memory_limit_kib=450000000\n'
  printf 'timeout_seconds=43200\n'
  printf 'python=%s\n' "$PYTHON_BIN"
  printf 'python_version=%s\n' "$($PYTHON_BIN --version 2>&1)"
  printf 'python_sha256=%s\n' "$(sha256sum "$PYTHON_BIN" | cut -d ' ' -f 1)"
  printf 'python_optimize=%s\n' "$PYTHON_OPTIMIZE"
  printf 'python_flint=%s\n' "$FLINT_VERSION"
  printf 'python_packages=%s\n' "$($PYTHON_BIN -m pip freeze | sort | tr '\n' ',')"
  printf 'h15_archive_sha256=%s\n' "$H15_ARCHIVE_SHA"
  printf 'h19_preregistration_sha256=%s\n' "$H19_PREREG_SHA"
  printf 'h19_replay_sha256=%s\n' "$H19_REPLAY_SHA"
  printf 'h19_runner_sha256=%s\n' "$H19_RUNNER_SHA"
  printf 'h19_erratum_sha256=%s\n' "$H19_ERRATUM_SHA"
  printf 'h19_manifest_sha256=%s\n' "$H19_MANIFEST_SHA"
  printf 'python_flint_module=%s\n' "$FLINT_MODULE"
  printf 'python_flint_module_sha256=%s\n' "$FLINT_MODULE_SHA"
} > "$META"

ulimit -v 450000000
export PYTHONHASHSEED=0
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MALLOC_ARENA_MAX=4
export PATH="$(dirname "$PYTHON_BIN"):/usr/bin:/bin"

if (
  cd "$SOURCE"
  AWS_RUN_TAG="$TAG" TD6_OUTPUT_DIR="$OUTPUT" \
    TD6_Q_EXPONENT=2 TD6_Q_SCOPE=q2-q14-q16-q24 \
    TD6_PIVOT_POLICY=ascending TD6_PIVOT_SCOPE=all-staged \
    TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U \
    /usr/bin/timeout --signal=TERM --kill-after=60 43200 \
    /usr/bin/time -v bash run_v89h19r1_raw_p13_coordinate12_audit.sh
) > "$STDOUT" 2> "$STDERR"; then
  RC=0
else
  RC=$?
fi

if [[ "$RC" == 0 ]]; then
  for required in \
    "$OUTPUT/RAW_P13_COORDINATE12_R1.tsv" \
    "$OUTPUT/RAW_P13_COORDINATE12_ACTIVE_ADDENDS_R1.tsv" \
    "$OUTPUT/RAW_P13_COORDINATE12_RESULT_R1.txt"; do
    if [[ ! -s "$required" ]]; then
      echo "missing/empty required output: $required" >> "$STDERR"
      RC=126
    fi
  done
fi
if [[ "$RC" == 0 ]]; then
  RESULT="$OUTPUT/RAW_P13_COORDINATE12_RESULT_R1.txt"
  grep -Fqx 'source_addend_sum_equals_frozen_H15_compiler=true' "$RESULT" || RC=126
  grep -Fqx 'source_omission_label=f1_times_dg2:i=13:j=1' "$RESULT" || RC=126
  grep -Fqx 'source_omission_applied_before_aggregation=true' "$RESULT" || RC=126
  grep -Fqx 'source_omission_changes_F0_coordinate12=true' "$RESULT" || RC=126
  grep -Eq '^TD6-V89H19R1-RAW-P13-COORDINATE12-(DIRECT-UNIT|FIRST-CANCELLATION-REQUIRED) PASS$' \
    "$STDOUT" || RC=126
fi

{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$RC"
  printf 'stdout_sha256=%s\n' "$(sha256sum "$STDOUT" | cut -d ' ' -f 1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$STDERR" | cut -d ' ' -f 1)"
  printf 'final_state=%s\n' "$([[ "$RC" == 0 ]] && echo COMPLETE || echo FAILED_CLOSED)"
} >> "$META"
printf '%s lane=%s rc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$TAG" "$RC" \
  > "$RUN/lanes.log"

(
  cd "$JOB_ROOT"
  sha256sum orchestrator.sh
  find payload source_root output run -type f -print0 | sort -z | xargs -0 sha256sum
) > "$JOB_ROOT/EVIDENCE.sha256"
exit "$RC"
