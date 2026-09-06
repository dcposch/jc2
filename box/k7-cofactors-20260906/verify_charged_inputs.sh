#!/usr/bin/env bash
set -euo pipefail

receipt=${1:-/home/ubuntu/jc2/xmodel/k7-cofactors-sol56-20260906.run.v2}
out=${2:-/home/ubuntu/jc2/box/k7-cofactors-20260906}
manifest="$out/charged-inputs.sha256"
check="$out/charged-inputs.check.log"

awk -F= '
  $1=="lane_inputs_dir" { dir=$2 }
  $1 ~ /^charged_input_[0-9]+_basename$/ {
    split($1,k,"_"); base[k[3]]=$2; if (k[3]>n) n=k[3]
  }
  $1 ~ /^charged_input_[0-9]+_sha256$/ {
    split($1,k,"_"); sha[k[3]]=$2; if (k[3]>n) n=k[3]
  }
  END {
    if (dir=="") { print "missing lane_inputs_dir" > "/dev/stderr"; exit 2 }
    for (i=1; i<=n; i++) {
      if (base[i]=="" || sha[i]=="") {
        print "missing receipt fields for charged input " i > "/dev/stderr"; exit 2
      }
      printf "%s  %s/%s\n", sha[i], dir, base[i]
    }
  }
' "$receipt" >"$manifest"
sha256sum -c "$manifest" | tee "$check"
