#!/usr/bin/env bash
# Archive-external binding for the closed-successor R1 source packet.
# Frozen (with the archive sidecar) in LAUNCH_MANIFEST.sha256; kept outside
# the source archive to avoid hash self-reference.
set -euo pipefail

: "${SOURCE_ARCHIVE:?}"
: "${JOB_ROOT:?}"
: "${JOB_TAG:?}"
: "${CPU_ID:?}"
: "${EXPECTED_INSTANCE_ID:?}"
: "${EXPECTED_HOSTNAME:?}"

expected_archive_name=ggv_triple02_closed_successor_resume_r1_SOURCE.tar.gz
expected_archive_sha=6a4dc35fe31cdbd1ca3eed7064b417e798072d75240e31b60d0e4b70462e6a9f
case_rel=cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r1_20260829
[[ "$(basename "$SOURCE_ARCHIVE")" == "$expected_archive_name" ]]
[[ "$(sha256sum "$SOURCE_ARCHIVE" | awk '{print $1}')" == "$expected_archive_sha" ]]
[[ "$(basename "$JOB_ROOT")" == "$JOB_TAG" ]]
[[ "$JOB_TAG" == ggv_triple02_closed_successor_resume_r1_* ]]
[[ ! -e "$JOB_ROOT" ]]

# Check all names and types before extraction.  This reads only the frozen
# archive metadata and rejects links, devices, duplicate names, traversal, and
# any member outside the exact jc2 packet/dependency prefixes.
python3 - "$SOURCE_ARCHIVE" <<'PY'
import pathlib
import sys
import tarfile

archive = pathlib.Path(sys.argv[1])
allowed = (
    "jc2/cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r1_20260829/",
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

mkdir -m 0700 "$JOB_ROOT"
mkdir -m 0700 "$JOB_ROOT/source"
install -m 0400 "$SOURCE_ARCHIVE" "$JOB_ROOT/source_archive.tar.gz"
tar -xzf "$JOB_ROOT/source_archive.tar.gz" -C "$JOB_ROOT/source"
(cd "$JOB_ROOT/source/jc2" && sha256sum -c "$case_rel/SOURCE_MANIFEST.sha256") \
  > "$JOB_ROOT/source_manifest_launch_check.txt"
chmod -R a-w "$JOB_ROOT/source"
export EXPECTED_SOURCE_ARCHIVE_SHA256="$expected_archive_sha"
exec bash "$JOB_ROOT/source/jc2/$case_rel/aws_supervisor.sh"
