#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only one-parameter Rees runner refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only one-parameter Rees runner refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 6 ]]; then
  echo "usage: run_oneparam_aws.sh AWS_ROOT AWS_RUN TAG INPUT CAP_KIB TIMEOUT_SECONDS" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
input=$4
cap_kib=$5
timeout_seconds=$6

mkdir -p "$aws_run"
sha256sum "$input" > "$aws_run/SINGULAR_INPUT.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" \
  "$aws_root" "$aws_run" "$lane_tag" \
  timeout "$timeout_seconds" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_run/$lane_tag.stdout"
validation="$aws_run/$lane_tag.validation"
{
  printf 'engine_rc=%s\n' "$engine_rc"
  printf 'required_source=%s\n' 'ONEPARAM_SOURCE_HASHES=PASS'
  printf 'required_linearity=%s\n' 'ONEPARAM_LOAD_LINEARITY=PASS'
} > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi
for required in \
  'ONEPARAM_SOURCE_HASHES=PASS' \
  'ONEPARAM_LOAD_LINEARITY=PASS' \
  'ONEPARAM_STAGE_LAMBDA_DONE' \
  'ONEPARAM_STAGE_J_DONE' \
  'ONEPARAM_STAGE_IRRELEVANT_DONE' \
  'ONEPARAM_REES_ENDPOINT=PASS'
do
  if [[ "$(grep -Fxc "$required" "$stdout" || true)" -ne 1 ]]; then
    printf 'validator=FAIL_MISSING_OR_NONUNIQUE:%s\n' "$required" >> "$validation"
    exit 90
  fi
done
if grep -Fq '=FAIL' "$stdout" || grep -Eq '^\? ' "$stdout"; then
  printf 'validator=FAIL_SENTINEL_OR_DIAGNOSTIC\n' >> "$validation"
  exit 90
fi
printf 'validator=PASS\n' >> "$validation"
