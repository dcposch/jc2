#!/usr/bin/env bash
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" || $# -ne 8 ]]; then exit 125; fi
aws_root=$1; aws_job=$2; tag=$3; characteristic=$4; cap_kib=$5; compile_wall=$6; engine_wall=$7; archive_sha=$8
package=cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827
mkdir -p "$aws_job/run"
{
  printf 'tag=%s\nhost=%s\npid=%s\nstart_utc=%s\n' "$tag" "$(hostname)" "$$" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'characteristic=%s\ncap_kib=%s\ncompile_wall=%s\nengine_wall=%s\nsource_archive_sha256=%s\n' "$characteristic" "$cap_kib" "$compile_wall" "$engine_wall" "$archive_sha"
} > "$aws_job/launch_registration.txt"
printf '%s\n' "$$" > "$aws_job/launcher.pid"
cd "$aws_root"
sha256sum -c "$package/FREEZE.sha256" > "$aws_job/freeze_check.stdout"
export JC2_REGISTERED_AWS_LANE="$tag"; ulimit -v "$cap_kib"
set +e
/usr/bin/time -v timeout "$compile_wall" python3 "$package/export_allrows_g15_v22.py" "$aws_job/compiled" --characteristic "$characteristic" > "$aws_job/compiler.stdout" 2> "$aws_job/compiler.stderr"
compiler_rc=$?
set -e
printf 'compiler_rc=%s\n' "$compiler_rc" > "$aws_job/compiler.validation"; if [[ "$compiler_rc" -ne 0 ]]; then exit "$compiler_rc"; fi
script=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["control_script"])' "$aws_job/compiled/result.json")
engine_tag="${tag}_singular"
set +e
bash ops/aws_exact_lane.sh "$aws_root" "$aws_job/run" "$engine_tag" timeout "$engine_wall" Singular -q "$script"
engine_rc=$?
set -e
printf 'engine_rc=%s\n' "$engine_rc" > "$aws_job/engine.validation"; if [[ "$engine_rc" -ne 0 ]]; then exit "$engine_rc"; fi
stdout="$aws_job/run/${engine_tag}.stdout"; stderr="$aws_job/run/${engine_tag}.stderr"
set +e
python3 "$package/validate_export_v22.py" --compiler-result "$aws_job/compiled/result.json" --stdout "$stdout" --stderr "$stderr" --characteristic "$characteristic" --output "$aws_job/RESULT.json" > "$aws_job/validator.stdout" 2> "$aws_job/validator.stderr"
validator_rc=$?
set -e
printf 'validator_rc=%s\n' "$validator_rc" > "$aws_job/validator.validation"; if [[ "$validator_rc" -ne 0 ]]; then exit "$validator_rc"; fi
printf 'validator=PASS_TOTAL_REES_ALLROWS_G15_EXPORT_V22\n' >> "$aws_job/validator.validation"
find "$aws_job" -type f ! -name EVIDENCE.sha256 -print0 | sort -z | xargs -0 sha256sum > "$aws_job/EVIDENCE.sha256"

