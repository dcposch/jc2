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
CASE=cases/max12_912_order3_nu_q8_w0_rankdrop_b1_finite_c_modstd_aws_20260825
OUT=$OUT_ROOT/$TAG
mkdir -p "$OUT"
ulimit -v "$VM_KIB"
cd "$REPO"
sha256sum -c "$CASE/PREREGISTRATION.manifest.sha256"
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
  echo "engine=Singular-modStd-Q-polynomial-c"
  echo "scope=frozen-d4-finite-c-pointed-selected-landing"
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
test "$(grep -c '^modstd_control_zero=1$' "$OUT/stdout")" -ge 1
test "$(grep -c '^original_remainders_zero=1$' "$OUT/stdout")" -eq 1
test "$(grep -c '^contraction_remainders_zero=1$' "$OUT/stdout")" -eq 1
test "$(grep -c '^landing_remainders_zero=1$' "$OUT/stdout")" -eq 1
test "$(grep -c Q8_W0_RANKDROP_B1_FINITE_C_MODSTD_PASS "$OUT/stdout")" -eq 1
! grep -Eiq 'redefining|not defined|undefined|error occurred|segmentation fault|killed|timed out|no standard basis|mismatch of number of vars|cannot make ring|expected .*expression|wrong type declaration|// \*\*' "$OUT/stdout" "$OUT/stderr"
