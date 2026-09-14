#!/bin/bash
# DISABLED/UNBOUND primitive, NOT an authorized complete release script.
# Full freshly authenticated host/holder/namespace/registration/cgroup/FIFO
# identity checks are still mandatory in the separately reviewed caller.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then exit 2; fi
test "$#" = 1
test "$1" = ROOT_RELEASE_EXACT_PREFLIGHT9_ONLY
test "$(id -u)" = 0
jc2_fifo='/run/jc2-closedchild-preflight9-20260912a-admission/release.fifo'
jc2_token='JC2_PREHOLDER_RELEASE_TOKEN_PLACEHOLDER'
jc2_stop='1789203720'
[[ "$jc2_stop" =~ ^[1-9][0-9]{0,10}$ ]]
test "$(date -u +%s)" -lt "$((jc2_stop - 3))"
test -p "$jc2_fifo"
test ! -L "$jc2_fifo"
# The only child is bash with a builtin printf; the FIFO open happens inside
# that timed child. Therefore a dead reader cannot hang the untimed parent
# while setting up a shell redirection. Original holder/worker caps survive.
exec /usr/bin/timeout --foreground --signal=TERM --kill-after=1s 2s \
 /bin/bash -c 'printf "RELEASE %s\n" "$2" > "$1"' jc2-fifo "$jc2_fifo" "$jc2_token"
