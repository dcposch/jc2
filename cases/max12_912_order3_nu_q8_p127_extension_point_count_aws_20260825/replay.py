#!/usr/bin/env python3
"""Portable fail-closed audit of the frozen two-host F_(127^2) count."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re


CASE = Path(__file__).resolve().parent
P = 127
Q = P * P
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
SOURCE_HASHES = {
    "count_shard.py": "ec1fafa373f2f46c6f6899bfb424dc2510323f8930ac1d52408e32d35efaec12",
    "run_shard.sh": "cd1bed208596eddd17ad56a78916977733f10b80c5725ee8b3843f56f9d02c2f",
    "dispatch.sh": "6d863b475710130f98f3535f9d28e5163afb930429ce114169ae38c5654072eb",
    "aggregate.py": "b068081d154e5839a6197b48e8f88db552c503bb1f4af058b5a8ed892c451c43",
    "run_aggregate.sh": "83819ad66a4aefe264b8e57d4ed7b53e9649cb454fbfd4fad7b04588e95c88e2",
    "direct_control.py": "933ca69de6fbe4ced91c63558ba6570790fd2e4ebead90d96b70b06471bdba65",
    "run_direct_control.sh": "1127d6e1be832c3e14c206dc2985f773bc9eb868201808d5c283beba4e8fa357",
}
AGGREGATE_HASHES = {
    "aws_box02_v2_aggregate/result.json": "031da7561db2eaffad4ec12310b79ded986964accd35b65e356da4b3b7ac7614",
    "aws_r6d_v2_aggregate/result.json": "528de912e52df836de5d65219cbb8b29fcdd513817bd88b86777ce7bc01f66bd",
}
TAR_HASHES = {
    "q8_p127_fq2_points_box02_v1_harvest.tgz": "e9b7157464f2b1ca706ad52df46fcb7666475fb9c2fa02b572728e2faf80bbfc",
    "q8_p127_fq2_points_r6d_v1_harvest.tgz": "455f44fc514903427e0a40870cb8cfcad30bd0f2060489728fde1e70a8bef7da",
}
DIRECT_HASH = "9cc104c5d826c607c8e134cbaaf0a187220a0b42fdcc9e54863bf721d1bc24b3"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_hashes(expected: dict[str, str]) -> None:
    for relative, wanted in expected.items():
        got = digest(CASE / relative)
        if got != wanted:
            raise RuntimeError(("hash", relative, got, wanted))


def audit_partition(root: Path, prefix: str, shard_count: int) -> dict:
    cursor = 0
    per_w: list[list[int]] = []
    result_hashes = []
    for index in range(shard_count):
        shard = root / f"{prefix}_i{index:02d}"
        meta = (shard / "run.meta").read_text()
        if not re.search(r"^rc=0$", meta, re.MULTILINE):
            raise RuntimeError(("shard rc", shard))
        for source, wanted in (
            ("count_shard.py", SOURCE_HASHES["count_shard.py"]),
            ("run_shard.sh", SOURCE_HASHES["run_shard.sh"]),
        ):
            if wanted not in meta or source not in meta:
                raise RuntimeError(("source pin", shard, source))
        if CANDIDATE_SHA256 not in meta:
            raise RuntimeError(("candidate pin", shard))
        if (shard / "runner.stderr").read_bytes() or (shard / "runner.stdout").read_bytes():
            raise RuntimeError(("runner output", shard))
        record = json.loads((shard / "result.json").read_text())
        if (
            record.get("status") != "PASS"
            or record.get("prime") != P
            or record.get("extension_degree") != 2
            or record.get("field_order") != Q
            or record.get("candidate_sha256") != CANDIDATE_SHA256
            or record.get("field_modulus") != "x^2 + 126*x + 3"
            or record.get("start") != cursor
            or record.get("stop") - record.get("start") != record.get("w_count")
        ):
            raise RuntimeError(("shard endpoint", shard))
        rows = record.get("per_w")
        if [row[0] for row in rows] != list(range(record["start"], record["stop"])):
            raise RuntimeError(("shard interval", shard))
        sums = [sum(row[column] for row in rows) for column in (1, 2, 3)]
        expected_sums = [
            record["rational_affine_point_count"],
            record["smooth_rational_affine_point_count"],
            record["singular_rational_affine_point_count"],
        ]
        if sums != expected_sums or sums[0] != sums[1] + sums[2]:
            raise RuntimeError(("shard sums", shard, sums, expected_sums))
        per_w.extend(rows)
        cursor = record["stop"]
        result_hashes.append(digest(shard / "result.json"))
    if cursor != Q or len(per_w) != Q:
        raise RuntimeError(("partition", cursor, len(per_w)))
    counts = [sum(row[column] for row in per_w) for column in (1, 2, 3)]
    if counts != [16174, 16168, 6]:
        raise RuntimeError(("partition counts", counts))
    return {
        "shard_count": shard_count,
        "w_count": len(per_w),
        "counts_total_smooth_singular": counts,
        "ordered_result_hashes_sha256": sha256(
            ("\n".join(result_hashes) + "\n").encode()
        ).hexdigest(),
    }


def main() -> None:
    require_hashes(SOURCE_HASHES)
    require_hashes(AGGREGATE_HASHES)
    require_hashes(TAR_HASHES)
    box = audit_partition(
        CASE / "harvest_box02", "q8_p127_fq2_points_box02_v1", 16
    )
    r6d = audit_partition(CASE / "harvest_r6d", "q8_p127_fq2_points_r6d_v1", 8)
    for relative in AGGREGATE_HASHES:
        directory = CASE / Path(relative).parent
        meta = (directory / "run.meta").read_text()
        if not re.search(r"^rc=0$", meta, re.MULTILINE):
            raise RuntimeError(("aggregate rc", directory))
        aggregate = json.loads((directory / "result.json").read_text())
        if (
            aggregate.get("status") != "PASS"
            or aggregate.get("rational_affine_point_count") != 16174
            or aggregate.get("smooth_rational_affine_point_count") != 16168
            or aggregate.get("singular_rational_affine_point_count") != 6
            or aggregate.get("p1_rational_point_count") != 16130
            or aggregate.get("genus_positive_if_geometrically_integral") is not True
        ):
            raise RuntimeError(("aggregate endpoint", directory))
    direct_path = CASE / "aws_r6d_direct_control_v1/result.json"
    if digest(direct_path) != DIRECT_HASH:
        raise RuntimeError("direct-control hash")
    direct = json.loads(direct_path.read_text())
    if direct.get("status") != "PASS" or [
        row["w_index"] for row in direct.get("records", [])
    ] != [0, 39, 71, 128]:
        raise RuntimeError("direct-control endpoint")
    for row in direct["records"]:
        if row["direct_counts_total_smooth_singular"] != row[
            "gcd_counts_total_smooth_singular"
        ]:
            raise RuntimeError(("direct-control mismatch", row["w_index"]))
    output = {
        "status": "PASS",
        "candidate_sha256": CANDIDATE_SHA256,
        "box02": box,
        "r6d": r6d,
        "independent_counts_agree": box["counts_total_smooth_singular"]
        == r6d["counts_total_smooth_singular"],
        "smooth_count": 16168,
        "p1_count": 16130,
        "strict_excess": 38,
        "positive_genus_given_reviewed_geometric_integrality": True,
        "scope": "standalone pinned H over F_127 only",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
