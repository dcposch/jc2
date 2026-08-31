#!/usr/bin/env bash
# Ship and start one D8 lane on a freshly audited named campaign worker.
set -euo pipefail

if (( $# != 7 )); then
  echo "usage: $0 HOST SUFFIX CHARACTERISTIC PROFILE ENGINE MEMORY_KIB TIMEOUT_SECONDS" >&2
  exit 125
fi

readonly HOST=$1
readonly SUFFIX=$2
readonly CHARACTERISTIC=$3
readonly PROFILE=$4
readonly ENGINE=$5
readonly MEMORY_KIB=$6
readonly TIMEOUT_SECONDS=$7
case "$HOST" in
  r6a) INSTANCE_ID=i-02cb2b4a379ffcc64 ;;
  r6b) INSTANCE_ID=i-0f089e64c378f5da3 ;;
  r6c) INSTANCE_ID=i-040b7a1c2ed72d4cc ;;
  r6d) INSTANCE_ID=i-07eeaf8ba6f0bc419 ;;
  *) echo "host must be one of r6a,r6b,r6c,r6d" >&2; exit 125 ;;
esac
readonly INSTANCE_ID

readonly SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
readonly REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd -P)
readonly SOURCE_ROOT=/home/ubuntu/jobs/.quartic_inv_mu2_d8_source_d19c494e
readonly IP=$(aws ec2 describe-instances --profile personal --instance-ids "$INSTANCE_ID" \
  --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
[[ -n "$IP" && "$IP" != None ]] || { echo "no running public IP for $HOST" >&2; exit 125; }
readonly TARGET=ubuntu@$IP
readonly SSH_KEY=/Users/dc/.ssh/claude-cli.pem
readonly SSH_OPTIONS=(-i "$SSH_KEY" -o BatchMode=yes -o ConnectTimeout=8)

"$REPO_ROOT/ops/sg_autoupdate.sh"
ssh "${SSH_OPTIONS[@]}" "$TARGET" \
  "test \"\$(tr -d '\\n' </sys/class/dmi/id/board_asset_tag)\" = '$INSTANCE_ID' && ! pgrep -u ubuntu -x Singular >/dev/null && ! pgrep -u ubuntu -x msolve >/dev/null && ! pgrep -u ubuntu -f '[g]enerate_mu2_d8.py|[a]ws_mu2_d8_run.sh' >/dev/null && mkdir -p '$SOURCE_ROOT'"

scp "${SSH_OPTIONS[@]}" \
  "$SCRIPT_DIR/aws_mu2_d8_run.sh" \
  "$SCRIPT_DIR/generate_mu2_d8.py" \
  "$SCRIPT_DIR/launch_mu2_d8_lane.sh" \
  "$TARGET:$SOURCE_ROOT/"

ssh "${SSH_OPTIONS[@]}" "$TARGET" \
  "cd '$SOURCE_ROOT' && test \"\$(sha256sum aws_mu2_d8_run.sh | cut -d ' ' -f 1)\" = '2d26b0f1a2ca2e27d3bc055b07c7d38030fa16cb23ee1a67733dfb3d2a420545' && test \"\$(sha256sum generate_mu2_d8.py | cut -d ' ' -f 1)\" = '44f2d1a47fdd9ee7cfbf8916ab1bf224879f99f3f2f3d9b85efcb773c986be79' && bash launch_mu2_d8_lane.sh '$SUFFIX' '$INSTANCE_ID' '$CHARACTERISTIC' '$PROFILE' '$ENGINE' '$MEMORY_KIB' '$TIMEOUT_SECONDS'"
