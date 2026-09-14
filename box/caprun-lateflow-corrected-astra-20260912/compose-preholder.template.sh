#!/bin/bash
# DISABLED/UNBOUND preholder-only composer. It never admits a holder.
set -euo pipefail
grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0" && exit 2
test "$#" = 1
test "$1" = ROOT_COMPOSE_REVIEWED_DISABLED_ENTRIES_ONLY
jc2_box=/home/ubuntu/jc2/box/caprun-lateflow-corrected-astra-20260912
jc2_kernel=/home/ubuntu/jc2/box/caprun-lateflow-repair-root-20260912/ORCHESTRATION-KERNEL.js
test "$(sha256sum "$jc2_kernel" | cut -d' ' -f1)" = 2ceb9bcbc4ccd89079d691a3ec4c50d97898129bd3ecdee01bdc6646d1180e44
test "$(sha256sum "$jc2_box/FLOW.tail.template.js" | cut -d' ' -f1)" = 'JC2_REVIEWED_TAIL_SHA256_PLACEHOLDER'
test "$(readlink -e "$jc2_box")" = "$jc2_box"
test "$(stat -c %a "$jc2_box")" = 700
# ROOT owns this private parent exclusively; noclobber adds file-create protection.
for jc2_entry in ADMIT ATTEST INSTALL RELEASE; do
 test ! -e "$jc2_box/$jc2_entry.functions.exec.js"; test ! -L "$jc2_box/$jc2_entry.functions.exec.js"
done
for jc2_entry in ADMIT ATTEST INSTALL RELEASE; do
 jc2_target="$jc2_box/$jc2_entry.functions.exec.js"
 test ! -e "$jc2_target"; test ! -L "$jc2_target"
 ( umask 077; set -o noclobber; sed "s/@@ENTRY@@/$jc2_entry/" "$jc2_kernel" "$jc2_box/FLOW.tail.template.js" >"$jc2_target" )
 test "$(grep -c 'const JC2_ENTRY = ' "$jc2_target")" = 1
 test -z "$(grep '@@ENTRY@@' "$jc2_target" || true)"
 chmod 0444 "$jc2_target"
done
sha256sum "$jc2_box"/*.functions.exec.js
# Result remains disabled because FROZEN-CONFIG.json is absent until separate
# ROOT binding/review. Composition itself creates no authority or runtime data.
