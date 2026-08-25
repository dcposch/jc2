#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 6 ]]; then
  echo "usage: run_v3_remote.sh VM_KIB REPO OUT TAG ENGINE ORDER" >&2
  exit 64
fi
vm_kib=$1; repo=$2; outroot=$3; tag=$4; engine=$5; order=$6
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"
ulimit -v "$vm_kib"
sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/generate.py" \
  "$case_dir/generate_v2.py" "$case_dir/generate_v3.py" \
  "$case_dir/run_v3_remote.sh" "$case_dir/V3.manifest.sha256" \
  "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
  "$repo/cases/max12_912_order3_fibre_20260824/order3_fibre.py" > "$out/source.sha256"
python3 "$case_dir/generate_v3.py" --engine "$engine" --order "$order" \
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
if [[ $rc -ne 0 ]]; then exit "$rc"; fi
if grep -Eiq 'redefining|not defined|error occurred|segmentation fault|killed|timed out' \
  "$out/stdout" "$out/stderr"; then exit 90; fi
for expected in cylinder_dim=2 source_rows_zero=1 Fw_zero=1 \
  all_6x6_minors_zero=1 rank5_minor_identity=1 a_kernel_zero=1 \
  Q8_W0_X5_CYLINDER_LOCAL_GERM_PASS; do
  test "$(grep -c "^${expected}$" "$out/stdout" || true)" = 1
done
