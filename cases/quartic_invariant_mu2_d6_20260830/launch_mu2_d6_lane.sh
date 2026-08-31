#!/usr/bin/env bash
# Remote, orphan-safe launcher for one hash-pinned quartic invariant lane.
set -euo pipefail

if (( $# != 7 )); then
  echo "usage: $0 SUFFIX EXPECTED_INSTANCE_ID CHARACTERISTIC JACOBIAN_TARGET ENGINE MEMORY_KIB TIMEOUT_SECONDS" >&2
  exit 125
fi

readonly SUFFIX=$1
readonly EXPECTED_INSTANCE_ID=$2
readonly CHARACTERISTIC=$3
readonly JACOBIAN_TARGET=$4
readonly ENGINE=$5
readonly MEMORY_KIB=$6
readonly TIMEOUT_SECONDS=$7
if [[ ! "$SUFFIX" =~ ^[A-Za-z0-9][A-Za-z0-9_-]{0,95}$ ]]; then
  echo "malformed lane suffix" >&2
  exit 125
fi

readonly SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
readonly RUNNER=$SCRIPT_DIR/aws_mu2_d6_run.sh
readonly LANE_TAG=quartic_inv_mu2_d6_$SUFFIX
readonly JOB_ROOT=/home/ubuntu/jobs/$LANE_TAG
readonly SUPERVISOR=/home/ubuntu/jobs/.$LANE_TAG.supervisor.log
readonly RUNNER_SHA=04b80b51c461efa79783f1b953a93fdfaf8e50c53c8b3112e0d623d756557bac
readonly GENERATOR_SHA=edcbc3796ffae65265a89b10bbd19836d6b5a60cd0c35c561c555c0b6afc5dd1
readonly GIT_BASIS=aa0f341f8553e78a28084eaf51c1e4ffbc2ad21a

mkdir -p /home/ubuntu/jobs
if [[ -e "$JOB_ROOT" || -e "$SUPERVISOR" ]]; then
  echo "refusing duplicate lane artifacts: $LANE_TAG" >&2
  exit 125
fi

umask 077
nohup setsid "$RUNNER" \
  "$JOB_ROOT" "$LANE_TAG" "$EXPECTED_INSTANCE_ID" \
  "$CHARACTERISTIC" "$JACOBIAN_TARGET" "$ENGINE" \
  "$MEMORY_KIB" "$TIMEOUT_SECONDS" "$RUNNER_SHA" "$GENERATOR_SHA" \
  "$GIT_BASIS" \
  </dev/null >"$SUPERVISOR" 2>&1 &
readonly PID=$!
printf 'lane=%s pid=%s job_root=%s supervisor=%s\n' \
  "$LANE_TAG" "$PID" "$JOB_ROOT" "$SUPERVISOR"
