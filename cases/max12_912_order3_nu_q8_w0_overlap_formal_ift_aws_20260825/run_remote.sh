#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 6 ]]; then
  echo "usage: run_remote.sh VM_KIB REPO OUT TAG ENGINE ORDER" >&2
  exit 64
fi
vm_kib=$1; repo=$2; outroot=$3; tag=$4; engine=$5; order=$6
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_overlap_formal_ift_aws_20260825"
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
/usr/bin/time -v timeout 3600 Singular -q "$out/input.sing" > "$out/stdout" 2> "$out/stderr"
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
  a3_normal_rank3_everywhere=1 obstruction_vanishes_at_d0=1 \
  obstruction_Dd2_empty=1 obstruction_Dd4_empty=1 \
  triangular_block_identity=1 triangular_block_det=64/729 \
  exact_boundary_sheet=1 x5_support_membership=1 x3_support_membership=1 \
  x1_support_membership=1 lower_rows_x_linear_zero=1 \
  residual_linear_identity=1 residual_linear_det=-16/81 \
  Q8_W0_OVERLAP_FORMAL_IFT_PASS; do
  test "$(grep -c "^${marker}$" "$out/stdout" || true)" = 1
done
