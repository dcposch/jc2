#!/usr/bin/env bash
set -euo pipefail

TD6_ROOT=/home/ubuntu/td6-aws-handoff-20260824
TD6_PYTHON=/home/ubuntu/venvs/td6/bin/python
TD6_LANE=/home/ubuntu/aws_td6_v4_lane.sh
TD6_TAG=td6_v4_$(date -u +%Y%m%dT%H%M%SZ)
TD6_RUN=$TD6_ROOT/runs/$TD6_TAG

mkdir -p "$TD6_RUN"
cd "$TD6_ROOT"
sha256sum -c SOURCE.sha256 > "$TD6_RUN/source_verify.stdout" 2> "$TD6_RUN/source_verify.stderr"
{
  printf 'tag=%s\n' "$TD6_TAG"
  printf 'host=%s\n' "$(hostname)"
  printf 'launch_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'archive_sha256=%s\n' '4bb6352397a8f608345e11560687d9c8ef444e3f009f8b5cc4ba05c08674755e'
  printf 'python=%s\n' "$($TD6_PYTHON --version 2>&1)"
  printf 'python_flint=%s\n' "$($TD6_PYTHON -c 'import flint; print(flint.__version__)')"
} > "$TD6_RUN/launch.meta"

launch_lane() {
  TD6_NAME=$1
  shift
  nohup "$TD6_LANE" "$TD6_ROOT" "$TD6_RUN" "$TD6_NAME" "$@" \
    > "$TD6_RUN/$TD6_NAME.supervisor" 2>&1 &
  printf '%s %s\n' "$!" "$TD6_NAME" >> "$TD6_RUN/pids"
}

launch_lane eps2 \
  jc2/cases/td6_c1_c3_first_ideal_eps2_20260824/replay.py
launch_lane generic \
  jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py
launch_lane b_local \
  jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --b-local-pivots
launch_lane u_zero \
  jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=u-zero
launch_lane h_zero \
  jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=h-zero
launch_lane intersection \
  jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=intersection

printf '%s\n' "$TD6_RUN"
