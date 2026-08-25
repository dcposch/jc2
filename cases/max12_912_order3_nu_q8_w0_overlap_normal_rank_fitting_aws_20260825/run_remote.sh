#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 6 ]]; then
  echo "usage: run_remote.sh VM_KIB REPO OUT TAG ENGINE ORDER" >&2
  exit 64
fi
vm_kib=$1; repo=$2; outroot=$3; tag=$4; engine=$5; order=$6
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_overlap_normal_rank_fitting_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"
ulimit -v "$vm_kib"
sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/generate.py" \
  "$case_dir/run_remote.sh" "$case_dir/PREREGISTRATION.manifest.sha256" \
  "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
  "$repo/cases/max12_912_order3_fibre_20260824/order3_fibre.py" > "$out/source.sha256"
python3 "$case_dir/generate.py" --engine "$engine" --order "$order" \
  > "$out/input.sing" 2> "$out/generator.stderr"
test ! -s "$out/generator.stderr"
sha256sum "$out/input.sing" >> "$out/source.sha256"
{
  echo "tag=$tag"; echo "host=$(hostname)"; echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)";
  echo "virtual_memory_limit_kib=$vm_kib"; echo "engine=$engine"; echo "order=$order";
  cat "$out/source.sha256";
} > "$out/run.meta"
set +e
/usr/bin/time -v timeout 7200 Singular -q "$out/input.sing" > "$out/stdout" 2> "$out/stderr"
rc=$?
set -e
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "rc=$rc";
  sha256sum "$out/stdout" "$out/stderr";
} >> "$out/run.meta"
echo "$rc" > "$out/runner.rc"
test "$rc" = 0
if grep -Eiq 'redefining|not defined|error occurred|segmentation fault|killed|timed out|no standard basis|// \*\*' \
  "$out/stdout" "$out/stderr"; then exit 90; fi
for marker in a3_source_rows_zero=1 a3_tangent_columns_zero=1 \
  Q8_W0_OVERLAP_NORMAL_RANK_FITTING_PASS; do
  test "$(grep -c "^${marker}$" "$out/stdout" || true)" = 1
done
test "$(grep -c '^K[0-3]_BASIS_BEGIN$' "$out/stdout" || true)" = 4
test "$(grep -c '^K[0-3]_BASIS_END$' "$out/stdout" || true)" = 4
