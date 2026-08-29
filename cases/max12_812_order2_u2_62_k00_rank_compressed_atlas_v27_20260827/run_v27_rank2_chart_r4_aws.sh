#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V27 R4 selected-chart runner refused host" >&2
  exit 125
fi
if [[ $# -ne 10 ]]; then
  echo "usage: $0 SOURCE_ROOT JOB_ROOT TAG VMEM_KIB OUTER_TIMEOUT INNER_TIMEOUT FREEZE_REL EXPECTED_FREEZE_SHA256 SOURCE_ARCHIVE EXPECTED_ARCHIVE_SHA256" >&2
  exit 125
fi
k00_source_root=$1
k00_job_root=$2
k00_lane_tag=$3
k00_cap_kib=$4
k00_outer_timeout=$5
k00_inner_timeout=$6
k00_freeze_rel=$7
k00_expected_freeze_sha=$8
k00_source_archive=$9
k00_expected_archive_sha=${10}
k00_case_rel=cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827
case "$k00_lane_tag" in
  max12_812_order2_u2_62_k00_v27_r4_rank2_chart_*_r6a) ;;
  *) echo "malformed registered V27 R4 selected-chart lane" >&2; exit 125 ;;
esac
if [[ "$k00_cap_kib" != 402653184 ]] || \
   [[ "$k00_outer_timeout" != 21600 ]] || [[ "$k00_inner_timeout" != 21000 ]]; then
  echo "R4 resource envelope mismatch" >&2
  exit 125
fi
if [[ ! -d "$k00_source_root" ]] || [[ ! -f "$k00_source_archive" ]] || \
   [[ -e "$k00_job_root" ]]; then
  echo "source/archive missing or job not fresh" >&2
  exit 125
fi
if find "$k00_source_root" -type f -perm /222 -print -quit | grep -q .; then
  echo "immutable source tree contains writable file" >&2
  exit 125
fi
k00_freeze="$k00_source_root/$k00_freeze_rel"
if [[ ! -f "$k00_freeze" ]] || \
   [[ "$(sha256sum "$k00_freeze" | awk '{print $1}')" != "$k00_expected_freeze_sha" ]] || \
   [[ "$(sha256sum "$k00_source_archive" | awk '{print $1}')" != "$k00_expected_archive_sha" ]]; then
  echo "source custody mismatch" >&2
  exit 125
fi
mkdir -p "$k00_job_root/run"
{
  printf 'tag=%s\nhost=%s\nstart_utc=%s\n' "$k00_lane_tag" "$(hostname)" \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact\nworkers=1\nnice_level=5\n'
  printf 'virtual_memory_cap_kib=%s\nouter_timeout_seconds=%s\ninner_timeout_seconds=%s\n' \
    "$k00_cap_kib" "$k00_outer_timeout" "$k00_inner_timeout"
  printf 'source_freeze_sha256=%s\nsource_archive_sha256=%s\n' \
    "$k00_expected_freeze_sha" "$k00_expected_archive_sha"
  printf 'lifecycle=UNREVIEWED_SPECULATIVE_ROLLBACK_R1_R2_R3\n'
  printf 'selected_chart=I2_rows_5_7_columns_6_7_one_minor_only\n'
  printf 'rational_point_claim=false\nsampled_pencil_claims_consumed=false\n'
  printf 'protected_box02_lanes=R2_R5_NO_SIGNAL_NO_RENICE_NO_MODIFICATION\n'
} > "$k00_job_root/launch_registration.txt"
{
  date -u +snapshot_utc=%Y-%m-%dT%H:%M:%SZ
  free -b
  swapon --show
  ps -eo pid,ppid,stat,etimes,rss,pcpu,comm,args
} > "$k00_job_root/protected_capacity_preflight.txt"
if [[ -n "$(swapon --show --noheadings 2>/dev/null)" ]]; then
  echo "nonzero swap device/state forbidden" >&2
  exit 125
fi
cd "$k00_source_root"
sha256sum -c "$k00_freeze_rel" > "$k00_job_root/freeze_check.stdout"
if [[ ! -s "$k00_job_root/freeze_check.stdout" ]] || \
   grep -Fq ': FAILED' "$k00_job_root/freeze_check.stdout"; then
  echo "source freeze replay failed" >&2
  exit 125
