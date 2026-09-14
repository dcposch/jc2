#!/usr/bin/env bash
# Mechanically reconstruct the mandated direct /tmp manifest from this receipt.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

INPUT_DIR=$(awk -F= '$1=="lane_inputs_dir" {print $2}' receipt.run.v2)
INPUT_COUNT=$(awk -F= '$1=="charged_inputs" {print $2}' receipt.run.v2)
test -n "$INPUT_DIR" -a "$INPUT_COUNT" -eq 8
awk -F= -v dir="$INPUT_DIR" -v count="$INPUT_COUNT" '
/^charged_input_[0-9]+_basename=/ {
  key=$1; sub(/^charged_input_/, "", key); sub(/_basename$/, "", key); base[key]=$2
}
/^charged_input_[0-9]+_sha256=/ {
  key=$1; sub(/^charged_input_/, "", key); sub(/_sha256$/, "", key); hash[key]=$2
}
END {
  for (i=1; i<=count; i++) {
    if (!(i in base) || !(i in hash)) exit 2
    printf "%s  %s/%s\n", hash[i], dir, base[i]
  }
}' receipt.run.v2 > certificates/charged-inputs.from-receipt.sha256
sha256sum -c certificates/charged-inputs.from-receipt.sha256 \
  > certificates/charged-inputs.from-receipt.check.log
printf 'DIRECT_CHARGED_8_OF_8_OK\n'
