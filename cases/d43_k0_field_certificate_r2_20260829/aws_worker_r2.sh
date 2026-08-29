#!/bin/bash
set -euo pipefail

# Invoked by the externally bound absolute Bash binary as
#   <bash> --noprofile --norc <sealed-path> <python> <supervisor> <authorization>
# from a nondelegated systemd/cgroup-v2 service.  The unit constructs the
# environment from an allowlist; no caller shell environment is inherited.

if (( $# != 3 )); then
  exit 125
fi

D43_PYTHON=$1
D43_SUPERVISOR=$2
D43_AUTHORIZATION=$3

[[ "$D43_PYTHON" = /* && "$D43_SUPERVISOR" = /* && "$D43_AUTHORIZATION" = /* ]] \
  || exit 125

# Bash exports SHLVL and synthesizes PWD.  The unit binds SHLVL=0 and cwd=/;
# remove the two shell-generated variables so the Python process receives the
# exact preregistered allowlist.
unset PWD _
export SHLVL=0

# -I -B is kept from R1 and is now a checked custody property: runner_r2.py
# refuses to run outside isolated mode, and loads its sealed sibling modules
# by manifest-verified path instead of by sys.path search.
exec "$D43_PYTHON" -I -B "$D43_SUPERVISOR" \
  --authorization "$D43_AUTHORIZATION" \
  --i-understand-this-is-aws-only
