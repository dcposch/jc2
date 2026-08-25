#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 5 ]]; then
  echo "usage: run_v2_remote.sh VM_KIB REPO OUT TAG MODE [GENERATOR_ARGS...]" >&2
  exit 64
fi
vm_kib=$1; repo=$2; outroot=$3; tag=$4; mode=$5; shift 5
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_localized_fibre_classification_repaired_v2_aws_20260825"
parent="$repo/cases/max12_912_order3_nu_q8_w0_fibre_stratification_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"
ulimit -v "$vm_kib"

sha256sum "$case_dir/PREREGISTRATION.md" "$case_dir/find_irreducible_prime.py" \
  "$case_dir/run_v2_remote.sh" "$case_dir/PREREGISTRATION.manifest.sha256" \
  "$parent/generate.py" \
  "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
  "$repo/cases/max12_912_order3_fibre_20260824/order3_fibre.py" \
  "$repo/cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.py" \
  > "$out/source.sha256"
{
  echo "tag=$tag"; echo "host=$(hostname)"; echo "mode=$mode";
  echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)";
  echo "virtual_memory_limit_kib=$vm_kib"; cat "$out/source.sha256";
} > "$out/run.meta"

set +e
if [[ "$mode" == "scan" ]]; then
  /usr/bin/time -v timeout 600 python3 "$case_dir/find_irreducible_prime.py" \
    > "$out/stdout" 2> "$out/stderr"
else
  python3 "$parent/generate.py" "$@" > "$out/input.sing"
  sha256sum "$out/input.sing" >> "$out/run.meta"
  /usr/bin/time -v timeout 7200 Singular -q "$out/input.sing" \
    > "$out/stdout" 2> "$out/stderr"
fi
rc=$?
set -e
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "rc=$rc";
  sha256sum "$out/stdout" "$out/stderr";
} >> "$out/run.meta"
if [[ $rc -ne 0 ]]; then exit "$rc"; fi
if rg -i 'not defined|error occurred|segmentation fault|killed|timed out' "$out/stdout" "$out/stderr"; then exit 90; fi
if [[ "$mode" == "scan" ]]; then
  test "$(rg -c Q8_IRREDUCIBLE_PRIME_SEARCH_PASS "$out/stdout" || true)" = 1
else
  test "$(rg -c Q8_W0_FIBRE_STRATUM_PASS "$out/stdout" || true)" = 1
  rg -q '^original_remainder_zero=1$' "$out/stdout"
fi
