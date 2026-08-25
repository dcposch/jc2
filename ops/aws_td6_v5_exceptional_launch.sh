#!/usr/bin/env bash
set -euo pipefail

TD6_ROOT=/home/ubuntu/td6-v5/td6-aws-handoff-20260824
TD6_PYTHON=/home/ubuntu/venvs/td6/bin/python
TD6_LANE=/home/ubuntu/aws_td6_v4_lane.sh
TD6_TAG=td6_v5_exceptional_$(date -u +%Y%m%dT%H%M%SZ)
TD6_RUN=$TD6_ROOT/runs/$TD6_TAG

mkdir -p "$TD6_RUN"
cd "$TD6_ROOT"
sha256sum -c SOURCE.sha256 > "$TD6_RUN/source_verify.stdout" 2> "$TD6_RUN/source_verify.stderr"
{
  printf 'tag=%s\n' "$TD6_TAG"
  printf 'host=%s\n' "$(hostname)"
  printf 'launch_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'archive_sha256=%s\n' 'c7be01534de522c5404dfe92d857d3b1af580ab680debe462f51fda7a7f6ba2a'
  printf 'two_center_replay_sha256=%s\n' '8b4d6a360b3134fc40aab652ae03f523520b35b4e73a5c41dc646715042f9571'
  printf 'runbook_sha256=%s\n' 'e7bf5077c09f40a089eb0e483d5d2a719cd4a8d3a80ce42346b87c83b1f04e3b'
  printf 'python=%s\n' "$($TD6_PYTHON --version 2>&1)"
  printf 'python_flint=%s\n' "$($TD6_PYTHON -c 'import flint; print(flint.__version__)')"
} > "$TD6_RUN/launch.meta"

nohup "$TD6_LANE" "$TD6_ROOT" "$TD6_RUN" u_zero_v5 \
  jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=u-zero \
  > "$TD6_RUN/u_zero_v5.supervisor" 2>&1 &
printf '%s u_zero_v5\n' "$!" >> "$TD6_RUN/pids"

nohup "$TD6_LANE" "$TD6_ROOT" "$TD6_RUN" intersection_v5 \
  jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=intersection \
  > "$TD6_RUN/intersection_v5.supervisor" 2>&1 &
printf '%s intersection_v5\n' "$!" >> "$TD6_RUN/pids"

printf '%s\n' "$TD6_RUN"
