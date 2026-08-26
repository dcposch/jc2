#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "AWS-only seeded projection V3 refused non-Linux host" >&2
  exit 125
fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then
  echo "AWS-only seeded projection V3 refused vendor=${vendor:-unknown}" >&2
  exit 125
fi
if [[ $# -ne 5 ]]; then
  echo "usage: run_seeded_projection_aws_v3_rawgb.sh AWS_ROOT AWS_RUN TAG INPUT CAP_KIB" >&2
  exit 125
fi

aws_root=$1
aws_run=$2
lane_tag=$3
input=$4
cap_kib=$5

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
gq_warning_count=$(grep -Fc '// ** GQ is no standard basis' "$stdout" || true)
{
  printf 'engine_rc=%s\n' "$engine_rc"
  printf 'required_q_mark=%s\n' 'SEEDED_Q_SCALAR_NORMALIZATION_SB_MARK=1'
  printf 'required_raw_gb=%s\n' 'QRED_RAW_GB_CERTIFICATE=PASS'
  printf 'required_preflight=%s\n' 'SEEDED_Q_PREFLIGHT=PASS'
  printf 'required_final=%s\n' 'SEEDED_PROJECTION_CERTIFICATE=PASS'
  printf 'gq_not_standard_basis_warning_count=%s\n' "$gq_warning_count"
} > "$validation"
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi
for required in \
  'SEEDED_Q_SCALAR_NORMALIZATION_SB_MARK=1' \
  'QRED_RAW_GB_CERTIFICATE=PASS' \
  'SEEDED_Q_PREFLIGHT=PASS' \
  'SEEDED_PROJECTION_CERTIFICATE=PASS'
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
if [[ "$gq_warning_count" -ne 0 ]]; then
  printf 'validator=FAIL_UNEXPECTED_GQ_SB_WARNING\n' >> "$validation"
  exit 91
fi
printf 'validator=PASS\n' >> "$validation"
