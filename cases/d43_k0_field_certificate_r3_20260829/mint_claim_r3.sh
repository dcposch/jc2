#!/bin/bash
# Root-side one-shot mint for the D43 K0 field certificate, R3.
#
#   mint_claim_r3.sh <sealed-parent> <run-name> <authorization-json> <service-user>
#
# Invoked by systemd as
#   ExecStartPre=+<packet>/mint_claim_r3.sh ...
# The "+" prefix runs the command as root with the unit's sandboxing NOT
# applied, which is the only way the sealed parent can be written; the main
# ExecStart= then runs unprivileged as User=jc2k0 with the run directory as
# its only writable path.  ExecStartPre commands complete before the ExecStart
# mount namespace is built, so ReadWritePaths=<run dir> resolves.
#
# What this script establishes, and nothing else:
#   1. the sealed parent is root-owned, symlink-free and not group/world
#      writable (the same law aws_supervisor_r3.py re-checks unprivileged,
#      plus a realpath test the unprivileged side cannot safely make);
#   2. minting for a given authorization digest happens at most once, ever:
#      <sealed parent>/spent/<digest>.spent is created with O_EXCL BEFORE
#      anything else, so a crash halfway through can never be re-minted and a
#      unit restart dies here instead of re-running the job;
#   3. the per-run directory exists, owned by the service user, mode 0700;
#   4. the claim token inside it is root-owned 0444.  The service user can
#      neither create nor modify it; it can only delete it, which denies only
#      itself (the supervisor then refuses CLAIM_ABSENT).
#
# This script deliberately does not parse the authorization record.  The
# record-to-claim binding (route, run_path, service user, digest) is enforced
# by aws_supervisor_r3.verify_claim_token, which is the reviewed Python; a
# mint against the wrong run name simply produces a launch that refuses
# CLAIM_ABSENT or CLAIM_BINDING without consuming anything.

set -euo pipefail
umask 077

ROUTE="D43-K0-FIELD-CERT-R3"
CLAIM_SCHEMA="d43-k0-field-certificate-claim-token-r3"
CLAIM_PREFIX=".jc2-k0-r3-claim-"
CLAIM_SUFFIX=".json"

die() { printf 'MINT_REFUSED %s %s\n' "$1" "$2" >&2; exit "$3"; }

