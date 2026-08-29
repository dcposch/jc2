#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 7 || $# -gt 8 ]]; then
  echo "usage: $0 SOURCE_ROOT JOB_DIR TAG MODE MEMORY_KB WALL_SECONDS THREADS [CUSTODY_PROFILE]" >&2
  exit 64
fi

SOURCE_ROOT=$1
JOB_DIR=$2
TAG=$3
MODE=$4
MEMORY_KB=$5
WALL_SECONDS=$6
THREADS=$7
CUSTODY_PROFILE=${8:-box03}
CASE_REL=cases/ggv_8_28_upper_endpoint_branch_p_20260827
CASE_DIR=$SOURCE_ROOT/$CASE_REL

case "$MODE" in
  compile_reduce|exact_raw|exact_raw_dp|modp_raw|modp_raw_dp|modp_raw_msolve|exact_row_rref|exact_row_rref_dp|exact_prefix_quotient|exact_prefix_quotient_slimgb|exact_homogeneous_sat|exact_tail_deformation|exact_tail10_deformation|modp_row_rref|tracked_row_rref) ;;
  *) echo "invalid mode: $MODE" >&2; exit 125;;
esac

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing heavy lane outside Linux" >&2
  exit 125
fi
AWS_VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$AWS_VENDOR" != "Amazon EC2" ]]; then
  echo "refusing heavy lane outside Amazon EC2: vendor=${AWS_VENDOR:-unknown}" >&2
  exit 125
fi
AWS_PRODUCT=$(tr -d '\n' < /sys/class/dmi/id/product_name 2>/dev/null || true)
AWS_HOST=$(hostname)
AWS_INSTANCE_ID=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag 2>/dev/null || true)
case "$CUSTODY_PROFILE" in
  box03)
    if [[ "$AWS_PRODUCT" != "r6i.16xlarge" ||
          "$AWS_HOST" != "ip-172-30-0-249" ||
          "$AWS_INSTANCE_ID" != "i-0ece0b9a3b4a7512f" ]]; then
      echo "refusing heavy lane outside audited Box03: host=${AWS_HOST:-unknown} product=${AWS_PRODUCT:-unknown} instance=${AWS_INSTANCE_ID:-unknown}" >&2
      exit 125
    fi
    ;;
  box02_prefix)
    if [[ ( "$MODE" != "exact_prefix_quotient" &&
            "$MODE" != "exact_prefix_quotient_slimgb" ) ||
          "$MEMORY_KB" != "134217728" ||
          "$WALL_SECONDS" != "7200" ||
          "$THREADS" != "1" ]]; then
      echo "Box02 custody is licensed only for the fixed exact 466-generator prefix lane" >&2
      exit 125
    fi
    if [[ "$AWS_PRODUCT" != "x2idn.32xlarge" ||
          "$AWS_HOST" != "ip-172-30-0-186" ||
          "$AWS_INSTANCE_ID" != "i-010201a5da47795c4" ]]; then
      echo "refusing heavy lane outside audited Box02: host=${AWS_HOST:-unknown} product=${AWS_PRODUCT:-unknown} instance=${AWS_INSTANCE_ID:-unknown}" >&2
      exit 125
    fi
    BOX02_NPROC=$(nproc)
    BOX02_LOAD1=$(awk '{print $1}' /proc/loadavg)
    if [[ "$BOX02_NPROC" != "128" ]] ||
       ! awk -v load_value="$BOX02_LOAD1" \
           'BEGIN { exit !(load_value <= 16.0) }'; then
      echo "refusing contended Box02: nproc=$BOX02_NPROC load1=$BOX02_LOAD1" >&2
      exit 125
    fi
    BOX02_SINGULAR_SHA256=$(sha256sum /usr/bin/Singular | awk '{print $1}')
    if [[ "$BOX02_SINGULAR_SHA256" != "90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4" ]]; then
      echo "refusing unpinned Box02 Singular binary: $BOX02_SINGULAR_SHA256" >&2
      exit 125
    fi
    ;;
  *)
    echo "unknown custody profile: $CUSTODY_PROFILE" >&2
    exit 125
    ;;
esac
if [[ -z "$SOURCE_ROOT" || -z "$JOB_DIR" || -z "$TAG" ]]; then
  echo "source, job directory, and registered tag are required" >&2
  exit 125
fi
case "$MEMORY_KB:$WALL_SECONDS:$THREADS" in
  *[!0-9:]*|:*|*::*|*:)
    echo "caps and thread count must be positive integers" >&2
    exit 125
    ;;
esac
if [[ "$MEMORY_KB" -eq 0 || "$MEMORY_KB" -gt 471859200 ||
      "$WALL_SECONDS" -eq 0 || "$WALL_SECONDS" -gt 21600 ||
      "$THREADS" -eq 0 ]]; then
  echo "refusing caps outside preregistered envelope" >&2
  exit 125
