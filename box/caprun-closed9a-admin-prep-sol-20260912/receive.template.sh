#!/bin/bash
# DISABLED/UNBOUND; fixed preholder-installed receiver. Never run bash -s.
# This administrative primitive is NOT a complete staging qualification.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then exit 2; fi
test "$#" = 1
test "$(id -u)" = 0
jc2_stage='JC2_REMOTE_STAGE_PLACEHOLDER'
jc2_stop='JC2_ORIGINAL_ADMISSION_STOP_EPOCH_PLACEHOLDER'
[[ "$jc2_stop" =~ ^[1-9][0-9]{0,10}$ ]]
test "$(date -u +%s)" -lt "$jc2_stop"
test "$(readlink -e "$jc2_stage")" = "$jc2_stage"
test "$(stat -c '%u:%g:%a' "$jc2_stage")" = 0:0:700
case "$1" in
 --preflight)
  for jc2_name in ROOT-REGISTRATION.json ROOT-EXECUTION-CARD.md FINAL-INSTALL-INPUTS.sha256 final-install.sh native.sha256; do
   test ! -e "$jc2_stage/$jc2_name"
   test ! -L "$jc2_stage/$jc2_name"
  done
  exit 0 ;;
 ROOT-REGISTRATION.json|ROOT-EXECUTION-CARD.md|FINAL-INSTALL-INPUTS.sha256|final-install.sh|native.sha256) ;;
 *) exit 2 ;;
esac
jc2_target="$jc2_stage/$1"
test ! -e "$jc2_target"
test ! -L "$jc2_target"
umask 077
# excl is a CONVERSION, not an oflag. The actual creation is exclusive even
# if a competing writer appears after the two documentary absence checks.
# A partial/new file is retained on failure; never overwrite or retry it.
# Outer pinned command must bound both SSH and this exact remote writer.
exec /usr/bin/dd of="$jc2_target" conv=excl,fsync oflag=nofollow status=none
