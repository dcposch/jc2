#!/usr/bin/env bash
#
# Package and detach the TD6 V89H19R2 original-FIRST / total-F producer on one
# explicitly registered AWS host.  No host is discovered or resolved
# dynamically: only r6a and box01 are accepted, by fixed IP and instance id.
#
# usage: launch_p13_coordinate12_original_first_total_f_host.sh \
#            <r6a|box01> <STAMP:YYYYmmddTHHMMSSZ> [PYTHON_BIN]
#
set -euo pipefail

LABEL=${1:?host label required (r6a|box01)}
STAMP=${2:?stamp required (YYYYmmddTHHMMSSZ)}
PYTHON_BIN=${3:-/home/ubuntu/venvs/td6/bin/python}

CASE_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
KEY=/Users/dc/.ssh/claude-cli.pem
TAG_PREFIX=td6_v89h19r2_p13_c12_first_total_
VM_CAP_KIB=805306368
WALL_SECONDS=43200
ARCHIVE=source_p13_full_normal_form.tar.gz
ARCHIVE_SHA=2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81
MANIFEST=SOURCE_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.sha256
MANIFEST_SHA=dc71902c714e67d57e29e220021ad2781fcad12e7778023db920bd3f929c2862
CLIENT_SHA=ac233cc61ddc971befa1bd0d2972d6aeacb5a9730660c85ad6391fbace94dac9
RUNNER_SHA=db85757ab43afd15305a81550c2356a33a37f62696926318bf181c666d74b030
PREREG_SHA=7ecdeae31448e29f1b5ba102db58c2f180f32b9df07ffb831f6b15b06e65753a
FLINT_MODULE_SHA=1f7ef1f52024937f542772ff9190e2f74449228cd69a6746b6608fbbd449d138

case "$LABEL" in
  r6a)   HOST_IP=3.91.104.135;  INSTANCE_ID=i-02cb2b4a379ffcc64 ;;
  box01) HOST_IP=54.175.21.169; INSTANCE_ID=i-029d0899cdb7c1ed1 ;;
  *) echo "refusing unregistered host label: $LABEL" >&2; exit 125 ;;
esac
[[ "$STAMP" =~ ^[0-9]{8}T[0-9]{6}Z$ ]] || {
  echo "refusing malformed stamp: $STAMP" >&2; exit 125; }
[[ -r "$KEY" ]] || { echo "missing ssh key: $KEY" >&2; exit 125; }

H18_OUTPUT="$CASE_DIR/harvest_h18_box02_20260826T223100Z/output"
H19_OUTPUT="$CASE_DIR/harvest_h19r1_r6a_20260826T234603Z/output"

# Complete pinned closure: the H15 archive plus every H15/H18/H19R1/H19R2
# artifact the client and runner rehash.
CASE_FILES=(
  PREREGISTRATION_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.md
  H19R2_V1_FORBIDDEN_MODULE_PROBE_ERRATUM.md
  replay_v89h19r2_p13_coordinate12_original_first_total_f.py
  run_v89h19r2_p13_coordinate12_original_first_total_f.sh
  SOURCE_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.sha256
  PREREGISTRATION_RAW_P13_COORDINATE12_AUDIT_R1.md
  replay_v89h19r1_raw_p13_coordinate12_audit.py
  run_v89h19r1_raw_p13_coordinate12_audit.sh
  SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256
  P13_RAW_COORDINATE12_AUDIT_R1_RESULT.md
  P13_RAW_COORDINATE12_AUDIT_R1_FREEZE.sha256
  P13_FULL_NORMAL_FORM_RESULT.md
  P13_FULL_NORMAL_FORM_FREEZE.sha256
  P13_FULL_NORMAL_FORM_EVIDENCE.sha256
  P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md
  P13_COORDINATE12_UNIT_RESULT.md
  P13_COORDINATE12_UNIT_FREEZE.sha256
  P13_COORDINATE12_UNIT_EVIDENCE.sha256
)
HARVEST_FILES=(
  "$H18_OUTPUT/P13_COORDINATE12_UNIT.tsv"
  "$H19_OUTPUT/RAW_P13_COORDINATE12_R1.tsv"
  "$H19_OUTPUT/RAW_P13_COORDINATE12_ACTIVE_ADDENDS_R1.tsv"
)

local_sha() { LC_ALL=C shasum -a 256 "$1" | cut -d ' ' -f 1; }

[[ "$(local_sha "$CASE_DIR/$ARCHIVE")" == "$ARCHIVE_SHA" ]] || {
  echo "H15 archive hash mismatch" >&2; exit 125; }
