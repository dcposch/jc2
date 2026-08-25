#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 5 ]]; then
  echo "usage: run_clean_remote.sh VM_KIB REPO OUT TAG GENERATOR_ARGS..." >&2
  exit 64
fi
vm_kib=$1
repo=$2
outroot=$3
tag=$4
shift 4
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_escape_boundary_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"
ulimit -v "$vm_kib"

sha256sum "$case_dir/generate.py" "$case_dir/generate_clean.py" \
  "$case_dir/run_clean_remote.sh" "$case_dir/PREREGISTRATION.manifest.sha256" \
  "$case_dir/LAUNCH.manifest.sha256" \
  "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
  > "$out/source.sha256"
python3 "$case_dir/generate_clean.py" "$@" > "$out/input.sing"
sha256sum "$out/input.sing" >> "$out/source.sha256"
{
  echo "tag=$tag"; echo "host=$(hostname)";
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)";
  echo "virtual_memory_limit_kib=$vm_kib"; echo "args=$*";
  cat "$out/source.sha256";
} > "$out/run.meta"

set +e
/usr/bin/time -v timeout 14400 Singular -q "$out/input.sing" \
  > "$out/singular.stdout" 2> "$out/singular.stderr"
rc=$?
set -e
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "rc=$rc";
  sha256sum "$out/singular.stdout" "$out/singular.stderr";
} >> "$out/run.meta"
if [[ $rc -ne 0 ]]; then exit "$rc"; fi
if rg -i 'redefining|not defined|error occurred|segmentation fault|killed|timed out' \
  "$out/singular.stdout" "$out/singular.stderr"; then exit 90; fi
test "$(rg -c 'Q8_W0_(ESCAPE_FINITE|X5_GENERIC_TANGENT)_PASS' "$out/singular.stdout" || true)" = 1
