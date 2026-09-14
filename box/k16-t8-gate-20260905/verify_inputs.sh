#!/bin/bash
set -euo pipefail
awk -F= '
/^charged_input_[0-9]+_sha256=/ {
  k=$1; sub(/_sha256$/, "", k); hash[k]=$2
}
/^charged_input_[0-9]+_basename=/ {
  k=$1; sub(/_basename$/, "", k); base[k]=$2
}
END {
  for (k in hash)
    print hash[k] "  /tmp/jc2-lane.yGKJor/inputs/" base[k]
}' xmodel/k16-t8-gate-astra-20260905.run.v2 > /tmp/k16-t8-gate-astra-20260905.sha256
sha256sum -c /tmp/k16-t8-gate-astra-20260905.sha256
