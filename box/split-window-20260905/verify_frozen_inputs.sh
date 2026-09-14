#!/usr/bin/env bash
set -euo pipefail

repo=/home/ubuntu/jc2
receipt="$repo/xmodel/split-window-alldeg-sol56-20260905.run.v2"
input_dir=/tmp/jc2-lane.D5nDdq/inputs
out_dir="$repo/box/split-window-20260905"
manifest="$out_dir/frozen-inputs.sha256"
check_log="$out_dir/frozen-inputs.check.log"

awk -F= '
  /^charged_input_[0-9]+_sha256=/ {
    i=$1; sub(/^charged_input_/, "", i); sub(/_sha256$/, "", i); sha[i]=$2
  }
  /^charged_input_[0-9]+_basename=/ {
    i=$1; sub(/^charged_input_/, "", i); sub(/_basename$/, "", i); base[i]=$2
  }
  END {
    for (i in sha) {
      if (!(i in base)) exit 2
      print sha[i] "  " dir "/" base[i]
    }
  }
' dir="$input_dir" "$receipt" | sort -k2 > "$manifest"

sha256sum -c "$manifest" | tee "$check_log"

