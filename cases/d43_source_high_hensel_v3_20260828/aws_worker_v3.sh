#!/bin/bash
set -euo pipefail

# This file is invoked by the externally bound absolute Bash binary as
# `<bash> --noprofile --norc <sealed-path> ...`.
# from a nondelegated systemd/cgroup-v2 service.  The supervisor constructs the
# environment from an allowlist; no caller shell environment is inherited.

if (( $# != 10 )); then
  exit 125
fi

D43_PYTHON=$1
D43_RUNNER=$2
D43_EXECUTION_ROOT=$3
D43_TARGET=$4
D43_STATE=$5
D43_REPORT=$6
D43_CERTIFICATE=$7
D43_P2_REFERENCE=$8
D43_D21_PRIVATE=$9
D43_CORE23=${10}

case "$D43_TARGET" in
  16|64) ;;
  *) exit 125 ;;
esac

[[ "$D43_PYTHON" = /* && "$D43_RUNNER" = /* &&
   "$D43_EXECUTION_ROOT" = /* && "$D43_STATE" = /* &&
   "$D43_REPORT" = /* && "$D43_CERTIFICATE" = /* &&
   "$D43_P2_REFERENCE" = /* && "$D43_D21_PRIVATE" = /* &&
   "$D43_CORE23" = /* ]] || exit 125

# Bash exports SHLVL and ordinarily synthesizes PWD.  The supervisor binds
# SHLVL=0 and cwd=/; remove the two unneeded shell-generated variables so the
# Python process receives the exact preregistered allowlist.
unset PWD _
export SHLVL=0

exec "$D43_PYTHON" -I -B "$D43_RUNNER" \
  --target-exponent "$D43_TARGET" \
  --state "$D43_STATE" \
  --report "$D43_REPORT" \
  --certificate "$D43_CERTIFICATE" \
  --p2-reference "$D43_P2_REFERENCE" \
  --d21-private "$D43_D21_PRIVATE" \
  --core23 "$D43_CORE23" \
  --execution-root "$D43_EXECUTION_ROOT"
