#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 || $# -gt 6 ]]; then
  echo "usage: $0 UTC_STAMP SUFFIX [MODE [MEMORY_KB [WALL_SECONDS [THREADS]]]]" >&2
  exit 64
fi
STAMP=$1
SUFFIX=$2
MODE=${3:-compile_reduce}
MEMORY_KB=${4:-471859200}
WALL_SECONDS=${5:-21600}
THREADS=${6:-1}
case "$STAMP" in *[!0-9TZ]*) echo "invalid UTC stamp" >&2; exit 65;; esac
case "$SUFFIX" in *[!a-zA-Z0-9_-]*) echo "invalid suffix" >&2; exit 65;; esac
case "$MODE" in
  compile_reduce|exact_raw|exact_raw_dp|modp_raw|modp_raw_dp|modp_raw_msolve|exact_row_rref|exact_row_rref_dp|exact_prefix_quotient|exact_homogeneous_sat|exact_tail_deformation|exact_tail10_deformation|modp_row_rref|tracked_row_rref) ;;
  *) echo "invalid mode: $MODE" >&2; exit 65;;
esac
case "$MEMORY_KB:$WALL_SECONDS:$THREADS" in
  *[!0-9:]*|:*|*::*|*:) echo "caps and thread count must be positive integers" >&2; exit 65;;
esac
if [[ "$MEMORY_KB" -eq 0 || "$WALL_SECONDS" -eq 0 || "$THREADS" -eq 0 ]]; then
  echo "caps and thread count must be positive" >&2
  exit 65
fi
if [[ "$MEMORY_KB" -gt 471859200 || "$WALL_SECONDS" -gt 21600 ]]; then
  echo "caps exceed preregistered 450-GiB VM / six-hour envelope" >&2
  exit 65
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
  exact_prefix_quotient)
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
  echo "caps exceed mode-specific preregistration" >&2
  exit 65
fi

REPO=$(cd "$(dirname "$0")/../.." && pwd -P)
CASE_REL=cases/ggv_8_28_upper_endpoint_branch_p_20260827
TAG="ggv_8_28_upper_endpoint_branch_p_${STAMP}_${SUFFIX}"
REMOTE_SOURCE="/home/ubuntu/jobs/$TAG/source"
REMOTE_JOB="/home/ubuntu/jobs/$TAG/output"
SSH_TARGET=ubuntu@98.80.65.144
SSH_OPTIONS=(-i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes -o ConnectTimeout=10)
ARCHIVE=$(mktemp -t ggv-upper-p-endpoint.XXXXXX.tar.gz)
trap 'rm -f "$ARCHIVE"' EXIT

cd "$REPO"
ACTUAL_CASE_FILES=$(find "$CASE_REL" -type f ! -name SOURCE.sha256 -print | LC_ALL=C sort)
MANIFEST_CASE_FILES=$(awk -v prefix="$CASE_REL/" '$2 ~ "^" prefix && $2 !~ /SOURCE.sha256$/ {print $2}' \
  "$CASE_REL/SOURCE.sha256" | LC_ALL=C sort)
if [[ "$ACTUAL_CASE_FILES" != "$MANIFEST_CASE_FILES" ]]; then
  echo "source manifest does not cover the exact case file set" >&2
  exit 68
fi
sha256sum -c "$CASE_REL/SOURCE.sha256" >/dev/null
COPYFILE_DISABLE=1 tar --no-xattrs -czf "$ARCHIVE" \
  "$CASE_REL" \
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md \
  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md \
  xmodel/ideation-20260827T1808Z-sol.md

if ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" "test -e '/home/ubuntu/jobs/$TAG'"; then
  echo "refusing existing remote namespace: $TAG" >&2
  exit 66
fi
read -r REMOTE_HOST REMOTE_PRODUCT REMOTE_AVAILABLE REMOTE_SWAP_USED < <(
  ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" \
    "printf '%s ' \"\$(hostname)\" \"\$(tr -d '\\n' < /sys/class/dmi/id/product_name)\"; free -b | awk 'NR==2{a=\$7} NR==3{print a,\$3}'"
)
if [[ "$REMOTE_HOST" != "ip-172-30-0-249" || "$REMOTE_PRODUCT" != "r6i.16xlarge" ]]; then
  echo "refusing non-Box03 target: host=$REMOTE_HOST product=$REMOTE_PRODUCT" >&2
  exit 67
fi
MIN_HEADROOM_BYTES=161061273600
CAP_BYTES=$((MEMORY_KB * 1024))
if [[ "$REMOTE_SWAP_USED" -ne 0 ]]; then
  echo "refusing launch with nonzero swap" >&2
  exit 67
fi
HEADROOM_ENFORCED=0
case "$MODE" in exact_raw|exact_prefix_quotient) HEADROOM_ENFORCED=1;; esac
if [[ "$HEADROOM_ENFORCED" -eq 1 &&
      "$REMOTE_AVAILABLE" -lt $((CAP_BYTES + MIN_HEADROOM_BYTES)) ]]; then
  echo "refusing launch without 150-GiB requested-cap headroom" >&2
  exit 67
fi
ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" "mkdir -p '$REMOTE_SOURCE'"
scp "${SSH_OPTIONS[@]}" "$ARCHIVE" "$SSH_TARGET:$REMOTE_SOURCE/source.tar.gz"
ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" \
  "cd '$REMOTE_SOURCE' && tar -xzf source.tar.gz && chmod -R a-w '$REMOTE_SOURCE' && sha256sum -c '$CASE_REL/SOURCE.sha256' >/dev/null && mkdir -p '$REMOTE_JOB'"
REMOTE_PID=$(ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" \
  "nohup setsid bash '$REMOTE_SOURCE/$CASE_REL/run_aws.sh' '$REMOTE_SOURCE' '$REMOTE_JOB' '$TAG' '$MODE' '$MEMORY_KB' '$WALL_SECONDS' '$THREADS' > '$REMOTE_JOB.outer.stdout' 2> '$REMOTE_JOB.outer.stderr' < /dev/null & pid=\$!; printf '%s\\n' \"\$pid\"")
printf 'host=Box03\ntag=%s\nmode=%s\nmemory_kb=%s\nwall_seconds=%s\nthreads=%s\nremote_source=%s\nremote_job=%s\n' \
  "$TAG" "$MODE" "$MEMORY_KB" "$WALL_SECONDS" "$THREADS" "$REMOTE_SOURCE" "$REMOTE_JOB"
printf 'remote_pid=%s\n' "$REMOTE_PID"
