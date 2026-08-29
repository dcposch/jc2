#!/usr/bin/env python3
"""Deterministic sealer for the D43 `K0` field certificate packet, R2.

Rebuilds ``PAYLOAD.sha256``, ``SOURCE_ARCHIVE.tar``, ``SOURCE_ARCHIVE.sha256``
and ``SOURCE_SEAL.sha256`` from the working tree, byte for byte.  Run with
``--verify`` to rebuild into memory and compare against what is on disk
without writing anything; that is the check a reviewer runs.

Determinism: members are the sorted repo-relative paths, PAX format, uid and
gid 0, empty uname and gname, mtime 0, mode 0444, regular files only.  Nothing
about the producer host enters the bytes.

R2 adds three external members to the sealed archive: the hashed E5/E6 bridge
that ``E_LITERAL_PIN`` parses, the Grok 4.6 theorem review the unconditional
layer's prose steps rest on, and the Fable 5 R1 source review this packet
repairs.  All three are pinned in ``execution_pins_r2.json`` and checked by
``SRC_FILE_HASHES``.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import tarfile
from pathlib import Path

PACKET_REL = "cases/d43_k0_field_certificate_r2_20260829"
EXTERNAL_MEMBERS = (
    "cases/d43_common_integral_emitter.py",
    "cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py",
    "cases/d43_full_pointbank_p105337.pkl",
    "cases/d43_full_pointbank_p105673.pkl",
    "xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md",
    "xmodel/d43-k0-splitting-primary-research-opus5-20260828.md",
    "xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md",
    "xmodel/d43-k0-field-certificate-r1-hostile-review-fable5-20260829.md",
)
GENERATED = ("PAYLOAD.sha256", "SOURCE_ARCHIVE.tar", "SOURCE_ARCHIVE.sha256",
             "SOURCE_SEAL.sha256")
ARCHIVE_EXCLUDED = ("SOURCE_ARCHIVE.tar", "SOURCE_ARCHIVE.sha256",
                    "SOURCE_SEAL.sha256")


def sha256(blob):
    return hashlib.sha256(blob).hexdigest()


def packet_files(root, exclude):
    return sorted(f.name for f in (root / PACKET_REL).iterdir()
                  if f.is_file() and f.name not in exclude)


def build_payload(root):
    lines = ["%s  %s/%s" % (sha256((root / PACKET_REL / name).read_bytes()),
                            PACKET_REL, name)
             for name in packet_files(root, GENERATED)]
    return ("\n".join(lines) + "\n").encode("ascii")


def build_archive(root):
    members = sorted(
        ["%s/%s" % (PACKET_REL, n)
         for n in packet_files(root, ARCHIVE_EXCLUDED)]
        + list(EXTERNAL_MEMBERS))
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for rel in members:
            src = root / rel
            info = tarfile.TarInfo(name=rel)
            info.size = src.stat().st_size
            info.mtime = 0
            info.mode = 0o444
            info.type = tarfile.REGTYPE
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            with src.open("rb") as fh:
                tar.addfile(info, fh)
    return members, buf.getvalue()


def build_archive_seal(root, members, archive_blob):
    lines = ["%s  %s/SOURCE_ARCHIVE.tar" % (sha256(archive_blob), PACKET_REL)]
    lines += ["%s  %s" % (sha256((root / rel).read_bytes()), rel)
              for rel in members]
    return ("\n".join(lines) + "\n").encode("ascii")


def build_source_seal(root):
    lines = ["%s  %s/%s" % (sha256((root / PACKET_REL / name).read_bytes()),
                            PACKET_REL, name)
             for name in packet_files(root, ("SOURCE_SEAL.sha256",))]
    return ("\n".join(lines) + "\n").encode("ascii")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True)
    ap.add_argument("--verify", action="store_true",
                    help="compare against disk, write nothing")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    pkt = root / PACKET_REL

    payload = build_payload(root)
    if not args.verify:
        (pkt / "PAYLOAD.sha256").write_bytes(payload)
    members, archive = build_archive(root)
    if not args.verify:
        tar_path = pkt / "SOURCE_ARCHIVE.tar"
        if tar_path.exists():           # the previous seal left it 0444
            tar_path.chmod(0o644)
        tar_path.write_bytes(archive)
        tar_path.chmod(0o444)
    seal = build_archive_seal(root, members, archive)
    if not args.verify:
        (pkt / "SOURCE_ARCHIVE.sha256").write_bytes(seal)
    source_seal = build_source_seal(root)
    if not args.verify:
        (pkt / "SOURCE_SEAL.sha256").write_bytes(source_seal)

    report = {"packet": PACKET_REL, "archive_members": len(members),
              "external_members": len(EXTERNAL_MEMBERS),
              "archive_sha256": sha256(archive),
              "payload_sha256": sha256(payload),
              "archive_seal_sha256": sha256(seal),
              "source_seal_sha256": sha256(source_seal)}
    if args.verify:
        report["matches_disk"] = {
            "PAYLOAD.sha256":
                (pkt / "PAYLOAD.sha256").read_bytes() == payload,
            "SOURCE_ARCHIVE.tar":
                (pkt / "SOURCE_ARCHIVE.tar").read_bytes() == archive,
            "SOURCE_ARCHIVE.sha256":
                (pkt / "SOURCE_ARCHIVE.sha256").read_bytes() == seal,
            "SOURCE_SEAL.sha256":
                (pkt / "SOURCE_SEAL.sha256").read_bytes() == source_seal,
        }
        report["ok"] = all(report["matches_disk"].values())
    else:
        report["ok"] = True
    sys.stdout.write(json.dumps(report, sort_keys=True, indent=1) + "\n")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
