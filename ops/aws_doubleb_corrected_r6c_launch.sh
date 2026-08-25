#!/bin/sh
# One-shot launcher for the corrected p-saturated double-B projection on r6c.
# The generator hash is checked by the caller before this script is launched.
set -eu

repo=/home/ubuntu/jc2doubleb/repo
out=/home/ubuntu/jc2doubleb/out
runner=$repo/ops/aws_doubleb_run.sh

launch() {
  tag=$1
  backend=$2
  characteristic=$3
  cap=$4
  nohup env JC2_DOUBLEB_OUT="$out" "$runner" \
    "$tag" "$backend" "$characteristic" "$cap" \
    >"$out/$tag.launcher.log" 2>&1 &
  echo "$tag pid=$!"
}

# Two independent characteristic-zero engines.  modStd supplies a modular
# reconstruction route; slimgb supplies a direct rational route.
launch q_exact_singular_satp_modstd_corrected_v2 singular-p-sat-modstd 0 172800
launch q_exact_singular_satp_slimgb_corrected_v2 singular-p-sat-slimgb 0 172800

# Cross-prime support/degree checks with the corrected (dp(8),dp(1)) order.
for prime in 32003 65521 100003 104729 105337 105673 200257 1000003 1048573 2147483629
do
  launch "mod_singular_satp_slimgb_corrected_p$prime" \
    singular-p-sat-slimgb "$prime" 43200
done
