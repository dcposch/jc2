#!/bin/bash
# SEPARATE DISABLED/UNBOUND ROOT release. Never called by RECIPE.js.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then exit 2; fi
test 'JC2_ROOT_SEPARATE_RELEASE_DECISION_PLACEHOLDER' = ROOT_SEPARATELY_AUTHORIZED_ONE_FIFO_FRAME
test "$(id -u)" = 0
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_HOLDER_CUTOFF_PLACEHOLDER' +%s)"
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_ADMISSION_STOP_PLACEHOLDER' +%s)"
jc2_unit='JC2_UNIT_PLACEHOLDER'
jc2_holder=JC2_HOLDER_PID_PLACEHOLDER
jc2_start=JC2_HOLDER_START_TICKS_PLACEHOLDER
jc2_invocation='JC2_INVOCATION_ID_PLACEHOLDER'
jc2_fifo='JC2_FIFO_PLACEHOLDER'
jc2_final='JC2_FINAL_REGISTRATION_PLACEHOLDER'
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p MainPID --value)" = "$jc2_holder"
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p ActiveState --value)" = active
test "$(/usr/bin/timeout 3 systemctl show "$jc2_unit" -p InvocationID --value)" = "$jc2_invocation"
test "$(sed 's/^.*) //' /proc/"$jc2_holder"/stat | awk '{print $20}')" = "$jc2_start"
jc2_hz=$(getconf CLK_TCK)
jc2_uptime=$(awk '{print $1}' /proc/uptime)
awk -v up="$jc2_uptime" -v start="$jc2_start" -v hz="$jc2_hz" 'BEGIN { exit !((up-start/hz) >= 0 && (up-start/hz) < 120) }'
test "$(stat -c '%u:%g:%a' "$jc2_final")" = 0:0:444
test "$(sha256sum "$jc2_final" | cut -d ' ' -f 1)" = 'JC2_FINAL_REGISTRATION_SHA256_PLACEHOLDER'
test -p "$jc2_fifo"
test ! -L "$jc2_fifo"
test "$(stat -c '%u:%g:%a' "$jc2_fifo")" = 0:0:600
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_HOLDER_CUTOFF_PLACEHOLDER' +%s)"
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_ADMISSION_STOP_PLACEHOLDER' +%s)"
printf 'RELEASE %s\n' 'JC2_FIXED_HOLDER_TOKEN_PLACEHOLDER' > "$jc2_fifo"
# Redirection closes the sole FIFO writer. No retry, second holder, or cleanup.
