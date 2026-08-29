#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only quadratic runner refused host" >&2
  exit 125
fi
if [[ $# -ne 5 ]]; then
  echo "usage: run_quadratic_aws.sh AWS_ROOT AWS_RUN TAG CAP_KIB TIMEOUT_SECONDS" >&2
  exit 125
fi
aws_root=$1
aws_run=$2
lane_tag=$3
cap_kib=$4
timeout_seconds=$5
rel=cases/max12_812_order2_u2_62_k00_normal_quadratic_v6_20260827
mkdir -p "$aws_run"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" timeout "$timeout_seconds" \
  env JC2_REGISTERED_AWS_LANE="$lane_tag" python3 "$aws_root/$rel/replay_k00_quadratic.py" "$aws_run/output"
engine_rc=$?
set -e
stdout="$aws_run/$lane_tag.stdout"
validation="$aws_run/$lane_tag.validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi
python3 "$aws_root/$rel/validate_quadratic.py" \
  "$stdout" "$aws_run/output/RESULT.json" "$aws_run/output/quadratic_rows.json" \
  > "$aws_run/validator.stdout" 2> "$aws_run/validator.stderr"
printf 'validator=PASS_REPLAY_ONLY\n' >> "$validation"
sha256sum "$aws_run/output/RESULT.json" "$aws_run/output/quadratic_rows.json" \
  > "$aws_run/ENDPOINT_EVIDENCE.sha256"