fi
MODE_MAX_MEMORY_KB=471859200
MODE_MAX_WALL_SECONDS=21600
MODE_MAX_THREADS=$THREADS
case "$MODE" in
  exact_raw)
    MODE_MAX_MEMORY_KB=293601280
    MODE_MAX_THREADS=1
    ;;
  exact_raw_dp|exact_row_rref_dp|exact_homogeneous_sat)
    MODE_MAX_MEMORY_KB=104857600
    MODE_MAX_THREADS=1
    ;;
  exact_row_rref)
    MODE_MAX_MEMORY_KB=134217728
    MODE_MAX_THREADS=1
    ;;
  tracked_row_rref)
    MODE_MAX_THREADS=1
    ;;
  exact_prefix_quotient|exact_prefix_quotient_slimgb)
    MODE_MAX_MEMORY_KB=134217728
    MODE_MAX_WALL_SECONDS=7200
    MODE_MAX_THREADS=1
    ;;
  exact_tail_deformation)
    MODE_MAX_MEMORY_KB=16777216
    MODE_MAX_WALL_SECONDS=3600
    MODE_MAX_THREADS=1
    ;;
  exact_tail10_deformation)
    MODE_MAX_MEMORY_KB=25165824
    MODE_MAX_WALL_SECONDS=3600
    MODE_MAX_THREADS=1
    ;;
esac
if [[ "$MEMORY_KB" -gt "$MODE_MAX_MEMORY_KB" ||
      "$WALL_SECONDS" -gt "$MODE_MAX_WALL_SECONDS" ||
      "$THREADS" -gt "$MODE_MAX_THREADS" ]]; then
  echo "refusing caps outside mode-specific preregistration" >&2
  exit 125
fi
MIN_HEADROOM_BYTES=161061273600
CAP_BYTES=$((MEMORY_KB * 1024))
MEMORY_AVAILABLE_BYTES=$(free -b | awk 'NR==2{print $7}')
SWAP_USED_BYTES=$(free -b | awk 'NR==3{print $3}')
if [[ "$SWAP_USED_BYTES" -ne 0 ]]; then
  echo "refusing heavy lane with nonzero swap: $SWAP_USED_BYTES" >&2
  exit 125
fi
HEADROOM_ENFORCED=0
case "$MODE" in exact_raw|exact_prefix_quotient|exact_prefix_quotient_slimgb) HEADROOM_ENFORCED=1;; esac
if [[ "$HEADROOM_ENFORCED" -eq 1 &&
      "$MEMORY_AVAILABLE_BYTES" -lt $((CAP_BYTES + MIN_HEADROOM_BYTES)) ]]; then
  echo "refusing cap without 150-GiB host headroom: available=$MEMORY_AVAILABLE_BYTES requested=$CAP_BYTES" >&2
  exit 125
