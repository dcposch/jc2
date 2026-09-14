#!/usr/bin/env bash
# Rebuild both manifests from their receipts; no digest is transcribed here.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

mkdir -p certificates
awk -F= '
/^charged_input_[0-9]+_basename=/ {
  key=$1; sub(/^charged_input_/, "", key); sub(/_basename$/, "", key); base[key]=$2
}
/^charged_input_[0-9]+_sha256=/ {
  key=$1; sub(/^charged_input_/, "", key); sub(/_sha256$/, "", key); hash[key]=$2
}
END {
  for (i=1; i<=8; i++) printf "%s  frozen/%s\n", hash[i], base[i]
}' receipt.run.v2 > certificates/frozen-inputs.sha256
sha256sum -c certificates/frozen-inputs.sha256 \
  > certificates/frozen-inputs.check.log

awk -F= '
/^charged_input_[0-9]+_basename=/ {
  key=$1; sub(/^charged_input_/, "", key); sub(/_basename$/, "", key); base[key]=$2
}
/^charged_input_[0-9]+_sha256=/ {
  key=$1; sub(/^charged_input_/, "", key); sub(/_sha256$/, "", key); hash[key]=$2
}
END {
  for (i=1; i<=20; i++) printf "%s  legacy/inputs/%s\n", hash[i], base[i]
}' legacy/receipt.run.v2 > certificates/legacy-inputs.sha256
sha256sum -c certificates/legacy-inputs.sha256 \
  > certificates/legacy-inputs.check.log

test "$(sha256sum original_band_engine.py | awk '{print $1}')" = \
  "$(awk -F= '$1=="charged_input_5_sha256" {print $2}' receipt.run.v2)"
printf 'CURRENT_8_OF_8_OK\nLEGACY_20_OF_20_OK\nORIGINAL_ENGINE_PIN_OK\n'
