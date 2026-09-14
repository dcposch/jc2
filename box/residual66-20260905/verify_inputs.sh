#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/../.." && pwd)"
out_dir="$repo_root/box/residual66-20260905"
receipt="$repo_root/xmodel/residual66-roster-sol56-20260905.run.v2"
audit_tmp="$(mktemp -d)"
trap 'rm -rf -- "$audit_tmp"' EXIT

input_dir="$(awk -F= '$1 == "lane_inputs_dir" { print $2 }' "$receipt")"
expected="$(awk -F= '$1 == "charged_inputs" { print $2 }' "$receipt")"
test -n "$input_dir"
test "$expected" -gt 0

awk -F= -v dir="$input_dir/" -v expected="$expected" '
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
    for (i=1; i<=expected; i++) {
      if (!(i in basename) || !(i in digest)) exit 2
      print digest[i] "  " dir basename[i]
    }
  }
' "$receipt" > "$audit_tmp/inputs.sha256"

test "$(wc -l < "$audit_tmp/inputs.sha256")" -eq "$expected"
sha256sum -c "$audit_tmp/inputs.sha256" | tee "$audit_tmp/inputs.check.log"
mv "$audit_tmp/inputs.sha256" "$out_dir/inputs.sha256"
mv "$audit_tmp/inputs.check.log" "$out_dir/inputs.check.log"