if (( $# != 4 )); then
  printf 'usage: mint_claim_r3.sh <sealed-parent> <run-name> <authorization-json> <service-user>\n' >&2
  exit 64
fi

PARENT=${1%/}
RUN_NAME=$2
AUTH_JSON=$3
SERVICE_USER=$4

if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  die MINT_NOT_ROOT "minting requires root; this is the privilege boundary" 77
fi
[[ "$PARENT" = /* ]]    || die MINT_PARENT_SHAPE "$PARENT is not absolute" 64
[[ "$AUTH_JSON" = /* ]] || die MINT_AUTH_SHAPE "$AUTH_JSON is not absolute" 64
[[ "$RUN_NAME" =~ ^run-[0-9]{8}T[0-9]{6}Z$ ]] \
  || die MINT_RUN_NAME "$RUN_NAME is not run-YYYYMMDDTHHMMSSZ" 64
[[ "$SERVICE_USER" =~ ^[a-z][a-z0-9_-]{0,30}$ ]] \
  || die MINT_SERVICE_USER "$SERVICE_USER is not a plain user name" 64
id -u "$SERVICE_USER" >/dev/null 2>&1 \
  || die MINT_SERVICE_USER "$SERVICE_USER has no passwd entry" 72

# portable stat and sha256, so the same script can be audited off-host
st() { stat -c '%u %g %a' "$1" 2>/dev/null || stat -f '%u %g %Lp' "$1"; }
sha() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | cut -d' ' -f1
  else
    shasum -a 256 "$1" | cut -d' ' -f1
  fi
}
# group- or world-writable, read from the octal mode arithmetically so that a
# four-digit (setuid/sticky) mode cannot slip past a character-class test
writable_by_others() { (( (8#$1 & 8#22) != 0 )); }

[[ -d "$PARENT" ]] || die MINT_PARENT_ABSENT "$PARENT is not a directory" 72
[[ "$(realpath "$PARENT")" == "$PARENT" ]] \
  || die MINT_PARENT_SYMLINK "$PARENT resolves elsewhere" 72
read -r P_UID P_GID P_MODE <<<"$(st "$PARENT")" \
  || die MINT_PARENT_STAT "cannot stat $PARENT" 72
[[ "$P_UID" == 0 ]] || die MINT_PARENT_OWNER "$PARENT is owned by uid $P_UID" 72
! writable_by_others "$P_MODE" \
  || die MINT_PARENT_MODE "$PARENT is mode $P_MODE (group/world writable)" 72

[[ -f "$AUTH_JSON" && ! -L "$AUTH_JSON" ]] \
  || die MINT_AUTH_SHAPE "$AUTH_JSON is not a regular file" 72
read -r A_UID A_GID A_MODE <<<"$(st "$AUTH_JSON")" \
  || die MINT_AUTH_STAT "cannot stat $AUTH_JSON" 72
[[ "$A_UID" == 0 ]] || die MINT_AUTH_OWNER "$AUTH_JSON is owned by uid $A_UID" 72
! writable_by_others "$A_MODE" \
  || die MINT_AUTH_MODE "$AUTH_JSON is mode $A_MODE (group/world writable)" 72

AUTH_SHA=$(sha "$AUTH_JSON")
[[ "$AUTH_SHA" =~ ^[0-9a-f]{64}$ ]] || die MINT_AUTH_DIGEST "$AUTH_SHA" 72

RUN_DIR="$PARENT/$RUN_NAME"
SPENT_DIR="$PARENT/spent"
SPENT="$SPENT_DIR/$AUTH_SHA.spent"
TOKEN="$RUN_DIR/$CLAIM_PREFIX$AUTH_SHA$CLAIM_SUFFIX"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# ---- step 1: the one-shot gate, before anything else exists --------------
mkdir -p -m 0700 "$SPENT_DIR"
chown 0:0 "$SPENT_DIR"
chmod 0700 "$SPENT_DIR"
set -C                                   # noclobber makes > an O_EXCL create
{ printf '{"authorization_sha256":"%s","minted_utc":"%s","route":"%s","run_path":"%s"}\n' \
    "$AUTH_SHA" "$NOW" "$ROUTE" "$RUN_DIR" > "$SPENT"; } 2>/dev/null \
  || die MINT_ALREADY_SPENT \
       "$SPENT exists: this authorization has been minted before; issue a new coordinator record" 75
chmod 0444 "$SPENT"

# Deliberate: the digest is spent before the run directory is touched, so a
# mint against a name that already exists retires the authorization without
# producing a launchable directory.  That costs a coordinator record and is the
# fail-closed direction; the alternative would let a second mint attempt
# succeed after a partial first one.
# ---- step 2: the run directory, root-owned while it is being built -------
mkdir -m 0700 "$RUN_DIR" \
  || die MINT_RUN_DIR_EXISTS "$RUN_DIR already exists" 73
chown 0:0 "$RUN_DIR"

# ---- step 3: the root-owned, no-replace claim token ----------------------
printf '{"authorization_sha256":"%s","minted_utc":"%s","route":"%s","run_path":"%s","schema":"%s","service_user":"%s"}\n' \
  "$AUTH_SHA" "$NOW" "$ROUTE" "$RUN_DIR" "$CLAIM_SCHEMA" "$SERVICE_USER" > "$TOKEN"
set +C
chown 0:0 "$TOKEN"
chmod 0444 "$TOKEN"

# ---- step 4: hand the directory, and only the directory, to the service --
chown "$SERVICE_USER:$SERVICE_USER" "$RUN_DIR"
chmod 0700 "$RUN_DIR"
sync

printf 'MINT_OK %s %s %s\n' "$AUTH_SHA" "$RUN_DIR" "$(sha "$TOKEN")"
