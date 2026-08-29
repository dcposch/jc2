#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 7 ]]; then exit 125; fi
aws_root=$1; evidence=$2; tag=$3; characteristic=$4; timeout_seconds=$5; cap_kib=$6; source_sha=$7
case "$tag" in max12_812_order2_square_d1_a8d3_connection_rankjump_*) ;; *) exit 125 ;; esac
case "$characteristic" in 0|65519|65521) ;; *) exit 125 ;; esac
if [[ -e "$evidence" ]]; then exit 125; fi
mkdir -p "$evidence/run"
{
  printf 'tag=%s\n' "$tag"; printf 'host=%s\n' "$(hostname)"; printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$evidence"; printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"; printf 'timeout_seconds=%s\n' "$timeout_seconds"
  printf 'virtual_memory_cap_kib=%s\n' "$cap_kib"; printf 'source_archive_sha256=%s\n' "$source_sha"
} > "$evidence/launch_registration.txt"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_owner_d1_a8d3_connection_rankjump_20260826/FREEZE.sha256 > "$evidence/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$evidence/run" "$tag" timeout "$timeout_seconds" \
  python3 cases/max12_812_order2_square_owner_d1_a8d3_connection_rankjump_20260826/analyze_rankjump.py \
  "$evidence/compiled" --characteristic "$characteristic"
engine_rc=$?
set -e
stdout="$evidence/run/${tag}.stdout"; stderr="$evidence/run/${tag}.stderr"; validation="$evidence/validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit 90; fi
sha256sum "$evidence/compiled"/* > "$evidence/compiled.sha256"
for required in \
  'A8D3_RANKJUMP_SOURCE_HASHES=PASS' \
  'A8D3_RANKJUMP_ALPHA_A2=1/4' \
  'A8D3_RANKJUMP_ALPHA_RC=-1/4' \
  'A8D3_RANKJUMP_INCOMPATIBLE_ALPHA=1' \
  'A8D3_RANKJUMP_DETERMINANT_OVER_P=9/512' \
  'A8D3_RANKJUMP_TARGET_ROW7_IN_TWO_COLUMN_SPAN_ON_D_P=1' \
  'A8D3_RANKJUMP_ENDPOINT=PASS_NO_UNIVERSAL_ODD_FUNCTIONAL'; do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Fq '=FAIL' "$stderr" || grep -Fq '// **' "$stdout" \
   || grep -Eq '^[[:space:]]*\? ' "$stdout" || grep -Fq 'error occurred' "$stderr"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90
fi
if grep -Eq '^[[:space:]]*Swaps: [1-9]' "$stderr"; then
  printf 'validator=FAIL_NONZERO_SWAP\n' >> "$validation"; exit 90
fi
printf 'validator=PASS_A8D3_CONNECTION_RANKJUMP\n' >> "$validation"
