#!/usr/bin/env bash
set -euo pipefail

readonly LAUNCH_TAG=ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d
readonly LAUNCH_STAGE=/home/ubuntu/launch/$LAUNCH_TAG
readonly LAUNCH_JOB_ROOT=/home/ubuntu/jobs/$LAUNCH_TAG
readonly LAUNCH_INSTANCE=i-07eeaf8ba6f0bc419
readonly LAUNCH_HOST=ip-172-30-0-45

[[ "$(uname -s)" == Linux ]]
[[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" == "Amazon EC2" ]]
[[ "$(hostname)" == "$LAUNCH_HOST" ]]
[[ ! -e "$LAUNCH_JOB_ROOT" ]]

export SOURCE_ARCHIVE="$LAUNCH_STAGE/ggv_triple02_proper_open_resume_r5_SOURCE.tar.gz"
export JOB_ROOT="$LAUNCH_JOB_ROOT"
export JOB_TAG="$LAUNCH_TAG"
export CPU_ID=0
export EXPECTED_INSTANCE_ID="$LAUNCH_INSTANCE"
export EXPECTED_HOSTNAME="$LAUNCH_HOST"

exec bash "$LAUNCH_STAGE/aws_launch_preflight.sh"
