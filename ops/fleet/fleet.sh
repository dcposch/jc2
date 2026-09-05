#!/bin/bash
# jc2 fleet driver — launch/drive/terminate ephemeral CAS workers from math-hq.
# Self-sufficient: no claude-cli key, no IAM instance profile. Workers boot from
# stock Ubuntu 24.04, provision the CAS stack (Singular, msolve, python-flint,
# sympy, qqideal, msolveio) via worker-userdata.sh, and are reached over SSH with
# the jc2-fleet key (private key on math-hq at ~/.ssh/jc2-fleet).
#
# Usage:
#   ops/fleet/fleet.sh launch [COUNT] [TYPE] [spot|ondemand]  # default 1 $DEFAULT_TYPE ondemand; spot ~58% cheaper
#   ops/fleet/fleet.sh ips                        # list workers: id, private IP, provision state
#   ops/fleet/fleet.sh wait <ID...|all>          # block until running + PROVISION_DONE
#   ops/fleet/fleet.sh run <IP> <cmd...>          # ssh exec on a worker
#   ops/fleet/fleet.sh push <IP> <src> <dst>      # rsync math-hq -> worker
#   ops/fleet/fleet.sh pull <IP> <src> <dst>      # rsync worker -> math-hq
#   ops/fleet/fleet.sh term <ID...>               # terminate specific workers
#   ops/fleet/fleet.sh term-all                   # terminate ALL jc2-worker instances
set -eu; (set -o pipefail 2>/dev/null) && set -o pipefail
REGION=us-east-1
AMI=ami-066263bf15bd856de   # jc2-worker-base (math-hq snapshot: Singular+python+repo). Fast boot; apt fallback in userdata if bare.
SG=sg-09ffa8932558f0a79
SUBNET=subnet-948915c9
KEY=jc2-fleet
DEFAULT_TYPE=c7i.4xlarge            # subagent rec: x86 compute; big-mem fallback r7i.4xlarge; cost lever c7g.4xlarge (validate ARM)
HERE="$(cd "$(dirname "$0")" && pwd)"
SSHK="$HOME/.ssh/jc2-fleet"
SSHO="-i $SSHK -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=10"
q(){ aws ec2 "$@" --region $REGION; }
udata(){ sed "s|__JC2_FLEET_PUB__|$(tr -d '\n' < "$HERE/jc2-fleet.pub")|" "$HERE/worker-userdata.sh" | base64 -w0; }

cmd=${1:-help}; shift || true
case "$cmd" in
  launch)
    # launch [COUNT] [TYPE] [spot|ondemand]   (default ondemand; spot ~58% cheaper, restartable batch)
    COUNT=${1:-1}; TYPE=${2:-$DEFAULT_TYPE}; MARKET=${3:-ondemand}; TS=$(date -u +%Y%m%dT%H%M%SZ)
    MOPT=""; [ "$MARKET" = spot ] && MOPT="--instance-market-options MarketType=spot"
    q run-instances --image-id $AMI --instance-type "$TYPE" --count "$COUNT" \
      --key-name $KEY --security-group-ids $SG --subnet-id $SUBNET $MOPT \
      --associate-public-ip-address --user-data "$(udata)" \
      --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=jc2-worker-$TS},{Key=jc2fleet,Value=1},{Key=market,Value=$MARKET},{Key=Owner,Value=${FLEET_OWNER:-${JC2_LANE:-manual}}}]" \
      --query 'Instances[].InstanceId' --output text ;;
  msolve)
    # install the official msolve 0.10.1 (AVX-512 build) on workers; msolveio requires 0.10.x
    MSB=${MSOLVE_BIN:-$HOME/.local/share/jc2/msolve-0.10.1-avx512}
    [ -x "$MSB" ] || MSB=/home/ubuntu/jc2/box/moh14-charts-20260905/tools/msolve-0.10.1-official-intel-avx512/msolve
    for ip in "$@"; do
      scp -q -o StrictHostKeyChecking=no -i $SSHK "$MSB" ubuntu@$ip:/home/ubuntu/msolve-0.10.1 && \
      ssh -o StrictHostKeyChecking=no -i $SSHK ubuntu@$ip 'sudo install -m755 /home/ubuntu/msolve-0.10.1 /usr/local/bin/msolve && msolve -h 2>&1 | grep -oE "0\.[0-9]+\.[0-9]+" | head -1' && echo "msolve 0.10.1 installed on $ip" || echo "msolve install FAILED on $ip"
    done ;;
  ips)
    q describe-instances --filters Name=tag:jc2fleet,Values=1 Name=instance-state-name,Values=running,pending \
      --query 'Reservations[].Instances[].{ID:InstanceId,Priv:PrivateIpAddress,State:State.Name,Type:InstanceType,Owner:Tags[?Key==`Owner`]|[0].Value,Launched:LaunchTime}' --output table ;;
  wait)
    IDS="$*"; [ "$IDS" = all ] && IDS=$(q describe-instances --filters Name=tag:jc2fleet,Values=1 Name=instance-state-name,Values=running,pending --query 'Reservations[].Instances[].InstanceId' --output text)
    for id in $IDS; do
      until [ "$(q describe-instances --instance-ids $id --query 'Reservations[].Instances[].State.Name' --output text)" = running ]; do sleep 8; done
      ip=$(q describe-instances --instance-ids $id --query 'Reservations[].Instances[].PrivateIpAddress' --output text)
      echo -n "$id ($ip) provisioning"; for i in $(seq 1 60); do
        if ssh $SSHO ubuntu@$ip 'test -f ~/PROVISION_DONE' 2>/dev/null; then echo " READY"; ssh $SSHO ubuntu@$ip 'cat ~/PROVISION_VERSIONS' 2>/dev/null; sh "$0" msolve $ip; break; fi
        echo -n .; sleep 20; done; done ;;
  run)  IP=$1; shift; ssh $SSHO ubuntu@$IP "$@" ;;
  push) IP=$1; rsync -az -e "ssh $SSHO" "$2" ubuntu@$IP:"$3" ;;
  pull) IP=$1; rsync -az -e "ssh $SSHO" ubuntu@$IP:"$2" "$3" ;;
  term) q terminate-instances --instance-ids "$@" --query 'TerminatingInstances[].{ID:InstanceId,S:CurrentState.Name}' --output text ;;
  term-all)
    IDS=$(q describe-instances --filters Name=tag:jc2fleet,Values=1 Name=instance-state-name,Values=running,pending,stopped --query 'Reservations[].Instances[].InstanceId' --output text)
    [ -n "$IDS" ] && q terminate-instances --instance-ids $IDS --query 'TerminatingInstances[].{ID:InstanceId,S:CurrentState.Name}' --output text || echo "no workers" ;;
  *) sed -n '2,30p' "$0" ;;
esac
