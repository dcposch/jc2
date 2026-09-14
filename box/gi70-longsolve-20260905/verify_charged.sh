#!/usr/bin/env bash
set -euo pipefail
ROOT=/home/ubuntu/jc2
RECEIPT=$ROOT/xmodel/gi70-longsolve-sol56-20260905.run.v2
OUT=$ROOT/box/gi70-longsolve-20260905/custody
awk -F= '
  /^lane_inputs_dir=/ { dir=$2 }
  /^charged_input_[0-9]+_basename=/ { split($1,a,"_"); base[a[3]]=$2 }
  /^charged_input_[0-9]+_sha256=/ { split($1,a,"_"); hash[a[3]]=$2 }
  END {
    for (i=1; i<=6; i++) {
      if (!(i in base) || !(i in hash) || dir=="") exit 2
      print hash[i] "  " dir "/" base[i]
    }
  }
' "$RECEIPT" > "$OUT/charged-from-receipt.sha256"
sha256sum -c "$OUT/charged-from-receipt.sha256" | tee "$OUT/charged-check.log"
