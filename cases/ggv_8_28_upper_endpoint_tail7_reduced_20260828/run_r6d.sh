#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: $0 SOURCE_ROOT JOB_DIR TAG exact_q|modp" >&2
  exit 64
fi

SOURCE_ROOT=$1
JOB_DIR=$2
TAG=$3
MODE=$4
CASE_REL=cases/ggv_8_28_upper_endpoint_tail7_reduced_20260828
CASE_DIR=$SOURCE_ROOT/$CASE_REL

case "$MODE" in
  exact_q)
    MEMORY_KB=134217728
    WALL_SECONDS=10800
    ENGINE=$CASE_DIR/TAIL7_REDUCED/tail7_reduced_q.sing
    ;;
  modp)
    MEMORY_KB=33554432
    WALL_SECONDS=3600
    ENGINE=$CASE_DIR/TAIL7_REDUCED/tail7_reduced_p65521.sing
    ;;
  *)
    echo "invalid mode: $MODE" >&2
    exit 125
    ;;
esac

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing outside Linux" >&2
  exit 125
fi
AWS_VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
AWS_PRODUCT=$(tr -d '\n' < /sys/class/dmi/id/product_name 2>/dev/null || true)
AWS_INSTANCE_ID=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag 2>/dev/null || true)
if [[ "$AWS_VENDOR" != "Amazon EC2" ||
      "$AWS_PRODUCT" != "r6i.16xlarge" ||
      "$AWS_INSTANCE_ID" != "i-07eeaf8ba6f0bc419" ]]; then
  echo "refusing outside audited r6d: vendor=$AWS_VENDOR product=$AWS_PRODUCT instance=$AWS_INSTANCE_ID" >&2
  exit 125
fi

SINGULAR_SHA256=$(sha256sum /usr/bin/Singular | awk '{print $1}')
if [[ "$SINGULAR_SHA256" != "90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4" ]]; then
  echo "refusing unpinned Singular binary: $SINGULAR_SHA256" >&2
  exit 125
fi

SWAP_USED_BYTES=$(free -b | awk 'NR==3{print $3}')
MEMORY_AVAILABLE_BYTES=$(free -b | awk 'NR==2{print $7}')
CAP_BYTES=$((MEMORY_KB * 1024))
MIN_HEADROOM_BYTES=161061273600
if [[ "$SWAP_USED_BYTES" -ne 0 ]]; then
  echo "refusing nonzero swap: $SWAP_USED_BYTES" >&2
  exit 125
fi
if [[ "$MEMORY_AVAILABLE_BYTES" -lt $((CAP_BYTES + MIN_HEADROOM_BYTES)) ]]; then
  echo "refusing cap without 150-GiB headroom: available=$MEMORY_AVAILABLE_BYTES cap=$CAP_BYTES" >&2
  exit 125
fi

if [[ -e "$JOB_DIR" ]]; then
  if [[ ! -d "$JOB_DIR" || -n "$(find "$JOB_DIR" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
    echo "refusing nonempty output namespace: $JOB_DIR" >&2
    exit 125
  fi
else
  mkdir "$JOB_DIR"
fi
if ! (set -o noclobber; : > "$JOB_DIR/RUN_STARTED") 2>/dev/null; then
  echo "refusing reused output marker" >&2
  exit 125
fi

finalize() {
  local rc=$?
  trap - EXIT
  set +e
  {
    printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'exit_code=%s\n' "$rc"
    printf 'memory_available_after=%s\n' "$(free -b | awk 'NR==2{print $7}')"
    printf 'swap_used_after=%s\n' "$(free -b | awk 'NR==3{print $3}')"
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

cd "$SOURCE_ROOT"
if find . -type f ! -path "./$CASE_REL/SOURCE.sha256" -perm -u=w -print -quit \
    | grep -q .; then
  echo "refusing writable source bytes" >&2
  exit 125
fi
ACTUAL_FILES=$(find . -type f ! -path "./$CASE_REL/SOURCE.sha256" -print \
  | sed 's#^./##' | LC_ALL=C sort)
MANIFEST_FILES=$(awk '{print $2}' "$CASE_REL/SOURCE.sha256" | LC_ALL=C sort)
if [[ "$ACTUAL_FILES" != "$MANIFEST_FILES" ]]; then
  echo "source manifest does not cover the exact immutable bundle" >&2
  exit 125
fi
sha256sum -c "$CASE_REL/SOURCE.sha256" > "$JOB_DIR/source_check.stdout"

{
  printf 'tag=%s\n' "$TAG"
  printf 'mode=%s\n' "$MODE"
  printf 'host=%s\n' "$(hostname)"
  printf 'aws_vendor=%s\n' "$AWS_VENDOR"
  printf 'aws_product=%s\n' "$AWS_PRODUCT"
  printf 'aws_instance_id=%s\n' "$AWS_INSTANCE_ID"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'memory_cap_kb=%s\n' "$MEMORY_KB"
  printf 'wall_cap_seconds=%s\n' "$WALL_SECONDS"
  printf 'threads=1\n'
  printf 'memory_available_before=%s\n' "$MEMORY_AVAILABLE_BYTES"
  printf 'minimum_headroom_bytes=%s\n' "$MIN_HEADROOM_BYTES"
  printf 'swap_used_before=%s\n' "$SWAP_USED_BYTES"
  printf 'singular_sha256=%s\n' "$SINGULAR_SHA256"
  printf 'source_manifest_sha256=%s\n' "$(sha256sum "$CASE_REL/SOURCE.sha256" | cut -d ' ' -f 1)"
} > "$JOB_DIR/METADATA.txt"
ps -eo pid,ppid,state,etimes,pcpu,rss,vsz,comm,args --sort=-rss \
  > "$JOB_DIR/prelaunch_processes.txt"

ulimit -v "$MEMORY_KB"
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1

set +e
timeout --signal=TERM --kill-after=120 900 \
  /usr/bin/time -v python3 -B "$CASE_DIR/verify_tail7_reduced.py" \
  > "$JOB_DIR/verify.stdout" 2> "$JOB_DIR/verify.stderr"
VERIFY_RC=$?
set -e
printf '%s\n' "$VERIFY_RC" > "$JOB_DIR/verify.rc"
if [[ "$VERIFY_RC" -ne 0 ]]; then
  exit "$VERIFY_RC"
fi

set +e
timeout --signal=TERM --kill-after=120 "$WALL_SECONDS" \
  /usr/bin/time -v /usr/bin/Singular -q "$ENGINE" \
  > "$JOB_DIR/engine.stdout" 2> "$JOB_DIR/engine.stderr"
ENGINE_RC=$?
set -e
printf '%s\n' "$ENGINE_RC" > "$JOB_DIR/engine.rc"
exit "$ENGINE_RC"
