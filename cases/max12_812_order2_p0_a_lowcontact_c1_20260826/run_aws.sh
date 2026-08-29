#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" || $# -ne 7 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; characteristic=$5; compile_timeout=$6; engine_timeout=$7
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\nlauncher_pid=%s\njob_dir=%s\nstart_utc=%s\n' "$tag" "$(hostname)" "$$" "$aws_job" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\ncompile_timeout_seconds=%s\nengine_timeout_seconds=%s\nvirtual_memory_cap_kib=%s\n' "$characteristic" "$compile_timeout" "$engine_timeout" "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_p0_a_lowcontact_c1_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_p0_a_lowcontact_c1_20260826/compile_p0_a_c1.py "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
label="p${characteristic}"; if [[ "$characteristic" -eq 0 ]]; then label=q; fi
input="$aws_job/compiled/p0_a_c1_${label}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_job/run" "$tag" timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_job/run/$tag.stdout"; validation="$aws_job/run/$tag.validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"; exit 124; fi
if [[ "$engine_rc" -ne 0 ]]; then printf 'validator=FAIL_ENGINE\n' >> "$validation"; exit "$engine_rc"; fi
for required in \
  P0_CUSP_G10_G11_SOURCE_HASHES=PASS \
  P0_CUSP_RAW_G12_CECH_ENDPOINT=PASS_DIRECT_REGISTERED_UNIT_CERTIFICATE \
  P0_A_C1_G11_RAW_TRIANGULAR=1 \
  P0_A_C1_DA0_RAISES_C=1 \
  P0_A_C1_DA1_G12_SQUARE=1 \
  P0_A_C1_ARBITRARY_R_CONTACT_GE1=1 \
  P0_A_C1_ENDPOINT=PASS_FIXED_P0_C_CONTACT_ONE_RAISED
do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90; fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Eq '^\? ' "$stdout"; then printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90; fi
printf 'validator=PASS_P0_A_C1\n' >> "$validation"
