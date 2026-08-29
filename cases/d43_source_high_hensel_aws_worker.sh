#!/usr/bin/env bash
set -euo pipefail

# Route-specific payload shim.  The Python supervisor creates and hashes the
# authorization envelope, starts this file in a fresh process group, and
# monitors that whole group.  `exec` is mandatory: the payload group contains
# one process and cannot hide an unmonitored shell child.

if [[ "${OSTYPE:-}" != linux* ]]; then
  echo "D43 high-Hensel worker refuses non-Linux host" >&2
  exit 125
fi

if [[ ! -r /sys/class/dmi/id/sys_vendor ]]; then
  echo "D43 high-Hensel worker cannot read DMI vendor" >&2
  exit 125
fi
IFS= read -r D43_VENDOR < /sys/class/dmi/id/sys_vendor
if [[ "$D43_VENDOR" != "Amazon EC2" ]]; then
  echo "D43 high-Hensel worker refuses non-EC2 host" >&2
  exit 125
fi

if [[ -z "${JC2_D43_HENSEL_AWS_AUTH:-}" || \
      -z "${JC2_D43_HENSEL_AWS_AUTH_SHA256:-}" ]]; then
  echo "D43 high-Hensel worker lacks authenticated lane marker" >&2
  exit 125
fi

if (( $# != 8 )); then
  echo "usage: $0 ROOT PYTHON RUNNER TARGET STATE REPORT CERTIFICATE P2_REFERENCE" >&2
  exit 125
fi

D43_ROOT=$1
D43_PYTHON=$2
D43_RUNNER=$3
D43_TARGET=$4
D43_STATE=$5
D43_REPORT=$6
D43_CERTIFICATE=$7
D43_P2_REFERENCE=$8

if [[ "$D43_TARGET" != "16" && "$D43_TARGET" != "64" ]]; then
  echo "D43 high-Hensel worker permits target 16 or 64 only" >&2
  exit 125
fi

cd "$D43_ROOT"
exec "$D43_PYTHON" -I "$D43_RUNNER" \
  --target-exponent "$D43_TARGET" \
  --state "$D43_STATE" \
  --report "$D43_REPORT" \
  --certificate "$D43_CERTIFICATE" \
  --p2-reference "$D43_P2_REFERENCE"
