#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "R4-00 packet build refused non-AWS host" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: $0 AWS_ROOT AWS_JOB REGISTERED_TAG CAPRUN RSS_BYTES WALL_SECONDS" >&2
  exit 125
fi
aws_root=$1
aws_job=$2
lane_tag=$3
caprun=$4
rss_bytes=$5
wall_seconds=$6
if [[ -z "$aws_root" || -z "$aws_job" || -z "$lane_tag" || ! "$rss_bytes" =~ ^[1-9][0-9]*$ || ! "$wall_seconds" =~ ^[1-9][0-9]*$ ]]; then
  echo "R4-00 packet build registration malformed" >&2
  exit 125
fi
if [[ -e "$aws_job" ]]; then
  echo "R4-00 packet build job path already exists: $aws_job" >&2
  exit 125
fi
if [[ ! -f "$caprun" ]]; then
  echo "CAPRUN/v1 missing: $caprun" >&2
  exit 125
fi
rel=cases/max12_812_order2_u2_62_k00_r400_exact_deciders_20260829
builder="$aws_root/$rel/build_r400_packets.py"
if [[ ! -f "$builder" ]]; then
  echo "R4-00 packet builder missing" >&2
  exit 125
fi
mkdir -p "$aws_job"
meta="$aws_job/BUILD.meta"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'dmi_vendor=%s\n' "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)"
  printf 'dmi_product_uuid=%s\n' "$(cat /sys/class/dmi/id/product_uuid 2>/dev/null | tr -d '\n' || printf unavailable)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'builder_sha256=%s\n' "$(sha256sum "$builder" | cut -d ' ' -f 1)"
  printf 'caprun_sha256=%s\n' "$(sha256sum "$caprun" | cut -d ' ' -f 1)"
  printf 'python=%s\n' "$(python3 --version 2>&1)"
  printf 'rss_cap_bytes=%s\n' "$rss_bytes"
  printf 'wall_seconds=%s\n' "$wall_seconds"
  printf 'input_characteristic=0\n'
  printf 'random_seed=NONE_DETERMINISTIC_SOURCE_EXPANSION\n'
  printf 'argv=python3 %q %q\n' "$builder" "$aws_job/compiled"
  uptime
  free -b
  df -B1 "$aws_job"
} > "$meta"
export JC2_REGISTERED_AWS_LANE="$lane_tag"
set +e
python3 "$caprun" \
  --wall-seconds "$wall_seconds" \
  --rss-bytes "$rss_bytes" \
  --rss-sample-seconds 0.1 \
  --term-grace-seconds 10 \
  --stdout-file "$aws_job/BUILD.stdout" \
  --stderr-file "$aws_job/BUILD.stderr" \
  --telemetry-file "$aws_job/BUILD.caprun.json" \
  --cwd "$aws_root" \
  -- python3 "$builder" "$aws_job/compiled"
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
} >> "$meta"
if [[ "$rc" -ne 0 ]]; then
  exit "$rc"
fi
grep -Fqx 'K00_R400_PACKET_ENDPOINT=PASS_EXACT_R400_PACKETS_REBUILT_FROM_FROZEN_LITERAL_SOURCE' \
  <(head -n 1 "$aws_job/BUILD.stdout")
(cd "$aws_job/compiled" && sha256sum -c PACKETS.sha256) > "$aws_job/PACKETS.verify"
find "$aws_job" -type f ! -name 'ENDPOINT.sha256' -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/ENDPOINT.sha256.tmp"
mv "$aws_job/ENDPOINT.sha256.tmp" "$aws_job/ENDPOINT.sha256"
printf 'validator=PASS_EXACT_R400_PACKETS_REBUILT_FROM_FROZEN_LITERAL_SOURCE\n' >> "$meta"
