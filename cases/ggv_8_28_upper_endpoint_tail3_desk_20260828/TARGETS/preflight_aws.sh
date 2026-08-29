#!/usr/bin/env bash
set -euo pipefail

case_dir=$(cd "$(dirname "$0")/.." && pwd -P)
required_mem_gib=${1:?required aggregate memory GiB}
required_disk_gib=${2:?required free disk GiB}
mode=${3:?mode}
scope=${4:?scope}
selected_charts=${5:?selected chart list}
allowed_instance_ids=(
  i-07eeaf8ba6f0bc419  # r6d
  i-040b7a1c2ed72d4cc  # r6c
  i-02cb2b4a379ffcc64  # r6a
)
expected_singular_sha=90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4

cd "$case_dir"
sha256sum -c SOURCE.sha256
sha256sum -c EVIDENCE.sha256
python3 analyze_tail3.py --check --output .

if [[ ! -s TARGETS/tail3_v_nonzero_d22_target.json ]]; then
  echo "STOP: frozen target JSON missing" >&2
  exit 19
fi
for required_command in python3 sha256sum setsid prlimit timeout curl ps awk; do
  command -v "$required_command" >/dev/null || {
    echo "STOP: missing command $required_command" >&2
    exit 19
  }
done
[[ -x /usr/bin/time ]] || { echo "STOP: /usr/bin/time missing" >&2; exit 19; }
singular_path=$(command -v Singular)
actual_singular_sha=$(sha256sum "$singular_path" | awk '{print $1}')
if [[ "$actual_singular_sha" != "$expected_singular_sha" ]]; then
  echo "STOP: Singular hash mismatch: $actual_singular_sha" >&2
  exit 20
fi

token=$(curl -fsS --connect-timeout 2 --max-time 4 -X PUT \
  -H 'X-aws-ec2-metadata-token-ttl-seconds: 60' \
  http://169.254.169.254/latest/api/token) || {
    echo "STOP: cannot acquire AWS instance metadata token" >&2
    exit 21
  }
instance_id=$(curl -fsS --connect-timeout 2 --max-time 4 \
  -H "X-aws-ec2-metadata-token: $token" \
  http://169.254.169.254/latest/meta-data/instance-id) || {
    echo "STOP: cannot read AWS instance id" >&2
    exit 21
  }
authorized=0
for allowed in "${allowed_instance_ids[@]}"; do
  if [[ "$instance_id" == "$allowed" ]]; then authorized=1; break; fi
done
if (( authorized == 0 )); then
  echo "STOP: instance $instance_id is outside the frozen host registry" >&2
  exit 21
fi
if [[ "$scope" == root ]]; then
  if [[ "$instance_id" != i-07eeaf8ba6f0bc419 || "$selected_charts" != none ]]; then
    echo "STOP: root diagnostic is pinned to r6d with no chart list" >&2
    exit 21
  fi
elif [[ "$mode" == mod ]]; then
  if [[ "$instance_id" != i-07eeaf8ba6f0bc419 || "$selected_charts" != 0,1,2,3,4,5 ]]; then
    echo "STOP: modular recon is pinned to explicit all-six on r6d" >&2
    exit 21
  fi
else
  case "$instance_id:$selected_charts" in
    i-02cb2b4a379ffcc64:0,1) ;; # r6a
    i-040b7a1c2ed72d4cc:2,3) ;; # r6c
    i-07eeaf8ba6f0bc419:4,5) ;; # r6d
    *)
      echo "STOP: exact chart pair does not match frozen host assignment" >&2
      exit 21
      ;;
  esac
fi

swap_total_kib=$(awk '/^SwapTotal:/ {print $2}' /proc/meminfo)
swap_free_kib=$(awk '/^SwapFree:/ {print $2}' /proc/meminfo)
swap_used_kib=$((swap_total_kib - swap_free_kib))
if (( swap_total_kib != 0 || swap_used_kib != 0 )); then
  echo "STOP: swap configured/used (${swap_total_kib}/${swap_used_kib} KiB)" >&2
  exit 22
fi

available_kib=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
required_kib=$((required_mem_gib * 1024 * 1024))
if (( available_kib < required_kib )); then
  echo "STOP: MemAvailable ${available_kib}KiB < ${required_kib}KiB" >&2
  exit 23
fi

available_bytes=$(df -PB1 "$case_dir" | awk 'NR==2 {print $4}')
required_bytes=$((required_disk_gib * 1024 * 1024 * 1024))
if (( available_bytes < required_bytes )); then
  echo "STOP: disk available ${available_bytes}B < ${required_bytes}B" >&2
  exit 24
fi

heavy=$(ps -u "$(id -u)" -o pid=,comm=,rss=,args= | awk '
  $2 ~ /^(Singular|sage|M2)$/ {print; next}
  $2 ~ /^python/ && $3 > 1048576 {print}
')
if [[ -n "$heavy" ]]; then
  echo "STOP: pre-existing heavy user process" >&2
  echo "$heavy" >&2
  exit 25
fi

# Mirror the worker process topology with a bounded memory-using dummy.  The
# preflight fails unless the recorded PGID accounts for the actual child RSS
# and validated TERM removes every namespace-bound descendant.
"$case_dir/TARGETS/regress_process_group_control.sh"

echo "PREFLIGHT=PASS"
echo "INSTANCE_ID=$instance_id"
echo "HOSTNAME=$(hostname)"
echo "SINGULAR=$singular_path"
echo "SINGULAR_SHA256=$actual_singular_sha"
echo "MEM_AVAILABLE_KIB=$available_kib"
echo "DISK_AVAILABLE_BYTES=$available_bytes"
echo "SWAP_TOTAL_KIB=$swap_total_kib"
echo "SWAP_USED_KIB=$swap_used_kib"