[[ "$(local_sha "$CASE_DIR/$MANIFEST")" == "$MANIFEST_SHA" ]] || {
  echo "source manifest hash mismatch" >&2; exit 125; }
[[ "$(local_sha "$CASE_DIR/replay_v89h19r2_p13_coordinate12_original_first_total_f.py")" \
   == "$CLIENT_SHA" ]] || { echo "client hash mismatch" >&2; exit 125; }
[[ "$(local_sha "$CASE_DIR/run_v89h19r2_p13_coordinate12_original_first_total_f.sh")" \
   == "$RUNNER_SHA" ]] || { echo "runner hash mismatch" >&2; exit 125; }
[[ "$(local_sha "$CASE_DIR/PREREGISTRATION_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.md")" \
   == "$PREREG_SHA" ]] || { echo "preregistration hash mismatch" >&2; exit 125; }

STAGE=$(mktemp -d "/tmp/td6_v89h19r2_${LABEL}_${STAMP}.XXXXXX")
trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/bundle/payload/h19r2"
cp "$CASE_DIR/$ARCHIVE" "$STAGE/bundle/payload/$ARCHIVE"
for name in "${CASE_FILES[@]}"; do
  cp "$CASE_DIR/$name" "$STAGE/bundle/payload/h19r2/$name"
done
for path in "${HARVEST_FILES[@]}"; do
  cp "$path" "$STAGE/bundle/payload/h19r2/$(basename "$path")"
done

# Every staged closure member must already match the frozen source manifest.
# Entries supplied by the H15 archive are absent here and are re-checked by the
# orchestrator's post-extract sha256sum -c inside the assembled source tree.
(
  cd "$STAGE/bundle/payload/h19r2"
  while read -r expected name; do
    if [[ -f "$name" ]]; then
      observed=$(LC_ALL=C shasum -a 256 "$name" | cut -d ' ' -f 1)
      if [[ "$observed" != "$expected" ]]; then
        echo "staged closure mismatch: $name" >&2
        exit 125
      fi
    fi
  done < "$MANIFEST"
)

cat > "$STAGE/bundle/orchestrator.sh" <<'ORCHESTRATOR'
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
  /home/ubuntu/jobs/td6_coordinate12_h19r2_*) ;;
  *) echo "refusing unregistered job root: $JOB_ROOT" >&2; exit 125 ;;
