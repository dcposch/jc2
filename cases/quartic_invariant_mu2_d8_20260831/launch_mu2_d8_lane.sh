#!/usr/bin/env bash
# Remote orphan-safe launcher for one source-hash-pinned degree-eight lane.
set -euo pipefail

if (( $# != 7 )); then
  echo "usage: $0 SUFFIX EXPECTED_INSTANCE_ID CHARACTERISTIC PROFILE ENGINE MEMORY_KIB TIMEOUT_SECONDS" >&2
  exit 125
fi

readonly SUFFIX=$1
readonly EXPECTED_INSTANCE_ID=$2
readonly CHARACTERISTIC=$3
readonly PROFILE=$4
readonly ENGINE=$5
readonly MEMORY_KIB=$6
readonly TIMEOUT_SECONDS=$7
[[ "$SUFFIX" =~ ^[A-Za-z0-9][A-Za-z0-9_-]{0,95}$ ]] || { echo "malformed lane suffix" >&2; exit 125; }

readonly SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
readonly RUNNER=$SCRIPT_DIR/aws_mu2_d8_run.sh
readonly LANE_TAG=quartic_inv_mu2_d8_$SUFFIX
readonly JOB_ROOT=/home/ubuntu/jobs/$LANE_TAG
readonly SUPERVISOR=/home/ubuntu/jobs/.$LANE_TAG.supervisor.log
readonly RUNNER_SHA=2d26b0f1a2ca2e27d3bc055b07c7d38030fa16cb23ee1a67733dfb3d2a420545
readonly GENERATOR_SHA=882a18964c5cd00971fb04191469241c08a6ed2064b32cb7fce8e0210cfda755
readonly GIT_BASIS=4e9c6646e91faabc0eb44498b9e30bca6a0af7e6

mkdir -p /home/ubuntu/jobs
if [[ -e "$JOB_ROOT" || -e "$SUPERVISOR" ]]; then
  echo "refusing duplicate lane artifacts: $LANE_TAG" >&2
  exit 125
fi

umask 077
nohup setsid bash "$RUNNER" \
  "$JOB_ROOT" "$LANE_TAG" "$EXPECTED_INSTANCE_ID" \
  "$CHARACTERISTIC" "$PROFILE" "$ENGINE" "$MEMORY_KIB" "$TIMEOUT_SECONDS" \
  "$RUNNER_SHA" "$GENERATOR_SHA" "$GIT_BASIS" \
  </dev/null >"$SUPERVISOR" 2>&1 &
readonly PID=$!
printf 'lane=%s pid=%s job_root=%s supervisor=%s\n' \
  "$LANE_TAG" "$PID" "$JOB_ROOT" "$SUPERVISOR"
