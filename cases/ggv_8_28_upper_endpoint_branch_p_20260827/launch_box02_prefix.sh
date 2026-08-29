#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 || $# -gt 4 ]]; then
  echo "usage: $0 UTC_STAMP SUFFIX [launch|--preflight] [std|slimgb]" >&2
  exit 64
fi

STAMP=$1
SUFFIX=$2
ACTION=${3:-launch}
ALGORITHM=${4:-std}
if [[ ! "$STAMP" =~ ^[0-9]{8}T[0-9]{6}Z$ ]]; then
  echo "invalid UTC stamp" >&2
  exit 65
fi
if [[ -z "$SUFFIX" || "$SUFFIX" == *[!a-zA-Z0-9_-]* ]]; then
  echo "invalid suffix" >&2
  exit 65
fi
if [[ "$ACTION" != "launch" && "$ACTION" != "--preflight" ]]; then
  echo "invalid action: $ACTION" >&2
  exit 65
fi
case "$ALGORITHM" in
  std) MODE=exact_prefix_quotient ;;
  slimgb) MODE=exact_prefix_quotient_slimgb ;;
  *) echo "invalid algorithm: $ALGORITHM" >&2; exit 65 ;;
esac

MEMORY_KB=134217728
WALL_SECONDS=7200
THREADS=1
MIN_HEADROOM_BYTES=161061273600
CAP_BYTES=$((MEMORY_KB * 1024))
MIN_AVAILABLE_BYTES=$((CAP_BYTES + MIN_HEADROOM_BYTES))
MAX_START_LOAD1=16.0

AWS_PROFILE_NAME=personal
AWS_REGION_NAME=us-east-1
EXPECTED_INSTANCE_ID=i-010201a5da47795c4
EXPECTED_INSTANCE_TYPE=x2idn.32xlarge
EXPECTED_AMI=ami-052355af2a014bd2c
EXPECTED_SUBNET=subnet-948915c9
EXPECTED_SECURITY_GROUP=sg-09ffa8932558f0a79
EXPECTED_HOST=ip-172-30-0-186
EXPECTED_NPROC=128
EXPECTED_SINGULAR_SHA256=90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4
EXPECTED_KEY_FINGERPRINT=8mg4kK7KYNflkiETs3z8e5H2/w8O0lxHbnuX23ojlfU
KEY_PATH=/Users/dc/.ssh/claude-cli.pem

read -r AWS_STATE AWS_TYPE AWS_IP AWS_AMI AWS_SUBNET AWS_SECURITY_GROUP < <(
  AWS_PROFILE="$AWS_PROFILE_NAME" AWS_REGION="$AWS_REGION_NAME" \
    aws ec2 describe-instances --instance-ids "$EXPECTED_INSTANCE_ID" \
      --query 'Reservations[0].Instances[0].[State.Name,InstanceType,PublicIpAddress,ImageId,SubnetId,SecurityGroups[0].GroupId]' \
      --output text
)
if [[ "$AWS_STATE" != "running" || "$AWS_TYPE" != "$EXPECTED_INSTANCE_TYPE" ||
      "$AWS_AMI" != "$EXPECTED_AMI" || "$AWS_SUBNET" != "$EXPECTED_SUBNET" ||
      "$AWS_SECURITY_GROUP" != "$EXPECTED_SECURITY_GROUP" ||
      -z "$AWS_IP" || "$AWS_IP" == "None" ]]; then
  echo "refusing mismatched Box02 AWS identity: state=$AWS_STATE type=$AWS_TYPE ip=$AWS_IP ami=$AWS_AMI subnet=$AWS_SUBNET sg=$AWS_SECURITY_GROUP" >&2
  exit 67
fi

AWS_KEY_FINGERPRINT=$(AWS_PROFILE="$AWS_PROFILE_NAME" AWS_REGION="$AWS_REGION_NAME" \
  aws ec2 describe-key-pairs --key-names claude-cli \
    --query 'KeyPairs[0].KeyFingerprint' --output text)