fi
export JC2_REGISTERED_AWS_LANE="$k00_lane_tag"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
ulimit -v "$k00_cap_kib"
set +e
/usr/bin/time -v timeout "$k00_outer_timeout" nice -n 5 python3 -B \
  "$k00_case_rel/run_v27_rank2_chart_r4_exact.py" \
  "$k00_source_root" "$k00_job_root/output" --timeout "$k00_inner_timeout" \
  > "$k00_job_root/run/rank2_chart_r4.stdout" 2> "$k00_job_root/run/rank2_chart_r4.stderr"
k00_rc=$?
set -e
printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$k00_rc" \
  >> "$k00_job_root/launch_registration.txt"
{
  date -u +snapshot_utc=%Y-%m-%dT%H:%M:%SZ
  free -b
  swapon --show
  ps -eo pid,ppid,stat,etimes,rss,pcpu,comm,args
} > "$k00_job_root/protected_capacity_postflight.txt"
k00_postflight_swap=$(swapon --show --noheadings 2>/dev/null || true)
k00_max_rss=$(sed -n 's/^[[:space:]]*Maximum resident set size (kbytes):[[:space:]]*//p' "$k00_job_root/run/rank2_chart_r4.stderr" | tail -n 1)
k00_swaps=$(sed -n 's/^[[:space:]]*Swaps:[[:space:]]*//p' "$k00_job_root/run/rank2_chart_r4.stderr" | tail -n 1)
k00_elapsed=$(sed -n 's/^[[:space:]]*Elapsed (wall clock) time (h:mm:ss or m:ss):[[:space:]]*//p' "$k00_job_root/run/rank2_chart_r4.stderr" | tail -n 1)
printf 'max_rss_kib=%s\nswaps=%s\nelapsed_wall=%s\n' \
  "${k00_max_rss:-MISSING}" "${k00_swaps:-MISSING}" "${k00_elapsed:-MISSING}" \
  > "$k00_job_root/run/TELEMETRY.validation"
k00_validation=DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE
k00_exit=90
if [[ "$k00_rc" -eq 124 ]] || [[ "$k00_rc" -eq 137 ]]; then
  k00_validation=RESOURCE_CAP_NO_VERDICT
  k00_exit=124
elif [[ "$k00_rc" -eq 0 ]] && [[ -s "$k00_job_root/run/rank2_chart_r4.stdout" ]] && \
     [[ -s "$k00_job_root/output/RESULT.json" ]] && \
     [[ "$k00_max_rss" =~ ^[0-9]+$ ]] && [[ "$k00_swaps" == 0 ]] && \
     [[ -z "$k00_postflight_swap" ]] && \
     (( k00_max_rss <= k00_cap_kib )); then
  k00_status=$(python3 -B -c 'import json,sys;print(json.load(open(sys.argv[1]))["status"])' \
    "$k00_job_root/output/RESULT.json")
  case "$k00_status" in
    PASS_V27_R4_SELECTED_I2_CHART_PROPER_ALGEBRAIC_RANK2_POINT_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3|PASS_V27_R4_SELECTED_I2_CHART_UNIT_ONLY_THIS_CHART_EMPTY_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3|RESOURCE_CAP_NO_VERDICT)
      k00_validation=$k00_status
      k00_exit=0
      ;;
    *) ;;
  esac
fi
if [[ "$k00_exit" -eq 0 ]]; then
  python3 -B - "$k00_job_root/output" <<'PY'
from hashlib import sha256
import json
from pathlib import Path
import sys
root = Path(sys.argv[1])
result = json.loads((root / "RESULT.json").read_text())
for name, record in result.get("artifacts", {}).items():
    path = root / name
    if not path.is_file():
        raise SystemExit("missing artifact: " + name)
    data = path.read_bytes()
    if len(data) != record["bytes"] or sha256(data).hexdigest() != record["sha256"]:
        raise SystemExit("artifact mismatch: " + name)
    if not data and not name.endswith(".stderr"):
        raise SystemExit("unexpected empty artifact: " + name)
PY
fi
printf 'engine_rc=%s\nvalidator=%s\n' "$k00_rc" "$k00_validation" \
  > "$k00_job_root/run/FINAL.validation"
(
  cd "$k00_job_root"
  find . -type f ! -name EVIDENCE.sha256 ! -name EVIDENCE.sha256.tmp -print0 \
    | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256.tmp
  mv EVIDENCE.sha256.tmp EVIDENCE.sha256
)
exit "$k00_exit"
