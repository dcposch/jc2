#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only seeded projection V2 refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only seeded projection V2 refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: run_seeded_projection_aws_v2.sh AWS_ROOT AWS_RUN TAG MODE INPUT CAP_KIB" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
mode=$4
input=$5
cap_kib=$6
case "$mode" in
  seeded-a6) final_pass='SEEDED_A6_CERTIFICATE=PASS' ;;
  seeded-prime) final_pass='SEEDED_PROJECTION_CERTIFICATE=PASS' ;;
  *) echo "invalid mode: $mode" >&2; exit 125 ;;
esac

mkdir -p "$aws_run"
sha256sum "$input" > "$aws_run/SINGULAR_INPUT.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" timeout 3600 Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_run/$lane_tag.stdout"
validation="$aws_run/$lane_tag.validation"
{
  printf 'engine_rc=%s\n' "$engine_rc"
  printf 'required_preflight=%s\n' 'SEEDED_Q_PREFLIGHT=PASS'
  printf 'required_final=%s\n' "$final_pass"
} > "$validation"
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi
if [[ "$(grep -Fxc 'SEEDED_Q_PREFLIGHT=PASS' "$stdout" || true)" -ne 1 ]] ||
   [[ "$(grep -Fxc "$final_pass" "$stdout" || true)" -ne 1 ]] ||
   grep -Fq '=FAIL' "$stdout" || grep -Eq '^\? ' "$stdout"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"
  exit 90
fi
printf 'validator=PASS\n' >> "$validation"