fi
if [[ -e "$JOB_DIR" ]]; then
  if [[ ! -d "$JOB_DIR" || -n "$(find "$JOB_DIR" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
    echo "refusing nonempty or non-directory output namespace: $JOB_DIR" >&2
    exit 125
  fi
else
  mkdir "$JOB_DIR"
fi
if ! (set -o noclobber; : > "$JOB_DIR/RUN_STARTED") 2>/dev/null; then
  echo "refusing nonfresh output namespace marker: $JOB_DIR" >&2
  exit 125
fi

finalize() {
  local rc=$?
  trap - EXIT
  set +e
  {
    printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'exit_code=%s\n' "$rc"
    printf 'memory_after=%s\n' "$(free -b | awk 'NR==2{print $3"/"$2" used"}')"
    printf 'swap_after=%s\n' "$(free -b | awk 'NR==3{print $3"/"$2" used"}')"
  } >> "$JOB_DIR/METADATA.txt"
  printf '%s\n' "$rc" > "$JOB_DIR/RUN_STATUS.txt"
  if [[ "$rc" -eq 0 ]]; then
    touch "$JOB_DIR/RUN_COMPLETE"
  else
    touch "$JOB_DIR/RUN_FAILED"
  fi
  find "$JOB_DIR" -type f ! -name EVIDENCE.sha256 -print0 \
    | sort -z | xargs -0 sha256sum > "$JOB_DIR/EVIDENCE.sha256"
  exit "$rc"
}
trap finalize EXIT

JOB_START_EPOCH=$(date +%s)
JOB_DEADLINE_EPOCH=$((JOB_START_EPOCH + WALL_SECONDS))
KILL_GRACE_SECONDS=120

cd "$SOURCE_ROOT"
ACTUAL_CASE_FILES=$(find "$CASE_REL" -type f ! -name SOURCE.sha256 -print | LC_ALL=C sort)
MANIFEST_CASE_FILES=$(awk -v prefix="$CASE_REL/" '$2 ~ "^" prefix && $2 !~ /SOURCE.sha256$/ {print $2}' \
  "$CASE_REL/SOURCE.sha256" | LC_ALL=C sort)
if [[ "$ACTUAL_CASE_FILES" != "$MANIFEST_CASE_FILES" ]]; then
  echo "source manifest does not cover the exact case file set" >&2
  exit 125
fi
printf 'SOURCE_COVERAGE_PASS files=%s\n' \
  "$(find "$CASE_REL" -type f ! -name SOURCE.sha256 | wc -l)" \
  > "$JOB_DIR/source_coverage.stdout"
sha256sum -c "$CASE_REL/SOURCE.sha256" > "$JOB_DIR/source_check.stdout"

{
  printf 'tag=%s\n' "$TAG"
  printf 'mode=%s\n' "$MODE"
  printf 'host=%s\n' "$(hostname)"
  printf 'kernel=%s\n' "$(uname -a)"
  printf 'aws_vendor=%s\n' "$AWS_VENDOR"
  printf 'aws_product=%s\n' "$AWS_PRODUCT"
  printf 'aws_host=%s\n' "$AWS_HOST"
  printf 'aws_instance_id=%s\n' "$AWS_INSTANCE_ID"
  printf 'custody_profile=%s\n' "$CUSTODY_PROFILE"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'memory_cap_kb=%s\n' "$MEMORY_KB"
  printf 'wall_cap_seconds=%s\n' "$WALL_SECONDS"
  printf 'global_deadline_epoch=%s\n' "$JOB_DEADLINE_EPOCH"
  printf 'kill_grace_seconds=%s\n' "$KILL_GRACE_SECONDS"
  printf 'threads=%s\n' "$THREADS"
  printf 'source_manifest_sha256=%s\n' "$(sha256sum "$CASE_REL/SOURCE.sha256" | cut -d ' ' -f 1)"
  printf 'python=%s\n' "$(python3 --version 2>&1)"
  printf 'singular=%s\n' "$(Singular --version 2>&1 | head -1)"
  printf 'msolve=%s\n' "$(msolve -h 2>&1 | grep -m1 -E 'msolve library|version' || true)"
  printf 'memory_before=%s\n' "$(free -b | awk 'NR==2{print $3"/"$2" used"}')"
  printf 'memory_available_before=%s\n' "$MEMORY_AVAILABLE_BYTES"
  printf 'minimum_headroom_bytes=%s\n' "$MIN_HEADROOM_BYTES"
  printf 'headroom_enforced=%s\n' "$HEADROOM_ENFORCED"
  printf 'swap_before=%s\n' "$(free -b | awk 'NR==3{print $3"/"$2" used"}')"
} > "$JOB_DIR/METADATA.txt"

if [[ "$CUSTODY_PROFILE" == "box02_prefix" ]]; then
  ps -eo pid,ppid,state,etimes,pcpu,rss,vsz,comm,args --sort=-rss \
    > "$JOB_DIR/prelaunch_processes.txt"
  {
    printf 'nproc=%s\n' "$BOX02_NPROC"
    printf 'load1=%s\n' "$BOX02_LOAD1"
    printf 'singular_sha256=%s\n' "$BOX02_SINGULAR_SHA256"
  } > "$JOB_DIR/box02_start_gate.txt"
fi

ulimit -v "$MEMORY_KB"
export OMP_NUM_THREADS="$THREADS"
export OPENBLAS_NUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1

run_timed() {
  local label=$1
  shift
  local now remaining
  now=$(date +%s)
  remaining=$((JOB_DEADLINE_EPOCH - now - KILL_GRACE_SECONDS))
  if [[ "$remaining" -le 0 ]]; then
    printf '%s\n' 124 > "$JOB_DIR/$label.rc"
    printf 'global wall deadline exhausted before stage %s\n' "$label" \
      > "$JOB_DIR/$label.stderr"
    : > "$JOB_DIR/$label.stdout"
    return 124
  fi
  set +e
  timeout --signal=TERM --kill-after="$KILL_GRACE_SECONDS" "$remaining" \
    /usr/bin/time -v "$@" \
    > "$JOB_DIR/$label.stdout" 2> "$JOB_DIR/$label.stderr"
  local rc=$?
  set -e
  printf '%s\n' "$rc" > "$JOB_DIR/$label.rc"
  return "$rc"
}

run_timed compile_check python3 -B "$CASE_DIR/compile_endpoint.py" --check

case "$MODE" in
  compile_reduce)
    run_timed raw_parse Singular -q "$CASE_DIR/raw_parse.sing"
    mkdir -p "$JOB_DIR/generated"
    run_timed triangular_reduce python3 -B "$CASE_DIR/triangular_reduce.py" --output "$JOB_DIR/generated"
    ;;
  exact_raw)
    run_timed exact_raw Singular -q "$CASE_DIR/raw_direct.sing"
    ;;
  exact_raw_dp)
    run_timed exact_raw_dp Singular -q "$CASE_DIR/raw_direct_q_dp_slimgb.sing"
    ;;
  modp_raw)
    run_timed modp_raw Singular -q "$CASE_DIR/raw_direct_p65521.sing"
    ;;
  modp_raw_dp)
    run_timed modp_raw_dp Singular -q "$CASE_DIR/raw_direct_p65521_dp_slimgb.sing"
    ;;
  modp_raw_msolve)
    run_timed modp_raw_msolve msolve -f "$CASE_DIR/raw_direct_p65521.ms" \
      -t "$THREADS" -v 1 -o "$JOB_DIR/modp_raw_msolve.out"
    ;;
  exact_row_rref)
    run_timed row_rref_check python3 -B "$CASE_DIR/row_rref_compile.py" \
      --output "$CASE_DIR/ROW_RREF" --check
    run_timed exact_row_rref Singular -q "$CASE_DIR/ROW_RREF/row_rref_q.sing"
    ;;
  exact_row_rref_dp)
    run_timed row_rref_check python3 -B "$CASE_DIR/row_rref_compile.py" \
      --output "$CASE_DIR/ROW_RREF" --check
    run_timed exact_row_rref_dp Singular -q \
      "$CASE_DIR/ROW_RREF/row_rref_q_dp_slimgb.sing"
    ;;
  exact_prefix_quotient)
    run_timed prefix_quotient_check python3 -B \
      "$CASE_DIR/prefix_quotient_compile.py" --check
    run_timed prefix_quotient_replay python3 -B \
      "$CASE_DIR/verify_prefix_quotient.py"
    run_timed exact_prefix_quotient Singular -q \
      "$CASE_DIR/PREFIX_QUOTIENT/prefix_quotient_q.sing"
    ;;
  exact_prefix_quotient_slimgb)
    run_timed prefix_quotient_check python3 -B \
      "$CASE_DIR/prefix_quotient_compile.py" --check
    run_timed prefix_quotient_replay python3 -B \
      "$CASE_DIR/verify_prefix_quotient.py"
    run_timed exact_prefix_quotient_slimgb Singular -q \
      "$CASE_DIR/PREFIX_QUOTIENT/prefix_quotient_q_slimgb.sing"
    ;;
  exact_homogeneous_sat)
    run_timed homogenized_check python3 -B "$CASE_DIR/homogenize_endpoint.py" \
      --output "$CASE_DIR/HOMOGENIZED" --check
    run_timed homogenized_replay python3 -B "$CASE_DIR/verify_homogenization.py"
    run_timed exact_homogeneous_sat Singular -q \
      "$CASE_DIR/HOMOGENIZED/homogenized_q_sat.sing"
    ;;
  exact_tail_deformation)
    mkdir -p "$JOB_DIR/tail_generated"
    run_timed tail_compile python3 -B "$CASE_DIR/tail_deformation.py" \
      --output "$JOB_DIR/tail_generated"
    run_timed exact_tail_deformation Singular -q \
      "$JOB_DIR/tail_generated/tail_q.sing"
    ;;
  exact_tail10_deformation)
    mkdir -p "$JOB_DIR/tail_generated"
    run_timed tail_compile python3 -B "$CASE_DIR/tail_deformation.py" \
      --cutoff 10 --output "$JOB_DIR/tail_generated"
    run_timed exact_tail10_deformation Singular -q \
      "$JOB_DIR/tail_generated/tail_q.sing"
    ;;
  modp_row_rref)
    run_timed row_rref_check python3 -B "$CASE_DIR/row_rref_compile.py" \
      --output "$CASE_DIR/ROW_RREF" --check
    run_timed modp_row_rref Singular -q "$CASE_DIR/ROW_RREF/row_rref_p65521.sing"
    ;;
  tracked_row_rref)
    run_timed row_rref_check python3 -B "$CASE_DIR/row_rref_compile.py" \
      --output "$CASE_DIR/ROW_RREF" --check
    cd "$JOB_DIR"
    run_timed tracked_parse Singular -q "$CASE_DIR/ROW_RREF/row_rref_q_tracked_parse.sing"
    run_timed tracked_row_rref Singular -q \
      "$CASE_DIR/ROW_RREF/row_rref_q_tracked_raw_certificate.sing"
    ;;
  *)
    echo "unknown mode: $MODE" >&2
    exit 65
    ;;
esac
