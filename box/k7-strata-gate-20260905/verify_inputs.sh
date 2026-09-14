#!/usr/bin/env bash
set -euo pipefail

root=/home/ubuntu/jc2
receipt="$root/xmodel/k7-strata-gate-sol56-20260905.run.v2"
inputs=/tmp/jc2-lane.qb6I1q/inputs
out="$root/box/k7-strata-gate-20260905"

mkdir -p "$out"
awk -F= -v inputs="$inputs" '
  /^charged_input_[0-9]+_basename=/ {
    key=$1
    sub(/^charged_input_/, "", key)
    sub(/_basename$/, "", key)
    basename[key]=$2
  }
  /^charged_input_[0-9]+_sha256=/ {
    key=$1
    sub(/^charged_input_/, "", key)
    sub(/_sha256$/, "", key)
    digest[key]=$2
  }
  END {
    for (i=1; i<=7; i++) {
      if (!(i in basename) || !(i in digest)) exit 2
      print digest[i] "  " inputs "/" basename[i]
    }
  }
' "$receipt" > "$out/frozen-inputs.sha256"

sha256sum -c "$out/frozen-inputs.sha256" > "$out/frozen-inputs.check.log"
cat "$out/frozen-inputs.check.log"
