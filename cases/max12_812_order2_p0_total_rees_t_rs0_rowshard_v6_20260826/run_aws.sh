#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" || $# -ne 8 ]]; then exit 125; fi
aws_root=$1
aws_job=$2
tag=$3
characteristic=$4
cap_kib=$5
compile_timeout=$6
engine_timeout=$7
archive_sha=$8
package=cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v6_20260826
stream_package=cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826
case "$characteristic" in 0|32003|65521|1000033) ;; *) exit 66 ;; esac
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\nlauncher_pid=%s\njob_dir=%s\nstart_utc=%s\n' \
    "$tag" "$(hostname)" "$$" "$aws_job" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\ncompile_timeout_seconds=%s\nengine_timeout_seconds=%s\nper_process_virtual_memory_cap_kib=%s\nsource_archive_sha256=%s\n' \
    "$characteristic" "$compile_timeout" "$engine_timeout" "$cap_kib" "$archive_sha"
  printf 'parallel_row_processes=7\nsingular_version=%s\n' "$(Singular --version 2>&1 | head -1)"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c "$package/FREEZE.sha256" > "$aws_job/freeze_check.stdout"
sha256sum -c "$stream_package/FREEZE.sha256" > "$aws_job/stream_freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"

set +e
timeout "$compile_timeout" python3 "$package/compile_t_rs0_rowshard.py" \
  "$aws_job/compiled" --characteristic "$characteristic" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi

label="p${characteristic}"
if [[ "$characteristic" -eq 0 ]]; then label=q; fi
sha256sum "$aws_job/compiled/result.json" "$aws_job"/compiled/t_rs0_row?_${label}.sing \
  > "$aws_job/compiled.sha256"

declare -a row_pids
set +e
for row in 1 2 3 4 5 6 7; do
  row_run="$aws_job/run/row${row}"
  mkdir -p "$row_run"
  bash ops/aws_exact_lane.sh "$aws_root" "$row_run" "${tag}_row${row}" \
    timeout "$engine_timeout" Singular -q "$aws_job/compiled/t_rs0_row${row}_${label}.sing" &
  row_pids[$row]=$!
done
engine_rc=0
for row in 1 2 3 4 5 6 7; do
  wait "${row_pids[$row]}"
  row_rc=$?
  printf 'row_%s_rc=%s\n' "$row" "$row_rc" > "$aws_job/run/row${row}.validation"
  if [[ "$row_rc" -ne 0 ]]; then engine_rc=$row_rc; fi
done
set -e
printf 'aggregate_row_rc=%s\n' "$engine_rc" > "$aws_job/engine.validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$aws_job/engine.validation"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ROW_ENGINE\n' >> "$aws_job/engine.validation"
  exit "$engine_rc"
fi

set +e
python3 "$package/prepare_certificate.py" \
  --job "$aws_job" --compiler-result "$aws_job/compiled/result.json" \
  --characteristic "$characteristic" \
  --certificate-input "$aws_job/certificate.sing" \
  --output "$aws_job/AGGREGATE_PRE.json" \
  > "$aws_job/prepare.stdout" 2> "$aws_job/prepare.stderr"
prepare_rc=$?
set -e
printf 'prepare_rc=%s\n' "$prepare_rc" > "$aws_job/prepare.validation"
if [[ "$prepare_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ROW_AGGREGATION\n' >> "$aws_job/prepare.validation"
  exit "$prepare_rc"
fi

cert_run="$aws_job/run/certificate"
mkdir -p "$cert_run"
cert_tag="${tag}_certificate"
set +e
bash ops/aws_exact_lane.sh "$aws_root" "$cert_run" "$cert_tag" \
  timeout "$engine_timeout" Singular -q "$aws_job/certificate.sing"
cert_rc=$?
set -e
printf 'certificate_rc=%s\n' "$cert_rc" > "$aws_job/certificate.validation"
if [[ "$cert_rc" -ne 0 ]]; then
  printf 'validator=FAIL_CERTIFICATE_ENGINE\n' >> "$aws_job/certificate.validation"
  exit "$cert_rc"
fi

set +e
python3 "$package/finalize_discovery.py" \
  --pre "$aws_job/AGGREGATE_PRE.json" \
  --compiler-result "$aws_job/compiled/result.json" \
  --certificate-input "$aws_job/certificate.sing" \
  --certificate-stdout "$cert_run/$cert_tag.stdout" \
  --certificate-stderr "$cert_run/$cert_tag.stderr" \
  --certificate-meta "$cert_run/$cert_tag.meta" \
  --characteristic "$characteristic" --output "$aws_job/DISCOVERY.json" \
  > "$aws_job/validator.stdout" 2> "$aws_job/validator.stderr"
validator_rc=$?
set -e
printf 'validator_rc=%s\n' "$validator_rc" > "$aws_job/validator.validation"
if [[ "$validator_rc" -ne 0 ]]; then
  printf 'validator=FAIL_FINAL_DISCOVERY\n' >> "$aws_job/validator.validation"
  exit "$validator_rc"
fi
printf 'validator=PASS_T_RS0_ROW_SHARD_V6_NAVIGATION_ONLY\n' >> "$aws_job/validator.validation"

: > "$aws_job/EVIDENCE.sha256"
for artifact in \
  "$aws_job/DISCOVERY.json" "$aws_job/AGGREGATE_PRE.json" \
  "$aws_job/certificate.sing" "$aws_job/compiled/result.json" \
  "$aws_job"/compiled/Keep*.poly \
  "$aws_job"/run/row*/*.stdout "$aws_job"/run/row*/*.stderr "$aws_job"/run/row*/*.meta \
  "$cert_run/$cert_tag.stdout" "$cert_run/$cert_tag.stderr" "$cert_run/$cert_tag.meta"
do
  sha256sum "$artifact" >> "$aws_job/EVIDENCE.sha256"
done
