#!/usr/bin/env bash
set -euo pipefail

here=$(cd -- "$(dirname -- "$0")" && pwd)
workspace=$(cd -- "$here/../.." && pwd)
receipt="$workspace/xmodel/k16-brcr-closedform-sol56-20260903.run.v2"
input_dir=/tmp/jc2-lane.5ksWeb/inputs
manifest="$here/charged_inputs.from_receipt.sha256"
check_log="$here/charged_inputs.check.log"

awk -F= -v input_dir="$input_dir" '
  /^charged_input_[0-9]+_sha256=/ {
    i=$1; sub(/^charged_input_/,"",i); sub(/_sha256$/,"",i); i+=0; hash[i]=$2; if (i>n) n=i
  }
  /^charged_input_[0-9]+_basename=/ {
    i=$1; sub(/^charged_input_/,"",i); sub(/_basename$/,"",i); i+=0; base[i]=$2; if (i>n) n=i
  }
  END {
    for (i=1; i<=n; i++) {
      if (!(i in hash) || !(i in base)) exit 2
      print hash[i] "  " input_dir "/" base[i]
    }
  }
' "$receipt" > "$manifest"

sha256sum -c "$manifest" | tee "$check_log"
