#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "R4-00 R2 exact runner refused non-AWS host" >&2
  exit 125
fi
if [[ $# -ne 8 ]]; then
  echo "usage: $0 AWS_ROOT COMPILED AWS_JOB TAG STAGE CAPRUN RSS_BYTES WALL_SECONDS" >&2
  exit 125
fi
aws_root=$1
compiled=$2
aws_job=$3
lane_tag=$4
stage=$5
caprun=$6
rss_bytes=$7
wall_seconds=$8
if [[ "$stage" != "BASE_LIFT" && "$stage" != "FULL_GRADE19" ]]; then
  echo "R4-00 R2 stage must be BASE_LIFT or FULL_GRADE19" >&2
  exit 125
fi
if [[ -z "$lane_tag" || ! "$lane_tag" =~ ^R400_R2_ || ! "$rss_bytes" =~ ^[1-9][0-9]*$ || ! "$wall_seconds" =~ ^[1-9][0-9]*$ ]]; then
  echo "R4-00 R2 registration malformed" >&2
  exit 125
fi
if [[ -e "$aws_job" ]]; then
  echo "R4-00 R2 job path already exists: $aws_job" >&2
  exit 125
fi
rel=cases/max12_812_order2_u2_62_k00_r400_exact_deciders_20260829
worker="$aws_root/$rel/run_exact_packet.py"
packet="$compiled/R2_${stage}.json"
if [[ ! -f "$worker" || ! -f "$packet" || ! -f "$caprun" || ! -f "$compiled/PACKETS.sha256" ]]; then
  echo "R4-00 R2 frozen input missing" >&2
  exit 125
fi
mkdir -p "$aws_job"
(cd "$compiled" && sha256sum -c PACKETS.sha256) > "$aws_job/PACKETS.verify"
meta="$aws_job/LAUNCH.meta"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'route=R4-00-R2\nstage=%s\n' "$stage"
  printf 'host=%s\n' "$(hostname)"
  printf 'dmi_vendor=%s\n' "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)"
  printf 'dmi_product_uuid=%s\n' "$(cat /sys/class/dmi/id/product_uuid 2>/dev/null | tr -d '\n' || printf unavailable)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'packet_sha256=%s\n' "$(sha256sum "$packet" | cut -d ' ' -f 1)"
  printf 'worker_sha256=%s\n' "$(sha256sum "$worker" | cut -d ' ' -f 1)"
  printf 'caprun_sha256=%s\n' "$(sha256sum "$caprun" | cut -d ' ' -f 1)"
  printf 'python=%s\n' "$(python3 --version 2>&1)"
  printf 'singular=%s\n' "$(Singular --version 2>&1 | head -n 1)"
  printf 'msolve=%s\n' "$(msolve --version 2>&1 | head -n 1 || printf unavailable)"
  printf 'input_characteristic=0\nrandom_seed=NONE_DETERMINISTIC_SINGULAR\n'
  printf 'msolve_unit_basis_consumed=false\n'
  printf 'rss_cap_bytes=%s\nwall_seconds=%s\n' "$rss_bytes" "$wall_seconds"
  printf 'argv=python3 %q %q %q --timeout %q\n' "$worker" "$packet" "$aws_job/output" "$wall_seconds"
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
  --term-grace-seconds 15 \
  --stdout-file "$aws_job/WORKER.stdout" \
  --stderr-file "$aws_job/WORKER.stderr" \
  --telemetry-file "$aws_job/WORKER.caprun.json" \
  --cwd "$aws_root" \
  -- python3 "$worker" "$packet" "$aws_job/output" --timeout "$wall_seconds"
rc=$?
set -e
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$rc"
} >> "$meta"
if [[ "$rc" -ne 0 ]]; then
  exit "$rc"
fi
grep -Eq '^K00_R400_EXACT_ENDPOINT=(EXACT_Q_|RESOURCE_CAP_)' "$aws_job/WORKER.stdout"
find "$aws_job" -type f ! -name 'ENDPOINT.sha256' -print0 | sort -z | \
  xargs -0 sha256sum > "$aws_job/ENDPOINT.sha256.tmp"
mv "$aws_job/ENDPOINT.sha256.tmp" "$aws_job/ENDPOINT.sha256"
