#!/usr/bin/env python3
"""Verify and extract the immutable upstream source and banked rank packets."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tarfile


ARCHIVES = {
    "r5_source": ("cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_rank_r5_SOURCE.tar.gz",
                  "908b73cd46821ec6a64ebd8e3aa17365616865c089dbdd45644b18baefc28bfb"),
    "p": ("cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_descent_r6_20260828/custody/ggv_lambda0_quotient_nf_descent_p_r6_20260828T161500Z_r6c.terminal.tar.gz",
          "fb778b1a7078314fa1fb941d39327cb9d99eab2ad2aa5a4c6c88f45062e26173"),
    "c8p02": ("cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_descent_r6_20260828/custody/ggv_lambda0_quotient_nf_descent_c8p02_r6_20260828T161500Z_r6e.terminal.tar.gz",
              "99cccf8c0508aa8818b00541eab0f29a1596ecbf7dcad9d9beee1a220b2419e6"),
    "q1p02": ("cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_q1p02_r5_20260828T160000Z_r6f.terminal.tar.gz",
              "992dbd0e0a81f6f37901f24c63141607c29c26d2a28195bebc37698c026b8424"),
    "q1p03": ("cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_q1p03_r5_20260828T160000Z_r6g.terminal.tar.gz",
              "9a8cf752e526d29679fa673af1359b81b66302af73998806c022a4e80c306c9c"),
    "triple02": ("cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_triple02_r5_20260828T160000Z_r6h.terminal.tar.gz",
                 "b947a2d3e81525902a93500026020c2cf9580f070767757389daadb9a6bbe3b2"),
    "triple03": ("cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_triple03_r5_20260828T160000Z_r6i.terminal.tar.gz",
                 "1d1871532a845f2ac964886035c06abcc211ae80f5c68e153850951ba242b809"),
}

LABELS = {
    "p": ("P", "P_SIZE9_RANK_WITNESS.tsv", 9),
    "c8p02": ("C8P02", "C8P02_SIZE9_RANK_WITNESS.tsv", 9),
    "q1p02": ("Q1P02", "Q1P02_RANK_WITNESS.tsv", 6),
    "q1p03": ("Q1P03", "Q1P03_RANK_WITNESS.tsv", 4),
    "triple02": ("TRIPLE02", "TRIPLE02_RANK_WITNESS.tsv", 6),
    "triple03": ("TRIPLE03", "TRIPLE03_RANK_WITNESS.tsv", 4),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe_extract(archive: tarfile.TarFile, destination: Path) -> None:
    base = destination.resolve()
    for member in archive.getmembers():
        target = (base / member.name).resolve()
        if base not in target.parents and target != base:
            raise SystemExit(f"UNSAFE_ARCHIVE_MEMBER:{member.name}")
    archive.extractall(destination)


def extract_suffix(archive_path: Path, suffix: str, output: Path) -> None:
    with tarfile.open(archive_path, "r:gz") as archive:
        matches = [m for m in archive.getmembers() if m.isfile() and m.name.endswith(suffix)]
        if len(matches) != 1:
            raise SystemExit(f"PACKET_MEMBER_CENSUS:{suffix}:{len(matches)}")
        source = archive.extractfile(matches[0])
        if source is None:
            raise SystemExit(f"PACKET_MEMBER_READ:{suffix}")
        output.write_bytes(source.read())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload-dir", required=True, type=Path)
    parser.add_argument("--work-dir", required=True, type=Path)
    args = parser.parse_args()
    payload = args.payload_dir.resolve()
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=False)
    verified = {}
    for key, (name, expected) in ARCHIVES.items():
        path = payload / name
        actual = sha256(path)
        if actual != expected:
            raise SystemExit(f"ARCHIVE_SHA_DRIFT:{key}:{actual}")
        verified[key] = {"name": name, "sha256": actual}

    source_root = work / "upstream_source"
    source_root.mkdir()
    with tarfile.open(payload / ARCHIVES["r5_source"][0], "r:gz") as archive:
        safe_extract(archive, source_root)

    packets = work / "banked"
    packets.mkdir()
    packet_meta = {}
    for component, (label, witness_name, rank) in LABELS.items():
        target = packets / component
        target.mkdir()
        archive_path = payload / ARCHIVES[component][0]
        names = {
            "residual": f"/{label}_NF_RESIDUAL_MATRIX.tsv",
            "pivots": f"/{label}_NF_RATIONAL_UNIT_PIVOTS.tsv",
            "witness": f"/{witness_name}",
            "factor": f"/{label}_BRANCH_FACTOR.txt",
            "standard_basis": f"/{label}_BRANCH_STANDARD_BASIS.txt",
        }
        files = {}
        for role, suffix in names.items():
            dest = target / suffix.rsplit("/", 1)[1]
            extract_suffix(archive_path, suffix, dest)
            files[role] = {"path": str(dest), "sha256": sha256(dest)}
        packet_meta[component] = {"label": label, "rank": rank, "files": files}

    manifest = {"archives": verified, "packets": packet_meta,
                "source_root": str(source_root / "jc2")}
    (work / "PREPARED_INPUTS.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    print("IMMUTABLE_BANKED_INPUT_PREPARATION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
