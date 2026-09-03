#!/usr/bin/env bash
set -euo pipefail

receipt="${1:-xmodel/k16-terminal-proof-sol56-20260903.run.v2}"
input_dir="$(awk -F= '$1=="lane_inputs_dir" {print $2}' "$receipt")"
count="$(awk -F= '$1=="charged_inputs" {print $2}' "$receipt")"
manifest="$(mktemp)"
trap 'rm -f "$manifest"' EXIT

awk -F= -v dir="$input_dir" -v count="$count" '
  /^charged_input_[0-9]+_sha256=/ {
    key=$1; sub(/^charged_input_/, "", key); sub(/_sha256$/, "", key)
    sha[key]=$2
  }
  /^charged_input_[0-9]+_basename=/ {
    key=$1; sub(/^charged_input_/, "", key); sub(/_basename$/, "", key)
    base[key]=$2
  }
  END {
    for (i=1; i<=count; i++) {
      if (!(i in sha) || !(i in base)) exit 2
      print sha[i] "  " dir "/" base[i]
    }
  }
' "$receipt" > "$manifest"

sha256sum -c "$manifest"
