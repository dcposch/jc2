#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; characteristic=$5; timeout_seconds=$6; source_sha=$7
case "$tag" in max12_812_order2_square_d1_unique_ac_d23_support_*) ;; *) exit 125 ;; esac
if [[ -e "$aws_job" ]]; then exit 125; fi
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"; printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"; printf 'source_archive_sha256=%s\n' "$source_sha"
} > "$aws_job/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_owner_d1_unique_ac_d23_small_a_support_miner_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$timeout_seconds" \
  python3 cases/max12_812_order2_square_owner_d1_unique_ac_d23_small_a_support_miner_20260826/mine_support.py \
  "$aws_job/output" --characteristic "$characteristic"
engine_rc=$?
set -e
stdout="$aws_job/run/${tag}.stdout"; stderr="$aws_job/run/${tag}.stderr"; validation="$aws_job/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$aws_job/output/result.json" "$aws_job/output/support_inventory.json" > "$aws_job/results.sha256"
for required in \
  'D1D23_SUPPORT_SOURCE_HASHES=PASS' \
  'D1D23_SUPPORT_BASELINE_COUNT=18' \
  'D1D23_SUPPORT_SAFE_COUNT=17' \
  'D1D23_SUPPORT_NEGATIVE_COUNT=1' \
  'D1D23_SUPPORT_MAX_TARGET_GRADE=34' \
  'D1D23_SUPPORT_SOLE_NEGATIVE=A1_D3_S1' \
  'D1D23_SUPPORT_C2_COEFFICIENT=3/8' \
  'D1D23_SUPPORT_RA2_NEGATIVE_COEFFICIENT=-3/8' \
  'D1D23_SUPPORT_MODULAR_CONTROL=1' \
  'D1D23_SUPPORT_ENDPOINT=PASS_SUPPORT_CENSUS_NO_EMPTINESS'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if [[ "$(grep -Ec '^D1D23_SUPPORT_INVENTORY_SHA256=[0-9a-f]{64}$' "$stdout" || true)" -ne 1 ]]; then
  printf 'validator=FAIL_INVENTORY_MARKER\n' >> "$validation"; exit 90
fi
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" \
   || grep -Fq 'Traceback' "$stdout" || grep -Fq 'Traceback' "$stderr" \
   || grep -Fq 'error occurred' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
if grep -Eq '^[[:space:]]*Swaps: [1-9]' "$stderr"; then
  printf 'validator=FAIL_NONZERO_SWAP\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_D1_D23_SMALL_A_SUPPORT_CENSUS\n' >> "$validation"
