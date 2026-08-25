#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 8 ]; then
  echo "usage: $0 VM_KIB REPO OUT_ROOT TAG MODE ENGINE ORDER TIMEOUT_SECONDS" >&2
  exit 64
fi

VM_KIB=$1
REPO=$2
OUT_ROOT=$3
TAG=$4
MODE=$5
ENGINE=$6
ORDER=$7
TIMEOUT_SECONDS=$8
CASE=cases/max12_912_order3_nu_q8_w0_rankdrop_loaded_rees_aws_20260825
OUT=$OUT_ROOT/$TAG
mkdir -p "$OUT"

ulimit -v "$VM_KIB"
cd "$REPO"
python3 "$CASE/generate.py" --mode "$MODE" --engine "$ENGINE" --order "$ORDER" > "$OUT/input.sing" 2> "$OUT/generator.stderr"
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
  echo "timeout_seconds=$TIMEOUT_SECONDS"
  echo "mode=$MODE"
  echo "engine=$ENGINE"
  echo "order=$ORDER"
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

if [ "$MODE" = loaded ]; then
  MARKER=Q8_W0_RANKDROP_LOADED_CLOSURE_PASS
elif [ "$MODE" = weighted_b1 ]; then
  MARKER=Q8_W0_RANKDROP_B1_SLOPE2_PASS
else
  MARKER=Q8_W0_RANKDROP_WEIGHTED_REES_PASS
fi
test "$(grep -c "$MARKER" "$OUT/stdout")" -eq 1
! grep -Eiq 'redefining|not defined|error occurred|segmentation fault|killed|timed out' "$OUT/stdout" "$OUT/stderr"
