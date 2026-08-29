#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 6 ]]; then
  echo "usage: $0 SOURCE_ROOT JOB_DIR TAG ENGINE_REL MEMORY_KB WALL_SECONDS" >&2
  exit 64
fi
SOURCE_ROOT=$1
JOB_DIR=$2
TAG=$3
ENGINE_REL=$4
MEMORY_KB=$5
WALL_SECONDS=$6
CASE_REL=cases/ggv_8_28_upper_endpoint_tail7_branches_20260828
CASE_DIR=$SOURCE_ROOT/$CASE_REL

case "$ENGINE_REL" in
  BRANCHES/shared_block_q.sing|BRANCHES/a3_4_q.sing|BRANCHES/a3_2_q.sing) ;;
  *) echo "unlicensed engine: $ENGINE_REL" >&2; exit 125;;
esac
case "$MEMORY_KB:$WALL_SECONDS" in
  8388608:1800|67108864:7200) ;;
  *) echo "unlicensed cap pair" >&2; exit 125;;
esac

AWS_VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
AWS_PRODUCT=$(tr -d '\n' < /sys/class/dmi/id/product_name 2>/dev/null || true)
AWS_INSTANCE_ID=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag 2>/dev/null || true)
if [[ "$(uname -s)" != "Linux" || "$AWS_VENDOR" != "Amazon EC2" ||
      "$AWS_PRODUCT" != "r6i.16xlarge" ||
      "$AWS_INSTANCE_ID" != "i-07eeaf8ba6f0bc419" ]]; then
  echo "r6d custody mismatch" >&2
  exit 125
fi
SINGULAR_SHA256=$(sha256sum /usr/bin/Singular | awk '{print $1}')
if [[ "$SINGULAR_SHA256" != "90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4" ]]; then
  echo "Singular custody mismatch" >&2
  exit 125
fi
SWAP_USED=$(free -b | awk 'NR==3{print $3}')
AVAILABLE=$(free -b | awk 'NR==2{print $7}')
CAP_BYTES=$((MEMORY_KB * 1024))
if [[ "$SWAP_USED" -ne 0 || "$AVAILABLE" -lt $((CAP_BYTES + 161061273600)) ]]; then
  echo "memory/swap start gate failed" >&2
  exit 125
fi
if [[ -e "$JOB_DIR" ]]; then
  [[ -d "$JOB_DIR" && -z "$(find "$JOB_DIR" -mindepth 1 -maxdepth 1 -print -quit)" ]] || exit 125
else
  mkdir "$JOB_DIR"
fi
(set -o noclobber; : > "$JOB_DIR/RUN_STARTED") 2>/dev/null || exit 125

finalize() {
  local rc=$?
  trap - EXIT
  set +e
  printf 'end_utc=%s\nexit_code=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc" >> "$JOB_DIR/METADATA.txt"
  printf '%s\n' "$rc" > "$JOB_DIR/RUN_STATUS.txt"
  [[ "$rc" -eq 0 ]] && touch "$JOB_DIR/RUN_COMPLETE" || touch "$JOB_DIR/RUN_FAILED"
  find "$JOB_DIR" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$JOB_DIR/EVIDENCE.sha256"
  exit "$rc"
}
trap finalize EXIT

cd "$SOURCE_ROOT"
if find . -type f ! -path "./$CASE_REL/SOURCE.sha256" -perm -u=w -print -quit | grep -q .; then
  echo "writable source bytes" >&2
  exit 125
fi
ACTUAL=$(find . -type f ! -path "./$CASE_REL/SOURCE.sha256" -print | sed 's#^./##' | LC_ALL=C sort)
MANIFEST=$(awk '{print $2}' "$CASE_REL/SOURCE.sha256" | LC_ALL=C sort)
[[ "$ACTUAL" == "$MANIFEST" ]] || { echo "source coverage mismatch" >&2; exit 125; }
sha256sum -c "$CASE_REL/SOURCE.sha256" > "$JOB_DIR/source_check.stdout"

{
  printf 'tag=%s\nengine=%s\n' "$TAG" "$ENGINE_REL"
  printf 'start_utc=%s\ninstance=%s\nproduct=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$AWS_INSTANCE_ID" "$AWS_PRODUCT"
  printf 'memory_cap_kb=%s\nwall_seconds=%s\navailable_before=%s\nswap_before=%s\n' "$MEMORY_KB" "$WALL_SECONDS" "$AVAILABLE" "$SWAP_USED"
  printf 'singular_sha256=%s\n' "$SINGULAR_SHA256"
} > "$JOB_DIR/METADATA.txt"
ps -eo pid,ppid,state,etimes,pcpu,rss,vsz,comm,args --sort=-rss > "$JOB_DIR/prelaunch_processes.txt"

ulimit -v "$MEMORY_KB"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
set +e
timeout --signal=TERM --kill-after=120 300 /usr/bin/time -v \
  python3 -B "$CASE_DIR/verify_tail7_branches.py" \
  > "$JOB_DIR/verify.stdout" 2> "$JOB_DIR/verify.stderr"
VERIFY_RC=$?
set -e
printf '%s\n' "$VERIFY_RC" > "$JOB_DIR/verify.rc"
[[ "$VERIFY_RC" -eq 0 ]] || exit "$VERIFY_RC"
set +e
timeout --signal=TERM --kill-after=120 "$WALL_SECONDS" /usr/bin/time -v \
  /usr/bin/Singular -q "$CASE_DIR/$ENGINE_REL" \
  > "$JOB_DIR/engine.stdout" 2> "$JOB_DIR/engine.stderr"
ENGINE_RC=$?
set -e
printf '%s\n' "$ENGINE_RC" > "$JOB_DIR/engine.rc"
exit "$ENGINE_RC"
