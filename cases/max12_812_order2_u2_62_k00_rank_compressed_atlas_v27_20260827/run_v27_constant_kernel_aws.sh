#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only V27 constant-kernel runner refused host" >&2
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
  max12_812_order2_u2_62_k00_v27_kernel_replay_*_r6a) ;;
  *) echo "malformed registered V27 kernel-replay lane" >&2; exit 125 ;;
esac
if [[ "$k00_cap_kib" != "8388608" ]] || \
   [[ "$k00_outer_timeout" != "600" ]] || \
   [[ "$k00_inner_timeout" != "540" ]]; then
  echo "kernel-replay resource envelope differs from preregistration" >&2
  exit 125
fi
if [[ ! -d "$k00_source_root" ]] || [[ ! -f "$k00_source_archive" ]] || \
   [[ -e "$k00_job_root" ]]; then
  echo "source/archive missing or job directory not fresh" >&2
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
  echo "source freeze/archive digest mismatch" >&2
  exit 125
fi

mkdir -p "$k00_job_root/run"
{
  printf 'tag=%s\n' "$k00_lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=Q_exact\nworkers=1\nnice_level=5\n'
  printf 'virtual_memory_cap_kib=%s\nouter_timeout_seconds=%s\ninner_timeout_seconds=%s\n' \
    "$k00_cap_kib" "$k00_outer_timeout" "$k00_inner_timeout"
  printf 'source_freeze_sha256=%s\nsource_archive_sha256=%s\n' \
    "$k00_expected_freeze_sha" "$k00_expected_archive_sha"
  printf 'lifecycle=AUXILIARY_PRODUCER_UNREVIEWED_EXPLANATORY_ONLY\n'
  printf 'sampled_pencil_claims_consumed=false\n'
} > "$k00_job_root/launch_registration.txt"
{
  date -u +snapshot_utc=%Y-%m-%dT%H:%M:%SZ
  free -b
  swapon --show
  ps -eo pid,ppid,stat,etimes,rss,pcpu,comm,args
} > "$k00_job_root/protected_capacity_preflight.txt"
cd "$k00_source_root"
sha256sum -c "$k00_freeze_rel" > "$k00_job_root/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$k00_lane_tag"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
ulimit -v "$k00_cap_kib"
set +e
/usr/bin/time -v timeout "$k00_outer_timeout" nice -n 5 python3 -B \
  "$k00_case_rel/run_v27_constant_kernel_replay.py" \
  "$k00_source_root" "$k00_job_root/output" --timeout "$k00_inner_timeout" \
  > "$k00_job_root/run/kernel.stdout" 2> "$k00_job_root/run/kernel.stderr"
k00_rc=$?
set -e
printf 'end_utc=%s\nrc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$k00_rc" \
  >> "$k00_job_root/launch_registration.txt"
k00_max_rss=$(sed -n 's/^[[:space:]]*Maximum resident set size (kbytes):[[:space:]]*//p' "$k00_job_root/run/kernel.stderr" | tail -n 1)
k00_swaps=$(sed -n 's/^[[:space:]]*Swaps:[[:space:]]*//p' "$k00_job_root/run/kernel.stderr" | tail -n 1)
k00_elapsed=$(sed -n 's/^[[:space:]]*Elapsed (wall clock) time (h:mm:ss or m:ss):[[:space:]]*//p' "$k00_job_root/run/kernel.stderr" | tail -n 1)
printf 'max_rss_kib=%s\nswaps=%s\nelapsed_wall=%s\n' \
  "${k00_max_rss:-MISSING}" "${k00_swaps:-MISSING}" "${k00_elapsed:-MISSING}" \
  > "$k00_job_root/run/TELEMETRY.validation"
k00_validation=DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE
k00_exit=90
if [[ "$k00_rc" -eq 124 ]] || [[ "$k00_rc" -eq 137 ]]; then
  k00_validation=RESOURCE_CAP_NO_VERDICT
  k00_exit=124
elif [[ "$k00_rc" -eq 0 ]] && [[ "$k00_swaps" == 0 ]] && \
     [[ "$k00_max_rss" =~ ^[0-9]+$ ]] && (( k00_max_rss <= k00_cap_kib )) && \
     [[ -s "$k00_job_root/output/RESULT.json" ]]; then
  k00_status=$(python3 -B -c 'import json,sys;print(json.load(open(sys.argv[1]))["status"])' \
    "$k00_job_root/output/RESULT.json")
  if [[ "$k00_status" == PASS_V27_AUX_CONSTANT_KERNEL_IDENTITIES_EXACT_EXPLANATORY_ONLY ]]; then
    k00_validation=$k00_status
    k00_exit=0
  fi
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
        raise SystemExit(f"missing artifact: {name}")
    data = path.read_bytes()
    if len(data) != record["bytes"] or sha256(data).hexdigest() != record["sha256"]:
        raise SystemExit(f"artifact mismatch: {name}")
    if not data and not name.endswith(".stderr"):
        raise SystemExit(f"unexpected empty artifact: {name}")
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
