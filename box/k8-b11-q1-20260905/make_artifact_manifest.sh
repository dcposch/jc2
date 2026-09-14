#!/usr/bin/env bash
# Hash the completed lane tree without creating a self-referential manifest.
set -euo pipefail

ROOT=$(cd "$(dirname "$0")" && pwd)
OUT="$ROOT/custody/artifacts.sha256"
CHECK="$ROOT/custody/artifacts.sha256.check.log"
TMP=$(mktemp /tmp/k8-b11-q1-artifacts.XXXXXX)
trap 'rm -f "$TMP"' EXIT

cd "$ROOT"
find . -type f \
  ! -path './custody/artifacts.sha256' \
  ! -path './custody/artifacts.sha256.check.log' \
  ! -path '*/__pycache__/*' \
  -print0 \
  | sort -z \
  | xargs -0 sha256sum > "$TMP"
mv "$TMP" "$OUT"
trap - EXIT
sha256sum -c "$OUT" > "$CHECK"
printf 'manifest=%s\n' "$OUT"
printf 'entries=%s\n' "$(wc -l < "$OUT")"
sha256sum "$OUT" "$CHECK"
