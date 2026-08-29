#!/bin/bash
# Root-side one-shot mint for the D43 K0 field certificate, R4.
#
#   mint_claim_r4.sh <absolute-run-directory> <authorization-json> <service-user>
#
# R4 interface change against R3 (REPAIR-1c).  R3 took the sealed parent and
# the run name as two separate arguments while the unit's ReadWritePaths=, the
# service-user dry run and the root retirement all named the run directory,
# and nothing checked that the two spellings composed to the same path.  R4
# takes the run directory itself and derives the parent and the run name from
# it, so the unit uses ONE sentinel, <ABSOLUTE_RUN_DIRECTORY>, in all four
# places and custody_selftest_r4.choreography_controls can check that
# agreement mechanically.  Every gate below is unchanged: the parent is still
# owner-, mode- and realpath-checked, and the run name must still be
# run-YYYYMMDDTHHMMSSZ.
#
# Invoked by systemd as the FIRST of the unit's two ExecStartPre commands:
#   ExecStartPre=+<packet>/mint_claim_r4.sh <run dir> <auth json> jc2k0
#   ExecStartPre=<python> -I -B <packet>/custody_selftest_r4.py \
#       --on-host-dry-run --run-path <run dir> --authorization <auth json>
#   ExecStart=... aws_worker_r4.sh ...
# The "+" prefix runs THIS command as root with the unit's sandboxing NOT
# applied, which is the only way the sealed parent can be written.  The second
# ExecStartPre carries no prefix, so systemd runs it with the unit's full
# User=/Group= and sandbox -- the same identity and the same namespace as
# ExecStart= -- and it verifies what this script just minted without taking
# the consumption lease.  The main ExecStart= then runs unprivileged as
# User=jc2k0 with the run directory as its only writable path.  ExecStartPre
# commands complete before the ExecStart mount namespace is built, so
# ReadWritePaths=<run dir> resolves.
#
# THERE IS NO EXTERNAL MINT.  A coordinator never runs this script by hand:
# the digest is spent here, once, and a hand mint would make the unit's own
# ExecStartPre die MINT_ALREADY_SPENT before the supervisor ever started.
# That was the R3 review's blocking finding, and it is why this file is only
# ever reached through the unit.
#
# What this script establishes, and nothing else:
#   1. the sealed parent is root-owned, symlink-free and not group/world
#      writable (the same law aws_supervisor_r4.py re-checks unprivileged,
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
# by aws_supervisor_r4.verify_claim_token, which is the reviewed Python; a
# mint against the wrong run name simply produces a launch that refuses
# CLAIM_ABSENT or CLAIM_BINDING without consuming anything.

set -euo pipefail
umask 077

ROUTE="D43-K0-FIELD-CERT-R4"
CLAIM_SCHEMA="d43-k0-field-certificate-claim-token-r4"
CLAIM_PREFIX=".jc2-k0-r4-claim-"
CLAIM_SUFFIX=".json"

die() { printf 'MINT_REFUSED %s %s\n' "$1" "$2" >&2; exit "$3"; }

if (( $# != 3 )); then
  printf 'usage: mint_claim_r4.sh <absolute-run-directory> <authorization-json> <service-user>\n' >&2
  exit 64
fi

RUN_ARG=${1%/}
AUTH_JSON=$2
SERVICE_USER=$3

if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  die MINT_NOT_ROOT "minting requires root; this is the privilege boundary" 77
fi
[[ "$RUN_ARG" = /* ]]   || die MINT_RUN_SHAPE "$RUN_ARG is not absolute" 64
[[ "$RUN_ARG" != *//* ]] \
  || die MINT_RUN_SHAPE "$RUN_ARG has an empty path component" 64
[[ "$RUN_ARG" != */../* && "$RUN_ARG" != */.. && "$RUN_ARG" != */./* ]] \
  || die MINT_RUN_SHAPE "$RUN_ARG is not a normalised path" 64
PARENT=$(dirname "$RUN_ARG")
RUN_NAME=$(basename "$RUN_ARG")
[[ "$PARENT" = /* && "$PARENT" != / ]] \
  || die MINT_PARENT_SHAPE "$RUN_ARG has no sealed parent" 64
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
[[ "$RUN_DIR" == "$RUN_ARG" ]] \
  || die MINT_RUN_SHAPE "$RUN_ARG does not recompose from its parent and name" 64
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
