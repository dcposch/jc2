#!/bin/bash
# Root-side retirement for the D43 K0 field certificate, R3.
#
#   retire_claim_r3.sh <run-directory>
#
# Invoked by systemd as
#   ExecStopPost=+<packet>/retire_claim_r3.sh <run dir>
# so it runs as root after the unit exits, whatever the exit reason.  It seals
# the finished run directory back to the custodian: root-owned and read-only,
# so the terminal, the manifest and the artifact archive can no longer be
# altered by the service user that produced them.
#
# It creates no authorization state and removes none: the spent marker minted
# by mint_claim_r3.sh is what makes a re-run impossible, and this script never
# touches it.  Running it twice is harmless.

set -euo pipefail
umask 077

die() { printf 'RETIRE_REFUSED %s %s\n' "$1" "$2" >&2; exit "$3"; }

if (( $# != 1 )); then
  printf 'usage: retire_claim_r3.sh <run-directory>\n' >&2
  exit 64
fi

RUN_DIR=${1%/}

if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  die RETIRE_NOT_ROOT "retirement requires root" 77
fi
[[ "$RUN_DIR" = /* ]] || die RETIRE_SHAPE "$RUN_DIR is not absolute" 64
[[ -d "$RUN_DIR" && ! -L "$RUN_DIR" ]] \
  || die RETIRE_ABSENT "$RUN_DIR is not a directory" 72
[[ "$(realpath "$RUN_DIR")" == "$RUN_DIR" ]] \
  || die RETIRE_SYMLINK "$RUN_DIR resolves elsewhere" 72
[[ "$(basename "$RUN_DIR")" =~ ^run-[0-9]{8}T[0-9]{6}Z$ ]] \
  || die RETIRE_RUN_NAME "$(basename "$RUN_DIR") is not run-YYYYMMDDTHHMMSSZ" 64

chown -R 0:0 "$RUN_DIR"
chmod -R a-w "$RUN_DIR"
find "$RUN_DIR" -type d -exec chmod 0555 {} +
sync

printf 'RETIRE_OK %s\n' "$RUN_DIR"
