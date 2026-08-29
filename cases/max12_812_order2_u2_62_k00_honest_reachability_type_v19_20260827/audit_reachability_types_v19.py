#!/usr/bin/env python3
"""Audit whether V18 duals compose with an honest Lambda<=19 source map."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


EXPECTED = {
    "result": "cc0f8443ecab0f03f992c76055a4c8db482a4dfc149822c424e29d5c73f93a11",
    "emitter": "d1b7b46afa53b6c1f7410ae7fcd609e0d19c55d937698f0b9b20b997d231af7a",
    "oneparam": "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    "oneparam_review": "1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de",
}
DIRECTIONS = {
    "K10": (4, "0d000075c664c55168d10d741f5d5c84aa780cda6b6470ce2d59f7969a742e1f", "9a8d078ef21f525693df4a10f47db3b7c64149cd9c6589321a9a98fadb6618b9"),
    "K6": (3, "f4638ff5a04b7cf02fc337978038f5946ec5312cb4b9a3a1ea32986b05609548", "d2b606cc6d41b2c5ee82ef846d5fe1d28b726997f64c1adefbe2f33b879fc5b7"),
    "K2": (2, "805750df2e740b34d66b74f85242badf0140df16a888c456e4b8b1199aaf7fd2", "6411c8497397ac76eefaecea6e17f714f52eddf1f88cd697884d18dd0af1f1ff"),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V19 type audit refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V19 type audit refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def parse_solution(path: Path, cutoff: int) -> tuple[dict[str, str], dict[int, int]]:
    metadata: dict[str, str] = {}
    dual: dict[int, int] = {}
    for line in path.read_text().splitlines():
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "y":
            if len(parts) != 3 or int(parts[1]) in dual:
                fail(("malformed dual", str(path), line))
            dual[int(parts[1])] = int(parts[2]) % 65521
        elif parts[0] == "x":
            fail(("incompatible endpoint contains lift", str(path)))
        else:
            if len(parts) != 2 or parts[0] in metadata:
                fail(("malformed metadata", str(path), line))
            metadata[parts[0]] = parts[1]
    if metadata.get("field") != "65521" or metadata.get("consistent") != "0" or int(metadata.get("cutoff", -1)) != cutoff:
        fail(("dual endpoint sentinel", str(path), metadata))
    if not dual or int(metadata.get("certificate_dot", "0")) % 65521 == 0:
        fail(("empty/nonseparating dual", str(path)))
    return metadata, dual


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    parser.add_argument("emitter", type=Path)
    parser.add_argument("oneparam", type=Path)
    parser.add_argument("oneparam_review", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--entry", action="append", nargs=3,
                        metavar=("DIRECTION", "SOLUTION", "ROW_MAP"), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for label, path in (("result", args.result), ("emitter", args.emitter),
                        ("oneparam", args.oneparam), ("oneparam_review", args.oneparam_review)):
        if digest(path) != EXPECTED[label]:
            fail(("charged hash mismatch", label, digest(path), EXPECTED[label]))
    result = json.loads(args.result.read_text())
    if result.get("status") != "PASS-K00-FILTERED-LOAD-V18-ENDPOINT" or result.get("field") != "65521":
        fail("V18 modular endpoint sentinel")
    if "NO_HONEST_SOURCE_REACHABILITY" not in result.get("firewall", ""):
        fail("V18 source-reachability firewall missing")
    supplied = {label: (Path(solution), Path(rows)) for label, solution, rows in args.entry}
    if set(supplied) != set(DIRECTIONS):
        fail(("direction coverage", sorted(supplied)))
    outcomes: dict[str, object] = {}
    for label, (cutoff, solution_sha, rows_sha) in DIRECTIONS.items():
        solution, row_map = supplied[label]
        if digest(solution) != solution_sha or digest(row_map) != rows_sha:
            fail(("dual/row-map hash mismatch", label, digest(solution), digest(row_map)))
        metadata, dual = parse_solution(solution, cutoff)
        rows = json.loads(row_map.read_text())
        if len(rows) != int(metadata["rows"]) or any(len(monomial) != 6 for monomial in rows):
            fail(("ambient row-map type", label))
        if any(index < 0 or index >= len(rows) or dual[index] == 0 for index in dual):
            fail(("dual support index", label))
        degrees = Counter(sum(rows[index]) for index in dual)
        outcomes[label] = {
            "classification": "NOT_TYPED_COMPOSABLE",
            "cutoff": cutoff,
            "dual_domain": f"dual of F_65521[d0,...,d5]_<=${cutoff}".replace("$", ""),
            "dual_entries": len(dual),
            "dual_support_degree_histogram": {str(key): degrees[key] for key in sorted(degrees)},
            "target_pairing_mod_65521": int(metadata["certificate_dot"]) % 65521,
            "missing_map": "common mixed six-row Lambda<=19 source/target/Jdet jet matrix",
            "reason": "packet contains only six-variable coefficient row maps and direction-specific quotient covectors",
        }
    output = {
        "status": "PASS-K00-V19-REACHABILITY-TYPE-AUDIT",
        "registered_aws_lane": tag,
        "field": "65521",
        "outcomes": outcomes,
        "common_mixed_map_present": False,
        "successor": "COMPILE_COMMON_SIX_ROW_LAMBDA19_KURANISHI_MAP_THEN_COMPOSE_DUALS",
        "scope": "TYPE_AND_INTERFACE_AUDIT_ONLY",
        "firewall": "NO_ZERO_OR_NONZERO_REACHABILITY_VERDICT_NO_ARC_EXCLUSION_NO_CLOSURE_NO_JC2",
    }
    args.output.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n")
    print("K00_V19_TYPE_AUDIT=PASS")
    for label in DIRECTIONS:
        print(f"K00_V19_{label}=NOT_TYPED_COMPOSABLE")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
