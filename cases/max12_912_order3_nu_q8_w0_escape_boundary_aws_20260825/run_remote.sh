#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 4 ]]; then
  echo "usage: run_remote.sh REPO OUT TAG GENERATOR_ARGS..." >&2
  exit 64
fi

repo=$1
outroot=$2
tag=$3
shift 3
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_escape_boundary_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"

sha256sum "$case_dir/generate.py" "$case_dir/run_remote.sh" \
  "$case_dir/PREREGISTRATION.md" "$case_dir/PREREGISTRATION.manifest.sha256" \
  "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
  "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256" \
  > "$out/source.sha256"

python3 "$case_dir/generate.py" "$@" > "$out/input.sing"
sha256sum "$out/input.sing" >> "$out/source.sha256"

{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "args=$*"
  cat "$out/source.sha256"
} > "$out/run.meta"

set +e
/usr/bin/time -v timeout 14400 Singular -q "$out/input.sing" \
  > "$out/singular.stdout" 2> "$out/singular.stderr"
rc=$?
set -e

{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "rc=$rc"
  sha256sum "$out/singular.stdout" "$out/singular.stderr"
} >> "$out/run.meta"

if [[ $rc -ne 0 ]]; then exit "$rc"; fi
if rg -i 'not defined|error occurred|segmentation fault|killed|timed out' \
  "$out/singular.stdout" "$out/singular.stderr"; then exit 90; fi
pass_count=$(rg -c 'Q8_W0_(ESCAPE_FINITE|X5_GENERIC_TANGENT|ESCAPE_PROJECTIVE)_PASS' \
  "$out/singular.stdout" || true)
test "$pass_count" = 1