esac
case "$HOST_LABEL" in
  r6a|box01) ;;
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
H19R2_MANIFEST=SOURCE_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.sha256

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
( cd "$PAYLOAD/h19r2" && sha256sum -c "$H19R2_MANIFEST" --ignore-missing )

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
cp "$PAYLOAD"/h19r2/* "$SOURCE/"

for manifest in \
  SOURCE_P13_FULL_NORMAL_FORM.sha256 \
  SOURCE_P12_FULL_NORMAL_FORM.sha256 \
  SOURCE_P12_FLAG.sha256 \
  PAYLOAD_CLOSURE.sha256 \
  SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256 \
  "$H19R2_MANIFEST"; do
  (cd "$SOURCE" && sha256sum -c "$manifest") \
    > "$RUN/${manifest%.sha256}_check.stdout" \
    2> "$RUN/${manifest%.sha256}_check.stderr"
done

STAMP=$(date -u +%Y%m%dT%H%M%SZ)
TAG="td6_v89h19r2_p13_c12_first_total_${STAMP}_${HOST_LABEL}"
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
  printf 'memory_limit_kib=805306368\n'
  printf 'timeout_seconds=43200\n'
  printf 'threads=1\n'
  printf 'python=%s\n' "$PYTHON_BIN"
  printf 'python_version=%s\n' "$($PYTHON_BIN --version 2>&1)"
  printf 'python_sha256=%s\n' "$(sha256sum "$PYTHON_BIN" | cut -d ' ' -f 1)"
  printf 'python_optimize=%s\n' "$PYTHON_OPTIMIZE"
  printf 'python_flint=%s\n' "$FLINT_VERSION"
  printf 'python_packages=%s\n' "$($PYTHON_BIN -m pip freeze | sort | tr '\n' ',')"
  printf 'python_flint_module=%s\n' "$FLINT_MODULE"
  printf 'python_flint_module_sha256=%s\n' "$FLINT_MODULE_SHA"
  printf 'h15_archive_sha256=%s\n' "$H15_ARCHIVE_SHA"
  printf 'h19r2_manifest_sha256=%s\n' \
    "$(sha256sum "$SOURCE/$H19R2_MANIFEST" | cut -d ' ' -f 1)"
  printf 'h19r2_preregistration_sha256=%s\n' "$(sha256sum \
    "$SOURCE/PREREGISTRATION_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.md" \
    | cut -d ' ' -f 1)"
  printf 'h19r2_replay_sha256=%s\n' "$(sha256sum \
    "$SOURCE/replay_v89h19r2_p13_coordinate12_original_first_total_f.py" \
    | cut -d ' ' -f 1)"
  printf 'h19r2_runner_sha256=%s\n' "$(sha256sum \
    "$SOURCE/run_v89h19r2_p13_coordinate12_original_first_total_f.sh" \
    | cut -d ' ' -f 1)"
} > "$META"

ulimit -v 805306368
export PYTHONHASHSEED=0
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MALLOC_ARENA_MAX=4
export PATH="$(dirname "$PYTHON_BIN"):/usr/bin:/bin"

if (
  cd "$SOURCE"
  AWS_RUN_TAG="$TAG" TD6_OUTPUT_DIR="$OUTPUT" \
    TD6_H15_ARCHIVE="$PAYLOAD/source_p13_full_normal_form.tar.gz" \
    TD6_Q_EXPONENT=2 TD6_Q_SCOPE=q2-q14-q16-q24 \
    TD6_PIVOT_POLICY=ascending TD6_PIVOT_SCOPE=all-staged \
    TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U \
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
    /usr/bin/timeout --signal=TERM --kill-after=60 43200 \
    /usr/bin/time -v bash run_v89h19r2_p13_coordinate12_original_first_total_f.sh
) > "$STDOUT" 2> "$STDERR"; then
  RC=0
else
  RC=$?
fi

if [[ "$RC" == 0 ]]; then
  for required in \
    "$OUTPUT/P13_ORIGINAL_FIRST_INVERSE.tsv" \
    "$OUTPUT/P13_COORDINATE12_FIRST_MULTIPLIERS.tsv" \
    "$OUTPUT/P13_COORDINATE12_FIRST_IDENTITY_C12.tsv" \
    "$OUTPUT/P13_ADDEND_FULL_E3_CENSUS.tsv" \
    "$OUTPUT/P13_OMISSION_MULTIPLIERS.tsv" \
    "$OUTPUT/ALLQ_P13_FULL_NORMAL_FORM.tsv" \
    "$OUTPUT/P13_AFFINE_PIVOT_MAP.tsv" \
    "$OUTPUT/P13_COORDINATE12_TOTAL_F_MULTIPLIERS.tsv" \
    "$OUTPUT/P13_COORDINATE12_TOTAL_F_H.tsv" \
    "$OUTPUT/P13_COORDINATE12_F0_DISPLAY.tsv" \
    "$OUTPUT/P13_COORDINATE12_FIRST_TOTAL_F_RESULT.txt"; do
    if [[ ! -s "$required" ]]; then
      echo "missing/empty required output: $required" >> "$STDERR"
      RC=126
    fi
  done
fi
if [[ "$RC" == 0 ]]; then
  RESULT="$OUTPUT/P13_COORDINATE12_FIRST_TOTAL_F_RESULT.txt"
  for line in \
    'q15_absent_target_shear=true' \
    'affine_pivot_map_equals_frozen_H12=true' \
    'full_normal_form_equals_frozen_H15=true' \
    'coordinate12_equals_frozen_H18_unit=true' \
    'original_FIRST_inverse_replay=true' \
    'original_FIRST_expansion_equals_NF=true' \
    'F0_denominators_in_U_V_V2minus4U3=true' \
    'total_F_division_exact=true' \
    'total_F_not_inverted=true' \
    'total_family_denominator_radical_subset_U_H_B3=true' \
    'B3_eq_V4_only_after_F=true' \
    'UH_eq_V2minus4U3_only_after_F=true' \
    'independent_total_F_unit_claim=true' \
    'whole_TD6_killed=false' \
    'source_landing_composed=false' \
    'JC2_resolved=false'; do
    grep -Fqx "$line" "$RESULT" || RC=126
  done
  grep -Eq '^omission_changes_(endpoint|cofactor)=true$' "$RESULT" || RC=126
  grep -Fqx \
    'TD6-V89H19R2-P13-COORDINATE12-ORIGINAL-FIRST-TOTAL-F PASS' "$STDOUT" \
    || RC=126
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
ORCHESTRATOR
chmod +x "$STAGE/bundle/orchestrator.sh"

BUNDLE="$STAGE/bundle.tar.gz"
COPYFILE_DISABLE=1 tar -czf "$BUNDLE" -C "$STAGE/bundle" orchestrator.sh payload
BUNDLE_SHA=$(local_sha "$BUNDLE")
ORCHESTRATOR_SHA=$(local_sha "$STAGE/bundle/orchestrator.sh")
JOB_ROOT="/home/ubuntu/jobs/td6_coordinate12_h19r2_${STAMP}_${LABEL}"

SSH_OPTS=(-i "$KEY" -o BatchMode=yes -o ConnectTimeout=20
          -o StrictHostKeyChecking=accept-new)

ssh "${SSH_OPTS[@]}" "ubuntu@$HOST_IP" bash -s -- "$JOB_ROOT" "$INSTANCE_ID" <<'PREPARE'
set -euo pipefail
JOB_ROOT=$1
EXPECTED_INSTANCE_ID=$2
[[ "$(uname -s)" == Linux ]] || { echo "non-Linux host" >&2; exit 125; }
grep -q 'Amazon EC2' /sys/class/dmi/id/sys_vendor || { echo "non-EC2" >&2; exit 125; }
OBSERVED=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)
[[ "$OBSERVED" == "$EXPECTED_INSTANCE_ID" ]] || {
  echo "instance mismatch: $OBSERVED != $EXPECTED_INSTANCE_ID" >&2; exit 125; }
[[ ! -e "$JOB_ROOT" ]] || { echo "refusing reused job root: $JOB_ROOT" >&2; exit 125; }
mkdir -p "$JOB_ROOT"
PREPARE

scp "${SSH_OPTS[@]}" "$BUNDLE" "ubuntu@$HOST_IP:$JOB_ROOT/bundle.tar.gz"

ssh "${SSH_OPTS[@]}" "ubuntu@$HOST_IP" bash -s -- \
  "$JOB_ROOT" "$LABEL" "$PYTHON_BIN" "$INSTANCE_ID" "$BUNDLE_SHA" \
  "$ORCHESTRATOR_SHA" <<'DEPLOY'
set -euo pipefail
JOB_ROOT=$1
LABEL=$2
PYTHON_BIN=$3
INSTANCE_ID=$4
BUNDLE_SHA=$5
ORCHESTRATOR_SHA=$6
cd "$JOB_ROOT"
OBSERVED=$(sha256sum bundle.tar.gz | cut -d ' ' -f 1)
[[ "$OBSERVED" == "$BUNDLE_SHA" ]] || {
  echo "remote bundle hash mismatch: $OBSERVED != $BUNDLE_SHA" >&2; exit 125; }
tar -xzf bundle.tar.gz -C "$JOB_ROOT"
OBSERVED=$(sha256sum orchestrator.sh | cut -d ' ' -f 1)
[[ "$OBSERVED" == "$ORCHESTRATOR_SHA" ]] || {
  echo "remote orchestrator hash mismatch: $OBSERVED" >&2; exit 125; }
printf 'bundle_sha256=%s\norchestrator_sha256=%s\nhost_label=%s\ninstance_id=%s\npython=%s\ncap_kib=805306368\ntimeout_seconds=43200\nthreads=1\ntag_prefix=td6_v89h19r2_p13_c12_first_total_\n' \
  "$BUNDLE_SHA" "$ORCHESTRATOR_SHA" "$LABEL" "$INSTANCE_ID" "$PYTHON_BIN" \
  > "$JOB_ROOT/launch.meta"
nohup setsid bash "$JOB_ROOT/orchestrator.sh" \
  "$JOB_ROOT" "$LABEL" "$PYTHON_BIN" "$INSTANCE_ID" \
  > "$JOB_ROOT/launcher.stdout" 2> "$JOB_ROOT/launcher.stderr" < /dev/null &
printf '%s\n' "$!" > "$JOB_ROOT/orchestrator.pid"
printf 'detached_orchestrator_pid=%s\n' "$(cat "$JOB_ROOT/orchestrator.pid")"
DEPLOY

printf 'host_label=%s\nhost_ip=%s\ninstance_id=%s\njob_root=%s\n' \
  "$LABEL" "$HOST_IP" "$INSTANCE_ID" "$JOB_ROOT"
printf 'bundle_sha256=%s\norchestrator_sha256=%s\n' \
  "$BUNDLE_SHA" "$ORCHESTRATOR_SHA"
printf 'archive_sha256=%s\nmanifest_sha256=%s\nclient_sha256=%s\n' \
  "$ARCHIVE_SHA" "$MANIFEST_SHA" "$CLIENT_SHA"
printf 'tag_prefix=%s\nvm_cap_kib=%s\nwall_seconds=%s\nthreads=1\n' \
  "$TAG_PREFIX" "$VM_CAP_KIB" "$WALL_SECONDS"
printf 'flint_module_sha256=%s\n' "$FLINT_MODULE_SHA"
