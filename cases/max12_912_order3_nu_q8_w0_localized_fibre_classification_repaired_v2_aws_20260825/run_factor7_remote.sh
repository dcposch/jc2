#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: run_factor7_remote.sh VM_KIB REPO OUT TAG" >&2
  exit 64
fi
vm_kib=$1; repo=$2; outroot=$3; tag=$4
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_localized_fibre_classification_repaired_v2_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"
ulimit -v "$vm_kib"

sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/find_irreducible_prime.py" \
  "$case_dir/generate_factor7.py" "$case_dir/run_factor7_remote.sh" \
  "$case_dir/PREREGISTRATION.manifest.sha256" > "$out/source.sha256"
python3 "$case_dir/generate_factor7.py" > "$out/input.sing" 2> "$out/generator.stderr"
test ! -s "$out/generator.stderr"
sha256sum "$out/input.sing" >> "$out/source.sha256"
{
  echo "tag=$tag"; echo "host=$(hostname)";
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)";
  echo "virtual_memory_limit_kib=$vm_kib";
  cat "$out/source.sha256";
} > "$out/run.meta"
set +e
/usr/bin/time -v timeout 600 Singular -q "$out/input.sing" > "$out/stdout" 2> "$out/stderr"
rc=$?
set -e
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "rc=$rc";
  sha256sum "$out/stdout" "$out/stderr";
} >> "$out/run.meta"
echo "$rc" > "$out/runner.rc"
if [[ $rc -ne 0 ]]; then exit "$rc"; fi
if rg -i 'redefining|not defined|error occurred|segmentation fault|killed|timed out' \
  "$out/stdout" "$out/stderr"; then exit 90; fi
for expected in \
  factor_count=1 degree_sum=8 degree8_count=1 multiplicity_one=1 \
  mutual_divisibility=1 Q8_MOD7_SINGULAR_IRREDUCIBLE_PASS; do
  test "$(rg -c "^${expected}$" "$out/stdout" || true)" = 1
done
