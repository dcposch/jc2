#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true); if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 8 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; cap_kib=$4; config=$5; characteristic=$6; compile_timeout=$7; engine_timeout=$8
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\nlauncher_pid=%s\njob_dir=%s\nstart_utc=%s\n' "$tag" "$(hostname)" "$$" "$aws_job" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'config=%s\ncharacteristic=%s\ncompile_timeout_seconds=%s\nengine_timeout_seconds=%s\nvirtual_memory_cap_kib=%s\n' "$config" "$characteristic" "$compile_timeout" "$engine_timeout" "$cap_kib"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c cases/max12_812_order2_square_third_tail_sharp_v2_20260826/FREEZE.sha256 > "$aws_job/freeze_check.stdout"
sha256sum -c cases/max12_812_order2_square_third_tail_sharp_20260826/FREEZE.sha256 >> "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 cases/max12_812_order2_square_third_tail_sharp_v2_20260826/compile_square_third_tail_sharp_v2.py "$aws_job/compiled" --config "$config" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
label="p${characteristic}"; if [[ "$characteristic" -eq 0 ]]; then label=q; fi
input="$aws_job/compiled/square_third_sharp_v2_${config}_${label}.sing"
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
  'SQUARE_THIRD_SHARP_SOURCE_HASHES=PASS' \
  'SQUARE_THIRD_SHARP_V2_PATCH=DERIVATIVE_FACTORIAL' \
  "SQUARE_THIRD_SHARP_CONFIG=$config" \
  'SQUARE_THIRD_SHARP_LAMBDA3_DIVISIBLE=1' \
  'SQUARE_THIRD_SHARP_QUOTIENT_IDENTITIES=1' \
  'SQUARE_THIRD_SHARP_POLYNOMIAL_MOTIONS_ABSENT=1' \
  'SQUARE_THIRD_SHARP_V2_EXTRACTOR_CONTROL=1' \
  'SQUARE_THIRD_SHARP_ROW_TRANSFORM_UNIT_DIAGONAL=1' \
  'SQUARE_THIRD_SHARP_ROW_IDENTITIES=1' \
  'SQUARE_THIRD_SHARP_P_MOD_L_MINUS_M3=1' \
  'SQUARE_THIRD_SHARP_RAW_R_S_RETAINED=1' \
  'SQUARE_THIRD_SHARP_ENDPOINT=PASS_COMPLETE_SOURCE_THIRD_TAIL'
do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90; fi
done
if [[ "$config" == "p0moving" ]]; then
  for required in 'SQUARE_THIRD_SHARP_P0_CONSTANT_MINUS_BETA3=1' 'SQUARE_THIRD_SHARP_P0_Z3_MINUS_ALPHA3=1'; do
    if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"; exit 90; fi
  done
fi
if grep -Fq '=FAIL' "$stdout" || grep -Eq '^\? ' "$stdout"; then printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"; exit 90; fi
printf 'validator=PASS_SQUARE_THIRD_SHARP_V2\n' >> "$validation"
