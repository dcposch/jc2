#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" || $# -ne 8 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4
cap_kib=$5; compile_timeout=$6; engine_timeout=$7; archive_sha=$8
package=cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826
v8=cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826
case "$characteristic" in 0|32003|65521|1000033) ;; *) exit 66 ;; esac
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\nlauncher_pid=%s\njob_dir=%s\nstart_utc=%s\n' "$tag" "$(hostname)" "$$" "$aws_job" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\ncompile_timeout_seconds=%s\nengine_timeout_seconds=%s\nper_process_virtual_memory_cap_kib=%s\nsource_archive_sha256=%s\n' "$characteristic" "$compile_timeout" "$engine_timeout" "$cap_kib" "$archive_sha"
  printf 'parallel_row_processes=7\nsingular_version=%s\n' "$(Singular --version 2>&1 | head -1)"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c "$package/FREEZE.sha256" > "$aws_job/freeze_check.stdout"
sha256sum -c "$v8/FREEZE.sha256" > "$aws_job/v8_freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 "$package/compile_coeffexport_v9.py" "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
label="p${characteristic}"; if [[ "$characteristic" -eq 0 ]]; then label=q; fi
declare -a row_pids
set +e
for row in 1 2 3 4 5 6 7; do
  row_run="$aws_job/run/row${row}"; mkdir -p "$row_run"
  bash ops/aws_exact_lane.sh "$aws_root" "$row_run" "${tag}_row${row}" timeout "$engine_timeout" Singular -q "$aws_job/compiled/t_rs0_row${row}_${label}.sing" &
  row_pids[$row]=$!
done
engine_rc=0
for row in 1 2 3 4 5 6 7; do
  wait "${row_pids[$row]}"; row_rc=$?
  printf 'row_%s_rc=%s\n' "$row" "$row_rc" > "$aws_job/run/row${row}.validation"
  if [[ "$row_rc" -ne 0 ]]; then engine_rc=$row_rc; fi
done
set -e
printf 'aggregate_row_rc=%s\n' "$engine_rc" > "$aws_job/engine.validation"
if [[ "$engine_rc" -ne 0 ]]; then exit "$engine_rc"; fi
set +e
python3 "$package/validate_coeffexport_v9.py" --job "$aws_job" --compiler-result "$aws_job/compiled/result.json" --characteristic "$characteristic" --output "$aws_job/COEFFICIENTS.json" > "$aws_job/validator.stdout" 2> "$aws_job/validator.stderr"
validator_rc=$?
set -e
printf 'validator_rc=%s\n' "$validator_rc" > "$aws_job/validator.validation"
if [[ "$validator_rc" -ne 0 ]]; then exit "$validator_rc"; fi
printf 'validator=PASS_T_RS0_EXACT_COEFFICIENT_EXPORT_V9\n' >> "$aws_job/validator.validation"
: > "$aws_job/EVIDENCE.sha256"
for artifact in "$aws_job/COEFFICIENTS.json" "$aws_job/compiled/result.json" "$aws_job"/compiled/[TF]g*.poly "$aws_job"/run/row*/*.stdout "$aws_job"/run/row*/*.stderr "$aws_job"/run/row*/*.meta; do
  sha256sum "$artifact" >> "$aws_job/EVIDENCE.sha256"
done