LOCAL_KEY_FINGERPRINT=$(ssh-keygen -lf "$KEY_PATH" | awk '{print $2}')
LOCAL_KEY_FINGERPRINT=${LOCAL_KEY_FINGERPRINT#SHA256:}
if [[ "${AWS_KEY_FINGERPRINT%=}" != "$EXPECTED_KEY_FINGERPRINT" ||
      "${LOCAL_KEY_FINGERPRINT%=}" != "$EXPECTED_KEY_FINGERPRINT" ]]; then
  echo "refusing key fingerprint mismatch: aws=$AWS_KEY_FINGERPRINT local=$LOCAL_KEY_FINGERPRINT" >&2
  exit 67
fi

SSH_TARGET="ubuntu@$AWS_IP"
SSH_OPTIONS=(-i "$KEY_PATH" -o BatchMode=yes -o ConnectTimeout=10)
read -r REMOTE_HOST REMOTE_PRODUCT REMOTE_INSTANCE_ID REMOTE_NPROC \
  REMOTE_AVAILABLE REMOTE_SWAP_USED REMOTE_LOAD1 REMOTE_SINGULAR_SHA256 < <(
  ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" \
    "printf '%s ' \"\$(hostname)\" \"\$(tr -d '\\n' < /sys/class/dmi/id/product_name)\" \"\$(tr -d '\\n' < /sys/class/dmi/id/board_asset_tag)\" \"\$(nproc)\"; free -b | awk 'NR==2{a=\$7} NR==3{printf \"%s %s \",a,\$3}'; printf '%s ' \"\$(awk '{print \$1}' /proc/loadavg)\"; sha256sum /usr/bin/Singular | awk '{print \$1}'"
)
if [[ "$REMOTE_HOST" != "$EXPECTED_HOST" ||
      "$REMOTE_PRODUCT" != "$EXPECTED_INSTANCE_TYPE" ||
      "$REMOTE_INSTANCE_ID" != "$EXPECTED_INSTANCE_ID" ||
      "$REMOTE_NPROC" != "$EXPECTED_NPROC" ]]; then
  echo "refusing non-Box02 target: host=$REMOTE_HOST product=$REMOTE_PRODUCT instance=$REMOTE_INSTANCE_ID nproc=$REMOTE_NPROC" >&2
  exit 67
fi
if [[ "$REMOTE_SINGULAR_SHA256" != "$EXPECTED_SINGULAR_SHA256" ]]; then
  echo "refusing unpinned Singular binary: $REMOTE_SINGULAR_SHA256" >&2
  exit 67
fi
if [[ "$REMOTE_SWAP_USED" -ne 0 ]]; then
  echo "refusing launch with nonzero swap: $REMOTE_SWAP_USED" >&2
  exit 67
fi
if [[ "$REMOTE_AVAILABLE" -lt "$MIN_AVAILABLE_BYTES" ]]; then
  echo "refusing launch without 150-GiB requested-cap headroom: available=$REMOTE_AVAILABLE required=$MIN_AVAILABLE_BYTES" >&2
  exit 67
fi
if ! awk -v load_value="$REMOTE_LOAD1" -v maximum="$MAX_START_LOAD1" \
    'BEGIN { exit !(load_value <= maximum) }'; then
  echo "refusing CPU-contended Box02: load1=$REMOTE_LOAD1 maximum=$MAX_START_LOAD1" >&2
  exit 67
fi

REPO=$(cd "$(dirname "$0")/../.." && pwd -P)
CASE_REL=cases/ggv_8_28_upper_endpoint_branch_p_20260827
TAG="ggv_8_28_upper_endpoint_branch_p_${STAMP}_${SUFFIX}"
REMOTE_SOURCE="/home/ubuntu/jobs/$TAG/source"
REMOTE_JOB="/home/ubuntu/jobs/$TAG/output"
ARCHIVE=$(mktemp -t ggv-upper-p-box02.XXXXXX.tar.gz)
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
if [[ "$ACTION" == "--preflight" ]]; then
  printf 'BOX02_PREFIX_PREFLIGHT_PASS instance_id=%s public_ip=%s mode=%s algorithm=%s available_bytes=%s swap_used_bytes=%s nproc=%s load1=%s source_manifest_sha256=%s\n' \
    "$EXPECTED_INSTANCE_ID" "$AWS_IP" "$MODE" "$ALGORITHM" "$REMOTE_AVAILABLE" "$REMOTE_SWAP_USED" \
    "$REMOTE_NPROC" "$REMOTE_LOAD1" \
    "$(sha256sum "$CASE_REL/SOURCE.sha256" | awk '{print $1}')"
  exit 0
fi
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
ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" "mkdir -p '$REMOTE_SOURCE'"
scp "${SSH_OPTIONS[@]}" "$ARCHIVE" "$SSH_TARGET:$REMOTE_SOURCE/source.tar.gz"
ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" \
  "cd '$REMOTE_SOURCE' && tar -xzf source.tar.gz && chmod -R a-w '$REMOTE_SOURCE' && sha256sum -c '$CASE_REL/SOURCE.sha256' >/dev/null && mkdir -p '$REMOTE_JOB'"
REMOTE_PID=$(ssh "${SSH_OPTIONS[@]}" "$SSH_TARGET" \
  "nohup setsid bash '$REMOTE_SOURCE/$CASE_REL/run_aws.sh' '$REMOTE_SOURCE' '$REMOTE_JOB' '$TAG' '$MODE' '$MEMORY_KB' '$WALL_SECONDS' '$THREADS' box02_prefix > '$REMOTE_JOB.outer.stdout' 2> '$REMOTE_JOB.outer.stderr' < /dev/null & pid=\$!; printf '%s\\n' \"\$pid\"")
printf 'host=Box02\ninstance_id=%s\npublic_ip=%s\ntag=%s\nmode=%s\nmemory_kb=%s\nwall_seconds=%s\nthreads=%s\nremote_source=%s\nremote_job=%s\nremote_pid=%s\n' \
  "$EXPECTED_INSTANCE_ID" "$AWS_IP" "$TAG" "$MODE" "$MEMORY_KB" \
  "$WALL_SECONDS" "$THREADS" "$REMOTE_SOURCE" "$REMOTE_JOB" "$REMOTE_PID"
