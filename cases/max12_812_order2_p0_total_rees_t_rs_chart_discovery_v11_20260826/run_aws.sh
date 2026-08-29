#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" || $# -ne 10 ]]; then exit 125; fi
aws_root=$1
aws_job=$2
tag=$3
characteristic=$4
grade=$5
algorithm=$6
cap_kib=$7
compile_timeout=$8
engine_timeout=$9
archive_sha=${10}
package=cases/max12_812_order2_p0_total_rees_t_rs_chart_discovery_v11_20260826
case "$characteristic" in 0|65521) ;; *) exit 66 ;; esac
case "$grade" in 10|11|12) ;; *) exit 67 ;; esac
case "$algorithm" in sat|elim) ;; *) exit 68 ;; esac
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\n' "$tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'job_dir=%s\n' "$aws_job"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\n' "$characteristic"
  printf 'prefix_grade=%s\n' "$grade"
  printf 'algorithm=%s\n' "$algorithm"
  printf 'compile_timeout_seconds=%s\n' "$compile_timeout"
  printf 'engine_timeout_seconds=%s\n' "$engine_timeout"
  printf 'per_process_virtual_memory_cap_kib=%s\n' "$cap_kib"
  printf 'source_archive_sha256=%s\n' "$archive_sha"
  printf 'singular_version=%s\n' "$(Singular --version 2>&1 | head -1)"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c "$package/FREEZE.sha256" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"
ulimit -v "$cap_kib"
set +e
timeout "$compile_timeout" python3 "$package/compile_chart_discovery_v11.py" \
  "$aws_job/compiled" --characteristic "$characteristic" --grade "$grade" \
  --algorithm "$algorithm" > "$aws_job/compiler.stdout" \
  2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"
if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["script"])' \
  "$aws_job/compiled/result.json")
set +e
bash ops/aws_exact_lane.sh "$aws_root" "$aws_job/run" "$tag" \
  timeout "$engine_timeout" Singular -q "$script"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/engine.validation"
if [[ "$engine_rc" -ne 0 ]]; then exit "$engine_rc"; fi
stdout="$aws_job/run/${tag}.stdout"
stderr="$aws_job/run/${tag}.stderr"
set +e
python3 "$package/validate_chart_discovery_v11.py" --job "$aws_job" \
  --compiler-result "$aws_job/compiled/result.json" --stdout "$stdout" \
  --stderr "$stderr" --characteristic "$characteristic" --grade "$grade" \
  --algorithm "$algorithm" --output "$aws_job/RESULT.json" \
  > "$aws_job/validator.stdout" 2> "$aws_job/validator.stderr"
validator_rc=$?
set -e
printf 'validator_rc=%s\n' "$validator_rc" > "$aws_job/validator.validation"
if [[ "$validator_rc" -ne 0 ]]; then exit "$validator_rc"; fi
printf 'validator=PASS_T_RS_CHART_DISCOVERY_V11\n' \
  >> "$aws_job/validator.validation"
: > "$aws_job/EVIDENCE.sha256"
for artifact in "$aws_job/RESULT.json" "$aws_job/compiled/result.json" \
  "$script" "$aws_job"/compiled/*.ideal "$stdout" "$stderr" \
  "$aws_job"/run/*.meta; do
  sha256sum "$artifact" >> "$aws_job/EVIDENCE.sha256"
done
