#!/usr/bin/env bash
# V1_8: extract source-complete native rows, then native msolve, then graph.
set -u
ROOT=${ROOT:-$HOME/moh-bigmem-20260905}
TDIR="$ROOT/targets/v18"
. "$TDIR/env.sh"
echo "V18_EXTRACT_START utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
bash "$ROOT/extract_native.sh" "$TDIR/classdir" "$TDIR/classdir/builders/C_n18m12_M2_9_ell2_s3_V1_8_builder.sing" 3600
erc=$?
echo "V18_EXTRACT_RC=$erc"
EXTRACTED="$TDIR/classdir/rows/C_n18m12_M2_9_ell2_s3_V1_8_rows.tsv"
if [[ -s "$EXTRACTED" ]] && grep -q NATIVE_DONE "$TDIR/classdir/extract/builder.stdout" 2>/dev/null; then
  echo "V18_NATIVE_ROWS_OK sha=$(sha256sum "$EXTRACTED")"
  export NATIVE_ROWS="$EXTRACTED"
  export NATIVE_META="$TDIR/native_meta.json"
else
  echo "V18_NATIVE_EXTRACT_FAILED; msolve will use graph presentation only"
  export NATIVE_ROWS=""
fi
bash "$ROOT/run_msolve_pipeline.sh" v18
