#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 8 ]]; then
  echo "usage: run_remote.sh VM_KIB REPO OUT TAG KIND STRATUM ENGINE ORDER" >&2
  exit 64
fi
vm_kib=$1
repo=$2
outroot=$3
tag=$4
kind=$5
stratum=$6
engine=$7
order=$8
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_horizontal_closure_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"
ulimit -v "$vm_kib"

sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/generate.py" "$case_dir/run_remote.sh" \
  "$case_dir/PREREGISTRATION.manifest.sha256" \
  "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
  "$repo/cases/max12_912_order3_fibre_20260824/order3_fibre.py" \
  > "$out/source.sha256"
python3 "$case_dir/generate.py" --kind "$kind" --stratum "$stratum" \
  --engine "$engine" --order "$order" > "$out/input.sing" 2> "$out/generator.stderr"
test ! -s "$out/generator.stderr"
sha256sum "$out/input.sing" >> "$out/source.sha256"
{
  echo "tag=$tag"; echo "host=$(hostname)";
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)";
  echo "virtual_memory_limit_kib=$vm_kib";
  echo "kind=$kind"; echo "stratum=$stratum"; echo "engine=$engine"; echo "order=$order";
  cat "$out/source.sha256";
} > "$out/run.meta"

set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=60 21600 Singular -q "$out/input.sing" \
  > "$out/result.out" 2> "$out/stderr.log"
rc=$?
set -e
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "rc=$rc";
  sha256sum "$out/result.out" "$out/stderr.log";
} >> "$out/run.meta"
echo "$rc" > "$out/runner.rc"
if [[ $rc -ne 0 ]]; then exit "$rc"; fi
if rg -i 'redefining|not defined|error occurred|segmentation fault|killed|timed out' \
  "$out/result.out" "$out/stderr.log"; then exit 90; fi
test "$(rg -c '^Q8_W0_HORIZONTAL_CLOSURE_PASS$' "$out/result.out" || true)" = 1
test "$(rg -c '^source_remainder_zero=1$' "$out/result.out" || true)" = 1
test "$(rg -c '^branch_remainder_zero=1$' "$out/result.out" || true)" = 1
