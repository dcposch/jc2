#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then exit 125; fi
vendor=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$vendor" != "Amazon EC2" ]]; then exit 125; fi
if [[ $# -ne 6 ]]; then exit 125; fi
aws_root=$1
aws_run=$2
tag=$3
input=$4
cap_kib=$5
timeout_seconds=$6
mkdir -p "$aws_run"
sha256sum "$input" > "$aws_run/SINGULAR_INPUT.sha256"
Singular --version </dev/null > "$aws_run/SINGULAR.version"
ulimit -v "$cap_kib"
set +e
"$aws_root/ops/aws_exact_lane.sh" "$aws_root" "$aws_run" "$tag" \
  timeout "$timeout_seconds" Singular -q "$input"
engine_rc=$?
set -e
stdout="$aws_run/$tag.stdout"
validation="$aws_run/$tag.validation"
printf 'engine_rc=%s\n' "$engine_rc" > "$validation"
if [[ "$engine_rc" -eq 124 ]]; then
  printf 'validator=TIMEOUT_NO_VERDICT\n' >> "$validation"
  exit 124
fi
if [[ "$engine_rc" -ne 0 ]]; then
  printf 'validator=FAIL_ENGINE\n' >> "$validation"
  exit "$engine_rc"
fi
for required in \
  'FIRST_NORMAL_SOURCE_HASHES=PASS' \
  'FIRST_NORMAL_LOAD_LINEARITY=PASS' \
  'FIRST_NORMAL_LAMBDA2_DIVISIBLE=1' \
  'FIRST_NORMAL_DIVISION_IDENTITY=1' \
  'FIRST_NORMAL_FORBIDDEN_INDEPENDENCE=1' \
  'FIRST_NORMAL_Q_STD_DONE' \
  'FIRST_NORMAL_K_SAT_DONE' \
  'FIRST_NORMAL_NORMAL_SAT_DONE' \
  'FIRST_NORMAL_ENDPOINT=PASS_NAVIGATION'
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
printf 'validator=PASS_NAVIGATION_ONLY\n' >> "$validation"
