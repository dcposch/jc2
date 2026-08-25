#!/usr/bin/env bash
set -euo pipefail

Q8_ROOT=/home/ubuntu/q8_component_grouping_20260824/jc2
Q8_CASE=$Q8_ROOT/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824
Q8_LANE=/home/ubuntu/aws_exact_lane.sh
Q8_TAG=q8_global_quotient_evidence_$(date -u +%Y%m%dT%H%M%SZ)
Q8_RUN=$Q8_ROOT/runs/$Q8_TAG
mkdir -p "$Q8_RUN"
cd "$Q8_ROOT"

sha256sum -c "$Q8_CASE/MANIFEST.sha256" \
  > "$Q8_RUN/manifest.stdout" 2> "$Q8_RUN/manifest.stderr"
{
  printf 'tag=%s\n' "$Q8_TAG"
  printf 'host=%s\n' "$(hostname)"
  printf 'launch_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'replay_sha256=%s\n' 'f0f52954bed71b65b9219fd497f7ea2bbe6652144c463ca06f03391b87957fdd'
  printf 'hostile_probe_sha256=%s\n' '9238fb05bf950953888f71513c4d7e580e6dd2b48455f2294d024941472bc2c3'
  printf 'virtual_memory_limit_kib=%s\n' '134217728'
} > "$Q8_RUN/launch.meta"

ulimit -v 134217728
nohup "$Q8_LANE" "$Q8_ROOT" "$Q8_RUN" frozen_replay \
  /usr/bin/python3 "$Q8_CASE/replay.py" \
  > "$Q8_RUN/frozen_replay.supervisor" 2>&1 &
printf '%s frozen_replay\n' "$!" >> "$Q8_RUN/pids"

nohup "$Q8_LANE" "$Q8_ROOT" "$Q8_RUN" hostile_probe \
  /usr/bin/env JC2_ROOT="$Q8_ROOT" /usr/bin/python3 "$Q8_ROOT/q8gq_probe.py" \
  > "$Q8_RUN/hostile_probe.supervisor" 2>&1 &
printf '%s hostile_probe\n' "$!" >> "$Q8_RUN/pids"
printf '%s\n' "$Q8_RUN"
