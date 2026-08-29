#!/usr/bin/env bash
# Archive-external binding for the closed-successor R3 source packet.
# Frozen (with the archive sidecar) in LAUNCH_MANIFEST.sha256; kept outside
# the source archive to avoid hash self-reference.  R3 (O-N5): the launch
# manifest no longer lists the producer report, so its hash is fully tabled
# in the R3 report and chargeable; the report hash lives in the post-report
# REPORT_BINDING.sha256.  As in R2: requires a nonempty schema-checked
# nonce, verifies its own bytes against the charged launch manifest,
# installs a copy of itself into the job root, and builds the atomic
# content-addressed lease that every later stage and the decision record
# bind to.
set -euo pipefail

: "${SOURCE_ARCHIVE:?}"
: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${JOB_STAMP:?}"
: "${JOB_NONCE:?}"
: "${CPU_ID:?}"
: "${EXPECTED_INSTANCE_ID:?}"
: "${EXPECTED_HOSTNAME:?}"
: "${LAUNCH_MANIFEST:?}"

expected_archive_name=ggv_triple02_closed_successor_resume_r4_SOURCE.tar.gz
expected_archive_sha=a59cdeb1ece45e98912a3617f3b8980c777f4a318a852e693cd98fe38c26aa85
case_rel=cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r4_20260829
job_tag_prefix=ggv_triple02_closed_successor_resume_r4_

# Nonce and tag schema: the tag is exactly prefix + UTC stamp + "_" + nonce.
[[ "$JOB_NONCE" =~ ^[a-z0-9]{8,32}$ ]]
[[ "$JOB_STAMP" =~ ^[0-9]{8}T[0-9]{6}Z$ ]]
[[ "$JOB_TAG" == "${job_tag_prefix}${JOB_STAMP}_${JOB_NONCE}" ]]

[[ "$(basename "$SOURCE_ARCHIVE")" == "$expected_archive_name" ]]
[[ "$(sha256sum "$SOURCE_ARCHIVE" | awk '{print $1}')" == "$expected_archive_sha" ]]
[[ "$(basename "$JOB_ROOT")" == "$JOB_TAG" ]]
[[ ! -e "$JOB_ROOT" ]]

# Self-binding: this launcher's own bytes and the archive sidecar must match
# the charged launch manifest exactly.
self_sha=$(sha256sum "$0" | awk '{print $1}')
launch_manifest_sha=$(sha256sum "$LAUNCH_MANIFEST" | awk '{print $1}')
grep -Fxq "$self_sha  $case_rel/aws_launch_preflight.sh" "$LAUNCH_MANIFEST"
grep -Fxq "$expected_archive_sha  $case_rel/custody/$expected_archive_name" \
  "$LAUNCH_MANIFEST"

# Check all names and types before extraction.  This reads only the frozen
# archive metadata and rejects links, devices, duplicate names, traversal, and
# any member outside the exact jc2 packet/dependency prefixes.
python3 - "$SOURCE_ARCHIVE" <<'PY'
import pathlib
import sys
import tarfile

archive = pathlib.Path(sys.argv[1])
allowed = (
    "jc2/cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r4_20260829/",
    "jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r5_20260828/",
    "jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/",
    "jc2/cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828/",
)
seen = set()
with tarfile.open(archive, "r:gz") as handle:
    members = handle.getmembers()
    if len(members) != 23:
        raise SystemExit("SOURCE_ARCHIVE_MEMBER_COUNT")
    for member in members:
        pure = pathlib.PurePosixPath(member.name)
        if (member.name in seen or pure.is_absolute() or ".." in pure.parts
                or not member.isfile()
                or not any(member.name.startswith(prefix) for prefix in allowed)):
            raise SystemExit("SOURCE_ARCHIVE_UNSAFE_OR_UNEXPECTED_MEMBER")
        seen.add(member.name)
PY

# Atomic namespace lease: the fresh job root.
mkdir -m 0700 "$JOB_ROOT"
mkdir -m 0700 "$JOB_ROOT/source"
install -m 0400 "$SOURCE_ARCHIVE" "$JOB_ROOT/source_archive.tar.gz"
tar -xzf "$JOB_ROOT/source_archive.tar.gz" -C "$JOB_ROOT/source"
(cd "$JOB_ROOT/source/jc2" && sha256sum -c "$case_rel/SOURCE_MANIFEST.sha256") \
  > "$JOB_ROOT/source_manifest_launch_check.txt"
chmod -R a-w "$JOB_ROOT/source"
install -m 0400 "$0" "$JOB_ROOT/launch_preflight_copy.sh"
[[ "$(sha256sum "$JOB_ROOT/launch_preflight_copy.sh" | awk '{print $1}')" == "$self_sha" ]]

# Content-addressed lease binding job tag, nonce, source archive, this
# launcher, and the launch manifest.  The supervisor, worker, every stage
# runner, and the decision record verify it.
launcher_starttime=$(awk '{print $22}' "/proc/$$/stat")
python3 "$JOB_ROOT/source/jc2/$case_rel/containment_contract.py" lease-build \
  --output "$JOB_ROOT/LEASE.json" --sidecar "$JOB_ROOT/LEASE.sha256" \
  --job-tag "$JOB_TAG" --job-nonce "$JOB_NONCE" \
  --source-archive-sha256 "$expected_archive_sha" \
  --launcher-sha256 "$self_sha" \
  --launch-manifest-sha256 "$launch_manifest_sha" \
  --launcher-pid "$$" --launcher-starttime "$launcher_starttime" \
  > "$JOB_ROOT/lease_build.stdout.txt"
grep -E '^LEASE_SHA256=[0-9a-f]{64}$' "$JOB_ROOT/lease_build.stdout.txt" \
  >/dev/null

export EXPECTED_SOURCE_ARCHIVE_SHA256="$expected_archive_sha"
export JOB_NONCE
exec bash "$JOB_ROOT/source/jc2/$case_rel/aws_supervisor.sh"
