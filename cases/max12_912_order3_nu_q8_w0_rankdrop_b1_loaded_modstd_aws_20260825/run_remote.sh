#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -ne 5 ]; then
  echo "usage: $0 VM_KIB REPO OUT_ROOT TAG TIMEOUT_SECONDS" >&2
  exit 64
fi
VM_KIB=$1
REPO=$2
OUT_ROOT=$3
TAG=$4
TIMEOUT_SECONDS=$5
CASE=cases/max12_912_order3_nu_q8_w0_rankdrop_b1_loaded_modstd_aws_20260825
OUT=$OUT_ROOT/$TAG
mkdir -p "$OUT"
ulimit -v "$VM_KIB"
cd "$REPO"
python3 "$CASE/generate.py" > "$OUT/input.sing" 2> "$OUT/generator.stderr"
test ! -s "$OUT/generator.stderr"
test -s "$OUT/input.sing"
set +e
/usr/bin/time -v timeout "$TIMEOUT_SECONDS" Singular -q "$OUT/input.sing" > "$OUT/stdout" 2> "$OUT/stderr"
RC=$?
set -e
printf '%s\n' "$RC" > "$OUT/runner.rc"
{
  echo "tag=$TAG"
  echo "host=$(hostname)"
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "virtual_memory_limit_kib=$VM_KIB"
  echo "engine=Singular-modStd"
  echo "algorithm=rational-multimodular-reconstruction-plus-exact-remainders-and-conditional-lift"
  echo "rc=$RC"
} > "$OUT/run.meta"
sha256sum \
  "$REPO/$CASE/PREREGISTRATION.md" \
  "$REPO/$CASE/generate.py" \
  "$REPO/$CASE/run_remote.sh" \
  "$REPO/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
  "$REPO/cases/max12_912_order3_fibre_20260824/order3_fibre.py" \
  "$OUT/input.sing" > "$OUT/source.sha256"
if [ "$RC" -ne 0 ]; then
  exit "$RC"
fi
test "$(grep -c Q8_W0_RANKDROP_B1_MODSTD_PASS "$OUT/stdout")" -eq 1
test "$(grep -c control_original_remainders_zero=1 "$OUT/stdout")" -eq 1
test "$(grep -c original_remainders_zero=1 "$OUT/stdout")" -eq 1
test "$(grep -c contraction_remainders_zero=1 "$OUT/stdout")" -eq 1
test "$(grep -c landing_remainders_zero=1 "$OUT/stdout")" -eq 1
if grep -q 'landing_empty=1' "$OUT/stdout"; then
  test "$(grep -c lift_residual_zero=1 "$OUT/stdout")" -eq 1
fi
! grep -Eiq 'redefining|not defined|error occurred|segmentation fault|killed|timed out|no standard basis|// \*\*' "$OUT/stdout" "$OUT/stderr"

