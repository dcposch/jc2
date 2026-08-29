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
package=cases/max12_812_order2_p0_total_rees_t_rs0_degscan_v4_20260826
stream_package=cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826
case "$characteristic" in 0|32003|65521|1000033) ;; *) exit 66 ;; esac
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\nlauncher_pid=%s\njob_dir=%s\nstart_utc=%s\n' \
    "$tag" "$(hostname)" "$$" "$aws_job" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\ncompile_timeout_seconds=%s\nengine_timeout_seconds=%s\nvirtual_memory_cap_kib=%s\nsource_archive_sha256=%s\n' \
    "$characteristic" "$compile_timeout" "$engine_timeout" "$cap_kib" "$archive_sha"
  printf 'singular_version=%s\n' "$(Singular --version 2>&1 | head -1)"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c "$package/FREEZE.sha256" > "$aws_job/freeze_check.stdout"
sha256sum -c "$stream_package/FREEZE.sha256" > "$aws_job/stream_freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"

set +e
timeout "$compile_timeout" python3 "$package/compile_t_rs0_degscan.py" \
  "$aws_job/compiled" --characteristic "$characteristic" \
  > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi

label="p${characteristic}"
if [[ "$characteristic" -eq 0 ]]; then label=q; fi
input="$aws_job/compiled/t_rs0_degscan_${label}.sing"
sha256sum "$input" "$aws_job/compiled/result.json" > "$aws_job/compiled.sha256"

set +e
bash ops/aws_exact_lane.sh "$aws_root" "$aws_job/run" "$tag" \
  timeout "$engine_timeout" Singular -q "$input"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/engine.validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$aws_job/engine.validation"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$aws_job/engine.validation"
  exit "$engine_rc"
fi

stdout="$aws_job/run/$tag.stdout"
meta="$aws_job/run/$tag.meta"
set +e
python3 "$stream_package/validate_t_rs0_stream.py" \
  --stdout "$stdout" --meta "$meta" \
  --compiler-result "$aws_job/compiled/result.json" \
  --input "$input" --output "$aws_job/DISCOVERY.json" \
  --characteristic "$characteristic" \
  > "$aws_job/validator.stdout" 2> "$aws_job/validator.stderr"
validator_rc=$?
set -e
printf 'validator_rc=%s\n' "$validator_rc" > "$aws_job/validator.validation"
if [[ "$validator_rc" -ne 0 ]]; then
  printf 'validator=FAIL_STREAM_PARSER\n' >> "$aws_job/validator.validation"
  exit "$validator_rc"
fi
printf 'validator=PASS_T_RS0_DEGSCAN_V4_NAVIGATION_ONLY\n' >> "$aws_job/validator.validation"
sha256sum "$aws_job/DISCOVERY.json" "$stdout" "$meta" "$aws_job/run/$tag.stderr" \
  > "$aws_job/EVIDENCE.sha256"
